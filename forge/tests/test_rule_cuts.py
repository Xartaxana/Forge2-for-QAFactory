# card: B22
"""Tests of rule_cuts.py (B22): the pure core on in-memory rule sets read with the real forge/rule-cuts.json (a data joint),
then one module-scoped git repository for range, base, blob and config rows. Rows are named by the draft t-2070 section 7
(T1-T41); `expected from:` names each source. Fixture words are chosen so every 4-character prefix is unique."""
import json
import os
import re
import subprocess
import sys
from contextlib import redirect_stdout
from io import StringIO

import pytest

FORGE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(FORGE, "tools"))
import ratchets  # noqa: E402
import rule_cuts as rc  # noqa: E402

REGF = "forge/owner-words.yaml"
with open(os.path.join(FORGE, "rule-cuts.json"), encoding="utf-8") as fh:
    CFG_TEXT = fh.read()
CFG = json.loads(CFG_TEXT)
RECS = [{"id": "W-1", "kind": "word"}, {"id": "D-1", "kind": "decision"}, {"id": "W-2", "kind": "word"},
        {"id": "W-3", "kind": "word", "supersedes": "W-2"}, {"id": "W-188", "kind": "word"}]
B1 = "- Lantern quokka rules every zephyr -- always.\n"
B2 = "- Marble otter guards each harbor (case: FR-7).\n"
J = "- Alfa bravo charlie delta echo foxtrot golf hotel india juliet.\n"
CYR = "- Правило запрещает тихий срез.\n"
LONG = "- " + " ".join("w%03d" % i for i in range(60)) + "\n"  # one 301-character fragment
CLAUDE = ("# Rules\n\n## Worker duties\n\ncarry: FR-7, FR-8\nrows: fr:A1\n\n" + B1 + B2 + J + CYR + LONG
          + "\n## Waits\n\n- Wait caps stay 3600 seconds firmly.\n- Quartz lynx sleeps.\n\n"
          "Velvet thistle opens. Copper walrus sings; amber ferret naps.\nBasalt heron flies.\n")
BOOT = "# Boot\n\ncarry: FR-9\n\n- Quartz lynx sleeps.\n- Nimbus gecko waits (case: FR-9).\n"
BASE = {"CLAUDE.md": CLAUDE, "forge/BOOT.md": BOOT}
CUT, CARRY, GL = (B1, ""), ("carry: FR-7, FR-8", "carry: FR-8"), 'rule-cut: "Lantern quokka rules every" -- %s'
LOW = (J, "- Alfa bravo charlie delta echo kilo lima mike november oscar.\n")  # 5 of 10 equal-weight tokens kept: 0.5


@pytest.fixture(autouse=True)
def clean_env(monkeypatch):
    for k in [k for k in os.environ if k.startswith("GIT_")] + ["FORGE_BASE"]:
        monkeypatch.delenv(k, raising=False)


def put(root, files):
    for rel, text in files.items():
        p = os.path.join(root, rel)
        if text is None:
            os.remove(p)
            continue
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "wb") as fh:
            fh.write(text if isinstance(text, bytes) else text.encode("utf-8"))


@pytest.fixture(scope="module")
def roots(tmp_path_factory):
    out = []
    for text in (json.dumps({"schema": "words/2", "records": RECS}), "{not json"):
        out.append(str(tmp_path_factory.mktemp("r")))
        put(out[-1], {REGF: text})
    return out


def core(roots, subs=(), extra=None, log="", broken=0):
    """The pure core on BASE against BASE edited (subs on CLAUDE.md; extra files, None deletes), filtered as tree() filters."""
    text = CLAUDE
    for old, new in subs:
        text = text.replace(old, new)
    head = {**BASE, "CLAUDE.md": text, **(extra or {})}
    head = {r: t for r, t in head.items() if t is not None and rc.in_set(r, CFG["files"])}
    code, said = rc.judge(BASE, head, log, CFG, lambda rid: ratchets.resolve(roots[broken], rid, ("word",)))
    return code, "\n".join(said)


def holds(out, has):
    """Each entry is in the output; one starting with `!` is not."""
    return all((h[1:] not in out) if h.startswith("!") else (h in out) for h in has)


# expected from: t-2070 2.1 (a cut, its place), 2.4 (the printed form, 200 characters), 3 (the line forms, gist_min, a leading
# `>`, `\r`), E24-E27, K1-K2; ratchets.resolve's texts (F252); the Lead's F11 (b) (not_confirming refused by code)
@pytest.mark.parametrize("subs, log, broken, code, has", [
    ([CUT], "", 0, 1, ['new: CLAUDE.md::Worker%20duties cut "- Lantern quokka rules every zephyr -- always." -- needs rule-cut: "<3+']),
    ([CUT], GL % "W-1", 0, 0, ["1 covered"]),
    ([CUT], GL % "D-1", 0, 1, ["new: CLAUDE.md::Worker%20duties cannot resolve D-1: kind decision, wants word"]),
    ([CUT], GL % "W-2", 0, 1, ["cannot resolve W-2: superseded by W-3"]),
    ([CUT], GL % "W-9", 0, 1, ["cannot resolve W-9: not in"]),
    ([CUT], GL % "W-1", 1, 1, ["registry unreadable"]),
    ([CUT], 'rule-cut: "quokka rules" -- W-1', 0, 1, ["not read: gist under 3 words", "0 covered"]),
    ([CUT], 'rule-cut: "quokka rules every" -- W-1', 0, 0, ["1 covered"]),
    ([CUT], "m\n\n  > " + GL % "W-1" + "\n", 0, 0, ["1 covered"]),
    ([CUT], GL % "W-1" + "\r\nnext", 0, 0, ["1 covered"]),
    ([CUT], 'rule-cut: "every zephyr -- always" -- W-1', 0, 0, ["1 covered"]),
    ([CUT], 'rule-cut:\nrule-cut: "Lantern quokka rules" W-1', 0, 1, ["0 covered", "!not read", "!unused"]),
    ([(LONG, "")], "", 0, 1, ['cut "%s..." -- needs' % LONG[:200]]),
    ([(LONG, "")], 'rule-cut: "%s" -- W-1' % " ".join("w%03d" % i for i in range(50, 58)), 0, 0, ["1 covered"]),
    ([], GL % "W-1", 0, 0, ["unused: " + GL % "W-1"]),
    ([CUT], GL % "W-188", 0, 1, ["cannot confirm: W-188 is listed in forge/rule-cuts.json not_confirming"]),
])
def test_cut(roots, subs, log, broken, code, has):
    c, o = core(roots, subs, None, log, broken)
    assert c == code and holds(o, has), o


# expected from: t-2070 2.3 (ids of carry/rows lines; one id line covers the id and the cut raw line holding it; a section's
# ids are no cover), E5-E7, E9 and F5 (a) (a deleted file: per fragment and id, one cover per rule), K3, K10
@pytest.mark.parametrize("subs, extra, log, code, has", [
    ([CARRY], {}, "", 1, ["new: FR-7 left every carry line (base: CLAUDE.md::Worker%20duties)"]),
    ([CARRY, ("## Waits\n", "## Waits\n\ncarry: FR-7\n")], {}, "", 0, ["0 ids gone"]),
    ([CARRY, (B2, "")], {}, "rule-cut: FR-7 -- W-1", 0, ["1 fragments, 1 ids gone, 2 covered"]),
    ([("rows: fr:A1", "rows:")], {}, "", 1, ["new: fr:A1 left every carry line"]),
    ([CUT], {}, "rule-cut: FR-8 -- W-1", 1, ["unused: rule-cut: FR-8", "new: CLAUDE.md::Worker%20duties cut"]),
    ([], {"forge/BOOT.md": None}, "", 1, ["new: FR-9 left", 'new: forge/BOOT.md::Boot cut "- Nimbus gecko waits ."', "1 fragments"]),
    ([], {"forge/BOOT.md": None}, "rule-cut: FR-9 -- W-1", 0, ["1 fragments, 1 ids gone, 2 covered"]),
])
def test_ids(roots, subs, extra, log, code, has):
    c, o = core(roots, subs, extra, log)
    assert c == code and holds(o, has), o


# expected from: t-2070 2.1 (removed lines over the whole set, fragments, windows, the share `>= keep`), 3 (rule-reworded),
# E1-E4, E10-E11, E28-E33, K4-K6; the Lead's F7 (a) (a case span is no text) and F8 (b) (a changed number is a cut)
@pytest.mark.parametrize("subs, extra, log, code, has", [
    ([CUT], {"forge/COORDINATOR.md": B1}, "", 0, ["cuts: 0 fragments", "!paired", "!new:"]),
    ([CUT], {"forge/calibration.md": B1}, "", 1, ["new: CLAUDE.md::Worker%20duties cut"]),
    ([], {"forge/BOOT.md": None, "forge/PRINCIPLES.md": BOOT}, "", 0, ["!new:"]),
    ([], {"forge/BOOT.md": None, "forge/calibration.md": BOOT}, "", 1, ["new: FR-9"]),
    ([("Copper walrus sings; amber ferret naps.\nBasalt", "Copper walrus\nsings; amber ferret naps. Basalt")], {}, "", 0, ["!new:"]),
    ([("\nBasalt heron flies.", "")], {}, "", 1, ['cut "Basalt heron flies."']),
    ([("Copper walrus sings; amber", "Amber")], {}, "", 1, ['cut "Copper walrus sings;"', "1 fragments"]),
    ([(J, "- Alfa bravo charlie delta echo. Foxtrot golf hotel india juliet.\n")], {}, "", 0, ["!new:", "!paired"]),
    ([("- Quartz lynx sleeps.\n", "")], {}, "", 0, ["cuts: 0 fragments"]),
    ([("## Worker duties", "## Duties of workers"), ("(case: FR-7)", "(case: FR-70)")], {}, "", 0, ["!new:"]),
    ([(J, "- Alfa bravo charlie delta echo foxtrot kilo lima mike november.\n")], {}, "", 0,
     ['paired: CLAUDE.md::Worker%20duties "- Alfa', "(0.60)"]),
    ([LOW], {}, "", 1, ['cut "- Alfa bravo charlie delta echo foxtrot']),
    ([LOW], {}, 'rule-reworded: "golf hotel india" -- "kilo lima mike"', 0, ['reworded (by line): "golf hotel india" -> "kilo']),
    ([LOW], {}, 'rule-reworded: "golf hotel india" -- "velvet thistle opens"', 1, ["not read: new gist names no new text"]),
    ([(CYR, "")], {}, 'rule-cut: "%s" -- W-1' % CYR[10:-2].casefold(), 0, ["1 covered"]),
    ([(CYR, CYR.replace("ло ", "ла "))], {}, "", 0, ["!new:"]),
    ([("3600 seconds", "7200 seconds")], {}, "", 1, ['cut "- Wait caps stay 3600 seconds firmly."']),
])
def test_kept(roots, subs, extra, log, code, has):
    c, o = core(roots, subs, extra, log)
    assert c == code and holds(o, has), o


@pytest.fixture(scope="module")
def repo(tmp_path_factory):
    """One repository: (root, shas, checkout(i)); commit 7 is on a side branch merged by commit 9 (t-1992 N6's form)."""
    g = str(tmp_path_factory.mktemp("g"))
    sh = lambda *a: subprocess.run(["git", "-C", g, "-c", "user.name=t", "-c", "user.email=t@t"] + list(a),
                                   capture_output=True).stdout.decode().strip()
    sh("init", "-q")
    cut, x1, shas, at = CLAUDE.replace(B1, ""), {"forge/tools/x.py": "x = 1\n"}, [], [None]
    nocarry = {"CLAUDE.md": CLAUDE.replace(*CARRY)}
    lose = json.dumps(dict(CFG, files=CFG["files"][:-1]))
    for i, (msg, files) in enumerate([
            ("empty", {}), ("start", {**BASE, **x1, REGF: json.dumps({"schema": "words/2", "records": RECS}), rc.REL: CFG_TEXT}),
            ("m", {"CLAUDE.md": cut}), ("m", BASE), (GL % "W-1", {}), ("m", {"CLAUDE.md": cut}), (GL % "W-1", {}),
            ('rule-cut: "Marble otter guards" -- W-1', {"CLAUDE.md": cut.replace(B2, "")}), ("m", {"forge/tools/x.py": "x = 2\n"}),
            ("merge", None), ("rule-to-code: FR-7 -- forge/tools/x.py", {**nocarry, **x1}), ("m", {"CLAUDE.md": cut}),
            ("rule-to-code: FR-7 -- forge/tools/x.py", nocarry), ("m", {"CLAUDE.md": b"\xff\xfe# x\n"}), ("m", {"CLAUDE.md": cut}),
            ("m", {rc.REL: lose}), ("ratchet-raise: rule-cuts.json files -- W-1", {rc.REL: CFG_TEXT})]):
        sh("checkout", "-q", "-b", "side") if i == 7 else sh("checkout", "-q", "-") if i == 8 else None
        if files is None:
            sh("merge", "-q", "--no-ff", "-m", msg, "side")
            shas.append(sh("rev-parse", "HEAD"))
            continue
        put(g, files)
        sh("add", "-A") if i == 1 else None  # later steps change tracked files only: -a (fewer processes)
        shas.append(re.search(r" ([0-9a-f]{7,})\]", sh("commit", "-a", "--allow-empty", "--no-verify", "-m", msg)).group(1))

    def checkout(i):  # rows are ordered by head: a checkout only when the head changes
        if at[0] != i:
            sh("checkout", "-q", shas[i])
            at[0] = i
    return g, shas, checkout


# expected from: t-2070 2.2 (committed trees, the lines of base..HEAD), 2.5 (a config key needs ratchet-raise, born), 3
# (rule-to-code: a tool file changed in the range), E14-E22, E36, K7-K9, T31-T34, T38-T41
@pytest.mark.parametrize("head, base, code, has", [
    (0, None, 2, ["absent at HEAD"]),
    (1, 0, 0, ["born: "]),
    (3, 1, 0, ["!new:"]),
    (5, 4, 1, ["new: CLAUDE.md::Worker%20duties cut"]),
    (6, 4, 0, ["1 covered", "!new:"]),
    (9, 8, 0, ["1 covered", "!new:"]),
    (10, 9, 0, ["to code (by line): FR-7 -> forge/tools/x.py", "!new:"]),
    (12, 11, 1, ["not read: forge/tools/x.py is no tool or hook file changed", "new: FR-7"]),
    (14, 13, 2, [":CLAUDE.md: not UTF-8"]),
    (15, 14, 1, ["new: forge/rule-cuts.json::files key changed needs `ratchet-raise: rule-cuts.json files"]),
    (16, 15, 0, ["!new:"]),
    (16, None, 0, ["cuts not judged: no base"]),
    (16, "nope", 2, ["not a commit"]),
    (16, 16, 0, ["cuts: 0 fragments, 0 ids gone"]),
])
def test_range(repo, head, base, code, has):
    g, shas, checkout = repo
    checkout(head)
    buf = StringIO()
    with redirect_stdout(buf):
        c = rc.main(["--root", g] + (["--base", shas[base] if isinstance(base, int) else base] if base is not None else []))
    assert c == code and holds(buf.getvalue(), has), buf.getvalue()


# expected from: t-2070 2.2 step 1 and 2.5 (a malformed config is exit 2); I3 (a config base that is no object refuses)
@pytest.mark.parametrize("raw", [b"{not json", b"\xff", json.dumps(dict(CFG, keep=0)).encode(), b"[]"])
def test_config(raw):
    with pytest.raises(ratchets.Refuse):
        rc.config_of(raw)
