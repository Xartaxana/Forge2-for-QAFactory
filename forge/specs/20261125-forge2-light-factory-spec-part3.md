Frame spec part 3: card bodies of phases 3-4, forge 2 and the light QA factory (t-1917, F19; draft r0, 25.11.2026). Frame = `docs/tasks/specs/20261125-forge2-light-factory-spec.md` r1 at 12a00c2c8; plan = `...-plan.md` v1.3; part 2 = `...-spec-part2.md`. `owns:` paths absolute; other paths relative to `C:/QAFactory/forge2-repo/`; `f/` = `factory/`. Contracts cited by frame section and rule id, never restated. Bodies are written against the FIXED contracts of re-review t-1919 N1-N9 as decided by the Lead for frame r2 (t-1920); section 4 lists which body rests on which N.

STATUS: returned at 55347 bytes, over the cap, with the designer's `decomposable:` line; the Lead's script moved the phase 4 bodies to part 3b byte for byte, nothing trimmed. Sections 1, 3, 4, 5 here hold for both files. Forks F41, F42, F43: taken as option (a) by the Lead until the owner's word. The frame r2 (8e7e07c5f) now holds the N1-N9 contracts these bodies were written against; the group label of F42 is its field `check_group`, the conductor's section of F43 is `decisions`.

## 1. Scope and pointers

**Adds:** bodies of the 16 cards the frame index (section 4) marks `P3`; forks F41-F43 (F40, F44 dropped: answered by N4, N7); frame gaps. **Rests on:** frame 1 (invariants, variety walk; bodies add no axis, F42 touches axis 11, held by table|role), 2a-2g, 3, 6, 7. The verdict t-1915's 22 fixes stay closed: no body re-opens them.

**Order** (frame 4: phase 3 after phase 1 and C2-8; phase 4 after 2 and 3; all owns disjoint, so cards run in parallel against the frame contracts with fixture data from the cards they wait for):
- Phase 3: C3-1 first (every reader loads the record). Then C3-2, C3-6, C3-7, C3-8 in parallel; C3-3 after C3-2 and C3-8 (stage rows name rule ids; G3.1 reads kinds); C3-4 and C3-5 after C3-1, in parallel with C3-3.
- Phase 4: C4-5, C4-6, C4-3, C4-4, C4-8 in parallel; C4-1 after C4-5 (launch line), C4-6 (journal), C4-3 (`ask.py`); C4-2 after C4-1's seam is fixed (same launch road); C4-7 last.

**Common to every card:** tests per `forge/TESTING.md` (C1-6): one table per test file, `expected from:` the frame, plan or this part, never code output; tests never launch a harness, a stand or the network (fixture launch line, frame 6); input from outside (a record or knowledge file a person or agent wrote, host event JSON, test runner output, answer words) gets the battery: magnitude, nesting, encoding (non-UTF-8, BOM), empty/broken, AT and BEYOND each limit. Every refusal follows frame 2c "Refusal" (all at once, each with its door, a `passes` door always); every absent or unreadable data file follows frame 2b (`rows.py`). No money figure or rate value anywhere (F7). Readers of each file: section 5.

## 2. Cards

### C3-1 Story record (2a)
- amended by: A2, A3, A4, A5, A7, A9, A15, A16, A17, A22, A24, A25, A26, A27, A28, A34, A35 (cards whose `amends:` line names this card; read them with it)
- Delivers: `record-schema.yaml`: `schema: record/1`; `header` (field -> type/enum, frame 2a); `sections` (name -> `prefix`, `fields` (name -> `type`, `enum` or `enum_from: <data file>`, `readers: [tool]`, `from_stage`)); `levels: [unit, api, integration, e2e_ui, manual, exploratory]` (the one level list, plan 1v test plan, slices:D1); optional fields of untyped sections that docs need: understanding `goal`, `depth`, `checking` (REQ ids), `not_checking` (REQ id + why), `affected`; check `breaks`, `impact`, `technique`; finding/assumption `about` (row id, stage, `knowledge:<key>`, or `plan:<section>` of C3-5). Sections of r2: `expectations` (N2: `requirement` id, kind or `none`, `readiness`, `group` per F42; requirement ids stable from stage 1 to delivery, `revise` only for a change of meaning); `reason_verdicts` (N7: `about` reason row, `accepted|returned`, `by`). Every row carries `group`, written by `record.py` from the launch env `FACTORY_GROUP` (N1), never by the agent. Writer-bound sections (N6): `passes` only through `ask.py`'s call naming a question whose answer row is tool-written; `probes` and critic `reason_verdicts` only under a `critic.py` launch (`by` from the launch env set by the launcher); a performer `add` of them -> refused, door "ask the person (ask.py)" / "the critic writes probes". `empty-outcomes.yaml`: `kind`, `section`, `words` (one row per required section, AR-23). `record.py` CLI, each command prints `ok <ids>` or a refusal:
  - `init --story <id> --route <id> --mode live|comparison|night`: writes header, `seq: 0`, `approved_plan_seq: null`; record exists -> refused, door "use the existing record or a new story id".
  - `add --stage <s> --by <agent:role> --batch <file|->`: rows as YAML list; ids and `seq` assigned under the lock; all or nothing (frame 2a).
  - `revise <id> --batch` (new row, `supersedes: <id>`); `stale <ids> --why` (over `from`, never over `supersedes`, frame 2a "Derived"); `empty --section --kind --stage`; `check`.
  - Library `load(path)`: the one reader every tool imports (AR-13).
- Refusal text: `refused: <n> rows; row <k> (<section>): <field> <what is wrong>; expected: <schema line>; door: <fix> | passes` (a `passes` door only where a gate rule stands behind it). In `mode: comparison|night` a `passes` or outward-permission row: `refused: <section> rows are not written in mode <mode>; door: stop named in the report; the gate stays` (frame 2a).
- Lock (F11 (a)): `record.yaml.lock` created exclusively, holding pid + time; retry every 0.2 s up to `record_lock_wait_s` (data, 10); then refused "record busy: held by <pid> since <time>; door: retry". A lock older than 60 s with a dead pid is broken and the break journaled. Write = temp file + atomic replace.
- `check` verifies: parses; header complete; every section/field known; ids unique, prefix matches section; `seq` unique, monotonic in file order; `from`/`supersedes` targets exist, no `supersedes` cycle; paths relative (AR-4) and under the story folder or a `repositories` root; exit 0 / 1 (named defects) / 2 (unreadable).
- owns: C:/QAFactory/forge2-repo/factory/data/record-schema.yaml, C:/QAFactory/forge2-repo/factory/data/empty-outcomes.yaml, C:/QAFactory/forge2-repo/factory/tools/record.py, C:/QAFactory/forge2-repo/factory/tests/test_record.py
- deps: C1-3, C1-6 (code, frame 6); F10, F11, F42; N1, N2, N6, N7.
- keys: K1 a batch with one bad row writes nothing and names every bad row; K2 `revise` then `stale` of the old id leaves the new row live; K3 `passes` refused in comparison and night with the frame text; K4 two concurrent `add` calls both land with distinct `seq`; K5 `check` names a dangling `from` and an absolute path; K6 a performer `add` of `passes` or `probes` refused with its door; K7 an `expectations` row keys REQ-n without changing REQ-n's id.
- error direction (N6, `add` as a gate on writers): the launch env can be forged by an agent's own shell, so `record.py` errs toward refusing; `exit_check.py` additionally counts a pass only when its question's answer row is tool-written and a probe only when its `by` matches a `critic.py` launch event in the journal (C4-6). Adversarial inputs that stay refused: `speaker: person` in a performer batch; `by: critic` in a performer batch; a pass naming an unanswered or performer-written question.
- edges: `add` refuses only what no later row can make valid (unknown section or field, enum outside its set, dangling reference, absolute path, mode-barred row); a missing typed field is accepted, its debt is the gate's at exit (invariant: no mid-stage block for incompleteness, plan 1a rule 1; no gate is bypassed: X1/G-rules still see it); empty batch -> refused "nothing to add"; batch over 500 rows -> refused naming the count (AT 500 accepted); field text is never cut; non-UTF-8 or BOM batch -> refused naming the byte offset; record absent -> every command but `init` refused, door `record.py init`; record unreadable -> exit 2, door `record.py check`, never read as empty (AR-28); `stale` of an already stale row -> no-op, named; `revise` of a superseded row -> refused, door "revise the live row <id>"; lock holder crashed -> broken after 60 s, never earlier (two writers never interleave).
- test: `factory/tests/test_record.py` one table, strongest first: batch all-or-nothing | frame 2a; revise/stale over `supersedes` | 2a "Derived"; mode refusals | 2a; concurrency | F11; check defects | this card; battery (empty, 500/501 rows, deep nesting, non-UTF-8, BOM, broken YAML) | CLAUDE.md rule 11.

### C3-2 Stages, routes, loader, W1, context (2b)
- amended by: A3, A4, A6, A7, A8, A10, A12, A16, A21, A24, A26, A27, A28, A31, A32, A33, B16 (cards whose `amends:` line names this card; read them with it)
- Delivers: `routes.yaml`: `story: [sources, product, plan, tests, reds, report]`. `stages.yaml` (frame 2b fields; X1-X6 implied on every row, not listed; `critic` names the stage's own `craft` set, F12):

| id | reads | leaves required / optional | craft (C2-x ids) | exit / after_critic | critic | stop | grouped, parallel_max |
|---|---|---|---|---|---|---|---|
| sources | - | sources, understanding, requirements, questions, exits / findings, assumptions, unknowns | requirements, questions | G1.1-G1.4, D2 / D1 | none | understanding + `approve` | no, 1 |
| product | sources, understanding, requirements, questions | runs, evidence, knowledge_writes, exits / findings, assumptions, unknowns, questions | stand, exploration | G2.1, G2.2 / - | none | `critical` only | no, 1 |
| plan | sources, understanding, requirements, questions, runs, evidence, findings | expectations, checks, exits / requirements (new ones), questions, findings, assumptions | requirements, check-selection, levels, automate, regression | G3.1-G3.4 / D1 | craft | test_plan + `approve` | no, 1 |
| tests | requirements, expectations, checks, questions, runs, evidence | tests, links, runs, results, evidence, exits / reds, findings, assumptions, questions | test-code, manual-pass, exploration, automate | G4.1-G4.4 / G4.5 | craft | none | yes, 2 |
| reds | requirements, checks, tests, runs, results, evidence | reds, bugs, exits / runs, findings | red-analysis, bug | G5.1-G5.3 / D1 | none | `bug_or_not` | no, 1 |
| report | all live sections | results, delivery, exits / findings | report | G6.2 / G6.1, G6.3, D1 | craft | test_report + `approve` | no, 1 |

- The `exit` column is the one source of where a rule falls DUE (N1): from that stage on it runs at every exit; D2 only at `sources`; stage-4 rules over the exiting group's rows.
- `rows.py`: `load()` of every `factory/data/*.yaml` (frame 2b); `walk` = W1: each `reads` section is a `leaves` of an earlier route stage; each `leaves` section has a later reader or a reader tool (`docs_build.py`, `export_md.py`); each typed field's `readers` exist as files in `factory/tools/`; each `craft` id in `craft-pages.yaml` with its file; each exit id in `gate-rules.yaml`; each stop id in `person-docs.yaml` or `questions.yaml`; prints every miss, exit 1.
- `context.py --story --stage [--group] [--relaunch <file>]`: writes `<story>/runs/context-<stage>-<group>-<n>.md`: the stage row; its craft pages whole; live rows of `reads` whole and byte-equal to the record (plan 1b needed 3); knowledge values with `absent_means` printed (C3-6); the tool command lines (`record.py`, `exit_check.py`, `run_tests.py`, `evidence.py`, `ask.py`, AR-8); the relaunch block (C4-1). Prints `start_load_bytes: <n>`; journaled by C4-1 (AR-11). F9 ceiling `null` -> number reported, no comparison; over the profile's `context_window_bytes` (C4-5) -> exit 3 `over window: <n> > <w>` and C4-1 moves to `no_move` (never cut, frame 2b).
- owns: C:/QAFactory/forge2-repo/factory/data/stages.yaml, C:/QAFactory/forge2-repo/factory/data/routes.yaml, C:/QAFactory/forge2-repo/factory/tools/rows.py, C:/QAFactory/forge2-repo/factory/tools/context.py, C:/QAFactory/forge2-repo/factory/tests/test_rows.py
- deps: C3-1, C2-1 (page index; fixture pages until C2-2..C2-5, frame 6); F12, F42; N1, N2.
- keys: K1 W1 green on the shipped rows; K2 W1 names a read with no producer and a field with no reader file; K3 context sections byte-equal the record rows; K4 an absent data file refuses `load()` naming file and card; K5 over-window exit 3 writes no cut file.
- edges: `reads` empty -> only stage 1 (frame 2b); a `reads` section with zero live rows -> handed as its `empty:` row or `not recorded: <section>`, never omitted; grouped stage with no group label on `expectations` rows -> one group (axis 11; F42); window field absent from the profile -> comparison `unknown`, journaled, launch proceeds (a host launch error then goes to `no_move`); craft page absent -> W1 names it, stage not launchable (frame 6 row "craft pages"); unknown route -> refused naming `story`.
- test: `factory/tests/test_rows.py` one table: W1 (each miss class, green rows) | frame 2b, 1b needed 1; loader absent/unreadable per file | 2b; context byte-equality and relaunch block | plan 1b needed 3; window over/at | 2b, F9; C3-7 rows | C3-7; battery on a person-edited data row (broken YAML, non-UTF-8, duplicate id) | rule 11.

### C3-3 Gate rules, reasons, red causes, exit check
- amended by: A3, A4, A6, A7, A8, A9, A16, A23, A24, A25, A26, A27, A28, A30, A33, A34 (cards whose `amends:` line names this card; read them with it)
- Delivers: `gate-rules.yaml` (frame 2c fields, one row per id of frame 3); `when` and door per id (door always also a `passes` row, frame 2c; `when` values beyond `exit|after_critic` are fork F41; ORDER per r2 N4: exit -> `docs_build.py` preview -> critic -> fix rounds, each rebuilding the preview -> `after_critic` on the built document -> stop; a stage with no critic: exit -> build -> `after_critic` -> stop). DUE per N1 at the stage whose `exit` column (C3-2) first names the rule; DEBTOR per N1: a shape rule on a row's own fields -> the row's stage; "each X has a Y" -> the stage leaving Y (G3.1 -> `plan` via `expectations`; G3.2 -> `plan`; G4.2, G6.2 -> `tests`); otherwise the exiting stage, never the author of X; debtor exited -> shortfall:

| ids | when | door (besides `passes`) |
|---|---|---|
| X1, X2, X4, X6 | exit | the row, an `empty:` row, a named reason (X6: `other` provisional until a `reason_verdicts` row, N7; `returned` opens a shortfall) |
| X3 | exit (per group; no `observe`: once at stage exit) | reference the file/run in a row |
| X5 | exit (hook `outward_write` mid-stage, C4-5) | a person's permission row |
| G1.1-G1.4, D2 | exit (D2 at `sources` only; a later requirement is placed by G3.2, N1) | read or "source unavailable" + attempt; the row |
| G2.1, G2.2 | exit | the run, or "no environment" + attempt; knowledge row or "nothing new" |
| G3.1-G3.4, G4.1-G4.4, G5.1-G5.3, G6.2 | exit | the field, link, run, evidence or reason; G4.1 a requirement row of lower `seq` (else defect); G4.4 `n/a` row without key `linter` |
| G4.5 | after_critic | `critic.py` relaunched for the unprobed tests only, inside F8, else a "not proven" row to the report (N5) |
| G6.3 | after_critic | close the debt or shortfall (-> `refused`, relaunch, back to after_critic, N5) |
| G6.1, D1 | after_critic, on the built document (N4) | a fix round: `revise` the author field, rebuild, critic re-check |
| G3.C, G4.C, G6.C | critic (state `in_critic`) | finding closed in a fix round, else `to_report` |
| G1.P, G2.P, G3.P, G5.P, G6.P | stop (state `at_stop`) | the person's answer (comparison/night: launching model, stops only) |
| D3 | ask (`ask.py`), floor at exit (C4-5) | cite a document/form id |
| W1 | ci (`rows.py walk`) | fix the stage row or schema |

- `reasons.yaml`: the seven rows of frame 2c plus `executed by agent, no evidence` (needs why; N8), each `id`, `words`, `needs` (attempt, words, or none). `red-causes.yaml` (plan V23): `product_bug`, `test_error`, `case_or_expectation_error`, `expectation_stricter_than_requirement`, `environment`, `wrong_version`, `flaky`, `no_defect`; each `who_acts`, `needs`.
- `exit_check.py --story --stage [--group] --when exit|after_critic`; predicates (closed list): `row_or_empty`, `exit_answers`, `world_unreferenced` (C3-4 output), `no_stale`, `outward_permitted`, `reason_closed`, `fields_present`, `xref_both_ways`, `lower_seq`, `result_per_obligation`, `probe_per_autotest`, `later_row`, `built_after_last_fix`, `within_budget`, `linter_passed`. One output (AR-18), YAML on stdout: `story, stage, group, when, verdict: met|refused|unknown, debts: [{rule, row, owed_by, kind: refused|shortfall, what, doors}], unknowns: [{rule, why, default}], provisional: [{row, reason}]`; exit 0 met, 1 debts, 2 cannot read (door `record.py check`), 3 unknown only.
- owns: C:/QAFactory/forge2-repo/factory/data/gate-rules.yaml, C:/QAFactory/forge2-repo/factory/data/reasons.yaml, C:/QAFactory/forge2-repo/factory/data/red-causes.yaml, C:/QAFactory/forge2-repo/factory/tools/exit_check.py, C:/QAFactory/forge2-repo/factory/tests/test_exit_check.py
- deps: C3-1, C3-2, C3-4 (output shape; fixture until built), C3-8; F12, F41; N1, N2, N4, N5, N6, N7, N8.
- keys: K1 every frame-3 id has one row with `when`, `door`, `protects`, `origin`; K2 a fixture record yields all debts at once, each with doors incl. `passes`; K3 a met row stays met after an unrelated new row (frame 2c invariant); K4 REQ added at stage 4 with no `expectations` row -> G3.1 shortfall owed by `plan` (N1 debtor), never a debt of `sources`; K5 `other` reason -> `provisional` until its `reason_verdicts` row, never a debt; K6 a `passes` over an `owner: data` rule also yields a `factory_findings` row request; K7 `sources` exits without any `expectations`, checks or results (N1: G3/G6 rules not yet due); K8 group A's exit sees no debt on group B's rows.
- edges: a pass whose question's answer is not tool-written, a probe with no matching `critic.py` launch event -> not counted (N6); a debt whose debtor exited -> `kind: shortfall` (N1); unknown predicate name in a row -> W1/CI red, never skipped; `on_unknown: default: <v>` -> printed in `unknowns`, never silent; no `linter` key -> G4.4 `n/a`; no VCS -> X3 `unknown` with the frame-3 behaviour; a reason row without its `needs` -> debt naming the missing attempt or words; zero rows in a required section and no `empty:` -> X1 debt (AR-23); record unreadable -> exit 2, never `met`; error direction: predicates read ids, links, `seq`, presence, never wording (FR-12) -- they err toward a debt on a missing link (door named) and never toward `met` on an unread row.
- test: `factory/tests/test_exit_check.py` one table, rule id x {met, debt, shortfall, unknown, passed}, strongest first: due stage + debtor + per-group scope + met stays met | frame 2c r2 (N1); G4.1 order | plan 1b check 4; X6 provisional | 2c, fix 1; G4.5 after critic | 2c ORDER; C3-8 kinds via G3.1 rows | C3-8; output shape | AR-18.

### C3-4 World diff per group (X3)
- amended by: A8, A16 (cards whose `amends:` line names this card; read them with it)
- Delivers: `world.py snapshot --story --stage [--group]` (called by C4-1 at launch: per `repositories` root: VCS head, status, sha256 of dirty and untracked files; stored in `<story>/runs/world-<stage>-<group>.yaml`); `world.py diff --story --stage [--group]`: touched set = paths of the group's agent's `observe` events (journal, C4-6) when the host proves `observe` (C4-5), else snapshot vs now for the whole stage; minus VCS-ignored files (`check-ignore` of the root's VCS), minus `work_root`; compares with every path field of live rows (any stage) and with run output files under `<story>/runs/`; output `{status: compared|unknown, why, unreferenced: [{path, op: created|changed|deleted}], runs_unreferenced: [run ids]}` for X3.
- owns: C:/QAFactory/forge2-repo/factory/tools/world.py, C:/QAFactory/forge2-repo/factory/tests/test_world.py
- deps: C3-1, C3-6 (`repositories`), C4-5/C4-6 (`observe` events; fixture events until built).
- keys: K1 group A's exit lists none of group B's files (fix 7); K2 an ignored build output is never listed; K3 no VCS -> `unknown: no VCS`; K4 no `observe` -> one diff at stage exit after all groups.
- edges: a file touched by two groups -> a reference in any live row clears both (the record is shared); created then deleted before exit -> not listed; a deleted tracked file -> listed `deleted`; a root outside `repositories` touched -> not X3's: X5/`outward_write` own it; snapshot absent at exit (launch crashed) -> `unknown: no snapshot`, never `compared` (AR-28); over 50 unreferenced files under one directory with none referenced -> one entry per that directory with the count (small choice, section 4); non-UTF-8 path -> kept as bytes escaped, never dropped.
- test: `factory/tests/test_world.py` one table on temp repos: parallel groups, ignored, deleted, no VCS, no observe, no snapshot, directory grouping | frame 3 X3, fix 7; battery on observe JSON (empty, broken, huge path list, non-UTF-8 path) | rule 11.

### C3-5 Person documents; templates
- amended by: A2, A3, A4, A5, A6, A7, A22, A24, A25, A26, A27, A28, A29, A30, A33, A34, A35 (cards whose `amends:` line names this card; read them with it)
- Delivers: `person-docs.yaml` (frame 2d fields) and `factory/templates/<id>.md`, fixed sections from plan 1v; `docs_build.py --story --doc <id> | --form bug_or_not` writes `<story>/docs/<id>.md`; counts and statuses only by code; author text from record fields, never cut by code; a list over its row budget shows the first rows then `and N more (ask to see them)` (the person never gets a working file, plan 1v issue rule 1); empty section -> its `empty-outcomes.yaml` words; absent record section -> `not recorded: <section>` (frame 2d).

| doc | from (record) | fixed sections | budget |
|---|---|---|---|
| understanding | sources, understanding, requirements, questions, assumptions, findings | Sources (read, unavailable + tried, gave no requirements); Why this change; How understood; What we check (row per requirement + source kind); What we do not check and why; What else may be affected; Contradictions; Blocking questions; count line | 40 lines; requirement rows 15 then "and N more" |
| test_plan | understanding, requirements, checks, findings `about: plan:<s>`, questions | Goal and depth; Pyramid decision per level (`levels`, C3-1); Checklist by level (row per check: what, requirement, breaks, impact, mode, level); Techniques; Seams; Requirements without a check + reason; Non-functional; Regression or "no regression: why" (P24); Environment; What you decided; Questions to the team | 40 lines; 15 check rows then "and N more" |
| manual_pass_report | checks (mode manual), results, evidence, runs | Count passed of planned; per case: expectation verbatim, how it was + source or "not recorded in requirements", what the agent saw, outcome, screenshots inline (relative paths, before/after); "executed by agent, no evidence: why" | list never cut (plan 1v); author text 6144 bytes |
| test_report | all live sections, passes, delivery preview | Look first (brief); Change; Verdict (three outcomes, P21); Proven; Checked by hand (link to manual_pass_report); Product bugs; Tests the critic did not accept; Left to you (`readiness`, `executable_where`, regression); Open questions; Skipped by plan; Not proven; Coverage level x mode; Readiness per requirement; What you decided (verbatim); Added after approval (`seq > approved_plan_seq`); Not critiqued; Reasons (with `reason_verdicts`, N7) and passes by name; Goes outward (C3-7 preview); Factory defects; Appendix traceability | author text 6144 bytes; brief 2048 bytes, 5 items |
| retro | - | F3 (a): row `required: false`, `when: none`, no template; F3 (b): plan 1v section 5 | - |

- Traceability appendix: one row per (requirement, obligation) with each linked test and outcome from `passed, bug, waiting, blocked, not_run, unreachable, deferred, not_planned` (plan 1v); many-to-many kept: an obligation with three tests is one row listing three, a test serving two obligations appears in both.
- `q-bug-or-not.md`: from bug-draft rows: what broke, expectation + source, fact, evidence path, repro, origin (plan V26), options with cost; 40 lines, 5 bugs then "and N more"; manual fails attach `manual_pass_report` (F2 (a)). Export templates `export-cases.md`, `export-bugs.md` for C4-8.
- owns: C:/QAFactory/forge2-repo/factory/data/person-docs.yaml, C:/QAFactory/forge2-repo/factory/templates/, C:/QAFactory/forge2-repo/factory/tools/docs_build.py, C:/QAFactory/forge2-repo/factory/tests/test_docs_build.py
- deps: C3-1, C3-6 (doc language), C3-7; F1, F2, F3, F4, F13; N4 (`--preview` before the critic, rebuilt each fix round), N2 (checklist and report read `expectations`).
- keys: K1 every count in a built doc equals a count over the record; K2 16 requirements -> 15 rows + "and 1 more"; 15 -> no marker; K3 a template holds no factory field, file or tool name (template test, F13 (a)); K4 every requirement placed in check / not check (D2 view); K5 empty section -> its words, never omitted.
- edges: author text over 6144 bytes or brief over 2048 bytes / 5 items -> built whole, D1 debt (code never cuts author text; door `revise`); 40-line budget vs one row per requirement (pair) -> row budget wins, "and N more" keeps the count; doc language key not `en` with no `templates/<lang>/` -> English template, line "template in English: no <lang> template" (F4); record section absent -> `not recorded`; evidence file missing -> case shows "evidence missing: <id>", never "passed"; no bug drafts -> no bug form built (C4-3); stale/superseded rows never shown.
- test: `factory/tests/test_docs_build.py` one table: per doc on one fixture record (counts, budgets AT/BEYOND, empty, absent, many-to-many appendix, language fallback, template names) | plan 1v, frame 2d; battery on author fields (huge, nested markdown, non-UTF-8, empty) | rule 11.

### C3-6 Project knowledge (2g)
- amended by: A1, A2, A6, A7, A8, A9, A10, A26, A27, A29, A30 (cards whose `amends:` line names this card; read them with it)
- Delivers: `knowledge-keys.yaml` rows `key`, `default`, `absent_means`, `asked_when`, `readers`:

| key | default | absent_means | asked_when | readers |
|---|---|---|---|---|
| work_root | `.light-factory` | default | never | every tool |
| commands (build, run, test, screenshot) | none | performer finds, records `found:<how>` | not found after an attempt | context.py, run_tests.py, evidence.py |
| linter | none | G4.4 `n/a` | never | exit_check.py |
| repositories (root, product/tests) | project root, product | project root only | first write under an unknown root (2e); never in comparison/night: only roots present at launch, the write refused and named (N9) | hooks, X5, world.py |
| surface_kind | none | performer judges | never | context.py |
| stand | none | "no environment" with attempt | first run need | context.py |
| raise_permission | false | not allowed (plan V13) | first need to raise | context.py |
| who_answers | the session's person | default | never | ask.py |
| accept_target | `md` | `md` + preview | never in phase 4 | docs_build.py, export_md.py, exit_check.py |
| doc_language | `en` | English, printed (F4) | never | docs_build.py |
| marathon_minutes | 20 | default | never | dashboard.py |

- `knowledge.py get <key>` (value, or `default: <v> (absent_means: ...)`), `set <key> --value --source "<words verbatim>"|found:<how> --by <agent:role>`, `list`; same lock and atomic write as C3-1; ONE writer (frame 2g).
- owns: C:/QAFactory/forge2-repo/factory/data/knowledge-keys.yaml, C:/QAFactory/forge2-repo/factory/tools/knowledge.py, C:/QAFactory/forge2-repo/factory/tests/test_knowledge.py
- deps: C3-2 (`rows.py`); F4.
- keys: K1 absent file -> each key's default printed with `absent_means`; K2 `set` keeps the words byte-equal; K3 unknown key -> refused naming the keys file, door "add a key row (factory finding)".
- edges: `knowledge.yaml` absent -> defaults (frame 6); unreadable -> error naming the file, door "fix or remove it", never defaults (AR-28); `set` without `--source` -> refused (no unsourced fact); a second `set` of a key -> new value row, old kept with its source; `repositories` root given absolute -> stored relative to the project root when inside it, else kept absolute as an outward root (AR-4 does not apply to roots).
- test: `factory/tests/test_knowledge.py` one table: get default/value, set verbatim, unknown key, unreadable, concurrent set | frame 2g; battery on `--value`/`--source` (10 KB, newline, non-UTF-8, empty) | rule 11.

### C3-7 Delivery targets (only `md`)
- Delivers: `delivery-targets.yaml`, one row: `id: md`, `writes: [cases, bugs, report]`, `where: <work_root>/stories/<id>/delivery/md/`, `outward: false`, `preview: true`, `tool: export_md.py`. Readers: `export_md.py` (C4-8), `docs_build.py` "Goes outward" (C3-5), `exit_check.py` X5 (`outward: false` needs no permission), key `accept_target` (C3-6).
- owns: C:/QAFactory/forge2-repo/factory/data/delivery-targets.yaml
- deps: C3-2.
- keys: K1 `rows.py load()` reads the row; K2 W1 finds a reader for each field.
- edges: `accept_target` names an id with no row -> `md` + preview, line "target <id> not built: md used" (axis 6; phase 7 adds rows); an outward target row in phase 4 -> none exists, X5 refuses outward (frame 6 row "seams").
- test: rows in `factory/tests/test_rows.py` | frame 4 index; frame 2e, axis 6.

### C3-8 Expectation-source kinds
- amended by: A4, A5, A7, A15, A27 (cards whose `amends:` line names this card; read them with it)
- Delivers: `expectation-sources.yaml` (plan V6): `explicit_requirement`, `keep_as_before` (old system, "keep as it was"; "was so but looks like a bug" is a question, not a kind), `confirmed_precedent`, `person_word` (needs a question id), `common_logic` (flagged, needs person confirmation: a question id); each `id`, `words`, `needs`. `none` = "no reliable expectation source" (frame 2a), never a row of its own; the product's code is never a kind (P20, FR-58). Readers: `record.py` (`enum_from` of `expectations.kind`, N2), `exit_check.py` G3.1, `docs_build.py` checklist and report, C2-2's page by citation.
- owns: C:/QAFactory/forge2-repo/factory/data/expectation-sources.yaml
- deps: C3-2.
- keys: K1 G3.1 met by each kind, by `none`, refused on an absent field; K2 a kind outside the file refused by `record.py add`.
- edges: `person_word` or `common_logic` without its question id -> G3.1 debt naming the missing id; `none` -> expectation open, no literal check (plan V6).
- test: G3.1 rows in `factory/tests/test_exit_check.py` | plan V6; frame 2a, 3.

Bodies C4-1..C4-8: part 3b, `docs/tasks/specs/20261125-forge2-light-factory-spec-part3b.md` (moved byte for byte by the Lead's script at acceptance).

## 3. Forks

F40 (G6.1/D1 timing) and F44 (carrier of an `other` reason's acceptance) of this draft are withdrawn: answered by the Lead's N4 and N7.

**F41** (C3-3; frame 2c `when: exit|after_critic` vs frame 3 rows owned by the critic, the person, `ask.py` and CI): (a) every frame-3 id stays a row of `gate-rules.yaml` (one home, F12 "How checked" generated from it, AR-19) and `when` gains `critic|stop|ask|ci`; `exit_check.py` evaluates only `exit|after_critic`. Cost: frame 2c enum grows. (b) C and P rows live only in stage rows (`critic`, `stop`), D3 in `ask.py`, W1 in `rows.py`; `gate-rules.yaml` holds data rows only -- How checked must then read three homes. Rec (a).

**F42** (C3-2, C4-1; frame 2b `grouped`, axis 11 "unknown value -> one group"): who forms stage-4 groups (N1's row `group` records the writing launch's group, not which requirements a launch gets). (a) The `plan` performer writes a group label on each `expectations` row (N2 section; judgment, axis 11 role); absent -> one group; a typed field + W1 reader (`context.py`, `run_stage.py`). (b) Code splits by a fixed count in id order -- related requirements split apart. (c) Always one group until the conductor splits on the window -- no parallel groups in practice. Rec (a).

**F43** (C4-1; frame 2a conductor out "rows `by: conductor`" names no section; N5 adds a target state but no section): (a) a new section `decisions` (decision, reason, option id, target state) in frame 2a -- clean, as fix 6 split critic findings from `findings`. (b) `findings` rows `about: conductor` -- re-overloads `findings` (fix 6's defect). Rec (a).

## 4. Frame gaps

Bodies resting on the Lead's r2 decisions (check against frame r2, t-1920, when it lands):
- N1 (due stage, debtor, row `group`, per-group scope, D2 G1-only): C3-1, C3-2, C3-3, C3-4, C4-1.
- N2 (`expectations` section, stable requirement ids): C3-1, C3-2, C3-3, C3-5, C3-8, F42.
- N3 (merged into N1): as N1.
- N4 (preview -> critic -> fix rounds -> after_critic on the built document -> stop): C3-3, C3-5, C4-1, C4-2.
- N5 (moves for unmet after_critic, G4.5 critic relaunch, conductor target state, critic-less fixes): C3-3, C4-1, C4-2, F43.
- N6 (`passes` only by `ask.py`, `probes` only from a `critic.py` launch): C3-1, C3-3, C4-2, C4-3.
- N7 (`reason_verdicts`): C3-1, C3-3, C3-5, C4-2, C4-3, C4-6.
- N8 (named reason "executed by agent, no evidence"): C3-3, C4-4.
- N9 (no new roots in comparison/night): C3-6, C4-3, C4-5.

Gaps of r1 still open after N1-N9:
- 2c `when` enum vs frame 3 C/P/D3/W1 rows -> F41; 2b `grouped` with no group-forming carrier -> F42; 2a conductor out with no section -> F43.
- 2a `at_stop` for a form with nothing to ask (G5.P, no bug drafts): reading in C4-3 -- not asked, `empty: no_bugs` closes G5.P.
- 2a `at_stop` "by answer (V4)" for free words: reading in C4-3/C4-1 -- the conductor classifies (judgment, P22), code never guesses.
- 2b `critic` (`none`|page) vs a stage with several craft pages and plan 5 "the same page": reading in C3-2 -- `critic` names the stage's craft set; W1 refuses a page outside it.
- 2a typed fields silent for D2 placement and the test-plan columns: settled in C3-1 as optional fields of untyped sections (frame 2a lists typed fields for seven row kinds only); test-plan sections with no section use `findings` `about: plan:<s>`.
- 2f ONE writer vs `observe` events from a hook: reading in C4-5 -- the hook calls `journal.py`.
- F7 "a rate row" with no file allowed to hold a rate: reading in C4-6 -- `--rates` at display, outside the repo.
- 2d budgets vs plan 1v "manual-pass list never cut": reading in C3-5 -- that list carries no row budget.

## 5. Trail

- Read whole: frame r1 (382 lines), part 2 (236 lines), verdict t-1915 (345 lines). Plan v1.3 read: 16-45, 523-940 (sections 1, 1a with the gate table, 1b, 1v, section 2 table V1-V30), 1078-1095, 1226-1296 ("Reshila sama"), 1380-1391 (V6 question). `docs/TESTING.md` 36-95. Host plan `20261124-host-profile-hooks-plan.md` 68-87, 173-219.
- Not read: plan 46-522, 941-1077, 1096-1225, 1297-1563; host plan sections 10-16; `forge/TESTING.md` (not yet in forge2-repo per brief); nothing under `experiments/**/runs/`.
- Facts used from `facts:`: frame r1 at 12a00c2c8, 39286 bytes; 16 `P3` rows; part 2 19 bodies; handoff absent before this write.
- Readers (rule 7): every file owned here is new in `C:/QAFactory/forge2-repo`; their readers are those the frame names (2a "Readers", 2b-2g "Readers", field `readers`) and each body's deps; no `owns_readers.py` block attached and no shell here -> `estimate`, the Lead runs `python -B tools/owns_readers.py --paths <owns>` once the files exist.
- Re-review t-1919 read: "New defects of the round" N1-N9 (lines 37-102) and the fix list (118-127), per the Lead's mid-task note.
- Size: `estimate`, about 50 KB before the N-edits, more after (Grep line-length bands on this file: lines at least 50/100/200/300/500/600/800/1000 chars = 182/139/97/60/23/16/5/2 of 256; band midpoints sum about 51 KB) -> over the cap, hence the `decomposable:` line at the top (no shell); Lead runs `python -B -c "import os,sys;print(os.path.getsize(sys.argv[1]))" docs/tasks/specs/20261125-forge2-light-factory-spec-part3.md`. DoD command `grep -c -E '^### C[34]-[0-9] ' <this file>` -> 16 expected (Grep check below).
- Small choices closed: stage ids `sources, product, plan, tests, reds, report`; `parallel_max` 2 for `tests`; `record_lock_wait_s` 10, batch cap 500, answer kept whole at any size, `test_timeout_s` 1800, run summary 20 lines; directory grouping over 50 unreferenced files (C3-4); language fallback to the English template (C3-5); `findings` `about: plan:<s>` for test-plan prose sections.
