# card: B9
"""Light session retro: counted by code from the journal, reasoned by the Lead (card B9).

retro.py [--root D] write <session>      create or refresh logs/retro/<session>.md (counts block refreshed, reasons kept)
retro.py [--root D] check <file>         recount, compare the counts block byte for byte; list reasons / answers missing
retro.py [--root D] sum --since <date>   add the counters of the sessions that began on or after YYYY-MM-DD
retro.py [--root D] missing              sessions with journal lines and no retro file

Exit: 0 done, 1 check red (counts block differs from a recount), 2 refused input (session, file, date).
Every counter reads journal lines only, through journal.load; a counter the closed event list cannot carry is not counted.
Output is at most 40 lines: the counts block holds BLOCK_MAX lines, detail lines (named bad lines, per-task lines) are
cut first with a marker, the totals never. The slug of ask_owner is the Lead's: a repeated question under a new slug
is not counted (residual).
"""
import argparse
import os
import re
import sys
from collections import Counter

from journal import SESSION_RE, load

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GIT = "git-hooks.jsonl"
BEGIN, END = "<!-- retro:counts:begin -->", "<!-- retro:counts:end -->"
OUT_MAX = 40
BLOCK_MAX = OUT_MAX - 2  # write prints the path line, the block, the missing line: all inside 40
ROLE = re.compile(r"role:(\S*)")
SLUG = re.compile(r"q:(\S+)")
# label, counter key (a key with a colon is a "by" breakdown: dispatch:<role>, refuse:<hook id>)
NAMES = (("dispatch", "dispatch"), ("accept", "accept"), ("reject", "reject"), ("return", "return"),
         ("retried tasks", "retried"), ("cut", "cut"), ("cap_warning", "cap_warning"), ("hook_failed", "hook_failed"),
         ("refuse", "refuse"), ("refuse (git hooks)", "git"), ("ask_owner", "ask_owner"),
         ("ask_owner repeats", "repeats"))
# old session-retro prompt, step 2 (q3-q7); q1 and q2 are carried by the counters and their reasons
QUESTIONS = ("Q1 What did the session have to find out itself although it belonged in the dispatch or on the boot page?",
             "Q2 What was read at the start and never needed?",
             "Q3 Per refusing hook or gate of the counts: refused rightly | refused wrongly | noise?",
             "Q4 Which decisions did the session take itself and is not sure about?",
             "Q5 Which questions to the owner are still open (only what she alone can know or decide)?")


def clean(v):
    """One token: whitespace runs and "=" become "_" (a newline or "=" in a journaled value split a block line; t-2021 B2c)."""
    return re.sub(r"\s+", "_", str(v).strip()).replace("=", "_") or "?"


def hook_id(note):
    return clean(note.split(":", 1)[0])


def own_event(c, per_task, o, ev, note):
    if ev in ("dispatch", "cut", "cap_warning"):  # the role is the note's leading role:<role>; `by` is the writer (t-2021 B1)
        m = ROLE.match(note)
        c["%s:%s" % (ev, clean(m.group(1)) if m else "?")] += 1
    elif ev == "refuse":
        c["refuse:" + hook_id(note)] += 1
    elif ev in ("accept", "reject", "return", "hook_failed"):
        c[ev] += 1
    if ev in ("reject", "return"):
        per_task[clean(o.get("task", ""))] += 1


def tally(entries, session):
    """Return (counter, {task: n} for tasks with more than one reject|return, window (first ts, last ts))."""
    own = session + ".jsonl"
    stamps = [e[0] for e in entries if e[1] == own and e[4] and e[0]]
    win = (min(stamps), max(stamps)) if stamps else ("", "")
    c, per_task, seen = Counter(), Counter(), set()
    for ts, f, _n, _raw, o in entries:  # ts order: a slug is a repeat when an earlier line, any file, carried it
        if not o:
            continue
        ev, note = o.get("event"), str(o.get("note", ""))
        m = SLUG.match(note) if ev == "ask_owner" else None
        if ev == "ask_owner" and f == own:
            c["ask_owner"] += 1
            c["repeats"] += 1 if (m and m.group(1) in seen) else 0
        if m:
            seen.add(m.group(1))
        if f == own and ev != "ask_owner":
            own_event(c, per_task, o, ev, note)
        elif f == GIT and ev == "refuse" and win[0] and win[0] <= ts <= win[1]:
            c["git:" + hook_id(note)] += 1  # a git hook has no session id: the window places it
    retried = {t: n for t, n in per_task.items() if n > 1}
    c["retried"] = len(retried)
    return c, retried, win


def total(c, key):
    return sum(v for k, v in c.items() if k == key or k.startswith(key + ":"))


def render(c, retried, bad, git_absent, status):
    out = ["counts: " + status]
    for label, key in NAMES:
        by = sorted((k.split(":", 1)[1], v) for k, v in c.items() if k.startswith(key + ":"))
        if key == "git" and git_absent:
            out.append(label + ": none journaled")
        else:
            out.append("%s: %s" % (label, " ".join("%s=%d" % kv for kv in by) if by else total(c, key)))
    details = ["  " + b for b in bad] + ["  task %s: %d" % kv for kv in sorted(retried.items())]
    room = BLOCK_MAX - len(out)
    if len(details) > room:
        details = details[:room - 1] + ["  [cut: %d of %d detail lines]" % (len(details) - room + 1, len(details))]
    return out + details


def dated_bad(entries):
    """Return (ts, file, line no) of each unparsable line, dated by the NEXT valid line of its file, "" when none.
    The journal is append-only, so that ts is no earlier than the bad line's write: a line written after a window's end
    never lands inside it. The previous line's ts (load's dating) is only a lower bound (t-2024 N1)."""
    out, nxt = [], {}
    for ts, f, n, _raw, o in sorted(entries, key=lambda e: (e[1], -e[2])):  # per file, last line first
        if o:
            nxt[f] = ts
        else:
            out.append((nxt.get(f, ""), f, n))
    return out


def problems(loaded, own, win):
    """Named problems that mark the block: an own bad line whatever its date; a git-hooks bad line dated inside the
    window; another file's dated up to the window end (an earlier slug feeds repeats, t-2021 F1); an unreadable own or
    git-hooks file (t-2024 N2: no lines read is not "none journaled")."""
    entries, bad, _ = loaded
    mine = ["unparsable line %d in %s" % (n, f) for ts, f, n in dated_bad(entries)
            if f == own or (ts and ts <= win[1] and (f != GIT or win[0] <= ts))]
    return sorted(mine + [b for b in bad if b in ("unreadable file " + own, "unreadable file " + GIT)])


def counts_block(loaded, session):
    """Return (block lines, labels of non-zero counters, window, counter); a function of lines dated up to the window end."""
    entries, _, found = loaded
    if not found:
        return ["counts: unknown -- no journal"], [], ("", ""), Counter()
    c, retried, win = tally(entries, session)
    mine = problems(loaded, session + ".jsonl", win)
    git_absent = not (win[1] and any(e[1] == GIT and e[0] and e[0] <= win[1] for e in entries))
    lines = render(c, retried, mine, git_absent, "incomplete" if mine else "ok")
    return lines, [label for label, key in NAMES if total(c, key) > 0], win, c


def sessions(entries):
    return sorted({e[1][:-6] for e in entries if e[1] != GIT})


def retro_path(root, session):
    return os.path.join(root, "logs", "retro", session + ".md")


def missing_list(root, entries, before=None):
    """Sessions with no retro file; with `before`, only those whose first ts is earlier than it (the card: the earlier ones)."""
    first = {}
    for e in entries:
        if e[4] and e[0]:
            first[e[1][:-6]] = min(e[0], first.get(e[1][:-6], e[0]))
    return [s for s in sessions(entries) if not os.path.exists(retro_path(root, s)) and
            (before is None or (first.get(s) and first[s] < before))]


def missing_line(names):
    return "missing: " + ("unknown" if names is None else ", ".join(names) or "none")


def reasons_section(text):
    lines = text.split("\n")
    a = lines.index("## REASONS") if "## REASONS" in lines else len(lines)
    b = lines.index("## QUESTIONS") if "## QUESTIONS" in lines else len(lines)
    return lines[a + 1:b], lines[b + 1:]


def answered(t):
    return bool(t.strip()) and "<why>" not in t


def gaps(text, names):
    """Return (labels with no reason, question ids with no answer) of a retro file's text."""
    reasons, qs = reasons_section(text)
    no_reason = [n for n in names if not any(l.startswith(n + ":") and answered(l[len(n) + 1:]) for l in reasons)]
    no_answer = [q.split(" ", 1)[0] for q in qs if re.match(r"Q\d ", q) and not answered(q.rpartition(" -> ")[2])]
    return no_reason, no_answer


def read(path):
    with open(path, encoding="utf-8", newline="") as fh:
        return fh.read().replace("\r\n", "\n")  # core.autocrlf checkouts return CRLF: not a hand edit


def fresh_file(session, win, block, names, miss):
    head = ["# retro " + session, "session: " + session, "window: %s .. %s" % win, BEGIN] + block + [END]
    reasons = [n + ": " for n in names] or ["nothing: <why>"]
    return "\n".join(head + ["## REASONS"] + reasons + ["## QUESTIONS"] + [q + " -> " for q in QUESTIONS] +
                     [missing_line(miss), ""])


def refreshed(old, win, block, names, miss):
    """The old text with the counts block, window and missing line replaced; the reasons and answers kept."""
    lines = old.split("\n")
    if not (BEGIN in lines and END in lines and "## REASONS" in lines):
        return None
    b, e = lines.index(BEGIN), lines.index(END)
    lines[b + 1:e] = block
    lines = [("window: %s .. %s" % win) if l.startswith("window: ") else
             missing_line(miss) if l.startswith("missing: ") else l for l in lines]
    reasons, _ = reasons_section("\n".join(lines))
    add = [n + ": " for n in names if not any(l.startswith(n + ":") for l in reasons)]
    at = lines.index("## REASONS") + 1
    lines[at:at] = add
    return "\n".join(lines)


def cmd_write(root, session):
    if not SESSION_RE.fullmatch(session) or session + ".jsonl" == GIT:
        print("refused: the session id must be a journal file stem, [A-Za-z0-9_-]{1,128}, not git-hooks")
        return 2
    loaded = load(root)
    if loaded[2] and session not in sessions(loaded[0]):
        print("refused: no journal lines of session %s" % session)
        return 2
    block, names, win, _ = counts_block(loaded, session)
    miss = missing_list(root, loaded[0], before=win[0]) if win[0] else None  # no window: "earlier" is unknown (t-2024 N3)
    path = retro_path(root, session)
    old = read(path) if os.path.exists(path) else None
    text = fresh_file(session, win, block, names, miss) if old is None else refreshed(old, win, block, names, miss)
    if text is None:
        print("refused: %s lacks the counts markers or the REASONS section; not overwritten" % path)
        return 2
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(path)
    print("\n".join(block + [missing_line(miss)]))
    return 0


def cmd_check(root, file):
    if not os.path.isfile(file):
        print("refused: no file %s" % file)
        return 2
    text = read(file)
    m = re.search(r"^session: (\S+)$", text, re.M)
    lines = text.split("\n")
    if not m or BEGIN not in lines or END not in lines or not SESSION_RE.fullmatch(m.group(1)):
        print("refused: no session line or counts markers in %s" % file)
        return 2
    block, names, _w, _c = counts_block(load(root), m.group(1))
    actual = lines[lines.index(BEGIN) + 1:lines.index(END)]
    no_reason, no_answer = gaps(text, names)
    if no_reason:
        print("reasons missing: " + ", ".join(no_reason))
    if no_answer:
        print("answers missing: " + ", ".join(no_answer))
    if actual != block:
        print("check red: the counts block of %s differs from a recount of the journal" % file)
        return 1
    print("check ok: %s" % file)
    return 0


def cmd_sum(root, since):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", since):
        print("refused: --since is a date YYYY-MM-DD")
        return 2
    loaded = load(root)
    if not loaded[2]:
        print("counts: unknown -- no journal")
        return 0
    total_c, used, bad_s, no_r, no_a = Counter(), [], [], [], []
    for s in sessions(loaded[0]):
        block, names, win, c = counts_block(loaded, s)
        if win[0] and win[0][:10] < since:
            continue
        used.append(s)
        total_c.update(c)
        bad_s += [s] if block[0] != "counts: ok" or not win[0] else []  # no window (every line unparsable): listed, never dropped
        if os.path.exists(retro_path(root, s)):
            r, a = gaps(read(retro_path(root, s)), names)
            no_r += ["%s(%s)" % (s, ",".join(r))] if r else []
            no_a += ["%s(%s)" % (s, ",".join(a))] if a else []
    git_absent = not any(e[1] == GIT for e in loaded[0])
    print("sessions since %s: %d (%s)" % (since, len(used), ", ".join(used) or "none"))
    print("\n".join(render(total_c, {}, [], git_absent, "sum")))
    for label, items in (("incomplete", bad_s), ("reasons missing", no_r), ("answers missing", no_a)):
        if items:
            print("%s: %s" % (label, ", ".join(items)))
    return 0


def cmd_missing(root):
    entries, _, found = load(root)
    if not found:
        print("missing: unknown -- no journal")
        return 0
    miss = missing_list(root, entries)
    print("missing: %d" % len(miss))
    print("\n".join(miss[:OUT_MAX - 2] + (["[cut: %d of %d]" % (len(miss) - OUT_MAX + 2, len(miss))]
                                          if len(miss) > OUT_MAX - 2 else [])))
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=ROOT)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("write").add_argument("session")
    sub.add_parser("check").add_argument("file")
    sub.add_parser("sum").add_argument("--since", required=True)
    sub.add_parser("missing")
    a = p.parse_args(argv)
    if a.cmd == "write":
        return cmd_write(a.root, a.session)
    if a.cmd == "check":
        return cmd_check(a.root, a.file)
    if a.cmd == "sum":
        return cmd_sum(a.root, a.since)
    return cmd_missing(a.root)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
