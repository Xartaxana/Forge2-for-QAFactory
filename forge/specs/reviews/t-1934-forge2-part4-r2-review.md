verdict: blocker

# t-1934 -- narrow critic pass on fix round r2 of spec part 4 (light factory), at 9e800eee8

Scope: F17 part 3 and N1-N9 of t-1932, plus new defects only inside the text r2 added or changed (all 22 `r2 N` marks; the 15 hunks of the attached diff). Text r2 did not touch was not re-reviewed. The 19 closed findings were not reopened. Part 4b was not read. Plan gate (rule 24).

## Findings of t-1932

- F17: closed -- part 3 (the proposed test) now keeps the person's yes on both roads. Before approval: A4 "NOT ONLY WHAT FAILED", the r2 N2 upgrade move at the plan stop. After approval: A3 G6.4, the REQ's own accepting `source` answer (r2 N1). Two caveats are new findings in the r2 text: M1 (the source road confirms too much) and M2 (the plan-stage assumption branch).
- N1: closed -- A3 "The question": the launcher skips a late REQ whose `source` is a tool-written accepting answer. G6.4 `late_confirmed` counts that answer. K4' and the G6.4 test row `{source = accepting answer}` cover it. This matches t-1932's fix line. But the source road is not scoped to its carrier (M1, blocking).
- N2: closed -- A4: an expectation tied to a "Questions to the team" row is kind `none` with `from` until the stop. At `approved`, `run_stage.py` revises it to `person_word` with the approve qid. `partial` stales the struck rows and `fixes` revises nothing. K4 and the `test_run_stage.py` rows cover it, and C4-1 is named in amends. This is t-1932's first fix alternative. Two defects remain: the added branch "any expectation resting on an assumption written at `plan`" confirms what the person was never shown (M2, blocking), and the invariant "always reaches `tests`" has no carrier (M7).
- N3: closed -- A24 now has a launch row `explore` (leaves `findings` required). Its exit judges only that launch's rows and never the stage's exit column. No stage state changes, the outcome is an `exits` row, and debts end as `stopped: debts` while the route goes on. K6 and the test rows cover it, and C3-2 and frame 2a are named. This is t-1932's fix road. But limiting the exit to X1 and X2 creates a new debt-routing defect (M3, blocking), and the new exit mode lacks its amends lines (M4).
- N4: closed -- A10 (3): only `run_stage.py`'s approval move writes a `sets_keys` key. It copies the value from the rows live at the approve seq. A launch's call is refused whatever `--value` says, and a K-new key plus three test rows cover it. This is t-1932's second fix alternative. The mechanism of "called by a launch" is unstated (M6, non-blocking).
- N5: closed -- A21 How checked adds X1-X6 to every page, with X5 in its A2 meaning, and W1 reads them as due at every stage. The r2 N5 key makes a missing X row red in `pages_check.py`. This matches t-1932's fix line.
- N6: closed -- A3: the rebuilt report goes back to the report stop with A5's changes block, and an answer that changes no status gives no second stop. The person no longer receives a report she was not shown. On the brief's question, "no critic round is owed": it holds against frame 2c ORDER only in part. ORDER's invariant ("the person never sees a document the critic has not seen") protects against unseen role-written content. For lines `docs_build.py` computes from rows (statuses, readiness, counts, frame 2d "counts never authored"), the critic has nothing it could judge, so the claim holds there. It fails for the role-written text of `test_report` ("author text 6144 bytes", brief "Look first", part3:97). That text can name the late REQ the answer just staled, and a rebuild from rows reproduces it unchanged. The literal invariant is also broken, A3's amends names no frame 2c exception, and the after_critic rules are not re-run before the second stop. See M5.
- N7: closed -- A1 MEASURES: `story_wall_s` excludes the `run_tests.py` child intervals, as `wall_s` does, and the report prints the test-run time on its own line. This differs from t-1932's fix line, which proposed deriving the row from `test_timeout_s` or naming an edge. The difference closes the finding: a 25-minute suite no longer cuts the story, and "6 x the stage wall cap" now compares like with like. Side effect on F70 (a): M8.
- N8: closed -- A22 Shared runs: with no failure location in the runner output, the probe of a shared run is invalid and rerun alone. The error direction is stated. Note, not a finding: `per_test` (part3b:48) has no location field, so as written every failed probe of a shared run is rerun alone. A shared run then saves runs only for survivors. This is safe and costs runs.
- N9: closed -- A6 Delivers: a code-built form with no rows file and no `templates/<chat_language>/` goes out with the English template, a journal `unknown: no template for <lang>`, a report line and a finding `template_missing`. It is never silent, which matches t-1932's fix line. The example list wrongly includes the `new_requirements` question (M9, non-blocking).

## New findings

M1 (blocking: yes; rule 15 pair, error direction). Where: A3 gate row G6.4 `late_confirmed` "OR on the REQ's own `source` question" and "The question" "whose `source` is not a tool-written answer carrying an accepting option" (part4.md:50-51, r2 N1).
- What breaks: the REQ's `source` is written by the performer through `record.py add`, which refuses only a dangling reference (part3 C3-1 edges). Nothing ties the accepting answer to this REQ. The source question was asked before the REQ existed, so it cannot name it, and nothing ties the REQ to the `findings` row that question was about.
- Concrete case: Q5 (`beyond`, about finding FND-3 "the empty cart shows 0.00") is answered `should_be_so`. At `tests`, a performer writes an unrelated REQ-30 "discount capped at 50 %" with `source: answer:Q5`. The launcher skips REQ-30 (the r2 clause), and G6.4 counts it confirmed. The report shows REQ-30 proven, though the person never saw it. One answer can also confirm any number of REQs.
- This contradicts A3's own error direction ("errs toward `unconfirmed`, never toward confirmed") and A3's edge invariant (part4.md:54, untouched by r2 and now false): "no late requirement is counted proven without the person's `is_requirement`".
- Fix:
  - The REQ names the answered finding (`from: <findings id>`). The source answer counts only when its question's rows hold that finding and its option accepts it, with at most one live REQ per (question, finding). Otherwise the REQ is `unconfirmed` and the launcher asks about it.
  - Reword the line-54 invariant to name both roads.
  - Add a G6.4 test row `{source answer on another finding -> unconfirmed and asked}`.

M2 (blocking: yes; yardstick "no autotest rests on an expectation the person has not confirmed"). Where: A4 "NOT ONLY WHAT FAILED", r2 N2: "and any expectation resting on an assumption written at `plan`".
- What breaks: the test plan does not show assumptions. Its row reads `understanding, requirements, checks, findings about: plan:<s>, questions` and has no assumptions section (part3:95). A5 adds "Agent's assumptions" to the understanding only, at the stage-1 stop. A plan-stage assumption row is therefore never in the text the plan stop shows. Yet on `approved`, its expectation becomes `person_word` and gets an autotest.
- Concrete case: the plan performer writes ASM-7 "the code rounds half-up intentionally" and an expectation kind `none` with `from: ASM-7`. The plan stop shows the test plan without ASM-7. The person approves, the move revises the expectation to `person_word`, and `tests` writes a literal check on an expectation she never saw. `partial` cannot strike what is not shown, so the stale-on-strike edge is dead for this branch.
- Fix: either drop the assumption branch from the move (a plan-stage assumption stays `none` or is asked as a "Questions to the team" row), or add a test-plan section "Agent's assumptions" (C3-5 amends, A5's form) so the approval covers only what was shown. Add a K row for the assumption branch; K4 covers only the "Questions to the team" branch.

M3 (blocking: yes; edge "a launch held by another launch's debt"). Where: A24 Exit, r2 N3: "the rules X1, X2 over the rows THIS launch wrote".
- What breaks: X3-X6 are implied on every exit (part3:34) and run over every live row whoever wrote it (frame 2c). Dropping them from the explore exit does not remove the debts. It moves them to the next exit of another launch, whose debtor cannot fix them.
- Concrete case, X6: explore writes `findings kind: beyond outcome: not_done reason: "stand unavailable"` with no attempt. A24's own edge invites this row. X6 (reason closure, spec:169) is not judged at the explore exit, so the exit is met. At the `plan` exit X6 finds the row. The debtor is the row's own `stage` = `product` (`FACTORY_STAGE=product`), so a shortfall relaunches the exited `product` performer. At `reds` the row carries `stage: reds`, so the reds exit is refused for explore's row. That is the very A16 invariant the r2 text cites.
- Concrete case, X5/X3: explore holds `exec`, and the hook errs green on indirect writes (A12 edge: "X3 and X5 at exit are the second net"). Its `npm run build` changes a tracked product file. The explore exit does not judge X5. A2's invariant makes it an X5 debt at the `plan` exit, debtor `plan`, which has `write_work` only and cannot undo it, so the debt goes to the conductor.
- Second defect in the same sentence: "its launch id" is a field no record section carries (grep `launch[_ ]id` over the spec files: one hit, this line). Scoping by launch id also breaks the relaunch. A first launch writes four looks but no exits row (X2 debt). The relaunch writes the exits row, and its own exit finds no `findings` row by its id (X1 debt). It loops to `stopped: debts` and the looks are lost.
- Fix:
  - The explore exit runs X1-X6. X3 and X5 are scoped to explore's own changes, by its observe events or by a snapshot at its start vs end (A16's form). X4 and X6 run over rows with `group: explore` of that stage occurrence. The debtor is the explore launch.
  - Scope by `group: explore` (unique per stage occurrence: one look per story at `product`, one per `reds`), not by a launch id. Or add the field to C3-1 and keep earlier launches' rows in scope.
  - Add test rows `{X6 reason without attempt -> explore's debt, never product's or reds'}` and `{relaunch inherits the first launch's rows}`.

M4 (blocking: no; fix before merge; edge "contradicts an accepted line without an amends line"). Where: A24 amends and Exit (r2 N3).
- What breaks: the new call `exit_check.py --launch explore --stage <s>` is a new CLI mode and a new scope on `exit_check.py`. Its CLI is C3-3's (part3: `exit_check.py --story --stage [--group] --when exit|after_critic`; C3-3 owns the file), and its output shape (`story, stage, group, when`) has no `launch` field. A24's amends and section 4's index (C3-3 <- A3, A4, A6-A9, A16, A23) do not name C3-3.
- A "launch row" in `stages.yaml` that is "not a stage" needs a row kind in frame 2b's stage fields. Otherwise `rows.py`, W1 ("each `reads` section is a `leaves` of an earlier route stage") and `run_stage.py` read it as a seventh stage. Frame 2b is not named.
- Fix: name C3-3 (CLI `--launch`, output field) and frame 2b (row field `kind: stage|launch`, W1 skips route checks for launch rows) in A24's amends and section 4.

M5 (blocking: no; fix before merge). Where: A3 "The question", r2 N6: "the changed lines are status fields computed by code from her own answer, so no critic round is owed".
- What breaks, (a): `test_report` carries role-written text ("author text 6144 bytes", brief "Look first", part3:97). A REQ written at `report` is the report performer's own row, so the brief may well cite it. Case: the brief says "new: discount cap at 50 %, proven by T-12". She answers `not_requirement`, so the REQ, its checks and T-12's result stale (rule 7). The rebuild from rows reproduces the brief unchanged beside a body that lists the REQ as "not a requirement". No critic or performer touches it, and A5's changes block lists rows, not the brief's words.
- What breaks, (b): frame 2c ORDER puts after_critic rules (D1, G6.1, and D4 per A6) on the built document before the stop. r2 sends the rebuilt one "BACK to the report stop" without re-running them. Staling T-12's result removes ids from "Proven", so the chat rows file now has extra ids: a D4 debt that nobody checks.
- What breaks, (c): the exception to ORDER's invariant is not named in an amends line.
- Fix: name the frame 2c exception in A3's amends ("a rebuild whose only changes are code-computed from the person's answer is not re-critiqued"). Re-run the after_critic rules on the rebuilt report, where a D4 or G6.1 debt goes to a report fix launch for those rows only. Author text that names a row the answer staled or confirmed goes to the same fix launch and a critic re-check of those rows (F60's "re-check of changed rows").

M6 (blocking: no). Where: A10 (3), r2 N4: "NOT open to a `knowledge.py set` called by a launch: only `run_stage.py`'s approval move writes it".
- What breaks: the text does not say how `knowledge.py` tells a launch from the approval move. A launch holds `exec`. If the test is the launch env (`FACTORY_KIND`), `FACTORY_KIND= python f/tools/knowledge.py set repositories --value src --source answer:Q7` passes.
- The test row "a row changed after the approve seq -> not written" also reads against the Delivers text, which copies the version live at the approve seq, so that version IS written.
- Fix: state that the `knowledge.py set` CLI refuses this road for every caller and that the approval move writes through a `run_stage.py` path that takes no value argument. Reword the test row to "the version live at the approve seq is written, the later revision is not".

M7 (blocking: no; fix before merge). Where: A4, r2 N2 invariant: "an approved proposed test always reaches `tests` as `person_word`".
- What breaks: the move finds proposed tests only through an expectation's `from`, and no gate checks that each proposed-test row in "Questions to the team" has an expectation `from` it.
- Case: the performer writes the question row and an expectation kind `none` without `from`. G3.1 is met (`none`), the person approves, and nothing is revised. The approved test never gets an autotest, which was N2's original failure, now silent.
- Fix: carry the invariant. Either the approval move lists each approved proposed-test row with no expectation `from` it in the report ("approved, no test written") and as a G4 shortfall, or this becomes a G3 critic criterion. State which.

M8 (blocking: no). Where: A1 MEASURES, r2 N7, against F70 (a) (part4-2:134: "measuring runs: 5 x the free arm's baseline time").
- What breaks: the free arm's baseline time includes its test runs, since the free agent has no `run_tests.py` exclusion. The factory's `story_wall_s` now excludes them, so the measuring-run cap compares two measures (pt. 6 (b): a comparison stays inside one metric). The error is toward a looser cap (it never cuts too early), and the comparison scoring itself is not touched.
- Fix: state F70 (a)'s measure (full wall minus `stop_wait` on both arms, or the free arm's test time subtracted where its transcript shows it), or name it as an edge.

M9 (blocking: no). Where: A6 Delivers, r2 N9: "a form built by code with no performer's rows file (A1's cut question, the launcher's `new_requirements` question of A3)".
- What breaks: D4 in the same card (part4.md:81) lists "the `new_requirements` question the launcher asks at this exit (A3)" among the texts the exiting performer's rows file covers. So that question has a rows file, and its `h:` and `o:` entries exist.
- Case: chat in Russian, a late REQ at `tests`. D4 forces the Russian entries, then by the r2 sentence the question goes out in English with `template_missing` and "asked in English". The two sentences prescribe different texts.
- Fix: drop `new_requirements` from the example. Name the forms truly without a rows file: A1's cut question (3rd rung `critical`) and any other launcher-built form.

## Standing questions (plan gate, rule 24; narrow to the r2 text)

- Q4 class: M1 is the pair class (the answer and the REQ on different carriers). Walked over every confirm road r2 opened or changed: `source` (M1), approval upgrade (M2, M7) and `sets_keys` (M6). M3 walked all six X rules for the new launch exit.
- Q6 duplication: none found beyond the reuse r2 names (`answered_ref` reading, A5 changes block, A2-style move). Grepped: `launch[_ ]id`, `--launch`, assumptions in the part3 test_plan row.
- Q12 one road: none found in the r2 text. A6's English fallback is a data folder per language (AR-1), not a language branch.
- VARIETY: a project with a long test suite benefits (N7). A Russian-chat project hits M9's contradiction. No r2 text blocks a stage on an unknown value. M3 can stall `plan` behind explore's debt.
- Q13 (c) premises re-run: part3:95 (the test_plan row has no assumptions section) reproduces, so M2 stands. Spec:164-169 (the X1-X6 definitions) reproduces, so M3 stands.

## Spot-checks

- `git log --oneline -1` -> `9e800eee8 spec: forge 2 light factory, part 4 fix round r2 ...`.
- `grep -o 'r2 N' part4*.md | wc -l` -> 22, which matches the brief's fact. Each mark was read in place.
- `grep -n -i -E 'launch[_ ]id' spec*.md` -> one hit (part4-2:124, the r2 line itself). The positive control is the same grep finding that line.
- `grep -n -E -- '--launch' spec*.md` -> part4-2:124 and 128 only. Nothing in part 3 (C3-3) has it.
- `grep -n -i assumption part3.md` -> the assumptions leaves of stage rows (38-41) and the understanding doc row (94). It does not appear in the test_plan row (95), whose full text was read by sed.
- part3:97 test_report row: "author text 6144 bytes; brief 2048 bytes" confirms the role-written text (M5).

## Trail

- Read: the diff part4_r2.diff whole (70 lines); t-1932 whole; part4.md 20-89; part4-2.md 1-135; part4-3.md whole; spec 100-140 (2a states, 2b, 2c ORDER at 131); part3 30-46, 72-80 (stage table, predicate list), 95, 97; part3b 46-50 (`per_test`, 48); spec 164-169 (X1-X6 by grep).
- Commands: the git log, grep counts and greps listed under Spot-checks; `sed -n 95p`, `97p` of part3.
- Not read: part 4b (non-goal); parts 2, 2b, 3 beyond the lines named; plan file. No finding depends on them.

```json
{
  "verdict": "blocker",
  "blockers": [
    "M1: A3 G6.4 late_confirmed source road (r2 N1) is not scoped to its carrier -- any performer-written REQ citing an unrelated accepting answer is counted confirmed and never asked; contradicts A3 error direction and the part4.md:54 invariant",
    "M2: A4 r2 N2 upgrades expectations resting on plan-stage assumptions to person_word on plan approval, but the test_plan shows no assumptions (part3:95) -- an autotest rests on what the person never saw",
    "M3: A24 r2 N3 explore exit judges only X1, X2 -- X3-X6 debts of explore's rows or writes fall on product (shortfall), reds or plan; launch-id scoping has no field and breaks the relaunch"
  ],
  "fixes": [
    "M4: A24 amends -- name C3-3 (exit_check --launch, output field) and frame 2b (row kind launch) in amends and section 4",
    "M5: A3 r2 N6 -- name the frame 2c exception; re-run after_critic (D1, D4, G6.1) on the rebuilt report; author text naming a changed row goes to a fix launch and critic re-check",
    "M6: A10 r2 N4 -- state the refusal holds for every caller of knowledge.py set and the approval move takes no value; reword the changed-row test",
    "M7: A4 r2 N2 -- carry the invariant: approved proposed-test row with no expectation from it is reported and owed",
    "M8: A1 r2 N7 vs F70 (a) -- state the measuring-run cap measure on both arms or name the edge",
    "M9: A6 r2 N9 -- new_requirements is covered by D4's rows file; drop it from the English-fallback example"
  ],
  "class_completeness": "F17 (3) and N1-N9 judged against the r2 text. Classes walked: every confirm road r2 opened or changed (REQ source answer M1, plan-approval upgrade M2/M7, sets_keys approval move M6); every implied X rule against the new explore exit (M3); every amends target the new explore exit mode touches (C3-3, frame 2b: M4); every after_critic rule and role-written section against the N6 rebuild (M5); every measure using story_wall_s (F70 a: M8); every form the N9 fallback names against D4 (M9).",
  "trail": {
    "read": [
      "scratchpad/part4_r2.diff (whole)",
      "docs/tasks/specs/reviews/t-1932-forge2-part4-rereview.md (whole)",
      "docs/tasks/specs/20261125-forge2-light-factory-spec-part4.md:20-89",
      "docs/tasks/specs/20261125-forge2-light-factory-spec-part4-2.md:1-135",
      "docs/tasks/specs/20261125-forge2-light-factory-spec-part4-3.md (whole)",
      "docs/tasks/specs/20261125-forge2-light-factory-spec.md:100-140,164-169",
      "docs/tasks/specs/20261125-forge2-light-factory-spec-part3.md:30-46,72-80,95,97",
      "docs/tasks/specs/20261125-forge2-light-factory-spec-part3b.md:46-50"
    ],
    "reruns": [
      {"command": "git log --oneline -1", "result": "9e800eee8 spec: forge 2 light factory, part 4 fix round r2"},
      {"command": "grep -o 'r2 N' part4*.md | wc -l", "result": "22"},
      {"command": "grep -n -i -E 'launch[_ ]id' spec*.md", "result": "one hit: part4-2:124 (the r2 line)"},
      {"command": "grep -n -E -- '--launch' spec*.md", "result": "part4-2:124, 128 only"},
      {"command": "grep -n -i assumption part3.md; sed -n 95p part3.md", "result": "assumptions in stage leaves and understanding row only; test_plan row has none"},
      {"command": "grep -n -E 'X[1-6] ' spec.md", "result": "164-169 X1-X6 definitions"}
    ]
  },
  "mutants": [],
  "mutants_none": "plan gate: spec documents only, no code diff and no tree named"
}
```
