# card: C1-3
"""Clone ratchet: copied logic in the C1-3 roots (tests out, F256), against forge/baselines/clone.json.

clone_ratchet.py [--root D] [--base R] [--update [--record ID]] [--basis] [--list]
Function clones: a body of at least 5 statements equal after normalisation. Fragment clones: windows of 6 consecutive
statements (no def, class or import in a window), equal windows that travel together merged into one maximal run, copies that
overlap thinned. A group wholly inside a larger function group is dropped. Normalisation: local names numbered by first
appearance, a literal keeps its type only; operators, call shapes, attribute and global names stay. ONE scope over all roots, so
a copy between roots counts. Finding: `new: <fp> <kind> <s> statements, <n> copies: <path>:<a>-<b>, ...`, <fp> the first 16 hex
of sha256 over `<kind>\\x1f<normalised code>`. A row is {id, members, reason}: stale with all members parsed prints `diverged`
(B20 (c)); a live group with fewer copies than the members is `shrunk:`, green. Scope, source reading, the driver and the list
rules are ratchets.py's.
"""
import ast
import hashlib
import re
import sys

import ratchets

SPEC = ratchets.Spec("forge/baselines/clone.json", scope=ratchets.globs(ratchets.ROOTS))
MIN, WINDOW = 5, 6
SKIP = frozenset({"ctx", "type_comment", "kind", "type_params", "annotation", "returns"})
BINDS = frozenset({("FunctionDef", "name"), ("AsyncFunctionDef", "name"), ("ClassDef", "name"), ("ExceptHandler", "name"),
                   ("alias", "asname"), ("MatchAs", "name"), ("MatchStar", "name"), ("MatchMapping", "rest")})
MARK = re.compile("\x00([^\x00]*)\x00")


# ---- normalisation

def strip_doc(body):
    """The body without its docstring (a first statement that is a bare string)."""
    first = body[0] if body else None
    if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant) and isinstance(first.value.value, str):
        return body[1:]
    return body


def is_import(stmt):
    """An import, or the `sys.path.insert/append(...)` bootstrap line: statements that say nothing about shared logic."""
    if isinstance(stmt, (ast.Import, ast.ImportFrom)):
        return True
    fn = stmt.value.func if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call) else None
    target = fn.value if isinstance(fn, ast.Attribute) and fn.attr in ("insert", "append") else None
    return isinstance(target, ast.Attribute) and target.attr == "path" and isinstance(target.value, ast.Name) \
        and target.value.id == "sys"


def blocks(stmt):
    """The statement lists directly inside a statement."""
    if isinstance(stmt, ratchets.DEFS):
        return [strip_doc(stmt.body)]
    out = []
    for _, value in ast.iter_fields(stmt):
        if isinstance(value, list) and value and all(isinstance(v, ast.stmt) for v in value):
            out.append(value)
        elif isinstance(value, list):
            out += [v.body for v in value if isinstance(v, (ast.ExceptHandler, ast.match_case))]
    return out


def count(stmts):
    """Statements in a list, nested ones included."""
    return len(stmts) + sum(count(b) for s in stmts for b in blocks(s))


def bound_name(n, fn):
    """The name a node binds that is no Name or arg: a nested def or class, except-as, a match capture."""
    if isinstance(n, ratchets.DEFS) and n is not fn:
        return [n.name]
    if isinstance(n, (ast.ExceptHandler, ast.MatchAs, ast.MatchStar)):
        return [n.name] if n.name else []
    return [n.rest] if isinstance(n, ast.MatchMapping) and n.rest else []


def local_names(fn):
    """Names bound inside a function (parameters, targets, with/for/walrus names, ...) minus global and nonlocal ones.
    Imports are not local: `json` and `yaml` stay different."""
    names, declared = set(), set()
    for n in ast.walk(fn):
        if isinstance(n, ast.Name) and isinstance(n.ctx, (ast.Store, ast.Del)):
            names.add(n.id)
        elif isinstance(n, ast.arg):
            names.add(n.arg)
        elif isinstance(n, (ast.Global, ast.Nonlocal)):
            declared.update(n.names)
        else:
            names.update(bound_name(n, fn))
    return frozenset(names - declared)


def name_of(identifier, locs):
    return "\x00%s\x00" % identifier if identifier in locs else "N:" + identifier


def const(v):
    return repr(v) if v is None or v is True or v is False or v is Ellipsis else "K:" + type(v).__name__


def bound(value, locs):
    return name_of(value, locs) if isinstance(value, str) else "None"


class T(str):
    """Literal text in ser's work list; a plain str there is a node's field value, written with repr."""


def fields_of(node, locs):
    """The work items of one node: its pieces in order, a nested node or list left unexpanded (F5: ser never recurses)."""
    cls = type(node).__name__
    items = [T("(" + cls)]
    for f, v in ast.iter_fields(node):
        if f in SKIP:
            continue
        v = strip_doc(v) if f == "body" and isinstance(node, ratchets.DEFS) else v
        items += [T(" %s=" % f), T(bound(v, locs)) if (cls, f) in BINDS else v]
    return items + [T(")")]


def ser(node, locs):
    """The canonical text of a node (see the module text); a local name is a mark that renum() numbers later. An explicit stack:
    a chain of 1500 terms parses and must be measured, not reported as unparsable (t-1996 F5)."""
    out, todo = [], [node]
    while todo:
        n = todo.pop()
        if isinstance(n, T):
            out.append(n)
        elif isinstance(n, list):
            out.append("[")
            todo.append(T("]"))
            todo.extend(reversed([x for v in n for x in (v, T(","))][:-1]))
        elif not isinstance(n, ast.AST):
            out.append(repr(n))
        elif isinstance(n, ast.Name):
            out.append(name_of(n.id, locs))
        elif isinstance(n, ast.Constant):
            out.append(const(n.value))
        elif isinstance(n, ast.arg):
            out.append("arg " + name_of(n.arg, locs))
        else:
            todo.extend(reversed(fields_of(n, locs)))
    return "".join(out)


def renum(text):
    """Local-name marks to numbers by order of first appearance in this text: `a + b` equals `c + d`, not `a + a`."""
    seen = {}
    return MARK.sub(lambda m: "\x01%d" % seen.setdefault(m.group(1), len(seen)), text)


def function_text(fn, locs):
    kind = "async" if isinstance(fn, ast.AsyncFunctionDef) else "def"
    return renum(kind + ser(fn.args, locs) + ser(strip_doc(fn.body), locs))


# ---- one file

def windows(stmts, locs):
    """(starts, ends, counts, window texts) of one statement list, or None when no window can hold."""
    if len(stmts) < WINDOW:
        return None
    brk = [isinstance(s, ratchets.DEFS) or is_import(s) for s in stmts]
    strs = [None if b else ser(s, locs) for s, b in zip(stmts, brk)]
    texts = [None if any(brk[p:p + WINDOW]) else renum("\x1f".join(strs[p:p + WINDOW])) for p in range(len(stmts) - WINDOW + 1)]
    if all(t is None for t in texts):
        return None
    return ([s.lineno for s in stmts], [s.end_lineno for s in stmts], [0 if b else count([s]) for s, b in zip(stmts, brk)], texts)


def inner(rel, s, locs, funcs):
    """The statement lists inside s as (stmts, locals); a function of enough statements is recorded."""
    if isinstance(s, ratchets.FUNCS):
        mine, body = local_names(s), strip_doc(s.body)
        if count(body) >= MIN:
            funcs.append((rel, s.lineno, s.end_lineno, count(body), function_text(s, mine)))
        return [(body, mine)]
    if isinstance(s, ast.ClassDef):
        return [(strip_doc(s.body), locs)]
    return [(b, locs) for b in blocks(s)]


def collect(rel, tree):
    funcs, lists, todo = [], [], [(strip_doc(tree.body), frozenset())]
    while todo:
        stmts, locs = todo.pop()
        w = windows(stmts, locs)
        if w:
            lists.append((rel,) + w)
        for s in stmts:
            todo.extend(inner(rel, s, locs, funcs))
    return rel, funcs, lists


# ---- groups

def group(kind, size, locs, key):
    digest = hashlib.sha256(("%s\x1f%s" % (kind, key)).encode("utf-8", "backslashreplace")).hexdigest()
    return {"fp": digest[:16], "kind": kind, "size": size, "locs": sorted(locs)}


def function_groups(funcs):
    by = {}
    for f in funcs:
        by.setdefault(f[4], []).append(f)
    return [group("function", fs[0][3], [f[:3] for f in fs], text) for text, fs in by.items() if len(fs) >= 2]


def linked(grouped, t1, t2):
    """The windows t1 and t2 (t2 one position on) travel together: every copy of t1 is followed by t2, every t2 preceded by t1."""
    o1, o2 = grouped.get(t1), grouped.get(t2)
    return o1 is not None and o2 is not None and len(o1) == len(o2) and {(li, p + 1) for li, p in o1} == set(o2)


def runs_of(lists, grouped):
    """{(first window, windows in the run): [(list, position)]}: maximal runs of windows copied together."""
    runs = {}
    for li, rec in enumerate(lists):
        ts = rec[4]
        for pos, t in enumerate(ts):
            if t not in grouped or (pos and linked(grouped, ts[pos - 1], t)):
                continue  # no copy, or not the start of a run
            k = 1
            while pos + k < len(ts) and linked(grouped, ts[pos + k - 1], ts[pos + k]):
                k += 1
            runs.setdefault((t, k), []).append((li, pos))
    return runs


def thin(starts, length):
    """Copies that overlap each other in one statement list are kept as non-overlapping ones."""
    kept, last_li, last_end = [], -1, -1
    for li, pos in starts:
        if li != last_li or pos >= last_end:
            kept.append((li, pos))
            last_li, last_end = li, pos + length
    return kept


def fragment_groups(lists):
    occ = {}
    for li, rec in enumerate(lists):
        for pos, t in enumerate(rec[4]):
            occ.setdefault(t, []).append((li, pos))
    grouped = {t: o for t, o in occ.items() if t is not None and len(o) >= 2}
    out = []
    for (text, k), starts in runs_of(lists, grouped).items():
        length = k + WINDOW - 1
        kept = thin(sorted(starts), length)
        spans = [(lists[li][0], lists[li][1][pos], lists[li][2][pos + length - 1], sum(lists[li][3][pos:pos + length]))
                 for li, pos in kept]
        if len(kept) >= 2:
            out.append(group("fragment", spans[0][3], [s[:3] for s in spans], "%s\x1f%d" % (text, k)))
    return out


def covers(big, g):
    """g says nothing new: every copy of g lies inside a copy of the larger function group `big`."""
    inside = lambda loc, m: loc[0] == m[0] and m[1] <= loc[1] and loc[2] <= m[2]
    return (g["kind"] == "fragment" or big["size"] > g["size"]) and all(
        any(inside(loc, m) for m in big["locs"]) for loc in g["locs"])


def clone_groups(funcs, lists):
    found = function_groups(funcs) + fragment_groups(lists)
    bigs = [g for g in found if g["kind"] == "function"]
    kept = [g for g in found if not any(covers(b, g) for b in bigs if b is not g)]
    return sorted(kept, key=lambda g: (-g["size"] * len(g["locs"]), -g["size"], g["kind"], g["locs"]))


def detail(g):
    return "%s %d statements, %d copies: %s" % (g["kind"], g["size"], len(g["locs"]), ", ".join("%s:%d-%d" % loc for loc in g["locs"]))


def row_notes(rows, groups, parsed):
    """B20 (c): a stale row whose members all parse says one copy changed (`diverged`); a live group with fewer copies than
    the row's members is `shrunk:`, green. A members value that is no list is no members."""
    live = {g["fp"]: g for g in groups}
    notes, green = {}, []
    for r in rows:
        rid, members = ratchets.ident(r), r.get("members")
        members = members if isinstance(members, list) else []
        if rid in live and len(live[rid]["locs"]) < len(members):
            green.append("shrunk: %s" % rid)
        elif rid not in live and members and all(m in parsed for m in members):
            notes[rid] = " diverged: changed in one place, check the other copy"
    return notes, green


def basis():
    return {"tool": "clone/1", "python": ratchets.python_minor(),
            "constants": {"normalisation": 1, "min_statements": MIN, "window": WINDOW}, "roots": list(ratchets.ROOTS)}


def scan(root, a, data):
    files = ratchets.scope(root, ratchets.ROOTS)
    found, broken, read = ratchets.parse_all(root, files, ratchets.tree_of(collect))
    groups = clone_groups([f for _, fs, _ in found for f in fs], [x for _, _, ls in found for x in ls])
    notes, green = row_notes(data[SPEC.field], groups, {rel for rel, _, _ in found})
    return ratchets.Scan([(g["fp"], detail(g)) for g in groups], broken, len(files), read, notes=notes, green=green)


def main(argv):
    return ratchets.entry(sys.modules[__name__], argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
