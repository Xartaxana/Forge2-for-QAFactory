# card: C1-3
"""Data-joint tests of C1-3: the three ratchets (crap, lint, clone) read a small temp tree, in-process through main(argv); ci.py
passes FORGE_BASE to its jobs. No coverage run: the coverage JSON is a fixture, a missing module is a monkeypatched sys.modules."""
import ast
import contextlib
import io
import json
import os
import re
import subprocess
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
import ci  # noqa: E402
import clone_ratchet as clone  # noqa: E402
import crap_ratchet as crap  # noqa: E402
import lint_ratchet as lint  # noqa: E402
import ratchets  # noqa: E402

TOOLS = {"crap": crap, "lint": lint, "clone": clone}
P = "factory/tools/u.py"
HOOK = "#!/usr/bin/env python\n"


@pytest.fixture(autouse=True)
def clean_env(monkeypatch):
    for k in [k for k in os.environ if k.startswith(("GIT_", "COVERAGE"))] + ["FORGE_BASE"]:
        monkeypatch.delenv(k, raising=False)


def put(root, files):
    for rel, text in files.items():
        p = os.path.join(root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "wb") as fh:
            fh.write(text if isinstance(text, bytes) else text.encode("utf-8"))


def run(mod, root, *args):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = mod.main(["--root", str(root)] + list(args))
    return code, buf.getvalue()


def new(out):
    return re.findall(r"^new: (\S+)", out, re.M)


def world(tmp_path, files, limit=20):
    """The files and forge/budgets.json: limit an int, "absent", raw text, or the rows dict."""
    root = str(tmp_path)
    put(root, files)
    rows = limit if isinstance(limit, dict) else {"crap_limit": {"unit": "limit", "ceiling": limit}}
    if limit != "absent":
        put(root, {"forge/budgets.json": limit if isinstance(limit, str) else json.dumps({"schema": "budgets/1", "rows": rows})})
    return root


def fn(name, c):  # complexity c by the F243 rule: 1 + (c - 1) ifs
    return "def %s(x):\n%s    return x\n\n" % (name, "".join("    if x == %d:\n        x += 1\n" % i for i in range(c - 1)))


def body(name, k, v):  # k statements; locals and literals differ with v, the normalised code does not
    s = ["    %s = z.get(%d)\n" % (v, len(v))] + ["    %s = %s + z.get(%d)\n" % (v, v, i) for i in range(1, k - 1)]
    return "def %s(z):\n%s    return %s\n\n" % (name, "".join(s), v)


def frag(name, k, v, tail):  # k equal statements then a tail that differs
    return "def %s(z):\n%s    %s\n\n" % (name, "".join("    %s = z.get(%d)\n" % (v, i) for i in range(k)), tail)


def cov(root, files, covered, tests="0", excl=False, data=True, keyf=str):
    out = {}
    for path, src in files.items():
        ex, miss = set(), set()
        for d in [d for d in ast.parse(src).body if isinstance(d, ast.FunctionDef)]:
            ex.add(d.lineno)
            (ex if d.name in covered else miss).update(s.lineno for s in ast.walk(d) if isinstance(s, ast.stmt) and s is not d)
        out[keyf(path)] = {"executed_lines": sorted(ex), "missing_lines": sorted(miss), "excluded_lines": sorted(ex) if excl else []}
    put(root, {"cov.json": json.dumps({"files": out if data else {}})})
    return ["--coverage-json", os.path.join(root, "cov.json"), "--tests-exit", tests]


LAY = {p: fn("f20", 20) + fn("f21", 21) for p in ("factory/a.py", "forge/tools/a.py", "forge/hooks/a.py", "measure/tools/a.py")}
LAY["forge/hooks/git/pre-x"] = HOOK + fn("f20", 20) + fn("f21", 21)
OUT = {"forge/hooks/git/pre-x.next": HOOK + fn("f22", 22), "forge/hooks/b.py.next": fn("f22", 22), "forge/tools/d.json": "{}",
       "forge/hooks/git/sh": "#!/bin/sh\n" + fn("f22", 22), "factory/tests/test_t.py": fn("t22", 22)}
H5, ALL = {P: fn("h5", 5)}, {"f20", "f21", "g25", "g26", "v5"}
DRIFT = dict(H5, **{"forge/baselines/crap.json": json.dumps({"basis": dict(crap.basis(), python="0.0"), "rows": []})})


# expected from: C1-3 part2:109-113 and the brief (PART 2 section 4 limits, coverage, F241 (a), F253 (a), F255 (a), F256)
@pytest.mark.parametrize("files, kw, code, ids, has", [
    (dict(LAY, **OUT), {"covered": ALL}, 1, [p + "::f21" for p in LAY], ""),  # c20 green, c21 red, .next and sh and tests out
    ({P: fn("u5", 5) + fn("u4", 4) + fn("v5", 5)}, {"covered": {"v5"}}, 1, [P + "::u5"], ""),  # c5 red, c4 at the limit green
    ({P: fn("v5", 5)}, {"covered": ALL, "excl": True}, 1, [P + "::v5"], ""),  # excluded = missing
    ({P: fn("g25", 25) + fn("g26", 26)}, {"limit": 25, "covered": ALL}, 1, [P + "::g26"], ""),
    ({P: fn("v5", 5)}, {"covered": ALL, "tests": "1"}, 3, [], "tests exit 1"),
    ({P: fn("v5", 5)}, {"covered": ALL, "data": False}, 3, [], "not measured: " + P),
    (H5, {}, 3, [], "pip install -r forge/ci-requirements.txt"),
    ({P: fn("h5", 5) + fn("big", 21)}, {}, 1, [P + "::big"], "not judged"),  # exit 1 beats 3
    (H5, {"limit": "absent"}, 2, [], "crap_limit"),
    (H5, {"limit": "{not json"}, 2, [], "crap_limit"),
    (H5, {"limit": {}}, 2, [], "crap_limit"),
    (H5, {"limit": {"crap_limit": {"unit": "bytes", "ceiling": 20}}}, 2, [], "crap_limit"),
    (H5, {"limit": {"crap_limit": {"unit": "limit", "ceiling": "20"}}}, 2, [], "crap_limit"),
    (H5, {"limit": True}, 2, [], "crap_limit"),
    (H5, {"limit": -1}, 2, [], "crap_limit"),
    ({P: fn("v5", 5)}, {"covered": set(), "key": "win"}, 1, [P + "::v5"], ""),  # M3: a Windows key
    ({P: fn("v5", 5)}, {"covered": set(), "key": "abs"}, 1, [P + "::v5"], ""),  # M3: an absolute key under the root
])
def test_crap(tmp_path, monkeypatch, files, kw, code, ids, has):
    root = world(tmp_path, files, kw.get("limit", 20))
    args = []
    if "covered" in kw:
        kf = {"win": lambda p: p.replace("/", "\\"), "abs": lambda p: root.replace("\\", "/") + "/" + p}.get(kw.get("key"), str)
        args = cov(root, files, kw["covered"], kw.get("tests", "0"), kw.get("excl", False), kw.get("data", True), kf)
    else:
        monkeypatch.setitem(sys.modules, "coverage", None)
    c, o = run(crap, root, *args)
    assert c == code and sorted(new(o)) == sorted(ids) and has in o, o


# expected from: PART 2 section 4 coverage and JSON edges (a named input that cannot be read is never covered, and 2 beats 1
# and 3 even when nothing needs coverage); F254 usage
@pytest.mark.parametrize("text, args, code, has, files", [
    (None, ["--coverage-json", "{j}", "--tests-exit", "0"], 2, "coverage JSON", H5),
    ("{not json", ["--coverage-json", "{j}", "--tests-exit", "0"], 2, "coverage JSON", H5),
    ('{"files": []}', ["--coverage-json", "{j}", "--tests-exit", "0"], 2, "files", H5),
    ('{"files": {"p": {"executed_lines": ["a"], "missing_lines": []}}}', ["--coverage-json", "{j}", "--tests-exit", "0"], 2, "integers", H5),
    ('{"files": {"p": {"executed_lines": [1]}}}', ["--coverage-json", "{j}", "--tests-exit", "0"], 2, "missing_lines", H5),
    ('{"files": {}}', ["--coverage-json", "{j}"], 3, "tests exit not given", H5),
    ('{"files": {}}', ["--tests-exit", "0"], 2, "usage", H5),
    ("{not json", ["--coverage-json", "{j}", "--tests-exit", "1"], 2, "coverage JSON", H5),  # F4: 2 beats 3
    (None, ["--coverage-json", "{j}", "--tests-exit", "0"], 2, "coverage JSON", {P: fn("h4", 4)}),  # F4: read first, though no function needs coverage
    (None, ["--coverage-json", "{j}", "--tests-exit", "0"], 2, "coverage JSON", DRIFT),  # t-1997 X2 probe E: 2 beats drift 3
    ("{not json", ["--coverage-json", "{j}", "--tests-exit", "0", "--update", "--record", "D-1"], 2, "coverage JSON", H5),  # X2
])
def test_coverage_input(tmp_path, text, args, code, has, files):
    root = world(tmp_path, files)
    j = os.path.join(root, "cov.json")
    put(root, {"cov.json": text} if text else {})
    c, o = run(crap, root, *[j if a == "{j}" else a for a in args])
    assert c == code and has in o, o


# expected from: PART 2 N23 (an identity is one token, whitespace %20) and N25 (rows of a part not judged are skipped, mutant M2)
@pytest.mark.parametrize("rel, rid", [(P, P + "::h5"), ("factory/tools/a b.py", "factory/tools/a%20b.py::h5")])
def test_crap_rows(tmp_path, monkeypatch, rel, rid):
    root = world(tmp_path, {rel: fn("h5", 5)})
    put(root, {"forge/baselines/crap.json": json.dumps({"basis": crap.basis(), "rows": [{"id": rid, "reason": "r"}]})})
    monkeypatch.setitem(sys.modules, "coverage", None)
    c, o = run(crap, root)
    assert c == 3 and "stale" not in o and rid + " complexity 5" in run(crap, root, "--list")[1], o


# expected from: PART 2 N23 (a lint identity with whitespace in its arguments is one token)
def test_lint_identity(tmp_path):
    root = world(tmp_path, {P: "from os import *\nfrom re import *\nx = path\n"}, "absent")
    assert P + "::ImportStarUsage:path,os,%20re " in run(lint, root, "--list")[1]


# expected from: F243 (the rule text) and PART 2 N22 (rows, qualnames, #k)
@pytest.mark.parametrize("src, want", [
    ("def f(x):\n    if x:\n        pass\n", {"f": 2}),
    ("def f(x):\n    for i in x:\n        pass\n    while x:\n        pass\n", {"f": 3}),
    ("def f(x):\n    try:\n        pass\n    except A:\n        pass\n    except B:\n        pass\n", {"f": 3}),
    ("def f(x):\n    return [a for a in x if a] if x else 0\n", {"f": 3}),
    ("def f(x):\n    assert x and x or x\n", {"f": 4}),
    ("def f(x):\n    match x:\n        case 1:\n            pass\n        case 2:\n            pass\n", {"f": 3}),
    ("def f(x):\n    with x:\n        pass\n", {"f": 1}),
    ("def f(x):\n    def g(y):\n        if y:\n            pass\n    return g\n", {"f": 1, "f.g": 2}),
    ("def f(x):\n    return lambda y: y if x else 0\n", {"f": 2}),
    ("class C:\n    if True:\n        pass\n    def m(self):\n        pass\n", {"C.m": 1}),
    ("def f(x):\n    pass\n\n\ndef f(x):\n    if x:\n        pass\n", {"f": 1, "f#2": 2}),
])
def test_complexity(tmp_path, src, want):
    c, o = run(crap, world(tmp_path, {"factory/tools/s.py": src}, 100), "--list")
    got = {k: int(v) for k, v in re.findall(r"^factory/tools/s\.py::(\S+) complexity (\d+)", o, re.M)}
    assert c == 0 and got == want, o


SRC = "import os\nimport re\n"
IDS = ["factory/tools/x.py::UnusedImport:os", "factory/tools/x.py::UnusedImport:re"]


# expected from: B20 part9:129-132, 138-140 (K1 a moved finding, K2 basis, K3 stale and --update, K4 dead scanner), reason rule
@pytest.mark.parametrize("src, rows, basis, args, code, has, left", [
    ("\n" * 10 + SRC, "ok", {}, [], 0, "", 2),
    (SRC, "bare", {}, [], 1, "row has no reason", 2),
    (SRC, "bare", {}, ["--update"], 1, "row has no reason", 2),  # t-1997 mutant M2: a reasonless row keeps --update red
    (SRC, "ok", {"python": "3.0"}, [], 3, "not judged here", 2),
    (SRC, "ok", {"tool": "pyflakes 0.0"}, [], 2, "0.0", 2),
    (SRC, "ok", {"roots": ["factory", "forge/tools", "forge/hooks", "measure/tools"]}, [], 2, "roots", 2),
    ("import os\n", "ok", {}, [], 1, "stale: " + IDS[1], 2),
    ("import os\n", "ok", {}, ["--update"], 0, "updated", 1),
    ("x = 1\n", "ok", {}, [], 2, "found nothing", 2),
    ("x = 1\n", "ok", {}, ["--update"], 2, "found nothing", 2),
    ("x = 1\n", "ok", {}, ["--update", "--record", "D-1"], 1, "cannot resolve D-1", 2),
])
def test_list_rules(tmp_path, src, rows, basis, args, code, has, left):
    root = world(tmp_path, {"factory/tools/x.py": src})
    path = "forge/baselines/lint.json"
    put(root, {path: json.dumps({"basis": dict(lint.basis(), **basis), "rows": [
        {"id": i, "reason": "r"} if rows == "ok" else {"id": i} for i in IDS]})})
    c, o = run(lint, root, *args)
    assert c == code and has in o and len(json.load(open(os.path.join(root, path)))["rows"]) == left, o


# expected from: B20 part9:127-132 (a row added, the list emptied and a basis change are raises; python alone is not)
@pytest.mark.parametrize("old, now, keys", [
    ({"rows": [{"id": "a"}], "basis": {"t": 1}}, {"rows": [{"id": "a"}, {"id": "b"}], "basis": {"t": 1}}, {"b"}),
    ({"rows": [{"id": "a"}], "basis": {}}, {"rows": [], "basis": {}}, {"clear"}),
    ({"rows": [], "basis": {"t": 1}}, {"rows": [], "basis": {"t": 2}}, {"basis"}),
    ({"rows": [], "basis": {"python": "3.11"}}, {"rows": [], "basis": {"python": "3.12"}}, set()),
    ({"nothing": 1}, {"rows": [], "basis": {}}, None),
])
def test_raised(old, now, keys):
    if keys is None:
        with pytest.raises(ratchets.Refuse):
            ratchets.raised(old, now, crap.SPEC)
    else:
        assert set(ratchets.raised(old, now, crap.SPEC)) == keys


A = {"forge/tools/c1.py": body("p", 5, "w"), "forge/hooks/c2.py": body("q", 5, "kk")}
B = {"forge/tools/e1.py": body("m", 6, "a"), "forge/hooks/e2.py": body("n", 6, "bb")}


# expected from: PART 2 N27 and section 4 (5 statements AT, 4 below; window 6 AT, 5 below; one scope; tests out, F256)
@pytest.mark.parametrize("files, has, hasnt", [
    (dict(A, **{"forge/tools/d1.py": body("p4", 4, "w"), "forge/hooks/d2.py": body("q4", 4, "kk"),
                "factory/tests/test_c.py": body("t", 5, "m")}), ["function 5 statements, 2 copies", "c1.py", "c2.py"],
     ["d1.py", "test_c.py"]),
    ({"forge/tools/d1.py": body("p4", 4, "w"), "forge/hooks/d2.py": body("q4", 4, "kk")}, [], ["new:"]),
    ({"forge/tools/f1.py": frag("a", 6, "w", "print(w)"), "forge/hooks/f2.py": frag("b", 6, "kk", "del kk")},
     ["fragment 6 statements, 2 copies"], []),
    ({"forge/tools/f1.py": frag("a", 5, "w", "print(w)"), "forge/hooks/f2.py": frag("b", 5, "kk", "del kk")}, [], ["new:"]),
    ({"forge/tools/t.py": "".join("x%d = %s\n" % (i, " + ".join(["1"] * 1500)) for i in range(6))}, [], ["new:"]),  # F5: deep, parses
])
def test_clone_measure(tmp_path, files, has, hasnt):
    c, o = run(clone, world(tmp_path, files, "absent"))
    assert c == (1 if has else 0) and all(h in o for h in has) and not any(h in o for h in hasnt), o


# expected from: B20 part9:131 (c) the diverged hint; PART 2 N27 (shrunk is green)
def test_clone_rows(tmp_path):
    root = world(tmp_path, dict(A, **B), "absent")
    fp = {"A": "", "B": ""}
    for line in [ln for ln in run(clone, root)[1].splitlines() if ln.startswith("new: ")]:
        fp["A" if "c1.py" in line else "B"] = line.split()[1]
    rows = [{"id": fp["A"], "members": ["forge/tools/c1.py", "forge/hooks/c2.py", "forge/tools/e1.py"], "reason": "r"},
            {"id": fp["B"], "members": ["forge/tools/e1.py", "forge/hooks/e2.py"], "reason": "r"}]
    put(root, {"forge/baselines/clone.json": json.dumps({"basis": clone.basis(), "rows": rows})})
    c, o = run(clone, root)
    assert c == 0 and "shrunk: " + fp["A"] in o and "new:" not in o, o
    put(root, {"forge/hooks/c2.py": "def q(z):\n    return 1\n"})
    c, o = run(clone, root)
    assert c == 1 and "stale: %s diverged: changed in one place" % fp["A"] in o, o


# expected from: PART 2 section 4 scope and reading (cannot parse is red in every tool, never allowed; --update refused)
@pytest.mark.parametrize("name", list(TOOLS))
@pytest.mark.parametrize("src", ["def (:\n", b"s = '\xe9'\n", "x = " + " + ".join(["1"] * 60000) + "\n"], ids=["syntax", "latin1", "deep"])
def test_unreadable(tmp_path, name, src):
    root = world(tmp_path, {"factory/tools/bad.py": src, "forge/tools/ok.py": "x = 1\n"})
    c, o = run(TOOLS[name], root)
    c2, o2 = run(TOOLS[name], root, "--update")
    assert (c, c2) == (1, 1) and "new: factory/tools/bad.py cannot parse" in o and not os.path.exists(root + "/forge/baselines"), o2


# expected from: PART 2 N29 and F246 (one driver: an unresolved --record is exit 1 before any scan; a scope no file of which could
# be read at all is exit 2, N2; one read but not parsed is still read, c13's red in all three); t-1997 probe A (the Lead's
# ruling (2): a bad base, 2, beats an unresolved record) and probe F (N23: a row id is one token, a hand row with a space is 2);
# t-1998 F1 probe and the Lead's ruling Q2 (non-python basis drift 2 > unresolved record 1 > python-minor drift 3)
@pytest.mark.parametrize("name", list(TOOLS))
@pytest.mark.parametrize("files, args, deny, code, has", [
    ({}, ["--update", "--record", "D-1"], False, 1, "cannot resolve D-1"),
    ({}, ["--update", "--record", "D-1", "--base", "nope"], False, 2, "base nope: not a commit"),
    ({"forge/baselines/%s.json" % n: json.dumps({"basis": {}, "rows": [{"id": "a b.py::h5", "reason": "r"}]}) for n in TOOLS},
     [], False, 2, 'row id "a b.py::h5" holds whitespace'),
    ({"factory/tools/bad.py": "x = 1\n"}, [], True, 2, "read none of the 1 files"),
    ({"factory/tools/bad.py": "def (:\n"}, [], False, 1, "cannot parse"),
    ({"forge/baselines/%s.json" % n: json.dumps({"basis": {}, "rows": []}) for n in TOOLS}, ["--update", "--record", "D-1"],
     False, 2, "basis tool missing"),  # t-1998 F1 (Lead Q2): a non-python basis drift, 2, beats an unresolved record
    ({"forge/baselines/%s.json" % n: {"python": "0.0"} for n in TOOLS}, ["--update", "--record", "D-1"], False, 1,
     "cannot resolve D-1"),  # t-1998 F1: an unresolved record, 1, beats a python-minor drift, 3 (a dict: the tool's basis)
])
def test_driver(tmp_path, monkeypatch, name, files, args, deny, code, has):
    def denied(root, rel):
        raise PermissionError(13, "denied")
    if deny:
        monkeypatch.setattr(ratchets, "raw_of", denied)
    files = {rel: json.dumps({"basis": dict(TOOLS[name].basis(), **t), "rows": []}) if isinstance(t, dict) else t
             for rel, t in files.items()}
    c, o = run(TOOLS[name], world(tmp_path, files, "absent"), *args)
    assert c == code and has in o, o


# expected from: t-1997 probe B (an unexpected error is exit 2, its line never an absolute path: entry prints describe)
def test_entry(tmp_path, monkeypatch):
    def boom(mod, argv):
        raise PermissionError(13, "denied", "/abs/secret/b.py")
    monkeypatch.setattr(ratchets, "drive", boom)
    c, o = run(crap, tmp_path)
    assert c == 2 and "cannot judge: PermissionError: denied" in o and "secret" not in o, o


# expected from: PART 2 section 4 (an empty file is green; K1 the empty repository; pyflakes first, exit 2 with the door)
@pytest.mark.parametrize("name", list(TOOLS))
@pytest.mark.parametrize("files", [{}, {"factory/tools/e.py": ""}])
def test_clean_inputs(tmp_path, name, files):
    assert run(TOOLS[name], world(tmp_path, files, "absent"))[0] == 0


def test_pyflakes_absent(tmp_path, monkeypatch):
    for mod in ("pyflakes", "pyflakes.api"):  # both: an earlier row may have cached the submodule
        monkeypatch.setitem(sys.modules, mod, None)
    c, o = run(lint, world(tmp_path, {}, "absent"))
    assert c == 2 and "pip install -r forge/ci-requirements.txt" in o


# expected from: PART 2 F254 (a): the tests row of the one job list, `python -B -m pytest <args>`
@pytest.mark.parametrize("jobs, want", [
    ([{"id": "tests", "command": "python -B -m pytest forge/tests -q", "card": "x", "state": "built"}], "forge/tests -q"),
    ([{"id": "tests", "command": "python -B -m pytest forge/tests", "card": "x", "state": "not_built"}], crap.NotJudged),
    ([{"id": "tests", "command": "pytest forge/tests", "card": "x", "state": "built"}], crap.NotJudged),
    ([], crap.NotJudged),
    (None, ratchets.Refuse),
])
def test_tests_command(tmp_path, jobs, want):
    put(str(tmp_path), {"forge/ci-jobs.json": json.dumps(jobs)} if jobs is not None else {})
    if isinstance(want, str):
        assert crap.tests_command(str(tmp_path)) == want
    else:
        with pytest.raises(want):
            crap.tests_command(str(tmp_path))


# expected from: F245 (c) and PART 2 section 4 (a job sees FORGE_BASE iff ci.py resolved a base, and it equals that base)
@pytest.mark.parametrize("given, want_base", [(True, True), (False, False)])
def test_ci_base(tmp_path, monkeypatch, given, want_base):
    head, got = ci.commit_of("HEAD"), os.path.join(str(tmp_path), "got.txt")
    put(str(tmp_path), {"job.py": "import os, sys\nopen(sys.argv[1], 'w').write(os.environ.get('FORGE_BASE', ''))\n"})
    put(str(tmp_path), {"jobs.json": json.dumps([{"id": "fb", "card": "x", "state": "built", "command": '"%s" -B "%s" "%s"' % (
        sys.executable, os.path.join(str(tmp_path), "job.py"), got)}])})
    monkeypatch.setenv("FORGE_BASE", "deadbeef")
    with contextlib.redirect_stdout(io.StringIO()):
        assert ci.main(["--list", os.path.join(str(tmp_path), "jobs.json")] + (["--base", head] if given else [])) == 0
    assert head and open(got).read() == (head if want_base else "")


# ci.py rows through main(argv): one temp git repo (4 commits) stands for ci.ROOT; the list under test is a file passed by --list
def row(i, state="built", cmd=None):
    return {"id": i, "card": "x", "state": state, "command": (cmd if cmd is not None else '"%s" -c "import sys; sys.exit(0)"' % sys.executable) if state == "built" else ""}


def exit_with(n, tail=""):
    return '"%s" -c "import sys; sys.exit(%d)"%s' % (sys.executable, n, tail)


OLD = [row("a"), row("b"), row("nb", "not_built")]


@pytest.fixture(scope="module")
def repo(tmp_path_factory):
    root, shas = str(tmp_path_factory.mktemp("cirepo")), {}
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}

    def git(*a):
        return subprocess.run(["git", "-C", root, "-c", "user.name=t", "-c", "user.email=t@t", "-c", "commit.gpgsign=false"] + list(a),
                              check=True, capture_output=True, env=env).stdout.decode().strip()
    git("init", "-q")
    for name, msg, text in (("c0", "born", None), ("c1", "list", json.dumps(OLD).encode()), ("c2", "retire-job: b -- merged away", None),
                            ("c3", "bad", b"\xff\xfe")):
        if text:
            put(root, {"forge/ci-jobs.json": text})
        git("add", "-A")
        git("commit", "-q", "--allow-empty", "-m", msg)
        shas[name] = git("rev-parse", "HEAD")
    shas["root"] = root
    return shas


@pytest.fixture
def ci_repo(repo, monkeypatch):
    monkeypatch.setattr(ci, "ROOT", repo["root"])
    return repo


def go(tmp_path, now, args, shas):
    """ci.main over the list `now` (rows or raw bytes); an argument @c1 is that commit's sha. Returns (code, stdout)."""
    path = os.path.join(str(tmp_path), "jobs.json")
    put(str(tmp_path), {"jobs.json": now if isinstance(now, bytes) else json.dumps(now)})
    argv = ["--list", path] + [shas[a[1:]] if a.startswith("@") else a for a in args]
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = ci.main(argv)
    return code, buf.getvalue()


# expected from: C1-6 part2:139-141 (check: not_built only shrinks, a built row is not deleted, a retire-job line retires it) and
# plan record 25.11 23:27 item 3 (retire-job: <id> -- <reason>); exit 2 for a base that cannot be judged
@pytest.mark.parametrize("now, args, code, has", [
    (OLD, [], 0, "no base"),
    (OLD, ["--base", "@c0"], 0, "born"),
    (OLD, ["--base", "@c1", "--head", "@c1"], 0, "ok   not_built did not grow"),
    (OLD + [row("n2", "not_built")], ["--base", "@c1", "--head", "@c1"], 1, "not_built grew against"),
    ([row("a"), row("nb", "not_built")], ["--base", "@c1", "--head", "@c1"], 1, "built row absent against"),
    ([row("a"), row("nb", "not_built")], ["--base", "@c1", "--head", "@c2"], 0, "retired: b -- merged away"),
    (OLD, ["--base", "@c3", "--head", "@c3"], 2, "not UTF-8"),
    (OLD, ["--base", "nope"], 2, "not a commit"),
])
def test_ci_check(tmp_path, ci_repo, now, args, code, has):
    c, o = go(tmp_path, now, ["check"] + args, ci_repo)
    assert c == code and has in o, o


# expected from: C1-6 part2:139-141 and B8 part4b-2:21 (matrix: one JSON object count/include/not_built; $GITHUB_OUTPUT lines)
@pytest.mark.parametrize("args, tail", [
    ([], None),
    (["--base", "@c1", "--head", "@c2"], "base=%(c1)s\nhead=%(c2)s\n"),
    (["--head", "@c2"], "base=\nhead=%(c2)s\n"),
])
def test_ci_matrix(tmp_path, ci_repo, args, tail):
    gh = os.path.join(str(tmp_path), "out.txt")
    c, o = go(tmp_path, OLD, ["matrix"] + args + (["--github-output", gh] if tail else []), ci_repo)
    assert c == 0 and json.loads(o) == {"count": 2, "include": [{"id": "a"}, {"id": "b"}], "not_built": ["nb"]}, o
    if tail:
        inc = json.dumps({"include": [{"id": "a"}, {"id": "b"}]})
        assert open(gh, encoding="utf-8").read() == "include=%s\ncount=2\nnb_line=not built: 1 (nb)\n" % inc + tail % ci_repo


# expected from: TESTING.md rules 6-7 and C1-6 part2:139-141 (exit 3 is not judged here, red on Actions; a token with no value is 3;
# --only names a built row)
@pytest.mark.parametrize("rows, args, actions, code, has, hasnt", [
    ([row("a")], [], None, 0, ["ok   a", "not built: 0"], ["FAIL"]),
    ([row("a", cmd=exit_with(1)), row("b"), row("nb", "not_built")], [], None, 1, ["FAIL a (exit 1)", "ok   b", "not built: 1 (nb)", "failed: a"], []),
    ([row("a", cmd=exit_with(3))], [], None, 0, ["not judged here: a"], ["FAIL", "failed"]),
    ([row("a", cmd=exit_with(3))], [], "true", 1, ["FAIL a (exit 3)", "failed: a"], ["not judged"]),
    ([row("a", cmd=exit_with(0, " {base}"))], [], None, 0, ["not judged here: a"], ["FAIL"]),
    ([row("a", cmd=exit_with(0, " {base}"))], [], "true", 1, ["FAIL a (exit 3)"], ["not judged"]),
    ([row("a", cmd=exit_with(0, " {base}"))], ["--base", "@c1"], "true", 0, ["ok   a"], ["FAIL"]),
    ([row("a", cmd=exit_with(1)), row("b")], ["--only", "b"], None, 0, ["ok   b"], ["FAIL", "not built"]),
    ([row("a"), row("nb", "not_built")], ["--only", "nb"], None, 2, ["cannot judge: --only nb"], ["ok"]),
    ([row("a")], ["--only", "zz"], "true", 2, ["cannot judge: --only zz"], ["ok"]),
])
def test_ci_run_all(tmp_path, ci_repo, monkeypatch, rows, args, actions, code, has, hasnt):
    monkeypatch.delenv("GITHUB_ACTIONS", raising=False) if actions is None else monkeypatch.setenv("GITHUB_ACTIONS", actions)
    c, o = go(tmp_path, rows, args, ci_repo)
    assert c == code and all(h in o for h in has) and not any(h in o for h in hasnt), o


def bad(**kw):
    return [dict(row("a"), **kw)]


# expected from: C1-6 part2:139-141 (the list is one array of rows with exactly four fields; every other shape is exit 2, cannot judge)
@pytest.mark.parametrize("text, has", [
    (b"{not json", "not valid JSON"),
    (b"", "not valid JSON"),
    (b"\xff\xfe", "not UTF-8"),
    (b'{"a": 1}', "one JSON array"),
    (b"[1]", "row 0 must hold exactly"),
    (b'[[{"id": "a"}]]', "row 0 must hold exactly"),
    (json.dumps(bad(extra=1)).encode(), "row 0 must hold exactly"),
    (json.dumps([{"id": "a", "card": "x", "state": "built"}]).encode(), "row 0 must hold exactly"),
    (json.dumps(bad(id="")).encode(), "row 0 has no id"),
    (json.dumps(bad(id="a\nb")).encode(), "must match"),
    (json.dumps(bad(id="A")).encode(), "must match"),
    (json.dumps(bad() + bad()).encode(), "duplicate id a"),
    (json.dumps(bad(state="done")).encode(), "unknown state"),
    (json.dumps(bad(card=" ")).encode(), "no card"),
    (json.dumps(bad(command=5)).encode(), "must be a string"),
    (json.dumps(bad(command=" ")).encode(), "holds no command"),
])
def test_ci_rows_refused(tmp_path, ci_repo, text, has):
    c, o = go(tmp_path, text, [], ci_repo)
    assert c == 2 and o.startswith("cannot judge: ") and has in o, o
