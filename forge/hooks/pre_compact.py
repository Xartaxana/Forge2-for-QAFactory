# card: C1-5
# hook: PreCompact
"""PreCompact hook (cards C1-5, F18, B7): writes a snapshot before the compaction. It writes only and NEVER refuses.

pre_compact.py [--root D] [--timeout-s N]   any input, an empty one included; D defaults to this repository, N to 45.
A snapshot.py that is absent, exits non-zero or outlives N seconds (it is killed), or an error of this hook -> one
`hook_failed` journal line `pre_compact: <why>` under the input's session (no session id: one stderr line) and exit 0.
Cuts: snapshot.py's output in <why> is cut at 150 characters, <why> at 250 (the journal note stays under its 300).
"""
import argparse
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from hio import io as HIO  # noqa: E402


def snapshot(root, timeout_s):
    """Return the failure text, or None when snapshot.py completed."""
    sp = os.path.join(root, "forge", "tools", "snapshot.py")
    if not os.path.isfile(sp):
        return "%s absent" % sp
    try:
        r = subprocess.run([sys.executable, "-B", sp, "--root", root], capture_output=True, env=HIO.genv(),
                           timeout=timeout_s)
    except subprocess.TimeoutExpired:
        return "snapshot.py killed after %s s" % timeout_s
    except (OSError, subprocess.SubprocessError) as exc:
        return "snapshot.py not started: %s" % exc
    if r.returncode:
        return "snapshot.py exit %d: %s" % (r.returncode, (r.stdout + r.stderr).decode("utf-8", "replace").strip()[:150])
    print(r.stdout.decode("utf-8", "replace").strip())
    return None


def body(payload, note, root, timeout_s):
    sid = payload.get("session_id") if payload else None
    try:
        why = snapshot(root, timeout_s)
    except Exception as exc:  # noqa: BLE001 -- the hook never refuses work
        why = "own error: %r" % exc
    if why:
        HIO.journal(root, "hook_failed", "pre_compact", sid, "pre_compact: " + why[:250])
    return 0


def run(v, n, argv):
    """The guarded body: a bad argument exits 0 with one visible line (the hook never refuses, t-1982)."""
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=os.path.dirname(os.path.dirname(HERE)))
    ap.add_argument("--timeout-s", type=float, default=45)
    try:
        a = ap.parse_args(argv)
    except SystemExit as exc:
        if exc.code:
            print("pre_compact not run: bad arguments (usage: --root D --timeout-s N)", file=sys.stderr)
        return 0
    return body(v, n, a.root, a.timeout_s)


if __name__ == "__main__":
    sys.exit(HIO.guard(lambda v, n: run(v, n, sys.argv[1:]), "pass", "json"))
