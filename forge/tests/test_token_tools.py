# card: C1-4
"""Tool tests of card C1-4 (journal, dispatch, trim, snapshot). Every run goes through --root <tmp_path>."""
import json
import os
import re
import subprocess
import sys
import time

import pytest

T = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools")
NAMES = ("task", "role", "caps", "given", "owns", "non-goals", "handoff", "edges", "DoD", "siblings", "test")


def run(tool, args, root, stdin=b"", env=None):
    e = {k: v for k, v in os.environ.items() if k != "FORGE_SESSION"}
    e.update(env or {})
    r = subprocess.run([sys.executable, "-B", os.path.join(T, tool), "--root", str(root)] + args, input=stdin,
                       capture_output=True, env=e, timeout=60)
    return r.returncode, (r.stdout + r.stderr).decode("utf-8", "replace")


def jw(root, event, note, task="t-1", session="s1"):
    return run("journal.py", ["--event", event, "--note", note, "--session", session] + (["--task", task] if task else []),
               root)


def put(root, rel, data):
    """Write bytes to root/rel; data None makes a folder of that name."""
    p = root / rel
    if data is None:
        p.mkdir(parents=True)
    else:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)


# expected from: card C1-4 and card B2 (the note cap, the closed event list, the session id) and B7, B9 (session_end,
# refuse, ask_owner); an ASCII-only session id is B2's pattern; a note with a newline is one line in the file
@pytest.mark.parametrize("event,note,task,session,code,word", [
    ("dispatch", "ok", "t-1", "s1", 0, ""),
    ("accept", "x" * 300, "t-1", "s1", 0, ""),
    ("accept", "x" * 301, "t-1", "s1", 2, "301"),
    ("accept", "  ", "t-1", "s1", 2, "empty"),
    ("invented", "n", "t-1", "s1", 2, "ask_owner"),
    ("refuse", "n", None, "s1", 0, ""),
    ("ask_owner", "n", None, "s1", 0, ""),
    ("session_end", "n", None, "s1", 0, ""),
    ("cut", "n", None, "s1", 2, "task"),
    ("accept", "a\nb", "t-1", "s1", 0, ""),
    ("accept", "n", "t-1", "y" * 128, 0, ""),
    ("accept", "n", "t-1", "y" * 129, 2, "session"),
    ("accept", "n", "t-1", "../evil", 2, "session"),
    ("accept", "n", "t-1", "a/b", 2, "session"),
    ("accept", "n", "t-1", "s\u00e9", 2, "session"),
    ("accept", "n", "t-1", "", 2, "session"),
])
def test_journal_write(tmp_path, event, note, task, session, code, word):
    got, out = jw(tmp_path, event, note, task, session)
    assert got == code and word in out
    assert bool(list((tmp_path / "logs" / "journal").glob("*.jsonl"))) == (code == 0)
    if code == 0:
        lines = (tmp_path / "logs" / "journal" / (session + ".jsonl")).read_text().splitlines()
        obj = json.loads(lines[0])
        assert len(lines) == 1 and list(obj) == ["ts", "task", "event", "by", "note"]
        assert obj["ts"].endswith("Z") and obj["by"] == "lead" and obj["note"] == note


# expected from: card C1-4 (the open list, the unparsable line, no journal is unknown)
@pytest.mark.parametrize("rows,tail,code,words", [
    ([], "", 0, ["unknown -- no journal"]),
    ([("dispatch", "t-1")], "", 0, ["t-1"]),
    ([("dispatch", "t-1"), ("accept", "t-1")], "", 0, ["none"]),
    ([("dispatch", "t-1"), ("dispatch", "t-2"), ("return", "t-1")], "", 0, ["t-2"]),
    ([("dispatch", "t-1")], "{broken\n", 1, ["unparsable line 2 in o.jsonl", "incomplete"]),
])
def test_journal_open_and_read(tmp_path, rows, tail, code, words):
    if tail:  # the one row whose journal is written by the tool: the write-then-open seam
        for ev, t in rows:
            jw(tmp_path, ev, "n", t, "o")
    elif rows:  # laid down as bytes in the tool's own line form; the write road has its own test
        put(tmp_path, "logs/journal/o.jsonl", "".join(
            json.dumps({"ts": "2026-11-25T10:00:0%dZ" % i, "task": t, "event": ev, "by": "lead", "note": "n"}) + "\n"
            for i, (ev, t) in enumerate(rows)).encode("utf-8"))
    if tail:
        with open(tmp_path / "logs" / "journal" / "o.jsonl", "a") as fh:
            fh.write(tail)
    got, out = run("journal.py", ["open"], tmp_path)
    assert got == code and all(w in out for w in words)
    if tail:
        assert run("journal.py", ["read"], tmp_path)[0] == 1


# expected from: the verdict t-1944 F1, F3 (a killed writer's tail, odd content and an unopenable file are named, never
# a traceback) and the dispatch's lock edge (a lock FILE nobody holds neither blocks nor waits)
@pytest.mark.parametrize("files,write,code,words", [
    ({"k.jsonl": b'{"ts": "2026-11-25T10:00:00Z", "task": "t-1", "ev'}, True, 1,
     ["unparsable line 1 in k.jsonl", "t-2", "incomplete"]),
    ({"o.jsonl": b'{"ts": "x", "task": ["t"], "event": "dispatch"}\n'}, False, 1,
     ["unparsable line 1 in o.jsonl", "incomplete"]),
    ({"o.jsonl": b'[1]\n'}, False, 1, ["unparsable line 1 in o.jsonl"]),
    ({"x.jsonl": None, "o.jsonl": b""}, False, 1, ["unreadable file x.jsonl", "incomplete"]),
    ({".lock": b"left by a killed writer"}, True, 0, ["t-2"]),
])
def test_journal_odd_files(tmp_path, files, write, code, words):
    for rel, data in files.items():
        put(tmp_path, "logs/journal/" + rel, data)
    t0 = time.time()
    if write:
        assert jw(tmp_path, "dispatch", "n", "t-2", "k")[0] == 0 and time.time() - t0 < 5
    got, out = run("journal.py", ["open"], tmp_path)
    assert got == code and "Traceback" not in out and all(w in out for w in words)
    assert run("journal.py", ["read"], tmp_path)[0] == code


# expected from: card C1-4 (read prints in ts order across files; --last N keeps the last N)
@pytest.mark.parametrize("args,want", [([], ["y", "x"]), (["--last", "1"], ["x"]), (["--session", "a"], ["x"])])
def test_journal_read_order(tmp_path, args, want):
    for f, ts, note in (("a", "2026-11-25T10:00:02Z", "x"), ("b", "2026-11-25T10:00:01Z", "y")):
        put(tmp_path, "logs/journal/%s.jsonl" % f, json.dumps({"ts": ts, "task": "", "event": "refuse", "note": note})
            .encode() + b"\n")
    got, out = run("journal.py", ["read"] + args, tmp_path)
    assert got == 0 and [json.loads(x)["note"] for x in out.splitlines()] == want


# expected from: card B7 and the dispatch of C1-4 (FORGE_SESSION names the file; else the newest file but git-hooks;
# else s-<UTC stamp>)
@pytest.mark.parametrize("env,files,pattern", [
    ({"FORGE_SESSION": "envs"}, {}, r"envs\.jsonl"),
    ({}, {"mine.jsonl": 100, "git-hooks.jsonl": 200}, r"mine\.jsonl"),
    ({}, {}, r"s-\d{8}T\d{6}Z\.jsonl"),
])
def test_journal_session_pick(tmp_path, env, files, pattern):
    for f, mtime in files.items():
        put(tmp_path, "logs/journal/" + f, b"")
        os.utime(tmp_path / "logs" / "journal" / f, (mtime, mtime))
    got, out = run("journal.py", ["--event", "refuse", "--note", "n"], tmp_path, env=env)
    assert got == 0 and re.search(pattern + r"\s", out.splitlines()[0] + "\n")


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


# expected from: card C1-4 and card B5 (the caps line in both worlds, the header lines, the owns rule) and R11-f (an
# owns path with a space is written in backticks)
@pytest.mark.parametrize("caps,owns,code,words", [
    (None, "ok", 0, ["caps: missing -- forge/caps.json (B5)", "DoD: `python -B x.py`"]),
    ([{"role": "builder", "tokens_warn": 1, "tokens_stop": 2, "wall_warn_s": 3, "wall_stop_s": 4}], "ok", 0,
     ["caps: tokens 1/2, wall 3/4 s -- at the cap: hand back done and not done"]),
    ("{bad", "ok", 0, ["caps: missing"]),
    ([{"role": "scout"}], "ok", 0, ["caps: missing"]),
    (None, "rel", 1, ["owns path not absolute or not inside the root: forge/tools/x.py"]),
    (None, "outside", 1, ["owns path not absolute or not inside the root"]),
    (None, "spaced", 0, ["`%s/forge/a b/c.py`"]),
    (None, "none", 1, ["missing: owns"]),
])
def test_dispatch_new(tmp_path, caps, owns, code, words):
    if caps is not None:
        (tmp_path / "forge").mkdir()
        (tmp_path / "forge" / "caps.json").write_text(caps if isinstance(caps, str) else json.dumps(caps))
    root = str(tmp_path).replace("\\", "/")
    own = {"ok": [root + "/forge/tools/x.py"], "rel": ["forge/tools/x.py"], "none": [],
           "outside": [root + "/../x.py"], "spaced": [root + "/forge/a b/c.py"]}[owns]
    got, out = run("dispatch.py", BASE + ["--owns"] + own, tmp_path)
    assert got == code and all((w % root if "%s" in w else w) in out for w in words)
    heads = [ln.split(":")[0] for ln in out.splitlines() if ln.split(":")[0] in NAMES]
    assert heads == list(NAMES)


def full(tmp_path):
    return ("task: t\nrole: builder\ncaps: x\ngiven:\na.md\nowns:\n%s/a.py\nnon-goals: n\nhandoff: h\nedges: e\n"
            "DoD: `c`\nsiblings: s\ntest: t\n" % str(tmp_path).replace("\\", "/"))


# expected from: card C1-4 and R11-f (check names each absent line; roles; one-line values; header lines are outside
# fences and quotes; a key-shaped line ends a path block; a path with spaces is in backticks)
@pytest.mark.parametrize("edit,code,word", [
    (lambda f: f, 0, "ok"),
    (lambda f: f.replace("`c`", "c"), 1, "missing: DoD"),
    (lambda f: f.replace("role: builder", "role: wizard"), 2, "designer"),
    (lambda f: f.replace("DoD: `c`\n", "") + "\n```\nDoD: `example`\n```\n", 1, "missing: DoD"),
    (lambda f: f.replace("DoD: `c`\n", "") + "\n~~~\nDoD: `example`\n~~~\n", 1, "missing: DoD"),
    (lambda f: f + "\n```\nowns:\nforge/x.py\n```\n", 0, "ok"),
    (lambda f: f + "\n> owns:\n", 0, "ok"),
    (lambda f: f + "\nrole: critic\n", 1, "repeated: role"),
    (lambda f: f.replace("a.py\n", "a.py\nfeature: F19\n"), 0, "ok"),
    (lambda f: f.replace("/a.py", "/../x.py"), 1, "not inside"),
    (lambda f: f.replace("/a.py", "/a b/c.py").replace("\nowns:\n", "\nowns:\n`").replace("c.py\n", "c.py`\n"), 0, "ok"),
] + [(lambda f, n=n: re.sub(r"(?m)^%s:.*\n" % n, "", f), 1, "missing: " + n) for n in NAMES if n not in ("owns", "given")]
  + [(lambda f, n=n: f.replace("\n%s:\n" % n, "\n"), 1, "missing: " + n) for n in ("owns", "given")])
def test_dispatch_check(tmp_path, edit, code, word):
    got, out = run("dispatch.py", ["check", "-"], tmp_path, edit(full(tmp_path)).encode())
    assert got == code and word in out


# expected from: card C1-4 (new refuses a newline and an unknown role; check of an unreadable file is no header defect)
# and the verdict t-1944 F7 (an empty --test prints no line for a non-builder, stays missing for a builder)
@pytest.mark.parametrize("args,code,word,absent", [
    (["new", "--role", "wizard"], 2, "scout", ""),
    (BASE[:-2] + ["--test", "a\nb"], 2, "--test", ""),
    (["check", "NO-SUCH-FILE"], 2, "cannot read", "Traceback"),
    (["new", "--role", "critic", "--test", "", "--task", "t", "--given", "a", "--non-goals", "n", "--handoff", "h",
      "--edges", "e", "--dod", "c", "--siblings", "s"], 0, "role: critic", "test:"),
    (BASE[:-2] + ["--test", ""], 1, "missing: test", ""),
])
def test_dispatch_other(tmp_path, args, code, word, absent):
    got, out = run("dispatch.py", args, tmp_path)
    assert got == code and word in out and not (absent and absent in out)


CRLF = "".join("line %d\r\n" % i for i in range(1, 72)).replace("line 41\r\n", "FAILED x\r\n").encode()


# expected from: card C1-4 (trim: at N whole, over N the marker and the last N, keep, replaced bytes, bad N and pattern)
# and the verdict t-1944 F8 (a $-anchored pattern matches a CRLF line)
@pytest.mark.parametrize("n,args,stdin,code,first,count,lastline", [
    (1000, [], None, 0, "[trimmed 970 of 1000 lines]", 31, "line 1000"),
    (30, [], None, 0, "line 1", 30, "line 30"),
    (31, [], None, 0, "[trimmed 1 of 31 lines]", 31, "line 31"),
    (1000, ["--keep", "line 17$"], None, 0, "[trimmed 969 of 1000 lines]", 32, "line 1000"),
    (71, ["--keep", "FAILED x$"], CRLF, 0, "[trimmed 40 of 71 lines]", 32, "line 71"),
    (3, ["--last", "2"], b"a\n\xff\xfe\nc\n", 0, "[trimmed 1 of 3 lines; non-UTF-8 bytes replaced]", 3, "c"),
    (2, ["--last", "2"], b"a\nb\xff\n", 0, "[trimmed 0 of 2 lines; non-UTF-8 bytes replaced]", 3, "b\ufffd"),
    (1, ["--last", "0"], None, 2, "--last must be at least 1, got 0", 1, ""),
    (1, ["--keep", "("], None, 2, "--keep", 1, ""),
])
def test_trim(tmp_path, n, args, stdin, code, first, count, lastline):
    data = stdin or "".join("line %d\n" % i for i in range(1, n + 1)).encode()
    got, out = run("trim.py", args, tmp_path, data)
    ls = out.splitlines()
    assert got == code and ls[0].startswith(first) and (code == 2 or (len(ls) == count and ls[-1] == lastline))


# expected from: card C1-4 and card B7 (snapshot sections, never refuses, --close prints the carriers rows) and the
# verdict t-1944 F10 (a journal it cannot read is named, the snapshot is still written), C1-4 (200 lines cut with a marker)
@pytest.mark.parametrize("git,carriers,close,extra,words", [
    (False, None, False, None, ["no journal lines", "git failed"]),
    (True, None, True, "journal", ["forge/carriers.json absent (B7)", "t-2", "git status"]),
    (True, [{"carrier": "BOOT.md", "what goes there": "state"}], True, None, ["state -> BOOT.md"]),
    (True, "{bad", True, None, ["carriers.json malformed"]),
    (True, "real", True, None, []),  # K2 (B7): the repository's own forge/carriers.json, every row printed
    (True, None, False, "many", ["no journal lines", "[cut: 200 of 205 lines shown]"]),
    (False, None, False, "odd", ["unreadable file x.jsonl", "incomplete"]),
])
def test_snapshot(tmp_path, git, carriers, close, extra, words):
    if git:
        subprocess.run(["git", "-C", str(tmp_path), "init", "-q"], capture_output=True)
    if extra == "journal":
        jw(tmp_path, "dispatch", "n", "t-2", "o1")
    for i in range(205 if extra == "many" else 0):
        put(tmp_path, "%d.txt" % i, b"")  # top-level: one status line each in every untracked mode
    if extra == "odd":
        put(tmp_path, "logs/journal/x.jsonl", None)
    if carriers == "real":
        with open(os.path.join(os.path.dirname(T), "carriers.json"), encoding="utf-8") as fh:
            rows = json.load(fh)
        assert rows and all(set(r) == {"carrier", "what goes there"} for r in rows)
        carriers, words = rows, ["%s -> %s" % (r["what goes there"], r["carrier"]) for r in rows]
    if carriers is not None:
        (tmp_path / "forge").mkdir()
        (tmp_path / "forge" / "carriers.json").write_text(carriers if isinstance(carriers, str) else json.dumps(carriers))
    got, out = run("snapshot.py", ["--close"] if close else [], tmp_path,
                   env={"GIT_CEILING_DIRECTORIES": str(tmp_path.parent)})
    snaps = list((tmp_path / "logs" / "journal" / "snapshots").glob("*.md"))
    assert got == 0 and len(snaps) == 1 and "Traceback" not in out
    assert all(w in out + snaps[0].read_text() for w in words)
