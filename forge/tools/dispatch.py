# card: C1-4
"""Print a dispatch's header lines checked, or check a header already written (cards C1-4, B5).

dispatch.py [--root D] new --role R --task T --given P... --owns P... --non-goals X --handoff X --edges X --dod CMD
                           --siblings X [--test X]      print the header lines, exit 0 only when check passes
dispatch.py [--root D] check <file | ->                 one line `missing: <name>` per absent line; else ok

Exit: 0 ok, 1 something missing or repeated or an owns path not absolute / outside the root, 2 unknown role, a newline
in a value or a file that cannot be read. Lines inside fences or after > are no header lines.
A called tool: it gates nothing. The caps line reads forge/caps.json (card B5), a JSON array of rows with role,
tokens_warn, tokens_stop, wall_warn_s, wall_stop_s; absent, malformed or without the role's row -> `caps: missing`.
"""
import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROLES = ("scout", "builder", "critic", "designer")
NAMES = ("task", "role", "caps", "given", "owns", "non-goals", "handoff", "edges", "DoD", "siblings", "test")
PATHS = ("given", "owns")
HEAD = re.compile(r"^(%s):(.*)$" % "|".join(re.escape(n) for n in NAMES))
TICKS = re.compile(r"`[^`\n]+`")
KEY = re.compile(r"^[A-Za-z0-9_-]+:(\s|$)")  # a drive path (C:/x) has a slash after its colon, so it is no key


def caps_line(root, role):
    miss = "caps: missing -- forge/caps.json (B5)"
    try:
        with open(os.path.join(root, "forge", "caps.json"), encoding="utf-8") as fh:
            row = next((r for r in json.load(fh) if r.get("role") == role), None)
        return ("caps: tokens %d/%d, wall %d/%d s -- at the cap: hand back done and not done"
                % (row["tokens_warn"], row["tokens_stop"], row["wall_warn_s"], row["wall_stop_s"])) if row else miss
    except (OSError, ValueError, AttributeError, KeyError, TypeError):
        return miss


def inside(root, path):
    if not os.path.isabs(path):
        return False
    try:
        r, q = os.path.normcase(os.path.abspath(root)), os.path.normcase(os.path.abspath(path))
        return os.path.commonpath([r, q]) == r
    except ValueError:
        return False


FENCE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")  # a fence marker, indented or not


def parse(text):
    """Return ({name: (inline value, [path lines])}, [repeated names]). Fenced and > quoted lines are no header lines
    (R11-f); the first of a repeated name stays; a key-shaped line ends a path block, any other line joins it."""
    out, rep, cur, fence = {}, [], None, None
    for ln in text.splitlines():
        f = FENCE.match(ln)
        if fence is None and f:
            fence = f.group(1)
            continue
        if fence is not None:
            # closed only by its own character, at least as long, nothing after it (review t-1947, N1); an unclosed
            # fence leaves the rest unread: a missing line is reported, never a false ok
            if f and f.group(1)[0] == fence[0] and len(f.group(1)) >= len(fence) and not f.group(2).strip():
                fence = None
            continue
        if ln.startswith(">"):
            continue
        m = HEAD.match(ln)
        if m:
            cur = m.group(1)
            if cur in out:
                rep.append(cur)
                cur = None
            else:
                out[cur] = (m.group(2).strip(), [])
        elif KEY.match(ln):
            cur = None
        elif cur in PATHS and ln.strip():
            out[cur][1].append(ln.strip())
    return out, rep


def problems(n, h, role, root):
    """The problem lines of header name n (empty when it is fine)."""
    if n not in h:
        return ["missing: " + n] if n != "test" or role == "builder" else []
    v, paths = h[n]
    if n not in PATHS:
        if not v or (n == "DoD" and not TICKS.search(v)):
            return ["missing: %s" % n + (" (no backticked command)" if n == "DoD" and v else "")]
        return []
    bad = []
    paths = ([v] if v else []) + paths
    if n == "owns" and role == "builder" and not paths:
        bad.append("missing: owns")
    paths = [p[1:-1] if len(p) > 1 and p[0] == p[-1] == "`" else p for p in paths]
    return bad + ["owns path not absolute or not inside the root: %s" % p for p in paths
                  if n == "owns" and not inside(root, p)]


def check(text, root):
    h, rep = parse(text)
    role = h.get("role", ("", []))[0]
    if role and role not in ROLES:
        print("unknown role %r; roles: %s" % (role, ", ".join(ROLES)))
        return 2
    bad = ["repeated: " + n for n in rep]
    for n in NAMES:
        bad += problems(n, h, role, root)
    print("\n".join(bad) if bad else "ok")
    return 1 if bad else 0


def new(a):
    if a.role not in ROLES:
        print("unknown role %r; roles: %s" % (a.role, ", ".join(ROLES)))
        return 2
    flags = {"task": a.task, "non-goals": a.non_goals, "handoff": a.handoff, "edges": a.edges, "dod": a.dod,
             "siblings": a.siblings, "test": a.test}
    for f, v in list(flags.items()) + [("given", " ".join(a.given)), ("owns", " ".join(a.owns))]:
        if v and re.search(r"[\r\n]", v):
            print("--%s holds a newline; a one-line value takes none" % f)
            return 2
    dod = a.dod
    if dod and not TICKS.search(dod):
        dod = "`%s`" % dod
    rows = ["task: %s" % (a.task or ""), "role: %s" % a.role, caps_line(a.root, a.role)]
    for n, paths in (("given", a.given), ("owns", a.owns)):
        rows += ["%s:" % n] + ["`%s`" % q if " " in q else q for q in paths]
    rows += ["non-goals: %s" % (a.non_goals or ""), "handoff: %s" % (a.handoff or ""), "edges: %s" % (a.edges or ""),
             "DoD: %s" % (dod or ""), "siblings: %s" % (a.siblings or "")]
    if a.test or a.role == "builder":
        rows.append("test: %s" % (a.test or ""))
    text = "\n".join(rows) + "\n"
    print(text, end="")
    return check(text, a.root)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=ROOT)
    sub = p.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("new")
    n.add_argument("--role", required=True)
    for f in ("task", "non-goals", "handoff", "edges", "dod", "siblings", "test"):
        n.add_argument("--" + f, dest=f.replace("-", "_"))
    for f in PATHS:
        n.add_argument("--" + f, nargs="*", default=[])
    c = sub.add_parser("check")
    c.add_argument("file")
    a = p.parse_args(argv)
    if a.cmd == "new":
        return new(a)
    try:
        text = sys.stdin.buffer.read() if a.file == "-" else open(a.file, "rb").read()
    except OSError:
        print("cannot read %s" % a.file)
        return 2
    return check(text.decode("utf-8", "replace"), a.root)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
