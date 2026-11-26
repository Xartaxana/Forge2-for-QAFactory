# card: C1-5
"""The ONE reader of a hook's input, the guard around a hook body and the ONE journal helper (cards C1-5, B9, B17).

The file name is B17's, but `_io` is also a CPython built-in module: `import _io` never finds this file, so every hook
loads it by path through hio.py. B17 adds write_output, run_steps and the policy table here.
"""
import json
import os
import subprocess
import sys
import threading


def genv(keep=()):
    """The environment of a subprocess: no GIT_* variable except the names in keep (an inherited GIT_DIR or GIT_INDEX_FILE
    would aim a fixture or ci.py at the wrong repository). Only secret_scan's reads of the repository git is committing keep
    GIT_INDEX_FILE, GIT_DIR, GIT_WORK_TREE: `git commit -a` and `git commit <path>` point the first at a temporary index
    (t-1983 F1)."""
    return {k: v for k, v in os.environ.items() if not k.startswith("GIT_") or k in keep}


def _pull(fd, deadline_s, limit):
    """Return (bytes or None, note): at most limit bytes are accepted, one more is refused."""
    buf, err = [], []

    def pump():
        n = 0
        try:
            while n <= limit:
                b = os.read(fd, 65536)
                if not b:
                    return
                buf.append(b)
                n += len(b)
        except OSError as exc:
            err.append(exc)

    t = threading.Thread(target=pump, daemon=True)
    t.start()
    t.join(deadline_s)
    if t.is_alive():
        return None, "no end of input within %s s" % deadline_s
    data = b"".join(buf)
    if err:
        return None, "unreadable input: %s" % err[0]
    return (None, "input over %d bytes" % limit) if len(data) > limit else (data, "")


def read_input(form, deadline_s=10, max_bytes=16777216, fd=None):
    """Return (value, note). Form json: an object, else None + why. Form lines: a list of str (None for a line that is not
    UTF-8), [] for an empty input, None + why when the input cannot be read. Form none: nothing is read."""
    if form == "none":
        return None, ""
    try:
        fd = sys.stdin.fileno() if fd is None else fd
        if os.isatty(fd):
            return None, "input is a terminal"
    except (ValueError, OSError, AttributeError) as exc:
        return None, "no input: %s" % exc
    data, note = _pull(fd, deadline_s, max_bytes)
    if data is None:
        return None, note
    if form == "lines":
        rows = data.split(b"\n")
        rows = rows[:-1] if rows[-1] == b"" else rows
        out = []
        for r in rows:
            try:
                out.append(r.decode("utf-8").rstrip("\r"))
            except UnicodeDecodeError:
                out.append(None)
        return out, ""
    if not data.strip():
        return None, "empty input"
    try:
        obj = json.loads(data.decode("utf-8"))
    except UnicodeDecodeError:
        return None, "input is not UTF-8"
    except ValueError:
        return None, "input is not JSON"
    return (obj, "") if isinstance(obj, dict) else (None, "input is not a JSON object")


def guard(body, policy, form):
    """Read the input, run body(value, note) -> exit code. A raise: policy "pass" gives one visible line and 0; a number
    is the exit code of a refusal (irreversible acts fail closed)."""
    name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
    for s in (sys.stdout, sys.stderr):
        s.reconfigure(encoding="utf-8", errors="replace")
    try:
        value, note = read_input(form)
        return body(value, note)
    except Exception as exc:  # noqa: BLE001 -- the whole point of the guard
        print("%s %s: own error: %r" % (name, "not checked" if policy == "pass" else "refused", exc), file=sys.stderr)
        return 0 if policy == "pass" else policy


def refuse_git(root, hook, text, door):
    """A git hook's refusal: the text on stderr and one `refuse` line in git-hooks.jsonl (no root known: no line)."""
    print("%s: refused: %s" % (hook, text), file=sys.stderr)
    if root:
        journal(root, "refuse", hook, "git-hooks", "%s: %s" % (hook, door))
    return 1


def journal(root, event, by, session, note, task=None):
    """Append one line through journal.py's CLI, the one writer. Never raises and never guesses a session (journal.py itself
    refuses an invalid id): a failure is one stderr line, cut at 200 characters of journal.py's answer, and the caller's
    verdict stays as it was. task: passed as --task when given (cap_warning and cut need one). Returns True when the line is written."""
    why = None
    jp = os.path.join(root, "forge", "tools", "journal.py")
    if not isinstance(session, str) or not session:
        why = "no session id"
    elif not os.path.isfile(jp):
        why = "%s absent" % jp
    else:
        try:
            r = subprocess.run([sys.executable, "-B", jp, "--root", root, "--event", event, "--by", by, "--session",
                                session, "--note=" + note] + (["--task", task] if task else []), capture_output=True,
                               env=genv(), timeout=30)
            if r.returncode:
                why = (r.stdout + r.stderr).decode("utf-8", "replace").strip()[:200] or "exit %d" % r.returncode
        except (OSError, subprocess.SubprocessError) as exc:
            why = str(exc)
    if why:
        print("journal not written: " + why, file=sys.stderr)
    return why is None


def run_root(name, doc, default_root, argv, with_root):
    """The guarded body of a hook that takes `--root D`: a bad argument exits 0 with the visible line (exit 2 would block EVERY
    tool call); else with_root(D) is the exit code. The ONE copy of this block (hooks budget, foreign_write)."""
    import argparse
    ap = argparse.ArgumentParser(description=doc)
    ap.add_argument("--root", default=default_root)
    try:
        a = ap.parse_args(argv)
    except SystemExit as exc:
        if exc.code:
            print("%s not checked: bad arguments (usage: --root D)" % name, file=sys.stderr)
        return 0
    return with_root(a.root)
