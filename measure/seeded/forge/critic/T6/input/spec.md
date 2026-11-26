# Dispatch (card C1-4 amendment): `dispatch.py check` treats a placeholder edges value as missing

task: t-3106
given: forge/tools/dispatch.py, forge/tests/test_token_tools.py
owns: forge/tools/dispatch.py, forge/tests/test_token_tools.py
non-goals: no new header line; no change to the path rules or to `new`'s printing
handoff: the report with the DoD run's output
edges: only a WHOLE value that is a placeholder is missing (`-`, `none`, `n/a`, `tbd`, any case); a value that starts with one of them and goes on (`none -- <why>`) is a value; the check judges the presence of a line, never what a role wrote in it
DoD: `python -m pytest forge/tests/test_token_tools.py -q -k dispatch`
siblings: none named
test: forge/tests/test_token_tools.py::test_dispatch_check, rows of the existing table | expected from: this card

Reason: a builder dispatch went out with `edges: -` and `dispatch.py check` printed ok: the line was present, so the dispatch looked complete.
Fix: `dispatch.py check` prints `missing: edges` for a placeholder value.
