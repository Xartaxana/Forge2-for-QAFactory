# t-2105 -- critic on B4 (+ B12 (ii)) price.py, at d3ffafd (diff main...d3ffafd)

verdict: blocker -- 8 blocking findings (F1-F8), 1 non-blocking (F9); failure_class: capability

## Verdict lines
- measure/tools/price.py: blocker -- writer poisons the file (F1); crashes on the spec's own `unmeasured` forms and on empty input (F2, F3, F6); fast long prompt priced at the short rate (F4); check green on a non-commit base (F5)
- measure/rates.yaml: fit -- header only, no rate rows (Lead's ruling); header owes the cache_write meaning (F8)
- forge/tests/test_score.py: fit_with_fixes -- edges at the boundaries unpinned (F7)
- decision bucket id `model|model@fast|model>N|model@fast>N`: fit -- theoretical collision only for a model id that itself ends in `@fast` or holds `>N`
- decision speed standard == no speed: fit
- decision `mixed:` key -> `unmeasured: mixed models`: fit -- safe direction; the producer (C0-4) has no spec line for the key: proposed node below
- decision harness_cost number | {amount, currency}: blocker -- F2
- decision mixed currency over the rows used: fit -- matches the edge "refused naming the rows"
- decision check compares non-comment lines byte for byte: blocker -- F5 (base resolution), the comparison itself fits K6
- decision `--run` with no test row (PARTIAL): blocker -- F6, it crashes on frame 2f's data form
- TESTS (Q5): fit_with_fixes -- F7; expected values sourced (`expected from:` with hand arithmetic, re-derived below); no duplicate row; one file, worlds per test via `rates()`, one git world
- DUPLICATION AND CONSISTENCY: F5 -- `check` re-implements forge/tools/ratchets.py::base_of / base_doc without their non-commit refusal; tokenizer: n/a; refusal-text builder: `unmeasured()` local, no shared one exists (grep `def unmeasured` forge/tools: 0); path resolver: ROOT from `__file__` as every forge tool
- CODE QUALITY: F6 (journal_groups 4 loop levels, price.py:148-157), F8 (ambiguous `cache_write`), files opened without close (price.py:28, 141, 149)
- ONE ROAD (Q12): fit -- no model, provider or language name in code; every model priced through rows by exact id; speed values `standard|fast` are the spec's own list (B12 (ii))
- VARIETY: blocker -- an unknown token key is dropped silently and a price shown (F3); unknown model/speed/tier -> `unmeasured` (fit)
- AR-n naming: F9 -- AR-14 (add-rate one writer), AR-27/AR-28 (unmeasured never 0), P18 touched, commits name none
- ratchet rows raised: none (ci-jobs.json `rates` row untouched, state not_built)
- K3: fit -- `grep -rli "price.py|rates.yaml" factory measure`: hits only measure/rates.yaml, measure/tools/price.py (positive control the same grep)
- class completeness: number encoding (F1), harness_cost shapes (F2), tokens_by_model shapes (F3), tier thresholds across speed and date (F4), base resolution (F5), journal token shapes (F6) walked; leftovers carry nodes below
- probe: none -- no runner with `--root` in forge 2 (tool: none yet; forge/tools has no mutate tool), and the dispatch forbids edits

## Findings

F1 (blocks) price.py::add_rate, lines 121-125, 132-133. `Decimal(v)` accepts forms JSON rejects. Measured: `--in .5`, `3.`, `+3`, `1_000` are each written (`"in": .5`) and the next `read_rows` raises JSONDecodeError -- every later compute, bucket and add-rate (which reads first) crashes; after merge the row cannot be removed (check red by design). `NaN` and `-3` are written and read (NaN makes the `<=` at line 98 raise InvalidOperation). Exponent `1.5E-1` (0.15) gives d=1 from the regex at line 33, tolerance 10x too wide. Fix: refuse unless `re.fullmatch(r"\d+(\.\d+)?", v)`, json.loads the built line before appending; read_rows turns a JSONDecodeError or a missing key (`currency`, `tariff_date`, `model`: measured KeyError 'currency') into a refusal naming the line (B12 edge "rates.yaml malformed -> B4's own refusal text shown").

F2 (blocks) price.py::compute, lines 92-98. B4 amends C0-4 K2: a run row holds `harness_cost: unmeasured: <why>`. Measured: `compute({"m-a": T}, "unmeasured: no figure")` -> InvalidOperation; `{"amount": "unmeasured: x", "currency": "USD"}` and `True` the same. `run_report` passes `r.get("harness_cost")` straight in, so one such row kills `--run`. Fix: an amount that is not an int/float (bool excluded) is no figure -> `agree: one source` + label (F100 (a)); one row in test_two_sources.

F3 (blocks) price.py::compute, lines 71-91. Measured: `compute({})` -> KeyError 'pop from an empty set' (a band with no answer yet, a failed run); key `None` -> TypeError at line 76; a token value that is a string -> AttributeError; a float count `1e6` -> TypeError; `{"in","out","cache_read","cache_write":0,"cache_write_5m": 1M}` -> price 18.0 with the 1M writes unpriced (an unknown field read as zero: AR-27/AR-28, VARIETY). Fix: no keys -> `unmeasured: no tokens`; a key that is not a str -> `unmeasured: no model named`; a kind outside KINDS -> `unmeasured: unknown token field <k> of <key>`; a value not a non-negative int -> `unmeasured: token field <k> of <key>`.

F4 (blocks) price.py::bucket, lines 49-52. Thresholds are taken per (model, speed). Rows m-a, m-a>200000, m-a@fast: `bucket("m-a","fast",300000)` -> `m-a@fast`, compute prices 45.0 at the short fast rate. B12 edge: "a fast-mode usage or a long prompt with no matching bucket row -> the same unknown rate for that bucket". Fix: overs from every row of the model whatever its speed -> `m-a@fast>200000` -> `unmeasured: no rate for m-a@fast>200000`; one row in test_bucket. (Thresholds across dates: a tier born later reprices `--at` earlier as unmeasured -- safe; noted, no fix.)

F5 (blocks) price.py::check, lines 136-142. Any git failure returns [] -> "rates: append-only holds", exit 0. Measured in this worktree: `check("no-such-ref-xyz", .../measure/rates.yaml)` -> []. The CI road is guarded (ci.py::resolve_base gives a commit or exit 3), the CLI door is not. forge/tools/ratchets.py::base_of (line 104) refuses a non-commit base, base_doc (line 115) prints `born:` for an absent file. Fix: reuse ratchets.git/base_of (import as universality.py does) or the same `rev-parse --verify -q <base>^{commit}`; non-commit -> refusal, exit 2; absent file at a commit base -> `born`, exit 0.

F6 (blocks) price.py::journal_groups / run_report, lines 145-169. Frame 2f / C4-6: a token field with no carrier is `unmeasured: <why>`. Line 157 `tot[k] + v` with v a string -> TypeError; `tokens` itself a string -> AttributeError at line 156; a launch with no `model` -> F3's TypeError; line 151 counts an event with no `event` key as a launch; KINDS[:4] at 154-157 drops `cache_write_1h` silently (same class as F3); 4 loop levels at 148-157 (over 3); files at 149, 166 never closed. No row exercises the `--run` door. Fix: only `event == "launch"`; a non-int value sets the kind None; all KINDS; split the per-event accumulation into a helper; one row with a fixture journal.jsonl (one unmeasured field) + runs.jsonl. Alternative for the Lead to decide: drop `--run` from this diff and open it as a node after C4-6 fixes the journal form.

F7 (blocks) forge/tests/test_score.py. No row sits on a boundary: tolerance AT the edge (18.10 -> yes, measured), prompt AT prompt_over (200000 -> `m-a`, measured), `--at` equal to a tariff date. Flipping `<=` at price.py:98, `>` at :51 or `<=` at :56 leaves all 15 rows green (by reading the rows' values 18.05/18.5, 100/200001, 2026-03-01; probe not run). Fix: add those three rows to the existing tables, plus the rows named in F1-F4, F6.

F8 (blocks, code quality) price.py::compute docstring line 65 and rates.yaml header line 3. Whether `cache_write` includes 1h writes is unwritten; B12 carries `cache_write_5m` and `cache_write_1h`; a caller passing total writes in `cache_write` plus `cache_write_1h` double-prices the 1h writes. Fix: state "cache_write = 5-minute writes only; 1h writes in cache_write_1h" in both.

F9 (non-blocking) commits 33cb3f8, d3ffafd name no AR-n: AR-14, AR-27/AR-28 and P18 are touched. Fix: name them in the next commit message.

## Seam and class notes
- B12 seam (proposed node t-2105-n1, owner: the Lead, executor the B12 builder): band.py must hand compute `cache_write` (5m) not `cache_write_5m`, else every band price reads `unmeasured: token field cache_write` (measured shape in F3). compute names only the FIRST missing bucket; B12 K2 `unknown_rate: [model-b]` with several unknowns needs either one compute call per bucket in band.py or compute listing all -- a fork for the Lead.
- C0-4 seam (proposed node t-2105-n2, owner: the Lead, executor the C0-4 designer): `collect` must emit the `mixed:<models>` key for a total-only multi-model harness; no C0-4 line names it.
- bucket re-reads rates.yaml on every call (band calls it per usage line); no finding without a measurement, B12 K7 measures.
- Siblings: callers of price.py/rates.yaml in measure/, forge/, factory/: none in code (grep above; forge/ci-jobs.json row `rates` not_built). B12's band (forge/tools/band.py) not built.

## Spot-checks (claims and empirics, control values by hand)
- A: in 3.0, out 15.0, 1M each -> 18.0; tol = 2 x 1 x 0.5 x 10^-1 = 0.10. 18.05 yes; 18.5 no, from 18.0 to 18.5 + finding; 18.10 yes; 17.90 yes; 18.1000001 no. cache_read 0.30 (d=2) 1M: price 18.3, tol 0.105: 18.405 yes, 18.4051 no. All match the rule.
- 1h write 5 on a row without cache_write_1h -> `unmeasured: no rate for m-a (cache_write_1h)` (holds the spec's `no rate for <bucket>`); 1h write 0 -> priced 18.0.
- prompt 200000 -> `m-a`; 200001 -> `m-a>200000`; m-a>200000 (in 6.0, out 15.0) 1M each -> 21.0.
- harness 0 -> agree no, from 0.0 to 18.0; {amount 18.0} with no currency -> not comparable (safe).
- Builder claim "check compares byte for byte": holds for base lines vs head lines (splitlines on both, CRLF neutral; rates.yaml has 0 CRLF).
- Control run green before any judgement (below).

## Trail
- Read: price.py whole, rates.yaml whole, test_score.py whole (d3ffafd); spec part4b B4 whole; part4b-4 B12 whole; frame spec 2f (event fields) and AR-27/AR-28 line; part3b C4-6 Delivers/edges; forge/tools/ratchets.py:96-127; forge/tools/ci.py:81-102; forge/ci-jobs.json row rates; .github/workflows/ci.yml fetch-depth 0; commit bodies main..d3ffafd.
- `git status --porcelain` in C:/QAFactory/forge2-wt/t-2105: empty; HEAD d3ffafd.
- `python -B -m pytest forge/tests/test_score.py -q -p no:cacheprovider` -> `15 passed in 0.59s`.
- Empirics: scratchpad b4/emp.py importing price from the worktree, rates in scratch files, outputs quoted in Findings and Spot-checks (`AT edge 18.10 -> agree yes`; `bucket fast 300000 -> m-a@fast`, price 45.0; `harness 'unmeasured: x' -> EXC InvalidOperation`; `empty tokens_by_model -> EXC KeyError`; `extra 5m key -> price 18.0`; `check bad ref -> []`; add-rate `.5|3.|+3|1_000 -> read EXC JSONDecodeError`).
- CI: no remote branch w/t-2105, no CI run; ratchet results not read.
- Builder's mechanical layer (DoD tails) was not in the dispatch; the narrow run above is the control re-run the dispatch allowed.
