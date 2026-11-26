# Hand-back t-3104 (builder)

Done:
1. snapshot.py: rejects(root) collects the reject lines of logs/journal/*.jsonl and prints the last 5 as `<task> <agent>: <note>`; the agent is the line's `agent` field, the same field the old journal carried and retro's role counts read. The section has its own guard. DONE, forge/tools/snapshot.py
2. test_snapshot_rejects: 7 rejects -> the last 5; no reject -> `none`. DONE, forge/tests/test_token_tools.py

Witness:
```
$ python -m pytest forge/tests/test_token_tools.py -q -k snapshot
.........                                                                [100%]
9 passed, 138 deselected in 2.31s
```

Deviations from the spec: none.
