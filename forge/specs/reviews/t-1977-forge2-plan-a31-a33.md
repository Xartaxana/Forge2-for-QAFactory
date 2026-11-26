# t-1977 -- plan critic, forge 2 spec part 10, topic 1: cards A31, A32, A33

Reviewed state: forge 2 `f8337da` (clean tree; `wc -c` part 10 = 53832; `factory/` not built yet). Frame: part 10 section 1, the owner's yardstick of the dispatch, plan record 26.11.2026 ~02:59 (F210 (a), F211 (a), F212 (a), F213 (a), F214 decided by the Lead). Source of the craft: `P/<role>` at b2f70ac5e (`git diff --stat b2f70ac5e HEAD -- ai-packages/qa-factory/agents`: empty).

- A31: blocker
- A32: fit_with_fixes
- A33: blocker

Verdict: REJECT A31 and A33 as written (F1, F11, F12, F13 change what is built); NEEDS WORK on A32 (fixes only). Accepting is the Lead's call.

## Findings

### A31

**F1 (A31, blocker) -- the `questions` page is told only at `sources`, not at `plan`, `tests` or `reds`.** A31 Delivers: "told at entry to `sources` and `plan` (both hold `requirements`, `questions`, C3-2)". C3-2 (part3:40-44): `plan` craft = requirements, check-selection, levels, automate, regression; no `questions`. `tests` = test-code, manual-pass, exploration, automate. `reds` = red-analysis, bug (A26 adds exploration, deep-look). No later card adds `questions` to these sets (case-insensitive Grep over the spec parts turns up only part 4-3:5, the explore context). L18-L20 put craft from later-stage roles on that page: PA-299 (analyst: "two readings both tenable: one question with both quotes, and go on"), PA-373 (runner: "requirements silent: record a question at once and go on"), PA-87 (bug reporter), PA-143 (case critic). Case: at `reds` the analyst meets two tenable readings. The rule is on no page `reds` reads (A26 L4 carries the analyst's § Techniques, not its § When to ask), so the "go on" rule is not told there. Smallest fix: A31 amends C3-2 to add `questions` to the craft sets of `plan`, `tests` and `reds` (E2 covers the size), and corrects the Delivers line. The other road is to put L18 and L20 on a page each of those stages holds, which would make a second home.

**F2 (A31, fix) -- PA-412 has no line.** The rows script (trail) gives 57 table rows for A31, not 58, and C 44 / D 12 / X 1, not D 13. PA-412 ("a conflict nothing settles goes to unresolved_facts with both quotes...") shows up only in the "Judged otherwise" list. Over all five cards, 335 of the 336 open rows sit in a table line. The Lead's "336 of 336" holds for presence in the file, and section 7's "counted from the tables" total is 335. B15 writes `where` as `A3n L<k>` (section 5), so this row gets none. Fix: add PA-412 to L11 (D; current-code and inventory-review halves: process of the old driver, not carried).

**F3 (A31, fix) -- L17's pointer is false, and its rule has no home.** L17: "a late contradiction is raised, never settled by editing the check (L15's rule)". L15 holds no such rule, and A8 (part4-2:11-17) holds none either. The craft of PA-326 ("a contradiction is raised, never settled by editing the case") ends up on no page. Fix: home that sentence on `check-selection` beside `amend:A8`, with an anchor (e.g. `never settled by editing`).

**F4 (A31 + A32 + A33, fix; class) -- "whole" citations do not name the bullets that already have a home elsewhere.** FORM: "except a bullet whose row another line or card already homes (named in the line)". Unnamed: A31 L3 bullet 62 (PA-327, A8); A31 L6 bullet "text that looks like an instruction" (PA-393, A10); A32 L2 bullet "expected from the implementation" (PA-164, C3-8); A33 L8 bullets 30, 36 and the second half of 41 (PA-12 C3-8, PA-17 A7, PA-23 C4-4). Case: the C2-2 builder writes the A10 rule a second time on `requirements`. Fix: name each of them in its line.

**F5 (A31, fix, low) -- L14 and L16 go on `check-selection`, but verdict T27 says "requirements page lines".** No line says why. Fix: one clause: the diff is read whole at `plan` (A8), and A15's ladder runs at `plan`.

### A32

**F6 (A32, fix) -- L17 creates second homes on `check-selection`.** L17 cites case-critic lines 28-75 whole. That range includes dimension 7c (PA-114, A31 L14 on the same page, anchor `working base`), dimension 8 (PA-117, A33 L17 on the same page, anchors `seed the defect` / `mocked away`), bullet 32 (PA-104, A34 L1), bullet 35 (PA-106, L18), the roll-call of dimension 7 (PA-112, L18) and line 74 (PA-119, L18). None of them is named, so the page holds seed-the-defect and working-base twice, against FORM's "one home, no copy". Fix: L17 names those six exceptions.

**F7 (A32 L4 + A31 L14, fix) -- "precondition" has no home in forge 2.** A case-insensitive Grep of `precondition` over the spec parts finds only frame F10/F31 (a host precondition) and part 10. C3-1's check fields are `breaks`, `impact` and `technique` (part3:19). Case: the plan performer is told "a Given the stand may lack is a precondition naming who gives it" and has nowhere to write it, so `tests` never learns of it. Fix: say where it goes. The check's own text, no field, naming the giver: the check itself, key `stand`'s account (A9), or a question (C4-3).

**F8 (A32, fix) -- L6 cites "(A3)" for a rule A3 does not hold, and the rule is on no page.** A3 (part4:48-57) covers a late requirement from any stage. It says nothing about "a findings row `about` a check, never a silent change". L6 also has no page and no anchor, so PA-184's craft (keep a field you disagree with and say so) is told nowhere. Fix: home it on `check-selection` and `test-code` with an anchor, citing C3-1 `findings.about`.

**F9 (A32, fix, low) -- the order of the pyramid is lost.** Strategist bullet 57 ("The pyramid, from the bottom. After deciding WHAT is automated, prefer the lowest level...") has no ledger row. A Grep of `pyramid` in the ledger finds PA-25 and PA-440 only. Its order (what first, then the level) lies on no line. Also, `levels` is not in the `tests` set, although L16's criterion judges "the author's choice -- level" at G4. Fix: L20 adds "after deciding what is automated (L11)"; a level changed at `tests` is a deviation (L15).

**F10 (A32, fix, low) -- L1 "whole" takes in bullet 61, "Never `raise` a question once it is raised".** That is an old mechanism word, and the bullet has no ledger row (a Grep of `raise` in the ledger gives 5 hits, none of them this one). Fix: L1 names bullet 61 -> C4-3 edge "already answered -> not asked" (A31 L19).

### A33

**F11 (A33, blocker) -- `cannot verify` duplicates three existing reasons with weaker `needs`, and closes without routing.** L14's `needs` lists "a tool, the stand, a missing oracle". Those are frame 2c's "no tool for this surface", "stand unavailable" (needs an attempt) and "no reliable expectation source" (frame line 134). The new row needs only words, and a named reason closes a debt unrouted, while `other` is routed (C3-3 K5). The old rows said the opposite: PA-300 "keep the obligation unverified, return the gap to its owner", PA-221 "reported unverified... a defect found by reading is rejected". Case: a G4.2 debt at `tests` is closed by `cannot verify: stand slow`. It needs no attempt, no critic judges named reasons (C4-2 judges `other` only), and the gap is never returned. Smallest fix: drop the row and carry PA-140, 221, 300 as D onto the three existing reasons (F211 then has two rows). If the Lead keeps it: `needs: attempt`, plus a page rule "only when no narrower named reason fits".

**F12 (A33, blocker) -- `field absent from the response` drops the question.** PA-49 says "a step the product does not allow **or a field the case reads that does not exist**: unresolved with reason impossible **and a question**", and PA-14 says "a question about the case". F211 gives `step impossible` a question id but gives this row only the shape source. Case-critic dimension 7e (ii), which A32 L17 carries whole, says a field the requirement needs and the product holds nowhere is "the requirement's one expected red". L12 says "never a bug". Case: the requirement names `delivery_date` and the product omits it. The test is closed by this reason, unrouted and never a bug, and the defect escapes past `reds`. Fix: `needs: the shape source read, a question id`. L12 adds: a field the requirement itself names is a red for `reds`, not this reason.

**F13 (A33, blocker) -- L20 (with L3 and L21's craft) is homed on `stand`, a stage-2 page.** `stand` comes from C2-4 F22 (a), "stage 2 product, smoke, stands and test data", and the `tests` and `reds` sets do not hold it (C3-2, A26). L8 and L9 move PA-22 and PA-34 off `test-code` explicitly, and PA-200 (G4 critic) and PA-266 (analyst) land there too. Since the G4 critic reads the same pages as the performer (F12), it cannot judge the rule either. Case: a test gets a 500 from the product at `tests`. "A product answer is a red, never a stand block" is not told there, and the obligation closes by `stand unavailable`. Fix: put L20's rules on `test-code`, with the control half on `red-analysis`, or amend C3-2 to add `stand` to the `tests` and `reds` sets. Add a line saying why against T26's "stand page". The same goes for L3's own-data and account rule, which the manual walk needs at `tests`.

**F14 (A33, fix, high) -- L20 maps "a step failing twice with nothing in its way" to `stand unavailable`.** The source word is `inconclusive` (runner:50). "Nothing in its way" means the stand is not shown at fault, and the default stays the product (analyst:33). Case: Save does nothing twice, the step is recorded as `stand unavailable`, and `reds` never sees it. Fix: hand it to `reds` (`handed`, A28 (d)) with both attempts, and never use `stand unavailable` without a shown obstacle.

**F15 (A33, fix) -- the net that F211 rests on is not built.** "The report lists each by name under Not proven" (Delivers; F211's "the Not proven list is the net"). A33's amends on C3-5 name only the flaky line, and the `test_docs_build.py` row covers flaky only. Fix: amend C3-5 so that Not proven lists every obligation closed by the new reasons, by name, and add a docs_build row.

**F16 (A33, fix) -- edge: a live `flaky` red whose obligation later runs green.** G6.2 counts the green as Proven, and L10 lists the red under Not proven, so the report contradicts itself. PA-288 says "an unfixed flake is not verified". Fix: state that the obligation is not counted Proven while its red's cause is `flaky` and the repair is not confirmed; K5 adds the case.

**F17 (A33, fix) -- L15 drops PA-298's reading discipline.** The source says to read the run's log, quote it, and write the failure verdict the log shows. C4-4 keeps the raw output, but no page tells `reds` to read it when the summary is `unknown`. Fix: one `red-analysis` rule: a run whose summary is unknown is read in its raw output; a failure it shows is triaged as a red, and the run is never counted passed.

**F18 (A33, fix, low) -- four small fixes.**
- The amends line omits L14's critic criterion.
- L19 marks an opposite half D. By E3, PA-209's product-mutation half needs `note: opposite: A22` (A26 L14's form).
- L21 rests on A29's lease while A29 is with the Architect (plan 02:43). Say that L21 holds on C3-6 and A9 alone if A29 changes.
- L21's "owner and remedy" is on no page; add it to L20's rule.

## Owner's yardstick, per card

- A31: free agent and more: yes for stage 1 (contradictions L11/L2/L7, gaps L1-L3, assumptions L9). Gate: no new gate. Told at entry: no for `plan`/`tests`/`reds` (F1). Nothing forgotten: PA-412 (F2), PA-326 (F3).
- A32: yes. Gate: no new gate. Told: yes, but some homes are unnamed (F6-F8). Nothing forgotten: the pyramid's order (F9).
- A33: free agent: no while F11-F14 stand (a named reason can close what a free agent would report as a red). Gate: F211's error direction is "toward closing" and its net is unbuilt (F15). Told: no at `tests`/`reds` (F13).

## Fidelity sample (carry line against its source section)

- A31: L1 (Good outcome 1, holds); L2 (14 = lines 32-45, holds); L3 (13 = 50-62, holds; F4); L6 (16 = 32-47, holds; F4); L7 (10 = 52-61, holds); L10 (scout:59 + GO4, holds); L11 (PA-309/317, holds); L14 (case-critic 7c, holds); L16 (scout:57, holds); L17 (F3).
- A32: L1 (13 = 49-61, holds; F10); L2 (14 = 31-44, holds); L3 (verbatim GO3); L4 (GO2 + Tools 69-70 + When to ask 82, meaning holds; F7); L9 (strategist 51-63, holds); L10 (holds); L13; L14 (automator 50-51, holds); L17 (F6); L20 (F9).
- A33: L2 (runner GO1-2, 30, 32, holds; the gist is offset by FORM's source-bullet rule); L6 (analyst:80-81, holds); L8 (14 = 30-43, holds; F4, F13); L9 (16 = 48-63, holds); L12 (F12); L14 (F11); L15 (F17); L16 (T23, holds); L17 (PA-117/154/175, holds); L20 (F13, F14).

## The dispatch's specific questions

- Stage 1 as hard as the old tester: yes in content. Told at the later stages: no (F1).
- Check design: independent vs sequential: A32 L2 ("order between cases", whole), A33 L9 ("a red hides no other"), A34 L7 (PA-198). Pyramid: L20 + L17 dim 2b + L14 (order: F9). "A case says WHAT, the automator HOW": PA-5/PA-148 found in C2-3 ("case and autotest not one-to-one"); no line weakens it.
- Run and red: a red read before it is named comes from A26 L4 (analyst § Techniques whole), not doubled. A probe never writes product code: A33 L19 / A22, holds. The three F211 words: F11, F12, F15.

## Plan gate (rule 24)

- Q13 (a) edges: F12, F14, F16 are silent edges. Each card states its E1-E4 and empty inputs.
- Q13 (b) meaning: the meaning of `cannot verify` overlaps three existing reasons (F11).
- Q13 (c) premises: re-ran the coverage fact (F2: 335 in lines) and the bullet counts (all hold).
- Q13 (d) readers: no `owns_readers.py` block was attached; not judged -- `factory/` does not exist yet (section 6 defers it to the Lead).
- Q13 (e) forks: F210 (a) agrees with T11. F211 (a) agrees with T20 in kind, but its rows contradict PA-300/PA-49 (F11, F12). F212/F213/F214 belong to topic 2.
- Q4 class: F4 (one class over three cards).
- Q6 duplication: F11 (a reason duplicating three), F6 (two homes).
- Q12 one road: none found (no language, runner or tracker name in A31-A33; checked by reading the tables).
- VARIETY: none (page lines and closed words); an unknown value at `tests` defaults to a closing reason (F11, F14).

## Trail

- Read: part 10 lines 1-131 and 188-246; themes (preamble, T2-T14, T18, T20-T27, T30); ledger rows of requirements-tester, scout, case-designer, case-critic, test-strategist, automator, failure-analyst, runner (Grep by source), plus PA-140, 196-221; P/ files requirements-tester, scout (whole), case-designer 19-85, case-critic 26-91, test-strategist 19-90, automator 13-89, failure-analyst 14-95, runner 14-76; part 6 A26 (33-130); part 4-2 A8-A22; part 4 A3-A5; part 3 C3-1..C3-5; part 3b C4-2..C4-4; part 2b C2-3, C2-4; frame line 134; plan record 02:59, 02:43, 01:45 (Grep).
- Reruns:
  - the rows script, card tables vs theme rows: A31 57 (missing PA-412), A32 84/84, A33 78/78.
  - the total script, open rows vs table lines: 335 of 336.
  - Grep `precondition` -i: frame + part 10 only.
  - Grep `pyramid`, `raise`, `split` -i in the ledger, with positive controls (PA-25, 5 hits, 3 hits).
  - `ls factory/`: absent.

```json
{
  "verdict": "blocker",
  "blockers": [
    "F1: A31 Delivers says plan holds the questions page; C3-2 plan, tests and reds sets do not; L18-L20 rules from analyst, runner, bug reporter and case critic are told only at sources -- add questions to those craft sets",
    "F11: A33 reason cannot verify duplicates no tool for this surface, stand unavailable and no reliable expectation source with weaker needs and closes unrouted, against PA-300 and PA-221 -- drop it or give it needs attempt and a narrowest-reason rule",
    "F12: A33 reason field absent from the response drops the question PA-49 and PA-14 require; a requirement-named field the product lacks closes as never a bug -- needs a question id; a requirement-named field is a red",
    "F13: A33 L20, L3 and L21 craft homed on stand, a stage-2 page absent from the tests and reds craft sets; L8 and L9 move PA-22 and PA-34 off test-code -- home on test-code and red-analysis or amend C3-2"
  ],
  "fixes": [
    "F2: add PA-412 to A31 L11; correct the counts",
    "F3: home A31 L17 contradiction rule on check-selection; drop the false L15 pointer",
    "F4: name the already-homed bullets in A31 L3, L6, A32 L2, A33 L8",
    "F5: one clause why A31 L14 and L16 sit on check-selection",
    "F6: A32 L17 names PA-114, 117, 104, 106, 112, 119 exceptions",
    "F7: say where a precondition is written (check text, giver named)",
    "F8: A32 L6 cite C3-1 findings.about and give it a page and anchor",
    "F9: A32 L20 adds the pyramid order; a level change at tests is a deviation",
    "F10: A32 L1 names bullet 61 to C4-3 edge",
    "F14: A33 L20 never maps an unobstructed double failure to stand unavailable; hand it to reds",
    "F15: A33 amends C3-5 Not proven to list the new reasons; a docs_build row",
    "F16: A33 states that a live flaky red keeps its obligation out of Proven",
    "F17: A33 red-analysis rule to read raw output when the summary is unknown",
    "F18: A33 amends adds L14; L19 note opposite A22; L21 holds without A29; owner and remedy onto L20"
  ],
  "class_completeness": "F4 is one class over A31, A32, A33 (whole citations not naming already-homed bullets), all instances named; F1 and F13 are one class (craft homed on a page the source role's stage does not read), both instances named; topic 2 cards not walked (another critic)",
  "trail": {
    "read": [
      "C:/QAFactory/forge2-repo/forge/specs/20261126-forge2-light-factory-spec-part10.md",
      "C:/QAFactory/forge2-repo/forge/specs/recon/carry/package-agents-themes.md",
      "C:/QAFactory/forge2-repo/forge/specs/recon/carry/package-agents.md",
      "C:/QAFactory/forge-repo/ai-packages/qa-factory/agents/qa-requirements-tester.md",
      "C:/QAFactory/forge-repo/ai-packages/qa-factory/agents/qa-scout.md",
      "C:/QAFactory/forge-repo/ai-packages/qa-factory/agents/qa-case-designer.md",
      "C:/QAFactory/forge-repo/ai-packages/qa-factory/agents/qa-case-critic.md",
      "C:/QAFactory/forge-repo/ai-packages/qa-factory/agents/qa-test-strategist.md",
      "C:/QAFactory/forge-repo/ai-packages/qa-factory/agents/qa-automator.md",
      "C:/QAFactory/forge-repo/ai-packages/qa-factory/agents/qa-failure-analyst.md",
      "C:/QAFactory/forge-repo/ai-packages/qa-factory/agents/qa-runner.md",
      "C:/QAFactory/forge2-repo/forge/specs/20261126-forge2-light-factory-spec-part6.md",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4-2.md",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4.md",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part3.md",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part3b.md",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part2b.md",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec.md",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-plan.md"
    ],
    "reruns": [
      {"command": "git -C C:/QAFactory/forge2-repo log --oneline -1; wc -c part10", "result": "f8337da; 53832"},
      {"command": "python -B scratchpad/rows.py (card tables vs theme rows)", "result": "A31 expected 58 in table 57 missing [412]; A32 84/84; A33 78/78"},
      {"command": "python -B scratchpad/total.py (open ledger rows vs table lines)", "result": "open rows 336 in table lines 335 missing from lines [412]"},
      {"command": "Grep -i precondition over forge/specs/*spec*.md", "result": "frame lines 342, 354 (host precondition) and part 10 only"},
      {"command": "grep -i pyramid|raise|split ledger", "result": "PA-25, PA-440; 5 hits none the bullet; 3 hits none the bullet"},
      {"command": "git -C C:/QAFactory/forge-repo diff --stat b2f70ac5e HEAD -- ai-packages/qa-factory/agents", "result": "empty"}
    ]
  },
  "mutants": [],
  "mutants_none": "plan gate: no diff and no new behaviour to probe; factory/ does not exist"
}
```
