# card: C1-2
"""Universality scanner: the one scanner of C1-2, two scans.

universality.py [--root D] [--base R] [--update [--record ID]] [--basis]    exit 0 green, 1 red, 2 cannot judge, 3 not judged here
Names: every name of forge/universality-names.json in factory/tools and factory/hooks, case-insensitive, bounded by any
non-letter or a camelCase step: lower to upper, or an acronym's end, a capital before a capital and a lower letter
(JIRAClient = JIRA + Client). So jira_url, run_pytest, python3, PytestRunner and getJiraIssue are flagged (t-1992 N5); a
common word that is a name errs red, its door an allow row; a name split by lowercase concatenation errs green (pytestish).
In code, comments and strings. Cyrillic U+0400-U+04FF: every file of factory/ (factory/data is not name-scanned, its text is).
An allow row is {file, token, reason}, no line. A row that suppresses nothing is `stale:` and red; one without a reason is red.
The list, basis, stale and reason rules, the --update road, the file-set and text readers are ratchets.py's (F246); this
file keeps no copy.
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
CYRILLIC = re.compile("[\u0400-\u04FF]")
RECORD = ("word", "decision")
DOOR = ("door: edit basis in %s; a removed root also needs `ratchet-raise: universality-names.json basis -- <W-n | D-n>`"
        "; --update does not touch basis" % REL)  # t-1992 N7: raised() asks the line only for a removed root
# A name's edge: a non-letter, a lower-to-upper step, or an acronym's end (t-1992 N5: camelCase carried names unflagged).
# Case-sensitive on purpose: only the name itself is matched case-insensitively.
EDGE = r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])"


def basis():
    return {"tool": ratchets.TOOL_VERSION, "python": ratchets.python_minor(),
            "constants": {"kinds": list(KINDS), "match": "non-letter- or camelCase-bounded, case-insensitive",
                          "cyrillic": "U+0400-U+04FF"},
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
    file, token = row["file"], row["token"]
    if not all(isinstance(x, str) and x.strip() for x in (file, token)):
        raise ValueError("an allow row needs file and token")
    return (file, token.strip().lower())


def pattern(names):
    words = sorted({w.strip() for ws in names.values() for w in ws}, key=len, reverse=True)
    alts = "|".join(map(re.escape, words))
    return re.compile(r"(?:(?<![A-Za-z])|%s)(?i:(%s))(?:(?![A-Za-z])|%s)" % (EDGE, alts, EDGE))  # F8, N5


def scan(root, names):
    """(name sites [((file, token), 'file:line')], Cyrillic sites [(file, line)], files read, files in scope)."""
    rx, hits, cyr, files = pattern(names), [], [], ratchets.files_of(root, [TEXT_ROOT + "/**"])
    for rel in files:
        in_names = rel.startswith(tuple(r + "/" for r in NAME_ROOTS))
        for n, line in enumerate(ratchets.text_file(root, rel).split("\n"), 1):
            if CYRILLIC.search(line):
                cyr.append((rel, n))
            if in_names:
                hits += [((rel, m.group(1).lower()), "%s:%d" % (rel, n)) for m in rx.finditer(line)]
    return hits, cyr, len(files), len(files)


def judge(found, allow, out):
    """(count of red findings, stale keys); the shared rules are ratchets.judge_list's."""
    hits, cyr, read, scope = found
    new, stale, bare = ratchets.judge_list(hits, allow, key_of, read, scope, out)
    for identity, detail in new:
        out(ratchets.finding("%s::%s" % identity, detail))
    for rel, n in cyr:
        out(ratchets.finding("%s::cyrillic" % rel, "%s:%d" % (rel, n)))
    return len(new) + len(cyr) + len(bare), set(stale)


def raised(old, data):
    """Raise keys against the base: allow rows added, allow emptied (`clear`, N4), names removed, roots removed (each:
    `word | decision`)."""
    try:
        seen = {key_of(r) for r in old.get("allow", [])}
    except (KeyError, TypeError, AttributeError, ValueError):
        raise ratchets.Refuse("%s at the base: must be one JSON object with well-formed allow rows" % REL)
    keys = {}
    for row in data["allow"]:
        if key_of(row) not in seen:
            keys["%s::%s" % key_of(row)] = "allow row added"
    if ratchets.cleared(old.get("allow"), data["allow"]):
        keys["clear"] = "allow emptied"
    words =lambda d: {w.strip() for ws in (d.get("names") or {}).values() for w in ws}
    for word in sorted(words(old) - words(data)):
        keys[word] = "scan narrowed: name removed"
    roots = lambda d: set((d.get("basis") or {}).get("roots") or [])
    if roots(old) - roots(data):
        keys["basis"] = "scan narrowed: root removed"
    return {k: (what, RECORD) for k, what in keys.items()}


def update(root, path, data, stale, new, record):
    """The shared road (ratchets.update, t-1992 N3) on the allow list; a site no row allows keeps the exit red."""
    code = ratchets.update(root, path, data, "allow", key_of, stale, record, RECORD, [TEXT_ROOT], print)
    return ratchets.verdict([code, 1 if new else 0])


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
    data, allow = ratchets.load_list(path, REL, key_of, must_exist=True)
    names = check_names(data.get("names"))
    base = ratchets.base_of(a.root, a.base)  # F4: a bad base is exit 2 even under Python drift
    drift = ratchets.check_basis(data["basis"], basis(), DOOR)
    if drift:
        print("not judged here: python %s, basis %s" % (ratchets.python_minor(), drift))
        return 3
    return finish(a, path, data, base, judge(scan(a.root, names), allow, print))


def finish(a, path, data, base, judged):
    new, stale = judged
    if a.update:
        return update(a.root, path, data, stale, new, a.record)
    old = ratchets.base_doc(a.root, base, REL, print)
    raises = ratchets.judge_raises(a.root, base, REL, raised(old, data), print) if old is not None else 0
    return ratchets.verdict([1 if new or stale else 0, raises])


def main(argv):
    return ratchets.guarded(run, argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
