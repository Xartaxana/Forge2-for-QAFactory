# card: C1-2
"""The one module of every ratchet (F246): finding lines, exit precedence, base and raise lines, one resolver door.

Exit: 0 green, 1 red, 2 cannot judge (Refuse), 3 part not judged here (red on Actions, TESTING rule 7). Precedence 2 > 1 > 3 > 0.
Finding line: `new: <identity> <detail>`, the identity one token (whitespace written %20); a stale row prints `stale: <id>`.
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys

TOOL_VERSION = "1"
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# B20 (d): the old `budget-raise:` keyword is not read. The line may sit anywhere in a message; a quote (`>`) or an indent
# (a fence inside a quote, t-1991 F5) before it is skipped, so such a line counts.
RAISE_RE = re.compile(r"^[ \t>]*ratchet-raise: (\S+) (\S+) -- (\S+)[ \t\r]*$", re.M)


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
    """keys: {key: (what, kinds)}. Each needs `ratchet-raise: <file> <key> -- <id>` in --base..HEAD, the id resolving to a kind."""
    if not keys:
        return 0
    log = text_of(git(root, "log", "--format=%B", "%s..HEAD" % base))
    lines, code = RAISE_RE.findall(log), 0
    for key, (what, kinds) in keys.items():
        ids = [i for f, k, i in lines if k == key and (rel == f or rel.endswith("/" + f))]
        errs = [resolve(i, kinds) for i in ids]  # F1: None is a record that resolves
        if None in errs:
            continue
        msg = errs[0] if ids else "%s needs `ratchet-raise: %s %s -- <W-n | D-n>`" % (what, os.path.basename(rel), key)
        out(finding("%s::%s" % (rel, key), msg))
        code = 1
    return code


def files_of(root, patterns):
    """The ONE file-set reader: files under root matching the globs, '/'-separated, sorted, never __pycache__ (t-1991 Q6)."""
    found = set()
    for pat in patterns:
        for rel in glob.glob(pat, root_dir=root, recursive=True, include_hidden=True):
            rel = rel.replace("\\", "/")
            if os.path.isfile(os.path.join(root, rel)) and "__pycache__" not in rel.split("/"):
                found.add(rel)
    return sorted(found)


def text_file(root, rel):
    """The ONE text reader: strict UTF-8; a file that is not UTF-8 is exit 2 naming it."""
    with open(os.path.join(root, rel), "rb") as fh:
        raw = fh.read()
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        raise Refuse("%s: not UTF-8" % rel)


def load_list(path, what, ident, field="allow", must_exist=False):
    """(data, rows) of a list file keyed by ident(row), which raises on a row without its id/file. No file is an empty list
    (unless must_exist): data {"basis": None, field: []}, which check_basis passes and update never writes (t-1992 N2: node
    B's baselines start absent). Not JSON, no basis, a malformed or duplicate row is exit 2; a reasonless row is judge_list's."""
    if not os.path.isfile(path) and not must_exist:
        return {"basis": None, field: []}, []
    data = read_json(path, what)
    rows = data.get(field) if isinstance(data, dict) else None
    if not isinstance(rows, list):
        raise Refuse("%s: must be one JSON object with a list %s" % (what, field))
    if not isinstance(data.get("basis"), dict):
        raise Refuse("%s: basis missing" % what)
    seen = set()
    for row in rows:
        key = row_key(ident, row, "%s: a %s row" % (what, field))
        if key in seen:
            raise Refuse("%s: duplicate %s row %s" % (what, field, key))
        seen.add(key)
    return data, rows


def row_key(ident, row, what):
    try:
        return ident(row)
    except (KeyError, TypeError, AttributeError, ValueError):
        raise Refuse("%s needs its id or file" % what)


def check_basis(old, now, door):
    """None when the basis matches or the file is not born yet (old None: no drift); the file's Python minor when only that
    differs (exit 3); a Refuse for any other drift."""
    if old is None:
        return None
    for key in now:
        if key not in old:
            raise Refuse("basis %s missing; %s" % (key, door))
        if key != "python" and old[key] != now[key]:
            raise Refuse("basis %s %s -> %s; %s" % (key, old[key], now[key], door))
    return None if old.get("python") == now.get("python") else old["python"]


def basis_changed(old, new):
    """N13's `basis` key: any basis key but python differs between the base and HEAD (constants, roots, tool; an added root
    too; a base with no basis object differs). A label cannot be ordered, so every change errs red as size's unit and paths
    do (t-1994 F1: a changed match constant passed unseen)."""
    strip = lambda b: {k: v for k, v in b.items() if k != "python"} if isinstance(b, dict) else b
    return strip(old) != strip(new)


def judge_list(sites, rows, key, files_read, scope_files, out=print):
    """sites: [(identity, detail)], rows keyed by key(row). Returns (sites no row allows, stale keys, keys of rows without a
    reason). A dead scanner (no site while rows exist; no file read while the scope holds files) is judged before stale."""
    if rows and not sites:
        raise Refuse("scanner found nothing (%d rows)" % len(rows))
    if scope_files and not files_read:
        raise Refuse("scanner read none of the %d files in scope" % scope_files)
    keys = {key(r) for r in rows}
    text = lambda k: re.sub(r"\s", "%20", "::".join(k) if isinstance(k, tuple) else k)
    stale = sorted(keys - {identity for identity, _ in sites})
    bare = [key(r) for r in rows if not str(r.get("reason", "")).strip()]
    for k in stale:
        out("stale: %s" % text(k))
    for k in bare:
        out(finding(text(k), "row has no reason"))
    return [s for s in sites if s[0] not in keys], stale, bare


def cleared(old_rows, new_rows):
    """N13's `clear` key: rows at the base, none at HEAD. An empty list switches off judge_list's first dead-scanner branch
    (N16), so emptying is a raise however it was done (t-1992 N4: by hand it passed unseen)."""
    return bool(old_rows) and not new_rows


def _shrink(path, data, field, key, stale, out=print):
    """update's helper, never a gate (t-1994 F3): drop the stale rows and write the file: True. No stale row: nothing
    written, False (a file not born stays unborn)."""
    keep = [r for r in data[field] if key(r) not in stale]
    if len(keep) == len(data[field]):
        return False
    data[field] = keep
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(data, indent=2) + "\n")
    out("updated: %d stale %s rows removed" % (len(stale), field))
    return True


def update(root, path, data, field, key, stale, record, kinds, scope, out=print):
    """The ONE --update / --record road of every list tool (F246, t-1992 N3): 0 done, 1 refused with nothing written.
    A record must resolve to one of kinds; only a resolved record may empty the list (N16); then _shrink, then a warning
    about uncommitted paths in scope, since the list describes the committed tree (N15). scope takes the globs files_of
    takes (each sent to git as `:(glob)`, t-1994 F2: plain pathspecs read `**` and `*` otherwise); an empty scope warns
    about the whole tree."""
    if record:
        err = resolve(record, kinds)
        if err:
            out(err)
            return 1
    if not record and cleared(data[field], [r for r in data[field] if key(r) not in stale]):
        out("refused: --update would empty %s; door: --record <W-n | D-n> and a `ratchet-raise: %s clear -- <id>` line"
            % (field, os.path.basename(path)))
        return 1
    _shrink(path, data, field, key, stale, out)
    specs = [":(glob)" + s for s in scope]
    dirty = [ln for ln in text_of(git(root, "status", "--porcelain", "--", *specs)).split("\n") if ln.strip()]
    if dirty:
        out("uncommitted changes in scope: %d paths -- the list describes the committed tree" % len(dirty))
    return 0
