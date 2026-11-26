# card: B3
"""Owner-words registry: forge/owner-words.yaml, schema words/2, written in JSON syntax (valid YAML) and read with json:
no PyYAML, as factory/data/secret-patterns.yaml. Card B3 (amended by B13, B14, B20).

words.py [--root D] check               every W-/D- citation in the rule files exists and is live; BOOT line classes
words.py [--root D] show <id>           print the record
words.py [--root D] resolve <id>        print `<id> <kind> live|superseded by <id>`; exit 0 only for a live record (B20)
words.py [--root D] add <file|->        the ONE writer: a record as UTF-8 JSON, append-only, every bad field named (B14)

Exit: check 0 green (`listed:` lines are for the owner, never red), 1 red, 2 cannot judge (registry unreadable or absent,
or a BOOT `plan` line with the plan copy absent);
add 0 written, 1 registry busy, 2 refused. Importable: resolve_id(root, id) (B20), plan_key_ok(root, key) (B13: the one
resolver of `plan <h>[.<n>]` keys). Two residuals, known: a paraphrase entered as words is not detectable by code (the
critic compares `words` with the text at `carrier`); a citation inside forge/tests/ or forge/specs/ is not counted
(fixtures and history).
"""
import argparse
import datetime
import json
import os
import re
import subprocess
import sys

import journal  # one OS lock form with the journal (B14): take_lock, jdir

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REG = "forge/owner-words.yaml"
PLAN = "forge/specs/20261125-forge2-light-factory-plan.md"
BOOT = "forge/BOOT.md"
SCHEMA = "words/2"
KINDS = ("word", "decision")
SCOPES = ("factory", "forge", "both", "unknown")
WHO = ("owner", "lead")
WORDS_MAX = 8192
COMMON = ("id", "kind", "date", "scope", "scope_by", "asked", "carrier", "executed_in", "open", "supersedes")
FIELDS = {"word": COMMON + ("words",), "decision": COMMON + ("text", "decided_by", "rests_on", "basis")}
ORDER = COMMON[:7] + ("words", "text", "decided_by", "rests_on", "basis") + COMMON[7:]
ID_RE = {"word": re.compile(r"W-[1-9]\d*"), "decision": re.compile(r"D-[1-9]\d*")}
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})(~([01]\d|2[0-3]):[0-5]\d)?")
CITE_RE = re.compile(r"(?<![\w-])([WD])-([1-9]\d*)\b")
CASE_W_RE = re.compile(r"\(case:\s*(W-[^)]*)\)")
EXEMPT = (re.compile(r"decided by the owner: forge/owner-words\.yaml"), re.compile(r"phase \d+: .+ -- \S+"))
EXEMPT_DIRS = ("forge/specs", "forge/tests")
DOOR = "run `python -B C:/QAFactory/forge2-repo/forge/tools/words.py` (the main checkout's script)"


def read_registry(root):
    """Return (records, error); error names file and line, and a half-read registry is never returned."""
    try:
        with open(os.path.join(root, REG), "rb") as fh:
            raw = fh.read()
    except OSError as e:
        return None, "%s: %s" % (REG, e.strerror)
    try:
        data = json.loads(raw.decode("utf-8"))
    except UnicodeDecodeError as e:
        return None, "%s:%d: not UTF-8" % (REG, raw[:e.start].count(b"\n") + 1)
    except ValueError as e:
        return None, "%s:%s: broken syntax (%s)" % (REG, getattr(e, "lineno", 1), e)
    recs = data.get("records") if isinstance(data, dict) else None
    if not isinstance(recs, list) or data.get("schema") != SCHEMA or not all(isinstance(r, dict) for r in recs):  # M3
        return None, "%s:1: not a %s registry" % (REG, SCHEMA)
    return recs, None


def render(records):
    """The file text: one record per line, so an append is one added line in a diff."""
    body = ",\n".join("  " + json.dumps(r, ensure_ascii=False) for r in records)
    return '{"schema": "%s", "records": [\n%s\n]}\n' % (SCHEMA, body)


def by_id(records):
    return {str(r.get("id")): r for r in records}


def superseded(records):
    """Map id -> id of the record that supersedes it; an id absent from the map is live."""
    return {r["supersedes"]: r["id"] for r in records if isinstance(r.get("supersedes"), str)}


def resolve_id(root, rid):
    """B20: (kind, None) for a live record, (kind, <superseding id>) for a superseded one, None when absent or unreadable."""
    records, err = read_registry(root)
    rec = None if err else by_id(records).get(rid)
    return None if rec is None else (rec.get("kind"), superseded(records).get(rid))


def text_problem(rec, key):
    v = rec.get(key)
    return [] if isinstance(v, str) and v.strip() else ["%s is missing or empty" % key]


def date_problems(d):
    m = DATE_RE.fullmatch(d) if isinstance(d, str) else None
    try:
        datetime.date.fromisoformat(m.group(1))
    except (AttributeError, ValueError):
        return ["date %r is not YYYY-MM-DD, optionally ~HH:MM" % (d,)]
    return []


def executed_problems(rec):
    ex = rec.get("executed_in")
    if not isinstance(ex, list) or not all(isinstance(x, str) and x for x in ex):
        return ["executed_in must be a list of non-empty strings"]
    return [] if ex else text_problem(rec, "open")


def common_problems(rec, known):
    out, rid, sup = [], rec.get("id"), rec.get("supersedes")
    if not (isinstance(rid, str) and ID_RE[rec["kind"]].fullmatch(rid)):
        out.append("id %r does not match %s" % (rid, ID_RE[rec["kind"]].pattern))
    elif rid in known:
        out.append("id %s exists: a record is never changed; write a new record with `supersedes`" % rid)
    out += date_problems(rec.get("date"))
    for key, allowed in (("scope", SCOPES), ("scope_by", WHO)):
        if rec.get(key) not in allowed:
            out.append("%s %r is not one of %s" % (key, rec.get(key), ", ".join(allowed)))
    out += text_problem(rec, "asked") + text_problem(rec, "carrier") + executed_problems(rec)
    if sup is not None and (not isinstance(sup, str) or sup not in known):
        out.append("supersedes %r names no earlier record" % (sup,))
    return out


def word_problems(rec):
    out, n = text_problem(rec, "words"), len(str(rec.get("words")).encode("utf-8", "surrogatepass"))
    if not out and n > WORDS_MAX:
        out.append("words is %d bytes, over %d; split into records by topic, each verbatim" % (n, WORDS_MAX))
    return out


def decision_problems(rec, known):
    out, rest = text_problem(rec, "text"), rec.get("rests_on")
    if rec.get("decided_by") not in WHO:
        out.append("decided_by %r is not one of %s" % (rec.get("decided_by"), ", ".join(WHO)))
    if not isinstance(rest, list) or not all(isinstance(x, str) and known.get(x, {}).get("kind") == "word" for x in rest):
        out.append("rests_on must be a list of existing W-ids")
    elif not rest:
        out += ["rests_on is empty and " + p for p in text_problem(rec, "basis")]
    return out


def problems(rec, known):
    """Every bad field of one record, named; known maps the ids of the records before it."""
    kind = rec.get("kind")
    if kind not in KINDS:
        return ["kind %r is not one of %s" % (kind, ", ".join(KINDS))]
    out = ["unknown field %r for kind %s" % (k, kind) for k in rec if k not in FIELDS[kind]]
    out += common_problems(rec, known)
    return out + (word_problems(rec) if kind == "word" else decision_problems(rec, known))


def plan_key_ok(root, key):
    """B13: does the plan key `<h>` or `<h>.<n>` resolve in the plan copy: exactly one `###` heading numbered h and, for
    h.n, exactly one item `n. ` under it. None when the plan copy is unreadable (a key is never judged on no data)."""
    try:
        with open(os.path.join(root, PLAN), "rb") as fh:
            lines = fh.read().decode("utf-8", "replace").split("\n")
    except OSError:
        return None
    m = re.fullmatch(r"(\d+[^\W\d_]?)(?:\.(\d+))?", key)
    heads = [i for i, s in enumerate(lines) if m and re.match(r"### %s\.? " % re.escape(m.group(1)), s)]
    if len(heads) != 1 or not m.group(2):
        return len(heads) == 1
    end = next((j for j in range(heads[0] + 1, len(lines)) if lines[j].startswith("#")), len(lines))
    return sum(1 for s in lines[heads[0] + 1:end] if re.match(r"\s*%s\. " % m.group(2), s)) == 1


def rule_files(root):
    found = ["CLAUDE.md"]
    for top in (".claude/agents", "forge", "factory"):
        for d, dirs, names in os.walk(os.path.join(root, top)):
            rel = os.path.relpath(d, root).replace(os.sep, "/")
            dirs[:] = sorted(x for x in dirs if x != "__pycache__" and rel + "/" + x not in EXEMPT_DIRS)
            found += [rel + "/" + n for n in sorted(names)]
    return [p for p in found if p != REG and os.path.isfile(os.path.join(root, p))]


def cite_findings(rel, n, rid, records):
    """(red, listed) for one cited id: missing, superseded, scope unknown, scope mismatch (red only when the owner named it)."""
    rec, where = by_id(records).get(rid), "%s:%d: %s" % (rel, n, rid)
    if rec is None:
        return [where + " no such record"], []
    if rid in superseded(records):
        return [where + " superseded by " + superseded(records)[rid]], []
    scope = rec.get("scope")
    if scope == "unknown":
        return [], [where + " scope unknown: for the owner"]
    if scope != "both" and (scope == "forge") == rel.startswith("factory/"):
        msg = where + " scope mismatch (record scope: %s)" % scope
        return ([msg], []) if rec.get("scope_by") == "owner" else ([], [msg + ", named by the lead: for the owner"])
    return [], []


def line_findings(rel, n, line, records):
    """(red, listed, citations) of one text line."""
    red, listed, ids = [], [], ["%s-%s" % m.groups() for m in CITE_RE.finditer(line)]
    for rid in ids:
        r, li = cite_findings(rel, n, rid, records)
        red, listed = red + r, listed + li
    red += ["%s:%d: decision cited as owner's word: %s" % (rel, n, g) for g in CASE_W_RE.findall(line) if any(m.group(1) == "D" for m in CITE_RE.finditer(g))]
    return red, listed, len(ids)


def citation_findings(root, records):
    red, listed, count = [], [], 0
    for rel in rule_files(root):
        try:
            with open(os.path.join(root, rel), "rb") as fh:
                text = fh.read().decode("utf-8", "replace")  # ids are ASCII: a non-UTF-8 file is still judged (B3-3)
        except OSError:
            continue  # an unreadable file holds no rule text
        for n, line in enumerate(text.split("\n"), 1):
            r, li, c = line_findings(rel, n, line, records)
            red, listed, count = red + r, listed + li, count + c
    return red, listed, count


class PlanAbsent(Exception):
    """A BOOT class-2 line met no plan copy: check cannot judge (exit 2), it is not a red."""


def boot_line(root, s):
    """The class of one BOOT line: an exempt marker, `ok`, or the red text (B1's classes: plan, exempt; no word class)."""
    m = re.search(r"\(plan (\S+)\)$", s)
    # t-2025 F3, t-2028 F5: the page states principles, her words stay records (W-101); a W or D id anywhere is refused
    kinds = {c.group(1) for c in CITE_RE.finditer(s)}
    if "W" in kinds:
        return "owner word on BOOT: cite the plan item that states the rule"
    if "D" in kinds:
        return "decision cited as owner's word"
    # t-2030 F6: ids are read before the exempt patterns, so an exempt line holding an id is refused too
    for i, pat in enumerate(EXEMPT):
        if pat.fullmatch(s):
            return "exempt:%d" % i
    if m:
        return {True: "ok", False: "plan id absent: " + m.group(1), None: "plan copy unreadable"}[plan_key_ok(root, m.group(1))]
    return "uncited line"


def boot_findings(root):
    """(red, listed) for forge/BOOT.md: absent -> `BOOT not written yet`, no line checked."""
    try:
        with open(os.path.join(root, BOOT), "rb") as fh:
            lines = fh.read().decode("utf-8", "replace").split("\n")
    except OSError:
        return [], ["BOOT not written yet"]
    red, seen = [], [0, 0]
    for n, s in enumerate((x.strip() for x in lines), 1):
        c = boot_line(root, s) if s and not s.startswith("#") else "ok"
        if c == "plan copy unreadable":
            raise PlanAbsent("%s:%d: plan copy %s unreadable" % (BOOT, n, PLAN))  # B3-4: a key is never judged on no data
        if c.startswith("exempt:"):
            seen[int(c[7:])] += 1
        elif c != "ok":
            red.append("%s:%d: %s" % (BOOT, n, c))
    red += ["%s: exempt line %d must stand exactly once, found %d" % (BOOT, i + 1, k) for i, k in enumerate(seen) if k != 1]
    return red, []


def registry_findings(records):
    """Shape of every record, in order, and the listed decisions that rest on a superseded word."""
    red, listed, known, sup = [], [], {}, superseded(records)
    for r in records:
        red += ["%s: %s" % (r.get("id"), p) for p in problems(r, known)]
        known[str(r.get("id"))] = r
        rests = r.get("rests_on") if isinstance(r.get("rests_on"), list) else []
        listed += ["%s rests on %s, superseded by %s" % (r.get("id"), w, sup[w]) for w in rests if w in sup]
    return red, listed


def check(root):
    records, err = read_registry(root)
    if err:
        print("cannot judge: " + err)
        return 2
    try:
        (r1, l1), (r2, l2, count), (r3, l3) = registry_findings(records), citation_findings(root, records), boot_findings(root)
    except PlanAbsent as e:
        print("cannot judge: " + str(e))
        return 2
    print("%d citations" % count)
    for tag, rows in (("red", r1 + r2 + r3), ("listed", l1 + l2 + l3)):
        for row in rows:
            print("%s: %s" % (tag, row))
    return 1 if r1 + r2 + r3 else 0


def linked_worktree(root):
    """B14: True when root is a linked git worktree (git-dir differs from git-common-dir); not a repository -> False."""
    dirs = []
    for flag in ("--git-dir", "--git-common-dir"):
        try:
            r = subprocess.run(["git", "-C", root, "rev-parse", flag], capture_output=True, text=True, timeout=20)
        except (OSError, subprocess.SubprocessError):
            return False
        if r.returncode:
            return False
        dirs.append(os.path.realpath(os.path.join(root, r.stdout.strip())))
    return dirs[0] != dirs[1]


def parse_record(raw):
    try:
        rec = json.loads(raw.decode("utf-8"))
    except UnicodeDecodeError as e:
        return None, "input is not UTF-8 (line %d)" % (raw[:e.start].count(b"\n") + 1)
    except ValueError as e:
        return None, "input is not JSON (%s)" % e
    return (rec, None) if isinstance(rec, dict) else (None, "input is not one JSON object")


def raw_registry(path):
    with open(path, "rb") as fh:
        return fh.read()


def append(root, rec):
    records, err = read_registry(root)
    path = os.path.join(root, REG)
    # CRLF is how git checks the file out under autocrlf: judged as LF, and the write below is LF (git converts back)
    if not err and raw_registry(path).replace(b"\r\n", b"\n") != render(records).encode("utf-8", "surrogatepass"):
        # B3-2: a re-render of a hand-edited file would drop its extra keys and collapse duplicates unseen
        err = "%s is not canonical (hand-edited); a record is only appended to a canonical file: " \
              "rewrite it with words.render(records) or restore it from git, then add again" % REG
    probs = [err] if err else problems(rec, by_id(records))
    if probs:
        print("\n".join("refused: " + p for p in probs))
        return 2
    try:
        blob = render(records + [{k: rec[k] for k in ORDER if k in rec}]).encode("utf-8")
    except UnicodeEncodeError:
        print("refused: text is not encodable as UTF-8")
        return 2
    with open(path + ".tmp", "wb") as fh:
        fh.write(blob)
    os.replace(path + ".tmp", path)
    print("added %s" % rec["id"])
    return 0


def add(root, raw):
    if linked_worktree(root):
        print("refused: %s is a linked worktree; the registry is written in the main checkout only: %s" % (root, DOOR))
        return 2
    rec, err = parse_record(raw)
    if err:
        print("refused: " + err)
        return 2
    os.makedirs(journal.jdir(root), exist_ok=True)
    lock = os.path.join(journal.jdir(root), ".lock")
    fd = journal.take_lock(lock)
    if fd is None:
        print("registry busy: %s held for over %d s, nothing written" % (lock, journal.LOCK_WAIT_S))
        return 1
    try:
        return append(root, rec)
    finally:
        journal.release_lock(fd)


def lookup(root, rid, full):
    """show (full) or resolve: the record, or kind and live state."""
    records, err = read_registry(root)
    if err:
        print("cannot judge: " + err)
        return 2
    rec, res = by_id(records).get(rid), resolve_id(root, rid)
    if rec is None:
        print("%s: no such record" % rid)
        return 1
    if full:
        print(json.dumps(rec, ensure_ascii=False, indent=1))
        return 0
    print("%s %s %s" % (rid, res[0], "live" if res[1] is None else "superseded by " + res[1]))
    return 0 if res[1] is None else 1


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=ROOT)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check")
    for name in ("show", "resolve"):
        sub.add_parser(name).add_argument("id")
    sub.add_parser("add").add_argument("file")
    a = p.parse_args(argv)
    if a.cmd == "check":
        return check(a.root)
    if a.cmd == "add":
        try:
            with (sys.stdin.buffer if a.file == "-" else open(a.file, "rb")) as fh:
                raw = fh.read()
        except OSError as e:
            print("refused: cannot read %s: %s" % (a.file, e.strerror or e))
            return 2
        return add(a.root, raw)
    return lookup(a.root, a.id, a.cmd == "show")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
