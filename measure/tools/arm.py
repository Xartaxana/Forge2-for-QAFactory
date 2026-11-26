# card: S11-1 (amends C0-4: the thin node of `launch --task`, the run row, the fingerprint with rules_bundle)
"""The one arm launcher (C0-4); built now as the thin node role-seeded sets need (S11-1, draft t-2037 F4 (a)).

arm.py launch --task <folder> --spec <launch.json> --out <dir> [--dry-run]
  Runs the spec's harness command once, cwd = <folder>, stdin empty, and prints ONE run row (JSON) on stdout; --dry-run
  runs only the version command and prints the row with its fingerprint, no harness session (seeded.py's reuse check).
  The spec (written by seeded.py from measure/seeded/arms.yaml `launch`): command, version_command, text_key, models_key,
  model, role, run, arm, and the fingerprint parts tree, task, rules_bundle. Placeholders in a command: {model}, {role},
  {task} (the folder's task.md text), {role_file} (the folder's role file, mechanism B).
arm.py compare <run.json> <run.json> [--allow FIELD]...   exit 0 comparable, 1 refused naming the differing field
Run row: run, arm, mode (comparison), fingerprint, start, end, wall_s, tokens (per model), status (`measured |
unmeasured: <why>`). A key matching cost|usd|price is dropped before anything is written (C0-4 K2). Raw stdout ->
<out>/raw.txt, the agent's text -> <out>/out.txt, the row -> <out>/run.json (all under copies_root).
Exit 0 a row printed (measured or not), 2 refused: spec or folder absent or malformed (the caller records `unmeasured`).
"""
import argparse
import datetime
import hashlib
import json
import os
import re
import subprocess
import sys
import time

MODE = "comparison"
SPEC_FIELDS = ("command", "version_command", "text_key", "models_key", "model", "role", "run", "arm", "tree", "task",
               "rules_bundle")
MONEY = re.compile(r"cost|usd|price", re.I)
ROLE_FILE = ".claude/agents/%s.md"


class Refuse(Exception):
    """The spec cannot be launched: exit 2, no row."""


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def drop_money(value):
    """C0-4 K2: a key matching cost|usd|price never reaches a written row, at any depth."""
    if isinstance(value, dict):
        return {k: drop_money(v) for k, v in value.items() if not MONEY.search(str(k))}
    return value


def load_json(path, what):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError) as exc:
        raise Refuse("%s %s: unreadable (%s)" % (what, path, type(exc).__name__))


def read_spec(path):
    spec = load_json(path, "spec")
    if not isinstance(spec, dict):
        raise Refuse("spec %s: must be one JSON object" % path)
    missing = [f for f in SPEC_FIELDS if f not in spec]
    if missing:
        raise Refuse("spec %s: no %s" % (path, missing[0]))
    return spec


def task_text(folder):
    try:
        with open(os.path.join(folder, "task.md"), encoding="utf-8") as fh:
            return fh.read()
    except (OSError, ValueError):
        return ""


def fill(argv, spec, folder):
    """The placeholders of a command row; {task} carries task.md whole (the E0 row runs with no tools, so the prompt is
    the task; Windows refuses a command line over ~32 KB, which run_cmd reports as a harness that cannot start)."""
    values = {"{model}": spec["model"], "{role}": spec["role"], "{task}": task_text(folder),
              "{role_file}": os.path.join(folder, ROLE_FILE % spec["role"])}
    return [re.sub(r"\{model\}|\{role\}|\{task\}|\{role_file\}", lambda m: values[m.group(0)], a) for a in argv]


def run_cmd(argv, cwd):
    """(exit code, stdout text), or (None, why) when the process cannot start."""
    try:
        done = subprocess.run(argv, cwd=cwd, capture_output=True, stdin=subprocess.DEVNULL)
    except OSError as exc:
        return None, "cannot start (%s)" % (exc.strerror or type(exc).__name__)
    return done.returncode, done.stdout.decode("utf-8", "replace")


def harness_version(spec, cwd):
    """The version line; "" when the command fails (an unknown harness never fingerprints as equal to another)."""
    code, out = run_cmd(fill(spec["version_command"], spec, cwd), cwd)
    return out.strip().splitlines()[0] if code == 0 and out.strip() else ""


def fingerprint(spec, harness):
    """C0-4's fingerprint as named fields, so compare names the one that differs; S11-1 adds rules_bundle (I1)."""
    launch = sha(json.dumps([spec["command"], spec["text_key"], spec["models_key"]], sort_keys=True).encode("utf-8"))
    return {"mode": MODE, "model": spec["model"], "harness": harness, "launch": launch, "tree": spec["tree"],
            "task": spec["task"], "rules_bundle": spec["rules_bundle"]}


def compare(a, b, allow=()):
    """None when the two fingerprints are equal in every field outside allow, else the first differing field (sorted)."""
    for field in sorted(set(a) | set(b)):
        if field not in allow and a.get(field) != b.get(field):
            return field
    return None


def doc_of(out):
    try:
        doc = json.loads(out)
    except ValueError:
        return None
    return doc if isinstance(doc, dict) else None


def model_status(spec, models):
    """S11-1 edge: the model the harness reports must be the row's one id, else `unmeasured: model` (none reported too)."""
    reported = sorted(models) if isinstance(models, dict) else []
    if reported != [spec["model"]]:
        return "unmeasured: model (row %s, reported %s)" % (spec["model"], ", ".join(reported) or "none")
    return "measured"


def from_json(spec, out):
    doc = doc_of(out)
    text = None if doc is None else doc.get(spec["text_key"])
    if not isinstance(text, str):
        return "unmeasured: no `%s` text in the output" % spec["text_key"], "", {}
    models = doc.get(spec["models_key"])
    return model_status(spec, models), text, drop_money(models if isinstance(models, dict) else {})


def outcome(spec, code, out):
    """(status, agent text, tokens). Every launch failure is `unmeasured: <why>`: an unmeasured run never scores."""
    if code is None:
        return "unmeasured: harness %s" % out, "", {}
    if code != 0:
        return "unmeasured: harness exit %d" % code, "", {}
    if not out.strip():
        return "unmeasured: no output", "", {}
    return from_json(spec, out)


def write(out_dir, name, text):
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, name), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def session(spec, cwd, out_dir):
    start, t0 = now(), time.monotonic()
    code, out = run_cmd(fill(spec["command"], spec, cwd), cwd)
    wall = round(time.monotonic() - t0, 3)
    status, text, tokens = outcome(spec, code, out)
    write(out_dir, "raw.txt", out)
    write(out_dir, "out.txt", text)
    return {"start": start, "end": now(), "wall_s": wall, "tokens": tokens, "status": status}


def emit(row, out_dir=None):
    if out_dir:
        write(out_dir, "run.json", json.dumps(row, indent=1) + "\n")
    print(json.dumps(row))
    return 0


def launch(a):
    spec = read_spec(a.spec)
    if not os.path.isdir(a.task):
        raise Refuse("task folder %s: absent" % a.task)
    harness = harness_version(spec, a.task)
    row = {"run": spec["run"], "arm": spec["arm"], "mode": MODE, "fingerprint": fingerprint(spec, harness)}
    if a.dry_run:
        return emit(row)
    row.update(session(spec, a.task, a.out) if harness else {"status": "unmeasured: harness version unknown"})
    return emit(row, a.out)


def fingerprint_of(path):
    row = load_json(path, "run row")
    found = row.get("fingerprint") if isinstance(row, dict) else None
    if not isinstance(found, dict):
        raise Refuse("run row %s: no fingerprint" % path)
    return found


def compare_cli(a):
    prints = [fingerprint_of(p) for p in (a.a, a.b)]
    field = compare(prints[0], prints[1], tuple(a.allow))
    print("comparable" if field is None else "refused: fingerprints differ in %s" % field)
    return 0 if field is None else 1


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    la = sub.add_parser("launch")
    for flag in ("--task", "--spec", "--out"):
        la.add_argument(flag, required=True)
    la.add_argument("--dry-run", action="store_true")
    co = sub.add_parser("compare")
    co.add_argument("a")
    co.add_argument("b")
    co.add_argument("--allow", action="append", default=[])
    a = ap.parse_args(argv)
    try:
        return (launch if a.cmd == "launch" else compare_cli)(a)
    except Refuse as exc:
        print("refused: %s" % exc)
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
