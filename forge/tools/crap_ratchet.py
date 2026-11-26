# card: C1-3
"""CRAP ratchet: cyclomatic complexity and CRAP of every function in the C1-3 roots, against forge/baselines/crap.json.

crap_ratchet.py [--root D] [--base R] [--update [--record ID]] [--basis] [--list] [--coverage-json F --tests-exit N]
Exit 0 green, 1 red, 2 cannot judge, 3 part not judged here (red on Actions, TESTING rule 7); precedence 2 > 1 > 3 > 0.
Complexity (F243: 1 + each If, For, AsyncFor, While, ExceptHandler, IfExp, comprehension, Assert, match_case, + values - 1 per
BoolOp; a nested def is a row of its own) is judged always, against the `crap_limit` row of forge/budgets.json. CRAP = c^2 x
(1 - p)^3 + c, p = coverage of the function's own body, exact (Fraction): red when above the limit. Coverage is read only
for a function whose worst case is above the limit (c <= limit < c^2 + c); it comes from --coverage-json (read and validated
first, judged only when --tests-exit is 0), else from `coverage run` of the `tests` row of forge/ci-jobs.json (F254); no
coverage module is exit 3 (F241). A file that cannot be parsed is red in every tool and no row allows it. Everything a list
tool shares (scope, readers, list, basis, stale and reason rules, --update, raise lines, the driver) is ratchets.py's (F246).
"""
import ast
import os
import shlex
import shutil
import subprocess
import sys
import tempfile
from collections import namedtuple
from fractions import Fraction

import ci
import ratchets

SPEC = ratchets.Spec("forge/baselines/crap.json", scope=ratchets.globs(ratchets.ROOTS))
BRANCH = (ast.If, ast.For, ast.AsyncFor, ast.While, ast.ExceptHandler, ast.IfExp, ast.comprehension, ast.Assert, ast.match_case)
PYTEST = "python -B -m pytest "
Fn = namedtuple("Fn", "id rel c node")


class NotJudged(Exception):
    """The coverage part cannot be judged here: its `not judged:` line, exit 3."""


# ---- complexity and the function rows

def own(fn):
    """Complexity of one function by F243; nested defs and classes are rows of their own and not counted here."""
    c, todo = 1, list(ast.iter_child_nodes(fn))
    while todo:
        n = todo.pop()
        if not isinstance(n, ratchets.DEFS):
            c += isinstance(n, BRANCH) + (len(n.values) - 1 if isinstance(n, ast.BoolOp) else 0)
            todo.extend(ast.iter_child_nodes(n))
    return c


def function_rows(rel, tree):
    """[Fn] of every function at any depth, source order. id = path::qualname, `#k` for the k-th (k >= 2) of one qualname."""
    out, seen, todo = [], {}, [(tree, "")]
    while todo:
        node, pre = todo.pop()
        if isinstance(node, ratchets.DEFS):
            pre += node.name
            if isinstance(node, ratchets.FUNCS):
                seen[pre] = seen.get(pre, 0) + 1
                ident = ratchets.encode("%s::%s%s" % (rel, pre, "#%d" % seen[pre] if seen[pre] > 1 else ""))  # F1: one token
                out.append(Fn(ident, rel, own(node), node))
            pre += "."
        todo.extend((ch, pre) for ch in reversed(list(ast.iter_child_nodes(node))))
    return out


def needs_coverage(c, limit):
    """Worst case (p = 0) above the limit while the complexity alone is not (N25)."""
    return c <= limit and c * c + c > limit


def limit_of(root):
    """The one data row `crap_limit` (F242), read once a function exists (F253 (a)): no function is judged against a guess."""
    rel = "forge/budgets.json"
    try:
        doc = ratchets.read_json(os.path.join(root, rel), rel)
    except ratchets.Refuse as exc:
        raise ratchets.Refuse("crap_limit: %s" % exc)
    rows = doc.get("rows") if isinstance(doc, dict) else None
    row = rows.get("crap_limit") if isinstance(rows, dict) else None
    ceiling = row.get("ceiling") if isinstance(row, dict) and row.get("unit") == "limit" else None
    if not isinstance(ceiling, int) or isinstance(ceiling, bool) or ceiling < 0:
        raise ratchets.Refuse("crap_limit: %s holds no `limit` row with a non-negative integer ceiling" % rel)
    return ceiling


# ---- coverage

def own_lines(fn):
    """The statement lines of the function's own body: first body line to the end, minus the bodies of defs nested in it."""
    gone = set()
    for d in ast.walk(fn):
        if d is not fn and isinstance(d, ratchets.FUNCS):
            gone.update(range(d.body[0].lineno, d.end_lineno + 1))
    return set(range(fn.body[0].lineno, fn.end_lineno + 1)) - gone


def coverage_of(fn, data):
    """p = executed / (executed + missing + excluded) over the own body; an excluded line is missing; none -> 0."""
    ex, miss, exc = data
    span = own_lines(fn)
    seen = (ex | miss | exc) & span
    return Fraction(len((ex - exc) & span), len(seen)) if seen else Fraction(0)


def judge_coverage(need, cov, limit):
    """(red sites, --list suffixes {id: text}, paths absent from the coverage data) of the functions that need coverage."""
    sites, text, lost = [], {}, set()
    for f in need:
        if f.rel not in cov:
            lost.add(f.rel)
            continue
        p = coverage_of(f.node, cov[f.rel])
        x = f.c * f.c * (1 - p) ** 3 + f.c  # exact: AT the limit is never red by rounding
        text[f.id] = " crap %.2f coverage %.1f%%" % (float(x), float(100 * p))
        if x > limit:
            sites.append((f.id, "crap %.2f (complexity %d, coverage %.1f%%)" % (float(x), f.c, float(100 * p))))
    return sites, text, lost


def cov_key(root, key):
    """A coverage path made root-relative with `/`; an absolute path outside the root is None (ignored)."""
    k = key.replace("\\", "/")
    k = k[2:] if k.startswith("./") else k
    base = os.path.abspath(root).replace("\\", "/").rstrip("/") + "/"
    if os.path.isabs(key):
        return k[len(base):] if k.startswith(base) else None
    return k


def lines_of(entry, key):
    got = []
    for name, need in (("executed_lines", True), ("missing_lines", True), ("excluded_lines", False)):
        val = entry.get(name, None if need else []) if isinstance(entry, dict) else None
        if not (isinstance(val, list) and all(type(n) is int for n in val)):
            raise ratchets.Refuse("coverage JSON: %s of %s is not a list of integers" % (name, key))
        got.append(set(val))
    return got


def read_cov(path, root):
    """{root-relative path: [executed, missing, excluded]}; a named input that cannot be read is exit 2, never covered."""
    doc = ratchets.read_json(path, "coverage JSON")
    files = doc.get("files") if isinstance(doc, dict) else None
    if not isinstance(files, dict):
        raise ratchets.Refuse("coverage JSON: no `files` object")
    out = {}
    for key, entry in files.items():
        parts = lines_of(entry, key)
        rel = cov_key(root, key)
        if rel is not None:
            out[rel] = parts
    return out


def check_coverage():
    try:
        import coverage
        ok = coverage.version_info >= (7, 10)  # `patch = subprocess` needs 7.10 (F244 (a))
    except ImportError:
        ok = False
    if not ok:
        raise NotJudged("coverage not importable (%s)" % ratchets.INSTALL)


def tests_command(root):
    """The arguments of the `tests` row of the one job list, which must be `python -B -m pytest <args>` (F254 (a))."""
    try:
        rows = ci.load(os.path.join(root, ci.LIST_REL))
    except ci.Refuse as exc:
        raise ratchets.Refuse(str(exc))
    row = {r["id"]: r for r in rows}.get("tests", {"state": "", "command": ""})
    cmd = row["command"] if row["state"] == "built" else ""
    if not cmd.startswith(PYTEST):
        raise NotJudged("no pytest tests row")
    return cmd[len(PYTEST):]


def step(root, cmd, why):
    done = subprocess.run(cmd, cwd=root, env=dict(os.environ, COVERAGE_CORE="pytrace"), stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT)
    if done.returncode:
        print(done.stdout.decode("utf-8", "replace")[-2000:])
        raise NotJudged(why.format(done.returncode))


def write_rc(root, tmp):
    roots = "".join("    %s\n" % r for r in ratchets.ROOTS if os.path.isdir(os.path.join(root, r)))
    text = ("[run]\nsource =\n%srelative_files = True\npatch = subprocess\ndata_file = %s/data\n\n[report]\nexclude_lines =\n"
            % (roots, tmp.replace("\\", "/")))
    path = os.path.join(tmp, "rc")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return path


def run_coverage(root, rest, tmp):
    rc = write_rc(root, tmp)
    cov = [sys.executable, "-B", "-m", "coverage"]
    step(root, cov + ["run", "--rcfile=" + rc, "-m", "pytest"] + shlex.split(rest), "tests exit {}")
    if len([n for n in os.listdir(tmp) if n.startswith("data")]) > 1:  # a subprocess writes a file of its own
        step(root, cov + ["combine", "--rcfile=" + rc], "coverage report failed")
    step(root, cov + ["json", "--rcfile=" + rc, "-o", os.path.join(tmp, "cov.json")], "coverage report failed")
    return os.path.join(tmp, "cov.json")


def default_road(root):
    check_coverage()
    rest = tests_command(root)
    tmp = tempfile.mkdtemp(prefix="crap-")
    try:
        return read_cov(run_coverage(root, rest, tmp), root)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def coverage_files(a, root, given):
    """given: --coverage-json, already read and validated (F4: 2 beats 3), or None when none was named."""
    if a.coverage_json is None:
        return default_road(root)
    if a.tests_exit != "0":
        raise NotJudged("tests exit %s" % (a.tests_exit if a.tests_exit is not None else "not given"))
    return given


def add_options(ap):
    ap.add_argument("--coverage-json")
    ap.add_argument("--tests-exit")


def check_args(a):
    """Usage, then --coverage-json read and validated before the driver judges anything (t-1997 X2: a named input that
    cannot be read is 2, which beats an unresolved --record, 1, and a basis drift, 3)."""
    if a.tests_exit is not None and a.coverage_json is None:
        raise ratchets.Refuse("usage: --tests-exit needs --coverage-json")
    a.coverage = read_cov(a.coverage_json, a.root) if a.coverage_json is not None else None


def basis():
    return {"tool": "crap/1", "python": ratchets.python_minor(),
            "constants": {"nodes": [n.__name__ for n in BRANCH], "boolop": "values-1"}, "roots": list(ratchets.ROOTS)}


def coverage_part(a, root, given, need, limit):
    """(red sites, --list suffixes, skip ids, code) of the functions that need coverage; one `not judged:` line says why not."""
    try:
        sites, text, lost = judge_coverage(need, coverage_files(a, root, given), limit)
    except NotJudged as exc:
        print("not judged: %s" % exc)
        return [], {}, {f.id for f in need}, 3
    for path in sorted(lost):
        print("not measured: %s" % path)  # F255 (a): an unknown shown as unknown
    return sites, text, {f.id for f in need if f.rel in lost}, 3 if lost else 0


def scan(root, a, data):
    given = a.coverage  # F4: read and validated in check_args
    files = ratchets.scope(root, ratchets.ROOTS)
    found, broken, read = ratchets.parse_all(root, files, ratchets.tree_of(function_rows))
    funcs = [f for fs in found for f in fs]
    if not funcs:
        return ratchets.Scan([], broken, len(files), read)
    limit = limit_of(root)  # the complexity part below never waits on the coverage part (exit 1 beats 3)
    sites = [(f.id, "complexity %d (limit %d)" % (f.c, limit)) for f in funcs if f.c > limit]
    need = [f for f in funcs if needs_coverage(f.c, limit)]
    more, text, skip, code = coverage_part(a, root, given, need, limit) if need else ([], {}, set(), 0)
    lines = ["%s complexity %d%s" % (f.id, f.c, text.get(f.id, "")) for f in funcs]
    return ratchets.Scan(sites + more, broken, len(files), read, lines, code, skip)


def main(argv):
    return ratchets.entry(sys.modules[__name__], argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
