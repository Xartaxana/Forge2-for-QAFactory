# card: C1-2
"""Universality scanner: the one scanner of C1-2, two scans.

universality.py [--root D] [--base R] [--update [--record ID]] [--basis]    exit 0 green, 1 red, 2 cannot judge, 3 not judged here
Names: every name of forge/universality-names.json in factory/tools and factory/hooks, case-insensitive, word-bounded, in
code, comments and strings (a common word that is a name errs red, its door an allow row; a name split by concatenation
errs green). Cyrillic U+0400-U+04FF: every file of factory/ (factory/data is not name-scanned, but its text is).
An allow row is {file, token, reason}, no line. A row that suppresses nothing is `stale:` and red; one without a reason is red.
"""
import json
import os
import re
import sys

import ratchets

REL = "forge/universality-names.json"
KINDS = ("language", "runner", "framework", "tracker", "case_manager", "harness")
NAME_ROOTS = ("factory/tools", "factory/hooks")
TEXT_ROOT = "factory"
CYRILLIC = re.compile("[Ѐ-ӿ]")
DOOR = "door: --update on the new basis with ratchet-raise: universality-names.json basis -- <W-n | D-n>"


def basis():
    return {"tool": ratchets.TOOL_VERSION, "python": ratchets.python_minor(),
            "constants": {"kinds": list(KINDS), "match": "word-bounded, case-insensitive", "cyrillic": "U+0400-U+04FF"},
            "roots": list(NAME_ROOTS) + [TEXT_ROOT]}


def check_names(names):
    if not isinstance(names, dict) or not names:
        raise ratchets.Refuse("%s: names must be a non-empty object (an empty table is never a pass)" % REL)
    for kind, words in names.items():
        if kind not in KINDS:
            raise ratchets.Refuse("%s: kind %s is outside %s" % (REL, kind, ", ".join(KINDS)))
        if not (isinstance(words, list) and words and all(isinstance(w, str) and w.strip() for w in words)):
            raise ratchets.Refuse("%s: kind %s needs a non-empty list of names" % (REL, kind))
    return names


def key_of(row):
    return (row["file"], row["token"].strip().lower())


def check_allow(allow):
    if not isinstance(allow, list):
        raise ratchets.Refuse("%s: allow must be a list" % REL)
    seen = set()
    for row in allow:
        if not isinstance(row, dict) or not all(isinstance(row.get(k), str) and row[k].strip() for k in ("file", "token")):
            raise ratchets.Refuse("%s: an allow row needs file and token" % REL)
        if key_of(row) in seen:
            raise ratchets.Refuse("%s: duplicate allow row %s::%s" % ((REL,) + key_of(row)))
        seen.add(key_of(row))
    return allow


def check_basis(old):
    """None when it matches; the file's Python minor when only that differs (exit 3); a Refuse for any other drift."""
    now = basis()
    if not isinstance(old, dict):
        raise ratchets.Refuse("%s: basis missing; %s" % (REL, DOOR))
    for key in now:
        if key not in old:
            raise ratchets.Refuse("basis %s missing in %s; %s" % (key, REL, DOOR))
        if key != "python" and old[key] != now[key]:
            raise ratchets.Refuse("basis %s %s -> %s; %s" % (key, old[key], now[key], DOOR))
    return None if old["python"] == now["python"] else old["python"]


def tree_files(root, rel):
    found = []
    for d, dirs, names in os.walk(os.path.join(root, rel)):
        dirs[:] = sorted(x for x in dirs if x != "__pycache__")
        found += [os.path.relpath(os.path.join(d, n), root).replace("\\", "/") for n in sorted(names)]
    return found


def read_text(root, rel):
    with open(os.path.join(root, rel), "rb") as fh:
        raw = fh.read()
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        raise ratchets.Refuse("%s: not UTF-8" % rel)


def pattern(names):
    words = sorted({w.strip() for ws in names.values() for w in ws}, key=len, reverse=True)
    return re.compile(r"(?<!\w)(%s)(?!\w)" % "|".join(map(re.escape, words)), re.I)


def scan(root, names):
    """(name hits [(file, line, token)], Cyrillic sites [(file, line)])."""
    rx, hits, cyr = pattern(names), [], []
    for rel in tree_files(root, TEXT_ROOT):
        in_names = rel.startswith(tuple(r + "/" for r in NAME_ROOTS))
        for n, line in enumerate(read_text(root, rel).split("\n"), 1):
            if CYRILLIC.search(line):
                cyr.append((rel, n))
            if in_names:
                hits += [(rel, n, m.group(1).lower()) for m in rx.finditer(line)]
    return hits, cyr


def judge(hits, cyr, allow, out):
    """(new finding lines printed, stale keys). The dead scanner is judged before the stale rule."""
    if not hits and allow:
        raise ratchets.Refuse("scanner found nothing (%d allow rows)" % len(allow))
    keys = {key_of(r) for r in allow}
    new = 0
    for rel, n, token in hits:
        if (rel, token) not in keys:
            out(ratchets.finding("%s::%s" % (rel, token), "%s:%d" % (rel, n)))
            new += 1
    for rel, n in cyr:
        out(ratchets.finding("%s::cyrillic" % rel, "%s:%d" % (rel, n)))
        new += 1
    for row in allow:
        if not str(row.get("reason", "")).strip():
            out(ratchets.finding("%s::%s" % key_of(row), "allow row has no reason"))
            new += 1
    stale = keys - {(rel, token) for rel, _, token in hits}
    for rel, token in sorted(stale):
        out("stale: %s::%s" % (rel, token))
    return new, stale


def raised(old, data):
    """Raise keys against the base: allow rows added, names removed, roots removed."""
    if not isinstance(old, dict):
        raise ratchets.Refuse("%s at the base: must be one JSON object" % REL)
    keys = {}
    seen = {key_of(r) for r in check_allow(old.get("allow", []))}
    for row in data["allow"]:
        if key_of(row) not in seen:
            keys["%s::%s" % key_of(row)] = "allow row added"
    words = lambda d: {w.strip() for ws in (d.get("names") or {}).values() for w in ws}
    for word in sorted(words(old) - words(data)):
        keys[word] = "scan narrowed: name removed"
    roots = lambda d: set((d.get("basis") or {}).get("roots") or [])
    if roots(old) - roots(data):
        keys["basis"] = "scan narrowed: root removed"
    return keys


def update(root, path, data, stale, new, record):
    """Shrink the allow list with no record; never empty it, and never at all while the file is unreadable (it was read)."""
    if record:
        print(ratchets.resolve(record, ("word", "decision")))
        return 1
    keep = [r for r in data["allow"] if key_of(r) not in stale]
    if data["allow"] and not keep:
        print("refused: --update would empty allow; door: --record <W-n | D-n> and a `ratchet-raise: universality-names.json clear -- <id>` line")
        return 1
    data["allow"] = keep
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(data, indent=2) + "\n")
    print("updated: %d stale allow rows removed" % len(stale))
    dirty = [ln for ln in ratchets.text_of(ratchets.git(root, "status", "--porcelain", "--", TEXT_ROOT)).split("\n") if ln.strip()]
    if dirty:
        print("uncommitted changes in scope: %d paths -- the baseline describes the committed tree" % len(dirty))
    return 1 if new else 0


def run(argv):
    ap = ratchets.parser(__doc__.split("\n")[0])
    ap.add_argument("--update", action="store_true")
    ap.add_argument("--record")
    ap.add_argument("--basis", action="store_true")
    a = ap.parse_args(argv)
    if a.basis:
        print(json.dumps(basis()))
        return 0
    path = os.path.join(a.root, REL)
    data = ratchets.read_json(path, REL)
    if not isinstance(data, dict):
        raise ratchets.Refuse("%s: must be one JSON object" % REL)
    names, allow = check_names(data.get("names")), check_allow(data.get("allow"))
    drift = check_basis(data.get("basis"))
    if drift:
        print("not judged here: python %s, basis %s" % (ratchets.python_minor(), drift))
        return 3
    base = ratchets.base_of(a.root, a.base)
    new, stale = judge(*scan(a.root, names), allow, print)
    if a.update:
        return update(a.root, path, data, stale, new, a.record)
    old = ratchets.base_doc(a.root, base, REL, print)
    raises = ratchets.judge_raises(a.root, base, REL, raised(old, data), print) if old is not None else 0
    return ratchets.verdict([1 if new or stale else 0, raises])


def main(argv):
    return ratchets.guarded(run, argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
