# card: B3
"""One table per behaviour for forge/tools/words.py (card B3): `check` over a small temp tree, the `add` battery, the linked
worktree refusal. Every row ends with `expected from:` (forge/TESTING.md rule 4); in-process through main(argv)."""
import contextlib
import io
import json
import os
import subprocess
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
import words  # noqa: E402

BOOT_OK = ("decided by the owner: forge/owner-words.yaml\nphase 1: build -- 2026-11-26\n# Heading\n"
           "## Sub\na plan line (plan 3.2)\n")


def rec(i, **kw):
    r = {"id": "W-%d" % i, "kind": "word", "date": "2026-11-25~01:30", "scope": "forge", "scope_by": "owner", "asked": "q",
         "carrier": "plan:1 (h)", "words": "слова", "executed_in": [], "open": "not traced"}
    r.update(kw)
    return {k: v for k, v in r.items() if v is not None}


def world(tmp_path, records, files=None):
    root = str(tmp_path)
    files = dict(files or {})
    if records is not None:
        files[words.REG] = records if isinstance(records, bytes) else words.render(records).encode("utf-8")
    files.setdefault(words.PLAN, "### 3. Section\n1. a\n2. b\n")
    for rel, text in [(k, v) for k, v in files.items() if v is not None]:  # None: the file is absent
        p = os.path.join(root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "wb") as fh:
            fh.write(text if isinstance(text, bytes) else text.encode("utf-8"))
    return root


def run(root, *args, stdin=b""):
    buf = io.StringIO()
    old = sys.stdin
    sys.stdin = io.TextIOWrapper(io.BytesIO(stdin))
    try:
        with contextlib.redirect_stdout(buf):
            code = words.main(["--root", root] + list(args))
    finally:
        sys.stdin = old
    return code, buf.getvalue()


FORGE, LEAD, FACT = rec(1), rec(2, scope_by="lead"), rec(3, scope="factory")
CHECK = [  # (records, files, exit, fragments in the output, expected from)
    ([FORGE], {"factory/a.md": "(case: W-1)"}, 1, ["factory/a.md:1: W-1 scope mismatch"], "card B3 K2; plan 3.11 (money case)"),
    ([LEAD], {"factory/a.md": "(case: W-2)"}, 0, ["listed: factory/a.md:1: W-2 scope mismatch", "named by the lead"], "card B3 K2"),
    ([FACT], {"CLAUDE.md": "x\n(case: W-3)"}, 1, ["CLAUDE.md:2: W-3 scope mismatch"], "card B3 check: a forge rule citing factory"),
    ([rec(1, scope="unknown", scope_by="lead")], {"CLAUDE.md": "W-1"}, 0, ["listed: CLAUDE.md:1: W-1 scope unknown"], "card B3"),
    ([FORGE], {"CLAUDE.md": "(case: W-1, D-4)"}, 1, ["decision cited as owner's word"], "card B3 check; v1.10 1694-1695"),
    ([FORGE], {"CLAUDE.md": "W-9 and D-0056 and FH-D-1"}, 1, ["CLAUDE.md:1: W-9 no such record"], "card B3 K2 (a missing id; old ids not read)"),
    ([FORGE, rec(2, supersedes="W-1")], {"CLAUDE.md": "W-1"}, 1, ["W-1 superseded by W-2"], "card B3 edge: later word supersedes"),
    ([FORGE, rec(2, scope_by="lead", supersedes="W-1"), rec(1, id="D-1", kind="decision", text="t", decided_by="lead",
      rests_on=["W-1"], words=None, scope_by="lead")], {}, 0, ["D-1 rests on W-1, superseded by W-2"],
     "card B3 edge: a decision resting on a superseded word is listed"),
    ([FORGE], {"forge/specs/x.md": "W-9", "forge/tests/t.py": "W-9"}, 0, ["0 citations"], "card B3 edge: specs copies not counted"),
    ([FORGE], {}, 0, ["listed: BOOT not written yet"], "card B3: BOOT absent -> BOOT not written yet"),
    ([FORGE], {"forge/BOOT.md": BOOT_OK}, 0, ["0 citations"], "card B1 line classes: plan, exempt (W-101: no word class)"),
    ([FORGE, rec(49)], {"forge/BOOT.md": BOOT_OK + "her words (W-49)\n"}, 1, ["BOOT.md:6: owner word on BOOT: cite the plan item"],
     "W-101, critic t-2025 F3: a live word record is still refused on BOOT"),
    ([FORGE, rec(49)], {"forge/BOOT.md": BOOT_OK + "x (W-49) (plan 3.2)\n"}, 1, ["BOOT.md:6: owner word on BOOT: cite the plan item"],
     "critic t-2028 F5: a W id before a resolving plan citation is still refused"),
    ([FORGE, rec(3, id="D-3", kind="decision", text="t", decided_by="lead", rests_on=["W-1"], words=None, scope_by="lead")],
     {"forge/BOOT.md": BOOT_OK + "x (D-3) (plan 3.2)\n"}, 1, ["BOOT.md:6: decision cited as owner's word"],
     "t-2028 F5 class: a live D id before a resolving plan citation is still refused"),
    ([FORGE, rec(49)], {"forge/BOOT.md": BOOT_OK.replace("build", "x (W-49)")}, 1, ["BOOT.md:2: owner word on BOOT: cite the plan item"],
     "critic t-2030 F6: an exempt phase line holding a W id is refused, not exempt"),
    ([FORGE, rec(3, id="D-3", kind="decision", text="t", decided_by="lead", rests_on=["W-1"], words=None, scope_by="lead")],
     {"forge/BOOT.md": BOOT_OK.replace("build", "x (D-3)")}, 1, ["BOOT.md:2: decision cited as owner's word"],
     "critic t-2034 M3-D: an exempt phase line holding a D id is refused, not exempt"),
    ([FORGE, rec(49), rec(3, id="D-3", kind="decision", text="t", decided_by="lead", rests_on=["W-1"], words=None, scope_by="lead")],
     {"forge/BOOT.md": BOOT_OK + "x (D-3) (W-49) (plan 3.2)\n"}, 1, ["BOOT.md:6: owner word on BOOT: cite the plan item"],
     "critic t-2030 M3: W and D on one line -> the W red (W before D)"),
    ([FORGE], {"forge/BOOT.md": BOOT_OK + "no citation here\n"}, 1, ["BOOT.md:6: uncited line"], "card B3 K2: a BOOT line with no citation"),
    ([FORGE], {"forge/BOOT.md": BOOT_OK + "x (plan 3.9)\ny (plan 8)\n"}, 1, ["BOOT.md:6: plan id absent: 3.9", "BOOT.md:7: plan id absent: 8"],
     "card B1 class 2: <h>.<n> under a ### heading"),
    ([FORGE], {"forge/BOOT.md": BOOT_OK + "z (D-1)\n"}, 1, ["BOOT.md:6: decision cited as owner's word"], "v1.10 1694-1695"),
    ([FORGE], {"forge/BOOT.md": "her words (W-1)\n"}, 1, ["exempt line 1 must stand exactly once, found 0"], "card B1 K2: exempt lines once each"),
    (None, {}, 2, ["cannot judge: forge/owner-words.yaml"], "card B3 edge: registry absent -> exit 2"),
    (b'{"schema": "words/2",\n"records": [\n x]}', {}, 2, ["owner-words.yaml:3: broken syntax"], "card B3 edge: broken YAML names the line"),
    (b'{"schema": "words/2",\n"records": []}\n\xff', {}, 2, ["owner-words.yaml:3: not UTF-8"], "card B3 edge: non-UTF-8 names the line"),
    (b"[]", {}, 2, ["not a words/2 registry"], "card B3 edge: schema"),
    (b'{"schema": "words/1", "records": []}\n', {}, 2, ["not a words/2 registry"], "t-2010 M3: a wrong schema on a dict"),
    ([FORGE], {"CLAUDE.md": "(case: W-1, see FH-D-12)"}, 0, ["1 citations"], "t-2010 B3-1: FH-D-12 is no citation"),
    ([FORGE], {"CLAUDE.md": "(case: W-1; old D-0056)"}, 0, ["1 citations"], "t-2010 B3-1: D-0056 is no citation"),
    ([FORGE], {"CLAUDE.md": "(case: W-1; D-12)"}, 1, ["decision cited as owner's word"], "t-2010 B3-1: a real D- still red"),
    ([FORGE], {"CLAUDE.md": b"\xff W-9 rule"}, 1, ["CLAUDE.md:1: W-9 no such record"], "t-2010 B3-3: non-UTF-8 judged"),
    ([FORGE], {"forge/BOOT.md": BOOT_OK, words.PLAN: None}, 2, ["cannot judge: forge/BOOT.md:5: plan copy"],
     "t-2010 B3-4; B1 edge: plan copy absent"),
    ([rec(1, scope="x")], {}, 1, ["W-1: scope 'x' is not one of"], "card B3: check reads the shape of every record"),
]


@pytest.mark.parametrize("records,files,code,frags,source", CHECK)
def test_check(tmp_path, records, files, code, frags, source):
    got, out = run(world(tmp_path, records, files), "check")
    assert got == code and all(f in out for f in frags), out


BAD = [  # (mutation of a valid word record, fragment of the refusal, expected from)
    ({"words": ""}, "words is missing or empty", "card B3 edge: empty words"),
    ({"scope": "both2"}, "scope 'both2' is not one of", "card B3 edge: scope outside the set"),
    ({"date": "2026-13-45"}, "date '2026-13-45' is not YYYY-MM-DD", "card B3 edge: bad date"),
    ({"id": "W-1"}, "id W-1 exists: a record is never changed", "card B3 K3: duplicate id / edit attempt"),
    ({"kind": "note"}, "kind 'note' is not one of word, decision", "card B3 edge: kind outside the set"),
    ({"carrier": None}, "carrier is missing or empty", "card B3 edge: a word without carrier"),
    ({"extra": 1}, "unknown field 'extra' for kind word", "card B3 (every bad field named)"),
    ({"executed_in": [], "open": None}, "open is missing or empty", "card B3: `[]` with `open: <why>`"),
    ({"executed_in": "x"}, "executed_in must be a list", "card B3 common fields"),
    ({"supersedes": "W-77"}, "supersedes 'W-77' names no earlier record", "card B3 edge: supersedes"),
    ({"words": "я" * 4096 + "a"}, "words is 8193 bytes, over 8192; split into records by topic, each verbatim", "card B3 edge: 8193 refused"),
    ({"id": "D-2", "kind": "decision", "text": "t", "decided_by": "boss", "rests_on": [], "words": None},
     "decided_by 'boss' is not one of owner, lead", "card B3 decision fields"),
    ({"id": "D-2", "kind": "decision", "text": "t", "decided_by": "lead", "rests_on": ["W-1"], "words": None,
      "open": "x", "scope_by": "lead"}, None, "card B3: a decision resting on an existing word is accepted"),
    ({"id": "D-2", "kind": "decision", "text": "t", "decided_by": "lead", "rests_on": [], "words": None}, "rests_on is empty and basis",
     "card B3: rests_on empty only with basis"),
    ({"words": "я" * 4096, "id": "W-2"}, None, "card B3 edge: 8192 bytes accepted"),
    ({"words": "\ud800", "id": "W-2"}, "text is not encodable as UTF-8", "rule 11: encoding battery"),
]


@pytest.mark.parametrize("mut,frag,source", BAD)
def test_add(tmp_path, mut, frag, source):
    root = world(tmp_path, [rec(1)])
    before = open(os.path.join(root, words.REG), "rb").read()
    path = os.path.join(root, "new.json")
    with open(path, "wb") as fh:
        fh.write(json.dumps(rec(2, **mut)).encode("ascii"))
    code, out = run(root, "add", path)
    after = open(os.path.join(root, words.REG), "rb").read()
    if frag is None:
        assert code == 0 and after.startswith(before[:-4]) and after.count(b"\n") == before.count(b"\n") + 1
    else:
        assert code == 2 and frag in out and after == before, out


def test_add_refusals(tmp_path):
    """expected from: t-2010 B3-2 (a non-canonical file is refused, bytes unchanged) and B3-5 (a missing input is exit 2)."""
    root = world(tmp_path, [rec(1)])
    path = os.path.join(root, words.REG)
    hand = words.render([rec(1)]).encode("utf-8").replace(b'{"schema"', b'{"note": "x", "schema"')
    with open(path, "wb") as fh:
        fh.write(hand)
    code, out = run(root, "add", "-", stdin=json.dumps(rec(2)).encode("ascii"))
    assert code == 2 and "not canonical" in out and "words.render" in out and open(path, "rb").read() == hand
    with open(path, "wb") as fh:
        fh.write(words.render([rec(1)]).encode("utf-8").replace(b"\n", b"\r\n"))
    code, out = run(root, "add", "-", stdin=json.dumps(rec(2)).encode("ascii"))
    assert code == 0 and b'"id": "W-2"' in open(path, "rb").read() and b'"id": "W-1"' in open(path, "rb").read()
    code, out = run(root, "add", os.path.join(root, "nope.json"))
    assert code == 2 and out.startswith("refused: cannot read ") and "nope.json" in out


def test_add_input_and_resolve(tmp_path):
    """expected from: card B3 edges (non-UTF-8 and broken input refused, nothing written); B20 resolve; B3 show."""
    root = world(tmp_path, [rec(1), rec(2, supersedes="W-1")])
    for raw, frag in ((b'{"words": "\xff"}', "not UTF-8"), (b"{", "not JSON"), (b"[]", "not one JSON object")):
        code, out = run(root, "add", "-", stdin=raw)
        assert code == 2 and frag in out
    assert run(world(tmp_path / "x", None), "add", "-", stdin=b"{}")[0] == 2
    assert run(root, "resolve", "W-2") == (0, "W-2 word live\n")
    assert run(root, "resolve", "W-1") == (1, "W-1 word superseded by W-2\n")
    assert run(root, "resolve", "W-5")[0] == 1 and run(root, "show", "W-5")[0] == 1
    assert '"words": "слова"' in run(root, "show", "W-1")[1]
    assert run(str(tmp_path / "none"), "show", "W-1")[0] == 2
    assert words.plan_key_ok(str(tmp_path / "none"), "3") is None and words.resolve_id(root, "W-9") is None


def test_linked_worktree_refused(tmp_path):
    """expected from: card B14 (amends B3): a root that is a linked worktree is refused, a main checkout and a non-repository pass."""
    main, wt = tmp_path / "main", str(tmp_path / "wt")
    world(main, [rec(1)])
    git = ["git", "-C", str(main), "-c", "user.name=t", "-c", "user.email=t@t"]
    for args in (["init", "-q"], ["commit", "-q", "--allow-empty", "-m", "x"], ["worktree", "add", "-q", wt, "-b", "w/x"]):
        subprocess.run(git + args, check=True, capture_output=True)
    world(tmp_path / "wt2", [rec(1)])
    new = json.dumps(rec(2)).encode("ascii")
    assert not words.linked_worktree(str(main)) and not words.linked_worktree(str(tmp_path / "wt2"))
    assert words.linked_worktree(wt)
    code, out = run(wt, "add", "-", stdin=new)
    assert code == 2 and "linked worktree" in out and "forge2-repo/forge/tools/words.py" in out
    assert run(str(main), "add", "-", stdin=new)[0] == 0
