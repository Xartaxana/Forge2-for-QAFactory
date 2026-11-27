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


def jw(root, event, note, task="t-1", session="s1", by="lead"):
    return run("journal.py", ["--event", event, "--note", note, "--session", session] + (["--task", task] if task else [])
               + (["--by", by] if by else []), root)


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
    ("decomposable", "split: a, b", None, "s1", 0, ""),  # plan S9
    ("decomposable", " ", None, "s1", 2, "empty"),
    ("dispatch_skipped", "designer: a narrow node", None, "s1", 0, ""),  # t-2059 B4
    ("dispatch_skipped", " ", None, "s1", 2, "empty"),
    ("dispatch_skipped", "a narrow node", None, "s1", 2, "<agent>: <reason>"),  # t-2061: the note form
    ("dispatch_skipped", "designer:  ", None, "s1", 2, "<agent>: <reason>"),
    ("dispatch_skipped", "Designer: x", None, "s1", 2, "<agent>: <reason>"),
    ("escalated", "architect: beyond my level", "t-1", "s1", 0, ""),  # old rule 1047
    ("escalated", "beyond my level", "t-1", "s1", 2, "<agent>: <reason>"),
    ("escalated", "lead tier: beyond my level", "t-1", "s1", 2, "<agent>: <reason>"),
    ("escalated", " ", "t-1", "s1", 2, "empty"),
    ("escalated", "n", None, "s1", 2, "task"),
    ("lead_degraded", "builder: lead model refused", None, "s1", 0, ""),  # old rules 1141-1145 (t-2066)
    ("lead_degraded", "lead model refused", None, "s1", 2, "<agent>: <reason>"),
    ("lead_restored", "lead: window accepted", None, "s1", 0, ""),
    ("lead_restored", "window accepted", None, "s1", 2, "<agent>: <reason>"),
    ("cut", "n", None, "s1", 2, "task"),
    ("accept", "a\nb", "t-1", "s1", 0, ""),
    ("accept", "n", "t-1", "y" * 128, 0, ""),
    ("accept", "n", "t-1", "y" * 129, 2, "session"),
    ("accept", "n", "t-1", "../evil", 2, "session"),
    ("accept", "n", "t-1", "a/b", 2, "session"),
    ("accept", "n", "t-1", "s\u00e9", 2, "session"),
    ("accept", "n", "t-1", "", 2, "session"),
    ("defect_found", "builder: the witness missed a branch", "t-1", "s1", 0, ""),  # t-2071 F3, dispatch t-2077 E3
    ("defect_found", "builder: x", None, "s1", 2, "task"),
    ("defect_found", "x", "t-1", "s1", 2, "<agent>: <reason>"),  # t-2081 F9: the note form is refused for defect_found
    ("calibrated", "weekly reading through 2026-11-26", None, "s1", 0, ""),
    ("accept", "n", "t-1", "s1", 2, "--by"),  # t-2071 F4: an accept naming no acceptor is refused, never read as lead
])
def test_journal_write(tmp_path, event, note, task, session, code, word):
    got, out = jw(tmp_path, event, note, task, session, by=None if word == "--by" else "lead")
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
    ([("dispatch", "t-1"), ("dispatch", "t-2"), ("return", "t-1")], "", 0, ["t-1 RESULT PENDING", "t-2"]),
    # the Lead's decision t-2101 on FR-1127 (a return never closes a dispatch); "!" = must not appear
    ([("dispatch", "t-1"), ("return", "t-1"), ("accept", "t-1")], "", 0, ["none", "!PENDING"]),
    ([("dispatch", "t-1"), ("return", "t-1"), ("reject", "t-1")], "", 0, ["none", "!PENDING"]),
    ([("dispatch", "t-1"), ("return", "t-1"), ("dispatch", "t-1")], "", 0, ["t-1", "!PENDING"]),
    ([("dispatch", "t-1"), ("return", "t-1"), ("return", "t-1")], "", 0, ["t-1 RESULT PENDING"]),
    ([("return", "t-1")], "", 0, ["none"]),  # an orphan return opens nothing
    ([("dispatch", "t-1"), ("accept", "t-1"), ("return", "t-1")], "", 0, ["none", "!PENDING"]),  # a late return: still closed
    ([("dispatch", "t-1"), ("defect_found", "t-1")], "", 0, ["t-1"]),  # t-2081 M3: defect_found never closes a task
    ([("dispatch", "t-1")], "{broken\n", 1, ["unparsable line 2 in o.jsonl", "incomplete"]),
    ([("dispatch", "t-1"), ("return", "t-1")], "{broken\n", 1, ["t-1 RESULT PENDING", "incomplete"]),
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
    assert got == code and all((w[1:] not in out) if w[0] == "!" else (w in out) for w in words)
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
                            "accept", "--task", "t", "--by", "lead", "--note", "w%d" % i, "--session", "r"],
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
    ([{"role": "scout", "tokens_warn": 5, "tokens_stop": 9, "wall_warn_s": None, "wall_stop_s": None}], "ok", 0,
     ["caps: tokens 5/9, wall none/none s -- at the cap: hand back done and not done; role unknown -- strictest row"]),
    ([{"role": "main", "tokens_warn": 5, "tokens_stop": None, "wall_warn_s": None, "wall_stop_s": None}], "ok", 0,
     ["caps: missing -- forge/caps.json (B5)"]),  # t-2032 N3 P3b: no worker row, as the hook (P3: the builder row above)
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


@pytest.mark.parametrize("src", [None, "def (:\n"])
def test_dispatch_caps_hook_not_loadable(tmp_path, monkeypatch, src):  # t-2032 N6: absent or a SyntaxError, the cause named
    monkeypatch.syspath_prepend(T)
    import dispatch
    if src:
        (tmp_path / "budget.py").write_text(src)
    monkeypatch.setattr(dispatch, "BUDGET", str(tmp_path / "budget.py"))
    assert dispatch.caps_line(str(tmp_path), "builder") == "caps: missing -- forge/hooks/budget.py not loadable (B5)"


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
    (True, None, True, "journal", ["forge/carriers.json absent (B7)", "t-2 (result pending)", "git status"]),
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
        jw(tmp_path, "return", "n", "t-2", "o1")
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


def jl(**kw):
    return json.dumps(dict({"task": "", "by": "lead", "note": "n"}, **kw)) + "\n"


def retro_fixture(root, git=True):
    """s1 is the session under test (window 10:00:00..10:00:19); s0 is an earlier file; ts are the hand-set minute marks."""
    rows = [("dispatch", "t-1", "role:builder go"), ("dispatch", "t-2", "role:builder go"), ("dispatch", "t-3", "role:lead go"),
            ("reject", "t-1", ""), ("reject", "t-1", ""), ("return", "t-2", ""), ("accept", "t-3", ""),
            ("cut", "t-1", "role:builder cut"), ("cut", "t-1", "role:builder cut"), ("cap_warning", "t-1", "role:lead cap"),
            ("hook_failed", "", ""), ("refuse", "", "foreign_write: a"), ("refuse", "", "foreign_write: b"),
            ("refuse", "", "budget: c"), ("ask_owner", "", "q:alpha one"), ("ask_owner", "", "q:beta two"),
            ("ask_owner", "", "q:alpha again"), ("session_end", "", "unseen: nothing"),
            ("dispatch", "t-4", "no token"), ("dispatch", "t-5", "role: spaced")]  # by is the Lead on every line: the role is the note's
    body = "".join(jl(ts="2026-11-20T10:00:%02dZ" % i, event=e, task=t, note=n or "n") for i, (e, t, n) in enumerate(rows))
    put(root, "logs/journal/s1.jsonl", body.encode())
    put(root, "logs/journal/s0.jsonl", (jl(ts="2026-11-19T09:00:00Z", event="ask_owner", note="q:beta old") +
                                        jl(ts="2026-11-19T09:00:01Z", event="dispatch", task="t-0")).encode())
    if git:
        put(root, "logs/journal/git-hooks.jsonl", (
            jl(ts="2026-11-20T09:59:59Z", event="refuse", note="pre-commit: before") +
            jl(ts="2026-11-20T10:00:05Z", event="refuse", note="pre-commit: x") +
            jl(ts="2026-11-20T10:00:09Z", event="refuse", note="pre-commit: y") +
            jl(ts="2026-11-21T10:00:00Z", event="refuse", note="pre-push: z")).encode())


HAND = ["counts: ok", "dispatch: ?=2 builder=2 lead=1", "accept: 1", "reject: 2", "return: 1", "retried tasks: 1",
        "cut: builder=2", "cap_warning: lead=1", "hook_failed: 1", "refuse: budget=1 foreign_write=2",
        "refuse (git hooks): pre-commit=2", "ask_owner: 3", "ask_owner repeats: 2", "  task t-1: 2"]


def block_of(root, session="s1"):
    lines = (root / "logs" / "retro" / (session + ".md")).read_text().split("\n")
    return lines[lines.index("<!-- retro:counts:begin -->") + 1:lines.index("<!-- retro:counts:end -->")]


# expected from: the verdict t-2101 F2 (a return is the worker's stop, never an attempt end: dispatch, return, reject is one
# attempt, not a retried task); control: two rejects are retried
@pytest.mark.parametrize("evs,want", [(["dispatch", "return", "reject"], "retried tasks: 0"),
                                      (["dispatch", "reject", "dispatch", "reject"], "retried tasks: 1")])
def test_retro_return_not_attempt(tmp_path, evs, want):
    put(tmp_path, "logs/journal/s1.jsonl", "".join(
        jl(ts="2026-11-20T10:00:%02dZ" % i, event=e, task="t-1") for i, e in enumerate(evs)).encode())
    assert run("retro.py", ["write", "s1"], tmp_path)[0] == 0 and want in block_of(tmp_path)


# expected from: card B9 K1, K5, K6 and the edge list; HAND is counted by hand from retro_fixture's rows (the first and
# third git-hooks lines are outside the window; the beta slug repeats an earlier file's, the alpha slug its own)
@pytest.mark.parametrize("mode", ["base", "stray", "twice"])
def test_retro_counts(tmp_path, mode):
    retro_fixture(tmp_path)
    if mode == "stray":
        put(tmp_path, "logs/stray.jsonl", jl(ts="2026-11-20T10:00:03Z", event="refuse", note="x: y").encode())
        put(tmp_path, "logs/journal/notes.txt", jl(ts="2026-11-20T10:00:03Z", event="accept", task="t-9").encode())
    got, out = run("retro.py", ["write", "s1"], tmp_path)
    assert got == 0 and block_of(tmp_path) == HAND and "missing: s0" in out
    text = (tmp_path / "logs" / "retro" / "s1.md").read_text()
    assert [text.count("\nQ%d " % i) for i in range(1, 6)] == [1] * 5 and "refuse: \n" in text
    if mode == "twice":
        (tmp_path / "logs" / "retro" / "s1.md").write_bytes(text.replace("refuse: \n", "refuse: right, hook x\n").encode())
        with open(tmp_path / "logs" / "journal" / "s1.jsonl", "a") as fh:
            fh.write(jl(ts="2026-11-20T10:00:30Z", event="accept", task="t-4"))
        got, _ = run("retro.py", ["write", "s1"], tmp_path)
        again = (tmp_path / "logs" / "retro" / "s1.md").read_text()
        assert got == 0 and "accept: 2" in block_of(tmp_path) and "refuse: right, hook x\n" in again
        assert again.count("\nQ1 ") == 1
        labels = [l.split(":")[0] for l in again.split("## REASONS\n")[1].split("## QUESTIONS")[0].splitlines()]
        assert len(labels) == len(set(labels))  # a refresh adds a label only when it has no reason line yet


# expected from: card B9 edges: unknown, incomplete, none journaled, zero session, cut with totals kept, refused input
@pytest.mark.parametrize("mode,session,code,words", [
    ("none", "s1", 0, ["counts: unknown -- no journal"]),
    ("bad", "s1", 0, ["counts: incomplete", "unparsable line 2 in s1.jsonl", "accept: 2"]),
    ("nogit", "s1", 0, ["refuse (git hooks): none journaled", "refuse: budget=1 foreign_write=2"]),
    ("zero", "s1", 0, ["nothing: <why>", "dispatch: 0"]),
    ("many", "s1", 0, ["retried tasks: 30", "  [cut: %d of 30 detail lines]" % (30 - (38 - 13) + 1), "accept: 0"]),
    ("nowin", "s1", 0, ["counts: incomplete", "  no window: no own line parsable", "missing: unknown"]),  # t-2024 N3, t-2031
    ("base", "s2", 2, ["no journal lines of session s2"]),
    ("base", "../x", 2, ["refused"]),
    ("base", "git-hooks", 2, ["refused"]),
    ("owndir", "s1", 2, ["refused: unreadable file s1.jsonl"]),  # t-2029 F2: unreadable, not "no journal lines"
])
def test_retro_edges(tmp_path, mode, session, code, words):
    if mode in ("base", "nogit"):
        retro_fixture(tmp_path, git=mode == "base")
    if mode == "owndir":
        put(tmp_path, "logs/journal/s1.jsonl", None)  # a folder: open() fails on every OS, load names it
    if mode == "bad":
        put(tmp_path, "logs/journal/s1.jsonl", (jl(ts="2026-11-20T10:00:00Z", event="accept", task="t-1") + "{oops\n" +
                                                jl(ts="2026-11-20T10:00:01Z", event="accept", task="t-2")).encode())  # dated
    if mode == "zero":
        put(tmp_path, "logs/journal/s1.jsonl", jl(ts="2026-11-20T10:00:00Z", event="session_end").encode())
    if mode == "nowin":
        retro_fixture(tmp_path)
        put(tmp_path, "logs/journal/s1.jsonl", b"{oops\n")
    if mode == "many":
        put(tmp_path, "logs/journal/s1.jsonl", "".join(jl(ts="2026-11-20T10:%02d:00Z" % (i % 30), event="reject", task="t-%d" % (i % 30))
                                                      for i in range(60)).encode())
    got, out = run("retro.py", ["write", session], tmp_path)
    f = tmp_path / "logs" / "retro" / (session + ".md")
    assert got == code and all(w in out + (f.read_text() if f.exists() else "") for w in words)
    assert len(out.splitlines()) <= 40 and (code == 2) == (not f.exists())


# expected from: card B9 K2, K3 and the weekly reading; sums are the hand counts of retro_fixture's s0 plus s1
def test_retro_check_sum_missing(tmp_path):
    retro_fixture(tmp_path)
    f = tmp_path / "logs" / "retro" / "s1.md"
    assert run("retro.py", ["missing"], tmp_path)[1].split() == ["missing:", "2", "s0", "s1"]
    run("retro.py", ["write", "s1"], tmp_path)
    assert run("retro.py", ["missing"], tmp_path)[1].split() == ["missing:", "1", "s0"]
    got, out = run("retro.py", ["check", str(f)], tmp_path)
    assert got == 0 and "reasons missing: dispatch" in out and "answers missing: Q1, Q2, Q3, Q4, Q5" in out
    f.write_bytes(f.read_bytes().replace(b"accept: 1", b"accept: 9"))
    assert run("retro.py", ["check", str(f)], tmp_path)[0] == 1
    f.write_bytes(f.read_bytes().replace(b"accept: 9", b"accept: 1").replace(b"\n", b"\r\n"))  # autocrlf checkout
    assert run("retro.py", ["check", str(f)], tmp_path)[0] == 0
    f.write_bytes(f.read_bytes().replace(b"accept: 1", b"accept: 9"))
    assert run("retro.py", ["check", str(f)], tmp_path)[0] == 1
    f.write_bytes(f.read_bytes().replace(b"accept: 9", b"accept: 1"))
    run("retro.py", ["write", "s0"], tmp_path)  # sum recounts retro files only (t-2031)
    got, out = run("retro.py", ["sum", "--since", "2026-11-01"], tmp_path)
    assert got == 0 and "(s0, s1)" in out and "ask_owner: 4" in out
    assert "dispatch: ?=3 builder=2 lead=1" in out
    got, out = run("retro.py", ["sum", "--since", "2026-11-20"], tmp_path)
    assert "(s1)" in out and "ask_owner: 3" in out
    assert run("retro.py", ["sum", "--since", "yesterday"], tmp_path)[0] == 2


# expected from: t-2021 B2 and the card's edge list: a retro nobody edited stays green whatever the journals gain later;
# a value with a newline, space or "=" is one token; t-2024 N1 G, S, T: a line killed mid-write after the window end,
# in a file whose last earlier line is inside the window, is dated by the next valid line (or none) and stays outside;
# t-2029 N5 (the Lead's ruling): check recounts in the file's window line, so B7's session_end journaled after write
# moves nothing (gitgap, badgap); a window line edited or missing is red, and write restores a missing one (t-2031 F6);
# t-2031: own lines after the end (the chat step) never enter (ownafter), sum recounts in the same window (N6), and a
# windowless line with its trailing space trimmed still parses (trimmed); t-2035 M1: an own line killed last at write is
# undated (never named), then dated past the end like one killed after write (ownafter); F9: an undated slug is no
# earlier slug (undatedslug)
@pytest.mark.parametrize("mode,code", [("gitline", 0), ("gitbad", 0), ("later", 0), ("values", 0), ("G", 0), ("S", 0),
                                       ("T", 0), ("gitgap", 0), ("badgap", 0), ("winedit", 1), ("nowinline", 1),
                                       ("ownafter", 0), ("trimmed", 0), ("undatedslug", 0)])
def test_retro_untouched(tmp_path, mode, code):
    retro_fixture(tmp_path, git=False)
    if mode == "values":
        put(tmp_path, "logs/journal/s1.jsonl", "".join(jl(ts="2026-11-20T10:00:0%dZ" % i, event=e, task=t, note=n) for i, (e, t, n) in enumerate([
            ("reject", "t 1\nZ=1", ""), ("reject", "t 1\nZ=1", ""), ("refuse", "", "fw\nx: door"), ("dispatch", "", "role:a=b")])).encode())
    if mode == "trimmed":
        put(tmp_path, "logs/journal/s1.jsonl", b"{oops\n")
    late, killed = jl(ts="2026-11-21T10:00:00Z", event="refuse", note="pre-push: z"), '{"ts": "2026-11-21T09:00:00Z", "ev'
    gap = jl(ts="2026-11-20T10:00:30Z", event="refuse", note="pre-commit: retro")  # after s1's last line, 10:00:19
    par = ("p0", jl(ts="2026-11-20T10:00:03Z", event="accept", task="t-7"))  # a parallel session, inside s1's window
    p0, p1 = {"G": ("git-hooks", jl(ts="2026-11-20T10:00:05Z", event="refuse", note="pre-commit: x")), "S": par,
              "T": par}.get(mode, ("", ""))
    if p0:
        put(tmp_path, "logs/journal/%s.jsonl" % p0, p1.encode())
    if mode == "ownafter":
        with open(tmp_path / "logs" / "journal" / "s1.jsonl", "a") as fh:
            fh.write(killed + "\n")  # the own file's last line at write, killed mid-write: undated
    f = tmp_path / "logs" / "retro" / "s1.md"
    got, out = run("retro.py", ["write", "s1"], tmp_path)
    assert got == 0 and "unparsable" not in out
    rel, data = {"gitline": ("git-hooks", late), "gitbad": ("git-hooks", "{oops\n" + late), "later": ("s9", "{oops\n"),
                 "G": (p0, p1 + killed + "\n" + late), "S": (p0, p1 + killed + "\n" + late), "T": (p0, p1 + killed),
                 "gitgap": ("git-hooks", gap), "badgap": ("p0", killed + "\n" + gap), "winedit": ("git-hooks", late),
                 "nowinline": ("git-hooks", late),
                 "undatedslug": ("p0", '{"task": "", "event": "ask_owner", "note": "q:alpha later"}\n')}.get(mode, ("", ""))
    if rel:
        put(tmp_path, "logs/journal/%s.jsonl" % rel, data.encode())
    chat = jl(ts="2026-11-20T10:00:40Z", event="ask_owner", note="q:alpha said in chat") + jl(
        ts="2026-11-20T10:00:41Z", event="refuse", note="foreign_write: chat") + killed + "\n" if mode == "ownafter" else ""
    if mode in ("gitgap", "badgap", "ownafter"):  # B7: the chat step and session_end come after write
        with open(tmp_path / "logs" / "journal" / "s1.jsonl", "a") as fh:
            fh.write(chat + jl(ts="2026-11-20T10:01:00Z", event="session_end"))
    edit = {"winedit": (" .. 2026-11-20T10:00:19Z", " .. 2026-11-22T00:00:00Z"), "nowinline": ("\nwindow: ", "\nspan: "),
            "trimmed": ("\nwindow:  .. \n", "\nwindow:  ..\n")}
    if mode in edit:
        assert edit[mode][0].encode() in f.read_bytes()
        f.write_bytes(f.read_bytes().replace(*[s.encode() for s in edit[mode]]))
    got, out = run("retro.py", ["check", str(f)], tmp_path)
    assert got == code and (mode != "nowinline" or "no window line" in out)
    if mode == "nowinline":
        assert run("retro.py", ["write", "s1"], tmp_path)[0] == 0 and run("retro.py", ["check", str(f)], tmp_path)[0] == 0
    if mode in ("gitgap", "badgap", "ownafter"):
        out = run("retro.py", ["sum", "--since", "2026-11-01"], tmp_path)[1]
        assert "incomplete" not in out and {"gitgap": "refuse (git hooks): 0", "badgap": "sessions since 2026-11-01: 1 (s1)",
                                            "ownafter": "ask_owner: 3"}[mode] in out
    if mode == "values":
        assert {"refuse: fw_x=1", "dispatch: a_b=1", "  task t_1_Z_1: 2"} <= set(block_of(tmp_path))


# expected from: t-2021 F1 (a bad line is pinned to its own file; one in an earlier file marks the block) and the card's
# "earlier sessions" for missing
@pytest.mark.parametrize("mode,words", [
    ("as1", ["counts: incomplete", "unparsable line 2 in as1.jsonl"]),
    ("s0", ["counts: incomplete", "unparsable line 1 in s0.jsonl", "ask_owner repeats: 1"]),
    ("later", ["missing: s0"]),
    ("gitdir", ["counts: incomplete", "  unreadable file git-hooks.jsonl", "refuse (git hooks): unknown"]),  # t-2024 N2, t-2029 F3
    ("p5dir", ["counts: incomplete", "  unreadable file p5.jsonl", "missing: p5, s0"]),  # t-2029 F1: lines unknown, not none
    ("gitpre", ["counts: ok", "refuse (git hooks): pre-commit=2"]),  # t-2029 M2: a git bad line dated before the window
])
def test_retro_bad_scope(tmp_path, mode, words):
    retro_fixture(tmp_path, git=mode != "gitdir")
    if mode in ("gitdir", "p5dir"):
        put(tmp_path, "logs/journal/%s.jsonl" % {"gitdir": "git-hooks", "p5dir": "p5"}[mode], None)  # a folder: open() fails
    if mode == "gitpre":
        put(tmp_path, "logs/journal/git-hooks.jsonl", b"{x\n" + (tmp_path / "logs" / "journal" / "git-hooks.jsonl").read_bytes())
    if mode == "as1":  # the bad line is dated by the next valid line, before s1's window end (t-2024 N1)
        put(tmp_path, "logs/journal/as1.jsonl", (jl(ts="2026-11-19T08:00:00Z", event="accept") + "{x\n" +
                                                 jl(ts="2026-11-19T08:00:01Z", event="accept")).encode())
    if mode == "s0":
        put(tmp_path, "logs/journal/s0.jsonl", ('{"ts":"2026-11-19T09:00:00Z","event":"ask_owner","note":"q:beta old"\n' +
                                               jl(ts="2026-11-19T09:00:01Z", event="accept")).encode())
    if mode == "later":
        put(tmp_path, "logs/journal/s2.jsonl", jl(ts="2026-11-22T10:00:00Z", event="accept").encode())
    got, out = run("retro.py", ["write", "s1"], tmp_path)
    assert got == 0 and all(w in out for w in words) and "in s1.jsonl" not in out
    assert mode != "later" or "missing: s0" in out.splitlines()  # the later s2 is not an earlier session
    if mode in ("gitdir", "p5dir"):  # t-2031 F7: the sum and missing doors meet the unreadable file too
        s_out, m_out = (run("retro.py", a, tmp_path)[1] for a in (["sum", "--since", "2026-11-01"], ["missing"]))
        assert "incomplete: s1" in s_out and ("p5" in m_out.split()) == (mode == "p5dir")
        assert {"gitdir": "refuse (git hooks): unknown", "p5dir": "missing: p5, s0"}[mode] in s_out


# expected from: t-2021 F3 (a session with no window is named), the card's refusals and the weekly sum's lists
def test_retro_refusals_sum(tmp_path):
    retro_fixture(tmp_path)
    put(tmp_path, "logs/journal/sx.jsonl", b"{oops\n")
    f = tmp_path / "logs" / "retro" / "s1.md"
    assert run("retro.py", ["check", str(f)], tmp_path)[0] == 2
    put(tmp_path, "logs/retro/s1.md", b"junk\n")
    assert run("retro.py", ["check", str(f)], tmp_path)[0] == 2
    got, out = run("retro.py", ["write", "s1"], tmp_path)
    assert got == 2 and "not overwritten" in out and f.read_bytes() == b"junk\n"
    f.unlink()
    assert "missing: s0, sx" in run("retro.py", ["write", "s1"], tmp_path)[1]  # t-2031 F5: an undated sx is never dropped
    got, out = run("retro.py", ["sum", "--since", "2026-11-20"], tmp_path)  # t-2031: no retro file -> only missing
    assert "missing: s0, sx" in out and "reasons missing: s1(" in out and "answers missing: s1(Q1" in out
    assert "incomplete" not in out and "(s1)" in out
    for data in (f.read_bytes().replace(b"\nwindow: ", b"\nspan: "), b""):  # t-2031 N6, t-2035 N8: named, never recounted
        f.write_bytes(data)
        out = run("retro.py", ["sum", "--since", "2026-11-20"], tmp_path)[1]
        assert "incomplete: s1" in out and "sessions since 2026-11-20: 0 (none)" in out
