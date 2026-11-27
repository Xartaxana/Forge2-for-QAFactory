# card: C1-5
"""Tool tests of card C1-5 (hooks, the one secret table). Pure functions run in-process; a real git fixture only where git
itself is the thing judged. Every git subprocess runs with all GIT_* variables removed (GIT_DIR, GIT_INDEX_FILE: an
inherited one would aim a fixture at the real repository). Tokens are built at run time, never written here."""
import datetime
import importlib.machinery
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import time

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HOOKS = os.path.join(ROOT, "forge", "hooks")
sys.path.insert(0, HOOKS)
import foreign_write as fw  # noqa: E402
import hio  # noqa: E402
import pre_compact as pcm  # noqa: E402
import secret_scan as ss  # noqa: E402


def load(name):
    path = os.path.join(HOOKS, "git", name)
    spec = importlib.util.spec_from_loader(name, importlib.machinery.SourceFileLoader(name, path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


pp, pc = load("pre-push"), load("pre-commit")
Z = "0" * 40
OW = "owner-word: \u00abyes, go\u00bb 2026-11-26"
FIX = [{"id": "env-file", "kind": "path_glob", "pattern": ".env*", "what": "env file"},
       {"id": "fixture-key", "kind": "token_regex", "pattern": "ZQXK[0-9]{12}", "what": "fixture key"}]
CI = ("import os,sys\nd=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n"
      "open(d+'/ci-ran','w').close()\ne=d+'/ci-exit'\nsys.exit(int(open(e).read()) if os.path.exists(e) else 0)\n")


def tok():
    return "ZQX" + "K" + "123456789012"


def table(rows, schema="secret-patterns/1"):
    return json.dumps({"schema": schema, "rows": rows})


def put(p, text):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def run(args, cwd, stdin=b"", **env):
    e = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    e.update(env)
    r = subprocess.run(args, cwd=str(cwd), input=stdin, capture_output=True, env=e, timeout=120)
    return r.returncode, (r.stdout + r.stderr).decode("utf-8", "replace")


def git(r, *a):
    return run(["git", "-C", str(r)] + list(a), r)


def hook(name, args, cwd, stdin=b"", **env):
    return run([sys.executable, "-B", os.path.join(HOOKS, name)] + args, cwd, stdin, **env)


def mkroot(p, remote=None, ci=True):
    """A fixture repository root with the table, the ci stub, remote.json and journal.py."""
    p = str(p)
    put(p + "/factory/data/secret-patterns.yaml", table(FIX))
    if ci:
        put(p + "/forge/tools/ci.py", CI)
    put(p + "/forge/remote.json", json.dumps(remote if remote is not None else {"origin": "o", "measure_cleared": None}))
    os.makedirs(p + "/forge/tools", exist_ok=True)
    shutil.copy(os.path.join(ROOT, "forge", "tools", "journal.py"), p + "/forge/tools/journal.py")
    return p


def mkrepo(p):
    p = mkroot(p, {"origin": "o", "measure_cleared": None})
    git(p, "init", "-q", "-b", "main")  # one git call, the config appended (t-1984 N5: the file runs under 10 s)
    with open(p + "/.git/config", "a", encoding="utf-8") as fh:
        fh.write("[user]\n\tname = t\n\temail = t@t\n[core]\n\tautocrlf = false\n")
    return p


def commit(r, msg, files=None, rm=()):
    for rel, text in (files or {}).items():
        put(r + "/" + rel, text)
        git(r, "add", "--", rel)
    for rel in rm:
        git(r, "rm", "-q", "--", rel)
    put(r + ".msg", msg + "\n")
    git(r, "commit", "-q", "--allow-empty", "--no-verify", "-F", r + ".msg")
    return git(r, "rev-parse", "HEAD")[1].strip()


@pytest.fixture(scope="module")
def leaky(tmp_path_factory):
    """c1 clean, c2 adds a token, c3 removes it: the token is gone from c3 and alive in the range. c4 is an evil merge."""
    r = mkrepo(tmp_path_factory.mktemp("leaky"))
    c1 = commit(r, "base", {"s/x.txt": "clean\n"})
    c2 = commit(r, "leak", {"s/k.txt": "key " + tok() + "\n"})
    c3 = commit(r, "unleak", rm=["s/k.txt"])
    git(r, "checkout", "-q", "-b", "side", c1)
    commit(r, "side", {"side.txt": "clean\n"})
    git(r, "checkout", "-q", "main")
    git(r, "merge", "-q", "--no-ff", "--no-commit", "side")
    return r, c1, c2, c3, commit(r, "evil merge", {"s/e.txt": "key " + tok() + "\n"})


def push(r, lines, url="o"):
    out = hook("git/pre-push", ["origin", url], r, "".join("%s %s %s %s\n" % x for x in lines).encode())
    ran = os.path.exists(r + "/ci-ran") and not os.remove(r + "/ci-ran")
    return out[0], out[1], ran


# expected from: card C1-5 (part2:127-133, staged paths and key-shaped tokens, one table); B8 (part4b-2:15, 20-22: the
# range scan, K3); the brief's section 3 Scan edges (staged deletion passes; the value is never printed)
@pytest.mark.parametrize("files,rm,code,seen", [
    ({"y.txt": "key " + tok() + "\n"}, [], 1, "fixture-key"),
    ({"z.txt": "clean\n"}, [], 0, ""),
    ({".env.local": "B=2\n"}, [], 1, "env-file"),
    ({}, ["s/x.txt"], 0, ""),
    ({"factory/data/secret-patterns.yaml": open(os.path.join(ROOT, "factory/data/secret-patterns.yaml"),
                                                encoding="utf-8").read()}, [], 0, "")])
def test_scan_staged(leaky, files, rm, code, seen):
    r = leaky[0]
    for rel, text in files.items():
        put(r + "/" + rel, text)
        git(r, "add", "--", rel)
    for rel in rm:
        git(r, "rm", "-q", "--", rel)
    out = hook("secret_scan.py", ["--staged"], r)
    git(r, "reset", "-q")
    put(r + "/factory/data/secret-patterns.yaml", table(FIX))
    assert out[0] == code and seen in out[1] and tok() not in out[1]


def test_scan_range(leaky):
    r, c1, c2, c3, c4 = leaky
    got = [hook("secret_scan.py", ["--range", a], r) for a in (c1 + ".." + c3, c1, c3, c3 + ".." + c4)]
    assert [g[0] for g in got] == [1, 0, 1, 1] and c2[:12] in got[0][1] and tok() not in got[0][1] and c4[:12] in got[3][1]


# expected from: B8 part4b-2:15 (pre-push scans the whole pushed range before ci.py; a new branch = every commit on no
# remote ref; the first push = all history; a delete has nothing to scan) and B9 (every refusal journaled, no value)
def test_pre_push_range(leaky):
    r, c1, c2, c3, _ = leaky
    line = lambda new, old=Z, ref="refs/heads/main": [(ref, new, ref, old)]  # noqa: E731
    got = {n: push(r, ls) for n, ls in (("twin", line(c1)), ("k3", line(c3, c1)), ("new", line(c3, Z, "refs/heads/b")),
                                        ("first", line(c3)), ("delete", [("(delete)", Z, "refs/heads/b", c3)]))}
    assert [got[n][0] == 0 for n in got] == [True, False, False, False, True]
    assert [got[n][2] for n in got] == [True, False, False, False, False]
    assert all(c2[:7] in got[n][1] and "fixture-key" in got[n][1] and tok() not in got[n][1] for n in ("k3", "new", "first"))
    log = open(r + "/logs/journal/git-hooks.jsonl", encoding="utf-8").read()
    assert '"event": "refuse"' in log and "pre-push:" in log and tok() not in log


# expected from: t-1983 F1, F6, M2 and the brief's section 8 A1 (pre-commit judges the index GIT_INDEX_FILE names, as git sets
# it for `commit -a` and `commit <path>`; the hook is called directly, never through core.hooksPath); the root commit holds
# the token, so `--range HEAD` finds it only with --root
def test_pre_commit_judges_git_index_file(tmp_path):
    r = mkrepo(tmp_path / "g")
    commit(r, "root", {"k.txt": "key " + tok() + "\n"})
    assert hook("secret_scan.py", ["--range", "HEAD"], r)[0] == 1
    idx = str(tmp_path / "idx")
    put(r + "/n.txt", "key " + tok() + "\n")
    for a in (["read-tree", "HEAD"], ["add", "--", "n.txt"]):
        run(["git", "-C", r] + a, r, GIT_INDEX_FILE=idx)
    code, out = hook("git/pre-commit", [], r, GIT_INDEX_FILE=idx)
    assert code == 1 and "fixture-key" in out and tok() not in out and hook("git/pre-commit", [], r)[0] == 0
    assert "pre-commit:" in open(r + "/logs/journal/git-hooks.jsonl", encoding="utf-8").read()


# expected from: the brief's section 3 Crash edge (git absent -> pre-push and pre-commit refuse; irreversible acts fail closed);
# t-1983 F7: inside a repository, so only git's absence can refuse
@pytest.mark.parametrize("name,stdin", [("git/pre-push", ("refs/heads/m %s refs/heads/m %s\n" % ("a" * 40, Z)).encode()),
                                        ("git/pre-commit", b"")])
def test_crash_git_absent(leaky, tmp_path, name, stdin):  # t-1984 N5: the module repo; git is absent anyway
    code, out = hook(name, ["origin", "o"], leaky[0], stdin, PATH=str(tmp_path))
    assert code == 1 and "refused" in out and "git failed" in out


# expected from: card C1-5 (the one table, AR-15) and the brief's section 3 Table edge (every malformed shape ->
# exit 2 naming file, row id and the door "restore secret-patterns.yaml (C1-5)"); AR-28
def _row(**kw):
    return dict(FIX[1], **kw)


@pytest.mark.parametrize("text,rid", [
    (None, ""), ("{not json", ""), ("schema: secret-patterns/1\nrows:\n- id: a\n", ""), ("[]", ""),
    (table([]), ""), (table(FIX, "other/1"), ""), (table(FIX + [_row(kind="word", id="k")]), "k"),
    (table(FIX + [dict(_row(id="x"), extra="1")]), "x"), (table(FIX + [{"id": "m", "kind": "path_glob"}]), "m"),
    (table(FIX + [_row(id="b", pattern="(")]), "b"), (table(FIX + [_row()]), "fixture-key")])
def test_table_refused(tmp_path, text, rid):
    if text is not None:
        put(str(tmp_path) + "/" + ss.TABLE, text)
    with pytest.raises(ss.Cannot) as e:
        ss.load_table(str(tmp_path))
    assert ss.TABLE in str(e.value) and "restore secret-patterns.yaml (C1-5)" in str(e.value) and rid in str(e.value)


def test_table_real_seed_rows():
    rows = ss.load_table(ROOT)
    blob = {"aws": "AKIA" + "ABCDEFGHIJ012345", "gh": "gh" + "p_" + "a1" * 18, "pat": "github" + "_pat_" + "a" * 22,
            "ant": "sk-" + "ant-" + "a" * 24, "slack": "xo" + "xb-" + "1234567890ab", "pem": "-----BEGIN " + "PRIVATE KEY-----",
            "jwt": "ey" + "J" + "a" * 12 + ".ey" + "J" + "b" * 12 + ".", "name": "aws_secret_" + "access_key",
            "assign": 'api_' + 'key = "' + "a" * 20 + '"'}
    paths = {".env.example": 1, "d/id_rsa": 1, "credentials.json": 1, "credentials.conf": 1, "k.pem": 1, "secrets.py": 0, "x/envelope.txt": 0}
    for text in blob.values():
        ss.git, old = (lambda *a, t=text: t.encode()), ss.git
        try:
            assert len(ss.scan(ROOT, rows, [("x", "f.txt", "sha" + text)])) == 1, text
        finally:
            ss.git = old
    ss.git, old = (lambda *a: b"clean"), ss.git
    try:
        assert {p: len(ss.scan(ROOT, rows, [("x", p, "s" + p)])) for p in paths} == paths
    finally:
        ss.git = old


# expected from: the brief's section 3 Pre-push steps and Owner-word edges (fixed order, first refusal stops, ci.py exit
# 0 passes, anything else refuses); B8 part4b-2:15, 21 (remote.json, other remote, measure_cleared, W-id refused: F237)
def steps(tmp_path, monkeypatch, remote, url="o", ents=(), msg="m", ref="refs/heads/main", ci=0, blob="clean", walk=None):
    root = mkroot(tmp_path, remote if remote != "absent" else None, ci is not None)
    if remote == "absent":
        os.remove(root + "/forge/remote.json")
    if ci:
        put(root + "/ci-exit", str(ci))
    msgs = [msg] if isinstance(msg, str) else msg  # one message per commit, the tip (the pushed sha) first
    ids = [c * 40 for c in "ad"][:len(msgs)]
    monkeypatch.setattr(ss, "git", lambda r, *a: msgs[ids.index(a[-1])].encode() if a[0] == "log" else (b"a" * 40 + b"\n")
                        if a[0] == "rev-parse" else blob.encode())
    monkeypatch.setattr(ss, "walk", lambda r, revs: (ids if walk is None else walk, [("c" * 40, p, "s" + p) for p in ents]))
    res = pp.steps(root, "origin", url, [[ref, "a" * 40, ref, "b" * 40]], True)
    return res, os.path.exists(root + "/ci-ran")


def ok(c):
    return {"origin": "o", "measure_cleared": c}


@pytest.mark.parametrize("kw,door,ci_ran", [
    (dict(remote="absent"), "remote", False), (dict(remote="x"), "remote", False), (dict(remote={"origin": "o"}), "remote", False),
    (dict(remote={"measure_cleared": None}), "remote", False), (dict(remote=ok(None), url="o/", msg=OW), None, True),
    (dict(remote=ok(None), url="other"), "other", False), (dict(remote=ok(None), url="other", msg=OW), None, True),
    (dict(remote=ok(None), url="other", msg=[OW, "m"]), None, True), (dict(remote=ok(None), url="other", msg=["m", OW]), "other", False),
    (dict(remote=ok(None), url="https://u:PW123@h/a.git"), "other", False),
    (dict(remote=ok(None), url="https://h/m.git?access_token=PW123"), "other", False),  # t-1984 N4: a query token
    (dict(remote=ok(None), url="other", walk=[]), "other", False),  # t-1984 N3, A2: an empty range still judges the tip
    (dict(remote={"origin": "https://h/a", "measure_cleared": None}, url="https://u:PW123@h/a.git"), None, True),
    (dict(remote=ok(None), ents=["measure/r.txt"]), "measure", False),
    (dict(remote=ok(OW), ents=["measure/r.txt"]), None, True), (dict(remote=ok("W-1"), ents=["measure/r.txt"]), "measure", False),
    (dict(remote=ok("yes"), ents=["measure/r.txt"]), "measure", False), (dict(remote=ok(5), ents=["measure/r.txt"]), "measure", False),
    (dict(remote=ok(None), ents=["x/measure/r.txt"]), None, True),
    (dict(remote=ok(None), ref="refs/tags/v1"), "release", False), (dict(remote=ok(None), ref="refs/tags/v1", msg=OW), None, True),
    (dict(remote=ok(None), ref="refs/heads/release"), "release", False), (dict(remote=ok(None), ref="refs/tags/x1"), None, True),
    (dict(remote=ok(None), ci=1), "ci", True), (dict(remote=ok(None), ci=2), "ci", True), (dict(remote=ok(None), ci=7), "ci", True),
    (dict(remote=ok(None), ci=None), "ci", False),
    (dict(remote="absent", blob=tok(), ents=["f"]), "remote", False),
    (dict(remote=ok(None), blob=tok(), ents=["f"], ci=1), "scan", False),
    (dict(remote=ok(None), blob=tok(), ents=["measure/a"], ref="refs/tags/v1", ci=1), "scan", False),
    (dict(remote=ok(None), ents=["measure/a"], ref="refs/tags/v1", ci=1), "measure", False),
    (dict(remote=ok(None), ref="refs/tags/v1", ci=1), "release", False)])
def test_pre_push_steps(tmp_path, monkeypatch, kw, door, ci_ran):
    res, ran = steps(tmp_path, monkeypatch, **kw)
    assert (res[1] if res else None) == door and ran == ci_ran and "PW123" not in str(res)
    assert door != "measure" or ("F88" in res[0]) == (kw["remote"]["measure_cleared"] is None)


def test_pre_push_lines(monkeypatch, tmp_path):
    calls = []
    monkeypatch.setattr(ss, "toplevel", lambda *a: str(tmp_path))
    monkeypatch.setattr(pp, "steps", lambda *a: calls.append(a) or None)
    good = "refs/heads/m %s refs/heads/m %s" % ("a" * 40, Z)
    assert pp.body([], "") == 0 and pp.body(None, "no input") == 1 and not calls
    assert pp.body([good], "") == 0 and calls[-1][3] == [good.split()] and calls[-1][4] is True
    assert pp.body(["a b c", None, "r " + "g" * 40 + " r " + Z, good], "") == 1 and calls[-1][3] == [good.split()]
    assert calls[-1][4] is False


@pytest.mark.parametrize("text,want", [
    (OW, True), ("x\n" + OW + "\ny", True), ('owner-word: "yes" 2026-11-26', False), ("owner-word: \u00ab \u00bb 2026-11-26", False),
    ("owner-word: \u00abyes\u00bb 2026-13-40", False), ("owner-word: \u00abyes\u00bb 26.11.2026", False),
    ("owner-word: \u00abyes\u00bb", False), ("owner-word: \u00aba \u00abb\u00bb c\u00bb 2026-11-26", True), ("> " + OW, False),
    ((b"junk \xff\n" + OW.encode()).decode("utf-8", "replace"), True), ("x\n" * 500000 + OW, True), (OW + "\r\n", True)])
def test_owner_word(text, want):
    assert pp.owner_word(text) is want


# expected from: the brief's section 3 Payload edge (F230 (c): json form returns None + a note; AT max_bytes read, one
# byte beyond refused; the deadline) and part 1 section 6 (outside input)
def feed(data, form="json", **kw):
    r, w = os.pipe()
    os.write(w, data)
    os.close(w)
    try:
        return hio.io.read_input(form, fd=r, **kw)
    finally:
        os.close(r)


@pytest.mark.parametrize("data,note", [(b"", "empty"), (b"x", "JSON"), (b"[]", "object"), (b"\xff\xfe{", "UTF-8"),
                                       (b'{"a": "' + b"x" * 1015 + b'"}', ""), (b'{"a": "' + b"x" * 1016 + b'"}', "over")])
def test_read_input_json(data, note):
    val, why = feed(data, max_bytes=1024)
    assert (val is None) == bool(note) and note in why


def test_read_input_lines_and_deadline():
    assert feed(b"") == (None, "empty input") and feed(b"", "lines") == ([], "") and feed(b"a b\n\xff\nz", "lines") == (["a b", None, "z"], "")
    r, w = os.pipe()
    try:
        assert hio.io.read_input("json", deadline_s=0.2, fd=r)[0] is None
    finally:
        os.close(w)
        os.close(r)


# expected from: the brief's section 3 foreign_write, Paths and Bash edges (whole components, normalisation, only literal
# paths in a write position count, a variable errs green); card C1-5 (Write/Edit/Bash) with F234 (NotebookEdit, PowerShell)
RT = ["c:/prot/root"]
P = "C:/Prot/Root"


def pay(tool, cwd="C:/work", **ti):
    return {"session_id": "s", "tool_name": tool, "tool_input": ti, "cwd": cwd}


FILES = [("Write", {"file_path": P + "/a"}, 1), ("Edit", {"file_path": P + "/a"}, 1), ("MultiEdit", {"file_path": P + "/a"}, 1),
         ("NotebookEdit", {"notebook_path": P + "/n.ipynb"}, 1), ("Write", {"file_path": P}, 1),
         ("Write", {"file_path": "C:/Prot/Root2/a"}, 0), ("Write", {"file_path": "C:/Prot/Roo/a"}, 0),
         ("Write", {"file_path": "C:/Other/a"}, 0), ("Write", {"file_path": "C:\\Prot\\Root\\a"}, 1),
         ("Write", {"file_path": "c:/PROT/root/a"}, 1), ("Write", {"file_path": "/c/Prot/Root/a"}, 1),
         ("Write", {"file_path": "C:/work/../Prot/Root/a"}, 1), ("Write", {"file_path": P + "/sp ace/\u0434/a"}, 1),
         ("Read", {"file_path": P + "/a"}, 0), ("Write", {"file_path": "x" * 100000}, 0),
         ("Write", {"file_path": P + "/" + "d/" * 40000 + "a"}, 1), ("Write", {"file_path": "//?/C:/Prot/Root/a"}, 1),
         ("Write", {"file_path": "\\\\.\\C:\\Prot\\Root\\a"}, 1), ("Write", {"file_path": "C:/Prot/Root./a"}, 1),
         ("Write", {"file_path": "C:/Prot/Root /a"}, 1), ("Write", {"file_path": "C:/Prot/Root/../a"}, 0)]
SHELL = [("echo x > \"%s/a\"" % P, 1), ("echo x >> /c/Prot/Root/a", 1), ("echo x 2>&1 | tee %s/a" % P, 1),
         ("cp C:/work/b %s/a" % P, 1), ("cp %s/a C:/work/b" % P, 0), ("cp -t %s C:/work/b" % P, 1),
         ("mv %s/a C:/work/b" % P, 1), ("rm -rf %s/d" % P, 1), ("sed -i 's/a/b/' %s/f" % P, 1), ("sed 's/a/b/' %s/f" % P, 0),
         ("git -C %s commit -m x" % P, 1), ("git -C %s log -1" % P, 0), ("( cd %s && git commit -m x )" % P, 1),
         ("cd %s; touch a" % P, 1), ("(cd %s && ls); touch a" % P, 0), ("echo x > $HOME/a", 0), ("cat %s/a" % P, 0),
         ("ls > /dev/null; echo hi 2>&1", 0), ("git clone https://x/y.git %s/y" % P, 1), ("dd if=a of=%s/f" % P, 1),
         ("cat > C:/work/a <<EOF\necho x > %s/zz\nEOF" % P, 0), ("echo a\ntouch %s/a" % P, 1), ("x=1 git -C C:\\Prot\\Root add .", 1),
         ("chmod 755 %s/a" % P, 1), ("chmod 755 C:/work/a", 0), ("cp a.txt \\\n  %s/x.txt" % P, 1), ("rm -rf \\\r\n  %s/d" % P, 1),
         ("rm %s/d \\\n" % P, 1), ("git -C C:/ -C Prot/Root commit -m x", 1), ("git -C %s -C C:/work commit -m x" % P, 0),
         ("git --git-dir=%s/.git --work-tree=%s commit" % (P, P), 1), ("git --git-dir %s/.git commit" % P, 1),
         ("GIT_DIR=%s/.git git commit" % P, 1), ("GIT_WORK_TREE=%s git add ." % P, 1),
         ("echo done \\\\\nrm -rf %s/d" % P, 1), ("GIT_DIR=.git GIT_WORK_TREE=. git -C %s commit -m x" % P, 1),  # t-1984 N1, N2
         ("GIT_DIR=C:/work/.git git -C %s checkout -- ." % P, 1), ("git -C %s --work-tree=C:/work commit -m x" % P, 1),
         ("echo \"x \\\\\" it\\'s; rm -rf %s/d" % P, 1), ("GIT_WORK_TREE=%s/new git clone https://x/y.git C:/work/y" % P, 1),  # t-1985
         ("git init %s/new" % P, 1), ("git worktree add %s/wt" % P, 1), ("git clone --separate-git-dir=%s/g u C:/work/y" % P, 1),
         ("cp --target-directory %s C:/work/b" % P, 1)]  # t-1986 D1 (residual R4)
POWER = [("Set-Content -Path \"%s/a\" -Value x" % P, 1), ("set-content C:\\Prot\\Root\\a x", 1), ("Remove-Item %s/a -Force" % P, 1),
         ("Copy-Item %s/a C:/work/b" % P, 0), ("Copy-Item C:/work/a -Destination %s/b" % P, 1), ("\"x\" | Out-File %s/a" % P, 1),
         ("echo x > %s/a" % P, 1), ("Get-Content %s/a" % P, 0), ("Move-Item %s/a C:/work/b" % P, 1),
         ("Set-Content `\n  -Path %s/a -Value 1" % P, 1), ("Get-ChildItem \"C:\\work\\\"; Remove-Item %s/x" % P, 1),  # t-1985 N7
         ("Write-Output \"a`\"b\"; Remove-Item %s/x" % P, 1)]  # t-1986 M3


@pytest.mark.parametrize("tool,ti,bad", FILES)
def test_foreign_write_files(tool, ti, bad):
    assert (fw.judge(pay(tool, **ti), RT)[0] == "refuse") == bool(bad)


@pytest.mark.parametrize("tool,cmds", [("Bash", SHELL), ("PowerShell", POWER)])
def test_foreign_write_shell(tool, cmds):
    assert [fw.judge(pay(tool, command=c), RT)[0] == "refuse" for c, _ in cmds] == [bool(b) for _, b in cmds]
    assert fw.judge(pay("Bash", cwd=P, command="git commit -m x"), RT)[0] == "refuse"
    assert fw.judge(pay("Bash", cwd=P, command="git status"), RT)[0] == "pass"


def test_foreign_write_bad_argv():
    code, out = hook("foreign_write.py", ["--root"], ROOT, b"{}")  # t-1983 F10: exit 2 would block every tool call
    assert code == 0 and "not checked" in out


@pytest.mark.parametrize("payload", [None, {}, {"tool_name": "Write"}, pay("Write", file_path=""), pay("Bash", command="  "),
                                     {"tool_name": "Write", "tool_input": []}])
def test_foreign_write_cannot_judge(payload):
    assert fw.judge(payload, RT)[0] == "skip"


# expected from: the brief's section 3 Roots file edge (absent, unreadable, not an object, empty list, non-absolute root ->
# the F231 (a) line on every call, exit 0; a session id missing from the input is still judged)
@pytest.mark.parametrize("text,good", [(None, 0), ('{"roots": []}', 0), ('{"roots": ["rel/x"]}', 0), ("nope", 0), ("[]", 0),
                                       ('{"roots": [5]}', 0), ('{"roots": ["C:/Prot/Root/"]}', 1)])
def test_roots_file(tmp_path, capsys, text, good):
    if text is not None:
        put(str(tmp_path) + "/forge/hooks/protected-roots.json", text)
    roots, why = fw.load_roots(str(tmp_path))
    assert (why is None) == bool(good) and (roots == RT if good else roots == [])
    assert fw.body(pay("Write", file_path=P + "/a"), "", str(tmp_path)) == (2 if good else 0)
    assert ("not checked" in capsys.readouterr().err) != bool(good)


# expected from: B9 part4b-2:27 (a refusal journals one `refuse` line under the hook input's session; a failed write never
# changes a verdict) and the brief's section 3 Journal edge (no valid session: no line, one stderr line; the note <= 300)
@pytest.mark.parametrize("sid,jrnl", [("s1", True), (None, True), ("bad id!", True), ("s1", False)])
def test_journal_refuse(tmp_path, capsys, sid, jrnl):
    root = mkroot(tmp_path, ci=False)
    put(root + "/forge/hooks/protected-roots.json", json.dumps({"roots": [root + "/prot"]}))
    if not jrnl:
        os.remove(root + "/forge/tools/journal.py")
    p = pay("Write", file_path=root + "/prot/a")
    p.pop("session_id")
    p.update({"session_id": sid} if sid else {})
    assert fw.body(p, "", root) == 2
    err, path = capsys.readouterr().err, root + "/logs/journal/s1.jsonl"
    assert os.path.exists(path) == (sid == "s1" and jrnl) and ("journal not written" in err) == (not (sid == "s1" and jrnl))
    assert not os.path.exists(root + "/logs/journal/bad id!.jsonl")
    if os.path.exists(path):
        assert '"event": "refuse"' in open(path, encoding="utf-8").read()


def test_doors_fit_the_journal_note():
    doors = [("foreign_write", fw.DOOR)] + [("pre-push", d) for d in pp.DOORS.values()] + [("pre-commit", d) for d in pc.DOORS.values()]
    assert all(len("%s: %s" % x) <= 300 for x in doors)


# expected from: card C1-5 (pre_compact calls snapshot.py, writes only, never refuses; F18 (a)) and the brief's section 3
# Pre-compaction edge (any payload; AT the timeout completes, BEYOND it is killed; a failure -> hook_failed, exit 0)
SLEEP = "import time\ntime.sleep(%s)\n"


@pytest.mark.parametrize("stub,timeout,why", [
    (None, 45, "absent"), ("import sys\nsys.exit(3)\n", 45, "exit 3"), (SLEEP % 0.1, 5, None), (SLEEP % 5, 0.5, "killed")])
def test_pre_compact_failures(tmp_path, stub, timeout, why):
    root = mkroot(tmp_path, ci=False)
    if stub:
        put(root + "/forge/tools/snapshot.py", stub)
    assert pcm.body({"session_id": "s1"}, "", root, timeout) == 0
    path = root + "/logs/journal/s1.jsonl"
    log = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
    assert (why in log and '"event": "hook_failed"' in log and "pre_compact:" in log) if why else not log


@pytest.mark.parametrize("n", [250, 251])  # t-1983 F15: the why is cut at 250, a why AT it is kept whole
def test_pre_compact_cut(monkeypatch, n):
    got = []
    monkeypatch.setattr(pcm, "snapshot", lambda *a: "w" * n)
    monkeypatch.setattr(hio.io, "journal", lambda *a: got.append(a[-1]))
    pcm.body({"session_id": "s"}, "", "r", 1)
    assert got == ["pre_compact: " + "w" * 250]


def test_pre_compact_bad_argv():
    code, out = hook("pre_compact.py", ["--timeout-s", "x"], ROOT, b"{}")  # a bad argv must not exit 2
    assert code == 0 and "not run" in out


def test_pre_compact_writes(tmp_path):
    root = mkroot(tmp_path, ci=False)
    shutil.copy(os.path.join(ROOT, "forge", "tools", "snapshot.py"), root + "/forge/tools/snapshot.py")
    got = [pcm.body(p, "", root, 45) for p in ({"session_id": "s1"}, None)]
    assert got == [0, 0] and len(os.listdir(root + "/logs/journal/snapshots")) == 2


# expected from: card B2 (part4b:66-71) -- SessionStart prints blocks per `source`, open ids, the cap, never fails (plan 3.10)
import session_start as sst  # noqa: E402


def jl(root, *evs):
    put(root + "/logs/journal/s.jsonl", "".join(json.dumps(dict(ts="2026-11-26T10:%02d" % i, by="t", note="n", task=t, event=e))
                                                + "\n" for i, (t, e) in enumerate(evs)))


def start(root, source, arm=False):
    return hook("session_start.py", ["--root", root], ROOT, json.dumps({"source": source}).encode() if source else b"",
                **({"FORGE_EVAL_ARM": "x"} if arm else {}))


@pytest.mark.parametrize("source,boot,carr,prev,arm", [
    ("startup", 1, 0, 1, False), ("resume", 0, 0, 0, False), ("clear", 1, 0, 0, False), ("compact", 1, 1, 0, False),
    (None, 1, 0, 1, False), ("bogus", 1, 0, 1, False), ("compact", 1, 1, 0, True)])
def test_session_start_blocks(tmp_path, source, boot, carr, prev, arm):
    root = mkroot(tmp_path, ci=False)
    put(root + "/logs/journal/snapshots/a.md", "x")
    jl(root, ("t1", "dispatch"), ("", "session_end"))
    code, out = start(root, source, arm)
    assert code == 0 and ("not written yet (B1)" in out) == (boot and not arm) and ("re-read: forge/BOOT.md" in out) == (not arm)
    assert ("(not written yet, B1)" in out) == (not arm) and (not arm or "BOOT" not in out)  # B2-1: presence on every source
    assert "snapshot: logs/journal/snapshots/a.md (~0m old) | open: t1" in out  # B17 (c): no stamp in the name -> file time, `~`
    assert ("forge/carriers.json absent (B7)" in out) == bool(carr) and ("previous session: closed" in out) == bool(prev)
    put(root + "/forge/BOOT.md", "BOOTTEXT")
    out = start(root, source, arm)[1]
    assert ("BOOTTEXT" in out) == bool(boot) and ("re-read: forge/BOOT.md" in out)


@pytest.mark.parametrize("evs,want", [
    ([("a", "dispatch"), ("b", "dispatch"), ("a", "accept")], "open: b"), ([("a", "dispatch"), ("a", "reject")], "open: none"),
    ([("a", "dispatch"), ("a", "return"), ("a", "dispatch")], "open: a"),
    ([("a", "dispatch"), ("a", "return")], "open: a (result pending)"), ([("t%d" % i, "dispatch") for i in range(12)], "t9 and 2 more"),
    ([], "open: none"), (None, "open: unknown -- no journal"), (None, "previous session: unknown -- no journal"),
    ([], "snapshot: none yet"), ([("a", "dispatch")], "previous session: no session_end after 2026-11-26T10:00 -- read")])
def test_session_start_open(tmp_path, want, evs):
    root = mkroot(tmp_path, ci=False)
    if evs is not None:
        jl(root, *evs)
    assert want in start(root, "startup")[1]
    if evs:
        put(root + "/logs/journal/s.jsonl", open(root + "/logs/journal/s.jsonl").read() + "{bad\n")
        assert "(incomplete: 1 unreadable journal lines)" in start(root, "startup")[1]


# expected from: plan S6 (the re-read line names the Lead's rules file) and S10 (ahead/behind of main, never a fetch, exit 0)
@pytest.mark.parametrize("mode,want", [
    ("ahead", "main: ahead 1, behind 0 of origin/main (no fetch)"), ("behind", "main: ahead 0, behind 1 of origin/main (no fetch)"),
    ("noorigin", "main: ahead/behind unknown (origin/main missing)"), ("nomain", "main: ahead/behind unknown (main missing)"),
    ("norepo", "main: ahead/behind unknown (git exit "), ("nogit", "main: ahead/behind unknown (git not found)")])
def test_session_start_rules_file_and_main_sync(tmp_path, mode, want):
    root = mkrepo(tmp_path) if mode not in ("norepo", "nogit") else mkroot(tmp_path, ci=False)
    if mode not in ("norepo", "nogit"):
        a = commit(root, "a")
        b = commit(root, "b")
        if mode not in ("nomain", "noorigin"):
            git(root, "update-ref", "refs/remotes/origin/main", a if mode == "ahead" else b)
        if mode == "behind":
            git(root, "update-ref", "refs/heads/main", a)
        if mode == "nomain":
            git(root, "branch", "-m", "other")
    for source in ("startup", "resume", "clear", "compact"):  # the Lead's ruling: every source prints the line
        code, out = hook("session_start.py", ["--root", root], ROOT, json.dumps({"source": source}).encode(),
                         **({"PATH": ""} if mode == "nogit" else {}))
        assert code == 0 and want in out and "re-read: forge/BOOT.md" in out and "forge/COORDINATOR.md (Lead, Architect)" in out


def test_session_start_crash_and_cap(tmp_path, monkeypatch, capsys):
    root = mkroot(tmp_path, ci=False)
    put(root + "/forge/BOOT.md", "B" * 4096)
    put(root + "/forge/carriers.json", json.dumps([{"what goes there": "w" * 100, "carrier": "c"}] * 30))
    jl(root, *[("t" * 120 + str(i), "dispatch") for i in range(10)])
    out = start(root, "compact")[1]
    assert len(out.encode()) <= 6144 and "[cut: open list]" in out and "[cut: checklist]" in out and "B" * 4096 in out
    put(root + "/forge/carriers.json", "nope")
    assert "carriers checklist: forge/carriers.json malformed:" in start(root, "compact")[1]
    for n in ("x.md", "x-2.md", "x-10.md"):  # B2-3: by (stamp, suffix number), not by name
        put(root + "/logs/journal/snapshots/" + n, "")
    assert "snapshot: logs/journal/snapshots/x-10.md (~" in start(root, "resume")[1]
    with open(root + "/forge/BOOT.md", "wb") as fh:
        fh.write(b"\xff" * 4096)
    code, out = start(root, "clear")
    assert code == 0 and len(out.encode()) <= 6144 and out.rstrip("\n").count("\n") >= 1  # B2-6, edges line
    m = re.search(r"cut after file byte (\d+) of 4096, fix the file", out)  # k = file bytes whose text was printed
    assert m and int(m.group(1)) == out.count("�") < 4096 and out.rstrip().split("\n")[0].startswith("�")
    with open(root + "/forge/BOOT.md", "wb") as fh:
        fh.write(b"ab\xe2\x82cd")  # a bad multi-byte run: one U+FFFD (t-2018 M1)
    out = start(root, "clear")[1]
    assert "ab�cd\nforge/BOOT.md not UTF-8: shown with replacement characters, fix the file" in out and "cut" not in out
    put(root + "/forge/BOOT.md", "B")
    jl(root, ("t1", "dispatch"))
    pad = 6144 - len(start(root, "clear")[1])  # B2-5: a text AT the cap is emitted whole, one byte more cuts the list
    put(root + "/forge/BOOT.md", "B" * (1 + pad))  # t-2106 F1: ids are clipped now, so a valid BOOT carries the padding
    at = start(root, "clear")[1]
    put(root + "/forge/BOOT.md", "B" * (2 + pad))
    assert len(at.encode()) == 6144 and "[cut" not in at and "[cut: open list]" in start(root, "clear")[1]
    monkeypatch.setattr(sst, "compose", lambda *a: 1 / 0)
    assert sst.body(None, "", root) == 0 and "reminder failed: division by zero; read forge/BOOT.md by hand" in capsys.readouterr().out


# expected from: card B17 (c) (d) start facts; owner's word 27.11.2026: stable lines first, so the start text keeps the
# longest byte-equal prefix between sessions (prompt cache) -- BOOT, re-read, hooks, checklist, then the volatile lines
def test_session_start_order_stable_first(tmp_path):
    root = mkroot(tmp_path, ci=False)
    put(root + "/forge/BOOT.md", "BOOTTEXT")
    out = start(root, "compact")[1]
    at = [out.index(k) for k in ("BOOTTEXT", "re-read:", "hooks:", "carriers checklist", "now:", "main:", "old processes:",
                                 "worktrees:")]
    assert at == sorted(at) and re.search(r"now: \d{4}-\d\d-\d\d [A-Z][a-z]{2} \d\d:\d\d [+-]\d\d:\d\d \| last: ", out)


CMD_A, CMD_B = 'python "$CLAUDE_PROJECT_DIR/forge/hooks/a.py"', 'python -B "$CLAUDE_PROJECT_DIR/forge/hooks/b.py"'


@pytest.mark.parametrize("settings,want", [  # K5: wired, not wired, broken, unparsed
    (None, "harness 0 of 2 wired (no settings.json)"), ("nope", "harness ?"), ({"hooks": []}, "harness ?"),
    ({"hooks": {"SessionStart": [{"hooks": [{"command": CMD_A}]}], "PreToolUse": [{"hooks": [{"command": CMD_B}]}]}},
     "harness 2 of 2 wired"),
    ({"hooks": {"PreToolUse": [{"hooks": [{"command": CMD_A}, {"command": CMD_A.replace("a.py", "gone.py")},
                                          {"command": "bash x.sh"}]}]}},
     "harness 0 of 2 wired (not wired: a.py@SessionStart, b.py@PreToolUse) (1 broken) (1 unparsed)")])
def test_session_start_hooks_line(tmp_path, settings, want):
    root = str(tmp_path)
    put(root + "/forge/hooks/a.py", "# card: X\n# hook: SessionStart\n")
    put(root + "/forge/hooks/b.py", "# card: Y\n# hook: PreToolUse\n")
    put(root + "/forge/hooks/_io.py", "# card: Z\n")  # no `hook:` mark: not a harness hook
    if settings is not None:
        put(root + "/.claude/settings.json", settings if isinstance(settings, str) else json.dumps(settings))
    assert sst.harness_text(root, sst.harness_hooks(root)) == want


@pytest.mark.parametrize("path,want", [(None, "hooksPath unset, "), ("forge/hooks/git", "hooksPath ok, "),
                                       ("elsewhere", "hooksPath wrong: elsewhere, ")])
def test_session_start_git_hooks(tmp_path, path, want):
    root = mkrepo(tmp_path)
    put(root + "/forge/hooks/git/pre-push", "#!/bin/sh\n")
    put(root + "/forge/hooks/git/pre-commit", "#!/bin/sh\n")  # untracked
    put(root + "/forge/hooks/git/notes.md", "x")  # an extension: not a git hook
    git(root, "add", "--", "forge/hooks/git/pre-push")
    git(root, "update-index", "--chmod=+x", "forge/hooks/git/pre-push")
    if path:
        git(root, "config", "core.hooksPath", path)
    assert sst.git_hooks_text(root) == want + "1 of 2 tracked executable (1 untracked)"


def test_session_start_last_and_snapshot_age(tmp_path):
    e = lambda o: ("ts", "f", 1, "", o)  # noqa: E731 -- journal.load's entry shape
    assert sst.last_text([], False) == "? -- no journal" and sst.last_text([], True) == "no journal lines"
    long = {"ts": "T", "event": "accept", "task": "x\ny" + "z" * 200, "by": "lead"}
    assert sst.last_text([e(long)], True) == "T accept x\\u000ay" + "z" * 56 + " by lead"  # FH-4107: escaped, cut at 64
    assert sst.last_text([e(long), e(None)], True).endswith(" by lead (incomplete)")
    put(str(tmp_path) + "/logs/journal/snapshots/20261127T100000Z.md", "")
    now = datetime.datetime(2026, 11, 27, 12, 30, tzinfo=datetime.timezone.utc)
    assert sst.newest_snapshot(str(tmp_path), now) == "logs/journal/snapshots/20261127T100000Z.md (2h30m old)"
    assert sst.newest_snapshot(str(tmp_path), now + datetime.timedelta(days=3)).endswith("(3d02h old)")


def test_session_start_old_processes(tmp_path, monkeypatch):  # K6
    root, now, me = str(tmp_path / "forge2-repo"), 100000.0, os.getpid()
    rows = [(me, 2, now - 10, "python hook"), (2, 3, now - 9000, "claude " + root),  # this hook's ancestors: excluded
            (3, 1, now - 99999, "explorer"),
            (10, 3, now - 7200, "python " + root + "/x.py"),  # AT the limit: not listed
            (11, 99, now - 7201, 'python "%s/forge/tools/a.py" --x' % root),  # parent absent -> gone
            (12, 13, now - 8000, "C:\\" + "p" * 60 + "\\python.exe forge/tools/b.py --root " + root.replace("/", "\\")),
            (13, 3, now - 100, "sh"),  # created after 12: a reused pid -> 12's parent is gone
            (15, 3, now - 7300, root + "/run.cmd"),  # a live, older parent
            (16, 3, now - 9000, "node " + root + "-old/y.js"),  # a sibling prefix: not this tree
            (17, 3, now - 9100, "node D:\\wt\\other\\z.js")]  # a linked worktree outside the root: listed
    monkeypatch.setattr(sst, "process_list", lambda now_s: (rows, 1, ""))
    wt = ([{"worktree": root}, {"worktree": "D:/wt/other"}], None)
    full, short = sst.old_text(root, now, wt)
    assert full.startswith("old processes: 4 started from this tree, older than 7200 s: 17 2h31m parent 3 node D:\\wt\\other\\z.js; ")
    assert "; 12 2h13m parent gone python.exe forge/tools/b.py --root " in full and "; 15 2h01m parent 3 " in full
    assert "; 11 2h00m parent gone python " in full and full.endswith(" (1 rows unreadable)")
    assert all(" %d " % p not in full for p in (me, 2, 10, 16))
    assert short == "old processes: 4 started from this tree, older than 7200 s [cut: rows] (1 rows unreadable)"
    for n, more in ((5, False), (6, True)):
        monkeypatch.setattr(sst, "process_list", lambda now_s: ([(100 + i, 1, now - 7300 - i, "x " + root) for i in range(n)], 0, ""))
        assert sst.old_text(root, now, wt)[0].endswith(" and 1 more") == more
    monkeypatch.setattr(sst, "process_list", lambda now_s: (None, 0, "process list slower than 5 s"))
    assert sst.old_text(root, now, wt)[0] == "old processes: ? (process list slower than 5 s)"


def test_session_start_process_parsers_and_budget(tmp_path, monkeypatch):
    nt = '[{"ProcessId":5,"ParentProcessId":1,"CreationDate":"/Date(1000)/","CommandLine":null},{"ProcessId":6}]'
    assert sst.parse_nt(nt) == [(5, 1, 1.0, ""), None] and sst.parse_ps(" 5 1 30 python x\nbad\n", 100) == [(5, 1, 70, "python x"), None]
    monkeypatch.setattr(sst, "T0", time.monotonic())  # the hook started now ...
    monkeypatch.setattr(sst, "START_BUDGET_S", 0)  # ... and its budget is spent: a call past it never starts
    assert sst.main_sync(str(tmp_path)) == "main: ahead/behind unknown (not collected: start budget)"
    assert sst.old_text(str(tmp_path), 0, (None, "x"))[0] == "old processes: ? (not collected: start budget)"
    assert sst.worktrees_text(sst.worktree_blocks(str(tmp_path)), [], "ok", [])[0] == "worktrees: ? -- not collected: start budget"


# expected from: t-2106 verdict F1-F7 and card B17 (c) (d) edges; each row names its finding
def test_session_start_f1_outside_values(tmp_path):  # F1: a newline id and a lone surrogate never forge a line or kill the print
    root = mkroot(tmp_path, ci=False)
    jl(root, ("a\nb: injected", "dispatch"), ("x\ud800", "dispatch"))
    code, out = start(root, "startup")
    assert code == 0 and "\nb: injected" not in out and "open: a\\u000ab: injected, x" in out and "reminder failed" not in out
    assert sst.emitted("x\ud800") == 3 and sst.previous([("t\nz", "f", 1, "", {"event": "d"})], True).endswith("after t\\u000az -- read the snapshot")


def test_session_start_f2_git_failure_is_unknown(tmp_path, monkeypatch):  # F2: AR-27/AR-28, a failed call is `?`, never `0 of n`
    root = mkrepo(tmp_path)
    put(root + "/forge/hooks/git/pre-push", "#!/bin/sh\n")
    real = sst.git_out
    monkeypatch.setattr(sst, "git_out", lambda r, *a: (None, "git exit 128") if "ls-files" in a else real(r, *a))
    assert sst.git_hooks_text(root) == "hooksPath unset, 1 files, tracked ? (git exit 128)"
    monkeypatch.setattr(sst, "START_BUDGET_S", 0)
    monkeypatch.setattr(sst, "T0", time.monotonic())
    monkeypatch.setattr(sst, "git_out", real)
    assert sst.git_hooks_text(root) == "? (not collected: start budget)"


def test_session_start_f3_f4_f6(tmp_path, monkeypatch):
    seen = []  # F3: T0 is taken in run() before guard reads stdin
    monkeypatch.setattr(sst, "T0", None)
    monkeypatch.setattr(sst.HIO, "guard", lambda *a: seen.append(sst.T0))
    sst.run(["--root", str(tmp_path)])
    assert seen[0] is not None
    root = mkrepo(tmp_path / "r")  # F4: one `git worktree list` per run; F6: a linked worktree reads the main checkout's hooks
    commit(root, "a")
    put(root + "/forge/hooks/git/pre-push", "#!/bin/sh\n")
    git(root, "config", "core.hooksPath", "forge/hooks/git")
    git(root, "worktree", "add", "-q", str(tmp_path / "wt"), "-b", "w/t1")
    calls, real = [], sst.git_out
    monkeypatch.setattr(sst, "git_out", lambda r, *a: calls.append(a) or real(r, *a))
    monkeypatch.setattr(sst, "T0", None)
    sst.compose(str(tmp_path / "wt"), "resume", False)
    assert sum(a[:2] == ("worktree", "list") for a in calls) == 1
    # N1: git resolves a relative hooksPath in the worktree it runs in; the linked one has no such folder -> wrong
    assert sst.git_hooks_text(str(tmp_path / "wt")) == "hooksPath wrong: forge/hooks/git, 0 of 1 tracked executable (1 untracked)"
    assert sst.git_hooks_text(root).startswith("hooksPath ok")


class Run:
    def __init__(self, out=b"", code=0, boom=None):
        self.stdout, self.returncode, self.boom = out, code, boom

    def __call__(self, *a, **k):
        if self.boom:
            raise self.boom
        return self


@pytest.mark.parametrize("res,why", [  # F7: the process_list battery of card B17 (d)
    (Run(boom=subprocess.TimeoutExpired("ps", 5)), "process list slower than 5 s"), (Run(b""), "process list exit 0, 0 bytes"),
    (Run(b"nope"), "process list unreadable: Expecting value"), (Run(b"\xff"), "process list unreadable: 'utf-8' codec"),
    (Run(b"[1]", 0), "all rows unreadable"), (Run(b"[]", 1), "process list exit 1, 2 bytes"),
    (Run(boom=OSError("denied")), "process list unreadable: denied")])
def test_session_start_f7_process_list(monkeypatch, res, why):
    monkeypatch.setattr(sst.subprocess, "run", res)
    monkeypatch.setattr(sst.os, "name", "nt")
    rows, _, got = sst.process_list(0)
    assert rows is None and got.startswith(why)


def test_session_start_f7_rows_and_long_command(monkeypatch):
    big = [{"ProcessId": i, "ParentProcessId": 1, "CreationDate": "/Date(1000)/", "CommandLine": "x" * 65536 if i == 0 else "p"}
           for i in range(10000)]
    monkeypatch.setattr(sst.subprocess, "run", Run(json.dumps(big).encode()))
    monkeypatch.setattr(sst.os, "name", "nt")
    rows, bad, _ = sst.process_list(0)
    assert len(rows) == 10000 and bad == 0 and len(sst.head(rows[0][3])) <= 64 
    # N2: past the CMD_MAX cut a path is not found, inside it is
    assert not sst.from_tree("x" * 65536 + " /zz/a", ["/zz"]) and sst.from_tree("x" * 100 + " /zz/a", ["/zz"])


def test_session_start_worktrees(tmp_path):
    root = mkrepo(tmp_path / "r")
    commit(root, "a")
    for br in ("w/t1", "w/t2", "w/t3", "other"):
        git(root, "worktree", "add", "-q", str(tmp_path / br.replace("/", "-")), "-b", br)
    jl(root, ("t1", "dispatch"), ("t2", "dispatch"), ("t2", "accept"))
    out = start(root, "startup")[1]
    assert "worktrees: 4 linked\n" in out and "(w/t1) -- task open" in out and "(w/t2) -- task closed" in out
    assert "(w/t3) -- state unknown: task never dispatched" in out and "(other) -- state unknown: no task in branch name" in out


def fx(tmp_path, ctx=None, role="builder", out=1000, handoff=True, caps=True, lines_n=1):
    """B5 fixture: a root with caps.json, a worker transcript (dispatch lines, then one usage line of ctx tokens)."""
    root = mkroot(tmp_path / "r", ci=False)
    if caps:
        shutil.copy(os.path.join(ROOT, "forge", "caps.json"), root + "/forge/caps.json")
    tp = str(tmp_path / "t" / "sess.jsonl")
    disp = ("role: %s\n" % role if role else "") + ("handoff: %s\n" % (tmp_path / "rep.md") if handoff else "")
    lines = [{"type": "user", "message": {"role": "user", "content": [{"type": "text", "text": disp}]}}]
    if ctx is not None:
        u = {"input_tokens": ctx - 100, "cache_creation_input_tokens": 50, "cache_read_input_tokens": 50, "output_tokens": out}
        lines += [{"type": "assistant", "message": {"id": "m1", "usage": u}}] * lines_n
    put(tp.replace(".jsonl", "") + "/subagents/agent-a1.jsonl", "".join(json.dumps(x) + "\n" for x in lines))
    return root, tp


def call(root, tp, tool="Read", agent="a1", age=None, seed={}, **ti):
    if age is not None:  # wall: the sidecar says the worker's first call was `age` s ago
        put(root + "/logs/budget/%s.json" % agent, json.dumps({"t0": time.time() - age, "role": "builder", "task": "t-1", **seed}))
    p = {"session_id": "s1", "transcript_path": tp, "agent_id": agent, "tool_name": tool, "tool_input": ti, "cwd": root}
    return hook("budget.py", ["--root", root], root, json.dumps(p).encode())


def events(root):
    return [json.loads(x) for x in open(root + "/logs/journal/s1.jsonl")] if os.path.exists(root + "/logs/journal/s1.jsonl") else []


@pytest.mark.parametrize("tool,ti,code", [
    ("SubagentHandback", {"message": "x"}, 0), ("Write", {"file_path": "REP"}, 0), ("Edit", {"file_path": "REP"}, 0),
    ("Write", {"file_path": "other.md"}, 2), ("Read", {"file_path": "x"}, 2), ("Bash", {"command": "git commit -m x"}, 0),
    ("Bash", {"command": "git diff --stat"}, 0), ("Bash", {"command": "git status && rm -r ."}, 2),
    ("PowerShell", {"command": "git add -A; git push"}, 2), ("Bash", {"command": "git push"}, 2), ("Bash", {"command": "ls"}, 2),
    ("Bash", {"command": "git add logs/budget/a1.json"}, 2)])  # t-2045 M1: a cut worker's plain git naming the state stays refused
def test_budget_cut_passes_only_three_moves(tmp_path, tool, ti, code):
    root, tp = fx(tmp_path, 400000)
    ti = {k: str(tmp_path / "rep.md") if v == "REP" else v for k, v in ti.items()}
    got = call(root, tp, tool, **ti)
    assert got[0] == code and (code == 0 or "budget cut: role:builder tokens 400000 of 400000" in got[1])
    assert [e["event"] for e in events(root)] == ["cut"] and events(root)[0]["note"].startswith("role:builder tokens 400000 of 400000")


@pytest.mark.parametrize("ctx,age,want", [
    (249999, None, ""), (250000, None, "role:builder tokens 250000 of 250000 spend 251000"),
    (399999, None, "tokens 399999 of 250000"), (None, 2879, ""), (None, 2880, "role:builder wall 2880 of 2880 s"),
    (None, 3599, "wall 3599 of 2880 s")])
def test_budget_warn_once_at_and_beyond(tmp_path, ctx, age, want):
    root, tp = fx(tmp_path, ctx)
    got = call(root, tp, age=age)
    again = call(root, tp)
    ev = [e for e in events(root) if e["event"] == "cap_warning"]
    assert got[0] == again[0] == 0 and (want in got[1]) and "write what is done" not in again[1] and len(ev) == bool(want)
    assert not want or ev[0]["note"].startswith("role:builder ")


def test_budget_warn_on_refused_shell_call_shown_and_journaled_once(tmp_path):  # expected from: t-2045 F1
    root, tp = fx(tmp_path, 300000)
    got = call(root, tp, "Bash", command="grep x logs/budget/a1.json")
    again = call(root, tp, "Bash", command="grep x logs/budget/a1.json")
    assert got[0] == again[0] == 2 and "tokens 300000 of 250000" in got[1] and "write what is done" not in again[1]
    assert [e["event"] for e in events(root)] == ["cap_warning", "refuse"]


@pytest.mark.parametrize("age,ctx", [(3599, None), (3600, None), (3601, 10)])
def test_budget_wall_cut_and_unreadable_transcript(tmp_path, age, ctx):
    root, tp = fx(tmp_path, ctx)
    got = call(root, tp.replace("sess", "gone") if ctx is None else tp, age=age)
    assert got[0] == (2 if age > 3599 else 0) and ("tokens unmeasured" in got[1]) == (ctx is None) and got[1].count("tokens unmeasured") == (ctx is None)
    assert (call(root, tp.replace("sess", "gone"))[0] == 2 or age < 3600) and ("cut" in str(events(root))) == (age > 3599)
    assert ctx is not None or age < 3600 or "wall 3600 of 3600 s spend unmeasured" in events(root)[0]["note"]  # F2


@pytest.mark.parametrize("role", [None, "wizard", "main"])
def test_budget_unknown_role_is_strictest_row(tmp_path, role):
    root, tp = fx(tmp_path, 260000, role)
    got = call(root, tp)
    assert got[0] == 0 and got[1].count("strictest row") == 1 and "role:unknown tokens 260000 of 250000" in str(events(root))
    assert "strictest" not in call(root, tp)[1]


@pytest.mark.parametrize("ctx,had,levels", [(299999, 0, 0), (300000, 0, 1), (349999, 1, 0), (350000, 1, 1), (400000, 2, 1)])
def test_budget_main_warned_never_cut(tmp_path, ctx, had, levels):
    root, tp = fx(tmp_path, ctx)
    put(tp, json.dumps({"type": "assistant", "message": {"usage": {"input_tokens": ctx}}}) + "\n")
    put(root + "/logs/budget/main-s1.json", json.dumps({"t0": 1, "level_tokens": had}))
    got = call(root, tp, agent=None)
    assert got[0] == 0 and len(events(root)) == levels and (levels == 0 or "spend %d" % ctx in got[1])


CAPS = json.load(open(os.path.join(ROOT, "forge", "caps.json")))
WORKERS, MAIN = json.dumps([r for r in CAPS if r["role"] != "main"]), json.dumps([r for r in CAPS if r["role"] == "main"])


# F6: absent, unparsable, malformed by type or by field; t-2032 N3 (Lead ruling): a role's caps are usable only when its own
# row is -- P3 (worker rows, no main) cuts a worker and is missing for main, P3b (main row only) is missing for a worker
@pytest.mark.parametrize("caps,agent,code", [
    (None, "a1", 0), ("nope", "a1", 0), ('[{"role": "main", "tokens_warn": "x"}]', "a1", 0), ('[{"role": "builder"}]', "a1", 0),
    (WORKERS, None, 0), (MAIN, "a1", 0), (WORKERS, "a1", 2)])
def test_budget_caps_usable_per_role(tmp_path, caps, agent, code):
    root, tp = fx(tmp_path, 900000, caps=False)
    if caps:
        put(root + "/forge/caps.json", caps)
    got = [call(root, tp, "Bash", agent=agent, command="rm -rf /") for _ in range(2)]
    assert [g[0] for g in got] == [code] * 2 and all(("caps missing" in g[1]) == (not code) for g in got)
    assert len(events(root)) == (code == 2)


@pytest.mark.parametrize("agent,had,role", [("a1", "builder", "builder"), ("a1", "main", "unknown"), (None, "builder", "main")])
def test_budget_crash_passes_and_journals_role(tmp_path, monkeypatch, agent, had, role):  # F3; t-2032 N2: cap notes' mapping
    import budget as bd
    root, tp = fx(tmp_path, 10)
    put(root + "/logs/budget/a1.json", json.dumps({"t0": 1, "role": had}))
    monkeypatch.setattr(bd, "evaluate", lambda *a: 1 / 0)
    assert bd.body({"session_id": "s1", "agent_id": agent}, "", root) == 0
    assert [e["event"] for e in events(root)] == ["hook_failed"] and events(root)[0]["note"].startswith("role:%s budget: Zero" % role)


def test_budget_spend_counts_a_message_once_and_main_has_no_stop(tmp_path):  # F1, F5
    root, tp = fx(tmp_path, 260000, lines_n=3)
    assert "tokens 260000 of 250000 spend 261000" in call(root, tp)[1]
    root, tp = fx(tmp_path / "m", 360000)
    put(root + "/forge/caps.json", open(root + "/forge/caps.json").read().replace('"tokens_stop": null', '"tokens_stop": 350000'))
    put(tp, json.dumps({"type": "assistant", "message": {"usage": {"input_tokens": 360000}}}) + "\n")
    assert call(root, tp, agent=None)[0] == 0


def test_budget_cut_edges(tmp_path):  # F7: no handoff line; t-2032 N1: a torn sidecar after a cut stays a cut; F9; F12
    root, tp = fx(tmp_path, 400000, handoff=False)
    assert call(root, tp, "Write", file_path=str(tmp_path / "rep.md"))[0] == 2 and call(root, tp, "SubagentHandback")[0] == 0
    side = root + "/logs/budget/a1.json"
    put(side, "{torn")
    got = [call(root, tp, t)[0] for t in ("Read", "SubagentHandback", "Read")]
    lost = [e["event"] for e in events(root) if "budget state unreadable" in e["note"]]
    assert got == [2, 0, 2] and lost == ["cut"] and "cut" in json.load(open(side))["said"]
    root, tp = fx(tmp_path / "b", 10)
    assert call(root, tp.replace("sess", "gone"))[0] == 0 and call(root, tp)[0] == 0  # dispatch unreadable at call 1, read at call 2
    got = json.load(open(root + "/logs/budget/a1.json"))
    assert (got["role"], got["handoff"]) == ("builder", str(tmp_path / "b" / "rep.md"))
    put(tp[:-6] + "/subagents/agent-a2.jsonl", json.dumps({"type": "user", "message": {"content": "x"}}) + "\n")
    assert ["no usage line" in call(root, tp, agent="a2")[1] for _ in range(3)] == [False, True, False]


# t-2032 N1 (Lead ruling, card B5 invariant "no call after the cap passes except the three moves"): a state that cannot be
# proved is a cut, journaled once; a Write naming logs/budget/ is a cut; t-2036 T1 (Lead ruling): a shell command naming it,
# a plain git move included, is refused for that call only, journaled once as `refuse`, and the next call passes
@pytest.mark.parametrize("side,ctx,tool,ti,cause,after,event", [
    ("{}", 900000, "Read", {}, "budget state unreadable", 2, "cut"),
    ('{"t0": 1, "said": 5}', 10, "Read", {}, "budget state unreadable", 2, "cut"),
    (None, 10, "Write", {"file_path": "SIDE"}, "tampering", 2, "cut"),
    (None, 10, "Bash", {"command": "git add logs\\budget\\a1.json"}, "Grep tool", 0, "refuse"),
    (None, 10, "PowerShell", {"command": "Select-String x logs/Budget/a1.json"}, "Grep tool", 0, "refuse")])
def test_budget_state_fail_closed(tmp_path, side, ctx, tool, ti, cause, after, event):
    root, tp = fx(tmp_path, ctx)
    if side:
        put(root + "/logs/budget/a1.json", side)
    ti = {k: v.replace("SIDE", root + "/logs/budget/a1.json") for k, v in ti.items()}
    got = [call(root, tp, tool, **ti) for _ in range(2)] + [call(root, tp)]
    evs = events(root)
    assert [g[0] for g in got] == [2, 2, after] and cause in got[0][1]
    assert [e["event"] for e in evs] == [event] and (event == "refuse" or cause in evs[0]["note"])


@pytest.mark.parametrize("side", ["{torn", '{"t0": 1, "said": 5}'])
def test_budget_main_lost_state_line_only(tmp_path, side):  # t-2036 R1: main is never cut, its unreadable sidecar a line
    root, tp = fx(tmp_path, 900000)
    put(root + "/logs/budget/main-s1.json", side)
    got = [call(root, tp, agent=None) for _ in range(2)]
    assert [g[0] for g in got] == [0, 0] and all("main is never cut" in g[1] for g in got) and not events(root)
    assert open(root + "/logs/budget/main-s1.json").read() == side


@pytest.mark.parametrize("fails,written", [(6, False), (2, True)])
def test_budget_save_retries_then_cleans(tmp_path, monkeypatch, capsys, fails, written):  # t-2032 N4 (edges line)
    import budget as bd
    real, tries = os.replace, []

    def flaky(a, b):
        tries.append(a)
        if len(tries) <= fails:
            raise PermissionError(13, "held by a reader")
        real(a, b)
    monkeypatch.setattr(bd.os, "replace", flaky)
    monkeypatch.setattr(bd.time, "sleep", lambda s: None)
    bd.save(str(tmp_path / "b" / "a1.json"), bd.fresh())
    assert len(tries) == min(fails + 1, 6) and os.listdir(tmp_path / "b") == (["a1.json"] if written else [])
    assert ("budget: state not written" in capsys.readouterr().err) != written


def test_budget_newest_line_without_usage_keeps_last_value(tmp_path):
    root, tp = fx(tmp_path, 260000)
    with open(tp.replace(".jsonl", "") + "/subagents/agent-a1.jsonl", "a") as fh:
        fh.write(json.dumps({"type": "user", "message": {"content": "r" * 80000}}) + "\n")
    assert "tokens 260000 of 250000 spend 261000" in call(root, tp)[1]


def test_codex_budget_reads_dispatch_and_cumulative_usage(tmp_path):
    import budget

    path = tmp_path / "rollout.jsonl"
    dispatch = {"type": "event_msg", "payload": {"type": "user_message", "message": "role: builder\ntask: fixture"}}
    event = {"type": "event_msg", "payload": {"type": "token_count", "info": {
        "last_token_usage": {"input_tokens": 300}, "total_token_usage": {"total_tokens": 700}}}}
    path.write_text("\n".join(map(json.dumps, [dispatch, event, event])) + "\n", encoding="utf-8")
    worker, key, transcript = budget.keys({"forge_host": "codex", "agent_id": "fixture-worker", "transcript_path": str(path)})
    assert (worker, key, transcript) == (True, "fixture-worker", str(path))
    state = budget.fresh()
    budget.read_dispatch(state, transcript)
    assert state["role"] == "builder" and state["task"] == "fixture"
    assert budget.scan(transcript, state, codex=True)
    assert (state["ctx"], state["spend"]) == (300, 700)


@pytest.mark.parametrize("name,stdin,args,seen", [
    ("pre-commit", b"", [], "env-file"),
    ("pre-push", b"invalid ref line\n", ["origin", "o"], "cannot judge pushed line"),
])
def test_git_launches_hook_interpreter(tmp_path, name, stdin, args, seen):
    root = mkrepo(tmp_path / "g")
    hook_dir = tmp_path / "g" / "forge" / "hooks"
    shutil.copytree(HOOKS, hook_dir, ignore=shutil.ignore_patterns("__pycache__"))
    put(root + "/.env", "FIXTURE=1\n")
    git(root, "add", "-f", "--", ".env")
    input_file = tmp_path / "hook-stdin"
    input_file.write_bytes(stdin)
    code, out = git(root, "-c", "core.hooksPath=forge/hooks/git", "hook", "run", f"--to-stdin={input_file}", name, "--", *args)
    assert code == 1 and f"{name}: refused" in out and seen in out


# expected from: C1-5 foreign-write refusal and B5 edit-path budget checks.
@pytest.mark.parametrize("name,inputs,code", [
    (None, None, 0),
    ("other", None, 0),
    ("Bash", {"command": "Get-Location", "shell": "pwsh", "workdir": "{root}"}, 0),
    ("apply_patch", {"command": "*** Begin Patch\n*** End Patch"}, 0),
    ("apply_patch", {"command": "*** Add File: safe.txt\n*** Update File: also-safe.txt"}, 0),
    ("apply_patch", {"command": "*** Update File: safe.txt\n*** Move to: {root}/outside/new.txt"}, 2),
])
def test_codex_hook_event_dispatch(tmp_path, monkeypatch, capsys, name, inputs, code):
    import codex_hook

    root = tmp_path.as_posix()
    monkeypatch.setattr(codex_hook, "ROOT", root)
    put(root + "/forge/hooks/protected-roots.json", json.dumps({"roots": [root + "/outside"]}))
    shutil.copyfile(os.path.join(ROOT, "forge", "caps.json"), root + "/forge/caps.json")
    tool_input = {k: v.replace("{root}", root) for k, v in inputs.items()} if inputs else inputs
    payload = {"tool_name": name, "tool_input": tool_input, "session_id": "fixture", "cwd": root}
    assert codex_hook.body(payload if name else None, "empty input") == code
    if code:
        assert "foreign_write: refused" in capsys.readouterr().err
