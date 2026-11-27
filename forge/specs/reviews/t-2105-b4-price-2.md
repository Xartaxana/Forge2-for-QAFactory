# t-2105 -- critic re-review of the fix round, diff d3ffafd..39538a8 (worktree C:/QAFactory/forge2-wt/t-2105, HEAD 39538a8)

verdict: blocker -- F1-F9 fixed; 4 new blocking findings (F10-F13), 1 non-blocking (F14); failure_class: capability

## Verdict lines
- F1: fixed: price.py::NUMBER (line 22) + add_rate refusal (157) + read-back `json.loads(line[1:])` before the append; read_rows turns bad JSON / missing model|currency|tariff_date into Refuse naming file:line; rows test_add_rate_refuses_what_json_cannot_read (8 forms), test_malformed_row_is_a_refusal_naming_the_line
- F2: fixed: compute: an amount that is not int/float, a bool or non-finite is no figure -> one source + label; two rows in test_two_sources (also measured: NaN, inf, True -> one source)
- F3: fixed: compute `no tokens` guard + price.py::token_why (unknown kind, non-str key, non-count value); five rows in test_unmeasured
- F4: fixed: bucket takes prompt_over of every row of the model whatever its speed; rows in test_bucket (`m-a@fast>200000` -> unmeasured)
- F5: fixed: check reuses ratchets.base_of / ratchets.git; non-commit -> Refuse, exit 2; no file at a commit base -> `born`; test_check_base
- F6: fixed: only `event == "launch"`, all KINDS, a non-count value makes the total None, helper add_event, files closed, test_run_report -- with a residual of the same class, F11
- F7: fixed: rows at 18.10 (yes) / 18.11 (no), bucket AT 200000, `--at` equal to the tariff date (the three flips named in round 1 are killed by these rows, by reading; probe not run)
- F8: fixed: compute docstring and rates.yaml header both state cache_write = 5-minute writes only
- F9: fixed: commit 39538a8 names AR-14, AR-27/AR-28, P18 (also touched and unnamed: AR-20, append-only check -- name it in the next commit, non-blocking)
- choice `check` refuses (exit 2) on an empty or all-zero base: fit -- ci.py::resolve_base never hands zeros to `{base}` (fill returns None, job not run), so only a hand-typed CLI meets it; price check has no other part to judge (ratchets.base_doc prints "raises not judged" while the ratchet's own state is still judged), and exit 2 is ratchets' "cannot judge (Refuse)"; the safe direction, never a green "append-only holds" with nothing compared
- measure/tools/price.py: blocker -- F10, F11, F12
- measure/rates.yaml: fit
- TESTS (Q5): fit_with_fixes -- F13; expected values sourced; builder claim "36 passed, 20 failed with the old price.py" reproduced (20 failed, 16 passed; 2 of the 20 are new-signature TypeErrors, check() / run_report(), weak reds but call-time, not collection)
- DUPLICATION AND CONSISTENCY: F13 (args_of re-builds test_writer_and_ratchet's Namespace), F14 (two refusal roads in one tool); base resolution now reused from forge/tools/ratchets.py::base_of (round-1 F5 closed); tokenizer: n/a; path resolver: ROOT from `__file__`
- CODE QUALITY: F12 (dead `else []`, price.py:181-182); nesting checked: journal_groups 3 levels, add_event 2; no function over 60 lines
- ONE ROAD (Q12): fit -- no model, provider or language name added; `ratchets` import is the shared mechanism, not a branch
- VARIETY: blocker -- an unknown journal token field is dropped and a price shown (F11)
- AR-n naming: see F9 line
- ratchet rows raised: none (ci-jobs.json untouched)
- class completeness: number encoding of every add-rate field (F1 -> F10: tariff_date, prompt_over, `--at`, Unicode digits), token shapes on both roads, compute and journal (F3 -> F11), broken input on every reader (rates: fixed; journal, runs.jsonl: F11), base and head presence in check (F5 -> F12)
- probe: none -- no runner with `--root` in forge 2 (tool: none yet), dispatch forbids edits

## Findings

F10 (blocks) price.py::add_rate (147-167) and the `--at` door (compute `at`, pick). Sibling of F1 that round 1 missed (its class walk covered rate numbers only): the writer accepts forms its readers misread. Measured on rows A (in 3.0, 2026-01-01) + `add-rate --in 9.0 --out 1 ... --tariff-date 2026-6-1`: `compute at=2026-07-01` -> `18.0 USD (tariff 2026-01-01)`, the old rate although the new one is in force; no `--at` -> `10.0 USD (tariff 2026-6-1)`; pick compares strings. `add-rate --prompt-over -5 --in 6.0`: `bucket("m-a","standard",100)` -> `m-a>-5`, priced 7.0 at the long rate, the plain row never used again (append-only: cannot be removed). `--at 2026-1-15` picks a 2026-06-01 row ("2026-06-01" <= "2026-1-15"). `--in ٣` or `３` pass NUMBER (`\d` is Unicode) and die at the read-back as a JSONDecodeError traceback (file intact: 2 lines before and after). Fix: tariff_date and `--at` must be `datetime.date.fromisoformat` of a `\d{4}-\d{2}-\d{2}` string, else refused; prompt_over > 0, else refused; `re.compile(r"\d+(\.\d+)?", re.ASCII)`; add the three forms to test_add_rate_refuses' table (one row each, no new test).

F11 (blocks, VARIETY) price.py::add_event (186-195), journal_groups (203), run_report (217). (a) add_event reads only KINDS, so a journal token field outside them is dropped: journal launch with `{"in":1M,"out":1M,"cache_read":0,"cache_write":0,"cache_write_5m":1M}` -> `agent a: 18.0 USD`, the 1M writes unpriced -- exactly F3's defect, closed on the compute road, open on the `--run` road. (b) a torn or non-JSON journal line -> JSONDecodeError traceback (measured `{"event": "launch", "agent": "a"` -> `Expecting ',' delimiter`); runs.jsonl has no blank-line skip and no dict check (`json.loads("\n")` raises, a JSON list -> AttributeError at `r.get`). Fix: in add_event a key of `tokens` outside KINDS is carried into tot as None under its own name, so compute's token_why answers `unknown token field <k> of <model>`; parse both stores through one helper that skips blank lines and raises ratchets.Refuse("<file>:<n>: not a journal event") for a non-JSON or non-object line; one more line in test_run_report's fixture journal (extra field -> unmeasured).

F12 (blocks, regression + dead branch) price.py::check, lines 181-182. `with open(path, "rb") as f: head = ... if os.path.isfile(path) else []` opens before the guard: with rates.yaml deleted at head and present at the base, check raises FileNotFoundError (measured in a scratch git world) instead of naming every removed row, as d3ffafd did; the `else []` is dead. Fix: `head = []` then `if os.path.isfile(path): with open(...) as f: head = f.read().splitlines()`; one assert in the test that already holds a git world (F13).

F13 (blocks, test file budget and copy-paste) forge/tests/test_score.py. (a) test_check_base (131) builds a second git world where test_writer_and_ratchet's (85) would do: an `--allow-empty` first commit there gives `born`, the bad ref the refusal, and the deleted head file F12's row. (b) args_of (104) copies the Namespace construction of test_writer_and_ratchet (89-93); the writer test should use args_of. (c) the control `add_rate(in=1.5)` + read-back (120-121) runs in all 8 rows of the refusal table; once suffices -- move it into test_writer_and_ratchet's successful add. Rows to cut, weakest first: the repeated control (c), then the second world (a).

F14 (non-blocking) price.py:151, 157 vs main's `except ratchets.Refuse` (exit 2). add_rate refuses by `sys.exit("refused: ...")` (exit 1, stderr), read_rows / check by Refuse (exit 2, stdout): one tool, two refusal roads and two exit codes. Fix: raise ratchets.Refuse in add_rate. Tests that expect SystemExit change to Refuse.

## Seam and class notes
- B12 seam (adds to proposed node t-2105-n1, owner the Lead): compute and bucket now raise ratchets.Refuse on a malformed rates.yaml; band.py must catch it or exit 2 through the same `except`, never a traceback.
- Round-1 nodes t-2105-n1 (band.py hands `cache_write` = 5m; one compute per bucket or compute listing all) and t-2105-n2 (C0-4 `mixed:` producer) stand unchanged; the Lead opens them.
- Hand-written exponent rows (`3.0E0`) still read with d=1; the one writer now refuses them, so no live input; noted, no fix.

## Spot-checks (round-1 control values re-run at 39538a8, hand values)
- 18.05 yes; 18.5 no (from 18.0 to 18.5); 18.10 yes; 17.90 yes; 18.1000001 no; cache_read d=2: 18.405 yes, 18.4051 no -- all as by hand (tol 0.10 / 0.105).
- 1h write 5, no 1h rate -> `unmeasured: no rate for m-a (cache_write_1h)`; 1h write 0 -> 18.0.
- bucket 200000 -> m-a; 200001 -> m-a>200000; fast 300000 -> m-a@fast>200000 -> unmeasured (was 45.0); long 1M -> 21.0.
- harness `unmeasured: x`, `{amount:"unmeasured: x"}`, True -> one source 18.0 (were InvalidOperation); 0 -> no, from 0.0 to 18.0; no currency -> not comparable.
- key None -> no model named; float count -> token field in; `{}` -> no tokens (was KeyError); extra 5m key -> unknown token field (was 18.0); malformed row / no currency -> Refuse naming file:line; bad ref -> Refuse `not a commit here` (was []); `0000000` -> Refuse `no base given`.
- Builder claim 20 failed with old price.py: reproduced in a scratch copy (git archive 39538a8 + `git show d3ffafd:measure/tools/price.py`): `20 failed, 16 passed`.
- Positive control for "no AR-20 in the commit": `git log -1 --format=%B 39538a8` read whole (names AR-14, AR-27/AR-28, P18).

## Trail
- `git status --porcelain` in the worktree: empty; HEAD 39538a8.
- Read: verdict t-2105-b4-price.md; `git diff d3ffafd..39538a8` whole (price.py, rates.yaml, test_score.py); price.py 40-72, 104-150, 225-260 at 39538a8; test_score.py 1-26, 84-101; forge/tools/ratchets.py base_of / base_doc / git / Refuse / exit legend; forge/tools/ci.py::resolve_base; forge/ci-jobs.json row rates; frame spec AR-20 line.
- `python -B -m pytest forge/tests/test_score.py -q -p no:cacheprovider` -> `36 passed in 1.61s`.
- Scratch empirics (scratchpad b4/emp.py round-1 values unchanged, b4/emp2.py new edges): outputs quoted above, e.g. `journal extra cache_write_5m -> agent a: 18.0 USD`, `check head file deleted -> EXC FileNotFoundError`, `compute at 2026-07-01 -> 18.0 USD (tariff 2026-01-01)`, `bucket m-a 100 tokens -> m-a>-5`, `add-rate unicode digit '٣' -> EXC JSONDecodeError`, file lines after: 2.
- Old-code run: scratch copy, `20 failed, 16 passed in 1.92s`.
- `git ls-files --eol`: index LF for all three files, unchanged.
- CI: no run read (no remote branch named in the dispatch).
