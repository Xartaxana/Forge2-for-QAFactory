verdict: blocker

# t-1932 -- critic re-review of fix round r1, spec part 4 (light factory), at 92f0e81c8

Scope: the 20 findings of t-1927, each judged against the plan block v1.10 (plan:1628-1702) and the owner's records (plan:2188-2309); new defects only where r1 introduced them. Part 4 read whole in its three files. Cards A11, A13, A15, A17, A18, A20 were not re-reviewed (byte-identical). Plan gate (rule 24). Nothing in v1.10 decides a finding differently from t-1927's fix line in a way that changes the judgment. F3 and F10 take the v1.10 road (exclusion from the wall; first-message language) and are judged on that road.

## Findings of t-1927

- F1: closed -- A3 (G6.4), A7 (G4.6), A8 (G3.5) and A16 (G5.4) each state due stage, `when`, predicate, debtor and page. So do D4 (A6) and the changed G4.1 (A23) and G3.1 (A4). The C3-2 exit column and the C3-3 predicate list are in section 4. How checked is generated from due rows (A21). The gate count is 45, at F9's budget (frame:338). But see N5: the implied X rules drop out of the generation.
- F2: closed -- A1 MEASURES: `tokens` is the latest call's context size (input + cache-write + cache-read), never a sum. K7 covers it. This is the same measure as B5 (part4b:105).
- F3: closed -- A1 `wall_s` excludes `run_tests.py` child intervals, each capped at its timeout (crash edge). A14 says the move is reachable. K6 and the A14 K-new check it. This is the v1.10 road.
- F4: closed -- A1 `story_wall_s` excludes `stop_wait` intervals, with an edge and K8. See N7 for a side effect of counting test runs in it.
- F5: closed -- (a) A2: `runner-forms.yaml` `test_files` globs per product root open only test-form paths. Inline tests go to a separate file, or one question is asked (cost named). (b) A2 "F71 (a) carrier": test-plan section "Where tests go", rows `about: plan:where_tests`, written to knowledge on approval with `answer:<approve qid>`. See N4 for the value check.
- F6: closed -- A3: the launcher asks one non-blocking `new_requirements` question at the finding stage's exit. G6.4 is `when: exit` at `report`, debtor `report`, and reads the option id. `decide_later`, open and silence give `unconfirmed`, never counted proven. No deadlock against the report stop remains. See N1 and N6 for the defects this introduced.
- F7: closed -- A4 "Guard at exit, not mid-stage": the r0 K1 refusal is withdrawn. An unanswered ground is a G3.1 debt at exit through `answered_ref`. See N2 for a timing defect in that guard.
- F8: closed -- A24 adds the C4-1 move after `product`, context, caps row, tools, env and the "cut ends it, no ladder" edge, as v1.10 F8 decides. The F90 (a) line adds the stage-5 road. See N3: its exit has no working carrier.
- F9: closed -- A12 grants `write_work` (under `work_root`) to every launch. A5 `--rows <file|->` takes stdin.
- F10: closed -- A5 "Chat language": the language is set at `start --chat-language`, else the first message's language (journaled `first_message`). `start` without it is refused. The repository language is never the default.
- F11: closed -- A6 sends every chat text through `docs_build.py --chat --lang` / `ask.py ask --lang` with the rows file, checked by D4. C4-3 and C3-5 are named in amends and in section 4. See N9 for the fallback of code-built forms.
- F12: closed -- A10 (3): person-only keys take only `answer:<qid>`. The check is a tool-written `ask.py` answer, speaker `person`, about `knowledge:<key>`. The refusal names its door. `context.py` lists the keys. See N4 for the second road (`sets_keys`).
- F13: closed -- A8: content-derived hunk ids (path + removed + added lines) and file ids `F-`. K3 (stable across a rebase) and K4 (one file id for a 3000-hunk lockfile) check them.
- F14: closed -- A9: each `run_tests.py` run measures the build identity (30 s limit) or records `unmeasured`, never copied from a probe. K3 covers a redeploy.
- F15: closed -- A12/A1 `launches.yaml`: tools per kind x stage for performer (all six stages), fix_round, critic (write only at `tests`), conductor and explore. W1 requires `tools` on each pair.
- F16: closed -- A16: the base is the red run's `tests_snapshot`, scoped to the red's own test files and reds-launch changes. `covers` gives one entry for a shared file. `to_approved` names any live expectation. Tests-stage shortfall changes are not G5.4's (K4, K5, K6).
- F17: not closed -- (1) and (2) are closed in A5: "Agent's assumptions" with reason and kind, approve all or strike, and an approved assumption grounds `person_word` with the approve qid. (3) is not closed: both roads for a proposed test lose the person's "yes". Before approval (A4: a "Questions to the team" row answered at G3.P), the expectation cannot name the question at `plan` exit, because the stop comes after the exit rules (2c ORDER). The door is kind `none`, and nothing upgrades it after approval, so an approved proposed test never gets an autotest (N2). After approval (`proposed_tests` `write` -> requirement), G6.4 reads only a `new_requirements` option, so the REQ is reported `unconfirmed`, or the person is asked a second time (N1). Fix: N1 and N2.
- F18: closed -- A19 names the one AR-16 exception, and `start --preflight-words` writes the `questions` row (`obtained_by: start_page`). The "words lost" edge says `answer: not kept`.
- F19: closed -- A22 "Shared runs": a substitution in a shared helper, fixture or mock gets its own run. A kill counts only when the probe's own function fails at its own check. Collection, import or setup errors make every probe of the run invalid. Inversion gets `method: inversion` and is reported apart. The C4-2 edge is reworded. See N8 for the error direction.
- F20: closed -- A23 edge and A16: `later_row` stays in the closed list (used by G5.2) and supplies the order for `new_expectation` inside `test_changes_entered`. Section 4 says "`later_row` kept".

## New findings

N1 (blocking: yes). Where: A3 (part4.md, gate row G6.4 and "The question") against A4 (part4.md, "Each look" and "NOT ONLY WHAT FAILED").
- What breaks: A4 says an accepting answer (`should_be_so`, `write`) creates a requirement whose source is that answer, and "that answer confirms it". After approval, that REQ is a late REQ (`seq > approved_plan_seq`). G6.4's `late_confirmed` counts only an option on a `new_requirements` question naming the REQ.
- Two outcomes, depending on how "with no question yet" (A3) is read:
  - (a) The `beyond` answer counts as the question. Then G6.4 finds no `new_requirements` question, so the result is "met, `unconfirmed`". A REQ the person confirmed ("yes, it should be so") is never counted proven.
  - (b) It does not count. Then the person is asked a second time ("is it a requirement?") about what she just confirmed. That is an extra round the yardstick forbids.
- The same holds for a `proposed_tests` `write`.
- Fix: `late_confirmed` counts the REQ's `source` question when its latest tool-written answer carries an accepting option (reuse `answered_ref`). The launcher skips a late REQ whose source is such an answer. Add a G6.4 test row `{source = should_be_so answer}`.

N2 (blocking: yes). Where: A4 (part4.md, gate row G3.1 `answered_ref`) and the "before approval" road in "NOT ONLY WHAT FAILED". The same holds for any `plan`-stage assumption grounded on the plan's own `approve`.
- What breaks: G3.1 is `when: exit` at `plan`. The plan's own `approve` answer exists only after exit rules -> critic -> after_critic -> stop (frame 2c ORDER, spec:131). So an expectation naming the plan's approve question is always a debt at plan exit, and the door forces kind `none`.
- After G3.P approves the "Questions to the team" row, no move upgrades `none` to `person_word`. Expectations are plan's leave (part3:40), and G3.1 is met by `none`. So the approved test is silently never written. A4's "`partial` striking it -> no test" implies the opposite for an approval.
- Fix: on `approved` at the plan stop, `run_stage.py` revises each expectation tied to an approved "Questions to the team" row or plan-stage assumption to `person_word` naming the approve qid. This is one move, like A2's knowledge write. Alternatively, `answered_ref` on the stage's own stop question yields `provisional` until the stop instead of a debt. State the edge and add a K row.

N3 (blocking: yes). Where: A24 (part4.md), Exit and the F90 (a) line.
- What breaks, part 1: "`exit_check --stage product --group explore` ... X1 over its leave `findings`" has no carrier.
  - A24 declares C3-2 unchanged ("none"). In C3-2, `product` is not grouped and `findings` is optional there (part3:39).
  - Group-scoped rule evaluation exists only for stage 4 (frame 2c: "Stage-4 rules see the exiting group's rows").
  - Stage states are per stage (frame 2a), and `product` is already `exited`, so "debts -> `refused` -> relaunch" has no state to hold it.
  - Run as written, the call re-judges `product`'s own exit column (G2.1, G2.2) and required leaves. An explore that writes nothing then passes.
- What breaks, part 2: at `reds` the same call runs before the reds exit rules. It evaluates G5.1-G5.4 over the reds performer's rows. Explore (`write_work` only) is then refused and relaunched for debts that belong to `reds` (up to `refusal_relaunch_max`, then the conductor). This contradicts A16's own invariant: a stage never owes for another launch.
- Fix:
  - Give the explore launch its own row: a C3-2 launch row with leaves `findings` required (row or `empty: nothing_beyond`) and exit X1/X2 over rows with `group: explore`. Or use a named predicate scoped to the launch's rows.
  - State its state record: per-launch state in 2a, or `exits` rows only, with no stage state change.
  - Name C3-2 and frame 2a in amends.

N4 (blocking: yes; safety, rule 15 pair). Where: A10 (part4-2.md, Enforced (3)) with A2 ("F71 (a) carrier").
- What breaks: on the `sets_keys` road, `knowledge.py set repositories|mock_base --value <row> --source answer:<approve qid>` checks only the answer side: tool-written, speaker `person`, the document's `sets_keys` holds the key, option `approved`. It does not check that the VALUE is a live `plan:where_tests` row of the version the person approved.
- Concrete case: a performer with `exec` runs `knowledge.py set repositories --value <product root as tests root> --source answer:<the real approve qid>`. The call passes, and A2's invariant ("product code stays closed unless a data row opens a named file pattern") falls. The A10 residual "value vs words" does not cover it, because the words are just "approved".
- Fix: on this road `--value` must name a `findings` row `about: plan:where_tests` that was live at the approve question's `seq`, and its value is copied from that row. Add a test row `{approve qid with a value not in the approved plan} -> refused`. Alternatively, reserve the road to `run_stage.py`'s approval move.

N5 (blocking: yes; owner ~20:56). Where: A21 (part4-2.md, How checked) against C3-2 (part3:34 "X1-X6 implied on every row, not listed").
- What breaks: A21 generates `## How checked` from "every gate row due at (the exit or after_critic column of) any stage". The X rules are never in that column. So X1-X6, which are asked at every exit (including X5's new meaning, A2), appear on no page.
- A2's "told at entry ... every page's How checked (A21)" is then false for X5. X1-X4 and X6 have no other teller. Under the old part2b:6 they could be authored; A21 replaces that.
- Fix: A21's generation adds the implied X rows to every page, and W1 reads them as due at every stage.

N6 (blocking: no; fix before merge). Where: A3 (part4.md, "The question", last sentence).
- What breaks: a REQ written at `report` is asked in the report stop's message, and "an answer that changes a status rebuilds the report once before `exited`". The person approves the report and changes a status in the same message, so the delivered report is not the one she approved and nobody re-shows it.
- This contradicts frame 2c ORDER ("never a silent rewrite"; "the person never sees a document the critic has not seen"), and no amends line names it.
- Fix: the rebuilt report goes back to the stop with A5's code-computed changes block. Or the `new_requirements` question for report-stage REQs is answered before the report stop is asked.

N7 (blocking: no; fix before merge). Where: A1 (part4.md, MEASURES `story_wall_s`) with F70 (a).
- What breaks: the stage wall now excludes test runs, but the story wall counts them. F70's temporary 2 h is still derived as "6 x the stage wall cap", a ratio that no longer measures the same thing.
- Concrete case: a project with a 25-minute suite. Runs at `tests`, the G4.5 probe runs, the G5.2 rerun and one diagnostic already take about 100 minutes. The story is cut, and the 3rd rung puts a question to the person on every such story.
- Fix: derive the row as stage caps plus k x `test_timeout_s` (`rows.py` invariant `story_wall_s` > n x `test_timeout_s`), or state the case as a named edge with its cost.

N8 (blocking: no). Where: A22 (part4-2.md, Shared runs).
- What breaks: "failing at its own check" needs a failure location. C4-4 `per_test` (part3b:48) promises only a per-test outcome.
- Fix: state the error direction. Where the location cannot be read from the output, the probe of a shared run is invalid and is rerun alone.

N9 (blocking: no). Where: A6 (part4.md, Delivers) with A1 (3rd rung `critical`) and A3 (`new_requirements` options).
- What breaks: some forms are built by code, outside any performer's rows file and outside D4 (D4 runs only at after_critic). A1's cut question is one: it can come mid-stage. For these forms, with no `templates/<chat_language>/`, the fallback "the rows file's `h:` entries" does not exist. The language they go out in is unstated.
- Fix: state the edge, e.g. the English template plus a journal `unknown: no template for <lang>`, named in the report. Never silent.

## Seam with part 4b (read only)

A1 MEASURES vs B5 (part4b:105) give the same measure: context size = input + cache write/creation + cache read of the latest call / last usage line. The event names `cap_warning` and `cut` are the same in A1 (amends 2f), B2's closed list (part4b:63) and B5. The seam holds.

## Spot-checks

- Gate budget: `sed -n 338p spec` gives "gate rules 45 (section 3: 40)". The five new rows (G3.5, G4.6, G5.4, G6.4, D4) make 45, at budget. No other new gate row was found in A1-A24 (`exits`, `cut` and W1 additions are not gate rows).
- `per_test`: grep over the spec files finds it only at part3b:48 (as a runner-forms field) and part4-2:98. The positive control is the same grep finding part4-2.
- `later_row`: present in part3:74 (closed list).
- Stage and craft table, part3:36-43: `findings` is optional at `product`, `grouped: no` for `product` and `reds`; `report`'s craft set is `report`; `reds` holds `red-analysis`; `plan` holds `check-selection`; `tests` holds `test-code` and `automate`.
- Frame 2a stage states, spec:102-118: per stage, no group-level state.

## Trail

- Read: part4.md 1-101, part4-2.md 1-151, part4-3.md 1-32 (whole); t-1927 verdict whole; plan 1620-1709 (v1.10) and 2188-2309 (owner records 20:50 to 21:47); frame spec 100-140, 155-212, 338; part3 34-46, 74-80; part3b 48-56; part4b grep for the cap and event names (lines 63, 103-110 and part4b-2:73, 125).
- Commands: `git log --oneline -1` -> 92f0e81c8; `sed -n 338p spec`; `grep -n -E 'later_row|lower_seq|xref_both_ways|world_unreferenced|per_test|approved_plan_seq|stop_wait|outward_permitted|result_per_obligation|craft'` over frame, part2b, part3, part3b; `grep -n -i -E 'per.test|per test'` over spec*.md; `grep -n -i -E 'cap_warn|cap_stop|\bcut\b|context size|cache'` over part4b*.md.
- Not read: `architecture.md`, `factory-rules.md`, `OWNER_PRINCIPLES.md` (no finding depends on them); parts 2-3b beyond the ranges above.

```json
{
  "verdict": "blocker",
  "blockers": [
    "F17: proposed-test road (3) loses the person's yes both before approval (N2) and after (N1)",
    "N1: G6.4 late_confirmed reads only a new_requirements option, while A4 says a beyond/proposed_tests accepting answer confirms the REQ -- confirmed REQ reported unconfirmed or asked twice",
    "N2: G3.1 answered_ref at plan exit cannot see the plan's own approve answer (stop comes after exit rules); approved Questions-to-the-team tests stay kind none forever",
    "N3: A24 explore exit via exit_check --stage product|reds --group explore has no carrier (ungrouped stages, per-stage states, C3-2 declared unchanged); at reds it charges explore with reds debts",
    "N4: A10 sets_keys road does not scope --value to the approved plan's where_tests rows; a performer can open a product root citing the real approve qid",
    "N5: A21 How checked generation reads only the exit/after_critic column, so implied X1-X6 (incl. X5's new meaning) are told on no page"
  ],
  "fixes": [
    "N6: A3 report rebuilt after approval when a report-stage late REQ status changes -- re-show with changes block or ask before the stop",
    "N7: A1 story_wall_s counts test runs while F70's 2 h is still 6x a stage cap that now excludes them -- derive with test_timeout_s or name the edge",
    "N8: A22 shared-run own-check attribution needs a failure location per_test does not promise -- state invalid as the direction",
    "N9: A6 code-built forms (A1 cut critical, new_requirements) with no template for chat_language -- state the fallback and journal it"
  ],
  "class_completeness": "All 20 t-1927 findings judged against v1.10. Classes walked: every new or changed gate row for due stage, when, predicate, debtor, page (G3.5, G4.6, G5.4, G6.4, D4, G3.1, G4.1, G6.2, X5) -- X rules found untold (N5); every road by which a person's answer confirms a row (approve, beyond, proposed_tests, new_requirements, critical about knowledge) -- N1, N2, N4; every new launch kind for caps, tools, move, exit (explore at product and reds) -- N3; every cap measure for consistency with stage and story (N7) and with B5 (seam holds).",
  "trail": {
    "read": [
      "docs/tasks/specs/20261125-forge2-light-factory-spec-part4.md:1-101",
      "docs/tasks/specs/20261125-forge2-light-factory-spec-part4-2.md:1-151",
      "docs/tasks/specs/20261125-forge2-light-factory-spec-part4-3.md:1-32",
      "docs/tasks/specs/reviews/t-1927-forge2-part4-critic.md",
      "docs/tasks/specs/20261125-forge2-light-factory-plan.md:1620-1709,2188-2309",
      "docs/tasks/specs/20261125-forge2-light-factory-spec.md:100-140,155-212,338",
      "docs/tasks/specs/20261125-forge2-light-factory-spec-part3.md:34-46,74-80",
      "docs/tasks/specs/20261125-forge2-light-factory-spec-part3b.md:48-56",
      "docs/tasks/specs/20261125-forge2-light-factory-spec-part4b.md:63,103-110 (grep)"
    ],
    "reruns": [
      {"command": "git log --oneline -1", "result": "92f0e81c8 plan: forge 2 and the light factory, v1.11"},
      {"command": "sed -n 338p spec.md", "result": "F9 (budgets): ... gate rules 45 (section 3: 40)"},
      {"command": "grep -n -i -E 'per.test|per test' spec*.md", "result": "part3b:48 runner-forms per_test; part4-2:98"},
      {"command": "grep -n -i -E 'cap_warn|cap_stop|cut|context size|cache' part4b*.md", "result": "B2 list and B5 use cap_warning, cut; B5 tokens = input + cache creation + cache read of last usage line"}
    ]
  },
  "mutants": [],
  "mutants_none": "plan gate: spec documents only, no code diff and no tree named"
}
```
