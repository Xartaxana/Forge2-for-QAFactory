- A24: fit_with_fixes -- the stage-2 look is the owner's picture with the record told at entry, but the X1 filter's empty outcome is not scoped to the exiting stage, and K3, the edges and the cut close line still use the pre-A26 forms.
- A25: fit_with_fixes -- the replay road fits the 23:50 idea, but G4.2 and the handover accept a replay that was never run, and a replay that fails on what the manual pass left on the stand has no stated outcome.
- A26: blocker -- the stage-5 explore launch (the deep look itself) is never given `deep-look` or the open-place rule its exit now asks for, the card puts refs:A20's deep rules on the page it declares shallow, and the `bug` answer is offered at stages that cannot write a `bugs` row.

# t-1949 -- critic on plan: A24 r2, A25 (part 5), A26 (part 6) at e8b7eae29

Verdict: NEEDS WORK (A24, A25) / REJECT (A26, `failure_class: spec`). This verdict is an input. Accepting the cards stays with the Lead.

Yardstick findings rank first. These are the findings where the factory would do less than a free agent, or where an exit asks for something entry never told: F1, F3, F4, F9.

## Findings

**F1 (A26, blocks) -- the explore launch at `reds` gets neither the deep page nor the X4 rule its exit asks.** Part6:39 says STAGE 5 is "the `reds` performer ... and its `explore` launch; pages red-analysis, bug, exploration, deep-look". Part6:30 amends only the `reds`, `tests` and `product` craft sets. The launch row `explore` is a separate row of `stages.yaml`, and A24 r1 (part4-3:5) gives it "the `exploration` craft page" only. K6 (part6:48) checks the `reds` context only. Part6:33 adds X4 to the explore exit, but A24 r1's sentence "X2, X4 and X6 are asked of them at no exit" (part4-3:5) is not rewritten. As written, the launch that does the deep look gets the shallow page and no `--group explore` context line. Its exit then asks X4. That is less than a free agent, and asked without being told. Fix: amend the `explore` launch row's craft set (exploration, deep-look, plus `perturbations` through `data`), and name the context line for `--group explore`. Rewrite the advisory sentence as "X2, X6 at no exit; X4 at explore's own exit only, never at a later stage exit (the `report` exit included)". Add a K row: the `--stage reds --group explore` context holds deep-look and the axes, and the `report` exit does not owe explore's open rows.

**F2 (A26, blocks) -- refs:A20 is homed on the page the card declares shallow.** Part6:28: "The carry lines' existing homes stand (refs:A20 -> `exploration` ...)". Recon `references` row A20 reads: "Exploration: hypothesis + oracle + refuting observation written BEFORE capture; one cell per call with a control" (explore-charter.md:11-60). Part6:38 says: "No deep technique is on this page (invariant ...; a deep rule on it is a C2-2 K2 finding)". K10 checks the same. The C2-4 builder cannot satisfy both. Fix: re-home refs:A20 to `deep-look`, keeping only "nothing broke needs what was tried" on `exploration`. Amend the C2-1 map line.

**F3 (A26) -- `bug` is offered where no `bugs` row can be written.** The X4 door (part6:32) and ANSWERS (part6:42) offer `bug (bug id)` at every stage. `bugs` is a leave of `reds` only (part3:44 stage table). `product` and `tests` do not leave it, and neither does the explore launch, which leaves `findings` only (part4-3:4). The `bug` page is in `reds`' set only. At `product`, the stage whose owner's picture is "сразу увидит ... если они совсем уж не правильно работает", the door names a road the receiver cannot take. Fix: `bug` is legal at `reds` only. At `product`, `tests` and explore, a suspected bug is `asked` (`bug_or_not` section `beyond`, A4). The X4 door text is per stage. Add a K row: `revise --outcome bug` at `product` is refused, door `asked`.

**F4 (A26/A24) -- the goal row meets the `reds` filter, and its outcome under X4 is unstated.** A24 r1 (part4-3:9) defines the goal as "`findings` `kind: beyond`, `about: plan:exploration`", written by the reds performer at `reds`. Under the X1 filter reading (part5:35), that row alone meets F114's record. So the goal plus a cut explore leaves the stage-5 look as a goal line with no look and no tried list, and the owner's 00:19 "нулевой исход без перечня — не исход" is bypassed. The goal's `outcome` (none? `open`?) is also unstated against the widened X4. Fix: a goal row does not count for the filter and carries no outcome that X4 reads. State it, and add a K row.

**F5 (A24 text, made live by A26) -- the empty outcome of a filtered leave is not stage-scoped.** Part5:35: "met by a live row ..., written at the exiting stage (`stage` field), ... or by its empty outcome". The empty outcome carries no stage condition. A product `nothing_beyond` stays live at the `reds` exit, so under F114 it meets reds' filter: one condition is satisfied by another stage's row (rule-15 class). Fix: "or by its empty outcome written at the exiting stage". Add a test row: a `product` `nothing_beyond` does not meet `reds`.

**F6 (A25) -- a replay never run passes G4.2 and reaches the person as regression.** The checks table (part5:15) and K4 ask for "a replay or `no_replay`", which is an evidence row. Nothing asks for a `runs` row with `replay_of`. F107's own reason for (a) is "a script that does not repeat reaches the person as 'ready regression' unchecked". As written it still can, and so can a replay whose only run is red with cause `environment`. Fix: G4.2's replay branch is met by a replay row plus a run of it (`runs.replay_of`). The door is "run it: `run_tests.py run --replay <id>`". The handover lists a replay whose last run is not green under "not proven to repeat: <cause>". Add K rows for both.

**F7 (A25) -- a replay that fails on the state the manual pass left.** The replay runs "once, right after recording, in the same launch" (part5:49), on the stand the pass just changed (a user created, an order placed). The edge "a replay that changes stand data -> as the manual pass did" (part5:53) does not cover a replay that cannot re-run over its own leftovers. A refusal such as "already exists" reads as "expectation not met -> `product_bug`", which sends a false bug draft to the person. The handed-over regression fails on its second run too. The old runner's "Your own data. Create ... and tear it down" (qa-runner.md:52) is not cited. Fix: the replay contract on the page says the script makes its own data per run (generated names) or restores it. A red whose cause is the pass's leftovers is `test_error` (rewrite). Add a K row.

**F8 (A25, minor) -- a stale `expects` row.** `expects` are checked only at store time. `stale` propagates over `from`, never over other fields (part3:22). Fix: state the outcome when an `expects` row goes stale later (the replay row is stale under X4: re-record or `no_replay`).

**F9 (A26) -- suspicions the run left that nobody opens.** L1 (part6:56) says "every red and every run suspicion is a place". X4 makes `tests` answer its own open places (part6:49, "the same X4 debt of that stage"), so no suspicion is handed to `reds`. The old analyst judged every observation "a green check's too" (qa-failure-analyst.md:26), as a second look. When the analyst was not dispatched, the old close wrote the gap "the analyst was not dispatched: no failure to triage" (place-answers.json:26). Both are lost without a drop line. Fix: either a `tests` place may be answered `asked`/handed with `about` to `reds`, and the red-analysis page names it, or L1/L13 become `dropped` with a decider (B15 form).

**F10 (A26) -- the zero-red stage.** No rule skips `reds` when there is no red (grep `no reds?|zero reds|skip.{0,40}reds|every red`: part3, part3b, frame 0, control part6 2). Its exit then asks the empty `reds` and `bugs` rows (X1, part3:44), the beyond row or `nothing_beyond` with tried (F114), and an answer for every place opened (X4). The card states none of this for zero reds, and `red-analysis` ("every red ... is a place") gives no subject when there is none. Fix: an edge and a K row for zero reds. The page says what is looked at then: the run's suspicions, and the seams of the changed feature.

**F11 (A24/A26) -- forms that A26 changed but A24 r2 still states.** A24 r2 K3 (part5:43) "with [`--reason`] -> met", and the edges "`nothing_beyond` with why" (part5:44). A26 makes `tried` mandatory (part6:31). Part6's section 5 names "A24 r2 (context line, `--tried`)" but no amends line rewrites K3. The A24 r2 cut close line ("the look is closed: do not resume it", part5:44) conflicts with part6:49 "an `open` place at a cut -> kept, named as a debt in the relaunch block". Fix: amend K3 and the edge, and add to the close line "each open place: revise to `not_done`, reason `stopped at a cap`".

**F12 (A26) -- `perturbations.yaml` drops `subject`.** Part6:36 carries `id, applies_to, kinds(id, why), oracle`. The old rows hold `"subject": "every input field of the flow you meet"`, "every action that saves", and "every sign-in you can reach with state built as a guest" (perturbations.json:17,29,37). The `steps` values ("12", "the limit plus one, 0, -1") are lost too, not just their syntax. Fix: carry `subject`, and carry the values as words in `why` or a `values` field.

**F13 (A26) -- L14 is a drop labelled D.** The old rule "never read the application's sources" (walk-charter.md:3-4). The new text says "reading code stays legal". This is the opposite. Under B15's own rule (part6:130) it is `dropped`, `note: opposite:`, with a decider. Fix: verdict F/dropped with a decider.

**F14 (A26) -- the order of the temporal world.** The C3-2 craft-set change makes `tests` and `reds` unlaunchable until `deep-look.md` exists (part6:44). The card does not say which move lands first. Fix: the craft-set row lands with or after C2-4's page.

**F15 (A26, minor, Q6) -- `seen` against `outcome`.** `outcome: matched, seen: missing` is accepted. Fix: state the pairs (`missing|unreachable|access|nature` never with `matched`).

## Fidelity sample of A26's carry lines (old source opened per line)

- L1 D (qa-failure-analyst.md:16,26,59): name only. Lost: "every observation of a manual check judged, a green one too" (F9).
- L3 C (:33-46, 14 bullets): carried. The card cites "the 14 lines".
- L4 C (:51-65): partly. Lost (not on any L-line): "Read the control experiment" (the ASSERT_STRICTER / not-this-story / ordinary-red reading), "One red, one triage" (dependent and independent Thens), "Judge a manual check by its captures", "One cause, one draft", "Repair the mechanism, never the expected value", "Say how far you got". The digest compressed 15 techniques to 4. Fix: cite § Techniques whole on `red-analysis`, as L3 does.
- L5 C (:57,65): partly. Lost: "A flaky test's repair is confirmed by reruns of the new bytes, not by one green", "counted across every role", "quarantining it is the person's call".
- L12 D (place-answers.json:5-9): partly. Lost: `capture_required` for `not_a_bug`, `requirement_silent`. `matched` asks for no evidence, and "`evidence` row cited" has no field. Fix: the page says `matched` names what was seen (evidence id or words), plus an optional field.
- L13 D (place-answers.json:22-35): carried differently for opened places (X4; explore `left open`). Lost: the gaps for unopened run suspicions (F9).
- L14 D (walk-charter.md:3-4): content reversed (F13).
- L15 C (walk-charter.md:14-15 via refs:A21 = :14-27): carried.
- L17 C (walk-charter.md:17-27): carried. refs:A21 covers "a second stop on that step is a result".
- L19 C (qa-runner.md:30-37, 8 bullets): carried by count.
- L22 C (qa-runner.md:46): carried (`deep-look` "one change at a time with an undisturbed control").
- L27 C (qa-runner.md:54): carried by source line, the path map included.
- L28 F (qa-runner.md:54): carried (F112). The definitions of `access` and `nature` go with L27's source line.
- L32 C (perturbations.json): partly (F12).
- L33 C (explore-charter.md:24-25): carried ("axis, requirements silent" -> question).
- L35 D (explore-charter.md:46-65): partly. Lost: "Its rows are observations, not oracles" (start from the first look), and "a failure that never fired ... is `not tried`" (the check behind fail-first). The A26 deep-look list (part6:39) also omits L35's own "start from stage-2 rows" and "make the failure before the action".
- L41 C (qa-test-strategist.md:32-46): partly. The file holds 15 bullets, not 13. "Data the stand cannot reset" and "Appearance is cheap, behaviour is not" are on no line. The plan/look split is not named per bullet (migrations, flags, dependency failure).
- L42 D (qa-test-strategist.md:62): partly. Lost: "time-boxed" (no box named for an exploratory check).
- L57 F (pile batch-2:28, read beyond the manifest): carried. The owner's word "как минимум эти 3 бага" is verified.

Package-agents ledger rows (B15, F118 (a): `blocks: A26`) may later catch L4/L41. A26's K10 checks only its own 65 lines, so the losses above stand against A26.

## Questions of the dispatch

- Told at entry. `tried`: the product context line, `exploration.md`, the reds context line; at explore, missing (F1). Open-place answer: the product and reds lines, `red-analysis`, How checked X4; at explore, missing (F1). Beyond row or nothing-found: How checked X1 with filter (A21) at `product` and `reds`. Replay: G4.2 in `manual-pass` How checked. The replay run is told but not asked (F6).
- Means counted at exit: none found in the three cards. `flaky` `needs` "the three isolated runs" is evidence for a classification (old L5), presence only. I judge it legal.
- X4 way out: stand down -> `not_done`, reason "stand unavailable" plus attempt (a frame 2c row). Explore stopped -> `left open: stopped at <cap>`, the route goes on. A stage unanswered after `refusal_relaunch_max` -> the conductor, `passes`. No deadlock and no silent pass, once F1's later-exit clause is written.
- A25: stand-data replay -> F7. A manual pass not repeatable -> `no_replay: <why>`, stated. A replay red on a working product -> `test_error` rewrite, capped at 2 then `no_replay`, stated (except F7's case).
- Closed vocabularies: `outcome`, `seen` and perturbations have one home each. No copy found.
- Accepted cards changed without an amends line: F1 (A24 r1's advisory sentence) and F11.

## Standing lines (plan gate)

- Q13(a) EDGES: F4, F5, F7, F8, F10, F14.
- Q13(b) MEANING: X4 after the change means "no stale row and no live `open` place the stage wrote". This contradicts part4-3:5's advisory sentence (F1).
- Q13(c) PREMISES: re-ran two. The analyst's 14 bullets reproduce. The digest's 13 strategist bullets do not: the file holds 15 (L41).
- Q13(d) READERS: no `owns_readers.py` block. Not run, because every touched factory file is unbuilt (`ls C:/QAFactory/forge2-repo/factory` -> no such directory) and the tool reads this repository's tree. The cards' readers stay `estimate` until build.
- Q13(e) FORKS: F107-F116 as decided. F113 (a) and F114 (a) are written for the decided option, except F3 and F4. F110 (a) breaks on F1 and F2. F112 (a) is fine.
- Q4 CLASS: the filter extension (F5) and the explore row (F1) are the unfixed siblings. Both are inside A26's owns.
- Q6 DUPLICATION: F15. None other found (grepped `no_stale`, `supersedes`, `bug_or_not` across the spec parts).
- Q12 ONE ROAD: none found. Axes and replay commands are data or role judgment; the project axes go through knowledge.
- VARIETY: a library or CLI project -> `not_done`/code reading, `no_replay` or a CLI replay, factory axes ignored by judgment. No block, no silent default.

## Trail

Read: part5 whole; part6 whole; plan 2667-3142; digest whole; part4-3:1-30; part4:59-68; part3:36-50 plus greps; frame:120-199 rows; the three agents, explore-charter, walk-charter, perturbations.json, place-answers.json whole; recon references rows A20/A21; pile exploratory batch-2 by grep (beyond the manifest). Commands: `git log --oneline -1` -> e8b7eae29; `git status --short` part5 part6 -> empty; the zero-reds grep with its control (above); `ls forge2-repo/factory` -> absent.

```json
{
  "verdict": "blocker",
  "blockers": [
    "F1: A26 never gives the explore launch at reds deep-look, perturbations or the open-place context line, yet its exit now asks X4; the advisory sentence of A24 r1 is not rewritten (part6:30,33,39; part4-3:5)",
    "F2: A26 keeps refs:A20 (hypothesis, one cell per call with a control) homed on exploration.md, which it declares shallow with K10 against deep rules (part6:28,38)"
  ],
  "fixes": [
    "F3: bug answer legal at reds only; product, tests and explore use asked; per-stage X4 door; K row",
    "F4: the explore goal row does not meet the reds filter and carries no outcome X4 reads",
    "F5: the X1 filtered leave's empty outcome is scoped to the exiting stage; test row",
    "F6: G4.2 replay branch needs a run with replay_of; handover marks not-proven replays",
    "F7: the replay contract makes its own data or restores it; a red caused by leftovers is test_error",
    "F8: state the outcome for an expects row staled after store",
    "F9: route tests-stage suspicions to reds, or record L1/L13 as dropped with a decider",
    "F10: zero-red reds stage edge and K row; page subject when there is no red",
    "F11: amend A24 r2 K3 and edges for tried; the cut close line answers open places as not_done",
    "F12: perturbations.yaml carries subject and the step values as words",
    "F13: L14 is a drop (opposite) with a decider",
    "F14: the craft-set change lands with or after the deep-look page",
    "F15: state the allowed seen and outcome pairs",
    "Fidelity: cite the analyst's Techniques whole (L4); restore the lost clauses of L5, L12, L35, L41, L42"
  ],
  "class_completeness": "Siblings walked inside the three cards: the X1 filter extended from product to reds (empty outcome scoping, F5), the explore launch row next to the reds stage row (craft and X4, F1), the bug answer across every stage that can open a place (F3). All fall inside A26 owns; none leaves the round.",
  "trail": {
    "read": [
      "C:/QAFactory/forge-repo/docs/tasks/specs/20261125-forge2-light-factory-spec-part5.md",
      "C:/QAFactory/forge-repo/docs/tasks/specs/20261126-forge2-light-factory-spec-part6.md",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-plan.md:2667-3142",
      "C:/QAFactory/forge2-repo/forge/specs/recon/20261126-forge2-recon-what-the-agent-looks-at.md",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4-3.md:1-30",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4.md:59-68",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part3.md:36-50",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec.md:120-199",
      "C:/QAFactory/forge-repo/ai-packages/qa-factory/agents/qa-failure-analyst.md",
      "C:/QAFactory/forge-repo/ai-packages/qa-factory/agents/qa-runner.md",
      "C:/QAFactory/forge-repo/ai-packages/qa-factory/agents/qa-test-strategist.md",
      "C:/QAFactory/forge-repo/ai-packages/qa-factory/references/explore-charter.md",
      "C:/QAFactory/forge-repo/ai-packages/qa-factory/references/walk-charter.md",
      "C:/QAFactory/forge-repo/ai-packages/qa-factory/references/perturbations.json",
      "C:/QAFactory/forge-repo/ai-packages/qa-factory/references/place-answers.json"
    ],
    "reruns": [
      {"command": "git -C C:/QAFactory/forge-repo log --oneline -1", "result": "e8b7eae29 state: narrative -- the owner's yes to the thin pass before the gates"},
      {"command": "git -C C:/QAFactory/forge-repo status --short -- part5 part6", "result": "empty"},
      {"command": "grep -c -i -E '(no reds?|zero reds|skip.{0,40}reds|every red)' part6 part3b part3 frame", "result": "part6:2 part3b:0 part3:0 frame:0"},
      {"command": "ls C:/QAFactory/forge2-repo/factory", "result": "No such file or directory"}
    ]
  },
  "mutants": [],
  "mutants_none": "plan gate: no code exists, no probe"
}
```
