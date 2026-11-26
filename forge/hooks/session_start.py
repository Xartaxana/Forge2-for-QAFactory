# card: B2
"""SessionStart hook (card B2): prints what to re-read at a session start and after a compaction. It prints only, exit 0.

session_start.py [--root D]   D defaults to this repository. Input: the event JSON on stdin, field `source`
(startup|resume|clear|compact); empty, broken or unknown -> as startup.
Blocks: (1) forge/BOOT.md on startup|clear|compact; (2) the re-read line, always; (3) the carriers checklist on compact;
(4) the previous session's end on startup. Any error -> one line `reminder failed: <error>; read forge/BOOT.md by hand`.
Cap 6144 emitted bytes: the open list is cut first, then the checklist, each with a `[cut: <what>]` marker; a valid
UTF-8 BOOT never; a non-UTF-8 BOOT last, to the cap, then the line `forge/BOOT.md not UTF-8: cut at <n> bytes, fix the file`.
The hook is inert until the Lead registers it in .claude/settings.json (the net is not the guarantee: the gates are).
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from hio import io as HIO  # noqa: E402

CAP = 6144
OPEN_MAX = 10
BOOT_SOURCES = ("startup", "clear", "compact")


def boot_block(root, eval_arm, show):
    """Return (text, present, bad). Presence is read on every source (t-2010 B2-1/B2-2); the text only when `show`.
    In an eval arm an absent BOOT prints nothing (B1's `without` arm, F3). bad: the replacement text of a non-UTF-8 BOOT."""
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
        return "", True, raw.decode("utf-8", "replace")


def bad_boot(replaced, n):
    """The non-UTF-8 BOOT text cut to n bytes at a character edge, then the one marker line (t-2010 B2-6)."""
    kept = replaced.encode("utf-8")[:n].decode("utf-8", "ignore")
    return kept + "\nforge/BOOT.md not UTF-8: cut at %d bytes, fix the file" % len(kept.encode("utf-8"))


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
    return "\n".join(x for x in (p["boot"], line, check, p["prev"]) if x)


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


def compose(root, source, eval_arm):
    sys.path.insert(0, os.path.join(HERE, "..", "tools"))
    import journal  # noqa: E402 -- lazily: a broken journal.py is a fallback line, not a crash at import
    loaded = journal.load(root)
    status, tasks, bad = journal.open_tasks(root, loaded)
    boot, present, badtext = boot_block(root, eval_arm, source in BOOT_SOURCES)
    field = "re-read: forge/BOOT.md | " if present else "" if eval_arm else "re-read: forge/BOOT.md (not written yet, B1) | "
    return fit({"boot": boot, "bad": badtext, "field": field,
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
