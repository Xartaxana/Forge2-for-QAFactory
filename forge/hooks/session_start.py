# card: B2
"""SessionStart hook (card B2): prints what to re-read at a session start and after a compaction. It prints only, exit 0.

session_start.py [--root D]   D defaults to this repository. Input: the event JSON on stdin, field `source`
(startup|resume|clear|compact); empty, broken or unknown -> as startup.
Blocks: (1) forge/BOOT.md on startup|clear|compact; (2) the re-read line, always; (3) the carriers checklist on compact;
(4) the previous session's end on startup; (5) on every source one line `main: ahead <a>, behind <b> of origin/main (no fetch)`, or
`main: ahead/behind unknown (<why>)` (S10). Any error -> one line `reminder failed: <error>; read forge/BOOT.md by hand`.
Cap 6144 emitted bytes: the open list is cut first, then the checklist, each with a `[cut: <what>]` marker; a valid
UTF-8 BOOT never; a non-UTF-8 BOOT last, to the cap, then a marker line: `shown with replacement characters` or `cut after file byte <k> of <total>`.
The hook is inert until the Lead registers it in .claude/settings.json (the net is not the guarantee: the gates are).
"""
import glob
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from hio import io as HIO  # noqa: E402

CAP = 6144
OPEN_MAX = 10
GIT_WAIT_S = 5
BOOT_SOURCES = ("startup", "clear", "compact")


def boot_block(root, eval_arm, show):
    """Return (text, present, bad). Presence is read on every source (t-2010 B2-1/B2-2); the text only when `show`.
    In an eval arm an absent BOOT prints nothing (B1's `without` arm, F3). bad: the raw bytes of a non-UTF-8 BOOT."""
    p = os.path.join(root, "forge", "BOOT.md")
    if not os.path.isfile(p):
        return ("" if eval_arm or not show else "forge/BOOT.md not written yet (B1)"), False, None
    if not show:
        return "", True, None
    with open(p, "rb") as fh:
        raw = fh.read()
    try:
        return raw.decode("utf-8"), True, None
    except UnicodeDecodeError:
        return "", True, raw


def span(raw, i):
    """(text, byte length) of the character at raw[i]: a valid one as is, a bad byte run as one U+FFFD."""
    chunk = raw[i:i + 4]
    try:
        ch = chunk.decode("utf-8")[0]
    except UnicodeDecodeError as exc:
        if exc.start == 0:
            return chr(0xFFFD), max(1, exc.end)
        ch = chunk[:exc.start].decode("utf-8")[0]
    return ch, len(ch.encode("utf-8"))


def bad_boot(raw, n):
    """The non-UTF-8 BOOT shown with replacement characters, cut to n text bytes at a character edge, then one marker line
    saying which: nothing cut, or cut after file byte k of the total (k = file bytes whose text was printed; t-2016 B2-N1)."""
    kept, used, k = [], 0, 0
    while k < len(raw):
        ch, size = span(raw, k)
        if used + len(ch.encode("utf-8")) > n:
            break
        kept.append(ch)
        used += len(ch.encode("utf-8"))
        k += size
    if k >= len(raw):
        return "".join(kept) + "\nforge/BOOT.md not UTF-8: shown with replacement characters, fix the file"
    return "".join(kept) + "\nforge/BOOT.md not UTF-8: cut after file byte %d of %d, fix the file" % (k, len(raw))


def open_text(status, tasks, bad):
    if status == "unknown":
        return "unknown -- no journal"
    more = " and %d more" % (len(tasks) - OPEN_MAX) if len(tasks) > OPEN_MAX else ""
    text = (", ".join(tasks[:OPEN_MAX]) + more) or "none"
    return text + (" (incomplete: %d unreadable journal lines)" % len(bad) if status == "incomplete" else "")


def snap_key(name):
    """(stamp, suffix number): snapshot.py names a second snapshot of one second `<stamp>-2.md` (t-2010 B2-3)."""
    m = re.match(r"^(.*?)(?:-(\d+))?\.md$", name)
    return (m.group(1), int(m.group(2) or 1)) if m else (name, 0)


def newest_snapshot(root):
    names = sorted((os.path.basename(n) for n in glob.glob(os.path.join(root, "logs", "journal", "snapshots", "*.md"))),
                   key=snap_key)
    return "logs/journal/snapshots/" + names[-1] if names else "none yet"


def checklist(root):
    """The rows come from snapshot.carriers(), the one reader (t-2010 B2-4): one wording for absent and malformed."""
    sys.path.insert(0, os.path.join(HERE, "..", "tools"))
    import snapshot  # noqa: E402 -- lazily, like journal in compose
    rows, error = snapshot.carriers(root)
    return "carriers checklist: " + error if error else "\n".join(["carriers checklist:"] + ["- " + r for r in rows])


def previous(entries, found):
    """Block (4): the last parsed journal line decides; a session_end last means the session was closed."""
    parsed = [e for e in entries if e[4]]
    if not found:
        return "previous session: unknown -- no journal"
    if parsed and parsed[-1][4].get("event") == "session_end":
        return "previous session: closed %s" % parsed[-1][0]
    return "previous session: no session_end after %s -- read the snapshot" % (parsed[-1][0] if parsed else "(no journal line)")


def render(p, cut_open, cut_list):
    """p: the parts dict; the open list and the checklist are the two cuttable pieces."""
    line = "%ssnapshot: %s | open: %s" % (p["field"], p["snap"], "[cut: open list]" if cut_open else p["open"])
    check = ("[cut: checklist]" if cut_list else p["check"]) if p["check"] else ""
    return "\n".join(x for x in (p["boot"], line, p.get("git", ""), check, p["prev"]) if x)


def emitted(text):
    """The bytes that leave the hook: the text and the one `\\n` emit() adds (t-2010 B2-5)."""
    return len(text.encode("utf-8")) + 1


def fit(p):
    """The whole text, then without the open list, then without the checklist too. A valid UTF-8 BOOT is never cut;
    a non-UTF-8 one (p["bad"]) is cut last, to the cap, with a marker line (t-2010 B2-6)."""
    if p.get("bad") is not None:
        p = dict(p, boot=bad_boot(p["bad"], CAP))
    for cut_open, cut_list in ((False, False), (True, False), (True, True)):
        text = render(p, cut_open, cut_list)
        if emitted(text) <= CAP:
            return text
    if p.get("bad") is None:
        return text
    n = CAP
    while True:
        text = render(dict(p, boot=bad_boot(p["bad"], n)), True, True)
        if emitted(text) <= CAP or n <= 0:
            return text
        n -= max(1, emitted(text) - CAP)


def git_out(root, *args):
    """(stdout, None) of one git command in root, or (None, why): absent, failing or slower than GIT_WAIT_S. Never a fetch."""
    try:
        r = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, timeout=GIT_WAIT_S)
    except FileNotFoundError:
        return None, "git not found"
    except subprocess.TimeoutExpired:
        return None, "git slower than %d s" % GIT_WAIT_S
    except OSError as exc:
        return None, "git failed: %s" % exc
    if r.returncode:
        return None, "git exit %d" % r.returncode
    return r.stdout, None


def main_sync(root):
    """Plan S10: how far the local `main` is from `origin/main` (refs are shared by worktrees), from the refs as they are --
    no fetch. A missing ref or a failing git is said as unknown, never an error (the hook exits 0 anyway)."""
    for ref in ("main", "origin/main"):
        got, why = git_out(root, "rev-parse", "--verify", "--quiet", ref + "^{commit}")
        if got is None and why != "git exit 1":
            return "main: ahead/behind unknown (%s)" % why
        if got is None:
            return "main: ahead/behind unknown (%s missing)" % ref
    got, why = git_out(root, "rev-list", "--left-right", "--count", "main...origin/main")
    nums = (got or "").split()
    if len(nums) != 2 or not all(n.isdigit() for n in nums):
        return "main: ahead/behind unknown (%s)" % (why or "unreadable git output")
    return "main: ahead %s, behind %s of origin/main (no fetch)" % tuple(nums)


def compose(root, source, eval_arm):
    sys.path.insert(0, os.path.join(HERE, "..", "tools"))
    import journal  # noqa: E402 -- lazily: a broken journal.py is a fallback line, not a crash at import
    loaded = journal.load(root)
    status, tasks, bad = journal.open_tasks(root, loaded)
    boot, present, badtext = boot_block(root, eval_arm, source in BOOT_SOURCES)
    rules = ", forge/COORDINATOR.md (Lead, Architect) | "  # plan S6: workers get no SessionStart; the Lead's rules file is named here
    field = "re-read: forge/BOOT.md" + rules if present else "" if eval_arm else "re-read: forge/BOOT.md (not written yet, B1)" + rules
    return fit({"boot": boot, "bad": badtext, "field": field, "git": main_sync(root),
                "snap": newest_snapshot(root), "open": open_text(status, tasks, bad),
                "check": checklist(root) if source == "compact" else "",
                "prev": previous(loaded[0], loaded[2]) if source == "startup" else ""})


def emit(text):
    """Bytes with `\\n` to stdout: Windows' text layer would turn each `\\n` into `\\r\\n` and break the cap count."""
    sys.stdout.flush()
    data = (text + "\n").encode("utf-8")
    try:
        sys.stdout.buffer.write(data)
        sys.stdout.buffer.flush()
    except AttributeError:
        print(text)


def body(value, note, root):
    source = value.get("source") if value else None
    if source not in ("startup", "resume", "clear", "compact"):
        source = "startup"
    try:
        emit(compose(root, source, bool(os.environ.get("FORGE_EVAL_ARM"))))
    except Exception as exc:  # noqa: BLE001 -- the hook never blocks or delays work (K1)
        print("reminder failed: %s; read forge/BOOT.md by hand" % exc)
    return 0


def run(argv):
    root = os.path.dirname(os.path.dirname(HERE))
    if argv[:1] == ["--root"] and len(argv) == 2:
        root = argv[1]
    return HIO.guard(lambda v, n: body(v, n, root), "pass", "json")


if __name__ == "__main__":
    sys.exit(run(sys.argv[1:]))
