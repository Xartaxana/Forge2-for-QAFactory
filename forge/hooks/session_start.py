# card: B2
# hook: SessionStart
"""SessionStart hook (cards B2, B17 (c) (d) start facts): prints what to re-read at a session start and after a compaction.
It prints only, exit 0.

session_start.py [--root D]   D defaults to this repository. Input: the event JSON on stdin, field `source`
(startup|resume|clear|compact); empty, broken or unknown -> as startup.
Order -- stable lines first, volatile ones last (owner's word 27.11.2026: the start text must not break the prompt cache; it
is written once per session, and a stable head keeps the longest prefix byte-equal between sessions):
(1) forge/BOOT.md on startup|clear|compact; (2) the re-read line, always; (3) `hooks: harness <w> of <n> wired[ (...)]; git:
hooksPath <ok|wrong: v|unset>, <t> of <m> tracked executable` (B17 (c)); (4) the carriers checklist on compact; then the volatile
lines: (5) `now: <date weekday HH:MM offset> | last: <ts> <event> <task> by <by> | snapshot: <newest> (<age> old) | open: <ids>`;
(6) `main: ahead <a>, behind <b> of origin/main (no fetch)` or `main: ahead/behind unknown (<why>)` (S10); (7) `old processes:
<k> started from this tree, older than 7200 s[: <pid> <age> <parent gone|parent <pid>> <head>; ...]` (B17 (d), advice: code
stops nothing); (8) `worktrees:` each linked worktree with its branch and task state, read-only (B17 (e)'s sweep is not built);
(9) the previous session's end on startup. Every call shares START_BUDGET_S; a call past it prints `not collected: start budget`.
Any error -> one line `reminder failed: <error>; read forge/BOOT.md by hand`.
Cap 6144 emitted bytes: the open list is cut first, then the checklist, then the process and worktree rows, each with a
`[cut: <what>]` marker; a valid UTF-8 BOOT never; a non-UTF-8 BOOT last, to the cap, then a marker line: `shown with
replacement characters` or `cut after file byte <k> of <total>`.
"""
import datetime
import glob
import json
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from hio import io as HIO  # noqa: E402

CAP = 6144
OPEN_MAX = 10
GIT_WAIT_S = 5
BOOT_SOURCES = ("startup", "clear", "compact")
START_BUDGET_S = 30  # B17 (c): every call of this hook shares it, counted from the hook's start
OLD_PROCESS_S = 7200  # B17 (d): strictly older is listed
ROWS_MAX = 5
PROCESS_LIST_TIMEOUT_S = 5
CUT = 64  # FH-4107: one cut for every outside value (journal fields, command heads, paths)
CMD_MAX = 65536  # FH-5131
T0 = None  # set by run() before the stdin read (t-2106 F3): the budget counts from the hook's start
UTC = datetime.timezone.utc
STAMP = re.compile(r"^(\d{8}T\d{6}Z)")
HOOK_MARK = re.compile(r"#\s*hook:\s*(\w+)$")
HOOK_CMD = re.compile(r'python(?:\s+-B)?\s+"\$CLAUDE_PROJECT_DIR/(forge/hooks/[\w.-]+\.py)"$')
NT_DATE = re.compile(r"/Date\((-?\d+)\)/")
PS_NT = ("[Console]::OutputEncoding=[Text.Encoding]::UTF8; Get-CimInstance Win32_Process | "
         "Select-Object ProcessId,ParentProcessId,CreationDate,CommandLine | ConvertTo-Json -Compress")


def boot_block(root, eval_arm, show):
    """Return (text, present, bad). Presence is read on every source (t-2010 B2-1/B2-2); the text only when `show`.
    In an eval arm an absent BOOT prints nothing (B1's `without` arm, F3). bad: the raw bytes of a non-UTF-8 BOOT."""
    p = os.path.join(root, "forge", "BOOT.md")
    if not os.path.isfile(p):
        return ("" if eval_arm or not show else "forge/BOOT.md not written yet (B1)"), False, None
    if not show:
        return "", True, None
    with open(p, "rb") as fh:
        raw = fh.read()
    try:
        return raw.decode("utf-8"), True, None
    except UnicodeDecodeError:
        return "", True, raw


def span(raw, i):
    """(text, byte length) of the character at raw[i]: a valid one as is, a bad byte run as one U+FFFD."""
    chunk = raw[i:i + 4]
    try:
        ch = chunk.decode("utf-8")[0]
    except UnicodeDecodeError as exc:
        if exc.start == 0:
            return chr(0xFFFD), max(1, exc.end)
        ch = chunk[:exc.start].decode("utf-8")[0]
    return ch, len(ch.encode("utf-8"))


def bad_boot(raw, n):
    """The non-UTF-8 BOOT shown with replacement characters, cut to n text bytes at a character edge, then one marker line
    saying which: nothing cut, or cut after file byte k of the total (k = file bytes whose text was printed; t-2016 B2-N1)."""
    kept, used, k = [], 0, 0
    while k < len(raw):
        ch, size = span(raw, k)
        if used + len(ch.encode("utf-8")) > n:
            break
        kept.append(ch)
        used += len(ch.encode("utf-8"))
        k += size
    if k >= len(raw):
        return "".join(kept) + "\nforge/BOOT.md not UTF-8: shown with replacement characters, fix the file"
    return "".join(kept) + "\nforge/BOOT.md not UTF-8: cut after file byte %d of %d, fix the file" % (k, len(raw))


def open_text(status, tasks, bad, pending=()):
    if status == "unknown":
        return "unknown -- no journal"
    more = " and %d more" % (len(tasks) - OPEN_MAX) if len(tasks) > OPEN_MAX else ""
    text = (", ".join(clip(t) + (" (result pending)" if t in pending else "") for t in tasks[:OPEN_MAX]) + more) or "none"  # F1
    return text + (" (incomplete: %d unreadable journal lines)" % len(bad) if status == "incomplete" else "")


def snap_key(name):
    """(stamp, suffix number): snapshot.py names a second snapshot of one second `<stamp>-2.md` (t-2010 B2-3)."""
    m = re.match(r"^(.*?)(?:-(\d+))?\.md$", name)
    return (m.group(1), int(m.group(2) or 1)) if m else (name, 0)


def spent():
    """True once the start budget is gone: no call starts after it (B17 (c))."""
    return T0 is not None and time.monotonic() - T0 >= START_BUDGET_S


def clip(value):
    """An outside value on one line: control characters as \\uXXXX, cut at CUT characters (FH-4107)."""
    return "".join(c if c.isprintable() else "\\u%04x" % ord(c) for c in str(value))[:CUT]


def age(seconds):
    m = max(0, int(seconds)) // 60
    return "%dm" % m if m < 60 else "%dh%02dm" % divmod(m, 60) if m < 1440 else "%dd%02dh" % (m // 1440, m % 1440 // 60)


def newest_snapshot(root, now):
    """The newest snapshot by name with its age: from the name's UTC stamp, else the file time marked `~` (B17 (c))."""
    folder = os.path.join(root, "logs", "journal", "snapshots")
    names = sorted((os.path.basename(n) for n in glob.glob(os.path.join(folder, "*.md"))), key=snap_key)
    if not names:
        return "none yet -- write one: python -B forge/tools/snapshot.py"
    m, made, mark = STAMP.match(names[-1]), None, ""
    try:
        made = datetime.datetime.strptime(m.group(1), "%Y%m%dT%H%M%SZ").replace(tzinfo=UTC) if m else None
    except ValueError:
        pass
    if made is None:
        made, mark = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(folder, names[-1])), UTC), "~"
    return "logs/journal/snapshots/%s (%s%s old)" % (clip(names[-1]), mark, age((now - made).total_seconds()))


def now_text(now):
    """FH-4111: the local clock with the weekday, so a session never trusts a narrated time; minutes, no seconds."""
    z = now.strftime("%z")
    return now.strftime("%Y-%m-%d %a %H:%M ") + z[:3] + ":" + z[3:]


def last_text(entries, found):
    """FH-4115: ts, event, task and agent of the journal's last parsed line; an unparsable tail says (incomplete)."""
    if not found:
        return "? -- no journal"
    parsed = [e for e in entries if e[4]]
    if not parsed:
        return "no journal lines" + (" (incomplete)" if entries else "")
    o = parsed[-1][4]
    tail = " (incomplete)" if parsed[-1] is not entries[-1] else ""
    return "%s %s %s by %s" % tuple(clip(o.get(k) or "-") for k in ("ts", "event", "task", "by")) + tail


def harness_hooks(root):
    """{forge/hooks/<file>: event} of the files whose first 3 lines carry `hook: <Event>`: the files are the list (FH-2009)."""
    want = {}
    for p in sorted(glob.glob(os.path.join(root, "forge", "hooks", "*.py"))):
        with open(p, encoding="utf-8", errors="replace") as fh:
            for line in [fh.readline() for _ in range(3)]:
                m = HOOK_MARK.match(line.strip())
                if m:
                    want["forge/hooks/" + os.path.basename(p)] = m.group(1)
    return want


def harness_text(root, want):
    """FH-2029, FH-2033, FH-2034: wired = .claude/settings.json names the file under its event; a missing file is broken,
    a command in no legal form unparsed, never guessed."""
    path = os.path.join(root, ".claude", "settings.json")
    if not os.path.isfile(path):
        return "harness 0 of %d wired (no settings.json)" % len(want)
    try:
        with open(path, encoding="utf-8") as fh:
            events = json.load(fh).get("hooks", {})  # a non-object `hooks` raises below: `?`, never read as empty
        wired, broken, unparsed = set(), 0, 0
        for event, h in [(e, h) for e, groups in events.items() for g in groups for h in g.get("hooks") or []]:  # F5: flat
            m = HOOK_CMD.match(str(h.get("command", "")).strip())
            if not m:
                unparsed += 1
            elif not os.path.isfile(os.path.join(root, m.group(1))):
                broken += 1
            else:
                wired.add((m.group(1), event))
    except (OSError, ValueError, AttributeError, TypeError):
        return "harness ?"
    miss = [clip("%s@%s" % (os.path.basename(f), e)) for f, e in sorted(want.items()) if (f, e) not in wired]
    notes = (["not wired: " + ", ".join(miss)] if miss else []) + (["%d broken" % broken] if broken else []) + \
        (["%d unparsed" % unparsed] if unparsed else [])
    return "harness %d of %d wired" % (len(want) - len(miss), len(want)) + "".join(" (%s)" % n for n in notes)


def git_hooks_text(root):
    """FH-2030, FH-2032, FH-2035: core.hooksPath resolves to forge/hooks/git of the main checkout; every extensionless file
    there is tracked with mode 100755. A relative hooksPath is resolved as git does: against the top of the work tree of `root`
    (git rev-parse --show-toplevel), so from a linked worktree whose hooks are not main's the line reads `wrong: <value>`
    (card B17 (c); t-2108 N1); the files are counted in the main checkout. A git call that
    fails is `?` with its reason, never a zero (AR-27, AR-28; t-2106 F2)."""
    common, why = git_out(root, "rev-parse", "--path-format=absolute", "--git-common-dir")
    if common is None:
        return "? (%s)" % why
    main = os.path.dirname(os.path.normpath(common.strip()))
    val, why = git_out(main, "config", "--get", "core.hooksPath")
    if val is None:
        hp = "unset" if why == "git exit 1" else "? (%s)" % why
    else:
        top, why = git_out(root, "rev-parse", "--show-toplevel")
        if top is None:
            hp = "? (%s)" % why
        else:
            same = os.path.normcase(os.path.normpath(os.path.join(top.strip(), val.strip()))) == \
                os.path.normcase(os.path.normpath(os.path.join(main, "forge", "hooks", "git")))
            hp = "ok" if same else "wrong: " + clip(val.strip())
    folder = os.path.join(main, "forge", "hooks", "git")
    files = sorted(f for f in os.listdir(folder) if "." not in f and os.path.isfile(os.path.join(folder, f))) \
        if os.path.isdir(folder) else []
    staged, why = git_out(main, "-c", "core.quotepath=false", "ls-files", "-s", "--", "forge/hooks/git")
    if staged is None:
        return "hooksPath %s, %d files, tracked ? (%s)" % (hp, len(files), why)
    modes = {}
    for line in staged.splitlines():
        head_, _, name = line.partition("\t")
        modes[name] = head_.split(" ")[0]
    execs = sum(modes.get("forge/hooks/git/" + f) == "100755" for f in files)
    loose = sum("forge/hooks/git/" + f not in modes for f in files)
    return "hooksPath %s, %d of %d tracked executable%s" % (hp, execs, len(files), " (%d untracked)" % loose if loose else "")


def hooks_text(root):
    if not os.path.isdir(os.path.join(root, "forge", "hooks")):
        return "hooks: none in the repo yet (C1-5)"
    return "hooks: %s; git: %s" % (harness_text(root, harness_hooks(root)), git_hooks_text(root))


def parse_nt(text):
    data = json.loads(text)
    data = [data] if isinstance(data, dict) else data
    if not isinstance(data, list):
        raise ValueError("not a list")
    out = []
    for d in data:
        d = d if isinstance(d, dict) else {}
        m, pid, ppid = NT_DATE.match(str(d.get("CreationDate") or "")), d.get("ProcessId"), d.get("ParentProcessId")
        ok = m and isinstance(pid, int) and isinstance(ppid, int)
        out.append((pid, ppid, int(m.group(1)) / 1000.0, d.get("CommandLine") or "") if ok else None)
    return out


def parse_ps(text, now_s):
    out = []
    for line in (x for x in text.splitlines() if x.strip()):
        parts = line.split(None, 3)
        ok = len(parts) >= 3 and all(p.isdigit() for p in parts[:3])
        out.append((int(parts[0]), int(parts[1]), now_s - int(parts[2]), parts[3] if len(parts) > 3 else "") if ok else None)
    return out


def process_list(now_s):
    """(rows, unreadable, why): rows [(pid, ppid, created_s, command)] from ONE OS call (FH-5121), or None with why."""
    if spent():
        return None, 0, "not collected: start budget"
    if os.name == "nt":
        argv, kw = ["powershell", "-NoProfile", "-NonInteractive", "-Command", PS_NT], {"creationflags": 0x08000000}
    else:
        argv, kw = ["ps", "-eo", "pid=,ppid=,etimes=,args="], {}
    try:
        r = subprocess.run(argv, capture_output=True, timeout=PROCESS_LIST_TIMEOUT_S, **kw)
        text = r.stdout.decode("utf-8")
        raw = (parse_nt(text) if os.name == "nt" else parse_ps(text, now_s)) if text.strip() and not r.returncode else None
    except subprocess.TimeoutExpired:
        return None, 0, "process list slower than %d s" % PROCESS_LIST_TIMEOUT_S
    except (OSError, ValueError) as exc:
        return None, 0, "process list unreadable: %s" % clip(exc)
    if raw is None:
        return None, 0, "process list exit %d, %d bytes" % (r.returncode, len(r.stdout))
    rows = [x for x in raw if x]
    return (rows or None), len(raw) - len(rows), ("" if rows else "all rows unreadable")


def worktree_blocks(root):
    """(blocks, why): `git worktree list --porcelain` read ONCE per run and shared (t-2106 F4); block 0 is the main one."""
    got, why = git_out(root, "worktree", "list", "--porcelain")
    if got is None:
        return None, why
    return [dict((x.split(" ", 1) + [""])[:2] for x in b.splitlines()) for b in got.strip().split("\n\n") if b.strip()], None


def tree_roots(root, blocks):
    """The main root and every worktree path (t-1973 F7 (d)); git failing -> the main root only, marked."""
    paths = [b["worktree"] for b in blocks or [] if "worktree" in b]
    return [root] + paths, "" if blocks is not None else " (worktree roots not read)"


def from_tree(command, roots):
    """A root followed by a separator, a quote, whitespace or the end, case-insensitive in `/` form: `...-old` is not it."""
    c = command[:CMD_MAX].replace("\\", "/").lower()
    return any(re.search(re.escape(r.replace("\\", "/").rstrip("/").lower()) + r"(?=[/\"'\s]|$)", c) for r in roots)


def head(command):
    """The executable's basename plus its arguments, cut like every outside value (t-1973 F7 (c))."""
    c = command.strip()
    exe, rest = c[1:].partition('"')[::2] if c.startswith('"') else c.partition(" ")[::2]
    return clip((re.split(r"[/\\]", exe)[-1] + " " + rest.strip()).strip())


def ancestors(by):
    """This hook and its ancestors; a parent link counts only when the parent is older than the child (FH-5117, FH-5118)."""
    out, pid = set(), os.getpid()
    while pid in by and pid not in out:
        out.add(pid)
        parent = by.get(by[pid][1])
        pid = parent[0] if parent and parent[2] <= by[pid][2] else None
    return out


def old_text(root, now_s, wt):
    """(full line, line with the rows cut): processes started from this tree, older than OLD_PROCESS_S (B17 (d))."""
    rows, unreadable, why = process_list(now_s)
    if rows is None:
        line = "old processes: ? (%s)" % why
        return line, line
    roots, note = tree_roots(root, wt[0])
    by = {r[0]: r for r in rows}
    skip = ancestors(by)
    old = sorted((r for r in rows if r[0] not in skip and now_s - r[2] > OLD_PROCESS_S and from_tree(r[3], roots)),
                 key=lambda r: (r[2], r[0]))

    def parent(r):  # FH-5127: absent, or created after the child (a reused pid) -> gone
        p = by.get(r[1])
        return "parent %d" % r[1] if p and p[2] <= r[2] else "parent gone"
    items = ["%d %s %s %s" % (r[0], age(now_s - r[2]), parent(r), head(r[3])) for r in old]
    more = " and %d more" % (len(items) - ROWS_MAX) if len(items) > ROWS_MAX else ""
    tail = (" (%d rows unreadable)" % unreadable if unreadable else "") + note
    lead = "old processes: %d started from this tree, older than %d s" % (len(old), OLD_PROCESS_S)
    if not items:
        return lead + tail, lead + tail
    return lead + ": " + "; ".join(items[:ROWS_MAX]) + more + tail, lead + " [cut: rows]" + tail


def worktrees_text(wt, entries, status, tasks):
    """(full rows, rows cut): each linked worktree with its branch and the state of its `w/<task>` task, read-only."""
    blocks, why = wt
    if blocks is None:
        line = "worktrees: ? -- %s" % why
        return line, line
    if len(blocks) < 2:
        return "worktrees: none linked", "worktrees: none linked"
    sent = {(e[4] or {}).get("task") for e in entries if (e[4] or {}).get("event") == "dispatch"}
    rows = []
    for b in blocks[1:]:
        branch = b.get("branch", "").replace("refs/heads/", "", 1) or "detached"
        task = branch[2:] if branch.startswith("w/") else ""
        if "prunable" in b:
            state = "folder gone -- run git worktree prune by hand"
        elif not task:
            state = "state unknown: no task in branch name"
        elif status != "ok":
            state = "state unknown: " + ("no journal" if status == "unknown" else "journal incomplete")
        else:
            state = "task open" if task in tasks else "task closed" if task in sent else "state unknown: task never dispatched"
        rows.append("- %s (%s) -- %s" % (clip(b.get("worktree", "?")), clip(branch), state))
    lead = "worktrees: %d linked" % len(rows)
    more = ["- and %d more" % (len(rows) - ROWS_MAX)] if len(rows) > ROWS_MAX else []
    return "\n".join([lead] + rows[:ROWS_MAX] + more), lead + " [cut: rows]"


def checklist(root):
    """The rows come from snapshot.carriers(), the one reader (t-2010 B2-4): one wording for absent and malformed."""
    sys.path.insert(0, os.path.join(HERE, "..", "tools"))
    import snapshot  # noqa: E402 -- lazily, like journal in compose
    rows, error = snapshot.carriers(root)
    return "carriers checklist: " + error if error else "\n".join(["carriers checklist:"] + ["- " + r for r in rows])


def previous(entries, found):
    """Block (4): the last parsed journal line decides; a session_end last means the session was closed."""
    parsed = [e for e in entries if e[4]]
    if not found:
        return "previous session: unknown -- no journal"
    if parsed and parsed[-1][4].get("event") == "session_end":
        return "previous session: closed %s" % clip(parsed[-1][0])
    return "previous session: no session_end after %s -- read the snapshot" % (clip(parsed[-1][0]) if parsed else "(no journal line)")


def render(p, cut):
    """p: the parts dict; cut = how many cuttable pieces go, in order: the open list, the checklist, the process and
    worktree rows. Stable lines first, volatile last (the module docstring says why)."""
    check = ("[cut: checklist]" if cut >= 2 else p["check"]) if p["check"] else ""
    facts = "now: %s | last: %s | snapshot: %s | open: %s" % (p["now"], p["last"], p["snap"],
                                                             "[cut: open list]" if cut >= 1 else p["open"])
    old, wt = (p["old"][1], p["wt"][1]) if cut >= 3 else (p["old"][0], p["wt"][0])
    return "\n".join(x for x in (p["boot"], p["field"], p["hooks"], check, facts, p["git"], old, wt, p["prev"]) if x)


def enc(text):
    """The one encoder: UTF-8 with replacement, so a lone surrogate costs a `?`, never the whole start text (t-2106 F1)."""
    return text.encode("utf-8", "replace")


def emitted(text):
    """The bytes that leave the hook: the text and the one `\\n` emit() adds (t-2010 B2-5)."""
    return len(enc(text + "\n"))


def fit(p):
    """The whole text, then without the open list, then without the checklist too. A valid UTF-8 BOOT is never cut;
    a non-UTF-8 one (p["bad"]) is cut last, to the cap, with a marker line (t-2010 B2-6)."""
    if p.get("bad") is not None:
        p = dict(p, boot=bad_boot(p["bad"], CAP))
    for cut in range(4):
        text = render(p, cut)
        if emitted(text) <= CAP:
            return text
    if p.get("bad") is None:
        return text
    n = CAP
    while True:
        text = render(dict(p, boot=bad_boot(p["bad"], n)), 3)
        if emitted(text) <= CAP or n <= 0:
            return text
        n -= max(1, emitted(text) - CAP)


def git_out(root, *args):
    """(stdout, None) of one git command in root, or (None, why): absent, failing, slower than GIT_WAIT_S or past the start
    budget. Never a fetch; read as UTF-8 with replacement (FH-2043)."""
    if spent():
        return None, "not collected: start budget"
    try:
        r = subprocess.run(["git", *args], cwd=root, capture_output=True, encoding="utf-8", errors="replace",
                           timeout=GIT_WAIT_S)
    except FileNotFoundError:
        return None, "git not found"
    except subprocess.TimeoutExpired:
        return None, "git slower than %d s" % GIT_WAIT_S
    except OSError as exc:
        return None, "git failed: %s" % clip(exc)
    if r.returncode:
        return None, "git exit %d" % r.returncode
    return r.stdout, None


def main_sync(root):
    """Plan S10: how far the local `main` is from `origin/main` (refs are shared by worktrees), from the refs as they are --
    no fetch. A missing ref or a failing git is said as unknown, never an error (the hook exits 0 anyway)."""
    for ref in ("main", "origin/main"):
        got, why = git_out(root, "rev-parse", "--verify", "--quiet", ref + "^{commit}")
        if got is None and why != "git exit 1":
            return "main: ahead/behind unknown (%s)" % why
        if got is None:
            return "main: ahead/behind unknown (%s missing)" % ref
    got, why = git_out(root, "rev-list", "--left-right", "--count", "main...origin/main")
    nums = (got or "").split()
    if len(nums) != 2 or not all(n.isdigit() for n in nums):
        return "main: ahead/behind unknown (%s)" % (why or "unreadable git output")
    return "main: ahead %s, behind %s of origin/main (no fetch)" % tuple(nums)


def compose(root, source, eval_arm):
    sys.path.insert(0, os.path.join(HERE, "..", "tools"))
    import journal  # noqa: E402 -- lazily: a broken journal.py is a fallback line, not a crash at import
    loaded = journal.load(root)
    status, tasks, bad = journal.open_tasks(root, loaded)
    boot, present, badtext = boot_block(root, eval_arm, source in BOOT_SOURCES)
    rules = ", forge/COORDINATOR.md (Lead, Architect)"  # plan S6: workers get no SessionStart; the Lead's rules file is named here
    field = "re-read: forge/BOOT.md" + rules if present else "" if eval_arm else "re-read: forge/BOOT.md (not written yet, B1)" + rules
    now, now_s, wt = datetime.datetime.now().astimezone(), time.time(), worktree_blocks(root)
    return fit({"boot": boot, "bad": badtext, "field": field, "hooks": hooks_text(root),
                "check": checklist(root) if source == "compact" else "",
                "now": now_text(now), "last": last_text(loaded[0], loaded[2]), "snap": newest_snapshot(root, now),
                "open": open_text(status, tasks, bad, journal.pending(loaded[0])), "git": main_sync(root), "old": old_text(root, now_s, wt),
                "wt": worktrees_text(wt, loaded[0], status, tasks),
                "prev": previous(loaded[0], loaded[2]) if source == "startup" else ""})


def emit(text):
    """Bytes with `\\n` to stdout: Windows' text layer would turn each `\\n` into `\\r\\n` and break the cap count."""
    sys.stdout.flush()
    data = enc(text + "\n")
    try:
        sys.stdout.buffer.write(data)
        sys.stdout.buffer.flush()
    except AttributeError:
        print(text)


def body(value, note, root):
    source = value.get("source") if value else None
    if source not in ("startup", "resume", "clear", "compact"):
        source = "startup"
    try:
        emit(compose(root, source, bool(os.environ.get("FORGE_EVAL_ARM"))))
    except Exception as exc:  # noqa: BLE001 -- the hook never blocks or delays work (K1)
        print("reminder failed: %s; read forge/BOOT.md by hand" % clip(exc))
    return 0


def run(argv):
    global T0
    T0 = time.monotonic()  # t-2106 F3: before the stdin read, so the card's 40 s bound holds from the hook's start
    root = os.path.dirname(os.path.dirname(HERE))
    if argv[:1] == ["--root"] and len(argv) == 2:
        root = argv[1]
    return HIO.guard(lambda v, n: body(v, n, root), "pass", "json")


if __name__ == "__main__":
    sys.exit(run(sys.argv[1:]))
