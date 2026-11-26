# card: C1-5
"""The ONE secret scanner (cards C1-5, B8): secret_scan.py [--root D] --staged | --range <a>..<b> | --range <sha>

Every pattern is a row of factory/data/secret-patterns.yaml (JSON syntax, valid YAML); no hook holds a pattern of its own.
--staged scans the index; --range scans every blob added or changed in the commits of `git rev-list <spec>` (a bare sha =
that commit's whole history). The matched value is never printed. Exit 0 clean, 1 found, 2 cannot judge (the table
absent or malformed, git failing).
"""
import argparse
import fnmatch
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hio import io as HIO  # noqa: E402

TABLE = "factory/data/secret-patterns.yaml"
DOOR = "restore secret-patterns.yaml (C1-5)"
KEYS = {"id", "kind", "pattern", "what"}
KINDS = ("path_glob", "token_regex")
KEEP = ("GIT_INDEX_FILE", "GIT_DIR", "GIT_WORK_TREE")  # the repository git is committing (t-1983 F1); no other GIT_*
RAW = ("--raw", "-z", "--no-renames", "--no-abbrev", "--diff-filter=ACMRT")


class Cannot(Exception):
    """The scan cannot be judged; the message is the whole refusal text."""


def git(root, *args):
    try:
        r = subprocess.run(["git", "-C", root] + list(args), capture_output=True, env=HIO.genv(KEEP))
    except (OSError, subprocess.SubprocessError) as exc:
        raise Cannot("git failed: %s" % exc)
    if r.returncode:
        raise Cannot("git %s failed: %s" % (args[0], r.stderr.decode("utf-8", "replace").strip() or r.returncode))
    return r.stdout


def toplevel(cwd="."):
    return git(cwd, "rev-parse", "--show-toplevel").decode("utf-8", "replace").strip()


def bad(why, row=None):
    raise Cannot("%s%s: %s; %s" % (TABLE, " row " + row if row else "", why, DOOR))


def check_row(r, seen):
    """One table row: its shape, a unique id, a known kind, a compiling pattern (r gets `rx`); else Cannot."""
    rid = r.get("id") if isinstance(r, dict) else None
    if not isinstance(r, dict) or set(r) != KEYS or not all(isinstance(r[k], str) and r[k] for k in KEYS):
        bad("a row needs exactly the non-empty text fields id, kind, pattern, what", rid if isinstance(rid, str) else None)
    if r["id"] in seen or r["kind"] not in KINDS:
        bad("duplicate id or kind outside path_glob|token_regex", r["id"])
    seen.add(r["id"])
    if r["kind"] == "token_regex":
        try:
            r["rx"] = re.compile(r["pattern"])
        except re.error as exc:
            bad("pattern does not compile: %s" % exc, r["id"])


def load_table(root):
    """Return the rows (dicts, token rows with a compiled `rx`); anything else is Cannot naming the file, the row, the door."""
    p = os.path.join(root, *TABLE.split("/"))
    if not os.path.isfile(p):
        bad("absent")
    try:
        with open(p, encoding="utf-8") as fh:
            doc = json.loads(fh.read())
    except (OSError, ValueError) as exc:
        bad("unreadable or not JSON syntax (a block-style edit is refused, write JSON): %s" % exc)
    rows = doc.get("rows") if isinstance(doc, dict) else None
    if not isinstance(doc, dict) or doc.get("schema") != "secret-patterns/1" or not isinstance(rows, list) or not rows:
        bad('not {"schema": "secret-patterns/1", "rows": [non-empty list]}')
    seen = set()
    for r in rows:
        check_row(r, seen)
    return rows


def parse_raw(out):
    """Raw -z diff output -> [(path, blob sha)]; submodule entries have no blob here and are skipped."""
    t, res, i = out.split(b"\0"), [], 0
    while i < len(t) - 1:
        f = t[i].split()
        if t[i].startswith(b":") and len(f) >= 5:
            if f[1] != b"160000":
                res.append((t[i + 1].decode("utf-8", "replace"), f[3].decode("ascii")))
            i += 2
        else:
            i += 1
    return res


def staged(root):
    return parse_raw(git(root, "diff", "--cached", *RAW))


def walk(root, revs):
    """Return (commits newest first, [(commit, path, sha)]) of the blobs each commit adds or changes (merges per parent)."""
    if any(r.startswith("-") and r != "--not" and not r.startswith("--remotes=") for r in revs):
        raise Cannot("not a revision: %s" % " ".join(revs))
    commits = git(root, "rev-list", *revs, "--").decode("ascii", "replace").split()
    ents = []
    for c in commits:
        ents += [(c, p, s) for p, s in parse_raw(git(root, "diff-tree", "-r", "-m", "--root", "--no-commit-id", *RAW, c))]
    return commits, ents


def scan(root, rows, ents):
    """ents: (label, path, sha). Return finding lines; one per row and file, the value is never in them."""
    out, seen = [], set()
    for label, path, sha in ents:
        hits = [(r, 0) for r in rows if r["kind"] == "path_glob" and fnmatch.fnmatchcase(
            (path if "/" in r["pattern"] else path.rsplit("/", 1)[-1]).lower(), r["pattern"].lower())]
        if sha not in seen:  # a blob is read once, at the newest commit that carries it
            seen.add(sha)
            todo = [r for r in rows if r["kind"] == "token_regex"]
            text = git(root, "cat-file", "blob", sha).decode("utf-8", "replace")
            for n, line in enumerate(text.split("\n"), 1):
                for r in [r for r in todo if r["rx"].search(line)]:
                    todo.remove(r)
                    hits.append((r, n))
                if not todo:
                    break
        out += ["secret: %s %s:%d row %s (%s)" % (label, path, n, r["id"], r["what"]) for r, n in hits]
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--staged", action="store_true")
    g.add_argument("--range", dest="rng")
    ap.add_argument("--root")
    a = ap.parse_args(argv)
    try:
        root = a.root or toplevel()
        rows = load_table(root)
        ents = [("staged", p, s) for p, s in staged(root)] if a.staged else \
            [(c[:12], p, s) for c, p, s in walk(root, [a.rng])[1]]
        found = scan(root, rows, ents)
    except Cannot as exc:
        print("secret_scan: cannot judge: %s" % exc, file=sys.stderr)
        return 2
    if found:
        print("\n".join(found))
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(HIO.guard(lambda v, n: main(), 2, "none"))
