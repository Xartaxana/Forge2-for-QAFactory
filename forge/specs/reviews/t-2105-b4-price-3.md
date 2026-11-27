# t-2105 -- critic re-review 3, fix diff b94ad77..2d47674 (worktree C:/QAFactory/forge2-wt/t-2105, HEAD 2d47674)

verdict: blocker -- F10-F14 fixed; 3 new blocking findings (F15 magnitude and sign of a rate, F16 an unknown non-launch line stops --run, F17 a false writer comment), 1 non-blocking node proposal (F18); failure_class: capability

## Verdict lines
- F10: fixed: price.py::DATE + day() (real date, fullmatch, ASCII), at_day() refuses any other `at` (compute and run_report), pick compares `_date`, add_rate refuses tariff_date and prompt_over (positive()), NUMBER has re.ASCII. Re-measured: `2026-6-1`, `--prompt-over -5`, `--in ٣`/`３` are refused and the file keeps 2 lines; `at=2026-10-01` over rows 01-01 + 06-01 -> 24.0 (06-01 row), `at=2026-05-31` -> 18.0. Rows: test_add_rate_refuses_what_its_reader_misreads (15), test_per_model_and_at (`2026-1-15`)
- F11: fixed: add_event carries an unknown field as None -> `agent c: unmeasured: unknown token field cache_write_5m of m-a` (re-measured, all three groups); objects() turns a torn or non-object line into Refuse `<file>:<n>`. A new defect came in with the group-key check: F16
- F12: fixed: `head = []`, opened only if the file exists; re-measured in a fresh git world: deleted head file -> the base row named (was FileNotFoundError); row at the end of test_writer_and_ratchet
- F13: fixed: one git world (test_check_base merged in), args_of used by the writer test, the control `in=1.5` read-back runs once
- F14: fixed: add_rate raises ratchets.Refuse; CLI `--run . --at 2026/01/01` -> `refused: ...`, rc 2
- blank runs.jsonl line refused, journal blanks skipped (builder's note, asked to judge): fit -- a refusal naming file:line, never a price. The only writer, measure/tools/seeded.py::append (414-417), writes `json.dumps(row) + "\n"` per row and never a blank line (real file measure/runs/forge-roles/critic/20261126/runs.jsonl: 44 lines, 0 blank). Two notes: the dispatch edge the builder cites is not in the journal (searched the session journal for t-2105 + blank: only the dispatch notes, no text), so the claim is unverified; the store's other reader, seeded.read_jsonl, skips blanks -- two readers of one store disagree (F18)
- row_why for hand-written rows (builder's sibling): fit_with_fixes -- right place, but it skips the sign and magnitude of a rate (F15)
- seeded.py::read_jsonl analog left outside owns: right call for this node; the convergence is proposed node t-2105-n3 (F18)
- measure/tools/price.py: blocker -- F15, F16, F17
- measure/rates.yaml: fit (header: prompt_over a positive integer)
- TESTS (Q5): fit_with_fixes -- 48 rows green; rows needed for F15 and F16 (one row each in the existing tables). Mutants checked by reading the code: dropping re.ASCII, the day() or positive() guard in add_rate, or the F12 guard each turns a row red (the `٣` row fails with JSONDecodeError, not Refuse). pick by string instead of by date is an equivalent mutant now that DATE is enforced on both sides
- DUPLICATION AND CONSISTENCY: F18 (third jsonl line reader: forge/tools/journal.py::load 59-87, measure/tools/seeded.py::read_jsonl 396-403, price.py::objects); inside the diff add_rate's own day()/positive() checks repeat row_why's, and they go away when the F15 fix reads back through row_why; tokenizer: n/a; refusal text: one road now (Refuse); path resolver: ROOT from `__file__`, unchanged
- CODE QUALITY: F17 (false comment); nesting: objects 3 levels, row_why 1; no function over 60 lines; no dead branch found (F12's `else []` gone)
- ONE ROAD (Q12): fit -- no model, provider or language name added
- VARIETY: blocker -- F16 (an unknown shape in a line nothing prices stops the whole --run report)
- AR-n naming: fit -- commit 2d47674 names AR-14, AR-20 (round-2 note closed), AR-27/AR-28. Its AR-14 sentence "the one writer writes only what reads back" claims more than the body does: the read-back is json.loads, not the reader (F15)
- ratchet rows raised: none (ci-jobs.json untouched)
- class completeness: walked magnitude (huge int and float rates, prompt_over, harness_cost), sign, date form and type of `at`, blank/CRLF/torn/non-object lines in both stores, list-valued keys in launch and non-launch lines, a head file deleted in check. Round 2's walk covered encoding forms only and missed magnitude; it is walked here (F15)
- probe: none -- forge 2 has no mutation runner with `--root` (tool: none yet; searched forge/tools for `restore-mismatch`, no hit), and the dispatch forbids edits

## Findings

F15 (blocks; surface: the number contract of a rate, writer and reader) price.py::figure, ::row_why, ::add_rate (the `json.loads(line[1:])` read-back). Measured:
(a) `add-rate --in <400 digits>` passes NUMBER and the json read-back, so the row is appended (3 lines). After that every read_rows/compute dies with `OverflowError: int too large to convert to float`: math.isfinite turns the int into a float.
(b) `--in <400 digits>.0` is appended too, then every read gives `Refuse w.yaml:3: rate in is not a number`. Either way the append-only file is poisoned by its one writer, which is F1/F10's class on the magnitude axis.
(c) runs.jsonl `"harness_cost": <10**400 int>` -> compute raises OverflowError (traceback, not one source).
(d) A hand-appended row `"in": -3.0` passes row_why and check, which only guards base rows: priced `12.0 USD`. The writer refuses `-3`, the reader takes it.
Fix: `figure(v)` = int/float, not bool, `math.isfinite(float(v))` inside `try/except OverflowError: False`; row_why demands `figure(v) and v >= 0` for KINDS; add_rate's read-back is `why = row_why(json.loads(line[1:]))` and refuses on `why`. That is one check for writer and reader (AR-14 as stated), and add_rate's own day()/positive() lines may then go. Rows: `("in", "1"*400)` in test_add_rate_refuses_what_its_reader_misreads, a `-3.0` hand row in test_broken_line_is_a_refusal_naming_it, harness `10**400` -> one source in test_two_sources.

F16 (blocks, VARIETY; a pair check not scoped to its carrier) price.py::objects (250-265). Any line of either store with a list or dict in agent/stage/story/model is refused, whatever its event. Only a launch's keys are used as group keys, and runs.jsonl rows are never grouped. Measured: a journal with one good launch + `{"event": "note", "agent": ["x"]}` -> `Refuse journal.jsonl:2`, no report. The factory journal form is not fixed yet (C4-6, round-1 F6), so the shape of non-launch lines is unknown. Real data checked: 42 lines of the exp-fvf fixture journals and 44 real runs.jsonl rows, no such key, so this is a latent stop, not a measured one. Fix: objects() checks only "a JSON object"; the key check moves to journal_groups for `event == "launch"` lines (refusal naming file:line there). Add a non-launch line with `"agent": ["x"]` to test_run_report's fixture journal; the asserted output stays the same.

F17 (blocks merge, code quality: false comment) price.py::run_report, line 286: `runs.jsonl has one writer (arm.py)`. arm.py::emit (168-172) only prints a row and writes run.json. runs.jsonl is written by measure/tools/seeded.py::append (414-417), called from seeded.record (424). Fix: name seeded.py::append.

F18 (non-blocking; proposed node t-2105-n3, owner the Lead, executor a builder owning forge/tools + measure/tools/seeded.py) One jsonl line reader. It should return (file, line, object) or Refuse `<file>:<n>`, with one blank-line policy per store. Today three exist: forge/tools/journal.py::load (skips blanks, collects bad lines), measure/tools/seeded.py::read_jsonl (skips blanks, refuses with no line number, no object check) and price.py::objects (refuses a blank runs.jsonl line). seeded and price read the same runs.jsonl under different blank rules. Not this node's owns, so it is not a fix for this round.

## Seam and class notes
- B12 seam (proposed node t-2105-n1, owner the Lead) still stands. Real runs.jsonl tokens use harness keys (`inputTokens`, `cacheCreationInputTokens`, ...): `price.py --run measure/runs/forge-roles/critic/20261126` -> `run 0: unmeasured: unknown token field inputTokens of claude-opus-5-5`. That is the right direction (never a price); the mapping to KINDS belongs to band.py / n1.
- t-2105-n2 (C0-4 `mixed:` producer) unchanged.
- When two unknown token fields are present, the one named depends on set order (`aa` named here). Either name is a correct `unmeasured`; noted, no fix.

## Spot-checks (money: control values re-run at 2d47674 with the round-1 script, by-hand values unchanged)
- 18.05 yes; 18.5 no (from 18.0 to 18.5); 18.10 yes; 17.90 yes; 18.1000001 no; cache_read d=2: 18.405 yes, 18.4051 no (tol 0.10 / 0.105, as by hand)
- 1h write 5, no 1h rate -> `unmeasured: no rate for m-a (cache_write_1h)`; 1h write 0 -> 18.0; bucket 200000 -> m-a, 200001 -> m-a>200000, fast 300000 -> unmeasured; long 1M -> 21.0
- harness `unmeasured: x`, `{amount:"unmeasured: x"}`, True, NaN, inf -> one source; 0 -> no, from 0.0 to 18.0; no currency -> not comparable; key None -> no model named; float count -> token field in; `{}` -> no tokens; tokens a list in runs.jsonl -> no tokens
- at `2026-01-01` (AT the tariff date) -> 18.0; `2025-12-31` -> `unmeasured: no rate for m-a`
- Negative "no blank-line edge in the journal": positive control in the same search, the two t-2105 dispatch notes printed

## Trail
- `git merge-base --is-ancestor b94ad77 2d47674` -> ANC; `git status --porcelain` empty before and after the empirics
- Read: verdict t-2105-b4-price-2.md; `git diff b94ad77..2d47674` whole (price.py, rates.yaml, test_score.py); `git log -1 --format=%B 2d47674`; price.py 60-190 and 192-225, 290-325 at HEAD; arm.py def list + emit; seeded.py read_jsonl/append; journal.py::load
- `python -B -m pytest forge/tests/test_score.py -q -p no:cacheprovider` -> `48 passed in 1.13s`
- Scratch empirics: scratchpad b4/emp.py (round-1 values, outputs above), b4/emp2.py (round-2 edges, now all refused or unmeasured as fixed), b4r3/emp3.py (new). Outputs include `add-rate --in 400 chars -> None`, `lines after -> 3`, `read_rows after -> EXC OverflowError int too large to convert to float`, `harness int 10**400 -> EXC OverflowError`, `hand row in -3.0 -> 12.0 USD`, `journal non-launch list agent -> EXC Refuse ...journal.jsonl:2`, `check head file deleted -> ['- {"model": "m-a", ...}']`. My CRLF row was invalid: a Windows text-mode write doubled the `\r`
- Real data: runs.jsonl 44 lines / 0 blank (`wc -l`, `grep -c '^\s*$'`); exp-fvf* journal.jsonl: 42 lines, 0 list/dict keys, 0 launches
- `git ls-files --eol`: index LF for all three files, unchanged
- CI: no run read (no remote branch named in the dispatch); the builder's mechanical layer was not in the given, and the narrow DoD file above was re-run as the control
