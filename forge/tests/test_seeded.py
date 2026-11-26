# card: S11-1
"""Tables for measure/tools/seeded.py and arm.py (card S11-1, amending C0-4 and C2-6): the arm tree per row (K1), the
canary and every launch outcome through arm.py (K2, K5), compare (K3), Q5's classes and the rank (K4), the refusals (K5).
No test starts a harness: the command rows run a fixture script (C0-4 edge). Every row ends with `expected from:`."""
import json
import os
import subprocess
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "measure", "tools"))
import arm  # noqa: E402
import seeded  # noqa: E402

MODEL = "claude-opus-5-5"
HARNESS = r'''import json, sys
mode, model = sys.argv[1], sys.argv[2]
if mode == "fail":
    sys.exit(1)
text = {"empty": "", "canary": "seen CANARY-T1x", "judge": "T1.D1: caught\nI1: unsure"}.get(mode, "blocker: off by one")
used = {"othermodel": "claude-haiku"}.get(mode, model)
print(json.dumps({"result": text, "modelUsage": {used: {"inputTokens": 5, "costUSD": 1.5}}}))
'''
ROLE_NEW = b"---\nname: critic\nmodel: opus\n---\nRules: CLAUDE.md section Critic.\n"
ROLE_OLD = b"---\nname: critic\nmodel: claude-opus-5-5\n---\nold critic rules\n"
KEY = {"canary": "CANARY-T1x", "items": [{"id": "T1.D1", "ledger_row": "forge-roles.1.md#c8", "old_text": "o",
                                         "new_text": "n", "judged_by": "critic", "catch": "names the off-by-one"}],
       "intact": [{"id": "I1", "passage": "the loop bound"}]}


def git(repo, *args):
    subprocess.run(["git", "-C", repo, "-c", "user.name=t", "-c", "user.email=t@t", "-c", "commit.gpgsign=false"]
                   + list(args), check=True, capture_output=True)


def repo(path, files):
    for rel, data in files.items():
        seeded.put_file(path, rel, data)
    git(path, "init", "-q")
    git(path, "add", "-A")
    git(path, "commit", "-q", "--no-verify", "-m", "x")
    return {"repo": path, "sha": subprocess.run(["git", "-C", path, "rev-parse", "HEAD"], capture_output=True,
                                                text=True).stdout.strip()}


@pytest.fixture(scope="module")
def world(tmp_path_factory):
    tmp = str(tmp_path_factory.mktemp("seeded"))
    f2 = repo(os.path.join(tmp, "f2"), {"CLAUDE.md": b"NEW RULES\n", ".claude/agents/critic.md": ROLE_NEW,
                                        ".claude/settings.json": b"{}", ".claude/skills/x/SKILL.md": b"exam",
                                        "forge/specs/s.md": b"card", "measure/seeded/forge/critic/T1/key.yaml": b"KEY",
                                        "forge/COORDINATOR.md": b"c", "forge/BOOT.md": b"b", "code.py": b"x = 1\n"})
    old = repo(os.path.join(tmp, "old"), {"CLAUDE.md": b"OLD RULES\n", ".claude/agents/critic.md": ROLE_OLD,
                                          "docs/TESTING.md": b"old testing\n"})
    seeded.put_file(tmp, "h.py", HARNESS.encode())
    py = [sys.executable, "-B", os.path.join(tmp, "h.py")]
    rules = ["CLAUDE.md", ".claude", "forge/COORDINATOR.md", "forge/BOOT.md"]
    doc = {"schema": "arms/1", "copies_root": os.path.join(tmp, "copies"), "export": f2,
           "host_paths": {"instructions": "CLAUDE.md", "role": ".claude/agents/<role>.md",
                          "settings": ".claude/settings.json", "skills": ".claude/skills"},
           "launch": {"mechanism": "A", "command": py + ["{task}", "{model}"], "judge_command": py + ["judge", "{model}"],
                      "version_command": [sys.executable, "-c", "print('fixture 1')"], "text_key": "result",
                      "models_key": "modelUsage"},
           "arms": [{"id": "new", "kind": "tree_overlay", "source": f2, "remove": [], "closure": [], "model": MODEL,
                     "put": {"instructions": "CLAUDE.md", "role": ".claude/agents/<role>.md"}},
                    {"id": "old", "kind": "tree_overlay", "source": old, "remove": rules, "closure": ["docs/TESTING.md"],
                     "put": {"instructions": "CLAUDE.md", "role": ".claude/agents/<role>.md"}, "model": MODEL},
                    {"id": "bare", "kind": "tree_overlay", "source": f2, "put": {"role": ".claude/agents/<role>.md"},
                     "remove": rules, "closure": [], "model": MODEL, "body": "Do the task."}]}
    return tmp, doc


def lay(tmp, doc, key=KEY, name="root"):
    """A repo root holding arms.yaml and set critic/T1; a value given as bytes is written as is (broken files)."""
    root = os.path.join(tmp, name)
    for rel, value in ((seeded.ARMS_REL, doc), (seeded.SETS_REL + "/critic/T1/key.yaml", key)):
        seeded.put_file(root, rel, value if isinstance(value, bytes) else json.dumps(value).encode())
    seeded.put_file(root, seeded.SETS_REL + "/critic/T1/task.md", b"review the diff in input/\n")
    seeded.put_file(root, seeded.SETS_REL + "/critic/T1/input/d.diff", b"+for i in range(n + 1):\n")
    return root


TREE = [  # (arm, {path: expected bytes}, paths absent, expected from)
    ("new", {"CLAUDE.md": b"NEW RULES\n", ".claude/agents/critic.md": ROLE_NEW.replace(b"opus", MODEL.encode()),
             "forge/COORDINATOR.md": b"c"}, [], "S11-1 I1; Q1 table row new, model forced equal"),
    ("old", {"CLAUDE.md": b"OLD RULES\n", ".claude/agents/critic.md": ROLE_OLD, "docs/TESTING.md": b"old testing\n"},
     ["forge/COORDINATOR.md", "forge/BOOT.md"], "S11-1 K1; Q1 row old, F2 closure"),
    ("bare", {".claude/agents/critic.md": ROLE_NEW.split(b"---\nR")[0].replace(b"opus", MODEL.encode()) + b"---\nDo the task.\n"},
     ["CLAUDE.md", "forge/COORDINATOR.md"], "Q1 row bare: no CLAUDE.md, one neutral line (F6)"),
]


@pytest.mark.parametrize("who,present,absent,src", TREE)
def test_tree_per_arm(world, who, present, absent, src):
    tmp, doc = world
    root = lay(tmp, doc)
    dest = os.path.join(tmp, "trees", who)
    row = next(r for r in doc["arms"] if r["id"] == who)
    parts = seeded.build(doc, row, "critic", os.path.join(root, seeded.SETS_REL, "critic", "T1"), dest)
    for rel, data in present.items():
        assert seeded.raw(os.path.join(dest, rel)) == data, (rel, src)
    always = ["measure/seeded", "forge/specs", ".claude/settings.json", ".claude/skills", "key.yaml"]
    assert [p for p in always + absent if os.path.exists(os.path.join(dest, p))] == [], src
    assert os.path.isfile(os.path.join(dest, "input", "d.diff")) and parts["tree"] == doc["export"]["sha"], src
    count = subprocess.run(["git", "-C", dest, "rev-list", "--count", "HEAD"], capture_output=True, text=True).stdout
    assert count.strip() == "1", "I2: a fresh one-commit repo, no history"


def exam(tmp, doc, name):
    ex = seeded.Exam.__new__(seeded.Exam)
    ex.root, ex.role, ex.doc, ex.keys, ex.seq, ex.stamp = tmp, "critic", doc, {"T1": KEY}, 0, name
    ex.out, ex.copies, ex.here = os.path.join(tmp, "out", name), os.path.join(tmp, "copies", name), set()
    return ex


LAUNCH = [  # (harness mode, arm.py path, run status prefix, item catch, intact catch, expected from)
    ("verdict", None, "measured", "caught", "missed", "C2-6 catch by a fresh judge; F170: unsure twice -> missed"),
    ("canary", None, "void: key canary", "void", "void", "C2-6 edge: key in the agent's context -> run void"),
    ("fail", None, "unmeasured: harness exit 1", "unmeasured", "unmeasured", "S11-1 edge: harness failure"),
    ("othermodel", None, "unmeasured: model", "unmeasured", "unmeasured", "S11-1 edge: reported model id differs"),
    ("empty", None, "measured", "missed", "missed", "S11-1 edge: the agent wrote no verdict -> missed"),
    ("verdict", "absent.py", "unmeasured: arm.py absent", "unmeasured", "unmeasured", "C2-6 edge: arm.py absent"),
    ("verdict", os.path.join(ROOT, "forge", "tools", "ci.py"), "unmeasured: arm.py refused", "unmeasured", "unmeasured",
     "C2-6 K6: arm.py refusing -> unmeasured, never a direct harness call"),
]


@pytest.mark.parametrize("mode,arm_path,status,catch,intact,src", LAUNCH)
def test_launch_through_arm(world, monkeypatch, mode, arm_path, status, catch, intact, src):
    tmp, doc = world
    doc = dict(doc, launch=dict(doc["launch"], command=doc["launch"]["command"][:3] + [mode, "{model}"]))
    if arm_path:
        monkeypatch.setattr(seeded, "ARM", arm_path)
    tree = os.path.join(tmp, "plain", mode + str(bool(arm_path)))
    seeded.put_file(tree, "task.md", b"task")
    ex = exam(tmp, doc, mode + str(bool(arm_path)))
    run_row, scores = seeded.attempt(ex, "T1", doc["arms"][0], ("r1", tree, {"tree": "t", "task": "k", "rules_bundle": "b"}))
    assert run_row["status"].startswith(status), (run_row["status"], src)
    assert [s["catch"] for s in scores] == [catch, intact], src
    assert "cost" not in seeded.text_at(os.path.join(ex.out, "runs.jsonl")).lower(), "C0-4 K2: no money key in a row"


FP = {"mode": "comparison", "model": MODEL, "harness": "h 1", "launch": "l", "tree": "t", "task": "k", "rules_bundle": "a"}
COMPARE = [  # (changed fields, allowed, expected, expected from)
    ({"rules_bundle": "b"}, ("rules_bundle",), None, "S11-1 K3: old/new differ only in rules_bundle"),
    ({"rules_bundle": "b"}, (), "rules_bundle", "Q5: old-arm reuse needs every field equal"),
    ({"rules_bundle": "b", "model": "x"}, ("rules_bundle",), "model", "S11-1 K3: else compare names the field"),
    ({"tree": "t2"}, ("rules_bundle",), "tree", "I1: same tree snapshot"),
    ({"harness": ""}, ("rules_bundle",), "harness", "I1: same harness version"),
]


@pytest.mark.parametrize("change,allow,expected,src", COMPARE)
def test_compare(change, allow, expected, src):
    assert arm.compare(FP, dict(FP, **change), allow) == expected, src


def rows(item, ledger, **arms):
    return [{"task": "T1", "item": item, "ledger_row": ledger, "arm": who, "run": "%s%d" % (who, n), "catch": c}
            for who, catches in arms.items() for n, c in enumerate(catches.split())]


CLASSES = [  # (old, new, bare, intact, expected class, expected from)
    ("caught", "missed caught missed", "missed", False, "LOSS", "Q5 LOSS; a 2-1 split is the majority"),
    ("missed", "caught", "missed", False, "GAIN", "Q5 GAIN, recorded (I5)"),
    ("missed", "missed", "missed", False, "NOISE", "Q5 NOISE: both miss, no rank (I4)"),
    ("caught", "caught", "caught", False, "does-not-rank", "F6: the bare arm catches it too"),
    ("caught", "caught", "missed", False, "held", "F6: discriminating and kept"),
    ("missed", "caught", "missed", True, "LOSS", "Q5: new raises a blocker on an intact passage, old does not"),
    ("unmeasured void", "missed", "missed", False, "unmeasured", "I9: an unmeasured run never counts as caught"),
]


@pytest.mark.parametrize("old,new,bare,intact,expected,src", CLASSES)
def test_classes(old, new, bare, intact, expected, src):
    lines = seeded.report(rows("I1" if intact else "T1.D1", None if intact else "L1", old=old, new=new, bare=bare))
    assert lines[0].split(" | ")[0].endswith(" " + expected), (lines, src)


def test_rank_and_adaptive():
    three = sum((rows("T1.D%d" % i, "L%d" % i, old="caught", new="caught", bare="missed") for i in range(3)), [])
    assert seeded.report(three)[-1].startswith("rank: ranks (3"), "F6: 3 discriminating items rank"
    assert seeded.report(three[3:])[-1].startswith("rank: does not rank (2"), "F6: fewer than 3 -> does not rank"
    split = rows("T1.D1", "L1", old="caught", new="missed")
    old, new = [[r for r in split if r["arm"] == w] for w in ("old", "new")]
    assert seeded.outcomes(old) != seeded.outcomes(new), "Q5: a disagreement sends both arms to 3 runs"


REFUSALS = [  # (what to change, expected fragment, expected from)
    ({"arms": b""}, "arms.yaml: empty", "S11-1 edge: arms.yaml empty"),
    ({"arms": b"arms: [old"}, "arms.yaml: broken YAML", "S11-1 edge: broken YAML"),
    ({"arm_field": {"extra": 1}}, "row new: unknown field extra", "S11-1 edge: unknown field, row named"),
    ({"key": b"  \n"}, "key.yaml: empty", "S11-1 edge: key.yaml empty"),
    ({"key": dict(KEY, extra=1)}, "key.yaml: unknown field extra", "S11-1 edge: key unknown field"),
    ({"key": dict(KEY, items=[{k: v for k, v in KEY["items"][0].items() if k != "ledger_row"}])},
     "key.yaml row T1.D1: no ledger_row", "S11-1 edge, I8: a key row without ledger_row"),
    ({"arm_field": {"closure": ["docs/GONE.md"]}}, "put source docs/GONE.md missing", "S11-1 edge: put source missing"),
    ({"arm_field": {"source": {"repo": "x", "sha": "0" * 40}}}, "frozen sha", "S11-1 edge: frozen sha unreachable"),
    ({"copies": "f2/inside"}, "outside every repo", "S11-1 edge: copies_root inside a repo"),
]


@pytest.mark.parametrize("change,fragment,src", REFUSALS)
def test_refusals(world, capsys, change, fragment, src):
    tmp, doc = world
    doc = json.loads(json.dumps(doc))
    doc["arms"][0].update(change.get("arm_field", {}))
    doc["copies_root"] = os.path.join(tmp, change.get("copies", "copies"))
    root = lay(tmp, change.get("arms", doc), change.get("key", KEY), "refusal")
    code = seeded.main(["run", "--set", "critic", "--root", root])
    out = capsys.readouterr().out
    assert code == 2 and fragment in out and not os.path.isdir(os.path.join(root, seeded.RUNS_REL)), (out, src)
