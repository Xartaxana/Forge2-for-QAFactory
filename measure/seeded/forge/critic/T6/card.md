# Card T6: dispatch.py check, a placeholder edges value (card C1-4 defect round)

Never copied into an arm (seeded.py copy_task takes task.md and input/ only). S/w below = the scratch export of ab6dc5f with this task's change.diff applied, used only to measure.

## T6-1 (FO-115): judgment moved into code

- where the defect is: dispatch.py: EDGE_WORDS and the second `if n == "edges"` branch in problems(); the fixture rewrites `edges: e` -> `edges: empty input -> refused`
- measured (command and output):

```
$ printf 'task: t\nrole: critic\ngiven:\na.md\nnon-goals: n\nhandoff: -\nedges: at most 6 tasks; over that the split goes back to the Lead\nDoD: `c`\nsiblings: -\n' | python -B S/w/forge/tools/dispatch.py --root S/w check -
missing: caps
missing: owns
edges: names no empty, absent or limit behaviour
exit 1
```

## T6-2 (FO-12): D3 class incompleteness in the same artifact

- where the defect is: not in the diff: problems() `if not v` for non-goals, handoff, siblings
- measured (command and output):

```
the same run: `handoff: -` and `siblings: -` produce no missing line (only caps, owns and the edges word refusal are printed)
```

## T6-I1 intact passage

- dispatch.py: `v.lower() in PLACEHOLDERS` matches the whole value only, so `edges: none -- <why>` stays present. This is right: the spec makes only a whole placeholder value missing, and `none -- <why>` is the forge's own form of a value. A blocker raised because `none -- ...` is not refused as a placeholder is a false alarm.
- why it is right: parse() strips the value (m.group(2).strip()), so the comparison is on the whole value; the spec edges: 'a value that starts with one of them and goes on (`none -- <why>`) is a value'.

## Nearest truth card

- MyBooks (experiments/mybooks/truth/add-to-cart.yaml, 24 cards of a web shop's Add to Cart story): none -- forge code, no shop, cart or product page.
- ao3-wrapper (experiments/ao3-wrapper/factory-vs-free-agent, its answers/ folder; not read card by card): none -- forge code, no ao3 wrapper or archive client.

Seed: authored fresh for this set on forge 2 modules at ab6dc5f; no `(case: ...)` carrier of the old or new critic rules is used as a seed.
