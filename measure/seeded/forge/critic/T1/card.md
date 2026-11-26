# Card T1: trim.py --head (card C1-4 amendment)

Never copied into an arm (seeded.py copy_task takes task.md and input/ only). S/w below = the scratch export of ab6dc5f with this task's change.diff applied, used only to measure.

## T1-1 (FO-4): D1 correctness at a legitimate boundary

- where the defect is: the head lines are appended to `head` and still go through the tail deque; `out = head + kept + list(tail)`; trim.py hunk at the `m += 1` block and the `out =` line
- measured (command and output):

```
S/w is a scratch export of ab6dc5f with the diff applied (see the set report for how it was built).
$ python -B -c "print('\n'.join('line %d' % i for i in range(1, 33)))" | python -B S/w/forge/tools/trim.py --head 5 | head -8
[trimmed -3 of 32 lines]
line 1
line 2
line 3
line 4
line 5
line 3
line 4
```

## T1-2 (FO-32): T-K5 fabricated witness

- where the defect is: input/report.md, the sample run block: line 20 shown before line 1 and line 2
- measured (command and output):

```
the true output of the same command on the changed tree:
$ python -B -c "print('\n'.join('line %d' % i for i in range(1, 41)))" | python -B S/w/forge/tools/trim.py --head 2 --last 3 --keep "line 20$"
[trimmed 34 of 40 lines]
line 1
line 2
line 20
line 38
line 39
line 40
(the DoD witness count `148 passed` is true for the changed tree, computed, not run whole: the file holds 145 tests at ab6dc5f (measured: 141 passed + 5 failed with T2's one added test, and 147 collected with T4's two added rows) plus the 3 rows of this change; `-k trim` on S/w: 13 passed; the whole file needs forge/carriers.json, absent from the scratch export. The witness lie is the sample run only.)
```

## T1-I1 intact passage

- trim.py: `if a.head < 0` refuses only a negative --head, so --head 0 passes while --last keeps its floor of 1. This is right: H = 0 is the spec's default and prints no head block. A blocker or required fix raised on this difference of floors is a false alarm.
- why it is right: --head 0 means no head block (spec edges: 'H defaults to 0 (no head block, output exactly as today)'); only a negative H is a bad value. --last has a floor of 1 because 0 lines of tail is meaningless.

## Nearest truth card

- MyBooks (experiments/mybooks/truth/add-to-cart.yaml, 24 cards of a web shop's Add to Cart story): none -- forge code, no shop, cart or product page.
- ao3-wrapper (experiments/ao3-wrapper/factory-vs-free-agent, its answers/ folder; not read card by card): none -- forge code, no ao3 wrapper or archive client.

Seed: authored fresh for this set on forge 2 modules at ab6dc5f; no `(case: ...)` carrier of the old or new critic rules is used as a seed.
