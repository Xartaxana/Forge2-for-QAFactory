# t-1919 -- re-review: frame spec r1 (12a00c2c8) and plan v1.3 fixes (3b6da0190) against verdict t-1915

Critic, plan gate, repeat pass (rule 24). Spec of the work = the 22 fix lines and the F5 condition of t-1915. Parts 2
and 3 not judged. The decision to accept, and every fork, stay with the Lead / the owner (rule 6).

Summary: the round did what was asked on 16 of 23 items, and did it compactly. But three of the new contracts, when
read together, build gates that can never be met at their position (N1, N2, N4). Two of the three come from my own
fix lines, which were too thin: fix 5 named no due stage, and fix 3 named no completion operation. These are bounded
edits of 2a/2c/3 and need no new frame. They do have to land before any phase-3/4 card is cut.

## Fixes

- fix 1: partly -- 2c "Reasons" (7 rows incl. "code not written yet", "no tool for this surface", `other` never refused, routed up), §3 X6, plan 1а rule 6 "молчания нет" -- the acceptance of an `other` reason (accepted / returned) has no carrier row that X6's "provisional until accepted" can read (N7)
- fix 2: partly -- spec: 2a `probes` (critic only), §3 G4.2 without can-fail, G4.5 `after_critic`, 2c ORDER + invariant, F8; plan положение 5 -- plan gate table row 4 (plan:673, "Код сверяет" after stage 4) still demands "записью «умеет упасть»" at the performer's exit, contradicting положение 5 and G4.5; G4.5's debt has no door its debtor can use (N5)
- fix 3: partly -- 2b stage 1 leaves `requirements`; 2a requirement `text`, `source` (stage 1); §3 G1.4, D2 "at G1"; plan положение 1 and gate row 1 -- "stage 3 completes" has no record operation: rows are append-only and `revise` mints a new id, so completing REQ-n renumbers every requirement the person approved at G1.P (N2); with 2c scope, stage-3/6 rules fire at G1 (N1)
- fix 4: partly -- 2a "Stage states" table (12 states) + conductor seam in/out; re-approval in `at_stop` -- no state/move for `after_critic` rules unmet (a `refused` relaunch would re-enter `in_critic`, a second critic call against F8); the conductor's output row has no named next move; person "fixes" at a critic-less stage 1 go to `fix_round`, whose move is "critic re-checks" (N5)
- fix 5: wrong -- 2c "SCOPE BY SECTION" -- as written, a rule runs "at every exit from the first stage leaving" its `over`, and the debt is "owed by the row's stage". Since fix 3, `requirements` are left by stage 1, so G3.1, G3.2 and G6.2 run at G1 and refuse stage 1 for stage-3/4 work. A missing dependent (a check, a result for REQ-1) is owed by REQ-1's stage, which sends a shortfall to stage 1 at G3/G4. This also contradicts the stage row's own `exit` column (2b). The late-row escape that fix 5 aimed at is closed. The cause is my fix line's missing "due stage" (N1)
- fix 6: fixed -- 2a Row `state` live|stale, `supersedes`, "Derived, never stored", `revise`, OBLIGATION `<CHK-n>.<k>`, `critic_findings` apart from `findings`, §3 G6.3 "critic findings: report, not debt" -- none (its interaction with fix 3 is N2)
- fix 7: partly -- §3 X3 per group by `observe` agent, VCS-ignored out, no `observe` -> once at stage exit -- fixed as my line was written. The sibling is open, and my verdict missed it. At group A's exit, G4.1-G4.3 and G4.5 (and G6.2 under N1) run over every live row of their sections, including group B's unfinished checks and tests. Those rows have `stage` 4, which is the exiting stage, so group A is `refused` for B's work. The 2a Row has no `group` field to scope by (N1 fix (c))
- fix 8: fixed -- 2a question `holds`, reader `run_stage.py`; state `held` -- none
- fix 9: fixed -- 2a state `no_move` ("context over the host window"), conductor seam options "split a group, sections by pointer, ask", "never cuts a context"; 2b last line -- none
- fix 10: fixed -- 2a header `mode`, section `passes` (rule, rows, words, speaker, stop), record.py refuses passes and outward permission in comparison|night; 2c door "always also a `passes` row", `factory_findings` over `owner: data`, `score.py` counts; §1 P13 line; plan положение 7 -- the new pass door can be forged by the performer (N6)
- fix 11: fixed -- 2d question forms `critical`, `approve`, `bug_or_not`, `conductor`; `bug_or_not` body by `docs_build.py`, template `q-bug-or-not.md`, 40 lines / 5 bugs; "every text to the person via `ask.py`" -- none
- fix 12: fixed -- §3 D3 owner data, class xref, on unknown refuse, working-file request returned to the performer; G6.C "author wording (F13; advice: factory ids)"; plan "Правила выдачи" 3 reads "по идентификатору документа, а не по словам" -- none
- fix 13: fixed -- §1 AR-7/P1/FR-47 line: `obtained_by` for runs, manual evidence tool-recorded, else "executed by agent, no evidence: why"; P26 line agrees -- that outcome has no row in the 2c reason list, so G4.2 can close it only as `other` (N8, wording)
- fix 14: fixed -- §1 "AR-6, P5: every read route, never an LLM agent: sources land whole" matches architecture.md:122 -- none
- fix 15: fixed -- §4 C3-7 delivery targets, C3-8 expectation kinds, C4-8 `.md` export (`export_md.py` in 2a readers); 2g keys `repositories`, surface kind, who answers, how results are accepted; §5 row "everything to .md -> C3-7, C4-8, C3-5" -- none
- fix 16: fixed -- 2f `factory_tool_calls` (record.py apart), `stop_wait`, `docs_given`; record-derived shortfalls, unpaired rows, passes, provisional reasons; labels `refound`, `working_file_opened`; F30; §5 rows "1b measured by", "1v issue rule 4" -- none
- fix 17: fixed -- 2b "`rows.py` loads every `factory/data/*.yaml`: absent or unreadable -> launch refused naming the file and its card"; §6 row -- none
- fix 18: partly -- 2a batch `add` all or nothing; §4 C2-8 + order "C2-8 before phase 3"; §6 row; plan phase 2 row -- plan phase table row 3 "Чего ждёт: фазы 1" (plan:1087) and row 2 "Параллельна с 1, 3" (plan:1086) do not carry the C2-8 dependency the spec states (one line, Q3); part 2 has no C2-8 body (part-2 line, not a finding)
- fix 19: fixed -- §1 AR-15 line, §4 C1-5 owns `f/data/secret-patterns.yaml`, C4-5 "reads C1-5's table", C2-6 "`seeded.py` calls `arm.py`", C1-6 `forge/ci-jobs.json`, §8 -- none
- fix 20: fixed -- 2e OUTWARD by key `repositories`, unknown root asked once, that write waits; §1 "axis 8: narrows", F31 -- in comparison|night the launching model's answer about an unknown root turns an outward write into an inward one (N9)
- fix 21: fixed -- 2a "Field readers (AR-22)": `readiness` -> `run_stage.py`, `docs_build.py`; `executable_where` -> `run_tests.py`, `docs_build.py`; §3 W1 "typed-field reader"; §1 AR-22 line -- none
- fix 22: fixed -- §1 names AR-8, AR-9 (+P15), AR-11, AR-15, AR-16, AR-18, AR-20, P5 (with AR-6), P18 -- none
- F5 condition: fixed -- §7 F5 (a) "FROZEN before any craft page or seeded set is written and its bugs are never seeds"; §4 C0-3, C2-6 index rows; §6 row "ao3 truth table"; plan phase 0 row and раздел 3 п. 2 (extended to both projects) -- none

## New defects of the round

N1 (blocks phase-3/4 cards). The place is 2c "SCOPE BY SECTION" × 2b stage `exit` column × §3 G3.1, G3.2, G6.2, D2 × fix 3.
What breaks:
- (a) A rule runs from "the first stage leaving" its `over`. Stage 1 now leaves `requirements`, so G3.1 ("each requirement: expectation kind or `none`"), G3.2 ("a check or reason") and G6.2 ("result per obligation, or reason") all run at G1. Stage 1 can never exit without doing stage 3's and stage 4's work. Each relaunch hits the same debts, and after `refusal_relaunch_max` the stage goes to the conductor every story.
- (b) "The debt is owed by the row's stage". For an xref rule of the form "each X has a Y", the missing thing is a Y that a later stage owes. At G3, G3.2 over REQ-1 (written at stage 1) yields a shortfall that relaunches stage 1 to write checks. At a G4 group exit, G6.2 does the same for results.
- (c) Under parallel groups, rules over stage-4 sections refuse group A for group B's rows (fix 7 sibling). The Row has no `group` field.
- (d) D2 says "at G1", which contradicts the every-exit scope. A requirement added at stage 3 or 4 would then owe a placement in the understanding the person already approved.
- (e) 2b's per-stage `exit` rule ids and 2c's section scope are two answers to "which rules run here".

Fix (spec 2b, 2c, 2a, §3):
- A rule falls DUE at the stage whose `exit` column first names it (one source: 2b).
- From then on it runs at every exit over every live row of `over`.
- The debt goes to the stage that leaves the missing section or field: for shape rules on a row's own fields, the row's stage; for "each X has a Y", the stage leaving Y. Otherwise it goes to the exiting stage, never to an author of X.
- Rows carry `group` (written by `record.py` from the launch), and stage-4 rules scope to the exiting group's rows.
- D2 is stated as G1-only, and a later requirement is placed by G3.2 instead. The invariant is kept as stated: a met row stays met.

N2 (blocks C3-1). The place is 2a Row typed fields × `record.py` ops × fix 3.
What breaks: a requirement's `expectation_source` and `readiness` are stage-3 fields on a stage-1 row. Rows are only `add`ed, `revise`d (a new id that `supersedes` the old one) or `stale`d. So "stage 3 completes" can only mean revising every requirement. Each REQ-n becomes REQ-m:
- the ids the person approved at G1.P no longer match;
- D2 at G1 is satisfied by superseded rows;
- the old rows' `from` dependents go stale;
- AR-26 ("the requirement is the unit from stage 1 to delivery") loses its stable unit.
Fix (spec 2a): put stage-3 requirement attributes in their own rows keyed by the requirement id (e.g. a section `expectations`: `requirement`, kind or `none`, `readiness`), or name an operation that adds fields without a new id. Keep `revise` for a change of meaning only. G3.1 then reads the keyed rows.

N3: merged into N1 (d).

N4 (blocks C3-3/C4-1). The place is 2c ORDER × §3 G6.1, D1, G6.C.
What breaks: the ORDER is "`exit` rules -> critic -> fix rounds -> `after_critic` rules -> `docs_build.py` -> stop".
- G6.1 ("report built by `docs_build.py`") and D1 (document budgets) check a document that is built only after every rule slot. Whichever `when` they carry, they can never be met.
- G6.C reads a "report preview" that nothing in the ORDER builds before the critic.
- A D1 author-text overrun found after the build sends the text back for a rewrite the critic never sees, which breaks the stated invariant.
Fix (spec 2c, §3): ORDER = `exit` -> `docs_build.py` preview -> critic -> fix rounds (each rebuilds the preview, critic re-checks) -> `after_critic` rules incl. D1, G6.1 on the built document -> stop. A D1 failure after the critic is a fix round with a re-check, not a silent rewrite.

N5 (fix before C4-1/C4-2). The place is 2a stage-state table × §3 G4.5 × AR-9 ("the door is in the refused party's own permitted set", architecture.md:145).
What breaks:
- An unprobed autotest makes G4.5 a debt, owed under 2c by the test's stage (4) as `refused`. But the performer may not write `probes` ("critic only"), so the refusal has no door its receiver can use. Two relaunches later it lands at the conductor.
- More generally, the table has no move for `after_critic` rules unmet.
- The conductor's output rows name no next state.
- A person's "fixes" at stage 1 go to `fix_round`, whose move requires a critic.
Fix (spec 2a, §3):
- G4.5 unmet -> `critic.py` relaunched for the unprobed tests only, inside the F8 count. Else the test gets a "not proven" row to the report, as its on-unknown column already says.
- Other `after_critic` debts -> `refused` -> relaunch -> back to `after_critic` (the critic re-checks the changed rows as a fix round).
- A conductor row names the target state.
- `fix_round` on a critic-less stage returns to `at_stop`.

N6 (fix before C3-1). The place is 2a `passes` and `probes` rows × "ONE writer `record.py` ... Content is the performer's".
What breaks: a `passes` row "closes any debt" (2c). Nothing stops the performer from adding one with `speaker: person` and invented `words`, and nothing stops it from adding a `probes` row of its own. Either way a stage with unfinished work passes, which is exactly what the owner's central requirement forbids. The only bound stated is the mode refusal.
Fix (spec 2a, 2c):
- A `passes` row is written only by `ask.py` from a tool-written answer. Equivalently, `exit_check.py` accepts a pass only when its `stop` names a question row whose answer, written by the tool (F2), holds `words`.
- `probes` rows are accepted only from a `critic.py` launch (`by` set by the launcher, not by the agent).

N7 (fix before C3-3). The place is 2c Reasons `other` × §3 X6 × 2a.
What breaks: X6 reads "provisional until accepted", and 2f counts "provisional reasons". But no row records who accepted or returned an `other` reason (critic, person or conductor), so that field has no producer. `dashboard.py` cannot tell provisional from accepted, and "returned (-> shortfall)" has no trigger.
Fix (spec 2a): a reason-verdict carrier, e.g. a critic-finding state `accepted|returned` with `about` = the reason row, a stop answer citing it, or a conductor row. X6 and `dashboard.py` read it.

N8 (wording, before C4-4). The place is §1 AR-7 line × 2c Reasons × §3 G4.2.
What breaks: "executed by agent, no evidence: why" is promised as an outcome but is not a reason row. G4.2 closes it only as `other`, which is provisional and routed up, every time.
Fix (spec 2c): add it as a named reason, or state in §1 that it travels as `other`.

N9 (fix before C4-5). The place is 2e OUTWARD "An unknown root is asked once ... stored" × 2a `mode` × fix 10.
What breaks: in comparison|night the launching model answers that question. Once it declares a new root in `repositories`, writes there become inward, so the model grants outward permission by another road. A test repository outside the clone gets a trace (P8, FR-53).
Fix (spec 2e): in comparison|night, roots come only from knowledge present at launch. An unknown root means the write is refused and named in the report, and other work goes on.

Looked for and not found: no state with two contradicting moves; no `on_unknown` that passes on silence (X6 `other` is provisional by design and routed up); no doorless refusal in 2b/2d/2g; no field without a reader in 2a/2f beyond N7.

## Plan and frame agree

- Order at a critic gate: they agree in substance. Plan положение 5 has "сверка кода -> критик -> круги починки -> сборка документа -> остановка" plus "наличие [умеет упасть] код сверяет после критика", and r1 2c ORDER matches. Both orders share N4 (no document-check slot, no preview before the critic). Plan gate table row 4 (plan:673) disagrees with both and still checks "умеет упасть" at the performer's exit.
- Start of the requirement list: they agree. Plan положение 1 and gate row 1 ("перечень требований (у каждого — источник)") match r1 2b, G1.4 and D2. Plan gate row 3 reads as completion. The N1/N2 defects sit on the spec side only.
- Bounds of the launching model: they agree. Plan положение 7 ("только отвечает на вопросы остановок; пройти гейт словом человека и разрешить запись наружу она не может") matches r1 2a `mode` refusal, §1 P13 and §3 G1.P. Shared gap: N9.
- Reason-list exit: they agree. Plan 1а rule 6 (two new rows; own words + attempt; "не отклоняет, а передаёт ... критику ближайшего гейта, иначе человеку на ближайшей остановке, иначе дирижёру"; in the report by name) matches r1 2c Reasons. Shared gap: N7.
- Spike timing (fix 18): the plan's phase rows 2 and 3 do not carry r1's "C2-8 before phase 3".

## Verdict on the round

The Lead can cut cards for phases 0-2 now, together with part 2: none of N1-N9 touches them. Part 2 needs a C2-8 body and the C0-5/C1-1/C1-5/C1-6 owns widening the index already states. Cards for phases 3-4 need one more bounded fix round of frame sections 2a, 2c, 2e and §3 (N1, N2, N4, N5, N6, N7) and two plan rows. No new frame and no third full review are needed. A targeted check of those items is enough.

verdict: fit_with_fixes

fixes:
1. spec 2b/2c "SCOPE BY SECTION" + §3 D2 -- due stage from the `exit` column; debtor = the stage leaving the missing part; Row `group`, stage-4 rules per group; D2 G1-only (N1). Blocks phase-3/4 cards.
2. spec 2a Row typed fields / `record.py` ops -- stage-3 requirement attributes keyed by requirement id, no renumbering (N2). Blocks C3-1.
3. spec 2c ORDER + §3 G6.1, D1, G6.C -- preview before the critic, document rules after the build, re-check after any rewrite (N4). Blocks C3-3/C4-1.
4. spec 2a stage-state table + §3 G4.5 -- moves for unmet `after_critic` rules, unprobed tests to the critic, conductor output to a state, critic-less fix round (N5).
5. spec 2a/2c `passes`, `probes` -- writer bound to `ask.py` / a `critic.py` launch (N6).
6. spec 2a/2c Reasons, §3 X6 -- carrier of `other` accepted/returned (N7).
7. spec 2c Reasons or §1 AR-7 line -- "executed by agent, no evidence" as a row or stated `other` (N8).
8. spec 2e OUTWARD -- no new roots in comparison|night (N9).
9. plan раздел 1а, gate table row 4 (plan:673) -- "умеет упасть" checked after the critic (fix 2).
10. plan, phase table rows 2-3 (plan:1086-1087) -- phase 3 waits for C2-8 (fix 18).

## Invariants (R6)

- AR-1 kept (reasons, forms, targets, kinds as rows). AR-2 kept by fix 1, broken by N1(a): a stage-1 refusal it cannot close. AR-9 broken by N5: the G4.5 door is outside the refused party's set. AR-10 kept (after-approval derived). AR-14 kept in form; N6 needs per-section writer bounds. AR-15 kept (fix 19). AR-16 kept (fix 11). AR-22 kept (fix 21; N7 has no producer). AR-25 partly (N5). AR-26 broken by N2 (unstable id). AR-28 kept (fix 17). AR-29 kept (`other` routed up, never refused).
- P8 / FR-53 kept except N9. P13 / FR-4 kept (fix 10), but forgeable (N6). P20 / FR-58 kept, conditional on N1 (late requirements reach G3.1 through the right debtor). P26 kept; join N8. P31 kept.
- FR-12 kept (D3 by id). FR-59 kept.

## Trail

Read:
- t-1915 whole (1-344).
- spec r1 whole (1-381).
- r0 lines 60-200 (`git show 8cc6b5192:...spec.md | sed -n 60,200p`), to compare 2a-2g, §3 and the r0 card bodies.
- plan diff `git diff 8cc6b5192 3b6da0190 -- plan` whole; plan 566-572, 873-887, 1086-1087 (sed); plan grep "умеет упасть" -> lines 233, 265, 494, 570, 576, 581, 673, 939, 951, 1009.
- architecture.md 122-124 (AR-6), 145-147 (AR-9), 302-305 (AR-26); grep of AR-6/8/9/11/15/16/18/20/22/26/29 headings -> 11 hits.
- part 2: grep of card headings (19 headings, C0-1..C2-7) and `C2-8` -> 0 (control: the same file's heading grep found C2-7); grep of secret|ci-jobs|arm.py -> lines 46, 51, 102, 107, 191, 206, 220.

Plan at HEAD = plan at 3b6da0190: `git diff --stat 3b6da0190 12a00c2c8 -- plan` printed nothing. The positive control is the same command over 8cc6b5192..12a00c2c8, which printed `plan.md | 64 +-`.

Not read: factory-rules.md (no fix leaned on an FR text beyond what t-1915 quoted); OWNER_PRINCIPLES.md (P-numbers taken from r1 §1 and t-1915 V3); plan outside the diff and the places above; part 3 (does not exist yet).

Negatives backed:
- "no `group` field on a Row": spec:105 Row field list read directly.
- "no reason-verdict carrier": spec:104-108 section and row lists read whole; `accepted` appears only in 2c:147 prose.
- "no update op in record.py": spec:112 op list read directly.

No probe: documents only.

```json
{
  "verdict": "fit_with_fixes",
  "blockers": [],
  "fixes": [
    "N1: spec 2b/2c scope by section and section 3 D2 -- rules fire from the first stage leaving their sections (G3.1, G3.2, G6.2 at G1); debt owed by the row's stage misroutes missing dependents; no group scope; due stage from the exit column, debtor = stage leaving the missing part, Row group, D2 G1-only. Blocks phase-3/4 cards",
    "N2: spec 2a requirement typed fields and record.py ops -- stage 3 completing stage-1 requirements only by revise renumbers approved ids (AR-26); key stage-3 attributes by requirement id. Blocks C3-1",
    "N3: merged into N1 (D2 at G1 versus section scope)",
    "N4: spec 2c ORDER and section 3 G6.1, D1, G6.C -- document rules and the critic preview have no slot; preview before critic, document rules after build, re-check after rewrite. Blocks C3-3/C4-1",
    "N5: spec 2a state table and section 3 G4.5 -- G4.5 debt owed to a performer who may not write probes (AR-9); no move for unmet after_critic rules; conductor output names no state; critic-less fix round",
    "N6: spec 2a/2c passes and probes -- forgeable by the performer through record.py; bind writers to ask.py and a critic.py launch",
    "N7: spec 2a/2c other reason -- no carrier for accepted/returned; X6 and dashboard cannot read it",
    "N8: spec 2c reasons or section 1 AR-7 line -- executed by agent, no evidence is not a reason row",
    "N9: spec 2e outward -- launching model can add repository roots in comparison/night mode",
    "plan 1a gate table row 4 (line 673) -- can-fail record still checked at the performer's exit (fix 2)",
    "plan phase table rows 2-3 (lines 1086-1087) -- phase 3 does not wait for C2-8 (fix 18)"
  ],
  "class_completeness": "Re-review of 22 fixes and F5. Siblings walked per fix: fix 5 scope over every section-3 rule whose over includes requirements, checks, evidence (N1); fix 7 parallel groups over all stage-4 rules, not only X3 (fix 7 partly, a sibling my t-1915 missed); fix 2 order over G3, G4, G6 and the document rules (N4); fix 10 pass door over every writer-restricted section, passes and probes (N6); fix 20 outward over the comparison/night bound (N9).",
  "trail": {
    "read": [
      "docs/tasks/specs/reviews/t-1915-forge2-plan-critic.md (whole)",
      "docs/tasks/specs/20261125-forge2-light-factory-spec.md r1 (whole, 381 lines)",
      "spec r0 at 8cc6b5192 lines 60-200",
      "plan diff 8cc6b5192..3b6da0190 (whole); plan 566-572, 873-887, 1086-1087",
      "ai-packages/qa-factory/design/architecture.md 122-124, 145-147, 302-305 and AR heading grep",
      "docs/tasks/specs/20261125-forge2-light-factory-spec-part2.md card headings and C2-8 grep"
    ],
    "reruns": [
      {"command": "git -C C:/QAFactory/forge-repo diff --stat 3b6da0190 12a00c2c8 -- plan", "result": "empty: plan at HEAD equals 3b6da0190 (control over 8cc6b5192..12a00c2c8: plan 64 lines changed)"},
      {"command": "grep -n 'umeet upast' (Cyrillic) over the plan", "result": "lines 233, 265, 494, 570, 576, 581, 673, 939, 951, 1009; row 4 at 673 unchanged"},
      {"command": "grep -n card headings and -c C2-8 over spec part 2", "result": "19 headings C0-1..C2-7; C2-8 count 0"}
    ]
  },
  "mutants": [],
  "mutants_none": "plan gate re-review: documents only, no code and no tree under review"
}
```
