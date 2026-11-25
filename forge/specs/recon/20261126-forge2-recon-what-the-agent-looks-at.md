# Recon digest t-1950: what the current factory tells its agents to look at on their own, what came from exploratory testing and charters, and whether the forge 2 spec names it

Scout hand-back of 26.11.2026, saved verbatim by the Lead (the scout writes no file). Accepted by trail: the Lead re-checked the four perturbation axes of references/perturbations.json, the absence of skills/qa-explore, the two quoted lines (qa-runner.md:54, qa-failure-analyst.md:56) and the negative claim (no heuristic-set or session-based name in agents/ and references/: 0 files, control oracle: 8 files). plans/exploratory-charters-proposal.md, cited by a finding as the source of ten axes, is not in the tree.

digest: v1 t-1950

Note on form: the DoD greps four headings with "^#+ ". The four sections below use "## " headings, as the DoD requires. The digest tables (Objects, Trail) come after them. Prose is kept short.

## What the agent looks at

Package root: C:/QAFactory/forge-repo/ai-packages/qa-factory (shortened to `P/` below). Paths and line numbers are real. Quotes are copied from the Read output.

There is no "analyst walks places by a list of tours" in the package. The looking is spread over seven things. None of them is named a charter, tour or heuristic set, with one exception: the strategist technique "Exploratory charters" (item 7).

1. **Analyst, S7 (`P/agents/qa-failure-analyst.md`).**
   - Looks at: every red, and every manual `observation` and recorder `surprise` line.
   - "Find out the truth on the page" (line 56): "every suspicious place nobody has confirmed is walked before you leave it: do what a person would do, a step or a short run at a time, look, decide the next."
   - Lists of what to notice:
     - "Where bugs hide" (lines 33-46): the comfortable reading, a timeout that is a race, test data weaker than the Given, an assert stricter than the requirement, a defect older than the story, one red hiding the Thens behind it, a runner whose captures contradict its verdict, several reds with one cause, behaviour that depends on the start state, and a suspicion left as the run left it.
     - Techniques (lines 51-65): control experiment, isolated reruns before "flaky", lay the drafts side by side, discriminate the cause by changing the start state.
   - Bounds:
     - Three isolated reruns before FLAKY.
     - A probe pass: 12 probes, 3 reproductions per target, a 20-minute timebox, read-only GET/HEAD/OPTIONS (`P/references/investigation-budget.json:4-8`).
   - Must leave: a triage row per failure with evidence path and `R-n` quote. It must also leave a `<case>#obs<n>` / `<case>#sur-<id>` row for each manual observation or surprise, and a draft in `work/bug-drafts/`.

2. **The "places" of S7 (`P/references/place-answers.json`, `P/scripts/place_answers.py`, `P/skills/qa-story/phases/s7.md:100-111`).**
   - What a place is: a suspicion the run left unconfirmed, joined from records that already exist. Sources are register rows, investigation targets (`case-`, `obs-`), drafts and the analyst's own `new-<slug>`.
   - Place id pattern: `^(req-R-\d+|case-.+|obs-.+|draft-.+|new-[a-z0-9-]{1,40})$` (line 10).
   - Bounds: `"brief_places_max": 40`, `"brief_neighbours_max": 10` (lines 17-18).
   - The walk itself: `manual_capture.py ui|http --case settle-<place id>`.
   - Must leave: ONE `evidence/place-answer-*.json` per place. The answer is one of "bug", "not_a_bug", "requirement_silent", "impossible". The expectation source is one of "requirement", "question", "person", "none" (`none` never for a bug). The record must carry a capture of this place and a quote from it.
   - If the analyst leaves a place unsettled, `close_unsettled` writes a gap. There are five `gap_reasons`.

3. **Walker, S6 (`P/references/walk-charter.md`, `P/scripts/walk_session.py`).**
   - How it walks: it reads the item and the app card, and "never read the application's sources" (line 4). It types "one character at a time" (line 14).
   - "A focus loss the recorder names is a finding of the item, never noise: no pass over it, ever." (line 14-15)
   - Steps per call: a manual case sends all steps at once. "Exploration cells, and any walk where the next step depends on the page, do not: send ONE step, or two or three obvious ones, look, decide the next." (lines 19-20)
   - The recorder stops at the first deviation. "Never send the same steps again unchanged" (line 26).
   - Must leave: "Every doubtful place is an observation: `step`, `expected`, `seen`, the `capture` and a `quote`" (lines 33-34). Also "The oracle is the requirement, never what the application happens to do" (line 35).

4. **Runner charter, S6 (`P/agents/qa-runner.md`).**
   - Craft "Where bugs hide" (lines 30-37), eight places: the step before the first Then; a field saved on every change; the same field emptied and past the limit; a dependency that fails; the state after an error; reload or back mid-save; state held before sign-in and merged on sign-in.
   - Techniques (lines 42-54): walk as a user; record the oddity at once; hypothesis before the route; "The axes to perturb: a request failing, a field keyed, an input at its edge, a reload."; boundary values; state transitions; state before and after; tell the stand from the product; and First look.
   - First look (line 54): "no test-design techniques here, you ask 'is it there, and where', not 'does it hold'". It makes one short path per requirement. Status words: `missing`, `unreachable`, `access`, `nature`. It is sent once with `first_look.py put`.
   - Stage: S3, optional, before the plan (`P/skills/qa-story/phases/s3.md:12-18,40`).

5. **Exploration cells (`P/references/explore-charter.md`, `P/references/perturbations.json`).**
   - What it is: the "Exploration charter - qa-runner at S6". The brief's `Exploration cells:` line names the cells. The same file says "read with your brief".
   - The matrix (`perturbations.json`, 4 axes):
     - `request_failure` (kinds `500`, `timeout`)
     - `keyboard_input` (kinds `multi_digit`, `empty`, `paste`, `beyond_limit`)
     - `reload_mid_operation` (kind `reload`)
     - `session_transition` (kinds `sign_in_with_state`, `sign_in_merge_failed`)
     - Each axis carries an `oracle` sentence, for example: "the page stays alive (the rest of it still shows), the person is told of the error in words, and no data is lost silently".
   - Cell form: `<axis> x <request or field> x <kind>`.
   - Techniques (lines 46-71): start from the first look; hypotheses before the route (`H-n` with an oracle and a refuting observation); one cell per call with a control; fail first, then act; vary the start; the sign-in cell; the `surprise:` line.
   - Tools: `look`, `watch` (at most five), `fill --whole`, `fail_request`.
   - Must leave: `work/evidence/manual/<case>/tried.md` with columns cell, hypothesis, oracle, refuted by, outcome, seen, evidence. Each `violated` row must also be an `observations[]` entry.
   - Quote (lines 30-31): "'Nothing broke' is an outcome only with the table: an empty `observations[]` and an empty register with no `tried` rows is not a clean result, it is an unexplored flow, and it is returned."
   - Bound: the number of cells is taken from the brief; there is no count cap in the file. `P/references/exploration.json:7-24` has limits for the other exploration (item 6): `turns_per_scout` 60, `e2_files_per_scout` 60, `hits_per_file` 5.

6. **`qa-explore` feature exploration (`P/references/exploration.json`, `P/scripts/exploration.py`, `explore_step.py`).**
   - It is not about looking at the product. It is a requirements and code search: steps E1 (requirements via qa-scout), E2 (feature map per repo via qa-scout), E3 (coverage matrix via qa-requirements-tester).
   - The skill `skills/qa-explore/` does NOT exist in the package (ev T15, T16). The batch code is partly there: `exploration.py`, `explore_step.py`, `exploration.json`. `feature_map.py`, `feature_hits.py`, `requirement_search.py` and `references/feature-map-form.json` are absent (ev T18).
   - `exploration.json` itself says its writers and readers "may be scripts of later nodes ... nothing here checks that they exist".

7. **Strategist, S3 (`P/agents/qa-test-strategist.md`).**
   - Where bugs hide (lines 32-46): the changed branches of the diff; a changed branch no row walks; "Seams between features. Where the changed code hands data to code it did not change"; shared mutable state; permissions and roles; concurrency; failure of a dependency; migrations; flags; the second time and the undo; leftovers; counts computed twice; norm rows.
   - Technique line 62: "Exploratory charters. When a risk is real but the result unknown, plan a time-boxed exploration with its mission and what counts as a finding."
   - Good outcome item 4: "Every function is walked", with a `walks` field.
   - Nothing in the package defines a charter form for this technique. It is one line.

8. **Observation register (`P/scripts/exploratory_findings.py`).**
   - `work/exploratory-findings.jsonl`. Kinds: `observation`, `unresolved_question`, `coverage_gap` (line 36). Statuses: `unverified`, `reproduced`, `not_reproduced`, `environment_event`.
   - Oracles: `none`, `documented_text_only`, `owner_question`, `person_confirmed`.
   - Must leave: `--why-not-a-bug` and `--evidence`. An entry is "never a product bug" (lines 3-6).

9. **Other charters that list places to look at** (not looking at the live product, but "where bugs hide" lists, same form):
   - `qa-requirements-tester.md:32-45` (14 places: compound requirements, implicit conditions, roles in the plural, failure and refusal, boundaries nobody wrote, and others).
   - `qa-requirements-tester.md:50-62` (techniques: equivalence partitioning, boundary value analysis, decision tables, state transition analysis, cause and effect, CRUD per object).
   - `qa-case-designer.md:31-44` (13 places) and 49-57 (techniques, including error guessing).
   - `qa-scout.md:32-47` (15 places: comments after the description, attachments, parent and siblings, linked bugs, requirements in disguise, deleted code) and 52-56.
   - All of these read documents or plans, not the running product.

Form of every charter: `P/references/charter-form.md` (six sections: Outcome, Good outcome, Where bugs hide, Techniques, Tools, When to ask). It allows at most 150 lines. It is checked by `P/scripts/charter.py` (audit A19).

Files in the package that match the names (case-insensitive: analyst, explor, charter, tour, heuristic, seam, transition; also the Russian forms). Total matches: 6891 occurrences in 738 files. Only counts were listed in full; the file list was cut at 120, so the rest is grouped.
- ABOUT looking at the product (listed above): `agents/qa-failure-analyst.md`, `qa-runner.md`, `qa-test-strategist.md`, `qa-requirements-tester.md`, `qa-case-designer.md`, `qa-scout.md`; `references/explore-charter.md`, `walk-charter.md`, `charter-form.md`, `perturbations.json`, `exploration.json`, `place-answers.json`, `investigation-budget.json`; `scripts/exploration.py`, `explore_step.py`, `exploratory_findings.py`, `place_answers.py`, `walk_session.py`, `first_look.py`, `investigation_probe.py`, `user_path_failures.py`; `skills/qa-story/phases/s3.md`, `s7.md`, `s9.md:193-196`.
- NOT about looking at the product (the match is the word "analyst", "transition" or "explor" used in another sense, one line each):
  - `agents/qa-retro-analyst.md`: a retro role.
  - `agents/qa-code-critic.md`, `qa-case-critic.md`, `qa-bug-reporter.md`, `qa-doc-scribe.md`: "oracle" and "test input seam" for code review.
  - `handoffs/*.yaml`, `handoffs/vocabulary.yaml`: handoff names such as `s6-runner-to-analyst`.
  - `references/stage-joints.json` (169 matches): stage "transition" joints.
  - `references/artifact-contract*.md`, `slices/`, `stages.json`, `field-producers.json`, `artifact-writers.json`, `role-commands.json`, `null-outcomes.json`, `inject-map.json`, `config-keys.json`, `gate-registry.json`: role and analyst wiring.
  - `design/state-exits.md`, `architecture.md`, `role-rules.json`, `factory-rules*.md`: design notes.
  - `scripts/driver_*.py`, `audit_factory.py`, `contract.py`, `contract_slices.py`, `brief_pack.py`, `gate_*.py`, `report_facts.py`, `refusal_registry.py`, `s7_pretriage.py` and others (about 100 files): machinery that dispatches the analyst or checks charters.
  - `scripts/tests/*`, `CHANGELOG.md` (190 matches), `changelog.d/*` (about 40 files, for example `fv1-24-place-born-draft-walk.md`, `onboarding-hooks-5-oh5-2b-charters-card.md`, `tr4-15-analyst-ratchet-raise.md`): tests and history.
  - Not read line by line: `s7_pretriage.py` and `first_look.py` (see Not done).

## From exploratory testing and charters

Claim in the question: part of the analyst's look was built from exploratory testing and from how charters are written.

A. What the package says about it.
   - The word "exploratory" appears in these package files: `agents/qa-test-strategist.md:62` (technique "Exploratory charters"); `scripts/exploratory_findings.py` (the register's name); and `explore-charter.md` with its title "Exploration charter" and the walker cells.
   - There is no text in the package naming session-based testing, tours, a heuristic set (HICCUPPS, SFDIPOT, FEW HICCUPPS), or an author (Bach, Hendrickson, Whittaker, Kaner). Search with the case-insensitive grep over `agents/` (T6) found only `Exploratory charters`, "oracle" and the words in the rows above. The `charter` in `charter-form.md` is a different meaning: "A role's `agents/<role>.md` is a charter: the experience of a tester at one stage, not a procedure" (line 3).
   - The code comment of the explore charter (`explore-charter.md:70-71`) says the rest of the craft "is in the runner's own charter".

B. What the pile INTENDED (`plans/piles/exploratory`; text is Russian, paraphrased).
   - README (lines 7-11): the pile adds a skill `/qa-factory:qa-explore "<функция>"` that finds requirements and code of a function, checks coverage, "придумывает чартеры с гипотезами, исследует приложение и пишет недостающие тесты".
   - README line 19: "Чартеров, гипотез, осей возмущений, карты швов в пакете нет" (at pile time, 31.10.2026).
   - Sources named for batch 1: requirements from "всех источниках онбординга, не только Jira" (batch 1 line 9): Jira JQL (XT1-3), Confluence CQL and git documents (XT1-4). Code is found with `git grep` across all repositories (XT1-5).
   - Feature map: XT1-6 (form of the feature map; scout modes E1 R-n, E2 hits only) and XT1-7 (coverage matrix: path or rule x {case, autotest, unit, nothing}).
   - Charter form: batch 2 line 12, outside samples. "образцы чартеров — `Xartaxana/ideal-test-factory` (`charter-designer`, `exploratory-tester`, `templates/charter.md`) и `exploratory-charters/PERTURBATIONS.md` Darker-фабрики". README line 49 says the same for batch 2 only, "для пачки 1 не читать".
   - The perturbation matrix: `plans/exploratory-charters-proposal.md` is cited as the source of "10 осей предложения" (release-next finding line 61). The file was not opened, since it is not in the four named files; see Not done.
   - The nodes that carry the matrix: XT2-2 (batch 2 line 28): axes `request_failure`, `keyboard_input`; acceptance is that the skill finds three MyBooks cart bugs (Б-1 "нельзя набрать «12»", Б-2 `GET /api/books/{id}` 500 takes the cart page down, Б-4 `POST /api/cart/merge` 500).
   - "Personality of exploration" (batch 3, name `lichnost-issledovaniya`): the pile means the PROCESS IDENTITY of the exploration (labels `Exploration: <slug>` and `QA_FACTORY_TASK=explore:<slug>` read by the guards before a story; batch 1 line 31 and batch 3 XT3-1). It is not a tester's personality or a charter style.
   - Not opened as to content: `plans/piles/speed-cost/batch-4-problem-2-exploratory.md` and `.../findings/20261027-fb13-kontrakt-otchyota-issledovatelskih-nablyudenij.md`. Only a grep for charter, tour, heuristic or observation words was run. The FB-13 title reads: "контракт отчёта для исследовательских наблюдений, пробелов покрытия и открытых вопросов о продукте". `docs/tasks/specs/t-1630-xt1-exploratory-batch-1.md` was grepped, not read; line 767 cites the proposal and the pile README only.

C. BUILT in the package vs. NOT BUILT.
   - Built: `charter-form.md` and `charter.py` (the role charter form); `explore-charter.md` (the runner's exploration cells, hypothesis, oracle, `tried.md`); `perturbations.json` (4 axes, 9 kinds, oracles per axis; the cells are printed into the brief); `exploratory_findings.py` (the observation register); `exploration.py`, `explore_step.py`, `exploration.json` (the E1-E3 frame and walk).
   - Not built (pile or finding only): the skill `skills/qa-explore/` (absent); `feature_map.py`, `feature_hits.py`, `requirement_search.py`, `references/feature-map-form.json`, `references/explore-modes.md` (absent, ev T17, T18); XT2-1 (product map at onboarding); E4-E5 charter nodes with hypotheses as separate roles ("две новые роли", README open question 1-4); E6-E7 (missing tests, report). All open nodes moved on 01.11.2026 to `release-next/1` and `execution-report/1`. Pile batch 3 (XT3-1) is "ожидает". `perturbations.json` is built for S3 request rows and the S6 brief; the pile's other proposal axes are absent from it (it has 4 axes).
   - Also in the packages: `plans/piles/thinking-roles/README.md:71` says "Не читать: кучки `execution-probes`, `exploratory`, `driver-controller` — их узлы написаны для пакета другого репозитория" (not read as input). Its line 83 names `references/walk-charter.md` as an object of a finding. `docs/factory-map` holds only `.svg` graphs (the control grep found `analyst|walker|runner` there); no text on charters, tours or exploratory testing was found there (T12, with control T13).

## Against forge 2

Forge 2 spec files read: part 5 (A24 r2, lines 28-45), part 4 (A4, lines 59-68), part 4-3 (A24 r1, lines 3-9), part 2b (C2-4, lines 48-55). Paths are under `C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part*.md`.

| item of Q1 | in forge 2? | card key and words |
|---|---|---|
| Stage-2 look (product performer looks "as a free agent and not deep") | found | A24 r2 Delivers, part5:40: "where things lie; does the product start; is the feature there at all; is it grossly broken; what is visible beyond the requirements" |
| Row it must leave | found | A24 r2: `findings` row `kind: beyond`, `outcome: matched/asked/not_done`, or `empty: nothing_beyond` with a reason; part5:40,44 |
| Bound | found | part5:40: stage caps row (A1) cuts the launch; "the look's share inside the stage is the performer's judgment, told at entry"; no count or time number of its own |
| Stage-5 look (analyst's places) | found | part5:40 "STAGE 5 LOOK (F90 (a), unchanged): the analyst's places -- what the bugs touch, seams, transitions between screens and states"; launch at `reds` (A24 r1 line 9) |
| Stage-5 bound | found | `explore` row 600 s, 100000 tokens, 30 turns (part4:27, A24 r1 F74); a goal row is needed (A24 r1 line 9) |
| Craft page `exploration.md` (C2-4) | found, no content | part2b:48-55: C2-4 delivers the file; `refs:A20`; the card holds no page text. A24 r2 line 39 adds a rule `amend:A24`; A4 amends the same page |
| Bug-or-not for a suspicious look | found | A4 and A24 r2: `ask.py ask --form bug_or_not --section beyond`; options `bug`, `should_be_so`, `intended`, `decide_later` (part4:61) |
| Places as a suspicion list with answers (the old `place_answers`) | not found | words searched: seam, transition, boundar, place, hypothes, perturb, charter, tour, heuristic, first look; see Trail T9-T11 |
| Seams, transitions between screens and states | found as three words in a list | part5:40 (the only hit for "transition"); part4 lines 11, 30 hit "seam" (see Trail T9: not read, claim for the word only) |
| Perturbation axes (request failure, keyboard, reload, sign-in transition) | not found | search `perturb`: zero matches (T8, control T9) |
| Hypothesis and oracle before the capture, `tried` table | not found as exploration rule | `hypothes`: zero matches (T8); the closest text is A4 "expectation ... kind `none` ... `person_word`" |
| First look (before the plan, per requirement) | not found | `first look`: zero matches (T8); the nearest idea is the stage-2 look above |
| Charter, tour, heuristic set, session-based testing | not found | words `charter`, `tour`, `heuristic`, `session-based`: zero matches (T8, T9) |
| Observation register with kinds and oracles | partly | `findings` rows with `kind: beyond/proposed_test` replace it |
| Walk steps (one step, look, decide) and recorder stops | not found | not in the four files, which are cards and not walk craft |
| Boundary values, state transitions as design techniques | not found | `boundar` matches only in other senses, `transition` once (part5:40) |
| Hard limit "nothing broke needs the table" | not found | `tried` as a table: no match in the four files |

"Explor" occurs 48 times in the four files: part2b 5, part4-3 16, part4 7, part5 20.

Caution: Trail T8 (the first search over the four files for `charter|tour|...`) returned zero. A first run with `\b` returned zero too, so it was rerun without `\b`, same result (T8). The control T9 (same op, target, flags, a pattern that exists: `seam|transition|boundar`) found 4 hits. The word searches of T8 are therefore a valid negative for those words.

## Trail

## Objects

| id | kind | gist | paths | status | owner | links | ev |
|---|---|---|---|---|---|---|---|
| q1a | role-charter | analyst walks every unconfirmed place on the stand; list of where bugs hide | P/agents/qa-failure-analyst.md:30-65 | found | — | q1b | T1 |
| q1b | data | places: id pattern, brief_places_max 40, brief_neighbours_max 10, 4 answers | P/references/place-answers.json:4-18 | found | — | q1a | T2 |
| q1c | data | probe budget 12 probes, 3 reproductions, 20 min, GET HEAD OPTIONS | P/references/investigation-budget.json:4-8 | found | — | q1a | T3 |
| q1d | charter | walk charter: step by step, stop at deviation, every doubt an observation | P/references/walk-charter.md:6-37 | found | — | q1e | T4 |
| q1e | charter | exploration cells, tried.md, hypothesis and oracle per cell | P/references/explore-charter.md:11-71 | found | — | q1f | T5 |
| q1f | data | 4 perturbation axes with kinds and oracles | P/references/perturbations.json:4-45 | found | — | q1e | T6 |
| q1g | role-charter | runner craft: 8 places, boundary values, state transitions, first look | P/agents/qa-runner.md:28-54 | found | — | q1e | T7 |
| q1h | role-charter | strategist: seams, shared state, diff branches, exploratory charters | P/agents/qa-test-strategist.md:30-62 | found | — | q2a | T8 |
| q1i | code | observation register kinds and oracles | P/scripts/exploratory_findings.py:36-40 | found | — | q1e | T9 |
| q1j | data | qa-explore E1-E3 requirement and code search, not product looking | P/references/exploration.json:37-64 | found | — | q2c | T10 |
| q2a | source | package names no tour, heuristic set, session-based testing or author | P/agents | absent | — | q1h | T11 |
| q2b | pile | pile intended charters with hypotheses, axes, sources; samples in outside repo | plans/piles/exploratory/README.md:7-19 | found | — | q2c | T12 |
| q2c | pile | skill qa-explore and feature map files absent in the package | P/skills | absent | — | q2b | T15, T16, T18 |
| q2d | pile | "personality of exploration" means process identity labels, not tester style | plans/piles/exploratory/batch-3-lichnost-issledovaniya-hvosty.md:25 | found | — | q2b | T13 |
| q2e | pile | docs/factory-map holds no text on charters or exploratory testing | docs/factory-map | absent | — | — | T20, T21 |
| q3a | forge2 | stage-2 look and stage-5 look named in A24 r2 | forge2 part5:40 | found | — | q1a | T22 |
| q3b | forge2 | craft page exploration.md delivered by C2-4, no page text | forge2 part2b:48-55 | found | — | q3a | T23 |
| q3c | forge2 | perturbation, hypothesis, first look, charter, tour, heuristic not in four spec files | forge2 specs part2b,4,4-3,5 | absent | — | q1e | T24, T25 |
| q3d | analog | the same class of hit: S3 first look, S6 cells and S7 places are three walks with three forms | P/skills/qa-story/phases/s3.md:40 | found | — | q1g | T7 |

## Not done

- Files not opened, only counted or grepped: `plans/exploratory-charters-proposal.md` (the source of "10 осей"), `docs/tasks/specs/t-1630-xt1-exploratory-batch-1.md` (grep only), `plans/piles/speed-cost/batch-4-problem-2-exploratory.md` and the FB-13 finding (grep returned only long lines, content not read), `P/scripts/s7_pretriage.py`, `P/scripts/first_look.py`, `P/scripts/place_answers.py` beyond its header, `P/scripts/user_path_failures.py`, `P/skills/qa-story/phases/s9.md:193-196`.
- The two release-next findings: the cart finding was read only through grep (lines 61-95).
- No file under any experiments/**/runs/ was opened. No price or spend figure was quoted.
- The full file list: the content search over the package gave 738 files; the listing was cut at 120 (`head_limit`), then grouped above. A line-by-line list of the remaining test and script files was not made.
- Part 4's two "seam" hits (lines 11, 30) were not read for meaning.
- Nothing is judged better or worse.
