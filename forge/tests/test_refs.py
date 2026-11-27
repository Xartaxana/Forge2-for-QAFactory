# card: B13
"""Tests of refs.py (B13, amended by B15, B16, B20): fixture repositories built per row; `expected from:` per table is the
card's test line. A bad reference is assembled at run time, never written as a literal."""
import hashlib
import json
import os
import subprocess
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
import refs  # noqa: E402

LR = "part" + "2:126"  # a line reference, built at run time
CFG = {"scan": [{"glob": "forge/specs/*.md"}, {"glob": "rules/*.md"}, {"glob": "AGENTS.md"}], "line_ok": [{"glob": "logs/journal/*.jsonl"}],
       "code_kinds": [{"glob": "**/*.py", "comment": "#"}, {"glob": "**/*.mjs", "comment": "//"}],
       "path_scan": ["rules/*.md"], "path_suffixes": [".md", ".py"], "local_roots": ["C:/Other/repo"]}
SPEC = "### B1 one\n- owns: forge/tools/a.py\n### B2 two\n"


def make(tmp, files, cfg=None):
    files = {"forge/specs/s.md": SPEC, "forge/specs/20261125-forge2-light-factory-plan.md": "### 3. Plan\n1. x\n",
             "forge/refs.json": json.dumps(dict(CFG, **(cfg or {}))), **files}
    for rel, body in files.items():
        p = os.path.join(tmp, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "wb") as fh:
            fh.write(body if isinstance(body, bytes) else body.encode())
    return str(tmp)


def run(root, *args):
    return refs.main(["--root", root] + (list(args) or ["check"]))


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


# expected from: card keys K1, K2, K6 and its edges (a key not found exactly once is red; a broken key is red)
@pytest.mark.parametrize("body,code,says", [
    ("cites B99\n", 1, "rules/r.md:1: card id B99 has no heading"),
    ("cites B1 and B2\n", 0, "green"),
    ("cites plan 3.1 and plan 3\n", 0, "green"),
    ("cites plan 3.2\n", 1, "plan 3.2"),
    ("cites L-7\n", 1, "cannot resolve L-7: no work list"),
    ("at 22:20 ~21:38 C:/QAFactory https://example.com:8080 sha256:abc fr:A14\n", 0, "green"),
    ("see example.com:8080\n", 1, "example.com:8080"),
    ("see " + LR + " and README.md:12\n", 1, LR),
    ("see logs/journal/s1.jsonl:4\n", 0, "green"),
])
def test_keys_and_line_references(tmp_path, capsys, body, code, says):
    assert run(make(tmp_path, {"rules/r.md": body})) == code
    assert says in capsys.readouterr().out


def test_card_heading_twice_names_both_files(tmp_path, capsys):
    root = make(tmp_path, {"forge/specs/t.md": "### B2 again\n", "rules/r.md": "B2\n"})
    assert run(root) == 1
    assert "forge/specs/s.md, forge/specs/t.md" in capsys.readouterr().out


# expected from: card key K3 (a missing line red, an absent card red, a shebang may precede, an empty file exempt)
@pytest.mark.parametrize("body,code", [("x = 1\n", 1), ("# card: B99\n", 1), ("#!/usr/bin/python\n# card: B1\n", 0),
                                       ("", 0), ("// card: B2, B1\n", 0), ("# card: B1\n", 0)])
def test_card_line(tmp_path, body, code):
    name = "t.mjs" if body.startswith("//") else "t.py"
    assert run(make(tmp_path, {name: body, "rules/r.md": "ok\n"})) == code


# expected from: card key K4 and AR-20 (a new token is always red, an old one never blocks, a row only shrinks)
@pytest.mark.parametrize("text,legacy,code,says", [
    ("old " + LR + "\n", [LR], 0, "green"),
    ("one " + LR + " and new part" + "3:9\n", [LR], 1, "new line reference"),
    ("swapped part" + "3:9\n", [LR], 1, "new line reference"),
    ("old B77\n", ["B77"], 0, "green"),
    ("new B78\n", ["B77"], 1, "unresolved id: card id B78"),
    ("old " + LR + "\n", None, 1, "legacy forge/specs/c.md --base"),
])
def test_edited_copy(tmp_path, capsys, text, legacy, code, says):
    rows = [{"file": "forge/specs/c.md", "tokens": legacy}] if legacy else []
    root = make(tmp_path, {"forge/specs/c.md": "### B3 c\n" + text,
                           "forge/specs/SOURCES.md": "| file | sha256 |\n|---|---|\n| c.md | %s |\n" % sha("orig")},
                {"legacy": rows})
    assert run(root) == code
    assert says in capsys.readouterr().out


def test_frozen_copy_exempt_and_code_in_copy(tmp_path):
    body = "### B3 c\n" + "\n".join(LR for _ in range(3)) + "\n"
    root = make(tmp_path, {"forge/specs/c.md": body, "forge/specs/stand.py": "x\n",
                           "forge/specs/SOURCES.md": "| file | sha256 |\n|--|--|\n| c.md | %s |\n| stand.py (b) | %s |\n" % (sha(body), sha("x\n"))})
    assert run(root) == 0


# expected from: card key K4 `check --base` (row gaining a token red; new row with a token absent from base bytes red;
# row losing a token green; no base -> the named line, exit 0)
def test_base_rows(tmp_path, capsys):
    git = lambda *a: subprocess.run(["git", "-C", str(tmp_path), "-c", "user.name=t", "-c", "user.email=t@t"] + list(a),
                                    check=True, capture_output=True)
    P3, P9 = "part" + "3:9", "part" + "9:1"
    src = {"forge/specs/SOURCES.md": "| file | sha256 |\n|--|--|\n| c.md | %s |\n" % sha("orig")}

    def put(toks, *held):
        make(tmp_path, {"forge/specs/c.md": "### B3 c\n" + " ".join(held) + "\n", **src},
             {"legacy": [{"file": "forge/specs/c.md", "tokens": toks}]})
        return str(tmp_path)
    root = put([LR, P3], LR, P3)
    git("init", "-q")
    git("add", "-A")
    git("commit", "-qm", "base")
    assert run(root, "check") == 0 and "legacy rows not judged against a base" in capsys.readouterr().out
    assert run(root, "legacy", "forge/specs/c.md", "--base", "HEAD") == 0
    assert json.loads(capsys.readouterr().out)["tokens"] == sorted([LR, P3])
    assert run(put([LR], LR), "check", "--base", "HEAD") == 0  # a row losing a token, its text fixed
    assert run(put([LR, P9], LR, P9), "check", "--base", "HEAD") == 1  # a row gaining a token
    assert "gains token " + P9 in capsys.readouterr().out
    git("rm", "-q", "--cached", "forge/refs.json")
    git("commit", "-qm", "no refs.json at this base")
    assert run(put([LR, P9], LR, P9), "check", "--base", "HEAD") == 1  # a new row, a token the base bytes do not hold
    assert "new legacy row lists " + P9 in capsys.readouterr().out


# expected from: card edges (absent plan copy, absent refs.json, unparsable SOURCES.md, no headings, non-UTF-8 -> exit 2) and
# B20 (an allow row that suppresses nothing is red; a row without reason is red)
def test_cannot_judge(tmp_path):
    root = make(tmp_path / "a", {"rules/r.md": "plan 3.1\n"})
    os.remove(os.path.join(root, "forge/specs/20261125-forge2-light-factory-plan.md"))
    assert run(root) == 2
    assert run(make(tmp_path / "b", {"forge/refs.json": "{"})) == 2
    assert run(make(tmp_path / "c", {"forge/specs/SOURCES.md": "| file | sha256 |\n|--|--|\n| c.md | nothex |\n"})) == 2
    assert run(make(tmp_path / "d", {"forge/specs/s.md": "no cards\n"})) == 2
    assert run(make(tmp_path / "e", {"rules/r.md": b"\xff\xfe\n"})) == 2


def test_allow_row_rules(tmp_path, capsys):
    ok = {"file": "rules/r.md", "token": "example.com:8080", "reason": "a host"}
    assert run(make(tmp_path / "a", {"rules/r.md": "example.com:8080\n"}, {"allow": [ok]})) == 0
    assert run(make(tmp_path / "b", {"rules/r.md": "fine\n"}, {"allow": [ok]})) == 1
    assert "stale" in capsys.readouterr().out
    assert run(make(tmp_path / "c", {"rules/r.md": "example.com:8080\n"}, {"allow": [dict(ok, reason="")]})) == 1
    assert "no reason" in capsys.readouterr().out


# expected from: B16 class (4) and its WORLDS line; B20 class (5) and its edges
@pytest.mark.parametrize("files,code,says", [
    ({"AGENTS.md": "# P\n- `rules/r.md`: rules\n", "CLAUDE.md": "x\n", "rules/r.md": "ok\n"}, 0, "green"),
    ({"AGENTS.md": "# P\nWorkers must obey.\n", "CLAUDE.md": "x\n"}, 1, "holds text, not a pointer"),
    ({"AGENTS.md": "# P\n- `rules/none.md`: gone\n", "CLAUDE.md": "x\n"}, 1, "does not exist"),
    ({"CLAUDE.md": "x\n"}, 1, "AGENTS.md: absent"),
    ({"rules/r.md": "x\n"}, 0, "AGENTS.md not judged: no CLAUDE.md"),
    ({"rules/r.md": "`rules/r.md` `forge/specs/s.md` `r.md` `<id>.md` `3.1` `e.g.`\n"}, 0, "green"),
    ({"rules/r.md": "`rules/gone.md`\n"}, 1, "rules/gone.md"),
    ({"rules/r.md": "`gone.md`\n"}, 1, "gone.md"),
    ({"rules/r.md": "`C:/Other/repo/rules/r.md`\n"}, 0, "green"),
    ({"rules/r.md": "`D:/Elsewhere/x.md`\n"}, 0, "not judged: outside the repository"),
])
def test_agents_and_paths(tmp_path, capsys, files, code, says):
    assert run(make(tmp_path, files)) == code
    assert says in capsys.readouterr().out


# expected from: card K5 (`cards` prints a card with code owns and no file naming it; never red); B15 (importable)
def test_cards_prints_unbuilt(tmp_path, capsys):
    root = make(tmp_path, {"t.py": "# card: B2\n"})
    assert run(root, "cards") == 0
    assert capsys.readouterr().out.strip() == "not built: B1"
    assert refs.cards_not_built(root) == ["B1"]
