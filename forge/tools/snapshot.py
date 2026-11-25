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


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=ROOT)
    p.add_argument("--close", action="store_true")
    a = p.parse_args(argv)
    if a.close:
        print("\n".join(carriers(a.root)))
    entries, bad, found = journal.load(a.root)
    status, tasks, _ = journal.open_tasks(a.root)
    none = "no journal lines"
    opened = none if not entries else ("\n".join(tasks) if tasks else "none") + (
        "\n(incomplete: unparsable lines)" if bad else "")
    last = "\n".join(e[3] for e in entries[-20:]) or none
    st = git(a.root, "status", "--short", "--untracked-files=all")
    rows = st.split("\n")
    if len(rows) > STATUS_MAX:
        st = "\n".join(rows[:STATUS_MAX] + ["[cut: %d of %d lines shown]" % (STATUS_MAX, len(rows))])
    text = "# Snapshot\n\n## open tasks\n%s\n\n## last 20 journal lines\n%s\n\n## git status --short\n%s\n\n## branch\n%s\n" % (
        opened, last, st or "clean", git(a.root, "branch", "--show-current") or "(none)")
    d = os.path.join(a.root, "logs", "journal", "snapshots")
    os.makedirs(d, exist_ok=True)
    stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    path, i = os.path.join(d, stamp + ".md"), 1
    while os.path.exists(path):
        i += 1
        path = os.path.join(d, "%s-%d.md" % (stamp, i))
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(path)
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
