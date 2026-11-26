# card: C1-2
"""Data-joint tests of C1-2: budgets.json and universality-names.json read by size_ratchet.py and universality.py (in-process
on temp trees). Git fixtures only for raises: one module-scoped repository per tool. `expected from:` names each source."""
import contextlib
import io
import json
import os
import subprocess
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
import ratchets  # noqa: E402
import size_ratchet as sz  # noqa: E402
import universality as uni  # noqa: E402

B = {"rules_worker": {"unit": "bytes", "paths": ["CLAUDE.md"], "ceiling": 12288},
     "factory_code": {"unit": "nonblank_lines", "paths": ["factory/tools/**/*.py"], "ceiling": 3},
     "gate_rules": {"unit": "rows", "paths": ["factory/data/gate-rules.yaml"], "ceiling": 45},
     "stage_start_load": None, "crap_limit": {"unit": "limit", "ceiling": 20}}


@pytest.fixture(autouse=True)
def clean_env(monkeypatch):
    for k in [k for k in os.environ if k.startswith("GIT_")] + ["FORGE_BASE"]:
        monkeypatch.delenv(k, raising=False)


def put(root, files):
    for rel, text in files.items():
        p = os.path.join(root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "wb") as fh:
            fh.write(text if isinstance(text, bytes) else text.encode("utf-8"))


def budg(rows):
    return {"forge/budgets.json": json.dumps({"schema": "budgets/1", "rows": rows})}


def names(allow=(), basis=None):
    return {"forge/universality-names.json": json.dumps(
        {"basis": basis or uni.basis(), "names": {"runner": ["pytest"], "tracker": ["jira"], "framework": ["playwright"]},
         "allow": list(allow)})}


def run(mod, root, *args):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = mod.main(["--root", str(root)] + list(args))
    return code, buf.getvalue()


def row(f, **kw):
    return dict({"file": "factory/tools/%s.py" % f, "token": "pytest", "reason": "r"}, **kw)


def ceil(**kw):
    return {k: dict(v, ceiling=kw.get(k, v["ceiling"])) if v else v for k, v in B.items()}


def world(tmp_path_factory, steps):
    """One repository for a module: steps are (message, files or None); (root, shas, checkout(i)). t-1992 N6."""
    g = str(tmp_path_factory.mktemp("g"))
    cmd = ["git", "-C", g, "-c", "user.name=t", "-c", "user.email=t@t"]
    sh = lambda *a: subprocess.run(cmd + list(a), capture_output=True).stdout.decode().strip()
    sh("init", "-q")
    tracked = set()
    for msg, files in steps:
        put(g, files or {})
        if set(files or ()) - tracked:  # a new path is added once; later commits use -a (fewer processes)
            sh("add", "-A")
            tracked |= set(files)
        sh("commit", "-q", "-a", "--allow-empty", "--no-verify", "-m", msg)
    shas = sh("rev-list", "--reverse", "HEAD").split()
    return g, shas, lambda i: sh("checkout", "-q", shas[i])


@pytest.fixture(scope="module")
def repo(tmp_path_factory):
    fc = B["factory_code"]
    return world(tmp_path_factory, [(msg, rows and budg(rows)) for msg, rows in (
        ("empty", None), ("budgets", B), ("raise", ceil(factory_code=4)),
        ("ratchet-raise: budgets.json factory_code -- W-1", ceil(factory_code=4)),
        ("budget-raise: crap_limit -- x", ceil(factory_code=2, crap_limit=21)),
        ("removed", {k: v for k, v in B.items() if k != "factory_code"}),
        ("unit", dict(B, factory_code=dict(fc, unit="bytes"))),
        ("paths", dict(B, factory_code=dict(fc, paths=["nothing/*.py"]))),
        ("quoted\n\n  > ratchet-raise: budgets.json factory_code -- W-1", ceil(factory_code=5)))])


# expected from: B20 part9:127, 132, 139; C1-2 part2:100; F245; the owner's word 26.11 about 11:01 (crap_limit); t-1991 B2, F5, M1 (F8 rows: test_universality)
@pytest.mark.parametrize("head, base, env, code, has, hasnt", [
    (2, 1, 0, 1, "new: forge/budgets.json::factory_code", None),
    (2, 1, 1, 1, "new: forge/budgets.json::factory_code", None),
    (3, 1, 0, 1, "cannot resolve W-1", None),
    (3, 0, 0, 0, "born", None),
    (4, 3, 0, 1, "new: forge/budgets.json::crap_limit", "::factory_code"),
    (4, 0, 0, 0, "born", "new:"),
    (4, None, 0, 0, "raises not judged: no base", "new:"),
    (4, "nope", 0, 2, "not a commit", None),
    (3, 2, 0, 0, "ceiling 4", "new:"),
    (5, 4, 0, 1, "row removed", None),
    (6, 4, 0, 1, "scan narrowed", None),
    (7, 4, 0, 1, "scan narrowed", None),
    (8, 4, 0, 1, "cannot resolve W-1", "needs"),
])
def test_raises(repo, monkeypatch, head, base, env, code, has, hasnt):
    g, shas, checkout = repo
    checkout(head)
    ref = shas[base] if isinstance(base, int) else base
    if env:
        monkeypatch.setenv("FORGE_BASE", ref)
    c, o = run(sz, g, *(["--base", ref] if ref and not env else []))
    assert c == code and has in o and (hasnt is None or hasnt not in o), o


# expected from: C1-2 part2:100-105; B16 part8:105 and F180 (not set); B20 part9:134 (figure line); the brief section 4
@pytest.mark.parametrize("files, code, has", [
    ({}, 0, ["not set", "absent: 0", "tests: 0 lines, product: 0 lines"]),
    ({"factory/tools/a.py": "a = 1\n\nb = 2\nc = 3\n"}, 0, ["3 nonblank_lines"]),
    ({"factory/tools/a.py": "a\nb\nc\nd\n"}, 1, ["new: forge/budgets.json::factory_code"]),
    ({"factory/data/gate-rules.yaml": "{not json"}, 2, ["cannot judge"]),
    ({"factory/data/gate-rules.yaml": '{"rows": []}', "forge/tools/t.py": "x\n", "forge/tests/t.py": "x\ny\n"}, 0,
     ["gate_rules: 0 rows", "tests: 2 lines, product: 1 lines (ratio 2.00)"]),
    ({"forge/budgets.json": "{not json"}, 2, ["cannot judge"]),
    ({"forge/budgets.json": json.dumps({"rows": {"x": {"unit": "bytes", "paths": ["a"], "ceiling": -1}}})}, 2, ["ceiling"]),
    ({"forge/budgets.json": json.dumps({"rows": {"crap_limit": None}})}, 2, ["unit"]),
    ({"forge/budgets.json": json.dumps({"rows": {"stage_start_load": {"unit": "bytes"}}})}, 2, ["C4-6 not built"]),
    ({"forge/hooks/git/pre-push": "a\nb\n", "forge/tools/t.py": "x\n"}, 0, ["product: 3 lines"]),
    ({"forge/tests/old.py": b"# caf\xe9\n"}, 0, ["(ratio n/a: forge/tests/old.py: not UTF-8)"]),
    ({"forge/hooks/git/blob": b"\x00\xff"}, 0, ["(ratio n/a: forge/hooks/git/blob: not UTF-8)"]),
    ({"factory/tools/a.py": b"a = '\xe9'\n"}, 2, ["factory/tools/a.py: not UTF-8"]),
])
def test_size(tmp_path, files, code, has):
    put(tmp_path, dict(budg(B), **files))
    c, o = run(sz, tmp_path)
    assert c == code and all(h in o for h in has), o


def test_files_absent(tmp_path):
    assert (run(sz, tmp_path)[0], run(uni, tmp_path)[0]) == (2, 2)


# expected from: C1-2 part2:100 (case-insensitive, word-bounded, code/comments/strings; factory/data not counted); B20 part9:129,
# 131-132; t-1992 N5 and the Lead's edge (PytestRunner, JiraClient, getJiraIssue, playwrightConfig flagged, pytestish not)
@pytest.mark.parametrize("files, allow, code, has, hasnt", [
    ({"factory/tools/x.py": "# runs PyTest\nr = 'pytestish'\n", "factory/data/d.yaml": "r: pytest\n"}, [], 1,
     "factory/tools/x.py:1", "x.py:2"),
    ({"factory/hooks/h": "a = 'pytest'\n"}, [], 1, "factory/hooks/h:1", "d.yaml"),
    ({"factory/tools/j.py": "def run_pytest(): pass\n"}, [], 1, "j.py:1", None),
    ({"factory/tools/j.py": "x = 'pytest3'\n"}, [], 1, "j.py:1", None),
    *[({"factory/tools/c.py": src}, [], 1, "c.py:1", None)  # t-1992 N5: camelCase steps and an acronym's end
      for src in ("class PytestRunner:", "JiraClient()", "x = getJiraIssue", "'playwrightConfig'", "JIRAClient")],
    ({"factory/tools/c.py": "x = 'pytestish' + 'myjira'\n"}, [], 0, "", "c.py"),
    ({"factory/tools/y.py": "a = 'pytest'\n"}, [row("y")], 0, "", "y.py:"),
    ({"factory/tools/y.py": "a = 'pytest'\n"}, [row("y", reason="")], 1, "reason", None),
    ({"factory/tools/y.py": "a = 'pytest'\n"}, [row("y"), row("z")], 1, "stale: factory/tools/z.py::pytest", "y.py:"),
    ({"factory/tools/y.py": "a = 1\n"}, [row("y")], 2, "found nothing", None),
    ({"factory/tools/y.py": "a = 1\n"}, [row("y"), row("y")], 2, "duplicate", None),
    ({"factory/notes.md": "ok\nzh \u0436\n"}, [], 1, "factory/notes.md:2", None),
    ({"factory/bad.txt": b"\xff\xfe\x00x"}, [], 2, "factory/bad.txt", None),
])
def test_universality(tmp_path, files, allow, code, has, hasnt):
    put(tmp_path, dict(names(allow), **files))
    c, o = run(uni, tmp_path)
    assert c == code and has in o and (hasnt is None or hasnt not in o), o


# expected from: B20 part9:130, 139 (basis drift exit 2, another Python minor exit 3); C1-2 part2:100 (kinds); AR-28 (an empty table)
@pytest.mark.parametrize("data, code, has", [
    ({"basis": dict(uni.basis(), tool="0")}, 2, "basis tool 0 -> 1"),
    ({"basis": dict(uni.basis(), python="9.9")}, 3, "not judged here"),
    ({"basis": {}}, 2, "missing"),
    ({"names": {"runner": []}}, 2, "non-empty list"),
    ({"names": {"cook": ["x"]}}, 2, "outside"),
    ({"names": {}}, 2, "never a pass"),
])
def test_names_file(tmp_path, data, code, has):
    put(tmp_path, {"forge/universality-names.json": json.dumps(dict(json.loads(names()["forge/universality-names.json"]), **data))})
    c, o = run(uni, tmp_path)
    assert c == code and has in o, o


# expected from: B20 part9:131-132 (--update shrinks, never empties, --record unresolved); brief section 4
def test_update(tmp_path):
    put(tmp_path, dict(names([row("y"), row("z")]), **{"factory/tools/y.py": "a = 'pytest'\n"}))
    assert "cannot resolve W-1" in run(uni, tmp_path, "--update", "--record", "W-1")[1]
    assert run(uni, tmp_path, "--update")[0] == 0 and run(uni, tmp_path)[0] == 0
    os.remove(tmp_path / "factory/tools/y.py")
    put(tmp_path, {"factory/tools/z.py": "a = 'pytest'\n"})
    c, o = run(uni, tmp_path, "--update")
    assert c == 1 and "refused" in o


def test_resolved_raise(repo, monkeypatch):
    g, shas, checkout = repo
    checkout(3)
    monkeypatch.setattr(ratchets, "resolve", lambda i, kinds=("word",): None)
    assert run(sz, g, "--base", shas[1])[0] == 0


@pytest.fixture(scope="module")
def uni_repo(tmp_path_factory):
    doc = json.loads(names()["forge/universality-names.json"])
    state = lambda y, **kw: {"forge/universality-names.json": json.dumps(dict(doc, **kw)), "factory/tools/y.py": y}
    clean, held = state("a = 1\n"), state("a = 'pytest'\n", allow=[row("y")])  # each state green but for its raises
    wide = state("a = 1\n", names=dict(doc["names"], runner=["pytest", "jest"]),
                 basis=dict(uni.basis(), roots=uni.basis()["roots"] + ["x"]))
    other = state("a = 1\n", basis=dict(uni.basis(), constants=dict(uni.basis()["constants"], match="x")))
    older = state("a = 1\n", basis=dict(uni.basis(), python="0.0"))  # a value no live interpreter matches (t-1995 P1)
    return world(tmp_path_factory, [("m", clean), ("m", held), ("m", None), ("m", clean),
                                    ("ratchet-raise: universality-names.json clear -- W-1", None), ("m", wide), ("m", clean),
                                    ("m", other), ("m", clean), ("m", older), ("m", clean)])


# expected from: t-1991 M2, t-1992 N4, t-1994 F1 (probe P3), t-1995 P1 (answer section 8) and the brief section 4 (allow row added, allow emptied, name
# removed, a basis change are raises, N13 `clear` and `basis`; until B3 a raise line cannot resolve; no change is green)
@pytest.mark.parametrize("head, base, code, has, hasnt", [
    (1, 0, 1, "allow row added needs", None),
    (2, 1, 0, "", "new:"),
    (3, 2, 1, "universality-names.json::clear allow emptied needs", None),
    (4, 2, 1, "cannot resolve W-1", "needs"),
    (6, 5, 1, "name removed needs", None),
    (6, 5, 1, "names.json::basis basis changed needs", None),
    (8, 7, 1, "names.json::basis basis changed needs", None),
    (10, 9, 0, "", "basis"),  # t-1995 P1: a python-only basis change is not a raise
])
def test_universality_raises(uni_repo, head, base, code, has, hasnt):
    g, shas, checkout = uni_repo
    checkout(head)
    c, o = run(uni, g, "--base", shas[base])
    assert c == code and has in o and (hasnt is None or hasnt not in o), o


# expected from: t-1994 M3 mutant and F2 probe P1 (N15: --update warns about an uncommitted path in scope; the files_of glob
# factory/tools/**/*.py also holds a file directly under factory/tools); the dirty file is restored before the asserts
def test_update_warns(uni_repo):
    g, shas, checkout = uni_repo
    checkout(8)
    with open(os.path.join(g, "factory/tools/y.py"), "rb") as fh:
        kept = fh.read()
    put(g, {"factory/tools/y.py": "a = 2\n"})
    c, o = run(uni, g, "--update")
    said = []
    ratchets.update(g, "", {"allow": []}, "allow", uni.key_of, set(), None, uni.RECORD, ["factory/tools/**/*.py"], said.append)
    put(g, {"factory/tools/y.py": kept})
    assert c == 0 and "uncommitted changes in scope: 1 paths" in o and said and "1 paths" in said[0], (o, said)


# expected from: t-1992 N2 and the brief section 4 (no list file -> empty list; a file not born has no drift, is never written)
def test_no_list_file(tmp_path):
    path, said = str(tmp_path / "absent.json"), []
    data, rows = ratchets.load_list(path, "x", uni.key_of)
    assert (data, rows) == ({"basis": None, "allow": []}, []) and ratchets.check_basis(None, uni.basis(), "d") is None
    assert ratchets.update(str(tmp_path), path, data, "allow", uni.key_of, set(), None, uni.RECORD, ["f"], said.append) == 0
    assert not os.path.exists(path) and said == []


# expected from: t-1991 F1, F4; the brief section 4 (a resolved record opens the road; the dead scanner is exit 2); t-1997
# probe A (the Lead's ruling (2): a bad base, 2, beats an unresolved record) and probe D (X3: universality takes no --list)
def test_doors(tmp_path, monkeypatch):
    put(tmp_path, dict(names([row("y")], dict(uni.basis(), python="9.9")), **{"factory/tools/y.py": "a = 'pytest'\n"}))
    assert [run(uni, tmp_path, *a)[0] for a in (["--base", "nope"], ["--update", "--record", "D-1", "--base", "nope"])] == [2, 2]
    with pytest.raises(SystemExit, match="2"):
        run(uni, tmp_path, "--list")
    put(tmp_path, names([row("z")]))
    allow = lambda: json.load(open(tmp_path / "forge/universality-names.json"))["allow"]
    assert run(uni, tmp_path, "--update", "--record", "W-1")[0] == 1 and allow() == [row("z")]
    monkeypatch.setattr(ratchets, "resolve", lambda i, kinds=("word",): None)
    run(uni, tmp_path, "--update", "--record", "W-1")
    assert allow() == []
    with pytest.raises(ratchets.Refuse, match="none of the 2"):
        ratchets.judge_list([(("f", "t"), "")], [], str, 0, 2)
