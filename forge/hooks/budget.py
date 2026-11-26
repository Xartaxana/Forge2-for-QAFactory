# card: B5
"""PreToolUse hook (card B5, amended by A30, B18): context size and wall time caps per forge worker launch.

budget.py [--root D]   the tool call JSON arrives on the input. The worker = the input's agent_id; its role and handoff path
are the `role:` and `handoff:` lines of the first user message of its own transcript
(<transcript_path minus .jsonl>/subagents/agent-<id>.jsonl); the rows are forge/caps.json. State: logs/budget/<key>.json.
TOKENS = input + cache creation + cache read of the NEWEST transcript line that holds usage (B18: a newest line without
usage leaves the last measured value; the scan is incremental by byte offset). SPEND = the sum of input + output + cache
creation + cache read over every usage line, printed and journaled beside the use (A30), never a cap. A value AT a cap acts.
Warn: once per measure, as additionalContext on stdout, journal `cap_warning`. Cut (a stop row reached, sticky: a
compaction lowers context, not wall): journal `cut` once; exit 2 on every call except SubagentHandback, a Write/Edit of
exactly the dispatch's `handoff:` path and ONE plain git command. `main` is warned at tokens_warn and every further 50000,
never cut. Journal notes start `role:<role>` (card B9 reads the role there).
Edges, named: the wall cap acts only at a call boundary. No agent_id -> `main`. An agent_id with no readable `role:` or an
unknown one -> the strictest worker row, said once. An unreadable or absent transcript -> `tokens unmeasured` once, the wall
cap still applies; a readable one with no usage line yet is silent (nothing to say, nothing to cut). caps.json absent or
malformed -> `caps missing` on every call, no cut. The hook's own error -> the call passes and `hook_failed` is journaled;
a call with no session id journals nothing (stderr only).
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
FIELDS = ("tokens_warn", "tokens_stop", "wall_warn_s", "wall_stop_s")


def load_rows(root):
    """The rows of forge/caps.json by role, or None when the file is absent or malformed."""
    try:
        with open(os.path.join(root, "forge", "caps.json"), encoding="utf-8") as fh:
            return {r["role"]: r for r in json.load(fh)}
    except (OSError, ValueError, KeyError, TypeError):
        return None


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


def line_use(line):
    """(context, spend) of one transcript line, or None when it holds no usage."""
    try:
        u = (json.loads(line).get("message") or {}).get("usage") if '"usage"' in line else None
        g = [u.get(k) or 0 for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")]
    except (ValueError, AttributeError, TypeError):
        return None
    return (sum(g[:3]), sum(g)) if all(isinstance(x, int) for x in g) else None


def scan(path, st):
    """Advance st (offset, ctx, spend) over the complete new lines. False when the file cannot be read."""
    try:
        with open(path, "rb") as fh:
            if st["offset"] > os.fstat(fh.fileno()).st_size:
                st.update(offset=0, ctx=None, spend=0)
            fh.seek(st["offset"])
            data = fh.read()
    except OSError:
        return False
    cut = data.rfind(b"\n") + 1
    for line in data[:cut].decode("utf-8", "replace").split("\n"):
        use = line_use(line)
        if use:
            st["ctx"], st["spend"] = use[0], st["spend"] + use[1]
    st["offset"] += cut
    return True


def state_of(path):
    fresh = {"t0": None, "offset": 0, "ctx": None, "spend": 0, "role": None, "handoff": None, "task": None, "said": []}
    try:
        with open(path, encoding="utf-8") as fh:
            return {**fresh, **json.load(fh)}
    except (OSError, ValueError, TypeError):
        return fresh


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


def judge(st, row, now, is_main):
    """The cap events of this call: [(kind, measure, use, cap)] in kind warn / cut; marks st['said'] so each fires once."""
    out = []
    wall = int(now - st["t0"])
    for measure, use in (("tokens", st["ctx"]), ("wall", wall)):
        warn, stop = row.get(measure + "_warn" if measure == "tokens" else "wall_warn_s"), row.get(
            measure + "_stop" if measure == "tokens" else "wall_stop_s")
        if use is None:
            continue
        if stop is not None and use >= stop:
            out.append(("cut", measure, use, stop))
        elif is_main and warn is not None and use >= warn:
            level = (use - warn) // STEP + 1
            if level > st.get("level", 0):
                st["level"] = level
                out.append(("warn", measure, use, warn))
        elif warn is not None and use >= warn and measure not in st["said"]:
            st["said"].append(measure)
            out.append(("warn", measure, use, warn))
    return out


def tell(root, session, role, st, events):
    """The lines for the agent, each journaled as cap_warning or cut; returns (warn lines, cut lines)."""
    warns, cuts = [], []
    for kind, measure, use, cap in events:
        unit = " s" if measure == "wall" else ""
        note = "role:%s %s %d of %d%s spend %d" % (role, measure, use, cap, unit, st["spend"])
        if kind == "cut":
            if "cut" in st["said"]:
                cuts.append(note)
                continue
            st["said"].append("cut")
            cuts.append(note)
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


def first_call(st, worker, path):
    """The sidecar of a worker's first call: t0, and the role, handoff and task lines of its dispatch."""
    st["t0"] = time.time()
    text = (first_user_text(path) if worker and path else None) or ""
    got = [re.search(r"(?m)^%s:\s*(.+?)\s*$" % n, text) for n in ("role", "handoff", "task")]
    got = [m.group(1).strip("`") if m else None for m in got]
    st["role"] = got[0].split()[0] if got[0] else None
    st["handoff"], st["task"] = got[1], got[2].split()[0] if got[2] else None


def pick_row(st, rows, worker, info):
    """(role, row): main, the worker's row, or the strictest worker row said once for an absent or unknown role."""
    if not worker:
        return "main", rows["main"]
    role = st["role"] if st["role"] in rows and st["role"] != "main" else "unknown"
    if role == "unknown":
        once(st, "role", "role: absent or unknown in the dispatch; the strictest worker row applies", info)
    return role, rows.get(role) or strictest(rows)


def verdict(payload, st, role, cuts):
    """The cut lines still standing after the allowed moves: a cut worker's three moves pass."""
    if "cut" not in st["said"]:
        return cuts
    if allowed(payload, st["handoff"]):
        return []
    return cuts or ["cut earlier; role:%s spend %d" % (role, st["spend"])]


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
    first = st["t0"] is None
    if first:
        first_call(st, worker, path)
    role, row = pick_row(st, rows, worker, info)
    if worker and first:
        info.append("caps: tokens %s/%s, wall %s/%s s -- at the cap: hand back done and not done" % tuple(row[f] for f in FIELDS))
    if not (path and scan(path, st)):
        once(st, "unmeasured", "tokens unmeasured: the transcript is absent or unreadable; the wall cap still applies", info)
    warns, cuts = tell(root, payload.get("session_id"), role, st, judge(st, row, time.time(), not worker))
    cuts = verdict(payload, st, role, cuts)
    save(sp, st)
    if cuts:
        return 2, CUT_TEXT % cuts[0], []
    return 0, "", info + warns


def save(sp, st):
    try:
        os.makedirs(os.path.dirname(sp), exist_ok=True)
        with open(sp, "w", encoding="utf-8") as fh:
            json.dump(st, fh)
    except OSError as exc:
        print("budget: state not written: %s" % exc, file=sys.stderr)


def body(payload, note, root):
    if payload is None:
        print("budget not checked: %s" % note, file=sys.stderr)
        return 0
    try:
        code, err, info = evaluate(payload, root)
    except Exception as exc:  # noqa: BLE001 -- the hook never refuses on its own error
        print("budget not checked: own error: %r" % exc, file=sys.stderr)
        HIO.journal(root, "hook_failed", "budget", payload.get("session_id"), "budget: %r" % exc)
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
