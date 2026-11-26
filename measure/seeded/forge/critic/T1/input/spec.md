# Dispatch (card C1-4 amendment): trim.py --head H

task: t-3101
given: forge/tools/trim.py, forge/tests/test_token_tools.py
owns: forge/tools/trim.py, forge/tests/test_token_tools.py
non-goals: no change to --keep or --last; no other tool
handoff: the report with the DoD run's output and one sample run of the new flag
edges: H defaults to 0 (no head block, output exactly as today); H below 0 is refused with exit 2, like a bad --last; at or under N lines the text is printed whole, as today; no line is ever printed twice, whatever H, N and --keep; the marker's K stays the number of lines not printed
DoD: `python -m pytest forge/tests/test_token_tools.py -q`
siblings: none -- trim.py has no other reader of its output form
test: forge/tests/test_token_tools.py::test_trim, rows of the existing table | expected from: this card

Why: a long failing run trimmed to its last 30 lines loses the first lines of a traceback, which name the step that failed.

Behaviour: `trim.py --head H` prints, after the marker line, the first H lines of the input, then the kept lines (--keep) in their order, then the last N lines. Order of the output when over N: marker, head lines, kept lines, last N lines.
