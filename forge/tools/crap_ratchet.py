# card: C1-3
"""CRAP ratchet, and the one engine of the three C1-3 ratchets (crap, lint, clone): scope, source reading, the driver.

crap_ratchet.py [--root D] [--base R] [--update [--record ID]] [--basis] [--list] [--coverage-json F --tests-exit N]
Exit 0 green, 1 red, 2 cannot judge, 3 part not judged here (red on Actions, TESTING rule 7); precedence 2 > 1 > 3 > 0.
Complexity (F243: 1 + each If, For, AsyncFor, While, ExceptHandler, IfExp, comprehension, Assert, match_case, + values - 1 per
BoolOp; a nested def is a row of its own) is judged always, against the `crap_limit` row of forge/budgets.json. CRAP = c^2 x
(1 - p)^3 + c, p = coverage of the function's own body, exact (Fraction): red when above the limit. Coverage is read only
for a function whose worst case is above the limit (c <= limit < c^2 + c); it comes from --coverage-json (judged only when
--tests-exit is 0), else from `coverage run` of the `tests` row of forge/ci-jobs.json (F254); no coverage module is exit 3
(F241). A file that cannot be parsed is red in every tool and no row allows it. The list, basis, stale and reason rules, the
--update road and the base/raise lines are ratchets.py's (F246); lint_ratchet.py and clone_ratchet.py import this file's
scope, source reader and driver: the one copy.
"""
import ast
import io
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import tokenize
import warnings
from collections import namedtuple
from fractions import Fraction

import ci
import ratchets

NAME = "crap"
ROOTS = ("factory", "forge/tools", "forge/hooks", "measure/tools")
RECORD = ("word", "decision")
BRANCH = (ast.If, ast.For, ast.AsyncFor, ast.While, ast.ExceptHandler, ast.IfExp, ast.comprehension, ast.Assert, ast.match_case)
FUNCS = (ast.FunctionDef, ast.AsyncFunctionDef)
DEFS = FUNCS + (ast.ClassDef,)
BAD = (SyntaxError, ValueError, RecursionError, MemoryError, OSError)  # ValueError holds UnicodeError and a NUL byte
PYTEST = "python -B -m pytest "
INSTALL = "python -m pip install -r forge/ci-requirements.txt"
Fn = namedtuple("Fn", "id rel c node")


class NotJudged(Exception):
    """The coverage part cannot be judged here: its `not judged:` line, exit 3."""


class Scan:
    """What a tool measured. sites [(identity, detail)]; broken [(path, why)] (red, no row allows it); files in scope; lines
    for --list (None: the sites); code 0 or 3 (a part not judged); skip: row ids not judged; notes {row id: text added to its
    stale line}; green: lines printed with no verdict."""

    def __init__(self, sites, broken, files, lines=None, code=0, skip=(), notes=None, green=()):
        self.sites, self.broken, self.files, self.code = sites, broken, files, code
        self.lines = lines if lines is not None else ["%s %s" % s for s in sites]
        self.skip, self.notes, self.green = set(skip), notes or {}, list(green)


# ---- scope and source (shared by the three tools)

def is_python(root, rel):
    """A `*.py`, or an extensionless file whose first line is a python shebang (a git hook). Anything else is out."""
    name = rel.rsplit("/", 1)[-1]
    if "." in name:
        return name.endswith(".py")
    try:
        with open(os.path.join(root, rel), "rb") as fh:
            first = fh.readline(512)
    except OSError:
        return True  # unreadable: it is reported as a file that cannot be parsed, never skipped
    return first.startswith(b"#!") and b"python" in first


def is_test(rel):
    parts = rel.split("/")
    return "tests" in parts or (parts[-1].startswith("test_") and parts[-1].endswith(".py"))


def scope(root, extra=(), tests=False):
    """The files of the roots (an absent root is empty), `/`-separated, sorted. F256: test files are in for lint only."""
    found = ratchets.files_of(root, ["%s/**" % r for r in ROOTS + tuple(extra)])
    return [r for r in found if is_python(root, r) and (tests or not is_test(r))]


def read_source(root, rel):
    """The text of a file decoded by its PEP 263 line or BOM; a file that is not UTF-8 without a line raises."""
    with open(os.path.join(root, rel), "rb") as fh:
        raw = fh.read()
    return raw.decode(tokenize.detect_encoding(io.BytesIO(raw).readline)[0])


def describe(exc):
    if isinstance(exc, OSError):  # str() of an OSError holds an absolute path
        return "%s: %s" % (type(exc).__name__, (exc.strerror or "cannot be read")[:200])
    lines = str(exc).splitlines()
    return "%s: %s" % (type(exc).__name__, lines[0][:200]) if lines else type(exc).__name__


def parse_all(root, files, build):
    """([build(rel, tree) per file], [(rel, why)]): a file that cannot be read or parsed is broken, never clean."""
    done, broken = [], []
    for rel in files:
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                done.append(build(rel, ast.parse(read_source(root, rel), filename=rel)))
        except BAD as exc:
            broken.append((rel, describe(exc)))
    return done, broken


# ---- complexity and the function rows

def own(fn):
    """Complexity of one function by F243; nested defs and classes are rows of their own and not counted here."""
    c, todo = 1, list(ast.iter_child_nodes(fn))
    while todo:
        n = todo.pop()
        if not isinstance(n, DEFS):
            c += isinstance(n, BRANCH) + (len(n.values) - 1 if isinstance(n, ast.BoolOp) else 0)
            todo.extend(ast.iter_child_nodes(n))
    return c


def function_rows(rel, tree):
    """[Fn] of every function at any depth, source order. id = path::qualname, `#k` for the k-th (k >= 2) of one qualname."""
    out, seen, todo = [], {}, [(tree, "")]
    while todo:
        node, pre = todo.pop()
        if isinstance(node, DEFS):
            pre += node.name
            if isinstance(node, FUNCS):
                seen[pre] = seen.get(pre, 0) + 1
                out.append(Fn("%s::%s%s" % (rel, pre, "#%d" % seen[pre] if seen[pre] > 1 else ""), rel, own(node), node))
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
        if d is not fn and isinstance(d, FUNCS):
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
        raise NotJudged("coverage not importable (%s)" % INSTALL)


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
    roots = "".join("    %s\n" % r for r in ROOTS if os.path.isdir(os.path.join(root, r)))
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


def coverage_files(a, root):
    if a.coverage_json is None:
        return default_road(root)
    if a.tests_exit != "0":
        raise NotJudged("tests exit %s" % (a.tests_exit if a.tests_exit is not None else "not given"))
    return read_cov(a.coverage_json, root)


def add_options(ap):
    ap.add_argument("--coverage-json")
    ap.add_argument("--tests-exit")


def check_args(a):
    if a.tests_exit is not None and a.coverage_json is None:
        raise ratchets.Refuse("usage: --tests-exit needs --coverage-json")


def basis():
    return {"tool": "crap/1", "python": ratchets.python_minor(),
            "constants": {"nodes": [n.__name__ for n in BRANCH], "boolop": "values-1"}, "roots": list(ROOTS)}


def coverage_part(a, root, need, limit):
    """(red sites, --list suffixes, skip ids, code) of the functions that need coverage; one `not judged:` line says why not."""
    try:
        sites, text, lost = judge_coverage(need, coverage_files(a, root), limit)
    except NotJudged as exc:
        print("not judged: %s" % exc)
        return [], {}, {f.id for f in need}, 3
    for path in sorted(lost):
        print("not measured: %s" % path)  # F255 (a): an unknown shown as unknown
    return sites, text, {f.id for f in need if f.rel in lost}, 3 if lost else 0


def scan(root, a, rows):
    files = scope(root)
    found, broken = parse_all(root, files, function_rows)
    funcs = [f for fs in found for f in fs]
    if not funcs:
        return Scan([], broken, len(files))
    limit = limit_of(root)  # the complexity part below never waits on the coverage part (exit 1 beats 3)
    sites = [(f.id, "complexity %d (limit %d)" % (f.c, limit)) for f in funcs if f.c > limit]
    need = [f for f in funcs if needs_coverage(f.c, limit)]
    more, text, skip, code = coverage_part(a, root, need, limit) if need else ([], {}, set(), 0)
    lines = ["%s complexity %d%s" % (f.id, f.c, text.get(f.id, "")) for f in funcs]
    return Scan(sites + more, broken, len(files), lines, code, skip)


# ---- the driver of the three tools

def ident(row):
    rid = row["id"]
    if not isinstance(rid, str) or not rid.strip():
        raise ValueError("an id is a non-empty string")
    return rid


def door(name):
    return ("door: edit basis in forge/baselines/%s.json; a basis change also needs `ratchet-raise: %s.json basis -- <W-n | D-n>`"
            "; --update does not touch basis" % (name, name))


def raised(old, data):
    """Raise keys against the base (N13): a row added, the list emptied (`clear`), a basis change (`basis`): word | decision."""
    try:
        seen = {ident(r) for r in old["rows"]}
    except (KeyError, TypeError, AttributeError, ValueError):
        raise ratchets.Refuse("the base list: must be one JSON object with well-formed rows")
    keys = {ident(r): "baseline row added" for r in data["rows"] if ident(r) not in seen}
    if ratchets.cleared(old["rows"], data["rows"]):
        keys["clear"] = "list emptied"
    if ratchets.basis_changed(old.get("basis"), data["basis"]):
        keys["basis"] = "basis changed"
    return {k: (what, RECORD) for k, what in keys.items()}


def stale_out(notes):
    def out(line):
        print(line + notes.get(line[len("stale: "):], "") if line.startswith("stale: ") else line)
    return out


def update(mod, a, held, scan, stale, new):
    if scan.broken:
        print("refused: --update while a file cannot be parsed (fix it first)")
        return 1
    scope_globs = ["%s/**" % r for r in ROOTS + getattr(mod, "EXTRA", ())]
    code = ratchets.update(a.root, held[1], held[2], "rows", ident, stale, a.record, RECORD, scope_globs, print)
    return ratchets.verdict([code, 1 if new else 0, scan.code])


def conclude(mod, a, held, scan):
    rel, path, data, rows, base = held
    if a.list and scan.lines:
        print("\n".join(sorted(scan.lines)))
    for where, why in scan.broken:
        print(ratchets.finding(where, "cannot parse: " + why))
    live = [r for r in rows if ident(r) not in scan.skip]
    sites = [(re.sub(r"\s", "%20", i), d) for i, d in scan.sites]
    new, stale, bare = ratchets.judge_list(sites, live, ident, scan.files, scan.files, stale_out(scan.notes))
    for identity, detail in new:
        print(ratchets.finding(identity, detail))
    for line in scan.green:
        print(line)
    if a.update:
        return update(mod, a, held, scan, set(stale), new)
    old = ratchets.base_doc(a.root, base, rel, print)
    code = ratchets.judge_raises(a.root, base, rel, raised(old, data), print) if old is not None else 0
    return ratchets.verdict([1 if (new or stale or bare or scan.broken) else 0, code, scan.code])


def judge(mod, a):
    rel = "forge/baselines/%s.json" % mod.NAME
    path = os.path.join(a.root, rel)
    if a.update and a.record:  # before the scan: a dead scanner must not hide that no record resolves yet (L11)
        err = ratchets.resolve(a.record, RECORD)
        if err:
            print(err)
            return 1
    data, rows = ratchets.load_list(path, rel, ident, "rows")
    base = ratchets.base_of(a.root, a.base)
    drift = ratchets.check_basis(data["basis"], mod.basis(), door(mod.NAME))
    if drift:
        print("not judged here: python %s, basis %s" % (ratchets.python_minor(), drift))
        return 3
    return conclude(mod, a, (rel, path, data, rows, base), mod.scan(a.root, a, rows))


def drive(mod, argv):
    ap = ratchets.parser(mod.__doc__.split("\n")[0])
    for flag in ("--update", "--basis", "--list"):
        ap.add_argument(flag, action="store_true")
    ap.add_argument("--record")
    getattr(mod, "add_options", lambda p: None)(ap)
    a = ap.parse_args(argv)
    getattr(mod, "check_args", lambda x: None)(a)
    if a.basis:
        print(json.dumps(mod.basis()))
        return 0
    return judge(mod, a)


def entry(mod, argv):
    """A tool's main: Refuse is exit 2 (ratchets.guarded); any other exception is exit 2 too, never a traceback exit 1."""
    try:
        return ratchets.guarded(drive, mod, argv)
    except Exception as exc:
        print("cannot judge: %s: %s" % (type(exc).__name__, exc))
        return 2


def main(argv):
    return entry(sys.modules[__name__], argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
