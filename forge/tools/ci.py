# card: C1-6
"""Run the one job list (forge/ci-jobs.json) locally; the workflow reads the same list through `matrix`.

ci.py [--list P] [--base R] [--head R] [--base-fallback REF] [--only ID]   run built rows, one line per job
ci.py matrix [--base R] [--head R] [--base-fallback REF] [--github-output F]   one JSON object: count, include (ids), not_built
ci.py check [--base R] [--head R] [--base-fallback REF]   not_built only shrinks; a built row is not deleted

Tokens {base}, {head}, {range} are filled in the run path only; a token with no value is exit 3 (not judged here,
red on Actions). Exit: 0 green, 1 a job failed (or the list rules broke), 2 cannot judge (the list absent or
malformed, --only not a built id, --head or check's base not a commit).
The job ids and commands live in the list only; this file names none of them.
"""
import argparse
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LIST_REL = "forge/ci-jobs.json"
FIELDS = {"id", "command", "card", "state"}
STATES = ("built", "not_built")
ID_RE = re.compile(r"[a-z0-9_-]+")  # an id reaches $GITHUB_OUTPUT: no newline, no key injection
RETIRE_RE = re.compile(r"^retire-job: (\S+) -- (\S.*)$", re.M)


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
        if not ID_RE.fullmatch(name):
            raise Refuse("%s: row %d id %r must match [a-z0-9_-]+" % (where, i, name))
        if name in seen:
            raise Refuse("%s: duplicate id %s" % (where, name))
        seen.add(name)
        if r["state"] not in STATES:
            raise Refuse("%s: row %s has unknown state %r" % (where, name, r["state"]))
        if not isinstance(r["card"], str) or not r["card"].strip():
            raise Refuse("%s: row %s has no card (a non-empty string)" % (where, name))
        if not isinstance(r["command"], str):
            raise Refuse("%s: row %s command must be a string" % (where, name))
        if r["state"] == "built" and not r["command"].strip():
            raise Refuse("%s: row %s is built but holds no command" % (where, name))
    return rows


def load(path):
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        raise Refuse("%s: absent or unreadable" % path)
    except UnicodeDecodeError:
        raise Refuse("%s: not UTF-8" % path)
    return parse_rows(text, path)


def git(*args):
    return subprocess.run(["git", "-C", ROOT] + list(args), capture_output=True)


def out_of(r):
    return r.stdout.decode("utf-8", "replace").strip() if r.returncode == 0 else ""


def commit_of(ref):
    """The commit sha of ref, or ''."""
    return out_of(git("rev-parse", "--verify", "-q", ref + "^{commit}"))


def resolve_base(base, head, fallback):
    """The one base resolution. Returns (base or None, note or None, invalid).

    A base that is empty, all zeros or not a commit has no value, unless the fallback ref resolves: then the base is
    the merge-base of that ref and the head (HEAD when none). A merge-base equal to the head commit, none, or an
    unresolved ref gives no base (a fallback never yields an empty range and never invents a base).
    invalid: a base was given that is neither empty, zeros nor a commit, and no fallback rescued it.
    """
    given = bool(base) and set(base) != {"0"}
    if given and commit_of(base):
        return base, None, False
    if fallback and commit_of(fallback):
        sha = out_of(git("merge-base", fallback, head or "HEAD"))
        if sha and sha != commit_of(head or "HEAD"):
            return sha, "base: %s (merge-base with %s)" % (sha, fallback), False
        return None, None, False
    return None, None, given


def fill(cmd, base, head):
    """Fill {range}, {base}, {head}; None when a token present in cmd has no value."""
    rng = ("%s..%s" % (base, head) if base else head) if head else None
    for token, value in (("{range}", rng), ("{base}", base), ("{head}", head)):
        if token in cmd:
            if not value:
                return None
            cmd = cmd.replace(token, value)
    return cmd


def not_built_line(rows):
    ids = [r["id"] for r in rows if r["state"] == "not_built"]
    return "not built: %d%s" % (len(ids), " (%s)" % ", ".join(ids) if ids else ""), ids


def job_env(base):
    """The env of every job: FORGE_BASE is the base this run resolved, else absent -- never a value inherited from the shell,
    so ci.py stays the one resolver (F245)."""
    env = {k: v for k, v in os.environ.items() if k != "FORGE_BASE"}
    if base:
        env["FORGE_BASE"] = base
    return env


def run_all(rows, base, head, only=None):
    on_actions = os.environ.get("GITHUB_ACTIONS") == "true"
    if only is not None and only not in [r["id"] for r in rows if r["state"] == "built"]:
        raise Refuse("--only %s: not a built row of the list" % only)
    failed = []
    for r in rows:
        if r["state"] != "built" or (only is not None and r["id"] != only):
            continue
        cmd = fill(r["command"], base, head)
        if cmd is None:
            code = 3  # a token with no value: part not judged
        else:
            code = subprocess.run(cmd, shell=True, cwd=ROOT, env=job_env(base)).returncode
        if code == 0:
            print("ok   %s" % r["id"])
        elif code == 3 and not on_actions:
            print("not judged here: %s" % r["id"])
        else:
            print("FAIL %s (exit %d)" % (r["id"], code))
            failed.append(r["id"])
    if only is None:
        print(not_built_line(rows)[0])
    if failed:
        print("failed: %s" % ", ".join(failed))
    return 1 if failed else 0


def matrix(rows, base, head, gh_path=None):
    """Ids only: tokens are filled and exit 3 is judged in run_all, on Actions as locally."""
    include = [{"id": r["id"]} for r in rows if r["state"] == "built"]
    line, ids = not_built_line(rows)
    print(json.dumps({"count": len(include), "include": include, "not_built": ids}))
    if gh_path:
        with open(gh_path, "a", encoding="utf-8") as fh:
            fh.write("include=%s\ncount=%d\nnb_line=%s\nbase=%s\nhead=%s\n"
                     % (json.dumps({"include": include}), len(include), line, base or "", head or ""))
    return 0


def check(rows, base, head):
    if not base:
        print("no base: the list rules were not judged (pass --base <ref>)")
        return 0
    where = "%s:%s" % (base, LIST_REL)
    shown = git("show", where)
    if shown.returncode:
        print("born: %s holds no list, nothing to compare" % base)
        return 0
    try:
        old = parse_rows(shown.stdout.decode("utf-8"), where)
    except UnicodeDecodeError:
        raise Refuse("%s: not UTF-8" % where)
    before = {r["id"] for r in old if r["state"] == "not_built"}
    grown = [r["id"] for r in rows if r["state"] == "not_built" and r["id"] not in before]
    now = {r["id"] for r in rows}
    gone = [r["id"] for r in old if r["state"] == "built" and r["id"] not in now]
    log = git("log", "--format=%B", "%s..%s" % (base, head or "HEAD")).stdout.decode("utf-8", "replace")
    retired = {m.group(1): m.group(2).strip() for m in RETIRE_RE.finditer(log)}
    bad = False
    if grown:
        print("FAIL not_built grew against %s: %s (a new job enters built)" % (base, ", ".join(grown)))
        bad = True
    dropped = []
    for jid in gone:
        if jid in retired:
            print("retired: %s -- %s" % (jid, retired[jid]))
        else:
            dropped.append(jid)
    if dropped:
        print("FAIL built row absent against %s: %s (a commit message line `retire-job: <id> -- <reason>` retires it)"
              % (base, ", ".join(dropped)))
        bad = True
    if not bad:
        print("ok   not_built did not grow and no built row is gone against %s" % base)
    return 1 if bad else 0


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("cmd", nargs="?", choices=("matrix", "check"))
    ap.add_argument("--list", dest="list_path", default=os.path.join(ROOT, *LIST_REL.split("/")))
    ap.add_argument("--base")
    ap.add_argument("--head")
    ap.add_argument("--base-fallback", dest="fallback")
    ap.add_argument("--only")
    ap.add_argument("--github-output", dest="gh_path")
    a = ap.parse_args(argv)
    for stream in (sys.stdout, sys.stderr):  # outside text (a commit message, an id) never crashes a print
        fix = getattr(stream, "reconfigure", None)  # a replaced or absent stream has none (review t-1947, N6)
        if fix:
            fix(errors="backslashreplace")
    try:
        rows = load(a.list_path)
        if a.head and not commit_of(a.head):
            raise Refuse("--head %r: not a commit here" % a.head)
        base, note, invalid = resolve_base(a.base, a.head, a.fallback)
        if invalid and a.cmd == "check":
            raise Refuse("--base %s: not a commit here" % a.base)
        if note:
            print(note, file=sys.stderr if a.cmd == "matrix" else sys.stdout)
        if a.cmd == "matrix":
            return matrix(rows, base, a.head, a.gh_path)
        if a.cmd == "check":
            return check(rows, base, a.head)
        return run_all(rows, base, a.head, a.only)
    except Refuse as exc:
        print("cannot judge: %s" % exc)
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
