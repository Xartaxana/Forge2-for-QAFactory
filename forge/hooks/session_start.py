# card: B2
"""SessionStart hook (card B2): prints what to re-read at a session start and after a compaction. It prints only, exit 0.

session_start.py [--root D]   D defaults to this repository. Input: the event JSON on stdin, field `source`
(startup|resume|clear|compact); empty, broken or unknown -> as startup.
Blocks: (1) forge/BOOT.md on startup|clear|compact; (2) the re-read line, always; (3) the carriers checklist on compact;
(4) the previous session's end on startup. Any error -> one line `reminder failed: <error>; read forge/BOOT.md by hand`.
Cap 6144 UTF-8 bytes: the open list is cut first, then the checklist, each with a `[cut: <what>]` marker; BOOT never.
The hook is inert until the Lead registers it in .claude/settings.json (the net is not the guarantee: the gates are).
"""
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from hio import io as HIO  # noqa: E402

CAP = 6144
OPEN_MAX = 10
BOOT_SOURCES = ("startup", "clear", "compact")


def boot_block(root, eval_arm):
    """Return (text, present). In an eval arm an absent BOOT prints nothing (B1's `without` arm, F3)."""
    p = os.path.join(root, "forge", "BOOT.md")
    if not os.path.isfile(p):
        return ("" if eval_arm else "forge/BOOT.md not written yet (B1)"), False
    with open(p, "rb") as fh:
        raw = fh.read()
    try:
        return raw.decode("utf-8"), True
    except UnicodeDecodeError:
        return raw.decode("utf-8", "replace") + "\nforge/BOOT.md is not UTF-8: printed with replacement characters", True


def open_text(status, tasks, bad):
    if status == "unknown":
        return "unknown -- no journal"
    more = " and %d more" % (len(tasks) - OPEN_MAX) if len(tasks) > OPEN_MAX else ""
    text = (", ".join(tasks[:OPEN_MAX]) + more) or "none"
    return text + (" (incomplete: %d unreadable journal lines)" % len(bad) if status == "incomplete" else "")


def newest_snapshot(root):
    names = sorted(glob.glob(os.path.join(root, "logs", "journal", "snapshots", "*.md")))
    return "logs/journal/snapshots/" + os.path.basename(names[-1]) if names else "none yet"


def checklist(root):
    p = os.path.join(root, "forge", "carriers.json")
    if not os.path.isfile(p):
        return "carriers checklist: forge/carriers.json not written yet (B7)"
    try:
        with open(p, encoding="utf-8") as fh:
            rows = ["- %s -> %s" % (r["what goes there"], r["carrier"]) for r in json.load(fh)]
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return "carriers checklist unreadable: %s" % exc
    return "\n".join(["carriers checklist:"] + rows)


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


def fit(p):
    """The whole text, then without the open list, then without the checklist too; BOOT is never cut."""
    for cut_open, cut_list in ((False, False), (True, False), (True, True)):
        text = render(p, cut_open, cut_list)
        if len(text.encode("utf-8")) <= CAP:
            break
    return text


def compose(root, source, eval_arm):
    sys.path.insert(0, os.path.join(HERE, "..", "tools"))
    import journal  # noqa: E402 -- lazily: a broken journal.py is a fallback line, not a crash at import
    loaded = journal.load(root)
    status, tasks, bad = journal.open_tasks(root, loaded)
    boot, present = boot_block(root, eval_arm) if source in BOOT_SOURCES else ("", False)
    return fit({"boot": boot, "field": "re-read: forge/BOOT.md | " if present or not eval_arm else "",
                "snap": newest_snapshot(root), "open": open_text(status, tasks, bad),
                "check": checklist(root) if source == "compact" else "",
                "prev": previous(loaded[0], loaded[2]) if source == "startup" else ""})


def body(value, note, root):
    source = value.get("source") if value else None
    if source not in ("startup", "resume", "clear", "compact"):
        source = "startup"
    try:
        print(compose(root, source, bool(os.environ.get("FORGE_EVAL_ARM"))))
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
