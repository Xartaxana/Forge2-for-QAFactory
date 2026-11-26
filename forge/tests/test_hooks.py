# card: C1-5
"""Tool tests of card C1-5 (hooks, the one secret table). Pure functions run in-process; a real git fixture only where git
itself is the thing judged. Every git subprocess runs with all GIT_* variables removed (GIT_DIR, GIT_INDEX_FILE: an
inherited one would aim a fixture at the real repository). Tokens are built at run time, never written here."""
import importlib.machinery
import importlib.util
import json
import os
import shutil
import subprocess
import sys

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
    for a in (["init", "-q"], ["symbolic-ref", "HEAD", "refs/heads/main"], ["config", "user.name", "t"],
              ["config", "user.email", "t@t"], ["config", "core.autocrlf", "false"]):
        git(p, *a)
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
    line =lambda new, old=Z, ref="refs/heads/main": [(ref, new, ref, old)]  # noqa: E731
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
def test_crash_git_absent(tmp_path, name, stdin):
    empty = tmp_path / "nobin"
    empty.mkdir()
    code, out = hook(name, ["origin", "o"], mkrepo(tmp_path / "r"), stdin, PATH=str(empty))
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
def steps(tmp_path, monkeypatch, remote, url="o", ents=(), msg="m", ref="refs/heads/main", ci=0, blob="clean"):
    root = mkroot(tmp_path, remote if remote != "absent" else None, ci is not None)
    if remote == "absent":
        os.remove(root + "/forge/remote.json")
    if ci:
        put(root + "/ci-exit", str(ci))
    msgs = [msg] if isinstance(msg, str) else msg  # one message per commit, the tip first
    ids = [c * 40 for c in "cd"][:len(msgs)]
    monkeypatch.setattr(ss, "git", lambda r, *a: msgs[ids.index(a[-1])].encode() if a[0] == "log" else (b"c" * 40 + b"\n")
                        if a[0] == "rev-parse" else blob.encode())
    monkeypatch.setattr(ss, "walk", lambda r, revs: (ids, [("c" * 40, p, "s" + p) for p in ents]))
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
         ("GIT_DIR=%s/.git git commit" % P, 1), ("GIT_WORK_TREE=%s git add ." % P, 1)]
POWER = [("Set-Content -Path \"%s/a\" -Value x" % P, 1), ("set-content C:\\Prot\\Root\\a x", 1), ("Remove-Item %s/a -Force" % P, 1),
         ("Copy-Item %s/a C:/work/b" % P, 0), ("Copy-Item C:/work/a -Destination %s/b" % P, 1), ("\"x\" | Out-File %s/a" % P, 1),
         ("echo x > %s/a" % P, 1), ("Get-Content %s/a" % P, 0), ("Move-Item %s/a C:/work/b" % P, 1),
         ("Set-Content `\n  -Path %s/a -Value 1" % P, 1)]


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
