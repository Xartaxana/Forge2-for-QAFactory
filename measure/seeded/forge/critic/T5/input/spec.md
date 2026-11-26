# Dispatch (card B14 amendment): words.py caps the size of `asked`

task: t-3105
given: forge/tools/words.py, forge/tests/test_words.py
owns: forge/tools/words.py, forge/tests/test_words.py
non-goals: no change to the registry file, to check, or to the words cap itself
handoff: the report with the DoD run's output; any red explained with its evidence
edges: an asked over WORDS_MAX bytes of UTF-8 is refused with a named message; exactly WORDS_MAX bytes is accepted; an empty or missing asked keeps its one existing message
DoD: `python -m pytest forge/tests/test_words.py -q`
siblings: none named
test: forge/tests/test_words.py::test_add, rows of the BAD table | expected from: this card

Reason: a record whose `asked` held a whole pasted chat (41 000 bytes) was accepted by `words.py add`; the registry is read whole by every `check` and every session start.
Fix: `asked` over WORDS_MAX bytes of UTF-8 is refused, the message in the form of the words cap: `asked is <n> bytes, over 8192; ...`.
