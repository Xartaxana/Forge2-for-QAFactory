Frame spec part 2: card bodies of phases 0-2, forge 2 and the light QA factory (t-1914, F19; r0 25.11.2026; r1 = t-1918). Part 1 = `docs/tasks/specs/20261125-forge2-light-factory-spec.md` r1 (12a00c2c8); part 3 = `...-spec-part3.md` (bodies of phases 3-4); plan = `...-plan.md` v1.3. `owns:` paths are absolute; other paths are relative to `C:/QAFactory/forge2-repo/` unless they start with `C:/` or `experiments/` (= `C:/QAFactory/forge-repo/experiments/`).

## Revision r1
- r1.1 -> part 1 r1 (12a00c2c8), plan v1.3, part 3 named; part 1 section numbers cited are unchanged in r1; C3-*/C4-* bodies -> part 3; C0-1 copies part 3 at acceptance -> line 1, 1, C0-1, C2-1, C2-5
- r1.2 -> new body C2-8; fork F51 -> C2-8, 3
- r1.3 -> F15-F23 taken as (a) by the Lead, section 3 shortened; owns per (a) in C0-5, C1-1, C1-6, C2-4, C2-7; F18 hook definite; C1-2 budget counts role files -> 3, C0-*, C1-1, C1-2, C1-4..C1-6, C2-4, C2-7
- r1.4 -> one table `factory/data/secret-patterns.yaml` owned by C1-5; absent -> both hooks fail closed -> C1-5
- r1.5 -> one job list `forge/ci-jobs.json` for `ci.yml` and `ci.py` -> C1-6
- r1.6 -> `seeded.py` launches only via `arm.py launch --task`; no seed from a truth table; seed source F50 -> C2-6, C0-4, 3
- r1.7 -> both truth tables frozen at their acceptance commit before any page or seed; C2-2..C2-6 deps name it -> C0-2, C0-3, C2-2..C2-6, 1
- r1.8 -> `score.py` counts `passes`; every run in `mode: comparison` -> C0-4, C0-5
- r1.9 -> swept owns of the 20 index rows, order line, section 6 rows: only the r1.3-r1.5 mismatches; order gains C2-8 -> 1; small choices -> 4; `- Delivers:` label made uniform -> C0-2, C0-3, C1-3, C1-5
- size -> 50343 bytes as returned, over the cap; F52 (a): C2-* bodies moved to part 2b by the Lead's script -> 2, 3

## 1. Scope and pointers

**Adds:** bodies of the 20 cards of phases 0-2 (ids, names, owns: part 1 section 4); the phase 2 statement map (C2-1); the phase 1 forge carry map (C1-1); forks F15-F23 (taken), F50-F52.

**Rests on part 1 r1:** sections 1 (layout, invariants, variety walk; here AR-1/AR-2 via C1-2 and C2-1, AR-15 via C1-5, AR-29 via C2-6's judge, P31 via C0-4 and C2-6), 2a (`mode`, `passes`), 2c, 2f, 3, 6, 8 and forks F5, F6, F7, F9, F10, F12, F14, cited by id. Bodies of C3-*, C4-*: part 3.

**Order** (plan «Фазы»): phase 0 first (C0-1 -> C0-2 par C0-3 -> C0-4 -> C0-5); then phases 1 and 2 in parallel. Phase 1: C1-1, C1-6, C1-7, C1-4 par; C1-2, C1-3, C1-5 after C1-6 (CI runs the ratchets; the push hook calls the CI runner). Phase 2: C2-2..C2-6 par, none written before the C0-2 and C0-3 freezes (F5); C2-1's code after C1-3 and C1-6 (part 1 section 6 row 1); C2-7 after C0-5 and C2-1..C2-6; C2-8 after C0-5; phase 3 is not dispatched before C2-8 closes (part 1 section 6).

**Rules before the skeleton** (part 1 section 6 row 1): phase 0 cards, and phase 1-2 cards accepted before C1-1/C1-6 land, follow `C:/QAFactory/forge-repo/CLAUDE.md` and its `docs/TESTING.md`; tests run from the forge2 root, `python -m pytest <file> -q`. After C1-1/C1-6 commit, forge 2's own files rule.

**Common:** a measuring copy is never the owner's folder; nothing loads archiveofourown.org (ao3 `stand/stand.ps1:5-7`); no money figure in any file (F7); `experiments/**/runs/` is not read or quoted here; hooks are content until the Lead places them (C1-5).

## 2. Cards

### C0-1 Place: plan + spec copies, README
- amended by: B13 (cards whose `amends:` line names this card; read them with it)
- Delivers: byte copies of plan, part 1, part 2 (part 3 at its acceptance) in `forge/specs/`, sha256 + source commit in `forge/specs/SOURCES.md`; `README.md`: what forge 2 is, layout by pointer (part 1 section 1), the freeze (`C:/QAFactory/forge-repo/CURRENT_CONTEXT.md` «FROZEN since 25.11.2026»), rules in force (section 1), phase table 0-4 (`not started | in work | closed by <run file>`).
- owns: C:/QAFactory/forge2-repo/README.md, C:/QAFactory/forge2-repo/forge/specs/
- deps: the owner's yes on the plan; F20 (a).
- keys: K1 every copy equals its source by sha256; K2 README names the rule carriers and five phase rows; K3 no money figure.
- edges: source edited after the copy -> the copy is the home (F20 (a)), nothing mirrored (one home); copy bytes differ from the recorded sha256 -> K1 red (a copy of other bytes never counts); part 3 not accepted at C0-1 -> copied at its acceptance, a `SOURCES.md` row added; until then its forge-repo draft is its one home.
- test: none -- documents; witness: key script with a negative control (DOC-DISPATCH).

### C0-2 MyBooks measuring project
- amended by: A27, B13 (cards whose `amends:` line names this card; read them with it)
- Delivers: carried by byte copy (sha256 in `measure/mybooks/SOURCES.md`): `experiments/mybooks/truth/add-to-cart.yaml` -> `truth.yaml` (scored version `v2026-11-05-owner`, `judged: true`; Lead version kept as history); `factory-vs-free-agent/story/LOCAL-1.md` -> `story/`; the exported ticket `task/XPANBFLFA-44.xml` the story names (in the stand arm folder, `RUN-INSTRUCTIONS.md:97-98`; location `estimate`, trail) -> `story/`; `free-agent-prompt.md` (template) -> `free-prompt.md`; `stand/stand.ps1`, `stand/free-mcp.json` -> `stand/`; `judgment.yaml` -> `history/lr2-1-judgment.yaml` (no code reads it); `answers/README.md` and every answer about the PRODUCT or ENVIRONMENT (by name: `no-decision-yet`, `no-tracker`, `cart-quantity-multidigit`, `out-of-stock-disabled-button`, `no-change-current-code`; the builder confirms by reading) -> `answers/`.
- Left behind: old-flow answers (`gate-a-*`, `s2-*`..`s5-*`, `ticket-title-go-on`: the new factory never asks them); `RUN-INSTRUCTIONS.md` (free-arm rules -> `project.yaml`, C0-4); `notebook.md`; `factory-vs-free-agent.md` (scoring -> C0-4); `cart-1-run-problems.md`, `thinking-roles/`, `disputed-check-plain-agent/`; `runs/`.
- `project.yaml`: `source` (pristine clones, read only, `stand.ps1:13-14,30-31`), `commit` per source, `copies_root` (outside both repos), `story`, `truth`, `prompt_template` + values, `stand` (commands per arm, expected status), `env`, `model` (= roles' model, P7), `allowed_tools`, `forbidden_hosts`, `machine_notes` (RUN-INSTRUCTIONS §2 traps).
- FREEZE (F5 condition, plan v1.3): `truth.yaml` is frozen by the Lead's acceptance commit of this card; its hash is named in the card's result (hand-back and journal line) and cited by C2-2..C2-6; it precedes any craft page or seeded set.
- owns: C:/QAFactory/forge2-repo/measure/mybooks/
- deps: C0-1.
- keys: K1 every carried sha256 equals its source; K2 `truth.yaml` keeps 24 cards per version; K3 no old-flow answer; K4 a commit per source; K5 the freeze commit is older than the first commit of any `factory/craft/*.md` or `measure/seeded/` file (`git log`).
- edges: an answer mixing product and flow -> carried whole, flagged (a product word is never trimmed away); README cites `../thinking-roles/answers/` -> kept as text, no file follows (the free arm never gets forge material, `RUN-INSTRUCTIONS.md:40-41`); source dirty or off its commit -> `commit: unknown`, C0-5 cannot start (a copy of unknown bytes never scores); a truth change after the freeze -> only a new `version` with the owner's word, the frozen one kept (a page or seed never shapes the table it is scored by).
- test: none -- data; witness: sha256 table and `score.py` loading `truth.yaml` (C0-4).

### C0-3 ao3-wrapper measuring project (F5)
- amended by: B13 (cards whose `amends:` line names this card; read them with it)
- Delivers: carried as C0-2: `story/LOCAL-1.md`, `stand/stand.ps1`, `answers/README.md`, `answers/no-decision-yet.md`; the free prompt per F15 (a). Left behind: `answers/gate-a-*`, `s1-*`, `s5-*`; `notebook.md`, `factory-vs-free-agent.md` (truth sources only); `RUN-INSTRUCTIONS.md`; `runs/`.
- NEW per F5 (a): `truth.yaml`, schema `truth/1`, version `v2026-11-25-hand`; card = `source` (file:line), `class`, `confirmed` (`true` only with the owner's words verbatim + date, or a hand check with evidence), optional `credit` (closed: `question_or_accept`, `question_with_steps`, `autotest_required`, `mock_stated`). Sources: five owner decisions (`experiments/ao3-wrapper/factory-vs-free-agent/factory-vs-free-agent.md:21-28`); hand check (`notebook.md:470-493`: BUG-1 last tag not removable, overlay + panel one root; add tag appends = not_bug; five ratings = not_bug; notice with a filter on = not_bug); mock rule (`factory-vs-free-agent.md:16-17`, row н). Not hand-checked (`notebook.md:488-490`: Dim mode, swallowed errors) -> `unknown` with `why`.
- FREEZE as C0-2 (part 1 F5 (a)): frozen by this card's acceptance commit, after the owner's confirmation of disputed cards; hash in the card's result; its bugs are never seeds (C2-6).
- `project.yaml` as C0-2: `source: C:/QAFactory/ao3-wrapper` (read only), `stand.precheck_expect: "real site: NOT reachable"`, `forbidden_hosts: [archiveofourown.org]`, arms in sequence (one emulator, `RUN-INSTRUCTIONS.md:26-28`), no web fetch/search tools.
- owns: C:/QAFactory/forge2-repo/measure/ao3-wrapper/
- deps: C0-1; F5, F15.
- keys: K1 carried sha256; K2 every card has a source line; K3 every `confirmed: true` quotes the owner or names evidence; K4 the owner's confirmation of disputed cards recorded verbatim (person step, plan «Фазы» row 0); K5 as C0-2 K5.
- edges: unconfirmed card -> scored neutral (FR-59: no score rests on an unconfirmed class); a run's find outside the table -> hand check on the stand, doubt to the owner, `unverified` till then (`experiments/mybooks/factory-vs-free-agent/factory-vs-free-agent.md:40-42`); precheck text absent -> no run starts (the real site stays unreachable); owner's confirmation not given -> no freeze, C2-2..C2-6 wait (part 1 section 6); change after the freeze -> as C0-2.
- test: none -- data; witness as C0-2.

### C0-4 The one arm launcher; comparison scorer (counts passes)
- amended by: A27, A30, B1, B4, B12 (cards whose `amends:` line names this card; read them with it)
- Delivers: `measure/tools/arm.py`: `prepare` (clone, fill prompt, stand precheck; `--dry-run` prints the plan), `launch` (harness command row of `project.yaml`; `--task <folder>` launches a seeded task for C2-6, a stage context for C2-8), `answer` (resume with an answer file), `collect` (arm `out/` + run row into the run folder, F21 (a)). Every launch is `mode: comparison` (part 1 2a header, set at `record.py init` for factory arms): the launching model is the operator, answers stop questions only through `answer`, never passes a gate or grants outward permission. `measure/tools/score.py`: cells, table rows, `passes` count, `compare`.
- No trace (P8): `prepare` refuses a source with non-empty `git status --porcelain`; `git clone --no-hardlinks` into `<copies_root>/<run>/<arm>/`, `origin` removed, source HEAD + status recorded; `collect` re-reads them: unequal -> `trace: source changed`, never scored; copies kept, not deleted.
- Run row: `run`, `project`, `arm`, `mode`, `fingerprint`, `start`, `end`, `wall_s`, `turns`, `tokens` (in, out, cache read, cache write), `human_count`, `passes`, `status` (`measured | unmeasured: <why>`). Keys matching `cost|usd|price` are dropped before any repo write; raw harness logs stay in `copies_root`.
- Fingerprint: sha256 of story, filled prompt, answer set, truth version; source commits; stand build + seed command; model id; harness version line; `allowed_tools`; `mode`. Comparable iff all equal; `compare` refuses otherwise, naming the field.
- Cell: input = `truth.yaml` + a judgment file per run (`judgment/2`, written by the evaluator -- judgment, AR-29): per card one verdict of `bug_named | gap_named | asked | accepted | pass_named | not_checked_reason | not_noticed | unsure`, plus `evidence`, `steps`. Cell = rule(class, verdict, credit) per `experiments/mybooks/factory-vs-free-agent/factory-vs-free-agent.md:18-24,32-38` and ao3 `factory-vs-free-agent.md:21-28`: `found | missed | false_pass | false_bug | correct | not_noticed | plus | neutral | incomplete | unsure`. Rows б, в, г, д, е, з, и, к, л, н computed; а, ж, о evaluator text verbatim; м never. Expected values from truth and those lines, never from code output (P20). `passes` = the record's `passes` rows (part 1 2a, 2c: "`score.py` counts passes").
- owns: C:/QAFactory/forge2-repo/measure/tools/arm.py, C:/QAFactory/forge2-repo/measure/tools/score.py, C:/QAFactory/forge2-repo/forge/tests/test_score.py
- deps: C0-2, C0-3; F7, F21.
- keys: K1 each (class, verdict, credit) row gives its cell; K2 no money key in a run row or collected file; K3 dirty source refused before cloning; K4 `compare` names the one differing field; K5 `prepare --dry-run` for both projects, no network; K6 every run row carries `mode: comparison` and a `passes` count.
- edges: judgment empty, broken YAML, non-UTF-8, unknown verdict, card missing or extra -> refused with card id and the closed set (an unjudged card is never a miss or a find); `unsure` -> counted apart, resolved by Lead or owner (a doubt never becomes a score); class `unknown` -> `plus` only with evidence, else `neutral` (card 24 rule); unconfirmed -> `neutral`; precheck text missing -> `prepare` refuses (no script reaches the real site); tests never launch a harness or stand: fixture command rows; free arm (no record) -> `passes: n/a -- no record`, never 0; a `passes` row in a comparison record -> run unscored, named (a launching model's pass never counts, P13); factory arm before `record.py` exists (C3-1, part 3) -> `launch` refuses it naming the card (part 1 section 6).
- test: `forge/tests/test_score.py`, strongest first: cell table | expected from: mybooks `factory-vs-free-agent.md:18-38`, ao3 `:21-28`; passes counted, a pass in a comparison record unscores the run | part 1 2a, 2c; P13; money keys dropped | F7; source changed -> unscored, dirty refused | P8; compare refuses | this card; judgment battery | this card's edges.

### C0-5 Free-agent baseline (F6), MEASURING RUN closing phase 0
- amended by: B4 (cards whose `amends:` line names this card; read them with it)
- Delivers: two free runs per project (F6 (a)), sequential, stand reset/seed before each, launched by `arm.py` in `mode: comparison`; operator = the launching model, answers stop questions only, from `answers/` in the same words, own answers marked «мои» and given alike to every later run (fp:A11); each run judged by a fresh-context critic against `truth.yaml` (`judgment/2`), run order hidden; run folder `measure/runs/baseline/` (F21 (a)): result file `result.md` (fingerprint per project, per run table rows, wall, turns, tokens, human count; spread (min-max per countable row); repeatability (same delivery verdict, same bug set); unsure cells and unverified finds by name), judgment files, run rows, operator answers; money keys stripped; raw logs in `copies_root`.
- owns: C:/QAFactory/forge2-repo/measure/runs/baseline/
- deps: C0-4; F6, F21.
- keys: K1 four measured runs, pairs comparable (`compare` exit 0); K2 a spread per countable row; K3 money grep (the dollar sign, `usd`, `руб`, `cost`; -i) over the run folder: 0 hits; K4 an operator answer reaches every later run.
- edges: infrastructure failure -> `unmeasured: <why>`, rerun, both kept (an unmeasured run never scores); pair not comparable -> rerun, never compare across a field; no question asked -> human_count 0 is measured, not unknown; a write outside the copy -> `trace`, unscored, owner told; folder absent before the first run -> created by `collect` (C0-2/C0-3 freezes and C0-4 must exist first, part 1 section 6).
- test: none -- measuring run; witness score rows and `compare` output.

### C1-1 Forge rules, size-budgeted (F9); role files (F16)
- amended by: B1, B2, B3, B5, B6, B7, B9, B10, B11, B13, B14, B15, B16, B17, B18, B21 (cards whose `amends:` line names this card; read them with it)
- Delivers: `CLAUDE.md` (worker duties, dispatch form, hygiene, role sections) and thin `.claude/agents/{scout,builder,critic,designer}.md` (tools, model, a pointer to the role section; no rule text) <= 12 KB together (F16 (a)); `forge/COORDINATOR.md` (Lead/Architect: routing, acceptance, escalation, measuring runs, owner's words) <= 20 KB. One place per rule; each carried rule ends `(case: <carrier>)` (run, journal line, retro, owner's word); no case found -> dropped, a commit line (plan 3.4).
- Carry map (`fr:` = `...-recon-forge-rules.md`, `fp:` = `...-recon-forge-process.md`; equal rules share one text):
  - -> CLAUDE.md: fr:A1-A6, A12, A16, A20-A23, A27, A29-A31, C3, D9, D10, Q1-Q7, Q9-Q13; fp:A7 (=fr:A1), A8, A9 (also TESTING.md), A10 (=fr:A4), A25, A28.
  - -> COORDINATOR.md: fr:A7-A11, A13, A15, A17-A19, A24-A26, A28, B1-B6, D4, D7; fp:A3 (as the free-agent comparison), A11, A12, A16, A18 (=fr:D7), A19 (with C1-7's empty map), A20 (=fr:A21), A21 (=fr:A23), A26 (=fr:A28).
  - -> tools: fr:C2 -> `dispatch.py`; fr:C4, D14 note cap -> `journal.py`; fr:D6 -> C1-2/C1-3; fr:D1, D13, D15 -> size ratchet; fr:Q8 -> English check; fr:D8, fp:A15 -> `forge/TESTING.md`; fp:A22 -> live probe per hook; fp:A1, A4 -> C2-6; fp:A27 -> C1-7 if caught.
  - dropped: fr:A14, fp:A5 (replaced by plan 4.3); fr:A32 (stdlib-only vs F10; old package); fr:B7 (judge unbound, fr:X3); fr:C1, C5-C18 (machinery/MEANS, digest's C class; fp section C alike); fr:D2, D3, D5 (no such files; bytes budget); fr:D11 (harness numbers, re-measure); fr:D12 (pile machinery); fp:A2, A6 (no exams; no SessionStart hook, plan 3.5); fp:A13 (`score.py` + baseline); fp:A14 (dry story later, owner 25.11); fp:A17 (no old tests); fp:A23 (friction is C4-6); fp:A24 (factory conductor, P22).
- owns: C:/QAFactory/forge2-repo/CLAUDE.md, C:/QAFactory/forge2-repo/forge/COORDINATOR.md, C:/QAFactory/forge2-repo/.claude/agents/
- deps: C0-1; F9, F16.
- keys: K1 sizes within ceilings; K2 each carried id in exactly one file (a line `rows: ...` per section); K3 every carried rule has `(case: ...)`; K4 no rule text in both files; K5 each role file is a pointer: tools, model, one section name of `CLAUDE.md`.
- edges: over budget -> rules cut or merged, ceiling never raised (owner only, plan 4.2); an owner's word as case -> quoted with date, never paraphrased as hers; two rows, one rule -> one text citing both; before C1-1 lands, no role files: workers run as forge 1's roles (part 1 section 6 row 1); a role file holding rule text -> K5 red (one place per rule).
- test: none -- rule text; witness: key script (ids once, sizes) with a negative control.

### C1-2 Size ratchet, universality counter, English-only check
- amended by: B1, B16, B20 (cards whose `amends:` line names this card; read them with it)
- Delivers: `forge/budgets.json` (F9: `CLAUDE.md` + `.claude/agents/*.md` 12288 B (F16 (a)), `forge/COORDINATOR.md` 20480 B, factory tool code 6000 non-blank lines of `factory/tools/**/*.py` + `factory/hooks/**/*.py`, gate rules 45 rows, `stage_start_load: null`); `size_ratchet.py` (value vs ceiling; a ceiling raised against the previous committed `budgets.json` needs `budget-raise: <key> -- owner <date> «<words>»` in the commit); `universality.py` (one scanner, two scans: names of `universality-names.json` in `factory/tools/`, `factory/hooks/`, case-insensitive, word-bounded, in code, comments, strings; Cyrillic `\u0400-\u04FF` in every text file of `factory/`); `universality-names.json` (`names` by kind: language, runner, framework, tracker, case manager, harness -- plan 4.7; `allow` rows with reason, shrink-only).
- owns: C:/QAFactory/forge2-repo/forge/budgets.json, C:/QAFactory/forge2-repo/forge/universality-names.json, C:/QAFactory/forge2-repo/forge/tools/size_ratchet.py, C:/QAFactory/forge2-repo/forge/tools/universality.py, C:/QAFactory/forge2-repo/forge/tests/test_budgets.py
- deps: C1-6; F9.
- keys: K1 empty repository: all counts 0, green; K2 a `pytest` token in fixture `factory/tools/x.py` -> 1, exit 1; K3 raise without the line -> exit 1; K4 Cyrillic in a fixture `factory/` file -> exit 1 at file:line.
- edges: measured file absent (`factory/` unbuilt, gate rules before C3-3) -> `absent: 0` (nothing exists: zero is measured); `stage_start_load: null` -> `not set: first measured run (F9)`, exit 3, never a pass; `budgets.json` absent or malformed -> exit 2 (never green); first commit of `budgets.json` -> `born`, green; non-UTF-8 file in `factory/` -> exit 2 naming it (an unread file is never clean); error direction: errs RED on a common word that is a name (door: `allow` row) and GREEN on a name split by concatenation (residual, critic Q12); names in `factory/data/` -> not counted (plan 4.7).
- test: `forge/tests/test_budgets.py` one table: name in code/comment/string/data, allow row, Cyrillic, non-UTF-8, size at/over, raise with/without line, absent inputs | expected from: plan 4.2, 4.7; F9; this card.

### C1-3 CRAP, lint, clone ratchets at zero
- amended by: B20 (cards whose `amends:` line names this card; read them with it)
- Delivers: (F17 (a)) three tools of one shape -- measure, compare with `forge/baselines/<tool>.json` (accepted offenders, each with reason and the Lead's word, shrink-only), exit 0 green / 1 red / 2 cannot judge / 3 part not judged; scope `factory/`, `forge/tools/` (clones: tests excluded). Lint = pyflakes (as `C:/QAFactory/forge-repo/tools/lint_ratchet.py:1`); CRAP = `ast` complexity x `coverage` (pure-Python tracer), limit 30 (`.../crap_ratchet.py:17`); clones = normalised `ast` windows, identity without path or line (`.../dup_ratchet.py:24-26`).
- owns: C:/QAFactory/forge2-repo/forge/tools/crap_ratchet.py, C:/QAFactory/forge2-repo/forge/tools/lint_ratchet.py, C:/QAFactory/forge2-repo/forge/tools/clone_ratchet.py, C:/QAFactory/forge2-repo/forge/baselines/, C:/QAFactory/forge2-repo/forge/tests/test_ratchets.py
- deps: C1-6; F10, F17.
- keys: K1 empty repository: three exit 0; K2 a seeded offender per tool -> exit 1 naming it; K3 a baseline row without reason -> exit 1; K4 no coverage -> CRAP exit 3.
- edges: first run, no baseline file -> empty list (absence is the strictest reading, never "no check"); malformed baseline -> exit 2; unparsable file -> red, never baselined; coverage absent or tests not exit 0 -> coverage part `not judged`, exit 3 (FR-59); fixed offender -> `gone`, green, removed by `--update`; pyflakes/coverage not importable -> exit 2 with the install line (an unrun tool is never green).
- test: `forge/tests/test_ratchets.py` one table, tool x {empty repo, offender, no baseline, malformed, unparsable, gone, tool missing} | expected from: plan 3.6, 4.2; this card.

### C1-4 Token tools: journal, dispatch header, trim, snapshot
- amended by: B2, B5, B7, B9, B14, B15, B17, B18 (cards whose `amends:` line names this card; read them with it)
- Delivers: `journal.py` (append-only `logs/journal/<session>.jsonl`; `ts` UTC, `task`, `event` of a closed list, `by`, `note` <= 300 chars; a lock serialises writers; a fix is a new line); `dispatch.py` (prints and checks the rule 11 R11-f header lines -- `given`, `owns` absolute in the repo, `non-goals`, `handoff`, `edges`, `DoD` with a backticked command, `siblings`, `test`; names each missing line; a called tool, no gate); `trim.py` (last N lines, default 30, plus lines matching given patterns; first line `[trimmed K of M lines]`); `snapshot.py` (code writes `logs/journal/snapshots/<ts>.md`: open tasks, last 20 journal lines, `git status --short`, branch; trigger: C1-5's pre-compaction hook, F18 (a); also callable by hand).
- owns: C:/QAFactory/forge2-repo/forge/tools/journal.py, C:/QAFactory/forge2-repo/forge/tools/dispatch.py, C:/QAFactory/forge2-repo/forge/tools/trim.py, C:/QAFactory/forge2-repo/forge/tools/snapshot.py, C:/QAFactory/forge2-repo/logs/journal/, C:/QAFactory/forge2-repo/forge/tests/test_token_tools.py
- deps: C1-6; F18.
- keys: K1 a line written and read back; K2 301-char note refused with its length; K3 manifest without `owns` named; K4 1000 lines trimmed to marker + 30; K5 empty journal -> snapshot `no journal lines`.
- edges: note over 300 -> refused, never cut (a cut note loses a fact); unknown event -> refused with the list; journal absent -> created on first write; unparsable line on read -> named with its number, never skipped; trim input under N -> whole, no marker; the last line (exit/summary) never dropped; non-UTF-8 output -> replaced, the marker says so; two writers -> both lines land.
- test: `forge/tests/test_token_tools.py` one table: journal write/refuse/concurrent, dispatch per missing key, trim at/beyond N, snapshot empty/full | expected from: plan 3.3; fr:D14; rule 11 R11-f.

### C1-5 Forge hooks: push, release, foreign write, secrets, pre-compaction; the ONE secret table
- amended by: B2, B5, B8, B9, B11, B14, B17, B19 (cards whose `amends:` line names this card; read them with it)
- Delivers: AS CONTENT (the Lead registers PreToolUse hooks in `.claude/settings.json` and sets `git config core.hooksPath forge/hooks/git` at acceptance): `forge/hooks/git/pre-push` -- runs `forge/tools/ci.py` (F19 (a)), red -> refuse; release: a pushed `v*` tag or branch `release` needs `owner-word: «<words>» <date>` in the tagged commit (P13, fp:A16); `forge/hooks/foreign_write.py` (PreToolUse on Write/Edit/Bash: refuses a target under a root of `forge/hooks/protected-roots.json` -- `C:/QAFactory/ao3-wrapper`, `C:/QAFactory/mybooks-stand/MyBooks`, `C:/QAFactory/mybooks-stand/test-automation-framework`, `C:/QAFactory/forge-repo`); `forge/hooks/git/pre-commit` (staged `.env*`, key-shaped tokens of a row of the one table); `forge/hooks/pre_compact.py` (F18 (a): calls `snapshot.py`, writes only, never refuses); a live probe per hook (fp:A22).
- THE ONE SECRET TABLE (AR-15, verdict fix 19): `factory/data/secret-patterns.yaml`, rows `id`, `kind` (`path_glob|token_regex`), `pattern`, `what`; shipped with the factory, English; readers: this pre-commit hook, the factory `secrets` hook point (C4-5, part 3; part 1 2e), `rows.py` at launch (C3-2, part 3; part 1 2b). No second pattern list anywhere.
- owns: C:/QAFactory/forge2-repo/forge/hooks/, C:/QAFactory/forge2-repo/factory/data/secret-patterns.yaml, C:/QAFactory/forge2-repo/forge/tests/test_hooks.py
- deps: C1-6 (F19); C1-4 (`snapshot.py`); F18.
- keys: K1 each hook refuses its case, passes its clean twin; K2 a probe receipt per hook after placement (Lead); K3 hooks on no other event (plan 3.5 + the pre-compaction event, F18 (a)); K4 the pre-commit hook holds no pattern of its own (all from the table).
- edges: before placement -> inert; after placement a change comes as `<name>.next`, placed by the Lead (an unreviewed hook never gates work); crash on push, release, secrets -> refuse (irreversible fails closed); table absent, unreadable, or a row with an uncompilable `pattern` -> the forge secret hook refuses the commit naming the file and door "restore `secret-patterns.yaml` (C1-5)", and C4-5's point fails closed alike (part 1 section 6: never an empty list, AR-28); pre-compaction hook crash -> fails open, the miss logged (it never refuses work); Bash: only literal paths recognised -> errs GREEN on indirect writes, residual named; `arm.py` refuses protected targets itself (second road to the same roots); writes into `copies_root` -> allowed; no remote (F14) -> git fails, the hook still runs.
- test: `forge/tests/test_hooks.py` one table, strongest first: hook x {case, twin, crash} + secret table {absent, unreadable, bad pattern} + push calls `ci.py` + Bash path forms + pre-compaction writes, never refuses | expected from: plan 3.5; P8; P13; AR-15; part 1 section 6; this card.

### C1-6 CI and test rule (F14); one job list
- amended by: B3, B4, B8, B11, B13, B15, B16 (cards whose `amends:` line names this card; read them with it)
- Delivers: `forge/TESTING.md` (tests on tool code only; layers: stories on real run artifacts once they exist, data joints; one parameterised table per behaviour; `expected from:` spec, rule or owner's word, never code output; test lines <= code lines; new file <= 10 s; CI canon within an hour, fp:A15); `forge/ci-jobs.json`, the ONE job list (rows `id`, `command`, `card`: tests, lint, clone, CRAP, size, universality+English, pages check and W1 once built), read by `.github/workflows/ci.yml` (matrix from the file) and by `forge/tools/ci.py` (F19 (a); runs its rows locally); neither holds a list of its own (verdict fix 19).
- owns: C:/QAFactory/forge2-repo/forge/TESTING.md, C:/QAFactory/forge2-repo/.github/workflows/ci.yml, C:/QAFactory/forge2-repo/forge/ci-jobs.json, C:/QAFactory/forge2-repo/forge/tools/ci.py
- deps: C0-1; F10, F14, F19.
- keys: K1 `ci.py` exit 0 on the repo; K2 a seeded offender -> exit 1 naming the job; K3 TESTING.md lists the legal `expected from:` sources; K4 no job id or command in `ci.yml` or `ci.py` outside the list.
- edges: a job whose tool is not built -> `not built: <job>`, listed, never silent green; `ci-jobs.json` absent or malformed -> `ci.py` exit 2 naming it, `ci.yml`'s list step red (never green on no list); not pushed (F14) -> the same rows run in the pre-push hook through `ci.py`.
- test: none -- config, rule text; `ci.py`'s door is in C1-5's push rows (F19 (a)); witness: `ci.py` green + the seeded red + `ci-jobs.json` moved away by byte copy -> exit 2 (negative controls).

### C1-7 Calibration carry list, empty symmetry map
- amended by: B9 (cards whose `amends:` line names this card; read them with it)
- Delivers: `forge/calibration.md`: a row per carried old weekly check -- number, caught case (line in `C:/QAFactory/forge-repo/logs/journal/` or `docs/retro/`), outcome protected, how run now (tool, acceptance question, weekly reading); every other of the 52 (fp section B): `dropped: <reason>` (no caught case, or machinery, fp section C). `forge/siblings.md`: empty axis table (axis, what ties, caught case) and the rule: an axis is born only from a caught case (plan 3.8).
- owns: C:/QAFactory/forge2-repo/forge/calibration.md, C:/QAFactory/forge2-repo/forge/siblings.md
- deps: C0-1.
- keys: K1 52 numbers each once; K2 every carried case opens to a line naming the catch; K3 zero axis rows.
- edges: search finds nothing -> dropped, the command and its positive control written (hygiene pt 6); a catch only in the frozen package -> dropped (no package code in forge 2).
- test: none -- markdown; witness: key script with a negative control. Carried count: `estimate`, the builder measures.

Bodies C2-1..C2-8: part 2b, `docs/tasks/specs/20261125-forge2-light-factory-spec-part2b.md` (moved byte for byte by the Lead's script at acceptance, F52 (a)).

## 3. Forks

F15-F23 (plan v1.3 "Reshila sama"): bodies apply (a). F50-F52: taken as option (a) by the Lead until the owner's word.

**F15** (C0-3, C0-5): which free prompt (the used one is under `runs/`, ao3 `RUN-INSTRUCTIONS.md:18`)? (a) Past filled prompts, money-checked by the Lead, ao3 placeholders restored: continuity with 12.11, 24.11. (b) One new template. Status: taken as option (a) by the Lead until the owner's word.

**F16** (C1-1): typed agents need `.claude/agents/`; plan 3.4 says one file. (a) Thin role files inside the 12 KB. (b) None: no per-role tool limits. Status: taken as option (a) by the Lead until the owner's word.

**F17** (C1-3): which ratchets? (a) New at zero: `ast`, pyflakes, `coverage` (tracer `estimate`: `python -c "import coverage, pyflakes; print(coverage.__version__)"`). (b) Old tools (337, 483, 520 non-blank lines, Grep `.` count, `C:/QAFactory/forge-repo/tools/{lint,crap,dup}_ratchet.py`). Status: taken as option (a) by the Lead until the owner's word.

**F18** (C1-4, C1-5; plan 3.3 vs 3.5): snapshot trigger? (a) Fifth hook, pre-compaction, writes only, fails open. (b) By hand: auto compactions missed. Status: taken as option (a) by the Lead until the owner's word.

**F19** (C1-6; part 1 F14): `forge/tools/ci.py` unowned. (a) C1-6 owns it, door in `test_hooks.py` push rows. (b) The hook parses `ci.yml`. Status: taken as option (a) by the Lead until the owner's word.

**F20** (C0-1): spec home after the copy? (a) `forge/specs/`, forge-repo copies frozen. (b) Mirror: drift. Status: taken as option (a) by the Lead until the owner's word.

**F21** (C0-5, C2-7; part 3 C4-7): where run outputs live? (a) Run folders `measure/runs/baseline/`, `measure/runs/craft-pages/`, money stripped, raw logs in `copies_root`. (b) Outside, by sha256 (fr:A24). Status: taken as option (a) by the Lead until the owner's word.

**F22** (C2-4): stage 2 had no page (refs:A29, A30; slices:A9, A22, A25). (a) `factory/craft/stand.md`. (b) Fold into `exploration.md`: W1 names stage 2 missing. Status: taken as option (a) by the Lead until the owner's word.

**F23** (C2-7): what accepts the pages? (a) No worse than the baseline's worse run per countable row; seeded catches >= `without`, no more false alarms; wall, tokens within 5x (over 2x a finding). (b) Seeded sets only. Status: taken as option (a) by the Lead until the owner's word.

**F50** (C2-6; plan v1.3: truth-table bugs never seeds, both projects): where seeds come from instead. (a) Inputs authored for each set, incl. a small static fixture product with planted roots for manual-pass/exploration -- costs authoring the fixture, never touches a measured product. (b) Faults planted into a measuring copy of MyBooks at places no truth card names -- cheaper, realistic, but the pages arm meets the measured product before C2-7 and C4-7. Rec (a); C2-6 is written to (a).

**F51** (C2-8; plan phase 2 row says "six stages"; part 1 section 3 puts a critic in G3, G4, G6): (a) Walk the three critic contexts too (nine contexts) -- the "within 2x" ceiling covers the whole story, so leaving them out errs green. (b) Six stage contexts only, critics named unmeasured -- cheaper, but the outcome can then only be `incomplete`. Rec (a); C2-8 is written to (a).

**F52** (rule 8 size cap vs the brief's "one body to part 3"): this file, complete, is over 40000 bytes (estimate, section 5); no single body frees enough (largest C2-1, about 4.6 KB). (a) Phase 2 bodies C2-1..C2-8 move whole to `...-spec-part2b.md` (owns disjoint from C0-*, C1-*); the part 1 index column `P2` reads `P2b` for them -- two documents under the cap, nothing cut. (b) C2-1 and C2-8 move to part 3 -- fewer files, but phase 2 bodies split across two parts. (c) The cap is raised for this file -- not the designer's call. Rec (a). Decided (a): the Lead's script moved the bodies byte for byte at acceptance; nothing cut.

## 4. Small choices closed
- Digest-scoped ids `refs:`, `slices:`, `fr:`, `fp:` (all digests use `A<n>`).
- One test file per tests-owning card, one table each (TESTING.md «Бюджет / Файлы»); `arm.py` rows live in `test_score.py`, its docstring names both tools.
- The English check is the second scan of `universality.py` (scope all of `factory/`; names scan `factory/tools/`, `factory/hooks/`).
- Snapshots in `logs/journal/snapshots/`; `protected-roots.json` in `forge/hooks/` (inside owns).
- `score.py`'s rule table is a constant citing its source lines (same for both projects: one home).
- Stand scripts byte for byte; machine paths restated as `project.yaml` rows.
- ao3 truth version `v2026-11-25-hand`; `judgment/2` (closed verdicts), `judgment/1` kept as history.
- Ratchet exits 0/1/2/3 as the old forge (`crap_ratchet.py:30-36`).
- Freeze = the card's acceptance commit, its hash in the hand-back and journal line (a commit cannot carry its own hash).
- C2-8: the MyBooks story (stand and answers in place); ratio against the baseline mean, spread beside it; run rows as a table in its one owned file, stub and raw logs in `copies_root`.
- `secret-patterns.yaml` and `ci-jobs.json` row shapes as in C1-5, C1-6; run results named `result.md` inside the run folder.
- Part 3 copied into `forge/specs/` at its acceptance (C0-1).

## 5. Trail
- Read: part 1; plan 16-45, 170-215, 927-983, 1062-1263; the five given digests; mybooks truth, `judgment.yaml`, `factory-vs-free-agent.md`, `free-agent-prompt.md`, `answers/README.md`, `RUN-INSTRUCTIONS.md:1-80`; ao3 `RUN-INSTRUCTIONS.md`, `factory-vs-free-agent.md`, `answers/README.md`, `notebook.md:470-494`; `stand.ps1` heads; `docs/TESTING.md:36-125, 217-256`.
- Read for r1: part 1 r1 lines 1-369 (Revision r1, section 1, 2a-2g, 3, index of 4, 5, 6, 7); plan v1.3 headings, «Фазы» 1078-1095, «Цена» 1186-1201, "Reshila sama" 1226-1265; verdict t-1915 lines 70-121 (fixes 9-19), 220-234.
- Measured: Glob listings (mybooks `factory-vs-free-agent/{answers,stand,story}/**`: 31 files; ao3 folder top: 3; `judgment*.yaml`: 1); `XPANBFLFA-44.xml` named at `RUN-INSTRUCTIONS.md:97-98` (Grep); old ratchets non-blank lines (Grep `.` count: lint 337, crap 483, dup 520) and imports (Grep `^(import|from)`); old lint ratchet = pyflakes (`lint_ratchet.py:1`).
- Lead facts (t-1918 `facts:`): r0 at 3b6da0190, 39183 bytes; no C2-8; index 20 rows `| P2 |`; the two one-file run results named twice each (now 0); `secret-patterns` 0.
- Not read: every file under `experiments/**/runs/` (names seen in Glob only).
- Estimates (Lead commands): `XPANBFLFA-44.xml` location (`Get-ChildItem C:/QAFactory/mybooks-stand -Recurse -Filter XPANBFLFA-44.xml`); `coverage` tracer (F17); carried calibration count (C1-7); this file's size, `estimate`: Grep line-length bands (`^.{N,}` counts for N = 50..1500 step 50; 268 lines) on the first r1 write gave at least 45 KB of characters, about 51 KB with a 25-character mean remainder per line; the revision block and section 3 were then shortened (about 2.5 KB) -- `python -B -c "import os,sys;print(os.path.getsize(sys.argv[1]))" <this file>`.
- Readers (rule 7): every file is new in an empty repository. Shared files inside this spec: `secret-patterns.yaml` -- written by C1-5 only; read by C1-5's pre-commit, C4-5 `secrets`, `rows.py` (part 3), unchanged there; `ci-jobs.json` -- written by C1-6; read by `ci.yml`, `ci.py` (C1-6) and the pre-push hook through `ci.py` (C1-5), unchanged; `arm.py` -- written by C0-4; called by C2-6, C2-7, C2-8, C4-7, unchanged there.
- Plan vs part 1: r0 disagreements F18, F19 closed by (a); plan "phase 2 parallel to 1" vs part 1 section 6 decided by part 1 (C2-1 code waits); plan v1.3 extends the F5 seed rule to both truth tables (C2-6).
