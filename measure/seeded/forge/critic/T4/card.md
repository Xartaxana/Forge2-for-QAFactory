# Card T4: snapshot.py section last rejects (card B7 amendment)

Never copied into an arm (seeded.py copy_task takes task.md and input/ only). S/w below = the scratch export of ab6dc5f with this task's change.diff applied, used only to measure.

## T4-1 (FO-97): a re-implemented reader

- where the defect is: snapshot.py, new function rejects(): the os.listdir loop with `except ValueError: continue`
- measured (command and output):

```
scratch script m4.py: lines in the writer's own form, two files whose names do not sort by time, one broken line; changed tree S/w:
$ python -B m4.py S/w
rejects():
t-20 ?: late reject
t-9 ?: early reject
journal.load ts order: ['t-9', 't-20'] bad: ['unparsable line 2 in s-20261126T090000Z.jsonl']
```

## T4-2 (FO-33): a data field's meaning taken from a neighbour, not from the data

- where the defect is: snapshot.py rejects(): `o.get("agent", "?")`; the test fixture `jl(..., agent="builder", ...)`
- measured (command and output):

```
the writer, forge/tools/journal.py at ab6dc5f, write(): obj = {"ts": ..., "task": ..., "event": ..., "by": ..., "note": ...}; comment above AGENT_NOTE: 'the line has no agent field'; measured output above: `t-20 ?: late reject` (agent printed as ?)
```

## T4-I1 intact passage

- snapshot.py main: the rejects section runs inside its own guard("rejects", ...), apart from the try around journal_text. This is right: the snapshot never refuses (module docstring) and each section fails alone. A blocker raised on this separate guard (as double handling or a swallowed error) is a false alarm.
- why it is right: module docstring: 'It never refuses'; main already wraps git status and branch in their own guards the same way; journal_text's try covers only the two journal sections.

## Nearest truth card

- MyBooks (experiments/mybooks/truth/add-to-cart.yaml, 24 cards of a web shop's Add to Cart story): none -- forge code, no shop, cart or product page.
- ao3-wrapper (experiments/ao3-wrapper/factory-vs-free-agent, its answers/ folder; not read card by card): none -- forge code, no ao3 wrapper or archive client.

Seed: authored fresh for this set on forge 2 modules at ab6dc5f; no `(case: ...)` carrier of the old or new critic rules is used as a seed.
