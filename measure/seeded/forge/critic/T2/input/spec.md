# Dispatch (card C1-4 amendment): journal.load returns Loaded(entries, bad, found, files)

task: t-3102
given: forge/tools/journal.py, forge/tools/retro.py, forge/tests/test_token_tools.py
owns: forge/tools/journal.py, forge/tools/retro.py, forge/tests/test_token_tools.py
non-goals: no new event, no change to the line form or to write()
handoff: the report with the DoD run's output and the list of load()'s callers you updated
edges: an empty session file (no line at all) is a session: today it has no entry, so `retro.py missing` never names it; files is in name order; every caller of load() that unpacks its result is updated in this round (a caller left unpacking three values breaks at once)
DoD: `python -m pytest forge/tests/test_token_tools.py -q`
siblings: every caller of journal.load (find them; the report names each)
test: forge/tests/test_token_tools.py, one new test | expected from: this card

Change: journal.load returns a named tuple Loaded(entries, bad, found, files). entries, bad and found keep their meaning. files is the basename of every .jsonl file load found under logs/journal, in name order: readable or not, empty or not, git-hooks.jsonl included (load reports what it found; each reader filters for itself). retro.py's session list and `retro.py missing` read files, so an empty session file is listed as missing a retro. The test pins files for a journal of s1.jsonl (one line), s2.jsonl (empty) and git-hooks.jsonl (one line): files == ["git-hooks.jsonl", "s1.jsonl", "s2.jsonl"].
