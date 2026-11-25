# card: C1-4
"""The journal: one JSON line per event in logs/journal/<session>.jsonl (cards C1-4, B2, B7, B9).

journal.py [--root D] --event E --note T [--task ID] [--by WHO] [--session S]   append one line
journal.py [--root D] read [--session S] [--last N]                              print the lines, ts order
journal.py [--root D] open                                                        task ids dispatched, not closed

Exit: 0 done, 1 journal busy / an unparsable line (never skipped), 2 refused input (event, task, note, session).
The closed event list lives here and nowhere else; hooks of later cards import load() and open_tasks().
"""
import argparse
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EVENTS = ("dispatch", "accept", "reject", "return", "session_end", "cap_warning", "cut", "hook_failed", "refuse",
          "ask_owner")
NEEDS_TASK = ("dispatch", "accept", "reject", "return", "cap_warning", "cut")
CLOSING = ("accept", "reject", "return")
NOTE_MAX = 300
SESSION_RE = re.compile(r"[A-Za-z0-9_-]{1,128}")
LOCK_WAIT_S = 10
LOCK_STALE_S = 60


def jdir(root):
    return os.path.join(root, "logs", "journal")


def files(root):
    d = jdir(root)
    return sorted(os.path.join(d, f) for f in os.listdir(d) if f.endswith(".jsonl")) if os.path.isdir(d) else []


def load(root, session=None):
    """Return (entries, bad, found): entries (ts, file, n, raw, obj) in ts order; bad = [(n, file)]; found = any file."""
    paths = files(root)
    if session is not None:
        paths = [p for p in paths if os.path.basename(p) == session + ".jsonl"]
    out, bad = [], []
    for p in paths:
        last_ts = ""
        with open(p, encoding="utf-8", errors="replace", newline="") as fh:
            for n, raw in enumerate(fh.read().split("\n"), 1):
                if not raw.strip():
                    continue
                try:
                    obj = json.loads(raw)
                    if not isinstance(obj, dict):
                        raise ValueError
                    last_ts = str(obj.get("ts", ""))
                except ValueError:
                    obj = None
                    bad.append((n, os.path.basename(p)))
                out.append((last_ts, os.path.basename(p), n, raw, obj))
    out.sort(key=lambda e: (e[0], e[1], e[2]))
    return out, bad, bool(paths)


def open_tasks(root):
    """Return (status, tasks, bad): status is ok, unknown (no .jsonl) or incomplete (an unparsable line)."""
    entries, bad, found = load(root)
    if not found:
        return "unknown", [], bad
    last = {}
    for i, e in enumerate(entries):
        o = e[4] or {}
        t = o.get("task", "")
        if not t:
            continue
        if o.get("event") == "dispatch":
            last[t] = True
        elif o.get("event") in CLOSING and t in last:
            last[t] = False
    return ("incomplete" if bad else "ok"), [t for t, o in last.items() if o], bad


def pick_session(root, given):
    if given is None:
        given = os.environ.get("FORGE_SESSION")
    if given is None:
        d = jdir(root)
        cand = [os.path.join(d, f) for f in os.listdir(d)
                if f.endswith(".jsonl") and f != "git-hooks.jsonl"] if os.path.isdir(d) else []
        given = os.path.basename(max(cand, key=os.path.getmtime))[:-6] if cand else \
            "s-" + time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    return given


def take_lock(path):
    end = time.time() + LOCK_WAIT_S
    while True:
        try:
            os.close(os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY))
            return True
        except OSError:
            try:
                if time.time() - os.path.getmtime(path) > LOCK_STALE_S:
                    os.unlink(path)
                    print("journal lock older than %d s taken over" % LOCK_STALE_S)
                    continue
            except OSError:
                pass
        if time.time() > end:
            return False
        time.sleep(0.02)


def write(a):
    if a.event not in EVENTS:
        print("unknown event %r; the closed list: %s" % (a.event, ", ".join(EVENTS)))
        return 2
    if a.event in NEEDS_TASK and not a.task:
        print("--task is required for %s" % a.event)
        return 2
    note = a.note or ""
    if not note.strip():
        print("the note is empty")
        return 2
    if len(note) > NOTE_MAX:
        print("the note is %d characters, over %d; shorten it, it is never cut" % (len(note), NOTE_MAX))
        return 2
    session = pick_session(a.root, a.session)
    if not SESSION_RE.fullmatch(session):
        print("the session id must match [A-Za-z0-9_-]{1,128}")
        return 2
    obj = {"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "task": a.task or "", "event": a.event,
           "by": a.by, "note": note}
    line = json.dumps(obj, ensure_ascii=False)
    os.makedirs(jdir(a.root), exist_ok=True)
    lock = os.path.join(jdir(a.root), ".lock")
    if not take_lock(lock):
        print("journal busy: %s held for over %d s, nothing written" % (lock, LOCK_WAIT_S))
        return 1
    try:
        path = os.path.join(jdir(a.root), session + ".jsonl")
        with open(path, "a", encoding="utf-8", newline="\n") as fh:
            fh.write(line + "\n")
    finally:
        os.unlink(lock)
    print(path)
    print(line)
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=ROOT)
    p.add_argument("--event")
    p.add_argument("--note")
    p.add_argument("--task")
    p.add_argument("--by", default="lead")
    p.add_argument("--session")
    sub = p.add_subparsers(dest="cmd")
    r = sub.add_parser("read")
    r.add_argument("--session", dest="rsession")
    r.add_argument("--last", type=int)
    sub.add_parser("open")
    a = p.parse_args(argv)
    if a.cmd is None:
        if a.event is None:
            p.error("--event is required")
        return write(a)
    if a.cmd == "read":
        entries, bad, _ = load(a.root, a.rsession)
        shown = entries[-a.last:] if a.last and a.last > 0 else entries
        for ts, f, n, raw, obj in shown:
            print(raw if obj is not None else "unparsable line %d in %s" % (n, f))
        return 1 if bad else 0
    status, tasks, bad = open_tasks(a.root)
    if status == "unknown":
        print("unknown -- no journal")
        return 0
    for n, f in bad:
        print("unparsable line %d in %s" % (n, f))
    if bad:
        print("incomplete")
        return 1
    print("\n".join(tasks) if tasks else "none")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
