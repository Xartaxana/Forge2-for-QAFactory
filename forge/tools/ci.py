# card: C1-6
"""Run the one job list (forge/ci-jobs.json) locally; the workflow reads the same list through `matrix`.

ci.py [--list <path>] [--base <ref>] [--head <ref>]   run every built row, one line per job
ci.py matrix [--base R] [--head R]                    one JSON object: count, include (built rows), not_built
ci.py check --base <ref>                              the not_built ids may only shrink against <ref>

Exit: 0 green, 1 a built job failed (or the not_built set grew), 2 cannot judge (list absent or malformed).
The job ids and commands live in the list only; this file names none of them.
"""
import argparse
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LIST_REL = "forge/ci-jobs.json"
FIELDS = {"id", "command", "card", "state"}
STATES = ("built", "not_built")


class Refuse(Exception):
    """The list cannot be judged: exit 2 with the message."""


def parse_rows(text, where):
    try:
        rows = json.loads(text)
    except ValueError as exc:
        raise Refuse("%s: not valid JSON (%s)" % (where, exc))
    if not isinstance(rows, list):
        raise Refuse("%s: must be one JSON array of rows" % where)
    seen = set()
    for i, r in enumerate(rows):
        if not isinstance(r, dict) or set(r) != FIELDS:
            raise Refuse("%s: row %d must hold exactly %s" % (where, i, ", ".join(sorted(FIELDS))))
        name = r["id"]
        if not isinstance(name, str) or not name:
            raise Refuse("%s: row %d has no id" % (where, i))
        if name in seen:
            raise Refuse("%s: duplicate id %s" % (where, name))
        seen.add(name)
        if r["state"] not in STATES:
            raise Refuse("%s: row %s has unknown state %r" % (where, name, r["state"]))
        if not isinstance(r["command"], str) or (r["state"] == "built" and not r["command"].strip()):
            raise Refuse("%s: row %s is built but holds no command" % (where, name))
    return rows


def load(path):
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        raise Refuse("%s: absent or unreadable" % path)
    return parse_rows(text, path)


def fill(cmd, base, head):
    """Fill {base} and {head}; None when a token present in cmd has no value."""
    for token, value in (("{base}", base), ("{head}", head)):
        if token in cmd:
            if not value:
                return None
            cmd = cmd.replace(token, value)
    return cmd


def not_built_line(rows):
    ids = [r["id"] for r in rows if r["state"] == "not_built"]
    return "not built: %d%s" % (len(ids), " (%s)" % ", ".join(ids) if ids else ""), ids


def run_all(rows, base, head):
    on_actions = os.environ.get("GITHUB_ACTIONS") == "true"
    failed = []
    for r in rows:
        if r["state"] != "built":
            continue
        cmd = fill(r["command"], base, head)
        if cmd is None:
            code = 3  # a token with no value: part not judged
        else:
            code = subprocess.run(cmd, shell=True, cwd=ROOT).returncode
        if code == 0:
            print("ok   %s" % r["id"])
        elif code == 3 and not on_actions:
            print("not judged here: %s" % r["id"])
        else:
            print("FAIL %s (exit %d)" % (r["id"], code))
            failed.append(r["id"])
    line, _ = not_built_line(rows)
    print(line)
    if failed:
        print("failed: %s" % ", ".join(failed))
    return 1 if failed else 0


def matrix(rows, base, head):
    include = [dict(r, command=fill(r["command"], base, head) or r["command"]) for r in rows if r["state"] == "built"]
    print(json.dumps({"count": len(include), "include": include, "not_built": not_built_line(rows)[1]}))
    return 0


def check(rows, base, list_path):
    if not base:
        print("no base: the not_built rule was not judged (pass --base <ref>)")
        return 0
    git = ["git", "-C", ROOT]
    if subprocess.run(git + ["rev-parse", "--verify", "-q", base + "^{commit}"], capture_output=True).returncode:
        raise Refuse("--base %s: not a commit here" % base)
    shown = subprocess.run(git + ["show", "%s:%s" % (base, LIST_REL)], capture_output=True, text=True, encoding="utf-8")
    if shown.returncode:
        print("born: %s holds no list, nothing to compare" % base)
        return 0
    before = {r["id"] for r in parse_rows(shown.stdout, "%s:%s" % (base, LIST_REL)) if r["state"] == "not_built"}
    grown = [r["id"] for r in rows if r["state"] == "not_built" and r["id"] not in before]
    if grown:
        print("FAIL not_built grew against %s: %s (a new job enters built)" % (base, ", ".join(grown)))
        return 1
    print("ok   not_built did not grow against %s" % base)
    return 0


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("cmd", nargs="?", choices=("matrix", "check"))
    ap.add_argument("--list", dest="list_path", default=os.path.join(ROOT, *LIST_REL.split("/")))
    ap.add_argument("--base")
    ap.add_argument("--head")
    a = ap.parse_args(argv)
    try:
        rows = load(a.list_path)
        if a.cmd == "matrix":
            return matrix(rows, a.base, a.head)
        if a.cmd == "check":
            return check(rows, a.base, a.list_path)
        return run_all(rows, a.base, a.head)
    except Refuse as exc:
        print("cannot judge: %s" % exc)
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
