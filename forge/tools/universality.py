# card: C1-2
"""Universality scanner: the one scanner of C1-2, two scans.

universality.py [--root D] [--base R] [--update [--record ID]] [--basis]    exit 0 green, 1 red, 2 cannot judge, 3 not judged here
Names: every name of forge/universality-names.json in factory/tools and factory/hooks, case-insensitive, bounded by any
non-letter or a camelCase step: lower to upper, or an acronym's end, a capital before a capital and a lower letter
(JIRAClient = JIRA + Client). So jira_url, run_pytest, python3, PytestRunner and getJiraIssue are flagged (t-1992 N5); a
common word that is a name errs red, its door an allow row; a name joined to a word with no case step or non-letter errs
green (pytestish, JIRAAPI, JIRAs).
In code, comments and strings. Cyrillic U+0400-U+04FF: every file of factory/ (factory/data is not name-scanned, its text is).
An allow row is {file, token, reason}, no line. A row that suppresses nothing is `stale:` and red; one without a reason is red.
The list, basis, stale and reason rules, the --update road, the file-set and text readers are ratchets.py's (F246); this
file keeps no copy.
"""
import re
import sys

import ratchets

REL = "forge/universality-names.json"
KINDS = ("language", "runner", "framework", "tracker", "case_manager", "harness")
NAME_ROOTS = ("factory/tools", "factory/hooks")
TEXT_ROOT = "factory"
SCOPE = [TEXT_ROOT + "/**"]  # one glob for the scan and the --update warning (t-1994 F2)
CYRILLIC = re.compile("[\u0400-\u04FF]")
RECORD = ratchets.RECORD
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


def scan(root, a, data):
    """The name sites [((file, token), 'file:line')] and the Cyrillic findings, as one Scan; a file read is counted when read."""
    rx, hits, cyr, files = pattern(check_names(data.get("names"))), [], [], ratchets.files_of(root, SCOPE)
    read = 0
    for rel in files:
        in_names = rel.startswith(tuple(r + "/" for r in NAME_ROOTS))
        for n, line in enumerate(ratchets.text_file(root, rel).split("\n"), 1):
            if CYRILLIC.search(line):
                cyr.append(("%s::cyrillic" % rel, "%s:%d" % (rel, n)))
            if in_names:
                hits += [((rel, m.group(1).lower()), "%s:%d" % (rel, n)) for m in rx.finditer(line)]
        read += 1
    return ratchets.Scan(hits, [], len(files), read, lines=[], red=cyr)


def names_removed(old, data):
    """The tool's own raise key (N13): a name at the base gone at HEAD narrows the scan."""
    words = lambda d: {w.strip() for ws in (d.get("names") or {}).values() for w in ws}
    return {word: "scan narrowed: name removed" for word in sorted(words(old) - words(data))}


SPEC = ratchets.Spec(REL, key_of, "allow", SCOPE, ("allow row added", "allow emptied"), names_removed,
                     lambda data: check_names(data.get("names")), must_exist=True, listing=False)  # t-1997 X3: no --list


def main(argv):
    return ratchets.entry(sys.modules[__name__], argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
