# card: C1-4
"""Write a state snapshot before a compaction: logs/journal/snapshots/<UTC stamp>.md (cards C1-4, B7).

snapshot.py [--root D] [--close]     print the path; --close first prints each row of forge/carriers.json
                                     (card B7: array of rows with `carrier` and `what goes there`) as <what> -> <carrier>

Sections: open tasks, last 20 journal lines, git status --short (over 200 lines cut with a marker), branch.
It never refuses: git failing or carriers.json absent / malformed is said in the text and the snapshot is written.
"""
import argparse
import json
import os
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import journal  # noqa: E402

ROOT = journal.ROOT
STATUS_MAX = 200


def git(root, *args):
    try:
        r = subprocess.run(["git", "-C", root] + list(args), capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=60)
    except (OSError, subprocess.SubprocessError) as exc:
        return "git failed: %s" % exc
    return r.stdout.rstrip("\n") if r.returncode == 0 else "git failed: %s" % (r.stderr.strip() or r.returncode)


def carriers(root):
    p = os.path.join(root, "forge", "carriers.json")
    if not os.path.isfile(p):
        return ["forge/carriers.json absent (B7)"]
    try:
        with open(p, encoding="utf-8") as fh:
            return ["%s -> %s" % (r["what goes there"], r["carrier"]) for r in json.load(fh)]
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return ["forge/carriers.json malformed: %s" % exc]


def guard(name, fn):
    try:
        return fn()
    except Exception as exc:
        return "%s failed: %s" % (name, exc)


def journal_text(root):
    """Return (open tasks text, last 20 lines text); the loader's named problems stay in the first."""
    loaded = journal.load(root)
    entries, bad, _ = loaded
    tasks = journal.open_tasks(root, loaded)[1]
    none = "no journal lines"
    opened = none if not entries else ("\n".join(tasks) if tasks else "none")
    if bad:
        opened += "\n(incomplete)\n" + "\n".join(bad)
    return opened, "\n".join(e[3] for e in entries[-20:]) or none


def status(root):
    rows = git(root, "status", "--short", "--untracked-files=all").split("\n")
    if len(rows) > STATUS_MAX:
        rows = rows[:STATUS_MAX] + ["[cut: %d of %d lines shown]" % (STATUS_MAX, len(rows))]
    return "\n".join(rows) or "clean"


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=ROOT)
    p.add_argument("--close", action="store_true")
    a = p.parse_args(argv)
    if a.close:
        print(guard("carriers", lambda: "\n".join(carriers(a.root))))
    try:
        opened, last = journal_text(a.root)
    except Exception as exc:  # the snapshot is read by the next session: whatever the journal does, the file is written
        opened = last = "journal failed: %s" % exc
    text = "# Snapshot\n\n## open tasks\n%s\n\n## last 20 journal lines\n%s\n\n## git status --short\n%s\n\n## branch\n%s\n" % (
        opened, last, guard("git status", lambda: status(a.root)),
        guard("branch", lambda: git(a.root, "branch", "--show-current") or "(none)"))
    d = os.path.join(a.root, "logs", "journal", "snapshots")
    os.makedirs(d, exist_ok=True)
    stamp, i = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime()), 1
    while True:  # mode x: two snapshots started in the same second never overwrite each other
        path = os.path.join(d, stamp + ".md" if i == 1 else "%s-%d.md" % (stamp, i))
        try:
            fh = open(path, "x", encoding="utf-8", newline="\n")
        except FileExistsError:
            i += 1
            continue
        with fh:
            fh.write(text)
        break
    print(path)
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
