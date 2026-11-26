# card: S11-1 (amends C2-6: `run --set --arm` and `score` built now; launches only through arm.py, C0-4)
"""Role-seeded sets: does a reworded forge rule still make a worker act as the old text did (draft t-2037, card S11-1).

seeded.py run --set <role> [--arm <id>]... [--root D]   build each arm's tree, launch it through arm.py, judge, score rows
seeded.py score --set <role> [--date YYYYMMDD[-n]] [--root D]   per item LOSS | GAIN | NOISE | does-not-rank | held, the rank
Data: measure/seeded/arms.yaml (arm rows and the harness form), measure/seeded/forge/<role>/<task>/{task.md, input/,
key.yaml}. Both YAML files are written in JSON syntax and read with json (no PyYAML, as forge/owner-words.yaml).
Results: measure/runs/forge-roles/<role>/<yyyymmdd>[-n]/{runs.jsonl, scores.jsonl, lot.json, judges/}; raw logs in copies_root.
Exit 0 done, 2 refused naming file and row: every file is read and every source checked before the first launch.
Processes: git (the tree export), a key's `run` command, and arm.py for every harness session (I7, C2-6 K6: the draft's
Q1 puts the tree build here, so git is the one exception to K6's letter; no harness is ever called directly).
"""
import argparse
import datetime
import hashlib
import io
import json
import os
import random
import re
import shutil
import subprocess
import sys
import tarfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import arm  # noqa: E402  (compare and the run row's form live with the launcher)

ROOT = os.path.dirname(os.path.dirname(HERE))
ARM = os.path.join(HERE, "arm.py")
ARMS_REL = "measure/seeded/arms.yaml"
SETS_REL = "measure/seeded/forge"
RUNS_REL = "measure/runs/forge-roles"
# I2: never in an arm tree; host_paths settings and skills join them (F3). measure/runs/forge-roles holds result rows
# naming items and ledger rows: an arm with read tools would see them once the export is re-pinned (t-2062 F6).
ALWAYS = ("measure/seeded", "forge/specs", "measure/runs/forge-roles")
REFERENCE, CANDIDATE, CONTROL = "old", "new", "bare"  # draft Q5's three arms
RUNS = 3  # Q5: a disagreeing task runs both arms to a majority of 3
SET_RE = re.compile(r"[a-z0-9_-]+")
HEADER = ("schema", "note", "copies_root", "export", "host_paths", "launch", "arms")
HEADER_REQ = ("schema", "copies_root", "export", "host_paths", "launch", "arms")
HOST = ("instructions", "role", "settings", "skills")
LAUNCH = ("mechanism", "command", "judge_command", "version_command", "text_key", "models_key", "residual")
SOURCE = ("repo", "sha")
KINDS = ("tree_overlay",)
ROW = ("id", "kind", "source", "put", "remove", "closure", "model", "body")
ROW_TYPES = {"id": str, "kind": str, "source": dict, "put": dict, "remove": list, "closure": list, "model": str,
             "body": str}
KEY = ("canary", "items", "intact")
KEY_TYPES = {"canary": str, "items": list, "intact": list}
ITEM = ("id", "ledger_row", "old_text", "new_text", "judged_by", "catch", "command")
ITEM_REQ = ("id", "ledger_row", "old_text", "new_text", "judged_by", "catch")
ITEM_TYPES = {"id": str, "ledger_row": str, "catch": str, "command": list}
INTACT = ("id", "passage")
JUDGED_BY = ("critic", "run")
ITEM_CLASS = {("caught", "missed"): "LOSS", ("missed", "caught"): "GAIN", ("missed", "missed"): "NOISE"}
INTACT_CLASS = {("missed", "caught"): "LOSS", ("caught", "missed"): "GAIN"}  # caught = a blocker raised on the passage
FRONT = re.compile(rb"\A(---\r?\n.*?\r?\n---\r?\n)(.*)\Z", re.S)
MODEL_LINE = re.compile(rb"^model:[^\r\n]*", re.M)
MARK = re.compile(r"^[\s>*`-]*([A-Za-z0-9_.-]+)`?\s*:\s*`?(caught|missed|unsure)\b", re.M | re.I)
JUDGE_HEAD = """You judge one output, labelled %s, against a key. Use no tools; judge the text below only.
For every item listed, print exactly one line: `<item id>: caught`, `<item id>: missed` or `<item id>: unsure`.
`caught` only when the output meets the item's catch as written. These stay `missed`: the file named but not the defect;
the defect named as style or minor where a blocker is required; the defect named while the verdict accepts the work;
the defect only in a trail; a right finding with a wrong failure scenario.

## Items
"""


class Refuse(Exception):
    """The set is not run: exit 2 with the message (file and row named)."""


# ---- reading the data files

def read_doc(path, what):
    try:
        with open(path, "rb") as fh:
            raw = fh.read()
    except OSError:
        raise Refuse("%s: absent or unreadable" % what)
    if not raw.strip():
        raise Refuse("%s: empty" % what)
    try:
        return json.loads(raw.decode("utf-8"))
    except ValueError as exc:
        raise Refuse("%s: broken YAML (written in JSON syntax; %s)" % (what, str(exc)[:120]))


def row_id(row):
    return row.get("id", "?") if isinstance(row, dict) else "?"


def first_missing(obj, required):
    return next((f for f in required if f not in obj), None)


def fields(obj, allowed, required, where):
    if not isinstance(obj, dict):
        raise Refuse("%s: must be a mapping" % where)
    unknown = sorted(set(obj) - set(allowed))
    if unknown:
        raise Refuse("%s: unknown field %s" % (where, unknown[0]))
    if first_missing(obj, required):
        raise Refuse("%s: no %s" % (where, first_missing(obj, required)))
    return obj


def types(obj, table, where):
    bad = next((k for k, t in table.items() if k in obj and not isinstance(obj[k], t)), None)
    if bad:
        raise Refuse("%s: field %s must be a %s" % (where, bad, table[bad].__name__))


def is_path(p):
    return isinstance(p, str) and bool(p)


def check_paths(row, where):
    if set(row["put"]) - {"instructions", "role"}:
        raise Refuse("%s: put keys are instructions and role (settings and skills stay excluded)" % where)
    if not all(is_path(p) for p in list(row["put"].values()) + row["remove"] + row["closure"]):
        raise Refuse("%s: put, remove and closure hold non-empty paths" % where)


def check_row(row, i):
    where = "%s row %s" % (ARMS_REL, row.get("id", i) if isinstance(row, dict) else i)
    fields(row, ROW, ROW[:7], where)
    types(row, ROW_TYPES, where)
    fields(row["source"], SOURCE, SOURCE, where + " source")
    if row["kind"] not in KINDS:
        raise Refuse("%s: unknown kind %s" % (where, row["kind"]))
    check_paths(row, where)


def arm_ids(rows):
    return [r["id"] for r in rows]


def check_rows(rows):
    if not rows:
        raise Refuse("%s: arms must be a non-empty list" % ARMS_REL)
    if len(set(arm_ids(rows))) != len(rows):
        raise Refuse("%s: duplicate arm id" % ARMS_REL)


def one_model(rows):
    if len({r["model"] for r in rows}) > 1:
        raise Refuse("%s: rows differ in model (I1: one measured id for every arm)" % ARMS_REL)


def load_arms(root):
    doc = fields(read_doc(os.path.join(root, ARMS_REL), ARMS_REL), HEADER, HEADER_REQ, ARMS_REL)
    for name, allowed in (("host_paths", HOST), ("launch", LAUNCH), ("export", SOURCE)):
        fields(doc[name], allowed, allowed, "%s %s" % (ARMS_REL, name))
    rows = doc["arms"] if isinstance(doc["arms"], list) else []
    for i, row in enumerate(rows):
        check_row(row, i)
    check_rows(rows)
    one_model(rows)
    return doc


def check_item(rel, item):
    where = "%s row %s" % (rel, row_id(item))
    fields(item, ITEM, ITEM_REQ, where)
    types(item, ITEM_TYPES, where)
    if not item["ledger_row"].strip():
        raise Refuse("%s: ledger_row empty (I8: an item exists only for a ledger row)" % where)
    if item["judged_by"] not in JUDGED_BY:
        raise Refuse("%s: judged_by must be critic or run" % where)
    if (item["judged_by"] == "run") != ("command" in item):
        raise Refuse("%s: a `command` exactly when judged_by is run" % where)


def load_key(root, role, task):
    rel = "%s/%s/%s/key.yaml" % (SETS_REL, role, task)
    key = fields(read_doc(os.path.join(root, rel), rel), KEY, ("canary", "items"), rel)
    types(key, KEY_TYPES, rel)
    if not key["canary"].strip() or not key["items"]:
        raise Refuse("%s: needs a canary token and at least one item" % rel)
    check_key_rows(rel, key)
    return check_ids(rel, key)


def check_key_rows(rel, key):
    for item in key["items"]:
        check_item(rel, item)
    for passage in key.get("intact", []):
        fields(passage, INTACT, INTACT, "%s row %s" % (rel, row_id(passage)))


def check_ids(rel, key):
    ids = [r[0] for r in all_items(key)]
    if len(set(ids)) != len(ids):
        raise Refuse("%s: duplicate item id" % rel)
    return key


def tasks_of(root, role):
    set_dir = os.path.join(root, SETS_REL, role)
    tasks = sorted(n for n in os.listdir(set_dir) if os.path.isfile(os.path.join(set_dir, n, "task.md"))) \
        if os.path.isdir(set_dir) else []
    if not tasks:
        raise Refuse("%s/%s: no task (a folder holding task.md)" % (SETS_REL, role))
    return tasks


# ---- the arm tree (draft Q1, I2)

def git(repo, *args):
    return subprocess.run(["git", "-C", repo] + list(args), capture_output=True)


def fill(path, role):
    return path.replace("<role>", role)


def check_source(src, where):
    if git(src["repo"], "cat-file", "-e", src["sha"] + "^{commit}").returncode:
        raise Refuse("%s: frozen sha %s unreachable in %s" % (where, src["sha"], src["repo"]))


def blob(src, path):
    done = git(src["repo"], "show", "%s:%s" % (src["sha"], path))
    return None if done.returncode else done.stdout


def dropped(name, drop):
    return any(name == d or name.startswith(d + "/") for d in drop)


def always(doc):
    return ALWAYS + (doc["host_paths"]["settings"], doc["host_paths"]["skills"])


def targets(doc, row, role):
    """[(host path, source path)]: put keys through host_paths, closure files at their own path (F2)."""
    want = [(fill(doc["host_paths"][k], role), fill(v, role)) for k, v in sorted(row["put"].items())]
    return want + [(fill(p, role), fill(p, role)) for p in row["closure"]]


def wanted(doc, row, role):
    """A target inside an always-excluded path is refused: a row adds exclusions, never takes one away (S11-1)."""
    want = targets(doc, row, role)
    if [host for host, _ in want if dropped(host, always(doc))]:
        raise Refuse("%s row %s: put or closure writes into an excluded path" % (ARMS_REL, row["id"]))
    return want


def overlay(doc, row, role):
    """{host path: bytes}; a source missing at the frozen sha is refused naming it (an arm short of a rule file hides
    losses, I9)."""
    files = {}
    for host, src in wanted(doc, row, role):
        files[host] = blob(row["source"], src)
        if files[host] is None:
            raise Refuse("%s row %s: put source %s missing at %s" % (ARMS_REL, row["id"], src, row["source"]["sha"]))
    return files


def export(src, dest, drop):
    tar = git(src["repo"], "archive", "--format=tar", src["sha"])
    if tar.returncode:
        raise Refuse("export %s@%s: git archive failed" % (src["repo"], src["sha"]))
    with tarfile.open(fileobj=io.BytesIO(tar.stdout)) as tf:
        tf.extractall(dest, members=[m for m in tf.getmembers() if not dropped(m.name, drop)], filter="data")


def shape_role(data, row):
    """The role file's `model:` becomes the one measured id (Q1: forge 2 writes `opus`, the old file a full id); a row
    `body` replaces everything after the front matter (the bare arm's one neutral line, F6)."""
    m = FRONT.match(data)
    if not m:
        raise Refuse("%s row %s: role file has no front matter" % (ARMS_REL, row["id"]))
    head = MODEL_LINE.sub(b"model: " + row["model"].encode("utf-8"), m.group(1), count=1)
    return head + (row["body"].encode("utf-8") + b"\n" if "body" in row else m.group(2))


def digest(pairs):
    h = hashlib.sha256()
    for name, data in pairs:
        h.update(name.encode("utf-8") + b"\0" + hashlib.sha256(data).digest())
    return h.hexdigest()


def task_files(task_dir):
    names = ["task.md"]
    for base, _, files in os.walk(os.path.join(task_dir, "input")):
        names += [os.path.relpath(os.path.join(base, f), task_dir).replace("\\", "/") for f in files]
    return sorted(names)


def raw(path):
    with open(path, "rb") as fh:
        return fh.read()


def put_file(dest, rel, data):
    path = os.path.join(dest, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(data)


def copy_task(task_dir, dest):
    """task.md and input/ go in; key.yaml never (I2)."""
    shutil.copyfile(os.path.join(task_dir, "task.md"), os.path.join(dest, "task.md"))
    if os.path.isdir(os.path.join(task_dir, "input")):
        shutil.copytree(os.path.join(task_dir, "input"), os.path.join(dest, "input"), dirs_exist_ok=True)


def snapshot(dest):
    """A fresh one-commit repo: the export carries no history (c2: history carries keys)."""
    commit = ("-c", "user.name=seeded", "-c", "user.email=seeded@invalid", "-c", "commit.gpgsign=false", "commit", "-q",
              "--no-verify", "--allow-empty", "-m", "arm tree")
    for args in (("init", "-q"), ("add", "-A"), commit):
        if git(dest, *args).returncode:
            raise Refuse("arm tree %s: git %s failed" % (dest, args[0]))


def drops(doc, row, role):
    return always(doc) + tuple(fill(p, role) for p in row["remove"])


def build(doc, row, role, task_dir, dest):
    """One throw-away arm tree; returns the fingerprint parts it fixes: tree (the export sha), task, rules_bundle (I1)."""
    files = overlay(doc, row, role)
    export(doc["export"], dest, drops(doc, row, role))
    role_path = fill(doc["host_paths"]["role"], role)
    if role_path in files:
        files[role_path] = shape_role(files[role_path], row)
    for rel, data in files.items():
        put_file(dest, rel, data)
    copy_task(task_dir, dest)
    snapshot(dest)
    return {"tree": doc["export"]["sha"], "rules_bundle": digest(sorted(files.items())),
            "task": digest((n, raw(os.path.join(task_dir, n))) for n in task_files(task_dir))}


def inside_repo(path):
    cur = os.path.abspath(path)
    while not os.path.exists(os.path.join(cur, ".git")):
        if os.path.dirname(cur) == cur:
            return False
        cur = os.path.dirname(cur)
    return True


def preflight(doc, rows, role):
    """Every refusal before the first launch: copies_root, the export, each row's source and overlay (set not run)."""
    if not os.path.isabs(doc["copies_root"]) or inside_repo(doc["copies_root"]):
        raise Refuse("%s copies_root %s: must be an absolute path outside every repo (C0-2)" % (ARMS_REL, doc["copies_root"]))
    check_source(doc["export"], ARMS_REL + " export")
    for row in rows:
        check_source(row["source"], "%s row %s" % (ARMS_REL, row["id"]))
        overlay(doc, row, role)


# ---- launching through arm.py, judging, rows

class Exam:
    """One `run`: the arms file, the keys, where rows go, the earlier rows (reuse) and this run's counter."""

    def __init__(self, root, role, doc, keys):
        self.root, self.role, self.doc, self.keys, self.seq = root, role, doc, keys, 0
        self.stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%S%f")  # run ids unique
        self.out = next_dir(os.path.join(root, RUNS_REL, role), self.stamp[:8])
        self.copies = os.path.join(doc["copies_root"], "forge-roles", role, self.stamp)
        self.prior, self.here = prior_rows(os.path.join(root, RUNS_REL, role)), set()


def next_dir(base, day):
    """One folder per exam: a second exam the same day gets <yyyymmdd>-2 (its reused rows are copied in), so `score` never
    mixes two exams' new-arm rows."""
    name, n = day, 1
    while os.path.exists(os.path.join(base, name)):
        n += 1
        name = "%s-%d" % (day, n)
    return os.path.join(base, name)


def day_key(name):
    tail = name[9:]
    return name[:8], int(tail) if tail.isdigit() else 1


def read_jsonl(path):
    if not os.path.isfile(path):
        return []
    try:
        with open(path, encoding="utf-8") as fh:
            return [json.loads(ln) for ln in fh if ln.strip()]
    except ValueError:
        raise Refuse("%s: broken row" % path)


def prior_rows(base):
    runs, scores = {}, []
    for day in sorted(os.listdir(base), key=day_key) if os.path.isdir(base) else []:
        runs.update((r["run"], r) for r in read_jsonl(os.path.join(base, day, "runs.jsonl")))
        scores += read_jsonl(os.path.join(base, day, "scores.jsonl"))
    return runs, scores


def append(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8", newline="\n") as fh:
        fh.writelines(json.dumps(arm.drop_money(r)) + "\n" for r in rows)


def record(ex, run_rows, scores):
    """Rows already in this result folder (a reuse from the same day) are not written twice."""
    ids = {r["run"] for r in run_rows} - ex.here
    ex.here |= ids
    append(os.path.join(ex.out, "runs.jsonl"), [r for r in run_rows if r["run"] in ids])
    append(os.path.join(ex.out, "scores.jsonl"), [s for s in scores if s["run"] in ids])


def new_id(ex, task, who):
    ex.seq += 1
    return "%s-%s-%s-%d" % (ex.stamp, task, who, ex.seq)


def spec_for(ex, model, run_id, who, parts, command_key):
    launch = ex.doc["launch"]
    spec = {"command": launch[command_key], "version_command": launch["version_command"], "model": model,
            "text_key": launch["text_key"], "models_key": launch["models_key"], "role": ex.role, "run": run_id, "arm": who}
    spec.update(parts)
    return spec


def unmeasured(spec, why):
    return {"run": spec["run"], "arm": spec["arm"], "status": "unmeasured: " + why}


def row_of(spec, done):
    lines = done.stdout.decode("utf-8", "replace").strip().splitlines() or ["exit %d" % done.returncode]
    found = arm.doc_of(lines[-1]) if done.returncode == 0 else None
    return found or unmeasured(spec, "arm.py refused (%s)" % lines[-1][:200])


def call_arm(spec, folder, out_dir, dry=False):
    """The one road (I7, C2-6 K6): arm.py; absent or refusing -> `unmeasured`, never a direct harness call."""
    if not os.path.isfile(ARM):
        return unmeasured(spec, "arm.py absent")
    os.makedirs(out_dir, exist_ok=True)
    spec_path = os.path.join(out_dir, "launch.json")
    with open(spec_path, "w", encoding="utf-8") as fh:
        json.dump(spec, fh)
    argv = [sys.executable, "-B", ARM, "launch", "--task", folder, "--spec", spec_path, "--out", out_dir]
    return row_of(spec, subprocess.run(argv + ["--dry-run"] * dry, capture_output=True))


def text_at(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return ""


def all_items(key):
    """(id, ledger_row, judged_by, kind) of every item and intact passage. The kind sets the polarity at scoring, never a
    null ledger row (t-2062 B1: a null ledger_row once scored an item as a passage, LOSS printed as GAIN)."""
    rows = [(i["id"], i["ledger_row"], i["judged_by"], "item") for i in key["items"]]
    return rows + [(p["id"], None, "critic", "intact") for p in key.get("intact", [])]


def uniform(key, catch, judge):
    return {r[0]: (catch, judge) for r in all_items(key)}


def parse_marks(text, ids):
    """Per item the judge's one word; an item marked twice differently, or not at all, is `unsure` (never caught)."""
    seen = {}
    for item, word in MARK.findall(text):
        seen.setdefault(item, set()).add(word.lower())
    return {i: (min(seen[i]) if len(seen.get(i, ())) == 1 else "unsure") for i in ids}


def judge_prompt(key, ids, label, text):
    rows = {r["id"]: "catch: " + r["catch"] for r in key["items"]}
    rows.update({p["id"]: "intact passage (caught = the output raises a blocker on it): " + p["passage"]
                 for p in key.get("intact", [])})
    return JUDGE_HEAD % label + "".join("- %s: %s\n" % (i, rows[i]) for i in ids) + "\n## Output %s\n\n%s\n" % (label, text)


def ask_judge(ex, key, ids, run_row, text):
    """I3: a fresh context in a neutral folder (no rule files) holding the key and this one output, labelled X or Y by
    lot; the lot map is written beside the rows and read only after scoring."""
    if not ids:
        return {}
    label, jid = random.choice("XY"), new_id(ex, run_row["task"], "judge")
    folder = os.path.join(ex.copies, jid)
    prompt = judge_prompt(key, ids, label, text).encode("utf-8")
    put_file(folder, "task.md", prompt)
    parts = {"tree": "none", "task": digest([("task.md", prompt)]), "rules_bundle": "none"}
    jrow = call_arm(spec_for(ex, run_row["fingerprint"]["model"], jid, "judge", parts, "judge_command"), folder,
                    os.path.join(folder, "out"))
    jtext = text_at(os.path.join(folder, "out", "out.txt")) if jrow["status"] == "measured" else ""
    keep_judge(ex, dict(jrow, task=run_row["task"]), jtext, {"label": label, "arm": run_row["arm"], "run": run_row["run"]})
    return marks_of(jrow, jtext, ids)


def marks_of(jrow, jtext, ids):
    """A judge that did not run (status not measured) gives `unmeasured`, never `unsure` -> `missed`: F170 reads a
    verdict, and a failed judgment is no verdict (t-2062 B2, I9: the old arm's long outputs hit the argv cap first)."""
    if jrow["status"] != "measured":
        return {i: ("unmeasured", jrow["run"]) for i in ids}
    marks = parse_marks(jtext, ids)
    return {i: (marks[i], jrow["run"]) for i in ids}


def keep_judge(ex, jrow, jtext, lot):
    record(ex, [jrow], [])
    put_file(os.path.join(ex.out, "judges"), jrow["run"] + ".txt", jtext.encode("utf-8"))
    path = os.path.join(ex.out, "lot.json")
    lots = json.loads(text_at(path) or "{}")
    lots[jrow["run"]] = lot
    put_file(ex.out, "lot.json", (json.dumps(lots, indent=1) + "\n").encode("utf-8"))


def second_look(found, second):
    """Still `unsure` after a second fresh judge -> `missed` (A27/F170; I9: unsure never becomes caught)."""
    for i, (catch, judge) in second.items():
        found[i] = ("missed" if catch == "unsure" else catch, found[i][1] + "," + judge)
    return found


def judge_critic(ex, key, run_row, text):
    found = ask_judge(ex, key, [r[0] for r in all_items(key) if r[2] == "critic"], run_row, text)
    again = [i for i, (catch, _) in found.items() if catch == "unsure"]
    return second_look(found, ask_judge(ex, key, again, run_row, text)) if again else found


def run_check(argv, cwd):
    """A `judged_by: run` item: the key's command in the arm tree after the agent ran; non-zero = caught (C2-6); a
    command that cannot start is `unmeasured`, never missed."""
    try:
        done = subprocess.run(argv, cwd=cwd, capture_output=True, stdin=subprocess.DEVNULL)
    except OSError:
        return "unmeasured"
    return "caught" if done.returncode else "missed"


def verdicts_for(ex, task, tree, run_row, text):
    key = ex.keys[task]
    if run_row["status"] != "measured":
        return uniform(key, run_row["status"].split(":")[0], "-")
    if not text.strip():
        return uniform(key, "missed", "none: no verdict")  # S11-1 edge: the agent ran and wrote nothing
    found = judge_critic(ex, key, run_row, text)
    found.update({i["id"]: (run_check(i["command"], tree), "run") for i in key["items"] if i["judged_by"] == "run"})
    return found


def score_rows(key, task, run_row, verdicts):
    return [{"task": task, "item": i, "ledger_row": ledger, "kind": kind, "judged_by": by, "arm": run_row["arm"],
             "run": run_row["run"], "fingerprint": run_row.get("fingerprint", {}),
             "catch": verdicts[i][0], "judge": verdicts[i][1], "tokens": run_row.get("tokens", {}),
             "wall": run_row.get("wall_s")} for i, ledger, by, kind in all_items(key)]


def fresh(ex, task, row):
    rid = new_id(ex, task, row["id"])
    tree = os.path.join(ex.copies, rid, "tree")
    return rid, tree, build(ex.doc, row, ex.role, os.path.join(ex.root, SETS_REL, ex.role, task), tree)


def attempt(ex, task, row, built):
    rid, tree, parts = built
    out = os.path.join(ex.copies, rid, "out")
    run_row = dict(call_arm(spec_for(ex, row["model"], rid, row["id"], parts, "command"), tree, out), task=task)
    run_row.setdefault("fingerprint", {"model": row["model"]})
    text = text_at(os.path.join(out, "out.txt"))
    if ex.keys[task]["canary"] in text_at(os.path.join(out, "raw.txt")) + text:
        run_row["status"] = "void: key canary in the output"  # I2: a catch on a leaked key never counts
    scores = score_rows(ex.keys[task], task, run_row, verdicts_for(ex, task, tree, run_row, text))
    record(ex, [run_row], scores)
    return run_row, scores


def run_once(ex, task, row, built=None):
    """One arm run; an unmeasured or void run is rerun once, both rows kept (S11-1 edge; one retry, never a loop)."""
    run_row, scores = attempt(ex, task, row, built or fresh(ex, task, row))
    if run_row["status"] != "measured":
        scores = scores + attempt(ex, task, row, fresh(ex, task, row))[1]
    return scores


def matches(r, task, who, fp):
    return r.get("arm") == who and r.get("task") == task and r.get("status") == "measured" \
        and arm.compare(r.get("fingerprint", {}), fp) is None


def reusable(ex, task, row, fp):
    """An arm other than `new` reuses its earlier measured runs on the task while compare is equal in EVERY field of its
    own fingerprint (old text is frozen, draft Q5); a field differs -> it runs again."""
    if not fp or row["id"] == CANDIDATE:
        return []
    return sorted(rid for rid, r in ex.prior[0].items() if matches(r, task, row["id"], fp))


def once(scores):
    """Each (run, task, item) once: a reused run's rows sit in every folder that reused it, and counting each copy
    weighed one run several times in the majority (t-2062 B3)."""
    return list({(s["run"], s["task"], s["item"]): s for s in reversed(scores)}.values())[::-1]


def reuse(ex, task, row, fp):
    same = reusable(ex, task, row, fp)
    kept = once([s for s in ex.prior[1] if s.get("run") in same])
    record(ex, [ex.prior[0][rid] for rid in same], kept)
    return kept


def arm_rows(ex, task, row):
    built = fresh(ex, task, row)
    probe = call_arm(spec_for(ex, row["model"], built[0], row["id"], built[2], "command"), built[1],
                     os.path.join(ex.copies, built[0], "probe"), dry=True)
    return reuse(ex, task, row, probe.get("fingerprint")) or run_once(ex, task, row, built)


def outcomes(scores):
    """Per (task, item) the arm's outcome: the majority of its measured catches; a tie or nothing measured `unmeasured`."""
    marks = {}
    for s in scores:
        marks.setdefault((s["task"], s["item"]), []).append(s["catch"])
    return {k: majority(c) for k, c in marks.items()}


def majority(catches):
    caught, missed = catches.count("caught"), catches.count("missed")
    if caught == missed:
        return "unmeasured"
    return "caught" if caught > missed else "missed"


def measured_runs(scores):
    return len({s["run"] for s in scores if s["catch"] in ("caught", "missed")})


def row_by_id(rows, who):
    return next(r for r in rows if r["id"] == who)


def adaptive(ex, task, rows, got):
    """Q5: any old/new disagreement on an item -> both arms run to a majority of 3 on that task, rows kept."""
    if outcomes(got[REFERENCE]) == outcomes(got[CANDIDATE]):
        return got
    for who in (REFERENCE, CANDIDATE):
        for _ in range(RUNS - measured_runs(got[who])):
            got[who] = got[who] + run_once(ex, task, row_by_id(rows, who))
    return got


def run_task(ex, task, rows):
    got = {r["id"]: arm_rows(ex, task, r) for r in rows}
    if REFERENCE not in got or CANDIDATE not in got:
        return got
    return adaptive(ex, task, rows, got)


def pick(doc, ids):
    unknown = sorted(set(ids) - set(arm_ids(doc["arms"])))
    if unknown:
        raise Refuse("--arm %s: no such row in %s" % (unknown[0], ARMS_REL))
    return [r for r in doc["arms"] if r["id"] in ids]


def check_set(role):
    if not SET_RE.fullmatch(role or ""):
        raise Refuse("--set %r: a role name ([a-z0-9_-]+)" % role)
    return role


def run(a):
    role = check_set(a.set)
    doc = load_arms(a.root)
    rows = pick(doc, a.arm or arm_ids(doc["arms"]))
    keys = {t: load_key(a.root, role, t) for t in tasks_of(a.root, role)}
    preflight(doc, rows, role)
    ex = Exam(a.root, role, doc, keys)
    for task in sorted(keys):
        run_task(ex, task, rows)
    print("written: %s" % os.path.relpath(ex.out, a.root).replace("\\", "/"))
    return 0


# ---- score (draft Q5, I4, I5, F6)

def unchanged(bare, intact):
    return "same" if intact else ("does-not-rank" if bare == "caught" else "held")


def classify(old, new, bare, intact):
    """Per item: a LOSS is old caught, new missed (or new alone raising a blocker on an intact passage); GAIN the reverse,
    recorded, never an offset (I5); NOISE both missed (does not rank, I4); both caught and the bare arm caught too ->
    does-not-rank (F6); an arm without a measured majority leaves the item `unmeasured` (never caught, I9)."""
    if "unmeasured" in (old, new):
        return "unmeasured"
    return (INTACT_CLASS if intact else ITEM_CLASS).get((old, new)) or unchanged(bare, intact)


def split(scores, k):
    catches = [s["catch"] for s in scores if (s["task"], s["item"]) == k]
    return "%d/%d caught" % (catches.count("caught"), catches.count("caught") + catches.count("missed"))


def group(rows):
    by_arm = {}
    for s in rows:
        by_arm.setdefault(s["arm"], []).append(s)
    return by_arm


def got(out, who, k):
    return out.get(who, {}).get(k, "unmeasured")  # an arm with no rows on the item never counts as caught


def shown(by_arm, k):
    return "; ".join("%s %s" % (who, split(by_arm.get(who, []), k)) for who in (REFERENCE, CANDIDATE, CONTROL))


def measured_pair(s, task):
    return s["task"] == task and s["arm"] in (REFERENCE, CANDIDATE) and s["catch"] in ("caught", "missed")


def mismatch(rows, task):
    """K3 wired (I1, t-2062 F5): the measured old and new runs of a task must be equal in every fingerprint field but
    rules_bundle; else the first differing field, and the task's items are `unmeasured: <field>`."""
    prints = [s.get("fingerprint", {}) for s in rows if measured_pair(s, task)]
    return next((f for f in [arm.compare(prints[0], p, ("rules_bundle",)) for p in prints[1:]] if f), None)


def mismatches(rows, info):
    return {task: mismatch(rows, task) for task in {k[0] for k in info}}


def candidate(old, bare):
    return not (old == "missed" or bare == "caught")


def undecided(old, bare, verdict):
    """F7: a discriminating candidate (old not missed, bare not caught) whose verdict or discrimination is unmeasured;
    a fingerprint mismatch leaves every item of the task undecided."""
    if verdict.startswith("unmeasured"):
        return candidate(old, bare) or verdict != "unmeasured"
    return candidate(old, bare) and (old, bare) != ("caught", "missed")


def verdict_of(old, new, bare, kind, bad):
    return "unmeasured: %s" % bad if bad else classify(old, new, bare, kind == "intact")


def flags(old, bare, verdict, kind, bad):
    """(discriminating, undecided) for an item; an intact passage is neither (it never ranks)."""
    item = kind == "item"
    return item and (old, bare) == ("caught", "missed") and not bad, item and undecided(old, bare, verdict)


def item_line(k, info, out, by_arm, bad):
    """(line, class, discriminating, undecided); the polarity comes from the row's kind, never a null ledger row (B1)."""
    old, new, bare = [got(out, who, k) for who in (REFERENCE, CANDIDATE, CONTROL)]
    verdict = verdict_of(old, new, bare, info[1], bad)
    line = "%s %s %s %s | %s" % (k[0], k[1], info[0] or "intact", verdict, shown(by_arm, k))
    return (line, verdict) + flags(old, bare, verdict, info[1], bad)


def ledgers(rows):
    return {(s["task"], s["item"]): (s["ledger_row"], s.get("kind", "item")) for s in rows}


def outcomes_by_arm(by_arm):
    return {who: outcomes(sc) for who, sc in by_arm.items()}


def report(rows, residual):
    by_arm, info = group(rows), ledgers(rows)
    out, bad = outcomes_by_arm(by_arm), mismatches(rows, info)
    items = [item_line(k, info[k], out, by_arm, bad[k[0]]) for k in sorted(info)]
    return [i[0] for i in items] + [rank_line(items), residual_line(rows, residual)]


def count(items, pos, value):
    return sum(1 for i in items if i[pos] == value)


def rank_line(items):
    """F6: a set ranks only with at least 3 discriminating items (old caught, bare missed); fewer, with a candidate
    unmeasured, is `unmeasured (n)`, never the honest `does not rank` (t-2062 F7)."""
    d, u = count(items, 2, True), count(items, 3, True)
    word = "ranks" if d >= 3 else ("unmeasured (%d)" % u if u else "does not rank")
    return "rank: %s (%d discriminating, %d unmeasured; LOSS %d, GAIN %d)" % (
        word, d, u, count(items, 1, "LOSS"), count(items, 1, "GAIN"))


def residual_line(rows, residual):
    """B4 (i): every result names what the launch cannot exercise in either arm, and this set's run-judged items."""
    ids = sorted({s["item"] for s in rows if s.get("judged_by") == "run"})
    return "residual: %s; judged_by run items: %s" % (residual, ", ".join(ids) or "none")


def latest(base):
    days = sorted(os.listdir(base) if os.path.isdir(base) else [], key=day_key)
    return days[-1] if days else ""


def day_of(a, base):
    day = a.date or latest(base)
    if not re.fullmatch(r"\d{8}(-\d+)?", day):
        raise Refuse("%s/%s: no result folder (YYYYMMDD[-n]) %r" % (RUNS_REL, a.set, day))
    return day


def score(a):
    base = os.path.join(a.root, RUNS_REL, check_set(a.set))
    rows = read_jsonl(os.path.join(base, day_of(a, base), "scores.jsonl"))
    if not rows:
        raise Refuse("%s/%s: no score rows" % (RUNS_REL, a.set))
    print("\n".join(report(rows, load_arms(a.root)["launch"]["residual"])))
    return 0


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("run", "score"):
        p = sub.add_parser(name)
        p.add_argument("--set", required=True)
        p.add_argument("--root", default=ROOT)
    sub.choices["run"].add_argument("--arm", action="append")
    sub.choices["score"].add_argument("--date")
    a = ap.parse_args(argv)
    try:
        return (run if a.cmd == "run" else score)(a)
    except Refuse as exc:
        print("refused: %s" % exc)
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
