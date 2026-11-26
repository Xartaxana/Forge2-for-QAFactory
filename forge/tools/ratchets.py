# card: C1-2
"""The one module of every ratchet (F246): finding lines, exit precedence, base and raise lines, one resolver door.

Exit: 0 green, 1 red, 2 cannot judge (Refuse), 3 part not judged here (red on Actions, TESTING rule 7). Precedence 2 > 1 > 3 > 0.
Finding line: `new: <identity> <detail>`, the identity one token (whitespace written %20); a stale row prints `stale: <id>`.
"""
import argparse
import json
import os
import re
import subprocess
import sys

TOOL_VERSION = "1"
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# B20 (d): the old `budget-raise:` keyword is not read. The line may sit anywhere in a message, a fence or a quote included.
RAISE_RE = re.compile(r"^ratchet-raise: (\S+) (\S+) -- (\S+)[ \t\r]*$", re.M)


class Refuse(Exception):
    """The ratchet cannot be judged: exit 2 with the message."""


def python_minor():
    return "%d.%d" % sys.version_info[:2]


def finding(identity, detail):
    return "new: %s %s" % (re.sub(r"\s", "%20", identity), detail)


def verdict(codes):
    for code in (2, 1, 3):
        if code in codes:
            return code
    return 0


def parser(desc):
    ap = argparse.ArgumentParser(description=desc)
    ap.add_argument("--root", default=ROOT)
    ap.add_argument("--base")
    return ap


def guarded(fn, *args):
    for stream in (sys.stdout, sys.stderr):  # outside text (a commit message, a file name) never crashes a print
        fix = getattr(stream, "reconfigure", None)
        if fix:
            fix(errors="backslashreplace")
    try:
        return fn(*args)
    except Refuse as exc:
        print("cannot judge: %s" % exc)
        return 2


def read_json(path, what):
    try:
        with open(path, "rb") as fh:
            raw = fh.read()
    except OSError:
        raise Refuse("%s: absent or unreadable" % what)
    try:
        return json.loads(raw.decode("utf-8"))
    except ValueError as exc:  # UnicodeDecodeError is one too
        raise Refuse("%s: not valid UTF-8 JSON (%s)" % (what, exc))


def git(root, *args):
    return subprocess.run(["git", "-C", root] + list(args), capture_output=True)


def text_of(result):
    return result.stdout.decode("utf-8", "replace")  # a non-UTF-8 message is read with replacement


def base_of(root, arg):
    """--base, else FORGE_BASE (ci.py's resolved base, F245), else None. A value that is no commit is exit 2."""
    value = arg or os.environ.get("FORGE_BASE") or ""
    if not value or set(value) == {"0"}:
        return None
    result = git(root, "rev-parse", "--verify", "-q", value + "^{commit}")
    if result.returncode:
        raise Refuse("base %s: not a commit here" % value)
    return text_of(result).strip()


def base_doc(root, base, rel, out):
    """The JSON of rel at the base; None (with its line) when there is no base or the base holds no such file (born)."""
    if base is None:
        out("raises not judged: no base")
        return None
    shown = git(root, "show", "%s:%s" % (base, rel))
    if shown.returncode:
        out("born: %s holds no %s, raises not judged" % (base[:12], rel))
        return None
    try:
        return json.loads(text_of(shown))
    except ValueError as exc:
        raise Refuse("%s:%s: not valid JSON (%s)" % (base[:12], rel, exc))


def resolve(rid, kinds=("word",)):
    """B3's door (F252): None when the record resolves to one of kinds, else the red line. Until B3 there is no registry,
    so every id is red; B3's builder replaces this body with the words.py call."""
    return "cannot resolve %s: no registry" % rid


def judge_raises(root, base, rel, keys, out):
    """keys: {key: what was raised}. Each needs `ratchet-raise: <file> <key> -- <id>` in --base..HEAD, and the id resolving."""
    if not keys:
        return 0
    log = text_of(git(root, "log", "--format=%B", "%s..HEAD" % base))
    lines, code = RAISE_RE.findall(log), 0
    for key, what in keys.items():
        ids = [i for f, k, i in lines if k == key and (rel == f or rel.endswith("/" + f))]
        errs = [resolve(i) for i in ids]
        if ids and not all(errs):
            continue
        msg = errs[0] if ids else "%s needs `ratchet-raise: %s %s -- <W-n | D-n>`" % (what, os.path.basename(rel), key)
        out(finding("%s::%s" % (rel, key), msg))
        code = 1
    return code
