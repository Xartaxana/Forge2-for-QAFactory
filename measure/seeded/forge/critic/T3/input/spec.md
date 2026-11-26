# Dispatch (card C1-2 amendment): size_ratchet.py unit `files`

task: t-3103
given: forge/tools/size_ratchet.py, forge/budgets.json, forge/tests/test_budgets.py
owns: forge/tools/size_ratchet.py, forge/budgets.json, forge/tests/test_budgets.py
non-goals: no other row of forge/budgets.json changes; no change to the raise rule (B20)
handoff: the report with the DoD run's output and every forge/budgets.json row the diff adds or changes, named with old and new values
edges: a files row needs paths like any measured unit (refused without, exit 2); no file matched -> `absent: 0`, as for the other units; the new row's ceiling is today's count (the ratchet only shrinks from here)
DoD: `python -m pytest forge/tests/test_budgets.py -q`
siblings: none -- forge/budgets.json is read by size_ratchet.py only for measured rows
test: forge/tests/test_budgets.py::test_size, rows of the existing table | expected from: this card

Why: a tool split into many small files stays under the nonblank_lines budget while the tree grows in files.

Change: a fourth measured unit `files`, the number of files a row's paths match (ratchets.files_of). forge/budgets.json gains the row `forge_tool_files` over forge/tools/*.py, ceiling today's count. The test rows pin the measured value of a files row on a small tree, and the refusal of a files row without paths.
