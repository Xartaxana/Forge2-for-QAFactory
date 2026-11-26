# card: B5
"""PreToolUse hook (card B5, amended by A30, B18): context size and wall time caps per forge worker launch.

budget.py [--root D]   the tool call JSON arrives on the input. The worker = the input's agent_id; its role and handoff path
are the `role:` and `handoff:` lines of the first user message of its own transcript
(<transcript_path minus .jsonl>/subagents/agent-<id>.jsonl); the rows are forge/caps.json. State: logs/budget/<key>.json.
TOKENS = input + cache creation + cache read of the NEWEST transcript line that holds usage (B18: a newest line without
usage leaves the last measured value; the scan is incremental by byte offset). SPEND = input + output + cache creation + cache
read, a message's usage counted ONCE per message id (B12's rule; a real transcript repeats it per content block), `<synthetic>`
skipped; printed and journaled beside the use (A30), never a cap; `spend unmeasured` while no usage line was read. A value AT
a cap acts. Warn: once per measure, as additionalContext on stdout, journal `cap_warning`. Cut (a stop row reached, sticky: a
compaction lowers context, not wall): journal `cut` once; exit 2 on every call except SubagentHandback, a Write/Edit of
exactly the dispatch's `handoff:` path and ONE plain git command. `main` is warned at tokens_warn and every further 50000
(per measure), never cut, whatever its row says. Journal notes start `role:<role>` (card B9 reads the role there).
Edges, named: the wall cap acts only at a call boundary. No agent_id -> `main`. An agent_id with no readable `role:` or an
unknown one -> the strictest worker row, said once; role and handoff are re-read while None. An unreadable or absent transcript
-> `tokens unmeasured` once, the wall cap still applies; a readable one with no usage line says so once from the second call.
caps.json absent or malformed (a field neither null nor a non-negative integer), or holding no row for the caller (main: the
main row; a worker: its role's row; an unknown role: any worker row, for the strictest) -> `caps missing` on every call, no
cut; dispatch.py prints `caps: missing` by the same test (t-2032 N3). Fail closed on the state (t-2032 N1; the card's
invariant: no call after the cap passes except the three moves): a worker's sidecar that exists but cannot be read or is not
of the state's shape is a cut, `cut` journaled once with cause `budget state unreadable` and the sidecar rewritten as a cut
state; a worker Write/Edit whose path names logs/budget/ is refused, even as one of the three moves, and journaled as a cut
(tampering); a worker shell command naming logs/budget/ is refused for that call only (the Grep tool is the read door),
journaled once as `refuse`, never a cut (t-2036 T1, Lead ruling: a grep is no write). main is never cut: its unreadable sidecar is a line only, nothing written. The save is atomic:
a temporary file, os.replace retried up to 5 times with a short backoff, the temporary file removed on final failure.
Residuals, named: parallel calls read one snapshot, so one warn or cut may be journaled twice (readers dedup per agent); a
sidecar deleted by other means is a first call (the clock restarts); a command that builds the path (a variable, a glob) is
not seen as tampering; a read that loses all three tries to a concurrent save cuts the worker (fail closed). The hook's own
error -> the call passes and `hook_failed` is journaled; a call with no session id journals nothing (stderr only).
"""
import contextlib
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from hio import io as HIO  # noqa: E402

STEP = 50000
PLAIN_GIT = re.compile(r"^\s*git (add|commit|status|diff --stat)\b[^;&|<>`$\\()\r\n]*$")
SAFE = re.compile(r"[A-Za-z0-9_-]{1,128}")
CUT_TEXT = ("budget cut: %s -- hand back; the Lead relaunches fresh with the rest. Passing: SubagentHandback, a Write/Edit of "
            "the handoff path, one plain git command (add, commit, status, diff --stat)")
NAMES = {"tokens": ("tokens_warn", "tokens_stop"), "wall": ("wall_warn_s", "wall_stop_s")}
FIELDS = NAMES["tokens"] + NAMES["wall"]
USAGE = ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")
TRIES_READ, TRIES_SAVE = 3, 6  # a save: one try and up to 5 retries (t-2032 N4: os.replace loses to a reader on Windows)
TAMPER = re.compile(r"logs[\\/]+budget\b", re.I)
LOST, TAMPERED = "budget state unreadable", "budget state tampering: a Write/Edit names logs/budget/"
SHELL_TEXT = ("budget: refused for this call: logs/budget/ holds the hook's state, not a worker's to touch; to read it use the "
              "Grep tool. The next call is judged as usual")
NONE = type(None)
SHAPE = {"t0": (int, float), "offset": int, "ctx": (int, NONE), "spend": int, "last_id": (str, NONE), "role": (str, NONE),
         "handoff": (str, NONE), "task": (str, NONE), "said": list, "level_tokens": int, "level_wall": int}
MISSING = "caps missing: forge/caps.json is absent, malformed or holds no row for role:%s (card B5); no cap is judged"


def load_rows(root):
    """The rows of forge/caps.json by role, or None when the file is absent or malformed."""
    try:
        with open(os.path.join(root, "forge", "caps.json"), encoding="utf-8") as fh:
            rows = {r["role"]: r for r in json.load(fh)}
    except (OSError, ValueError, KeyError, TypeError):
        return None
    ok = all(f in r and (r[f] is None or (type(r[f]) is int and r[f] >= 0)) for r in rows.values() for f in FIELDS)
    return rows if ok else None


def strictest(rows):
    """The worker row with the lowest value of each field (a null field is no cap)."""
    ws = [r for k, r in rows.items() if k != "main"]
    return {f: min([r[f] for r in ws if r.get(f) is not None] or [None]) for f in FIELDS}


def first_user_text(path):
    """The text of the transcript's first user message, or None when the file has none or cannot be read."""
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                msg = json.loads(line) if '"user"' in line else None
                if isinstance(msg, dict) and msg.get("type") == "user":
                    c = (msg.get("message") or {}).get("content")
                    return c if isinstance(c, str) else "\n".join(b.get("text", "") for b in c if isinstance(b, dict))
    except (OSError, ValueError, TypeError, AttributeError):
        pass
    return None


def read_dispatch(st, path):
    """The role, handoff and task lines of the worker's dispatch; a value already read stays, an unreadable file changes nothing
    (t-2027 F12: re-read at later calls while role or handoff is still None)."""
    text = first_user_text(path) if path else None
    if text is None:
        return
    for name in ("role", "handoff", "task"):
        m = re.search(r"(?m)^%s:\s*(.+?)\s*$" % name, text)
        if m and st[name] is None:
            st[name] = m.group(1).strip("`") if name == "handoff" else m.group(1).split()[0].strip("`")


def line_use(line):
    """(message id or None, context, spend) of one transcript line, or None when it holds no usage or is synthetic."""
    try:
        m = json.loads(line).get("message") or {} if '"usage"' in line else {}
        g = [(m.get("usage") or {}).get(k) or 0 for k in USAGE]
    except (ValueError, AttributeError, TypeError):
        return None
    if not isinstance(m.get("usage"), dict) or m.get("model") == "<synthetic>" or not all(isinstance(x, int) for x in g):
        return None
    return m.get("id") if isinstance(m.get("id"), str) else None, sum(g[:3]), sum(g)


def scan(path, st):
    """Advance st (offset, ctx, spend) over the complete new lines. False when the file cannot be read. A message's usage is
    counted once (t-2027 F1, B12's rule): a real transcript repeats it on one line per content block, consecutively."""
    try:
        with open(path, "rb") as fh:
            if st["offset"] > os.fstat(fh.fileno()).st_size:
                st.update(offset=0, ctx=None, spend=0, last_id=None)
            fh.seek(st["offset"])
            data = fh.read()
    except OSError:
        return False
    cut = data.rfind(b"\n") + 1
    for line in data[:cut].decode("utf-8", "replace").split("\n"):
        use = line_use(line)
        if use:
            st["ctx"] = use[1]
            if use[0] is None or use[0] != st["last_id"]:
                st["spend"] += use[2]
            st["last_id"] = use[0]
    st["offset"] += cut
    return True


def spend_text(st):
    """The spend as printed and journaled: `unmeasured` while no usage line was read (an unknown spend is never zero)."""
    return "unmeasured" if st["ctx"] is None else "%d" % st["spend"]


def fresh():
    return {"t0": None, "offset": 0, "ctx": None, "spend": 0, "last_id": None, "role": None, "handoff": None, "task": None,
            "said": []}


def shaped(got):
    """The state when got has the state's shape (t0 a number, each field of its type, said a list of str), else None."""
    st = {**fresh(), **got} if isinstance(got, dict) else {"t0": None}
    ok = all(isinstance(st[k], t) for k, t in SHAPE.items() if k in st) and st["offset"] >= 0
    return st if ok and all(isinstance(x, str) for x in st["said"]) else None


def attempt(n, fn):
    """fn() tried up to n times on OSError, a short backoff before each retry and none after the last (t-2032 N4, Q7)."""
    for i in range(n):
        try:
            return fn()
        except OSError:
            if i == n - 1:
                raise
            time.sleep(0.005 * 2 ** (i + 1))


def state_of(path):
    """The sidecar state, fresh when the file is absent; None when it EXISTS and cannot be read or is not of the state's shape
    (t-2032 N1: the caller treats a worker as cut). Tried three times: a writer's os.replace holds the file for a moment on
    Windows; a parse error is not retried (the save is atomic, so it is no torn write)."""
    def read():
        if not os.path.exists(path):
            return fresh()
        with open(path, encoding="utf-8") as fh:
            return shaped(json.load(fh))
    try:
        return attempt(TRIES_READ, read)
    except (OSError, ValueError):
        return None


def call_of(payload):
    """(tool name, tool input as a dict) of the hook input."""
    ti = payload.get("tool_input")
    return payload.get("tool_name"), ti if isinstance(ti, dict) else {}


def tampers(payload):
    """`write` when a call's Write/Edit path names logs/budget/, `shell` when its shell command does, else None (t-2032 N1 (a):
    the state is the hook's alone; t-2036 T1: a shell command is refused for its call only, a write is a cut)."""
    tool, ti = call_of(payload)
    p, cmd = ti.get("file_path"), ti.get("command")
    if tool in ("Write", "Edit") and isinstance(p, str) and TAMPER.search(os.path.normpath(p)):
        return "write"
    return "shell" if tool in ("Bash", "PowerShell") and isinstance(cmd, str) and TAMPER.search(cmd) else None


def shell_door(root, session, role, st, payload, worker):
    """The refusal text of a worker's shell command naming logs/budget/, else None: refused for this call only, journaled once
    as `refuse`, never a cut (t-2036 T1, Lead ruling)."""
    if not worker or tampers(payload) != "shell":
        return None
    if "shell_state" not in st["said"]:
        st["said"].append("shell_state")
        HIO.journal(root, "refuse", "budget", session, "role:%s a shell command names logs/budget/; refused for this call" % role,
                    st["task"] or "unknown")
    return SHELL_TEXT


def allowed(payload, handoff):
    """The three moves that pass at a cut."""
    tool, ti = call_of(payload)
    if tool == "SubagentHandback":
        return True
    if tool in ("Write", "Edit"):
        p = ti.get("file_path")
        return bool(handoff) and isinstance(p, str) and norm(p, payload.get("cwd")) == norm(handoff, payload.get("cwd"))
    cmd = ti.get("command")
    return tool in ("Bash", "PowerShell") and isinstance(cmd, str) and bool(PLAIN_GIT.match(cmd))


def norm(p, cwd):
    return os.path.normcase(os.path.normpath(os.path.join(cwd if isinstance(cwd, str) else "", p.strip("`"))))


def new_warn(st, measure, use, warn, is_main):
    """True when this call owes a warn: a worker once per measure; main at the warn row and each further STEP, per measure."""
    if is_main:
        key = "level_" + measure
        old, st[key] = st.get(key, 0), max((use - warn) // STEP + 1, st.get(key, 0))
        return st[key] > old
    if measure in st["said"]:
        return False
    st["said"].append(measure)
    return True


def judge(st, row, now, is_main):
    """The cap events of this call: [(kind, measure, use, cap)] in kind warn / cut. main is never cut (the card, held by code)."""
    out = []
    for measure, use in (("tokens", st["ctx"]), ("wall", int(now - st["t0"]))):
        warn, stop = (row.get(f) for f in NAMES[measure])
        if use is None:
            continue
        if stop is not None and use >= stop and not is_main:
            out.append(("cut", measure, use, stop))
        elif warn is not None and use >= warn and new_warn(st, measure, use, warn, is_main):
            out.append(("warn", measure, use, warn))
    return out


def tell(root, session, role, st, events):
    """The lines for the agent, each journaled as cap_warning or cut; returns (warn lines, cut lines)."""
    warns, cuts = [], []
    for kind, measure, use, cap in events:
        unit = " s" if measure == "wall" else ""
        note = "role:%s %s %d of %d%s spend %s" % (role, measure, use, cap, unit, spend_text(st))
        if kind == "cut":
            cuts.append(cut_once(root, session, st, note))
        else:
            warns.append("%s; write what is done, hand back the rest" % note)
            HIO.journal(root, "cap_warning", "budget", session, note, st["task"] or "unknown")
    return warns, cuts


def cut_once(root, session, st, note):
    """A cut: sticky in the sidecar, journaled once; returns the note."""
    if "cut" not in st["said"]:
        st["said"].append("cut")
        HIO.journal(root, "cut", "budget", session, note, st["task"] or "unknown")
    return note


def once(st, key, text, lines):
    if key not in st["said"]:
        st["said"].append(key)
        lines.append(text)


def keys(payload):
    """(worker?, state key, transcript path or None); the key is None when no safe id exists."""
    sid, aid = payload.get("session_id"), payload.get("agent_id")
    worker = isinstance(aid, str) and bool(aid)
    key = aid if worker else "main-%s" % sid
    tp = payload.get("transcript_path")
    if not (isinstance(tp, str) and tp):
        return worker, key, None
    sub = os.path.join(tp[:-6] if tp.endswith(".jsonl") else tp, "subagents", "agent-%s.jsonl" % aid)
    return worker, key, (sub if worker else tp)


def map_role(role, rows):
    """A worker's role as notes print it: its dispatch role when caps.json holds that worker row, else unknown. The ONE mapping
    of cap notes, hook_failed notes and the dispatch caps line (t-2032 N2)."""
    return role if rows and role in rows and role != "main" else "unknown"


def row_of(rows, worker, role):
    """The row a caller's caps come from, None when it has none (t-2032 N3, the ONE usability test of the hook and dispatch.py):
    main its main row; a worker its role's row; an unknown role the strictest worker row, None with no worker row."""
    if rows is None:
        return None
    if not worker:
        return rows.get("main")
    if role != "unknown":
        return rows[role]
    return strictest(rows) if any(k != "main" for k in rows) else None


def pick_row(st, rows, worker, info):
    """(role, row or None): main, the worker's row, or the strictest worker row said once for an absent or unknown role."""
    if not worker:
        return "main", row_of(rows, False, "main")
    role = map_role(st["role"], rows)
    if role == "unknown":
        once(st, "role", "role unknown -- strictest row", info)
    return role, row_of(rows, True, role)


def verdict(payload, st, role, cuts):
    """The cut lines still standing after the allowed moves: a cut worker's three moves pass, never a tampering call."""
    if "cut" not in st["said"]:
        return cuts
    if allowed(payload, st["handoff"]) and not tampers(payload):
        return []
    return cuts or ["cut earlier; role:%s spend %s" % (role, spend_text(st))]


def caps_text(row):
    return "caps: tokens %s/%s, wall %s/%s s -- at the cap: hand back done and not done" % tuple(
        "none" if row[f] is None else row[f] for f in FIELDS)


MISS = "caps: missing -- forge/caps.json (B5)"


def caps_line(root, role):
    """The ONE caps line of a dispatch header (dispatch.py imports it; t-2027 F10): the role's row, the strictest worker row
    with the note `role unknown -- strictest row` for an absent or unknown role, MISS when the role has no usable row (row_of)."""
    rows = load_rows(root)
    role = map_role(role, rows)
    row = row_of(rows, True, role)
    if row is None:
        return MISS
    return caps_text(row) + ("; role unknown -- strictest row" if role == "unknown" else "")


def begin(st, worker, path):
    """Stamp t0 at the first call; read the dispatch while role or handoff is unknown (t-2027 F12). True at the first call."""
    first = st["t0"] is None
    if first:
        st["t0"] = time.time()
    if worker and (first or st["role"] is None or st["handoff"] is None):
        read_dispatch(st, path)
    return first


def measure(st, path, first, info):
    """Scan the transcript; an unmeasured context is said once (an unknown spend is never read as zero)."""
    if not (path and scan(path, st)):
        once(st, "unmeasured", "tokens unmeasured: the transcript is absent or unreadable; the wall cap still applies", info)
    elif st["ctx"] is None and not first:
        once(st, "nousage", "tokens unmeasured: the transcript holds no usage line; the wall cap still applies", info)


def cause_of(lost, worker, payload):
    """The cut a worker's state forces on this call, or None (t-2032 N1: a state that cannot be proved is a cut, not a pass)."""
    if lost:
        return LOST
    return TAMPERED if worker and tampers(payload) == "write" else None


def evaluate(payload, root):
    """(exit code, stderr text, additionalContext lines)."""
    rows = load_rows(root)
    worker, key, path = keys(payload)
    if not isinstance(key, str) or not SAFE.fullmatch(key):
        return 0, "", ["budget not checked: no safe worker or session id"]
    sp = os.path.join(root, "logs", "budget", key + ".json")
    st = state_of(sp)
    if st is None and not worker:  # main is never cut: nothing is judged, nothing is written
        return 0, "", ["%s: %s; main is never cut, no cap is judged on this call" % (LOST, sp)]
    lost, info, session = st is None, [], payload.get("session_id")
    st = st or fresh()
    first = begin(st, worker, path)
    role, row = pick_row(st, rows, worker, info)
    if row is None:
        return 0, "", [MISSING % role]
    if worker and first and not lost:
        info.append(caps_text(row))
    measure(st, path, first, info)
    warns, cuts = tell(root, session, role, st, [] if lost else judge(st, row, time.time(), not worker))
    cause = cause_of(lost, worker, payload)
    forced = [cut_once(root, session, st, "role:%s %s spend %s" % (role, cause, spend_text(st)))] if cause else []
    cuts = verdict(payload, st, role, forced + cuts)
    door = None if cuts else shell_door(root, session, role, st, payload, worker)
    save(sp, st)  # a lost state is rewritten here as a cut state, so the next call reads it
    if cuts:
        return 2, "\n".join([CUT_TEXT % cuts[0]] + info), []
    if door:
        return 2, "\n".join([door] + info), []
    return 0, "", info + warns


def save(sp, st):
    """Atomic: a temporary file, then os.replace retried (t-2032 N4); on final failure the temporary file is removed and the
    failure printed."""
    tmp = "%s.%d.tmp" % (sp, os.getpid())
    try:
        os.makedirs(os.path.dirname(sp), exist_ok=True)
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(st, fh)
        attempt(TRIES_SAVE, lambda: os.replace(tmp, sp))
    except OSError as exc:
        print("budget: state not written: %s" % exc, file=sys.stderr)
        with contextlib.suppress(OSError):
            os.remove(tmp)


def failed_role(payload, root):
    """The role for a hook_failed note (t-2027 F3): main, else the worker's recorded role mapped as cap notes map it (t-2032
    N2). Never raises."""
    try:
        aid = payload.get("agent_id")
        if not (isinstance(aid, str) and aid):
            return "main"
        st = state_of(os.path.join(root, "logs", "budget", aid + ".json")) or fresh()
        return map_role(st["role"], load_rows(root))
    except Exception:  # noqa: BLE001 -- a note about a failure must not fail
        return "unknown"


def body(payload, note, root):
    if payload is None:
        print("budget not checked: %s" % note, file=sys.stderr)
        return 0
    try:
        code, err, info = evaluate(payload, root)
    except Exception as exc:  # noqa: BLE001 -- the hook never refuses on its own error
        print("budget not checked: own error: %r" % exc, file=sys.stderr)
        HIO.journal(root, "hook_failed", "budget", payload.get("session_id"),
                    "role:%s budget: %r" % (failed_role(payload, root), exc))
        return 0
    if err:
        print(err, file=sys.stderr)
    if info:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "additionalContext": "\n".join(info)}}))
    return code


def run(v, n, argv):
    return HIO.run_root("budget", __doc__, os.path.dirname(os.path.dirname(HERE)), argv, lambda root: body(v, n, root))


if __name__ == "__main__":
    sys.exit(HIO.guard(lambda v, n: run(v, n, sys.argv[1:]), "pass", "json"))
