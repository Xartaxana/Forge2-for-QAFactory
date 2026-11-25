# card: C1-4
"""Tool tests of card C1-4 (journal, dispatch, trim, snapshot). Every run goes through --root <tmp_path>."""
import json
import os
import subprocess
import sys

import pytest

T = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools")


def run(tool, args, root, stdin=b"", env=None):
    e = {k: v for k, v in os.environ.items() if k != "FORGE_SESSION"}
    e.update(env or {})
    r = subprocess.run([sys.executable, "-B", os.path.join(T, tool), "--root", str(root)] + args, input=stdin,
                       capture_output=True, env=e, timeout=60)
    return r.returncode, (r.stdout + r.stderr).decode("utf-8", "replace")


def jw(root, event, note, task="t-1", session="s1"):
    return run("journal.py", ["--event", event, "--note", note, "--session", session] + (["--task", task] if task else []),
               root)


# expected from: card C1-4 and card B2 (the note cap, the closed event list, the session id) and B9 (refuse, ask_owner)
@pytest.mark.parametrize("event,note,task,session,code,word", [
    ("dispatch", "ok", "t-1", "s1", 0, ""),
    ("accept", "x" * 300, "t-1", "s1", 0, ""),
    ("accept", "x" * 301, "t-1", "s1", 2, "301"),
    ("accept", "  ", "t-1", "s1", 2, "empty"),
    ("invented", "n", "t-1", "s1", 2, "ask_owner"),
    ("refuse", "n", None, "s1", 0, ""),
    ("ask_owner", "n", None, "s1", 0, ""),
    ("cut", "n", None, "s1", 2, "task"),
    ("accept", "n", "t-1", "y" * 128, 0, ""),
    ("accept", "n", "t-1", "y" * 129, 2, "session"),
    ("accept", "n", "t-1", "../evil", 2, "session"),
    ("accept", "n", "t-1", "a/b", 2, "session"),
    ("accept", "n", "t-1", "", 2, "session"),
])
def test_journal_write(tmp_path, event, note, task, session, code, word):
    got, out = jw(tmp_path, event, note, task, session)
    assert got == code and word in out
    assert bool(list((tmp_path / "logs" / "journal").glob("*.jsonl"))) == (code == 0)
    if code == 0:
        obj = json.loads((tmp_path / "logs" / "journal" / (session + ".jsonl")).read_text().splitlines()[0])
        assert list(obj) == ["ts", "task", "event", "by", "note"] and obj["ts"].endswith("Z") and obj["by"] == "lead"


# expected from: card C1-4 (the open list, the unparsable line, no journal is unknown)
@pytest.mark.parametrize("rows,tail,code,words", [
    ([], "", 0, ["unknown -- no journal"]),
    ([("dispatch", "t-1")], "", 0, ["t-1"]),
    ([("dispatch", "t-1"), ("accept", "t-1")], "", 0, ["none"]),
    ([("dispatch", "t-1"), ("dispatch", "t-2"), ("return", "t-1")], "", 0, ["t-2"]),
    ([("dispatch", "t-1")], "{broken\n", 1, ["unparsable line 2 in o.jsonl", "incomplete"]),
])
def test_journal_open_and_read(tmp_path, rows, tail, code, words):
    for ev, t in rows:
        jw(tmp_path, ev, "n", t, "o")
    if tail:
        with open(tmp_path / "logs" / "journal" / "o.jsonl", "a") as fh:
            fh.write(tail)
    got, out = run("journal.py", ["open"], tmp_path)
    assert got == code and all(w in out for w in words)
    if tail:
        assert run("journal.py", ["read"], tmp_path)[0] == 1


# expected from: card C1-4 (a lock serialises writers: every line lands whole)
def test_journal_concurrent_writers(tmp_path):
    ps = [subprocess.Popen([sys.executable, "-B", os.path.join(T, "journal.py"), "--root", str(tmp_path), "--event",
                            "accept", "--task", "t", "--note", "w%d" % i, "--session", "r"],
                           stdout=subprocess.DEVNULL) for i in range(8)]
    assert [p.wait(timeout=60) for p in ps] == [0] * 8
    lines = (tmp_path / "logs" / "journal" / "r.jsonl").read_text().splitlines()
    assert sorted(json.loads(x)["note"] for x in lines) == sorted("w%d" % i for i in range(8))


BASE = ["new", "--role", "builder", "--task", "t-9", "--given", "a.md", "--non-goals", "n", "--handoff", "h", "--edges",
        "e", "--dod", "python -B x.py", "--siblings", "none -- s", "--test", "none -- t"]


# expected from: card C1-4 and card B5 (the caps line in both worlds, the header lines, the owns rule)
@pytest.mark.parametrize("caps,owns,code,words", [
    (None, "ok", 0, ["caps: missing -- forge/caps.json (B5)", "DoD: `python -B x.py`"]),
    ([{"role": "builder", "tokens_warn": 1, "tokens_stop": 2, "wall_warn_s": 3, "wall_stop_s": 4}], "ok", 0,
     ["caps: tokens 1/2, wall 3/4 s -- at the cap: hand back done and not done"]),
    ("{bad", "ok", 0, ["caps: missing"]),
    ([{"role": "scout"}], "ok", 0, ["caps: missing"]),
    (None, "rel", 1, ["x.py"]),
    (None, "none", 1, ["missing: owns"]),
])
def test_dispatch_new(tmp_path, caps, owns, code, words):
    if caps is not None:
        (tmp_path / "forge").mkdir()
        (tmp_path / "forge" / "caps.json").write_text(caps if isinstance(caps, str) else json.dumps(caps))
    own = {"ok": [str(tmp_path / "forge" / "tools" / "x.py")], "rel": ["forge/tools/x.py"], "none": []}[owns]
    got, out = run("dispatch.py", BASE + ["--owns"] + own, tmp_path)
    assert got == code and all(w in out for w in words)
    heads = [ln.split(":")[0] for ln in out.splitlines() if ln.split(":")[0] in
             ("task", "role", "caps", "given", "owns", "non-goals", "handoff", "edges", "DoD", "siblings", "test")]
    assert heads == ["task", "role", "caps", "given", "owns", "non-goals", "handoff", "edges", "DoD", "siblings", "test"]


# expected from: card C1-4 (check names each absent line; roles; one-line values)
@pytest.mark.parametrize("args,stdin,code,word", [
    (["check", "-"], "task: t\nrole: critic\ncaps: x\ngiven:\nowns:\nnon-goals: n\nhandoff: h\nedges: e\nDoD: `c`\n"
     "siblings: s\n", 0, "ok"),
    (["check", "-"], "task: t\nrole: critic\ncaps: x\ngiven:\nowns:\nnon-goals: n\nhandoff: h\nedges: e\nDoD: c\n"
     "siblings: s\n", 1, "missing: DoD"),
    (["check", "-"], "task: t\nrole: wizard\n", 2, "designer"),
    (["new", "--role", "wizard"], "", 2, "scout"),
    (BASE[:-2] + ["--test", "a\nb"], "", 2, "--test"),
])
def test_dispatch_check(tmp_path, args, stdin, code, word):
    got, out = run("dispatch.py", args, tmp_path, stdin.encode())
    assert got == code and word in out


# expected from: card C1-4 (trim: at N whole, over N the marker and the last N, keep, replaced bytes, bad N and pattern)
@pytest.mark.parametrize("n,args,stdin,code,first,count,lastline", [
    (1000, [], None, 0, "[trimmed 970 of 1000 lines]", 31, "line 1000"),
    (30, [], None, 0, "line 1", 30, "line 30"),
    (31, [], None, 0, "[trimmed 1 of 31 lines]", 31, "line 31"),
    (1000, ["--keep", "line 17$"], None, 0, "[trimmed 969 of 1000 lines]", 32, "line 1000"),
    (3, ["--last", "2"], b"a\n\xff\xfe\nc\n", 0, "[trimmed 1 of 3 lines; non-UTF-8 bytes replaced]", 3, "c"),
    (2, ["--last", "2"], b"a\nb\xff\n", 0, "[trimmed 0 of 2 lines; non-UTF-8 bytes replaced]", 3, "b�"),
    (1, ["--last", "0"], None, 2, "--last", 1, "--last 0 must be"),
    (1, ["--keep", "("], None, 2, "--keep", 1, ""),
])
def test_trim(tmp_path, n, args, stdin, code, first, count, lastline):
    data = stdin or "".join("line %d\n" % i for i in range(1, n + 1)).encode()
    got, out = run("trim.py", args, tmp_path, data)
    ls = out.splitlines()
    assert got == code and ls[0].startswith(first) and (code == 2 or (len(ls) == count and ls[-1] == lastline))


# expected from: card C1-4 and card B7 (snapshot sections, never refuses, --close prints the carriers rows)
@pytest.mark.parametrize("git,carriers,close,words", [
    (False, None, False, ["no journal lines", "git failed"]),
    (True, None, True, ["forge/carriers.json absent (B7)", "t-2", "o1.jsonl"]),
    (True, [{"carrier": "BOOT.md", "what goes there": "state"}], True, ["state -> BOOT.md"]),
    (True, "{bad", True, ["carriers.json malformed"]),
])
def test_snapshot(tmp_path, git, carriers, close, words):
    if git:
        subprocess.run(["git", "-C", str(tmp_path), "init", "-q"], capture_output=True)
        jw(tmp_path, "dispatch", "n", "t-2", "o1")
    if carriers is not None:
        (tmp_path / "forge").mkdir()
        (tmp_path / "forge" / "carriers.json").write_text(carriers if isinstance(carriers, str) else json.dumps(carriers))
    got, out = run("snapshot.py", ["--close"] if close else [], tmp_path)
    snaps = list((tmp_path / "logs" / "journal" / "snapshots").glob("*.md"))
    assert got == 0 and len(snaps) == 1 and all(w in out + snaps[0].read_text() for w in words)
