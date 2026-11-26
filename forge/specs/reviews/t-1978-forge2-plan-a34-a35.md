# t-1978 -- critic, plan gate: forge 2 spec part 10, cards A34, A35 (topic 2)

Reviewed state: forge 2 `f8337da` (git -C C:/QAFactory/forge2-repo log --oneline -1). Part 10 is 53832 bytes (wc -c), which matches the Lead's fact. Frame: section 1 of part 10 and the owner's yardstick from the dispatch. I take the Lead's fork decisions (plan record 26.11.2026 ~02:59: F212 (a), F213 (a), F214 "decided myself") as given. Sources: the role files at b2f70ac5e (`git show b2f70ac5e:ai-packages/qa-factory/agents/<file>`).

- A34: blocker -- F1, F2 block; F3-F6 fixes
- A35: fit_with_fixes -- F7-F14

Verdict line (rule 6): REJECT for A34 (failure_class: spec), NEEDS WORK for A35. That is 2 blocking findings and 12 fixes. Accepting the cards, or sending them back, is the Lead's decision.

Owner's yardstick, per card:
- A34: The yardstick asks whether the craft is told at entry. It is: one common entry, with no score and no roll-call. But F214 lets a test that went red for the wrong reason reach the report green and never probed (F1). The old critics produced three things that are not findings (the strictness note, the answer to each criterion, the list of what was not looked at), and these now have no home, or a home that opens rounds and shortfalls (F2). Nothing useful is dropped silently, except the probe-log craft (F3) and the round-sparing purpose of the cause list (F4).
- A35: The yardstick asks whether the bug, report and frame craft is carried, and it is: severity is optional (F213), the agent tool is denied, and personal data is masked. Gaps: the damage to a person has no carrier (F9); the "one cut" points at a card that cannot hold it (F7); one row's meaning was swapped for another's (F12); two details were dropped without a reason (F13).

## Findings

**F1 (A34 L10 + F214, blocker) -- a test red for the wrong reason skips its probe and comes back green, never probed.**
- Place: L10 "criterion: spend no probe where the run already shows red". The decision at 02:59 says such a test "owes no G4.5 probe -- its red already proves it can fail; it goes to `reds`".
- Source: the old waiver was not about the colour of the run. PA-216 (code-critic line 68): "A red test with its `contradicts_requirement` row takes no probe". The critic gave that row only after judging the failure (line 95): "a test that asserts its Then and fails against the implementation is accepted red with its `contradicts_requirement` row". The same file (line 48) says that "a timeout, a network error or a throw inside the check's own arguments shows it did not [fire]". A22 itself counts "a collection, import or setup error, a failure outside the substituted check" as proving nothing. So "a red proves it can fail" contradicts A22 and the source. L10 changes the row's meaning: a judged red becomes any red.
- Case:
  1. The G4 test for REQ-2 fails on a wrong locator: element not found, before its assert.
  2. Its run is red, so at G4.5 it owes no probe.
  3. `reds` classes it `test_error` and repairs the locator (A16 `to_approved`). G5.2 gets a later green run.
  4. `reds` has no critic. The G6 critic launch has no `write` (A12), so it cannot probe.
  5. G4.5 stands in no exit column after `tests` (C3-2 table; N1 carries only exit columns), so nothing asks for the probe again.
  6. The report shows a green test that was never shown able to fail on the bug, and it is not under Not proven.
- Smallest fix, in the F214 reading written into C4-2:
  1. The waiver holds only for a red whose failure is at the test's own check (the critic reads the failure line, as code-critic line 48 says). A red at collection, import, setup, a locator or a timeout is not "red against its requirement", so the probe stays owed.
  2. A waived test whose red `reds` classes as anything other than `product_bug`, and which ends green, is listed under Not proven as "repaired after red, never probed" (C3-5). It is never listed under Proven.
  3. Add a test row to `test_critic.py`/`test_docs_build.py`: waived red -> `test_error` -> green -> Not proven.

**F2 (A34 L3, L8, C4-2 amendment, blocker) -- what a critic says that is not a defect has no home, and the only home it has opens fix rounds and shortfalls.**
- Place: L8 "a Then asking more than the requirement is a note with no cause (a strictness note)"; L3 "name what you did not look at and why", "PA-98: answer each How checked criterion, weighed or rejected in one line"; amends "C4-2 Delivers (the critic answers each criterion of How checked)".
- Why there is no home: the critic writes only `critic_findings`, `probes` and `reason_verdicts` (C4-2 Delivers). A critic finding is `open|fixed|to_report` (frame 2a, line 95). `in_critic`: "findings -> `fix_round`" (frame line 111). C4-2 edge: "finding about a row of an exited stage -> shortfall to that stage".
- Source: the old note went "only in your findings file, never in the form's `findings[]`" (code-critic line 80): no cause, no round.
- Case: the G4 critic sees that the Then of CHK-3.1 asks more than REQ-2 and writes the note as a `critic_findings` row `about: CHK-3.1`. That opens a fix round at `tests`, plus a shortfall to `plan`, which has already exited. The per-criterion answers, written the same way, would open a round at every gate.
- Smallest fix (no new field): C4-2 lets the critic write a `critic_findings` row whose state is `to_report` at write time. That row is a note: it opens no fix round and makes no shortfall, and the report prints it under Not critiqued. L3 and L8 name this row as the home of the strictness note, the not-looked list and the per-criterion answers. If they are meant to stay craft with no output, L3 says so instead and turns PA-98 and PA-99 into D with that reason. Either way, add a `test_critic.py` row: a `to_report` note -> no round, no shortfall.

**F3 (A34 L7, L9, fix) -- the probe-log craft is folded into A22, which does not hold it, and two lines claim one row.** L9 sends PA-205 ("a timeout or throw in the check's own arguments shows it did not [fire]; an unplaced text is not guessed") and PA-222 (the probe verdict by judgment: `other_failure`/`cannot_judge` with a quote) to "the probe = A22". A22 makes a probe invalid only in a SHARED run; for a single probe run it gives no rule. Case: a single probe run times out at the substituted line, and the critic records `failed`, so a test that was not shown able to fail is counted proven. L7 also cites code-critic § Techniques "18 bullets (45-62), whole", which includes line 48 (PA-205), but its homed-elsewhere list leaves 205 out. Fix: move PA-205 and PA-222 to L7 as C criteria, in the source words: a failure that cannot be placed is not counted `failed`; it is rerun alone or recorded `impossible` with the quote. Drop them from L9.

**F4 (A34 L9, L12, fix) -- the cause list's home has no place on a critic finding, and L12's reason contradicts section 1.** L9: "causes = `red-causes.yaml`". But a critic finding carries gate, about, round, state and A17's `lower_layer`, and no cause (frame 2a). So PA-191's "a cause from the closed list" and PA-219's purpose (environment, tooling and reviewer_error are nobody's round) have no carrier. L12 gives the reason "code cannot read a cause class (AR-29)", but section 1 line 7 says "an enum word and a view row are presence and shape". Fix: give the true reason in L12 ("one counter for every stage, F8; a critic finding has no cause field, and adding one is beyond the budget"). Map environment and tooling to A13's `outside_control`, which is split off `to_report` and spends no further round. Say that a reviewer_error is the critic withdrawing its finding on re-check (mark `fixed`, with words).

**F5 (A34 L5, fix) -- the eight dimensions are told to the critic but nothing asks the critic to go through them.** L5 makes them "self-check lines the critic reads (A32 L17)". L3 has the critic answer each How checked criterion. But How checked is made of the gate rows, X1-X6 and the critic criteria (A21), not the page's self-check lines. The old critic scored every dimension for every case (case-critic lines 37-73). Fix: add one line to the common entry (F212), "on `check-selection`, each self-check line is a criterion for the G3 critic". Or state T5's own scope in L5: the critic looks at them and does not answer them.

**F6 (A34 L7, fix) -- the carried bullets keep old words that point at nothing in forge 2.** Examples: line 35 `blocked_by_check` row; line 50 `mechanical`, "our marker", a `find` model; line 60 `tests[].provisional`; line 62 `qa-provisional: P-n`. C2-2 forbids field and script names, but gives the builder no target to translate to. Fix: L7 names the targets: `blocked_by_check` -> results `not_reached` (C4-4); `mechanical` -> none, every round counts (L12); markers and provisional rows -> dropped, with this reason.

**F7 (A35 L17, fix) -- "the one cut is the Lead's line in B9" does not hold.** B9 is the forge's session retro. It reads "ONLY the forge journal" (B9 Delivers, K5), it has no cut line, and the Lead writes reasons per counter for forge events, not for the stages of a factory story. Theme T29 put "the dearest stage and one cut" into the dashboard view line. The old rule (retro-analyst line 53) says to name the cause of the overpay and the stage to cut, even on a clean run ("none worth making"). Two further gaps:
- "most tokens" replaces the old "highest cost" with no reason given. Tokens and cost rank differently when the models differ (A13 `model_rank`).
- The edge "a stage's tokens unmeasured -> prints `unmeasured`" leaves the partly measured case open.

Fix:
- Home the cut: who writes it, from this view, or record the drop with its decider.
- Write "tokens, because money is display-only (F7); with `--rates` the view ranks by money".
- Any stage unmeasured -> the line reads `unmeasured: <stages>`, with no maximum taken over the rest. This is the old rule: write "not measured", derive no number.

**F8 (A35 K7, owns, fix) -- the view may need code that A35 does not own.** A view row is `id`, `group_by`, `figures` (C4-6). "The stage with the most tokens, a tie names both, unmeasured never 0" is an argmax, not a group. Section 6 calls the no-code reading an `estimate`, yet `dashboard.py` is not in A35's owns. Fix: add `f/tools/dashboard.py` to owns as a C4-6 revision, or name the view grammar that expresses the argmax.

**F9 (A35 L9, fix) -- the damage to a person has no carrier.** L9 says "name the requirement broken, the damage, the steps and the failing test". The bug draft fields are steps, expectation + source, fact, evidence and repro (frame G5.3, line 194). K6's export prints severity, the answer id and the red test. The old Outcome (bug-reporter line 15) and Good outcome 1 (line 22, "User impact section") made the damage the centre of the bug. Fix (no new field): the damage goes in `severity_reason` as "who loses what", and the export prints it as `Impact:`. Or name `fact` as its words. Then add the case to K6.

**F10 (A35 amends C4-5, K5, fix) -- the card does not say where `host_adapter` learns which tool starts an agent.** C4-5 K5 forbids a harness name in `factory/tools`, so the name has to be profile data. The field is not named, and nothing says what happens when it is absent. Fix: optional `agent_tools: [...]` in `hosts/<host>.yaml`. When it is absent, the check is unproven and named once (A12's "restriction unproven" form); there is no load refusal, because that would make a new required profile field.

**F11 (A35 L5 against A32 L13, L14, L16, fix) -- two craft lines conflict, and the source's own resolution is carried by no line.** A35 L5 says that if the other group is changing a test file, put your check in a new file beside it. A32 says "a new file only for what nothing covers", "no near-copy", and gives the critic "extend versus new" as a criterion, so the G4 critic would write a finding against the file L5 asked for. The source settles it (code-critic line 34): "A new file beside a file another window claimed was forced by the guard: a note, never a finding". PA-197's `what` omits that sentence, and A32 L14 drops it. L5 also drops "your own file stays yours in repair rounds" (automator line 74). Fix: L5 adds both sentences, the first as a critic criterion.

**F12 (A35 L15, fix) -- PA-235's meaning is swapped for PA-245's.** PA-235 (doc-scribe line 23) is about Left with you being whole: one item for every left entry, of four kinds (a handed test, a worded deferral, an unconfirmed expectation, an assert stricter than its requirement), each with its requirement, case, whether a test exists and where it would run. L15 instead carries line 47 (PA-245: what you would see, what answer is wanted), which L14 already carries whole. C3-5 builds Left to you from `readiness`, `executable_where` and regression, so it is not stated whether a stricter assert or a worded deferral reaches it. Fix: L15 names each of the four kinds and the section built by code that holds it, or drops a kind with its reason.

**F13 (A35 L13, K6, fix) -- two details dropped without a reason.** PA-81's re-verification trigger for a quarantined flaky test (bug-reporter line 59): L13 keeps the mechanism and the decision, but not when to check it again. Bug-reporter line 24: "or the reason there is none" for the red test, where K6 prints a bare `no red test`. Fix: the Not proven flaky line carries the trigger, or L13 drops it with a reason. K6 prints `no red test: <why>` when the draft gives a reason.

**F14 (A35 L8, wording) -- one bullet has two homes on one page.** L8 cites bug-reporter § Techniques "9 bullets (42-50), whole" and names only PA-68 as homed elsewhere. Line 46 (search before you file) is also L10's rule on the same `bug` page. Fix: add "line 46 -> L10".

## Seam and class notes
- F1 is a class: a red treated as proof that a test can fail. I also checked the neighbours on the same surface. A22's shared-run rule already counts an unattributable failure as no kill. A33 L16 (red before the change) is topic 1, so I did not judge it.
- No new required field and no gate row: `severity` and `severity_reason` are optional, and F10's fix keeps the profile field optional. The size of part 10 was not judged, as the dispatch says.

## Spot-checks (FIDELITY sample, each against its cited source)
- A34 holds: L1 (lines 32, 83); L5 and L6 (lines 37-73, 107-120 and verdict T5); L8 (lines 22, 80-81, 86); L12 (automator line 84). L7: the counts hold (11 bullets at lines 30-40, 18 at 45-62), but the exception list is short (F3, F6). L3 holds the words but its output has no home (F2). L9 compresses its rows (F3, F4). L10 changes the meaning (F1).
- A35 holds: L4 (automator line 83); L8 (counts 7 at 31-37 and 9 at 42-50; F14); L11 (line 34); L14 (counts 10 at 31-40 and 13 at 45-57); L16 (C2-1 "not carried refs:A36, A37"). L5 is partial (F11). L9 has no carrier for the damage (F9). L13 is partial (F13). L15 is swapped (F12). L17's claim is false (F7).
- Facts by trail: these claims hold: the row counts (A34 45 = 11/31/3; A35 71 = 39/22/10, every PA id found, my script 71 of 71); every row's theme (T5, T14 and T28 lists; T1, T15-T17, T19 lists); A12's critic rows; A13's marks and `fix_rounds_max` 2; A17 `lower_layer`; C3-1 "field text is never cut"; C3-2 K4 (an absent data file refuses `load()` naming the card); A9's masking of secrets by the table; C2-1 K4 equality; A32 L17 and L18 as cited. These claims do not hold: B9 as the home of the cut (F7), and A22 as the home of PA-205 and PA-222 (F3).
- Not judged: none.

## Trail
- Read: part 10 (whole: sections 1-7, A32-A35); the themes file (lines 1-60, 126-270); ledger rows by id (script below); part 3b C4-2..C4-8; part 4-2 A12-A23; part 3 C3-1..C3-5; part 6 A26; the frame (2a lines 89-100, lines 111, 191-198); plan records 26.11 ~02:43 and ~02:59. Beyond the manifest: part 2b C2-1..C2-6, part 4b-2 B7-B10, part 4b-4 B12, and the role files at b2f70ac5e: case-critic, code-critic, bug-reporter, doc-scribe, automator (grep), retro-analyst (grep).
- `git -C C:/QAFactory/forge2-repo log --oneline -1` -> `f8337da specs: part 9 after its fix round, new part 10 (craft cards A31-A35); plan record`
- `wc -c .../part10.md` -> `53832`
- Ledger script (python, regex `\| PA-(\d+) \|` over the 71 ids of A35) -> `71 71`; the same for the 45 ids of A34 -> 45 rows printed.
- No probe: this is a plan gate with no diff.

```json
{
  "verdict": "blocker",
  "blockers": [
    "F1: A34 L10 + F214 -- the probe is waived for any red; a red at a locator, setup or timeout that reds repairs to green reaches the report never probed and not under Not proven; waive only a red at the test's own check, and list a waived test whose red is not product_bug and ends green under Not proven",
    "F2: A34 L3, L8, C4-2 amendment -- the strictness note, the per-criterion answers and the not-looked list have no home; a critic_findings row opens a fix round, plus a shortfall to an exited stage; a row written to_report at write time becomes a note with no round and no shortfall"
  ],
  "fixes": [
    "F3: A34 L7/L9 -- move PA-205 and PA-222 to L7 as criteria (a failure that cannot be placed is never counted failed); add 205 to the exception list",
    "F4: A34 L9/L12 -- give the true reason (no cause field on a critic finding; F8); map environment and tooling to A13 outside_control",
    "F5: A34 L5 -- a common line making the check-selection self-check lines criteria for the G3 critic, or state that they are looked at, not answered",
    "F6: A34 L7 -- name targets for old vocabulary (blocked_by_check to not_reached; mechanical to none; markers dropped)",
    "F7: A35 L17 -- B9 holds no cut; home the cut or drop it with a decider; give the reason for tokens over cost; partly unmeasured prints unmeasured with the stages",
    "F8: A35 owns -- add dashboard.py or name the view grammar for the argmax",
    "F9: A35 L9 -- the damage goes in severity_reason, printed as Impact in the export",
    "F10: A35 C4-5 -- optional profile field agent_tools; absent means unproven, named once",
    "F11: A35 L5 -- carry code-critic line 34 (a forced new file is a note, never a finding) and automator line 74",
    "F12: A35 L15 -- carry PA-235 (the four kinds of left items, and where each is built), not PA-245",
    "F13: A35 L13/K6 -- the flaky re-verification trigger; no red test with its reason",
    "F14: A35 L8 -- name line 46 as homed by L10"
  ],
  "class_completeness": "F1's class (a red taken as proof a test can fail): A22's shared-run rule is consistent with the fix; A33 L16 is topic 1 and was not judged. F2's class (critic outputs that are not findings): L3 and L8 both named. A plan gate, so the SIBLING_MAP axes of the old package do not apply (forge 2 touches no package file).",
  "trail": {
    "read": [
      "C:/QAFactory/forge2-repo/forge/specs/20261126-forge2-light-factory-spec-part10.md",
      "C:/QAFactory/forge2-repo/forge/specs/recon/carry/package-agents-themes.md",
      "C:/QAFactory/forge2-repo/forge/specs/recon/carry/package-agents.md (rows by id)",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part3b.md (C4-2..C4-8)",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4-2.md (A12-A23)",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part3.md (C3-1..C3-5)",
      "C:/QAFactory/forge2-repo/forge/specs/20261126-forge2-light-factory-spec-part6.md (A26)",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec.md (2a, 2c rows)",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-plan.md (records 02:43, 02:59)",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part2b.md (C2-1..C2-6)",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4b-2.md (B7-B10)",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4b-4.md (B12)",
      "b2f70ac5e:ai-packages/qa-factory/agents/qa-case-critic.md, qa-code-critic.md, qa-bug-reporter.md, qa-doc-scribe.md, qa-automator.md, qa-retro-analyst.md"
    ],
    "reruns": [
      {"command": "git -C C:/QAFactory/forge2-repo log --oneline -1", "result": "f8337da specs: part 9 after its fix round, new part 10 (craft cards A31-A35); plan record"},
      {"command": "wc -c part10", "result": "53832"},
      {"command": "python ledger row extraction over the 71 A35 ids", "result": "71 71"}
    ]
  },
  "mutants": [],
  "mutants_none": "plan gate: no diff and no new behaviour to probe"
}
```
