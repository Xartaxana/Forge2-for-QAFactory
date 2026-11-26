Frame spec: forge 2 and the light QA factory, phases 0-4 (t-1913, F19; r1 = t-1916, r2 = t-1920, 25.11.2026). Plan: `docs/tasks/specs/20261125-forge2-light-factory-plan.md` v1.4. Review: `docs/tasks/specs/reviews/t-1915-forge2-plan-critic.md`, `docs/tasks/specs/reviews/t-1919-forge2-frame-r1-rereview.md`. Card bodies: parts 2, 2b (phases 0-2), 3, 3b (phases 3-4).

Amended by cards A, B (parts 4, 4b): see their `amends:` lines.

## Revisions
- r1 (t-1916): 22 fixes of t-1915, card bodies moved out -- see commit 12a00c2c8
- r2 fix 1 -> due at first `exit`; debtor leaves the missing part; `group`; D2 G1-only -> 2a, 2b, 2c, 3
- r2 fix 2 -> section `expectations` keyed by requirement id; ids kept -> 2a, 2b, 3
- r2 fix 3 -> preview before the critic; D1, G6.1 `after_critic` -> 2c, 3
- r2 fix 4 -> moves: `after_critic` debts, G4.5, conductor target, no-critic fixes; F60 -> 2a, 3, 7
- r2 fix 5 -> `passes` only by `ask.py`, `probes` only by `critic.py` -> 2a, 2c
- r2 fix 6 -> section `reason_verdicts` for X6, `dashboard.py` -> 2a, 2c, 2f, 3
- r2 fix 7 -> named reason "executed by agent, no evidence" -> 1, 2c
- r2 fix 8 -> comparison|night roots only from launch-time knowledge -> 2e
- Lead at r2 acceptance -> part forks F41 (`when` values), F42 (`check_group`), F43 (`decisions`), F60: option (a); bodies in P2b, P3b -> 2a, 2c, 4, 7

## 1. Frame and invariants

**Layout of `C:/QAFactory/forge2-repo`.** The SHIPPED FACTORY is `factory/` only; the rest is FORGE 2. Files inside are named by the owning card (section 4).

| Path | Part | What (card) |
|---|---|---|
| `README.md` | forge | rewritten by C0-1 |
| `CLAUDE.md` | forge | the ONE worker rules file (C1-1) |
| `forge/` | forge | rules, budgets, baselines, calibration, specs, `tools/`, `tests/`, `hooks/` (C0-1, C1-*) |
| `.claude/settings.json` | forge | hook registration, placed by the Lead (C1-5) |
| `.claude/agents/` | forge | thin role files: tools, model, pointer into `CLAUDE.md` (C1-1, F16) |
| `.github/workflows/ci.yml` | forge | CI (C1-6) |
| `logs/journal/` | forge | written only by `forge/tools/journal.py` (C1-4) |
| `measure/` | forge | `mybooks/`, `ao3-wrapper/`, `tools/`, `runs/`, `seeded/` (C0-*, C2-6..8, C4-7) |
| `factory/` | FACTORY | `craft/`, `data/`, `templates/`, `tools/`, `hooks/`, `tests/`; English only |

In a project the factory writes under `<work_root>/` (2a, 2f, 2g) and test code under the roots of key `repositories` (2e).

**Invariants kept** (how -> what shows it broken).
- AR-7, P1, FR-47: no tool is the only road but each store's writer (AR-14); a run by another road counts with `obtained_by`; manual "passed" evidence is tool-recorded (P26), else reason "executed by agent, no evidence" (why; 2c) -> a run refused for its road; agent-written proof.
- AR-6, P5: every read route, never an LLM agent: sources land whole -> a `sources` row that is another agent's summary.
- AR-8: `context.py` hands the stage its sections, pages, commands -> a performer searching the package.
- AR-9, P15, FR-1, FR-2: a refusal names the expectation and a door the refused party has; a person's word passes it -> a doorless refusal.
- AR-10, FR-38: every check is in the stage's page before work (F12) -> a debt the page never named.
- AR-11: stage start load one number under F9 -> an unreported overrun.
- AR-12, P11, FR-55: friction measured each run (C4-6) -> a dearer stage, unreported.
- AR-13, AR-14: `record.py` one reader/writer -> another writer.
- AR-15: one secret table (`secret-patterns.yaml`) for both hooks -> a second table.
- AR-16, FR-6..10: every text to the person via `ask.py` -> a stop message built elsewhere.
- AR-18: `exit_check.py` one output shape -> a second refusal format.
- AR-20: forge ratchets only shrink, raises named -> a silent raise.
- AR-21, P4: findings whole; context by code -> a retold handoff.
- AR-22: W1 walks sections and typed fields -> CI red.
- AR-23: every required section has an empty outcome -> a pass on silence.
- AR-24, FR-8, FR-9: answers verbatim, with executor -> an answer with none.
- AR-25, AR-17, P3, P22: every stage state has a move (2a); the unknown goes to one conductor seam -> a dead end.
- AR-19 (narrowed): one exit check, one handoff form -> a check outside `gate-rules.yaml`.
- AR-26, P23: the requirement is the unit from stage 1 to delivery -> a check with no earlier requirement (G4.1).
- AR-27, AR-28, FR-59, P21: an unknown never passes, is reported by name; three outcomes -> `0` or green for an unmeasured fact.
- AR-29, P27: code judges shape, joins, presence; meaning by critic or person; unlisted reasons routed up -> code judging meaning or wording.
- P13, FR-4: a person's word passes any gate (`passes`), never the launching model's -> an unpassable gate; a pass in a comparison run.
- P20, FR-58: expectation never from code -> an expectation sourced from the implementation.
- P16, P17, P19, P28, P29: pyramid, WHAT in cases, many-to-many links, automate what reruns -> G3.C finding.
- P24: regression found, handed over, never run -> a regression run in a journal.
- P26, P30: code records evidence; the critic's probe breaks the value (G4.C) -> agent-written evidence.
- P31: one launcher, one record writer, one arm launcher -> a second road.
- P7, FR-52: the free agent's model in comparisons -> model mismatch in the journal.
- P8, FR-53: comparison runs leave no trace (clone, hook, no permission) -> an outward write.
- P18: tokens and time in files, money at display (F7); two-source equality phase 8 -> money in a file.
- FR-33: behaviour change accepted by a live comparison run -> merged on unit tests alone. FR-12: no phrase list over wording (F13).

**Variety walk** (`architecture.md` § A forms):
- axis 1: held by key -- commands, `repositories` (C3-6); unknown value -> performer finds and records the command; no code reads the language.
- axis 2: held by key|role -- surface kind; unknown value -> performer judges; reason "no tool for this surface".
- axis 3: held by key|table -- test command, runner forms (C4-4), test roots; unknown value -> raw output kept, summary `unknown`.
- axis 4: held by table|role -- `readiness`; unknown value -> performer judges as assumption; reason "code not written yet".
- axis 5: held by role -- every source route; unknown value -> attempt recorded, else "source unavailable".
- axis 6: held by table|key -- delivery targets (C3-7, only `md` now), key "how results are accepted"; unknown value -> `md` + preview.
- axis 7: held by key|role -- stand keys, raise permission; unknown value -> "no environment" with the attempt.
- axis 8: held by table|role -- host profile (C4-5); unknown value -> unproven point, floor at stage exit.
- axis 8: narrows -- a host without Python 3 has no record writer: launch refused, door "install Python 3"; fork F31.
- axis 9: held by table|key -- stops in stage rows, question forms, key "who answers"; unknown value -> answer verbatim, conductor.
- axis 10: held by key -- person-doc language (F4); package text English.
- axis 11: held by table|role -- stage 4 by requirement group; context over window -> conductor (2a); unknown value -> one group.
- axis 12: held by role -- functional only, declared scope (owner 17.11.2026, `architecture.md` "Decided by the owner").
- axis 13: held by key -- first story without onboarding; no state from the old factory (owner 25.11).
- AR-1: closed variety (routes, reasons, expectation kinds, red causes, forms, targets, gate rules, empty outcomes) is rows, one loader `rows.py` -> a value list in code.
- AR-2: performer judges open variety; debt with a door at exit only; unlisted reasons routed up -> a mid-stage refusal, silent default, dead end.
- AR-3: keys have `default`, `absent_means` -> a key with no row. AR-4: relative paths (`record.py check`) -> an absolute path. AR-5: one `host_adapter.py` -> a harness name in code (C1-2).

## 2. Shared contracts

### 2a Story record (`<work_root>/stories/<id>/record.yaml`, beside `docs/`, `evidence/`, `runs/`; schema `factory/data/record-schema.yaml`)
- Header: `story`, `route`, `schema`, `seq`, `mode` (`live|comparison|night`, set at init by the launcher), `stages` (state below + since), `approved_plan_seq` (`null` before approval and after "intent changed").
- Sections: `sources`, `understanding`, `requirements`, `expectations`, `checks`, `tests`, `links`, `runs`, `results`, `evidence`, `probes`, `reds`, `bugs`, `questions`, `passes`, `reason_verdicts`, `decisions`, `findings`, `critic_findings`, `factory_findings`, `assumptions`, `unknowns`, `knowledge_writes`, `exits`, `shortfalls`, `delivery`.
- Row: `id` (`<PREFIX>-<n>`), `seq` (global, monotonic), `stage`, `by` (agent + role), `from`, `supersedes` (optional), `state` (`live|stale`), `obtained_by`, `group` (`record.py` sets it from the launch); typed fields:
  - requirement: `text`, `source` (stage 1); id kept (AR-26). expectation (stage 3, `from` its requirement; one live each, else `revise`): `requirement`, kind (C3-8 or `none`), `readiness`, `check_group` (optional label by the stage-3 performer: the stage-4 group that checks it; none -> one group; F42; readers `context.py`, `run_stage.py`).
  - check: `requirement`, `level`, `mode` (auto|manual|person|none), `executable_where`, `then`. OBLIGATION = one Then of a check (plan V19), id `<CHK-n>.<k>`; `links` (many-to-many) and `results` key on obligations.
  - probe (critic only): `test`, what broken, `failed|survived|impossible`. question: `form`, `text`, `holds` (ids its answer gates; performer judgment), `answer` verbatim, `executor`. pass: `rule`, `rows`, `words`, `speaker`, `stop`. shortfall: what, `producer`, open|closed. critic finding: `gate`, `about`, `round`, open|fixed|to_report (`findings` = performer observations, F1). reason verdict: `about` (the `other` row), `accepted|returned`, `by`; latest live decides; `returned` -> shortfall on its stage.
- Derived, never stored (AR-10): after approval = `seq > approved_plan_seq` (none while `null`); superseded = a live row names it in `supersedes` -> out of the live set, its `from` dependents stale; `supersedes` never propagates stale.
- Field readers (AR-22): the schema lists `readers` per typed field (W1). expectation `readiness` -> `run_stage.py` (not-implemented: written, not run), `docs_build.py` "Left to you"; `executable_where` -> `run_tests.py`, `docs_build.py` "Left to you".
- Empty outcome: `empty: <kind>` from `factory/data/empty-outcomes.yaml`.
- ONE writer `factory/tools/record.py`: `init`; `add` (a batch per call, all or nothing: a bad row refuses the batch, every bad row named); `revise` (new row, `supersedes`; meaning changed); `stale` (over `from`); `empty`; `check`. Content is the performer's; groups F11. It takes `passes` only from `ask.py` (its `stop` names a question whose tool-written answer holds the `words`), `probes` only from a `critic.py` launch, `reason_verdicts` only from `critic.py`, `ask.py` or the conductor; a performer's `add` there: refused, door a question row. In `mode: comparison|night` it refuses `passes` and outward permission rows, door "stop named in the report; the gate stays".
- Readers: `context.py`, `exit_check.py`, `world.py`, `docs_build.py`, `run_stage.py`, `critic.py`, `ask.py`, `export_md.py`, `dashboard.py`.
- Plan 1b needed: N1 W1; N2 X1; N3 `context.py`; N4 G4.1, G4.3, after-approval; N5 `shortfall`. Found: F1 `findings`/`assumptions` + `about`; F2 tool-written runs, evidence, probes, answers; F3 X3; F4 X2; F5 critic gates + late rows (2c).
- Absent: stage 1 not started; other readers refuse, door `record.py init`. Unreadable: error with door `record.py check`; never empty (AR-28).

**Stage states** (`run_stage.py` takes every move):

| State | When | Move |
|---|---|---|
| `waiting` | `reads` not ready | launch when ready |
| `open` | launched | performer works, may call `exit_check.py`, asks exit |
| `refused` | exit or `after_critic` with open debts | relaunch fresh with the debt list and its sections, back to that step (`after_critic`: re-check of changed rows, F60); same debts refused `refusal_relaunch_max` (data, 2) times -> conductor |
| `in_critic` | `exit` rules met, preview built, stage has a critic | `critic.py`, fresh, same page; findings -> `fix_round`; none -> `after_critic` rules: G4.5 unmet -> `critic.py` for unprobed tests; other unmet -> `refused`; met -> stop or `exited` |
| `fix_round` | open critic findings, round n (F8) | relaunch fresh with findings and the sections they name; critic re-checks those; rounds spent -> `to_report`, go on; no critic: relaunch with the person's words, rebuild -> `at_stop` |
| `at_stop` | rules met, document built, stage has a stop | `ask.py`; by answer (V4): approved -> `exited` (stage 3 sets `approved_plan_seq`); fixes -> `fix_round` with the words; partial -> returned rows staled, `open`; intent changed -> `approved_plan_seq` `null`, old-intent rows staled, stage 1 or 3 reopened, next approval sets it; stop -> `stopped` |
| `held` | all remaining rows held by open questions | others go on; the answer releases them -> `open` |
| `stopped` | the person said stop | nothing runs; record kept; the person's relaunch resumes from it (V3) |
| `exited` | exit met | later stage stales its rows -> `stale`; shortfall names it -> `shortfall` |
| `stale` | rows of an exited stage staled (rule 7) | relaunch with stale rows only; met rows stay met |
| `shortfall` | open shortfall names an exited producer | relaunch the producer with those rows only; consumer holds only dependent rows |
| `no_move` | context over the host window, a state the data lacks, launch error | conductor seam |

Conductor seam, one entry in `run_stage.py`. In: state, evidence (row ids, refusal text, journal events), options from `conductor.md` (split a group, sections by pointer, ask). Out: `decisions` rows (decision, reason, option, target state; F43) or a question via `ask.py`; runs no commands, never cuts a context.

### 2b Stage row (`factory/data/stages.yaml`), route row (`routes.yaml`), loader
- Stage: `id`, `name`, `reads`, `leaves` (`required|optional`), `craft`, `exit` (rule ids; due from the first, 2c), `critic` (`none`|page), `stop` (`none`|doc id|form), `grouped`, `parallel_max`. Route: `id`, `stages`; only `story` now. Stage 1 leaves `sources`, `understanding`, `requirements`, `questions`; stage 3 leaves `expectations`.
- Writer C3-2 (a change is a behaviour change, comparison run). Readers: `rows.py`, `run_stage.py`, `context.py`, `exit_check.py`, W1.
- `rows.py` loads every `factory/data/*.yaml`: absent or unreadable -> launch refused naming the file and its card; never an empty list (AR-28).
- No `reads`: stage 1 only. Unknown route: refused, routes named. Missing page: W1 names it, not launchable. Context over the window: `no_move`, never cut.

### 2c Gate rule row (`factory/data/gate-rules.yaml`), reasons (`reasons.yaml`)
- Fields: `id`, `over` (sections), `when` (`exit|after_critic|critic|stop|ask|ci`: every section-3 id is a row, `exit_check.py` runs the first two; F41), `checks` (a predicate of `exit_check.py`), `owner` (`data|judgment|intent`), `class`, `debt` (what is open, what closes it), `door` (tool, field or reason; always also a `passes` row), `protects` + `origin` (plan 4.3), `on_unknown` (`ask`|`default: <v>`, printed).
- SCOPE BY SECTION: a rule falls DUE at the stage whose `exit` (2b) first names it, then runs at every exit over every live row of `over`, whoever wrote it. Debtor = the stage leaving the missing part: a row's own fields -> its `stage`; "each X has a Y" -> the stage leaving Y, never X's author; else the exiting stage. Debtor exiting -> `refused`; exited -> shortfall. Stage-4 rules see the exiting group's rows; other groups' at their own exit and the stage's last exit. Invariant (fix 5 vs rule 7): verdicts are per row and a met row stays met, so only new, revised or stale rows yield debts.
- Late rows (`seq` above what the section's critic saw) go to the next critic gate by name; after G6.C to its re-check, else the report "not critiqued".
- ORDER at G3, G4, G6: `exit` rules -> `docs_build.py` preview (none without a document) -> critic, reading it -> fix rounds (each rebuilds it; critic re-checks) -> `after_critic` rules incl. D1, G6.1 on the built document -> person stop; a failure there: fix round + re-check, never a silent rewrite. Critic-less stop (stages 1, 2, 5): `exit` rules -> build -> `after_critic` (D1) -> stop. Invariant: the person never sees a document the critic has not seen.
- Reasons: "stand unavailable" (attempt), "no reliable expectation source", "source unavailable", "person decided not to check" (words), "code not written yet", "no tool for this surface", "executed by agent, no evidence" (why), `other` (own words + attempt). A named row closes the debt; `other` is never refused: a provisional pass routed up (next critic gate, else the person at the next stop, else the conductor), accepted or returned in `reason_verdicts` (-> shortfall). Every reason is in the report by name.
- A `passes` row (writer `ask.py`, 2a) closes any debt (P13); over an `owner: data` rule it also writes `factory_findings` (FR-4); `score.py` counts passes.
- Refusal: all debts at once, each with its door; never "wrong form". Rule 10 label by the acceptor (measuring runs: F30); unlabelled = `unknown`.
- Writer C3-3. Readers: `exit_check.py` (any time; launcher at exit and after critic), page "how checked" (F12), `critic.py`, `dashboard.py`.

### 2d Person documents (`factory/data/person-docs.yaml`), question forms (`questions.yaml`)
- Documents, closed: `understanding`, `test_plan`, `manual_pass_report`, `test_report`, `retro` (F3). Fields: `id`, `when`, `from`, `template` (`factory/templates/<id>.md`), `budgets` (40 lines; 15 plan rows then "and N more"; 6144 bytes; brief 2 KB, 5 items), `language` (F4), `required`. `understanding` places every requirement in checking / not checking (D2).
- Question forms, not documents: `critical`, `approve`, `bug_or_not`, `conductor`. `bug_or_not` body: `docs_build.py` from bug-draft rows, template `q-bug-or-not.md`, 40 lines, 5 bugs then "and N more"; manual fails attach `manual_pass_report` (F2).
- Built only by `docs_build.py`; counts never authored; every text to the person via `ask.py`, citing only document and form ids (D3). Writers C3-5, C4-3 (forms). Empty section: own words, never omitted; absent record section: "not recorded: <section>".

### 2e Hook points (pointer: `docs/tasks/specs/20261124-host-profile-hooks-plan.md` §3, §8-§10)
- As designed there: points as data; one neutral event and verdict; profile translates; live probe accepts; unproven -> floor at stage exit.
- `factory/data/hook-points.yaml`: `outward_write` (closed, floor X5), `secrets` (closed, floor X5, `secret-patterns.yaml`), `stage_context`, `observe` (open, floor X3; carries `agent`, `group`), `person_address` (open, floor D3). Writer C4-5; readers `factory/hooks/*`, `host_adapter.py`, `exit_check.py`.
- OUTWARD = a write outside the roots of key `repositories` (product and test repositories; `work_root` inside) plus any publication (tracker, case manager, MR, push). An unknown root is asked once at first need and stored; that write waits, other work goes on. In `mode: comparison|night` roots are only the launch-time ones: an unknown root -> write refused, named in the report, other work goes on; `knowledge.py` adds no root there, whoever answers. Permission: a person's row, never in `mode: comparison|night`.

### 2f Run measurements (`<work_root>/stories/<id>/runs/journal.jsonl`; rows `factory/data/dashboard.yaml`)
- Event: `story`, `stage`, `group`, `agent`, `role`, `model`, `mode`, `start`, `end`, `turns`, `tokens` (in, out, cache read/write), `factory_tool_calls` (`record.py` apart), `refusals` (rule + label), `critic_findings`, `fix_round`, `stop_wait`, `docs_given` (id, bytes; `ask.py`).
- From the record (`dashboard.py`): shortfalls per stage, unpaired rows, passes, provisional reasons (no `accepted` verdict).
- Acceptor labels (judgment, FR-12; `label` events): `needed_not_done|gate_defect`; `refound` (found anew by the next stage); `working_file_opened` (factory defect, 1v issue rule 4). Labeller in measuring runs: F30.
- ONE writer `factory/tools/journal.py`. Reader `dashboard.py`: per agent and story (marathoners over `marathon_minutes`), rework after critic, time per story and stage; money F7.
- No carrier -> `unmeasured: <why>`, never 0. Absent journal: "no journal for story X".

### 2g Knowledge (`<work_root>/knowledge.yaml`; keys `factory/data/knowledge-keys.yaml`)
- Key: `key`, `default`, `absent_means`, `asked_when`. Value: `key`, `value`, `by`, `source` (words verbatim or `found:<how>`). ONE writer `knowledge.py`. Onboarding: phase 5.
- Keys (C3-6): `work_root`, commands, `linter`, `repositories` (root, product|tests), surface kind, stand, raise permission, who answers, how results are accepted (target id, C3-7), doc language, `marathon_minutes`.

## 3. Where judgment lives

Owner: data = code; judgment = a role, accepted a tier above; intent = the person. `X` rules run at every exit; "over" = 2c scope. Predicates read ids, links, `seq`, presence, counts, never wording (FR-12) or expectations (FR-58); unknown -> ask or printed default (FR-59). Every door includes the person's word.

| id | check | over | owner | class | on unknown |
|---|---|---|---|---|---|
| X1 | each required leave has a row or `empty:` | leaves | data | presence | debt |
| X2 | three exit answers; "nothing" is a row | exits | data; content judgment | presence | debt |
| X3 | each project file the group's agent made/changed (VCS-ignored out) and each run referenced | runs, evidence, tests | data | xref | no VCS: `unknowns` row; no `observe`: once at stage exit |
| X4 | no stale row among the stage's rows | all | data | xref | debt |
| X5 | nothing outward (2e) without a person's permission row | delivery | data | safety | refuse |
| X6 | reason closure: reasons row + attempt; `other` provisional until accepted (`reason_verdicts`) | rows with `reason`, `reason_verdicts` | data + judgment/intent | presence | debt |
| G1.1 | each listed source read, or unavailable with attempt | sources | data | presence | debt |
| G1.2 | understanding recorded | understanding | data | presence | debt |
| G1.3 | questions recorded; critical ones asked | questions | data | presence | debt |
| G1.4 | each requirement: text and source | requirements | data | shape | debt |
| G1.P | sources + understanding with requirements confirmed | - | intent | - | waits; launching model answers |
| G2.1 | product run + smoke, or "no environment" with attempt | runs, evidence | data | presence | debt |
| G2.2 | environment facts in knowledge, or "nothing new" | knowledge_writes, exits | data | presence | debt |
| G2.P | only a critical question | - | intent | - | waits |
| G3.1 | each requirement: an `expectations` row, kind or `none` | requirements, expectations | data | xref | debt |
| G3.2 | each requirement: a check or reason | requirements, checks | data | xref | debt |
| G3.3 | each check: requirement, level, mode, an obligation | checks | data | shape | debt |
| G3.4 | each source: requirements or "none" | sources, requirements | data | xref | debt |
| G3.C | requirements vs sources; checks meaningful; pyramid; not one-to-one (advice: link ratio) | requirements, checks | judgment (critic) | - | finding |
| G3.P | test plan approved, separate answer | - | intent | - | waits |
| G4.1 | each check/test has a requirement of lower `seq` | checks, tests | data | xref | debt (defect) |
| G4.2 | each planned check: autotest run, manual pass with tool evidence, or reason | checks, runs, evidence | data | presence | debt |
| G4.3 | links whole both ways | links, tests, evidence | data | xref | debt |
| G4.4 | linter passes on the stage's test files, if key `linter` | tests | data | presence | `n/a` row |
| G4.C | test checks its claim (probe, P30, rows via `record.py`); evidence shows it | tests, evidence | judgment (critic) | - | not proven |
| G4.5 | after critic: each autotest has a probe (unprobed: `critic.py` for those only, F8); `survived` = finding; `impossible` or rounds spent = "not proven" to the report | probes | data | presence | not proven |
| G5.1 | each red: cause from `red-causes.yaml`, evidence, actor | reds | data | presence | debt |
| G5.2 | red with cause `test` has a later run | reds, runs | data | xref | debt |
| G5.3 | bug draft: steps, expectation + source, fact, evidence, repro | bugs | data | shape | debt |
| G5.P | bug or not (form `bug_or_not`) | - | intent | - | waits |
| G6.1 | report built by `docs_build.py` after the last fix round; `after_critic` | delivery | data | presence | debt |
| G6.2 | each requirement: result per obligation, or reason | requirements, results | data | xref | debt |
| G6.3 | no open gate debt (critic findings: report, not debt) | all | data | presence | debt |
| G6.C | ask checked; conclusions match evidence; author wording (F13; advice: factory ids) | record, report preview | judgment (critic) | - | finding |
| G6.P | before MR and any outward write | - | intent | - | waits |
| D1 | document and form budgets; `after_critic` (2c ORDER) | docs | data | shape | debt |
| D2 | each requirement in checking or not checking; G1 only (later: G3.2, test plan) | understanding, requirements | data | xref | debt |
| D3 | stop message cites only document/form ids (`ask.py` field); a working-file request returns to the performer (1v issue rule 3) | questions | data | xref | refuse |
| W1 | each read and typed-field reader has a producer, each leave a reader (CI) | stage rows, schema | data | xref | CI red |

The critic sits only in G3, G4, G6 (stage row column). A red cause, reason, critical mark or `holds` is the performer's judgment: code checks presence and row-set membership (AR-29); critic, person or conductor accepts it.

## 4. Cards

All cards of phases 0-4. Owns under `C:/QAFactory/forge2-repo/` (absolute in bodies); `f/` = `factory/`. P2, P2b, P3, P3b = `docs/tasks/specs/20261125-forge2-light-factory-spec-part2.md`, `...-part2b.md`, `...-part3.md`, `...-part3b.md`. Part 2 forks F16, F19, F21, F22: option (a), rows widened.

| Card | Name | Ph | Owns | Body |
|---|---|---|---|---|
| C0-1 | Place: plan + spec copies, README | 0 | `README.md`, `forge/specs/` | P2 |
| C0-2 | MyBooks measuring project | 0 | `measure/mybooks/` | P2 |
| C0-3 | ao3-wrapper measuring project; truth table frozen before any page or seeded set (F5) | 0 | `measure/ao3-wrapper/` | P2 |
| C0-4 | The one arm launcher; scorer (counts passes) | 0 | `measure/tools/arm.py`, `measure/tools/score.py`, `forge/tests/test_score.py` | P2 |
| C0-5 | Free-agent baseline (F6), MEASURING RUN | 0 | `measure/runs/baseline/` | P2 |
| C1-1 | Forge rules, budgeted (F9); role files (F16) | 1 | `CLAUDE.md`, `forge/COORDINATOR.md`, `.claude/agents/` | P2 |
| C1-2 | Size ratchet, universality counter, English check | 1 | `forge/budgets.json`, `forge/universality-names.json`, `forge/tools/{size_ratchet,universality}.py`, tests | P2 |
| C1-3 | CRAP, lint, clone ratchets at zero | 1 | `forge/tools/{crap,lint,clone}_ratchet.py`, `forge/baselines/`, tests | P2 |
| C1-4 | Token tools | 1 | `forge/tools/{journal,dispatch,trim,snapshot}.py`, `logs/journal/`, tests | P2 |
| C1-5 | Forge hooks; the ONE secret table | 1 | `forge/hooks/`, `f/data/secret-patterns.yaml`, tests | P2 |
| C1-6 | CI, test rule (F14); one job list for `ci.yml` and the local step | 1 | `forge/TESTING.md`, `.github/workflows/ci.yml`, `forge/ci-jobs.json`, `forge/tools/ci.py` | P2 |
| C1-7 | Calibration carry list, symmetry map | 1 | `forge/calibration.md`, `forge/siblings.md` | P2 |
| C2-1 | Craft page form, index, check | 2 | `f/data/craft-pages.yaml`, `f/tools/pages_check.py`, test | P2b |
| C2-2 | Pages: requirements, questions, report | 2 | `f/craft/` those files | P2b |
| C2-3 | Pages: checks, techniques, levels, automate, regression | 2 | same | P2b |
| C2-4 | Pages: test code, manual pass, exploration, stand (F22) | 2 | same | P2b |
| C2-5 | Pages: red analysis, bug | 2 | same | P2b |
| C2-6 | Seeded sets, runner; `seeded.py` calls `arm.py`; ao3 truth bugs never seeds (F5) | 2 | `measure/seeded/`, `measure/tools/seeded.py`, test | P2b |
| C2-7 | Pages vs no pages, MEASURING RUN | 2 | `measure/runs/craft-pages/` | P2b |
| C2-8 | Stage-chain cost spike: six fresh stages by hand on a stub record vs "within 2x" | 2 | `measure/runs/stage-chain-spike.md` | P2b |
| C3-1 | Story record (2a) | 3 | `f/data/{record-schema,empty-outcomes}.yaml`, `f/tools/record.py`, `f/tests/test_record.py` | P3 |
| C3-2 | Stages, routes, loader, W1, context (2b) | 3 | `f/data/{stages,routes}.yaml`, `f/tools/{rows,context}.py`, `f/tests/test_rows.py` | P3 |
| C3-3 | Gate rules, reasons, red causes, exit check | 3 | `f/data/{gate-rules,reasons,red-causes}.yaml`, `f/tools/exit_check.py`, `f/tests/test_exit_check.py` | P3 |
| C3-4 | World diff per group (X3) | 3 | `f/tools/world.py`, `f/tests/test_world.py` | P3 |
| C3-5 | Person documents; templates incl. `q-bug-or-not.md`, C4-8's | 3 | `f/data/person-docs.yaml`, `f/templates/`, `f/tools/docs_build.py`, `f/tests/test_docs_build.py` | P3 |
| C3-6 | Project knowledge (2g) | 3 | `f/data/knowledge-keys.yaml`, `f/tools/knowledge.py`, `f/tests/test_knowledge.py` | P3 |
| C3-7 | Delivery targets (only `md`; tested in C3-2's file) | 3 | `f/data/delivery-targets.yaml` | P3 |
| C3-8 | Expectation-source kinds (tested by G3.1 rows) | 3 | `f/data/expectation-sources.yaml` | P3 |
| C4-1 | Launcher, states, conductor seam | 4 | `f/tools/run_stage.py`, `f/craft/conductor.md`, `f/tests/test_run_stage.py` | P3b |
| C4-2 | Critic, probes, fix rounds | 4 | `f/tools/critic.py`, `f/tests/test_critic.py` | P3b |
| C4-3 | Stops, question forms, `ask.py` | 4 | `f/data/questions.yaml`, `f/tools/ask.py`, `f/tests/test_ask.py` | P3b |
| C4-4 | Test runner, evidence recorder | 4 | `f/tools/{run_tests,evidence}.py`, `f/data/runner-forms.yaml`, `f/tests/test_run_tests.py` | P3b |
| C4-5 | Hooks, first host profile; `secrets` reads C1-5's table | 4 | `f/data/hook-points.yaml`, `f/data/hosts/`, `f/tools/host_adapter.py`, `f/hooks/`, `f/tests/test_hooks.py` | P3b |
| C4-6 | Run journal, dashboard (2f) | 4 | `f/tools/{journal,dashboard}.py`, `f/data/dashboard.yaml`, `f/tests/test_dashboard.py` | P3b |
| C4-7 | Main measurement, closes phase 4 | 4 | `measure/runs/phase4/` | P3b |
| C4-8 | `.md` export of cases and bugs | 4 | `f/tools/export_md.py`, `f/tests/test_export_md.py` | P3b |

Order: phase 0; phases 1, 2 in parallel; C2-8 before phase 3; 3 after 1; 4 after 2 and 3. Bodies: tests per `forge/TESTING.md`; external input gets the battery (magnitude, nesting, encoding, empty/broken, AT and BEYOND each limit).

## 5. Traceability

| Plan statement | Cards |
|---|---|
| 1.1 stages, fresh context, one record, code launches | C3-2, C4-1 |
| 1.1 requirements from stage 1, completed at stage 3 | C3-1, C3-2, C3-3 (G1.4, G3) |
| 1.2 craft pages, one home, "how checked" | C2-1..C2-5 |
| 1.3 typed record, one writer | C3-1 |
| 1.4 gates at stage exit | C3-3, C3-4 |
| 1.5 critic in three gates, order, probe | C3-2, C3-3 (G4.5), C4-2 |
| 1.6 project knowledge | C3-6; onboarding: phase 5 |
| 1.7 person on intent, named stops, verbatim | C4-3 |
| 1.7 launching model answers stops only | C3-1 (`mode`), C4-3 |
| 1.7 person's word passes a gate: recorded, counted | C3-1, C3-3, C4-3, C0-4 |
| 1.8 tools, few hooks, harness-neutral | C4-4, C4-5, C1-2 |
| 1.8 export of cases | C4-8 |
| 1.9 routes as rows, one road, conductor | C3-2, C4-1; other routes: phase 6 |
| 1a rules 1, 2, 5: exit only, outcome not path, all debts any time | C3-3, C4-1 |
| 1a rules 3, 4: code sees what it can, no "wrong form" | C3-1, C3-3, C3-4, C4-4 |
| 1a rule 6 named reasons, open row routed up | C3-3 (X6), C4-1 |
| 1a rule 7 going back is legal | C3-1 (`stale`, `revise`), C3-3 (scope), C4-1 |
| 1a rules 8, 9: hold only dependents; unknown to conductor | C3-1 (`holds`), C4-1 |
| 1a rule 10 gate measured | C4-6, C2-6; F30 |
| gate rows 1-6 | C3-3 (G1-G6, D2); C3-5 (1, 5, 6); C4-3 (1, 3, 5); C3-6 (2); C4-2 (3, 4, 6); C4-4 (4); C4-5 (6) |
| 1b needed 1-5 | C3-2 (1, 3), C3-3 (2), C3-1 + C3-3 (4), C4-1 (5) |
| 1b found 1-5 | C3-1 (1), C4-4 (2), C3-4 + C3-3 (3, 4), C4-2 (5) |
| 1b measured by: truth-table facts reach the report | C0-2, C0-3, C0-4, C4-7 |
| 1b measured by: shortfalls, unpaired rows, re-found findings | C4-6 (2f), F30 |
| 1v understanding, test plan | C3-5, C4-3 |
| 1v manual-pass report | C3-5, C4-4; F2 |
| 1v test report | C3-5 |
| 1v retro | F3; if kept, C3-5 |
| 1v common rules 1-5 | C3-5, C3-6, F13, F4 |
| 1v issue rules 1-3 | C3-5, C4-3 (D3), C4-5 (`person_address`) |
| 1v issue rule 4: documents, sizes, working file opened | C4-6, C4-3 |
| "bug or not" a question, not a document | C3-5, C4-3 |
| owner: universal across projects | C1-2, section 1 walk; unknown projects: phase 9 |
| owner: tests by pyramid levels | C2-3, C3-3 (G3.C) |
| owner: case and autotest not one-to-one | C3-1 (`links`), C3-3 (G3.C) |
| owner: code quality not worsened | C1-3, C1-6 |
| owner: not less than a free agent | C0-4, C0-5, C2-8, C4-7 |
| owner: code launches tests, no hard restriction | C4-4, C3-3 (rule 2) |
| owner: token tools, dashboard at once | C1-4, C4-6 |
| owner: everything to `.md` by default | C3-7, C4-8, C3-5; adapters: phase 7 |
| owner: two runs before release | C4-7, F6 |
| owner: dry story later, data from live runs | C4-7; phase 10 |

## 6. Worlds before and after

| Artifact | Created by | Reader behaviour while absent |
|---|---|---|
| forge 2 skeleton | C1-1..C1-6 | phase 0 follows the old forge's `CLAUDE.md`, `docs/TESTING.md`; no factory code before C1-3, C1-6 |
| truth tables, baseline | C0-2..C0-5 | no behaviour change accepted; unit tests only |
| ao3 truth table | C0-3 | no craft page or seeded set written (F5) |
| stage-chain spike | C2-8 | phase 3 not dispatched |
| craft pages | C2-2..C2-5 | W1 names the page; stage not launchable; phase 3 uses fixture pages |
| `record.yaml` | `record.py init` | readers refuse, door `record.py init` |
| any `factory/data/*.yaml` | its card | `rows.py` refuses the launch by name |
| `secret-patterns.yaml` | C1-5 | both secret hooks fail closed |
| `knowledge.yaml` | first `knowledge.py` write | defaults with `absent_means`; performer finds facts; asks at first need |
| `repositories` key | first answer or find | each root outside `work_root` asked once (2e) |
| host profile, hook points | C4-5 | fixture launch line; every check as its floor at stage exit |
| hook point a harness lacks | - | floor at stage exit, named once |
| run journal | first launch | "no journal" |
| doc language key | C3-6 | English, printed as default (F4) |
| seams, phases 6-10 | - | 6: unknown route refused, `story` named; 7: only `md`, X5 refuses outward, report previews; 8: same launcher, `mode: night`; 9: no profile -> floors; 10: C4-7 keeps record, journal, host answers |

## 7. Forks

Status: F1-F4 open for the owner; F5, F6, F7, F13 taken by the Lead by the recommendation until the owner's word (plan "Reshila sama"); F8-F12, F14, F30 by recommendation; F31 (a) until the owner's word (a narrowing: hers to decide). Forks of the parts (F15-F23, F41-F43, F50-F52) and F60: option (a) by the Lead; texts in parts 2 and 3.

**F1** (owner question 1): sources overview and understanding: (a) one document, one stop; (b) two, one more wait. Rec (a). C3-5, C4-3.

**F2** (question 2): manual-pass report with "bug or not" when cases failed, else with the test report: (a) so; (b) own stop. Rec (a). C3-5, C4-3.

**F3** (question 3): retro: (a) none in phase 4, numbers on the dashboard; (b) optional. Rec (a) until phase 8. C3-5.

**F4** (question 4): document language: (a) knowledge key, default English; (b) always English. Rec (a) (axis 10). C3-5, C3-6.

**F5** (plan phase 0 vs `experiments/ao3-wrapper/factory-vs-free-agent/RUN-INSTRUCTIONS.md:37`, no ao3 truth): (a) phase 0 builds the ao3 truth table from the 24.11 hand-verified claims, owner confirms disputed rows; it is FROZEN before any craft page or seeded set is written and its bugs are never seeds; (b) hand verification after each run; (c) ao3 measures traceability only. Rec (a). C0-3, C0-5, C2-6, C4-7.

**F6** (runs per measurement; answer "two"): (a) two factory + one free per project, baseline two free; (b) three + one. Rec (a). C0-5, C4-7.

**F7** (P18 vs "price per agent and story"): (a) files hold tokens by model and time, money at display from a rate row; (b) money column -- breaks P18. Rec (a). C4-6.

**F8** (finite fix rounds): (a) one critic call per gate (per group at G4), two rounds; a round = fresh performer with the findings and their sections, then the critic re-checks those only; rest to the report; (b) three. Rec (a). C4-2.

**F9** (budgets): `CLAUDE.md` 12 KB, `forge/COORDINATOR.md` 20 KB (now 85 KB in 5 files), factory code 6,000 lines, gate rules 45 (section 3: 39), start load at first run; or tighter; or none. Rec these. C1-1, C1-2.

**F10** (runtime): (a) Python 3 + pure-Python PyYAML; (b) JSON, stdlib; (c) other. Rec (a); host precondition F31. C1-3, C3-1.

**F11** (one file vs parallel groups): (a) one file, `record.py` lock + retry; (b) fragments merged. Rec (a); X3 per group. C3-1.

**F12** ("how checked" in page vs gate rows): (a) generated from the rules over every section the stage writes, plus critic criteria; (b) authored, rows cite it. Rec (a). C2-1, C3-3.

**F13** (1v common rule 1 vs FR-12): (a) templates carry no internal names (template test); wording by G6.C with code advice; D3 refuses by id only; (b) refusal on name tokens -- a phrase list. Rec (a). C3-5, C4-2, C4-3.

**F14** ("for now local" vs CI): (a) Actions once pushed; until then `ci.py` runs `forge/ci-jobs.json` pre-push; (b) local only. Rec (a); push by the owner's word. C1-6.

**F30** (fix 16; plan 1a rule 10 silent on who labels refusals, `refound`, `working_file_opened` in a measuring run): (a) the Lead, from record and journal, before scoring -- Lead time per run; (b) a fresh critic, the Lead samples -- one more agent call; (c) left `unknown` -- rule 10 unmeasured. Rec (a). C4-6, C0-4, C4-7.

**F31** (fix 20; `axis 8: narrows`): a host without Python 3. (a) declared precondition, launch refused with door "install Python 3" -- such hosts lose the factory until then; (b) a second writer in another runtime -- two writers (AR-14, P31), double cost; (c) a packaged binary -- does not load here, untestable. Rec (a); a narrowing: the owner decides. C3-1, C4-5.

**F60** (r2 fix 4; F8 vs the re-check after an `after_critic` refusal): (a) in the F8 count, spent -> conductor; (b) outside F8, up to `refusal_relaunch_max`. Rec (a); taken. C4-1, C4-2.

## 8. Small choices closed
- Only `factory/` ships; first harness Claude Code (Codex phase 9). Ids `<PREFIX>-<n>`, obligations `<CHK-n>.<k>`; global `seq`.
- `work_root` default `.light-factory`, out of X3; G4.4 on the stage's files only.
- Data rows: `marathon_minutes` 20, `refusal_relaunch_max` 2.
- Secret table owned by C1-5 (first reader in phase 1); `ci.yml` runs `ci.py <job>` per `ci-jobs.json` entry.
- `q-bug-or-not.md`, export templates in `factory/templates/` (C3-5).
- Forge documents may be Russian; `factory/` English-only (C1-2). 37 cards vs about 45 plan nodes.

## 9. Trail
- r1 read: verdict whole; r0 whole; plan v1.2 523-900, 1076-1092, 1224-1283, 1337-1563; `architecture.md` 66-72, AR-6/8/9/11/15/16/18/20/22 (Grep -A3), 176, 191; P5, P15, P18 (Grep); part 2 headings, F15-F23, 182-197.
- `facts:` used: r0 39683 bytes (8cc6b5192); 22 fixes; plan 479074d60; part 2 forks from F15 -> mine from F30.
- Size: measured by the Lead at each acceptance (journal `accepted` lines of t-1916, t-1920).
- Not read: plan 131-473, 902-940.
- r2 read: t-1919, r1 whole. Closed small: one live `expectations` row per requirement; latest verdict decides.
