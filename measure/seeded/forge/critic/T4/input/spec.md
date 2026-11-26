# Dispatch (card B7 amendment): snapshot.py section `last rejects`

task: t-3104
given: forge/tools/snapshot.py, forge/tools/journal.py, forge/tests/test_token_tools.py
owns: forge/tools/snapshot.py, forge/tests/test_token_tools.py
non-goals: no change to journal.py or to the other snapshot sections
handoff: the report with the DoD run's output
edges: no reject line -> the section says `none`; fewer than 5 -> all of them; the section is the 5 most recent rejects across all session files, oldest first; a journal problem never stops the snapshot (it never refuses) and is shown, not hidden
DoD: `python -m pytest forge/tests/test_token_tools.py -q -k snapshot`
siblings: none -- the snapshot file is read by the next session only
test: forge/tests/test_token_tools.py, a new parameterised test | expected from: this card

Why: after a compaction the next session reads the snapshot first; the work that came back (rejects) should be on it.

Change: a section `## last rejects` after `## last 20 journal lines`: one line per reject, `<task> <agent>: <note>`, where agent is the worker the reject sent back.
