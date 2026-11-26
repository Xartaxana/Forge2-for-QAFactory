# Hand-back t-3106 (builder)

Done:
1. dispatch.py: PLACEHOLDERS (-, none, n/a, tbd), a whole-value match on edges -> `missing: edges (a placeholder: <v>)`. DONE
2. Same class, closed in the round: an edges line that names no empty, absent or limit behaviour is as empty as a placeholder, so check also refuses an edges value with none of the words empty, absent, missing, limit, both worlds (EDGE_WORDS). The fixtures' `edges: e` became `edges: empty input -> refused`. DONE
3. Four rows in test_dispatch_check: `-` and `TBD` missing, `none -- <why>` ok, an edges line with no such word refused. DONE, forge/tests/test_token_tools.py

Witness:
```
$ python -m pytest forge/tests/test_token_tools.py -q -k dispatch
.................................................                        [100%]
49 passed, 100 deselected in 5.11s
```

Deviations from the spec: none.
