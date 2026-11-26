# Card T3: size_ratchet.py unit files (card C1-2 amendment)

Never copied into an arm (seeded.py copy_task takes task.md and input/ only). S/w below = the scratch export of ab6dc5f with this task's change.diff applied, used only to measure.

## T3-1 (FO-103): an unnamed ratchet raise

- where the defect is: forge/budgets.json hunk: "forge_code" ceiling 6000 -> 6500, next to the new row
- measured (command and output):

```
$ python -B forge/tools/size_ratchet.py   (C:/QAFactory/forge2-wt/s11-2, base tree)
forge_code: 4077 nonblank_lines (ceiling 6000)
changed tree (S/w): forge_code: 4080 nonblank_lines (ceiling 6500)
```

## T3-2 (FO-83): a test that cannot fail

- where the defect is: forge/tests/test_budgets.py, the first added test_size row
- measured (command and output):

```
scratch script m3.py runs the row's assertions on the changed size_ratchet with measure real and mutated:
real exit 0 row asserts hold: True | forge_tool_files: 2 files (ceiling 20)
mutant measure->0 exit 0 row asserts hold: True | forge_tool_files: 0 files (ceiling 20)
```

## T3-I1 intact passage

- forge/budgets.json: the new row forge_tool_files has ceiling 14, equal to today's count of forge/tools/*.py. This is right: the spec sets the ceiling at today's count and judge_row fails only on value > ceiling, so the tree passes today and every added tool file is red. A blocker calling the ceiling an off-by-one or asking for headroom is a false alarm.
- why it is right: $ git -C C:/QAFactory/forge2-wt/s11-2 ls-tree --name-only ab6dc5f forge/tools/ | grep -c "\.py$"  -> 14; judge_row: `if (value or 0) <= row["ceiling"]: return 0`.

## Nearest truth card

- MyBooks (experiments/mybooks/truth/add-to-cart.yaml, 24 cards of a web shop's Add to Cart story): none -- forge code, no shop, cart or product page.
- ao3-wrapper (experiments/ao3-wrapper/factory-vs-free-agent, its answers/ folder; not read card by card): none -- forge code, no ao3 wrapper or archive client.

Seed: authored fresh for this set on forge 2 modules at ab6dc5f; no `(case: ...)` carrier of the old or new critic rules is used as a seed.
