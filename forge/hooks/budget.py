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
caps.json absent or malformed (a field neither null nor a non-negative integer) -> `caps missing` on every call, no cut. A
sidecar that exists but cannot be read is NOT a first call: nothing is judged or written, `budget state unreadable` on every
call (the clock and a sticky cut live there; the save is atomic so a parallel call never sees a torn file). The hook's own
error -> the call passes and `hook_failed` is journaled; a call with no session id journals nothing (stderr only).
"""
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


def state_of(path):
    """The sidecar state; None when the file EXISTS and cannot be read (t-2027 F4: never read as a first call). The read is
    tried three times: a writer's os.replace may hold the file for a moment on Windows."""
    fresh = {"t0": None, "offset": 0, "ctx": None, "spend": 0, "last_id": None, "role": None, "handoff": None, "task": None,
             "said": []}
    for n in range(3):
        if not os.path.exists(path):
            return fresh
        try:
            with open(path, encoding="utf-8") as fh:
                got = json.load(fh)
            if isinstance(got, dict) and isinstance(got.get("t0"), (int, float)):
                return {**fresh, **got}
        except (OSError, ValueError):
            pass
        time.sleep(0.02 * n)
    return None


def allowed(payload, handoff):
    """The three moves that pass at a cut."""
    tool, ti = payload.get("tool_name"), payload.get("tool_input")
    ti = ti if isinstance(ti, dict) else {}
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
            cuts.append(note)
            if "cut" in st["said"]:
                continue
            st["said"].append("cut")
        else:
            warns.append("%s; write what is done, hand back the rest" % note)
        HIO.journal(root, "cap_warning" if kind == "warn" else "cut", "budget", session, note, st["task"] or "unknown")
    return warns, cuts


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


def pick_row(st, rows, worker, info):
    """(role, row): main, the worker's row, or the strictest worker row said once for an absent or unknown role."""
    if not worker:
        return "main", rows["main"]
    role = st["role"] if st["role"] in rows and st["role"] != "main" else "unknown"
    if role == "unknown":
        once(st, "role", "role unknown -- strictest row", info)
    return role, rows.get(role) or strictest(rows)


def verdict(payload, st, role, cuts):
    """The cut lines still standing after the allowed moves: a cut worker's three moves pass."""
    if "cut" not in st["said"]:
        return cuts
    if allowed(payload, st["handoff"]):
        return []
    return cuts or ["cut earlier; role:%s spend %s" % (role, spend_text(st))]


def caps_text(row):
    return "caps: tokens %s/%s, wall %s/%s s -- at the cap: hand back done and not done" % tuple(
        "none" if row[f] is None else row[f] for f in FIELDS)


MISS = "caps: missing -- forge/caps.json (B5)"


def caps_line(root, role):
    """The ONE caps line of a dispatch header (dispatch.py imports it; t-2027 F10): the role's row, the strictest worker row
    with the note `role unknown -- strictest row` for an absent or unknown role, MISS when caps.json is absent or malformed."""
    rows = load_rows(root)
    if rows is None:
        return MISS
    known = role in rows and role != "main"
    return caps_text(rows[role] if known else strictest(rows)) + ("" if known else "; role unknown -- strictest row")


def evaluate(payload, root):
    """(exit code, stderr text, additionalContext lines)."""
    info = []
    rows = load_rows(root)
    if rows is None or "main" not in rows:
        return 0, "", ["caps missing: forge/caps.json is absent or malformed (card B5); no cap is judged"]
    worker, key, path = keys(payload)
    if not isinstance(key, str) or not SAFE.fullmatch(key):
        return 0, "", ["budget not checked: no safe worker or session id"]
    sp = os.path.join(root, "logs", "budget", key + ".json")
    st = state_of(sp)
    if st is None:  # the clock and a sticky cut live there: nothing is judged, nothing is written, the file stays as found
        return 0, "", ["budget state unreadable: %s; no cap is judged on this call" % sp]
    first = st["t0"] is None
    if first:
        st["t0"] = time.time()
    if worker and (first or st["role"] is None or st["handoff"] is None):
        read_dispatch(st, path)
    role, row = pick_row(st, rows, worker, info)
    if worker and first:
        info.append(caps_text(row))
    if not (path and scan(path, st)):
        once(st, "unmeasured", "tokens unmeasured: the transcript is absent or unreadable; the wall cap still applies", info)
    elif st["ctx"] is None and not first:
        once(st, "nousage", "tokens unmeasured: the transcript holds no usage line; the wall cap still applies", info)
    warns, cuts = tell(root, payload.get("session_id"), role, st, judge(st, row, time.time(), not worker))
    cuts = verdict(payload, st, role, cuts)
    save(sp, st)
    if cuts:
        return 2, "\n".join([CUT_TEXT % cuts[0]] + info), []
    return 0, "", info + warns


def save(sp, st):
    """Atomic: a temporary file, then os.replace (t-2027 F4: a parallel call never reads a half-written sidecar)."""
    tmp = "%s.%d.tmp" % (sp, os.getpid())
    try:
        os.makedirs(os.path.dirname(sp), exist_ok=True)
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(st, fh)
        os.replace(tmp, sp)
    except OSError as exc:
        print("budget: state not written: %s" % exc, file=sys.stderr)


def failed_role(payload, root):
    """The role for a hook_failed note (t-2027 F3): main, the worker's recorded role, else unknown. Never raises."""
    try:
        aid = payload.get("agent_id")
        if not (isinstance(aid, str) and aid):
            return "main"
        return (state_of(os.path.join(root, "logs", "budget", aid + ".json")) or {}).get("role") or "unknown"
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
