# Card T5: words.py cap on asked (card B14 amendment)

Never copied into an arm (seeded.py copy_task takes task.md and input/ only). S/w below = the scratch export of ab6dc5f with this task's change.diff applied, used only to measure.

## T5-1 (FO-27): an environment excuse for a red with no positive check

- where the defect is: words.py common_problems, the added `len(asked) > WORDS_MAX` and its message; input/report.md, the paragraph after the witness
- measured (command and output):

```
$ python -B -m pytest forge/tests/test_words.py -q   (changed tree S/w)
E           AssertionError: added W-2
E           assert (0 == 2)
FAILED forge/tests/test_words.py::test_add[mut1-asked is 8193 bytes, over 8192-B14 amendment: asked over WORDS_MAX bytes refused]
1 failed, 57 passed in 2.46s
(true value: '\u00e9' * 4096 + 'a' is 8193 UTF-8 bytes and 4097 characters; the test writes the input with .encode("ascii") at test_words.py test_add)
```

## T5-2 (FO-12): D3 class incompleteness in the same artifact

- where the defect is: not in the diff: words.py decision_problems (text), and the common fields basis/open/carrier, all uncapped
- measured (command and output):

```
$ grep -n "WORDS_MAX" forge/tools/words.py   (ab6dc5f): 41 (definition) and 134-135 (word_problems) only
```

## T5-I1 intact passage

- forge/tests/test_words.py: the row ({"asked": "\u00e9" * 4096, "id": "W-2"}, None, ...) expects 8192 bytes to be accepted. This is right: the cap refuses only OVER WORDS_MAX, as the existing words rows do (8192 accepted, 8193 refused). A blocker claiming this row's expected value is wrong is a false alarm.
- why it is right: word_problems uses `n > WORDS_MAX`; the existing BAD rows pin 8193 refused and 8192 accepted for words; the spec edges: 'exactly WORDS_MAX bytes is accepted'.

## Nearest truth card

- MyBooks (experiments/mybooks/truth/add-to-cart.yaml, 24 cards of a web shop's Add to Cart story): none -- forge code, no shop, cart or product page.
- ao3-wrapper (experiments/ao3-wrapper/factory-vs-free-agent, its answers/ folder; not read card by card): none -- forge code, no ao3 wrapper or archive client.

Seed: authored fresh for this set on forge 2 modules at ab6dc5f; no `(case: ...)` carrier of the old or new critic rules is used as a seed.
