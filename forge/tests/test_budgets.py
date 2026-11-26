# card: C1-2
"""Data-joint tests of C1-2: budgets.json and universality-names.json read by size_ratchet.py and universality.py (in-process
on temp trees). Git fixtures only for raises: one repository of 5 commits. `expected from:` names each table's source."""
import contextlib
import io
import json
import os
import subprocess
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
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
        {"basis": basis or uni.basis(), "names": {"runner": ["pytest"]}, "allow": list(allow)})}


def run(mod, root, *args):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = mod.main(["--root", str(root)] + list(args))
    return code, buf.getvalue()


def row(f, **kw):
    return dict({"file": "factory/tools/%s.py" % f, "token": "pytest", "reason": "r"}, **kw)


def ceil(**kw):
    return {k: dict(v, ceiling=kw.get(k, v["ceiling"])) if v else v for k, v in B.items()}


@pytest.fixture(scope="module")
def repo(tmp_path_factory):
    g = str(tmp_path_factory.mktemp("g"))
    cmd = ["git", "-C", g, "-c", "user.name=t", "-c", "user.email=t@t"]
    sh = lambda *a: subprocess.run(cmd + list(a), capture_output=True).stdout.decode().strip()
    sh("init", "-q")
    shas = []
    for msg, rows in (("empty", None), ("budgets", B), ("raise", ceil(factory_code=4)),
                      ("ratchet-raise: budgets.json factory_code -- W-1", ceil(factory_code=4)),
                      ("budget-raise: crap_limit -- x", ceil(factory_code=2, crap_limit=21))):
        if rows is not None:
            put(g, budg(rows))
        sh("add", "-A")
        sh("commit", "-q", "--allow-empty", "--no-verify", "-m", msg)
        shas.append(sh("rev-parse", "HEAD"))
    return g, shas, lambda i: sh("checkout", "-q", shas[i])


# expected from: B20 part9:127, 132, 139; C1-2 part2:100; F245; the owner's word 26.11 about 11:01 (crap_limit)
@pytest.mark.parametrize("head, base, env, code, has, hasnt", [
    (2, 1, 0, 1, "new: forge/budgets.json::factory_code", None),
    (2, 1, 1, 1, "new: forge/budgets.json::factory_code", None),
    (3, 1, 0, 1, "cannot resolve W-1", None),
    (3, 0, 0, 0, "born", None),
    (4, 3, 0, 1, "new: forge/budgets.json::crap_limit", "::factory_code"),
    (4, 0, 0, 0, "born", "new:"),
    (4, None, 0, 0, "raises not judged: no base", "new:"),
    (4, "nope", 0, 2, "not a commit", None),
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
])
def test_size(tmp_path, files, code, has):
    put(tmp_path, dict(budg(B), **files))
    c, o = run(sz, tmp_path)
    assert c == code and all(h in o for h in has), o


def test_files_absent(tmp_path):
    assert (run(sz, tmp_path)[0], run(uni, tmp_path)[0]) == (2, 2)


# expected from: C1-2 part2:100 (case-insensitive, word-bounded, code/comments/strings; factory/data not counted); B20 part9:129, 131-132
@pytest.mark.parametrize("files, allow, code, has, hasnt", [
    ({"factory/tools/x.py": "# runs PyTest\nr = 'pytestish'\n", "factory/data/d.yaml": "r: pytest\n"}, [], 1,
     "factory/tools/x.py:1", "x.py:2"),
    ({"factory/hooks/h": "a = 'pytest'\n"}, [], 1, "factory/hooks/h:1", "d.yaml"),
    ({"factory/tools/y.py": "a = 'pytest'\n"}, [row("y")], 0, "", "y.py:"),
    ({"factory/tools/y.py": "a = 'pytest'\n"}, [row("y", reason="")], 1, "reason", None),
    ({"factory/tools/y.py": "a = 'pytest'\n"}, [row("y"), row("z")], 1, "stale: factory/tools/z.py::pytest", "y.py:"),
    ({"factory/tools/y.py": "a = 1\n"}, [row("y")], 2, "found nothing", None),
    ({"factory/tools/y.py": "a = 1\n"}, [row("y"), row("y")], 2, "duplicate", None),
    ({"factory/notes.md": "ok\nzh ж\n"}, [], 1, "factory/notes.md:2", None),
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
