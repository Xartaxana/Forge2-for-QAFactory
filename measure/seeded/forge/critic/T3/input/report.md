# Hand-back t-3103 (builder)

Done:
1. size_ratchet.py: unit `files` in UNITS, measured as len(files_of(paths)); docstring updated. DONE, forge/tools/size_ratchet.py
2. forge/budgets.json: row forge_tool_files {unit files, paths forge/tools/*.py, ceiling 14} -- 14 is today's count. DONE
3. test_budgets.py: a files row on a two-file tree, and a files row without paths refused. DONE

Witness:
```
$ python -m pytest forge/tests/test_budgets.py -q
....................................................................     [100%]
68 passed in 6.75s

$ python -B forge/tools/size_ratchet.py
rules_worker: 41742 bytes (ceiling 45056)
rules_coordinator: 53234 bytes (ceiling 57344)
boot_page: 3690 bytes (ceiling 4096)
factory_code: absent: 0 (ceiling 6000)
forge_code: 4080 nonblank_lines (ceiling 6500)
forge_tool_files: 14 files (ceiling 14)
plan_spec: 1631536 bytes (ceiling 1700000)
gate_rules: absent: 0 (ceiling 45)
stage_start_load: not set: first measured run (F9)
crap_limit: limit 20 (read by its tool)
raises not judged: no base
tests: 2423 lines, product: 5078 lines (ratio 0.48)
```

Rows of forge/budgets.json added or changed: forge_tool_files (new, ceiling 14).

Deviations from the spec: none.
