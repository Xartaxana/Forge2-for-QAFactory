# Card T2: journal.load returns Loaded with files (card C1-4 amendment)

Never copied into an arm (seeded.py copy_task takes task.md and input/ only). S/w below = the scratch export of ab6dc5f with this task's change.diff applied, used only to measure.

## T2-1 (FO-29): T-K3 unverified load-bearing negative

- where the defect is: not in the diff: forge/tools/snapshot.py journal_text, the line `entries, bad, _ = loaded` (snapshot.py:56 at ab6dc5f); the false claim is in input/report.md, 'Callers of load()'
- measured (command and output):

```
$ grep -n "journal.load\|entries, bad, _ = loaded" forge/tools/snapshot.py   (at ab6dc5f)
55:    loaded = journal.load(root)
56:    entries, bad, _ = loaded
measured, scratch script m2.py calling snapshot.journal_text on a one-line journal:
base tree (C:/QAFactory/forge2-wt/s11-2): ('t-1', '{"ts":"2026-11-20T10:00:00Z",...}')
changed tree (S/w): journal_text raised: ValueError too many values to unpack (expected 3)
and the full DoD file on the changed tree: `python -B -m pytest forge/tests/test_token_tools.py -q` -> 5 failed, 141 passed (the five test_snapshot rows), while the report's narrowed run gives 91 passed, 55 deselected
```

## T2-2 (FO-86): a test whose expected value matches the code, not the spec

- where the defect is: forge/tests/test_token_tools.py, new test, the assert on .files; journal.py load, the `if name != "git-hooks.jsonl": seen.append(name)` placed after the open
- measured (command and output):

```
spec line: files == ["git-hooks.jsonl", "s1.jsonl", "s2.jsonl"]; the code returns ["s1.jsonl", "s2.jsonl"] (the new test passes on the changed tree: part of the 91 passed above)
```

## T2-I1 intact passage

- retro.py cmd_write: `if loaded.found and session not in sessions(loaded.entries)` passes no files to sessions(). This is right: write counts a session's lines and an empty session file has none, so refusing it ('no journal lines of session') stays correct. A blocker raised because files is not passed here is a false alarm.
- why it is right: cmd_write counts lines of one session; with no lines the old refusal 'refused: no journal lines of session' is the right answer, and files would only make an empty session pass into an empty count.

## Nearest truth card

- MyBooks (experiments/mybooks/truth/add-to-cart.yaml, 24 cards of a web shop's Add to Cart story): none -- forge code, no shop, cart or product page.
- ao3-wrapper (experiments/ao3-wrapper/factory-vs-free-agent, its answers/ folder; not read card by card): none -- forge code, no ao3 wrapper or archive client.

Seed: authored fresh for this set on forge 2 modules at ab6dc5f; no `(case: ...)` carrier of the old or new critic rules is used as a seed.
