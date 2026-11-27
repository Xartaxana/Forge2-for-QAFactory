# card: B13
"""Tests of refs.py (B13, amended by B15, B16, B20): ONE table, strongest first, a fixture repository per row.
Columns: files (None deletes a default; "@base" = (files, cfg) committed before the row's world, "@env" = environment),
cfg (merged over CFG), args, expected exit, text the output must hold. A bad reference is assembled at run time."""
import hashlib
import json
import os
import subprocess
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
import refs  # noqa: E402

LR = "part" + "2:126"  # a line reference, built at run time
P3, P9 = "part" + "3:9", "part" + "9:1"
ALLOW = {"file": "rules/r.md", "token": "example.com:8080", "reason": "a host"}
CFG = {"scan": [{"glob": "forge/specs/*.md"}, {"glob": "rules/*.md"}, {"glob": "AGENTS.md"}], "line_ok": [{"glob": "logs/journal/*.jsonl"}],
       "code_kinds": [{"glob": "**/*.py", "comment": "#"}, {"glob": "**/*.mjs", "comment": "//"}], "card_id": "A<n> | B<n> | C<d>-<n>", "line_ref_aliases": ["part2", "part3", "part9"],
       "path_scan": ["rules/*.md"], "path_suffixes": [".md", ".py"], "local_roots": ["C:/Other/repo"]}
PLAN = "forge/specs/20261125-forge2-light-factory-plan.md"
SPEC = "### B1 one\n- owns: forge/tools/a.py\n### B2 two\n"
sha = lambda text: hashlib.sha256(text.encode()).hexdigest()
SRC = {"forge/specs/SOURCES.md": "| file | sha256 |\n|---|---|\n| c.md | %s |\n" % sha("orig")}


def copy(body, rows, **extra):
    """An edited spec copy c.md (its bytes differ from the recorded sha) with the legacy rows `rows`."""
    return dict({"forge/specs/c.md": "### B3 c\n" + body, **SRC}, **extra), {"legacy": [{"file": "forge/specs/c.md", "tokens": r, "reason": "t"}
                                                                                       for r in rows]}


BASE = copy("%s %s\n" % (LR, P3), [[LR]])  # the base: one legacy token, both references written
HEAD = copy("%s %s\n" % (LR, P3), [[LR, P3]])
STUB = "# card: B1\nimport sys\n"
ROWS = [
    # card K4 `check --base` and the ci.py road: FORGE_BASE is read as every base job reads it (t-2104 F1: it was ignored)
    (dict(HEAD[0], **{"@base": BASE, "@env": {"FORGE_BASE": "HEAD"}}), HEAD[1], ["check"], 1, "gains token " + P3),
    (dict(HEAD[0], **{"@base": BASE}), HEAD[1], ["check", "--base", "HEAD"], 1, "gains token " + P3),
    (dict(HEAD[0], **{"@base": BASE}), HEAD[1], ["check", "--base", "nope"], 2, "base nope: not a commit"),
    (dict(copy(LR + "\n", [[LR]])[0], **{"@base": BASE}), copy(LR, [[LR]])[1], ["check", "--base", "HEAD"], 0, "green"),  # a row losing a token
    (dict(HEAD[0], **{"@base": ({**copy(LR, [])[0], "forge/refs.json": None}, {})}), HEAD[1], ["check", "--base", "HEAD"], 1, "new legacy row lists"),
    (dict(HEAD[0], **{"@base": BASE}), HEAD[1], ["legacy", "forge/specs/c.md", "--base", "HEAD"], 0, LR),
    (copy("old " + LR + "\n", [[LR]])[0], copy("", [[LR]])[1], ["check"], 0, "legacy rows not judged against a base"),
    # card K4 / AR-20: a new token is red, an old one never blocks, a swap is red, an edited copy with no row is red
    (copy("one " + LR + " and new " + P3 + "\n", [[LR]])[0], copy("", [[LR]])[1], ["check"], 1, "new line reference"),
    (copy("swapped " + P3 + "\n", [[LR]])[0], copy("", [[LR]])[1], ["check"], 1, "new line reference"),
    (copy("old B77\n", [["B77"]])[0], copy("", [["B77"]])[1], ["check"], 0, "green"),
    (copy("new B78\n", [["B77"]])[0], copy("", [["B77"]])[1], ["check"], 1, "unresolved id: card id B78"),
    (copy("old " + LR + "\n", [])[0], {}, ["check"], 1, "legacy forge/specs/c.md --base"),
    # B20: ONE allow-list rule (judge_list): dead scanner exit 2 before stale; stale red; no reason red (t-2104 F4)
    ({"rules/r.md": "B99 fine\n"}, {"scan": [{"glob": "nomatch/*.md"}], "allow": [ALLOW]}, ["check"], 2, "scanner found nothing"),
    ({"rules/r.md": "B99 fine\n"}, {"allow": [ALLOW]}, ["check"], 1, "stale: rules/r.md::example.com:8080"),
    ({"rules/r.md": "example.com:8080\n"}, {"allow": [dict(ALLOW, reason="")]}, ["check"], 1, "row has no reason"),
    ({"rules/r.md": "example.com:8080\n"}, {"allow": [ALLOW]}, ["check"], 0, "green"),
    # card K1, K2, K6 and edges: a key not found exactly once is red; a broken key is red
    ({"rules/r.md": "cites B99\n"}, {}, ["check"], 1, "rules/r.md:1: card id B99 has no heading"),
    ({"rules/r.md": "B2\n", "forge/specs/t.md": "### B2 again\n"}, {}, ["check"], 1, "forge/specs/s.md, forge/specs/t.md"),
    ({"rules/r.md": "cites B1 and B2 plan 3.1 and plan 3\n"}, {}, ["check"], 0, "green"),
    ({"rules/r.md": "cites plan 3.2\n"}, {}, ["check"], 1, "plan 3.2"),
    ({"rules/r.md": "cites L-7\n"}, {}, ["check"], 1, "cannot resolve L-7: no work list"),
    ({"rules/r.md": "cites L-7\n", "forge/worklist.yaml": "x\n", "forge/tools/worklist.py": STUB + "print('L-7')\n"}, {}, ["check"], 0, "green"),
    ({"rules/r.md": "cites L-8\n", "forge/worklist.yaml": "x\n", "forge/tools/worklist.py": STUB + "print('L-7')\n"}, {}, ["check"], 1, "L-8: not in the list"),
    ({"rules/r.md": "cites L-7\n", "forge/worklist.yaml": "x\n", "forge/tools/worklist.py": STUB + "sys.exit(3)\n"}, {}, ["check"], 2, "worklist.yaml unreadable"),
    # card K2: line references (an alias for every spec file present, read from the folder: t-2104 F3)
    ({"rules/r.md": "see part4b-2:45 and part5:38-49\n", "forge/specs/20261125-x-spec-part4b-2.md": "x\n", "forge/specs/20261125-x-spec-part5.md": "x\n"},
     {}, ["check"], 1, "line reference part4b-2:45"),
    ({"rules/r.md": "see part8:1\n"}, {}, ["check"], 0, "green"),
    ({"rules/r.md": "see " + LR + " and README.md:12\n", "forge/specs/20261125-x-spec-part2.md": "x\n"}, {}, ["check"], 1, LR),
    ({"rules/r.md": "see example.com:8080\n"}, {}, ["check"], 1, "example.com:8080"),
    ({"rules/r.md": "at 22:20 ~21:38 C:/QAFactory https://example.com:8080 sha256:abc fr:A14\n"}, {}, ["check"], 0, "green"),
    ({"rules/r.md": "see logs/journal/s1.jsonl:4\n"}, {}, ["check"], 0, "green"),
    # card K3 card lines: missing red, absent card red, shebang may precede, empty exempt, the widened remark forms (F9 b)
    ({"t.py": "x = 1\n"}, {}, ["check"], 1, "t.py: no `# card: <id>` line"),
    ({"t.py": "# card: B99\n"}, {}, ["check"], 1, "card line names B99: no heading"),
    ({"t.py": "#!/usr/bin/python\n# card: B1\n"}, {}, ["check"], 0, "green"),
    ({"t.py": ""}, {}, ["check"], 0, "green"),
    ({"t.mjs": "// card: B2, B1\n"}, {}, ["check"], 0, "green"),
    ({"t.py": "# card: B1 (amends B2)\n"}, {}, ["check"], 0, "green"),
    ({"t.py": "# card: B1 B2\n"}, {}, ["check"], 1, "no `# card: <id>` line"),
    # the card_id row is read and used (t-2104 F6): a form it admits passes, a form it does not admit is exit 2
    ({"t.py": "# card: S1-2\n", "forge/specs/t.md": "### S1-2 x\n"}, {"card_id": "A<n> | B<n> | S<d>-<n>"}, ["check"], 0, "green"),
    ({"t.py": "# card: B1\n"}, {"card_id": "nonsense"}, ["check"], 2, "card_id"),
    # card K5 `cards`: a card with code owns and no file naming it, widened owns lines too (F5); never red
    ({"t.py": "# card: B2\n"}, {}, ["cards"], 0, "not built: B1"),
    ({"forge/specs/t.md": "### B5 five\n- owns (inside accepted cards): forge/tools/five.py\n"}, {}, ["cards"], 0, "not built: B1, B5"),
    # card edges: unreadable inputs are exit 2, naming the input (absent plan copy, refs.json, SOURCES.md, no headings, encoding)
    ({"rules/r.md": "plan 3.1\n", PLAN: None}, {}, ["check"], 2, "rules/r.md"),
    ({"forge/refs.json": "{"}, {}, ["check"], 2, "forge/refs.json"),
    ({"forge/specs/SOURCES.md": "| file | sha256 |\n|--|--|\n| c.md | nothex |\n"}, {}, ["check"], 2, "forge/specs/SOURCES.md"),
    ({"forge/specs/s.md": "no cards\n"}, {}, ["check"], 2, "no card heading"),
    ({"rules/r.md": b"\xff\xfe\n"}, {}, ["check"], 2, "rules/r.md: not UTF-8"),
    # a frozen copy is exempt (its bytes match the recorded sha)
    ({"forge/specs/c.md": "### B3 c\n" + LR + "\n", "forge/specs/SOURCES.md": "| file | sha256 |\n|--|--|\n| c.md | %s |\n" % sha("### B3 c\n" + LR + "\n")},
     {}, ["check"], 0, "green"),
    # B16 class (4) and B20 class (5) with their edges
    ({"AGENTS.md": "# P\n- `rules/r.md`: rules\n", "CLAUDE.md": "x\n", "rules/r.md": "ok\n"}, {}, ["check"], 0, "green"),
    ({"AGENTS.md": "# P\nWorkers must obey.\n", "CLAUDE.md": "x\n"}, {}, ["check"], 1, "holds text, not a pointer"),
    ({"AGENTS.md": "# P\n- `rules/none.md`: gone\n", "CLAUDE.md": "x\n"}, {}, ["check"], 1, "does not exist"),
    ({"CLAUDE.md": "x\n"}, {}, ["check"], 1, "AGENTS.md: absent"),
    ({"rules/r.md": "x\n"}, {}, ["check"], 0, "AGENTS.md not judged: no CLAUDE.md"),
    ({"rules/r.md": "`rules/r.md` `forge/specs/s.md` `r.md` `<id>.md` `3.1` `e.g.`\n"}, {}, ["check"], 0, "green"),
    ({"rules/r.md": "`rules/gone.md`\n"}, {}, ["check"], 1, "rules/gone.md"),
    ({"rules/r.md": "`gone.md`\n"}, {}, ["check"], 1, "gone.md"),
    ({"rules/r.md": "`C:/Other/repo/rules/r.md`\n"}, {}, ["check"], 0, "green"),
    ({"rules/r.md": "`D:/Elsewhere/x.md`\n"}, {}, ["check"], 0, "not judged: outside the repository"),
]


def build(tmp, files, cfg):
    for rel, body in files.items():
        if rel.startswith("@"):
            continue
        p = os.path.join(tmp, rel)
        if body is None:
            if os.path.exists(p):
                os.remove(p)
            continue
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "wb") as fh:
            fh.write(body if isinstance(body, bytes) else body.encode())


def world(tmp, files, cfg):
    defaults = {"forge/specs/s.md": SPEC, PLAN: "### 3. Plan\n1. x\n", "forge/refs.json": json.dumps(dict(CFG, **cfg))}
    build(tmp, {**defaults, **files}, cfg)


@pytest.mark.parametrize("files,cfg,args,code,says", ROWS, ids=range(len(ROWS)))
def test_refs(tmp_path, capsys, monkeypatch, files, cfg, args, code, says):
    root = str(tmp_path)
    monkeypatch.delenv("FORGE_BASE", raising=False)
    for k, v in files.get("@env", {}).items():
        monkeypatch.setenv(k, v)
    if "@base" in files:
        world(root, files["@base"][0], files["@base"][1])
        git = lambda *a: subprocess.run(["git", "-C", root, "-c", "user.name=t", "-c", "user.email=t@t"] + list(a), check=True, capture_output=True)
        git("init", "-q")
        git("add", "-A")
        git("commit", "-qm", "base")
    world(root, files, cfg)
    assert refs.main(["--root", root] + args) == code
    assert says in capsys.readouterr().out
