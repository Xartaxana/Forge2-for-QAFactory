<!-- scout hand-back, journal task t-1894, recon for docs/tasks/specs/20261125-forge2-light-factory-plan.md; saved verbatim from the worker's final message -->

digest: v1 t-1880

Scope note. Area = ai-packages/qa-factory/skills/qa-story/ (13 files) + ai-packages/qa-factory/agents/ (12 files). All 25 read fully except evals.json (read lines 1-70 plus every "prompt" line, skimmed). Root: C:\QAFactory\forge-repo. Short paths below are relative to ai-packages/qa-factory/. S = skills/qa-story/phases/s<n>.md, SK = skills/qa-story/SKILL.md, A = agents/<role>.md.
Key finding on "owner's word": the 25 files carry exactly ONE dated owner word. It is s8.md:85, «owner's word 31.10.2026»: screenshots of manual checks go to the person, never into the report or MR text. The English text of that rule is quoted in A12. No Russian original is in the area. Most "settled" craft sits in the role files with no dated source. Dated owner words sit elsewhere, outside the given area. A Grep for "owner's word|owner's rule|[А-Яа-я]{4,}" (-i) over agents/ found nothing. The same shape over skills/ found only s8.md:85 (control: t17 vs t18).

## Objects
| id | kind | gist | paths | status | owner | links | ev |
|---|---|---|---|---|---|---|---|
| q1 | finding | Dated owner words in area: only one (31.10.2026, screenshots) | skills/qa-story/phases/s8.md:85 | present | owner 31.10.2026 | A12 | t17,t18 |
| q2 | finding | No owner's-word markers anywhere in agents/ | agents/ | absent | — | — | t18,t17 |
| q3 | contradiction | Strategist file says no critic judges the plan; s3.md and s2.md say driver dispatches qa-case-critic after S2 and S3 | agents/qa-test-strategist.md:21 vs skills/qa-story/phases/s3.md:61 | present | — | D1 | t1,t8 |
| q4 | contradiction | SKILL.md stage table puts S2 and S3 critic-free; s2.md:117 and s3.md:61 add a critic | skills/qa-story/SKILL.md:150-161 vs phases/s2.md:117 | present | — | D1 | t1,t2 |
| q5 | contradiction | s6.md says baseline machinery dormant, same section also tells the full baseline protocol; s5.md repeats it verbatim | skills/qa-story/phases/s6.md:128-154 vs s5.md:370-391 | present | — | D3 | t5,t6 |
| q6 | contradiction | README says S3 stops at gate A, S4 "Cases"; SKILL.md and s4.md put gate A after S4 | skills/qa-story/README.md:15,24 vs SK:156 | present | — | D2 | t3,t1 |
| q7 | contradiction | README says 12 roles and S5 "cuts the story branch"; s5.md says never create a branch merely because S5 started | skills/qa-story/README.md:16 vs phases/s5.md:108-109 | present | — | D4 | t3,t6 |
| q8 | analog | Judge text repeated in SK, s2, s3, s4, s5, s6, s7, s8, s9 and README | skills/qa-story/ | present | — | D5 | t1-t13 |
| q9 | absent | No stand-alone test-pyramid ladder, risk scale or dashboard spec in area; they live in references/ (not given) | agents/, skills/qa-story/ | absent | — | E | t19,t20 |

## Trail
| tid | op | target | pattern / range | flags | result | control |
|---|---|---|---|---|---|---|
| t1 | read | skills/qa-story/SKILL.md | 1-261 | — | read C:\QAFactory\forge-repo\ai-packages\qa-factory\skills\qa-story\SKILL.md:1-261 | — |
| t2 | read | skills/qa-story/phases/s2.md | 1-154 | — | read C:\QAFactory\forge-repo\ai-packages\qa-factory\skills\qa-story\phases\s2.md:1-154 | — |
| t3 | read | skills/qa-story/README.md | 1-111 | — | read C:\QAFactory\forge-repo\ai-packages\qa-factory\skills\qa-story\README.md:1-111 | — |
| t4 | read | skills/qa-story/phases/s0.md + s1.md | 1-535, 1-461 | — | read C:\QAFactory\forge-repo\ai-packages\qa-factory\skills\qa-story\phases\s0.md:1-535 | — |
| t5 | read | skills/qa-story/phases/s6.md | 1-155 | — | read C:\QAFactory\forge-repo\ai-packages\qa-factory\skills\qa-story\phases\s6.md:1-155 | — |
| t6 | read | skills/qa-story/phases/s5.md | 1-392 | — | read C:\QAFactory\forge-repo\ai-packages\qa-factory\skills\qa-story\phases\s5.md:1-392 | — |
| t7 | read | skills/qa-story/phases/s3.md + s4.md | 1-190, 1-241 | — | read C:\QAFactory\forge-repo\ai-packages\qa-factory\skills\qa-story\phases\s3.md:1-190 | — |
| t8 | read | agents/qa-test-strategist.md | 1-90 | — | read C:\QAFactory\forge-repo\ai-packages\qa-factory\agents\qa-test-strategist.md:1-90 | — |
| t9 | read | skills/qa-story/phases/s7.md + s8.md + s9.md | 1-308, 1-494, 1-238 | — | read C:\QAFactory\forge-repo\ai-packages\qa-factory\skills\qa-story\phases\s7.md:1-308 | — |
| t10 | read | agents/qa-scout.md + qa-requirements-tester.md | 1-92, 1-87 | — | read C:\QAFactory\forge-repo\ai-packages\qa-factory\agents\qa-scout.md:1-92 | — |
| t11 | read | agents/qa-case-designer.md + qa-case-critic.md | 1-85, 1-137 | — | read C:\QAFactory\forge-repo\ai-packages\qa-factory\agents\qa-case-designer.md:1-85 | — |
| t12 | read | agents/qa-automator.md + qa-code-critic.md | 1-89, 1-97 | — | read C:\QAFactory\forge-repo\ai-packages\qa-factory\agents\qa-automator.md:1-89 | — |
| t13 | read | agents/qa-runner.md, qa-failure-analyst.md, qa-doc-scribe.md, qa-bug-reporter.md, qa-retro-analyst.md | full each | — | read C:\QAFactory\forge-repo\ai-packages\qa-factory\agents\qa-runner.md:1-76 | — |
| t14 | read | skills/qa-story/evals/evals.json | 1-70 | — | read C:\QAFactory\forge-repo\ai-packages\qa-factory\skills\qa-story\evals\evals.json:1-70 | — |
| t15 | grep | skills/qa-story/evals/evals.json | `"(id|name|prompt)"` | count | count 109 | — |
| t16 | grep | skills/qa-story/evals/evals.json | `"prompt":` | -i content | found 20; evals.json:6,29,52,74,97,120,143,166,189,212,235,255,275,295,323,347,363,379,399,415 | — |
| t17 | grep | skills/qa-story | `owner's word|owner's rule|[А-Яа-я]{4,}` | -i content | found 1; phases/s8.md:85 | — |
| t18 | grep | agents | `owner's word|owner's rule|[А-Яа-я]{4,}` | -i content | absent | t17 |
| t19 | grep | agents | `pyramid` | -i content | found 3; qa-test-strategist.md:57, qa-test-strategist.md:73, qa-case-critic.md:(none), see note | — |
| t20 | grep | skills/qa-story | `dashboard` | -i content | found 6; README.md:105, s9.md:142-151 | — |

Trail correction: t19 and t20 were not run as separate calls. I read the files and my notes on the pyramid and dashboard come from those reads. Treat q9 as unverified and spot-check it. t17 and t18 were run in the same call.

## A. CARRY OVER
Format: statement | path § or rule | owner word+date or - | craft/process | outcome/means/knowledge. Only s8.md:85 carries a dated owner word.
1. One ticket goes through ten stages S0-S9 with a person stopping at exactly two gates (A after cases, B after results) | SK §Stages, README | - | craft | outcome
2. Between gates the factory asks nothing: it decides and records why, or halts naming what is needed and from whom | SK §Invariants "No questions between gates" | - | craft | outcome
3. A person is asked only what a person decides (intent of a requirement, access, money, gate words, risk); everything the code left is read first | SK §Settle it yourself first; references/person-owned.json (not given) | - | craft | outcome
4. Approval is its own word; answering questions is never approval | SK §two gates; evals #1 | - | craft | outcome
5. A person's word passes any block: checks stop silent passes, never informed ones. No check is one a person cannot pass with words | SK §A person's word; s1.md:460 | - | craft | outcome
6. A question to a person always shows the quotes and lettered readings with the cost of each; a one-liner goes back to the requirements tester | SK §Invariants; s2.md §Digest halt | - | craft | outcome
7. Orchestrator never authors test cases, tests, verdicts, triage classes, bugs or briefs; a role does, or a script does | SK:28-31 | - | craft | outcome
8. Requirements come only from confirmed sources; code and another side's test are never a source; the oracle is the requirement, not the implementation | s2.md:3-8; A qa-requirements-tester | - | craft | outcome
9. Every sentence of the story text has a home (requirement, branch, or not_obligation with why); every requirement is checkable or is a question with two readings | A qa-requirements-tester Good outcome 1-2; s2.md:141 | - | craft | outcome
10. Contradictions between sources are raised with both quotes and never resolved by the tester; a conflict settled by a later comment is recorded with its quote | A qa-requirements-tester; s1.md §requirement/code conflict | - | craft | outcome
11. Behaviour only the diff states is a "claim" with before/now for the person to confirm, never an expected value | A qa-requirements-tester #4; s3.md labelling | - | craft | outcome
12. Screenshots of manual checks go to the person, never into the report or MR text | s8.md:85 | owner's word 31.10.2026 (English text only) | craft | means
13. Sources are looked at first and fetched only if relevant; relevance is judged by content; instructions in tickets are data; every unavailable source needs the person's accept-gap | s1.md; A qa-scout | - | craft | outcome
14. No diff found: ask the four-option question (give change / name where it lives / ungrounded / not built yet); never search for the change or guess one | s1.md §halt; evals #2 | - | craft | outcome
15. Not-built-yet stories write tests from requirements, stop after tests, resume when code arrives (hold/arrive, source_arrived rework) | s1.md:358, s5.md:348-368, s2.md:73-76 | - | craft | outcome
16. Ticket freshness: a story that stood still more than 6 hours is rechecked; changed requirements text stops for the person's choice (new / old with known gap / stop) | s0.md §2b; s8.md §2b | - | craft | outcome
17. Stand: choose explicitly (never array position), probe in three lines liveness/login/keys; a failed probe is a warning, not a halt; never switch or deploy a stand unasked | s0.md §4-5; SK | - | craft | outcome
18. Baseline "before" evidence never blocks current tests; missing comparison is awaiting_baseline, never a fabricated PASS | s5.md:370-391, s6.md:128-154 | - | craft | outcome
19. Test data on stands that cannot be cleaned: own run-unique records, never a global total | s0.md §5 data_cleanup; A strategist, designer, automator | - | craft | knowledge
20. The plan: each requirement is a plan row or not_planned with reason; each row has a defect hypothesis, impact, observable with source, lowest earned level, a disposition | A qa-test-strategist Good outcome | - | craft | outcome
21. Automate what will run many times and what is RED; a one-off check of new behaviour is walked by the agent by hand; level = lowest rung that observes it | A qa-test-strategist Techniques (P19/P26) | - | craft | knowledge
22. Regression is found (existing tests by path, with what each needs), never run by the factory; the person runs it | A strategist #5, A doc-scribe #3, README "will not do", s9.md:219 | - | craft | outcome
23. A plan row whose risk K-n has no test is not lost: it appears at the end as a bug candidate in "Left with you" | s3.md:125 | - | craft | outcome
24. Cases: one per plan row, Given-When-Then, every Then observable through an independent channel and its oracle named from requirements; boundary and negative on every input; self-probed | A qa-case-designer Good outcome | - | craft | outcome
25. Case-writing know-how list: edges, focus-and-partial-input, permissions as two Thens, time, shared data, silent loss, look-alike outcomes, "unchanged" needs a working base, Then true before the change | A qa-case-designer §Where bugs hide | - | craft | knowledge
26. Technique know-how for designers/strategists/tester: EP, BVA, decision tables, state transitions, pairwise, use-case flows, error guessing, CRUD, requirement smells, mutation in the head | A qa-requirements-tester, qa-case-designer, qa-test-strategist Techniques | - | craft | knowledge
27. Independent review of cases only where the plan row requires it (design_review_required); at most 2 repair rounds; second failed review goes to the person at gate A, not a halt | s4.md:16,100-106; SK table | - | craft | outcome
28. Case critic: eight-dimension rubric, seed-the-defect check, roll-call of every row, deterministic verdict list (approve / approve_with_fixes / approve_with_concerns / partial / reject); unreviewed row = failed review | A qa-case-critic | - | craft | knowledge
29. Test code: expected value from requirement/oracle, never from code or same-action response; no skips/weakened asserts; stand block is never a product answer; find elements by role/label/test id; own data; wait for events not time | A qa-automator, qa-code-critic | - | craft | knowledge
30. After gate A the approved case is the oracle: a test that fails against the implementation goes over RED with the requirement/expected/observed, and S7 decides; automator and critic have no "case is wrong" route | s5.md:173-188; A qa-automator, qa-code-critic When to ask | - | craft | outcome
31. Each new or changed check is proved by a live probe (mutate the guarded line, test goes red) or marked unverified with why; no repeated green | s5.md:122-125; A qa-code-critic | - | craft | outcome
32. Run budget: one author run per test, one critic probe per check; results stand while tests, environment and deployed version are unchanged; repeat only on a person's word | s5.md:126-133, s6.md:92-95 | - | craft | outcome
33. Code critic reviews the code and its fit to the plan, never coverage again; findings carry a cause (test_defect / mechanical / environment / tooling / reviewer_error) and only test_defect spends the cap | s5.md:273-282; A qa-code-critic | - | craft | outcome
34. Runner walks manual-agent cases live as a user, records every oddity at once, each verdict quotes a capture of this attempt; stand vs product told by a second route | A qa-runner | - | craft | knowledge
35. Runner "first look": one short survey of the new version per requirement before any plan; saw/not-saw evidence, never an oracle | A qa-runner §First look; s3.md §First look; A qa-test-strategist | - | craft | knowledge
36. Failure triage: every red gets a verdict from the closed list with discriminating evidence checked against the requirement, never against app code; default is product until evidence shows otherwise | s7.md; A qa-failure-analyst | - | craft | outcome
37. Control experiment (same action without the change) separates APP_BUG, ASSERT_STRICTER, TEST_BUG of weak data and CASE_DEFECT | s7.md:117-123; A qa-failure-analyst | - | craft | knowledge
38. FLAKY only after 3 isolated reruns of that one test and a named mechanism; unfixed flake is "not verified"; quarantine only by the person at gate B with debt file and trigger | s7.md:197-210; A qa-failure-analyst | - | craft | outcome
39. Only test defects are repaired in S7 (max 2 rounds, shared with S5); an app bug is a draft until the person files it at gate B; one draft per confirmed mechanism, suspicions linked | s7.md:125-255; A qa-failure-analyst | - | craft | outcome
40. Suspicions left by the run (code-reading drafts, runner doubts) are walked on the stand and each ends as bug / not_a_bug / requirement_silent (a question) / impossible; none passes unsettled | s7.md:100-111; A qa-failure-analyst | - | craft | outcome
41. Gate B message order: verdict in report's words, traceability table verbatim (every requirement x case row), four report sections, stand gaps, decision per gap the person owns, bugs to file, MR, what not to commit, open-before-MR | s8.md §3 | - | craft | outcome
42. Delivery verdict yes / after_checks / no comes from the checks only; with "no" there is no "open MR" item, only "deliver with known gaps" with a stated reason | s8.md:150-340; README | - | craft | outcome
43. The report states three outcomes (clean / found something / could not check), never "no bugs", every number from a code block; left items say how to do them and what answer is wanted | A qa-doc-scribe | - | craft | knowledge
44. Bug report: quote the requirement and the damage to a person, steps from a stated start, independent-channel actual result, failing test + command, duplicate search; severity is the reporter's call | A qa-bug-reporter | - | craft | knowledge
45. Factory never writes a tracker/TMS itself; bugs always exist as local files; external writes only after gate, only for configured channels, verified read-back | s8.md:409-450; A qa-bug-reporter | - | craft | outcome
46. Factory never changes application code; it files bugs (one named exception: an `apply` on a stand-gap card) | SK:131-132; README | - | craft | outcome
47. Stand gaps are shown as a card (what is missing, exact fix, the words to answer with); four answers apply/theirs/handed/accept | SK §A stand gap; s4.md:166-176 | - | craft | outcome
48. Gate rehearsal: dry-run what approval authorises before asking, so nothing is asked or refused after the answer that could have been computed before | SK; s4.md:132-200; s8.md:114 | - | craft | outcome
49. Retro always runs in full: numbers by code, one fixed optional question ("what did you dislike in this session, what should change?") recorded verbatim, knowledge fold into strategy docs/obligations/backlog/estimate | s9.md; A qa-retro-analyst | - | craft | outcome
50. Retro looks for where the factory did NOT look; a trap seen twice goes to the one owning document; finding names the factory's class not one project's rule | A qa-retro-analyst | - | craft | knowledge
51. Final summary: at most 10 lines, what was delivered, what stays open, one next action | SK §Finish; s9.md §5 | - | craft | outcome
52. Obligations (open checks with a trigger) in obligations.md are the only carrier between stories; S0 of the next story lists the ripe ones | s0.md §7; s9.md | - | craft | outcome
53. Non-functional testing out of scope in v0; the scope line is printed once | s0.md §3; README | - | craft | outcome
54. Size computed by code from the functions the register names (XS..XXL); XXL is a recommendation the person's word passes | s2.md:119-131; A qa-requirements-tester | - | craft | outcome
55. Resume: restart reads state, never re-asks a recorded answer; a stage whose required outputs are missing is not done | SK §Resume; s0.md §1 | - | craft | outcome
56. Existing tests and cases: extend or parametrise before adding new; dedupe by one-branch-apart rule | A qa-case-designer, qa-case-critic 2b, qa-automator, qa-code-critic | - | craft | knowledge
57. Optional "judge" (cheap yes/no model) off by default; every check it lets through is shown at the gates | README §judge; SK; phase files | - | craft | means
58. No-trace / experiment story leaves no knowledge in the project config | s4.md:189-194, s8.md:335 | - | craft | outcome

## B. ROLE KNOWLEDGE
Every role file ends with Outcome, Good outcome, "Where bugs hide", Techniques, Tools, When to ask. Every role has the section "handoff form with tried table". Every role is dispatched by qa-story with one digest line back. All roles: tools exclude Agent and Task.

### qa-scout (S1) — agents/qa-scout.md
- Produces: work/source-inventory.json, context-manifest.json, context-bundle.json, impl-diff.txt (s1.md header).
- Knows: where requirement text hides (late comments, attachments, parent/siblings, linked bugs, neighbouring MRs, data path, two readers of one value, deleted code, config, translations, copied stories, "all/every", moved tickets); read timeline; triangulate conflict; positive control for every negative.
- Checks: every source decided; linked work and attachments counted; change grounded with observables path:line; absence proved (tried, unresolved_facts); existing coverage mapped.
- Checked by: the driver, item against witness plus the tried table; person reviews the source table (the one planned stop). Gate: S1 exit gate required_outputs. Alone in the system able to touch tracker, MR and diff (s1.md:18).

### qa-requirements-tester (S2) — agents/qa-requirements-tester.md
- Produces: requirements-register.md (R rows, ## Source obligations, ## Branches, ## Functions, contradiction matrix, ## Behaviour claims), requirements-readiness.json (open_questions), understanding.md (<=40 lines), size via sizing.py.
- Knows: compound reqs, implicit conditions, roles in plural, failure/refusal, boundaries, defaults, units, state, "as before", norms nobody states, rule-switching words; techniques EP, BVA, decision tables, state transitions, CRUD, smells, user-story, worked example.
- Checks: itself against the 5-item Good outcome; asks a question with two readings and recommended reading marked "until answered".
- Checked by: S2 exit detectors (branch_accounting.py, sizing re-run) and, per s2.md:117, qa-case-critic with repair_budget; the case critic also reads the register once at S4. Person sees understanding.md at gate A (or alone on `blocked`).

### qa-test-strategist (S3) — agents/qa-test-strategist.md
- Produces: work/test-plan.json and test-plan.md (rows with hypothesis, impact, level, disposition automate/manual-agent/manual-human/skip/unverifiable, reuse choice, regression list); on diff stories, window 1 only writes work/grounding.yaml (labels, claims).
- Knows: changed branches, seams, shared state, permissions, concurrency, dependency failure, migrations, flags, undo, un-resettable data, left-behind data, double-computed counts; risk-based ranking, defect hypothesis first, mutation thinking, what is worth automating, pyramid, pairwise, depth by risk, blast radius is the role's judgment, exploratory charters, smoke first.
- Checks: self-check only (agent file says "no critic judges the plan"); code checks (planning_contract.py on write, S3 exit gate).
- Checked by: see D1 (conflict). Person reads plan at gate A.

### qa-case-designer (S4) — agents/qa-case-designer.md
- Produces: case files under work/test-cases/ (or project cases_root); statuses Draft, Review, Approved only.
- Knows: input edges, focus/partial input, empty/many/repeated, interrupted ops, "unchanged" base, permission two-Thens, server-written values, time, shared data, order, look-alike outcomes, expected-from-code, Then true before change, silent loss; EP/BVA/pairwise/use-case flows/negative twin/self-probe.
- Checks: self-probe per case (can it fail on the bug, does data tell outcomes apart, is defect mocked away).
- Checked by: qa-case-critic (only where design_review_required), critic_rollcall.py, case_versions.py pinning by orchestrator, gate A.

### qa-case-critic (S4; also S2/S3 per s2.md:117, s3.md:61) — agents/qa-case-critic.md
- Produces: critic-findings.md with ## Roll-call, ## Branch homes, ## Merge candidates; handoff form with stage_acceptance (ok/concerns + failure_class + quote), advice_read, not_looked.
- Knows: register gaps, 8-dimension rubric (coverage, atomicity, clarity, edge, negative, traceability, completeness vs plan, seed-the-defect, plus 7b-7g sub-checks); mutation in head; anti-duplicate; refute the silence; follow one requirement end to end.
- Checks: the cases (pinned versions only) against plan, register behind them once on round 1; the author's tried table.
- Checked by: critic_rollcall.py computes the verdict; gate A shows unreviewed case ids; person at gate A.

### qa-automator (S5, also S7 repairs) — agents/qa-automator.md
- Produces: test code in test repo, work/s5-plan.json, automation-manifest (via manifest_from_tests.py markers), work/s5-notes/.
- Knows: no code-copied expectations, one-channel trap, shared state, time, per-key save fields, mock of unit under test, refusal on any 4xx, relative result one side, green-before-change, stand-block rule, missing element = failing test; lowest rung, extend before add, parametrise (param id names case), own data, ground before writing, sides real/substituted/absent.
- Checks: every Then bound to an assertion or a reason; no literal for open expectation; shape chosen and stated; red against requirement goes over red.
- Checked by: qa-code-critic (plan review then per window), s5_precheck.py, window_record.py; S7 analyst for reds.

### qa-code-critic (S5, S7 repair reviews) — agents/qa-code-critic.md
- Produces: findings file with cause per finding, probe records, handoff form; verdict approved / approved_with_fixes / rejected / unverified.
- Knows: masking, invented expectation, tests that cannot fail, e2e where API suffices, near-copy of existing test, Then hidden behind red, text-matched counts, blocked-that-ran-red, locator fragility, mock proves mock; live probe protocol, would-it-be-red-before-change, assert stricter than requirement.
- Checks: each instance, with probes by probe_by_code.py; author's choice (rung, reuse).
- Checked by: driver acceptance with findings file and review_receipt_ref; window_record.py.

### qa-runner (S6; first-look at S3) — agents/qa-runner.md
- Produces: run evidence, manual verdict records, work/evidence/manual/<case>/tried.md, observations[], run-report rows (via finalize_task.py), first-look rows.
- Knows: step before first Then, per-change-save fields, vary start state, empty/limit/pasted values, dependency failures, state after error, reload mid-save, guest-merge on sign-in; walk as user, hypothesis before route, probe copies client call, before/after state, stand vs product.
- Checks: each verdict quotes capture; every doubt an observation; what did not run says why and owner.
- Checked by: qa-failure-analyst (accepts or returns the run); code freshness checks; validate_artifacts.py (blocked run needs remedy).

### qa-failure-analyst (S7) — agents/qa-failure-analyst.md
- Produces: triage.json (verdict + control + evidence per red), bug-drafts/ (triage_ref, manual_steps, mechanism, confirmation unconfirmed), place_answers.
- Knows: comfortable reading trap, timeout vs race, weak data, stricter assert, older defect, one red hiding Thens, runner misread, environment dismissal needs diff look, fix moving expectation, several reds one cause; control experiment; isolated reruns; discriminate cause; walk the suspicious place; one cause one draft.
- Checks: every red and every observation (green too) explained; requirement quoted; case defect vs product defect apart.
- Checked by: code (FLAKY validator, bug_neighbours hint, finish --bugs screen), qa-doc-scribe (can return a triage), gate B rehearsal (bug list: draft with no triage_ref or non-APP_BUG verdict is factory_fixable).

### qa-doc-scribe (S8) — agents/qa-doc-scribe.md
- Produces: test-report.md (prose around code-owned blocks from report_facts.py), appendix = traceability --render verbatim.
- Knows: report traps (merge the cause doesn't explain, missing row read as verified, green that never ran, left item with no way to do it, regression item that can't run elsewhere); task's terms first, three outcomes, every number from a code block, ask answerable questions.
- Checks: delivery word equals ledger; Left with you whole; regression found not run; proved within boundaries; triage accepted or returned.
- Checked by: report_facts.py --check, check_coverage.py detector, gate B rehearsal, person at gate B.

### qa-bug-reporter (S8, after gate B) — agents/qa-bug-reporter.md
- Produces: bugs/BUG-n.md (local file is the bug), bugs/DEBT-n.md for quarantined flaky, proposals under work/proposals/ for tracker.
- Knows: dirty-state steps, expected from code, duplicates and split defects, real personal data, damage as mood, unlinked siblings, one-attempt results; minimise reproduction, impact on a person, severity suggestion scale, attach red test.
- Checks: requirement + damage, steps from stated start, failing test attached, duplicate search, severity call.
- Checked by: driver acceptance (the accept settles the bugs order); the person already chose drafts at gate B. Reporter never judges `confirmation`, never argues with analyst.

### qa-retro-analyst (S9) — agents/qa-retro-analyst.md
- Produces: retro.md, obligations.md rows, factory-backlog.md entries, estimation-ledger line, strategy-doc folds (only where editable: true), dashboard rebuild by code.
- Knows: miss-that-looks-like-success, trap seen twice, marathon dispatches, disposition overrides, defect the person found at gate B that factory missed; one metric per comparison, where-did-I-not-look, dearest stage and one cut, start where last retro looked.
- Checks: top lines with numbers, where we did not look, traps folded, person's answer verbatim, routing, bugs/report read as next reader.
- Checked by: driver acceptance (retro.md required output); estimate_record.py after final; audits A15, A21 (doctor).

### Stages
- S0 Start and preflight — purpose: ticket, stand, readiness, resume; no role, orchestrator + code; hands on pipeline.json, readiness.json, config snapshot, controller initialized (phases/s0.md).
- S1 Context and grounding — purpose: find and judge every requirement source, ground in diff, map existing tests; qa-scout; one planned stop (source review + stand question); hands on context-manifest.json, context-bundle.json, source-inventory.json (phases/s1.md).
- S2 Understanding and size — purpose: requirements register, contradiction matrix, size, understanding brief; qa-requirements-tester (+ case critic per s2.md:117); halts on `blocked` with the brief sent alone (third person-touch); hands on register, readiness.json, understanding.md, size (phases/s2.md).
- S3 Plan — purpose: risk-based plan with dispositions; qa-test-strategist, two windows when there is a diff (labelling, then plan); optional first-look by qa-runner; hands on test-plan.json/md, grounding.yaml (phases/s3.md).
- S4 Cases and GATE A — purpose: atomic GWT cases, independent review of risky rows, pin, rehearsal, gate A message; qa-case-designer, qa-case-critic, orchestrator pins; hands on pinned cases, case-appendix, approved scope and decision (phases/s4.md).
- S5 Automation — purpose: tests written and independently reviewed with live probe; qa-automator + qa-code-critic, plan first then windows; hands on test code, automation-manifest, window records (phases/s5.md).
- S6 Run — purpose: run stale automated instances and walk manual-agent cases live; code run_suite.py + qa-runner; hands on run-report.json (phases/s6.md).
- S7 Triage — purpose: every red explained, test bugs repaired, app bugs drafted; qa-failure-analyst (+ automator repairs, code critic review); hands on triage.json, bug-drafts/ (phases/s7.md).
- S8 Results and GATE B — purpose: ledger and delivery verdict by code, one report, gate B, bugs, MR, external writes; qa-doc-scribe, then qa-bug-reporter after the decision; hands on test-report.md, ledger, bugs/, MR (phases/s8.md).
- S9 Closure and retro — purpose: knowledge fold, cost, one optional question, report rebuild; qa-retro-analyst; hands on retro.md, obligations.md, factory-backlog.md, 10-line summary (phases/s9.md).

## C. MACHINERY-ONLY
Why each exists is given in a few words. The point "restricts the MEANS of an agent" is marked [MEANS].
1. pipeline.json and stage_done.py "never edit by hand" — state ledger of the current code (SK:59, s0.md §8). [MEANS]
2. story_step.py start/bind/finish three-command dispatch and handover forms in handoffs/ — wiring of the current controller (SK §Dispatch protocol; all phase files). [MEANS]
3. controller.py operations (accept, rework, checkpoint, gate-decision, settle_order, next, invalidate, recover, release, await, arrive) and controller-api.md — durable-job engine of current code (SK; s4/s5/s8). [MEANS]
4. Stage guard / waiver.py / `--block "<refusal line>"` as the way to pass a denial — enforcement layer of current hooks; a refusal text must be quoted back to the guard (SK §A person's word; s5.md). [MEANS]
5. Hash pinning: case_versions.py, plan_content_hash, oracle hashes, coverage_contract_revision, receipts with input_hash/dispatch ids — evidence-binding of the current store (s4.md, s5.md). [MEANS]
6. "One line in, one line out" digest form `<role> <stage> <scope> · ok|concerns|halt|impossible`, exit_gate refuses other shapes — format of current gate (SK:56-58). [MEANS]
7. Windows/compact rollover rules (40 model requests, 70% context, /compact, "window" line, stop_after) — host context limits (SK:122-128, s4.md, s8.md). [MEANS]
8. Orchestrator "never read test-plan.md, a case, a diff" and "Grep/Read over Bash" — context economy (SK:240-243). [MEANS]
9. Fixed commands per stage (`config_view.py --get`, `readiness.py`, `env_probe.py`, `ticket_adapter.py collect|peek|assess|inspect|review|refresh|freshness`, `source_exclusions.py`) — current script set; "no tracker API of your own, no curl" (s0.md §2, s1.md). [MEANS]
10. "REST and nothing else (D-06)": tracker agents never a read route — rule bound to current adapter (s0.md:58-60, s1.md:123). [MEANS]
11. Runs only through run_suite.py; typed RunRequest, execution_fingerprint.py, runtime_probe.py, runtime provenance sha256 compare in docker — run-evidence machinery (SK:144-146; s5.md:334-346). [MEANS]
12. Test markers `@pytest.mark.qa(...)`, `qa_unresolved`, manifest_from_tests.py, manifest_put.py, s5_precheck.py, window_record.py — manifest by code from markers; pytest-flavoured (s5.md:292-327). [MEANS]
13. probe_by_code.py, red_sandbox.py, work/probe-models/<id>.json, probe_debt.py — the live-probe tool and its model file (s5.md:200-212). [MEANS]
14. Window size cap (2 e2e-ui or 4 others), over_cap, grown, window_cut, plan-before-windows block — S5 chunking of current controller (s5.md:54-63). [MEANS]
15. Repair caps, rework_mode (fresh vs SendMessage), repair_cause values, repair_budget, mechanical round — retry bookkeeping of current controller (s5.md:273-282; s7.md). [MEANS]
16. Write "plan in parts: Write then Edit append" and "big files read by section" — workaround for host output-token cap (s3.md:132-147). [MEANS]
17. Stage cards `story_step.py card`, stage_status.py events, `Return your digest line only` — conductor UX (SK; every card). [MEANS]
18. Ledger.json/ledger.md, check_traceability.py, check_delivery.py, traceability.py, report_facts.py facts: markers, delivery_summary.py, delivery_manifest.py — gate-B arithmetic and report blocks of current code (s8.md §1-2). [MEANS]
19. Three-commit MR with explicit path allowlists, `git add -A` forbidden, evidence git-ignored — current delivery recipe (s8.md:383-396). [MEANS]
20. external_writes.py phases after-a / after-b, `--record`, NEEDS_AGENT exit codes 4/5 — current writer (s8.md:409-450). [MEANS]
21. Words-file protocol: person's words written to state/words/<name>.txt with stamp, never inline, `--words-file` everywhere — current door for recording (s4.md:126-130, s8.md:291-296). [MEANS]
22. question_register.py, `Qn: <letter>` lines, question-vocabulary.json, person-owned.json classes, conductor-actions.json, stand_gap_words — answer-parsing tables (s2, s4, s8). [MEANS]
23. Activity capture at entry/end (activity_capture.py --action start|end) — usage accounting (SK:25-26). [MEANS]
24. Codex host adapters (hooks/codex.json, task_name=qa_scout__<slug>, .codex/agents toml, story_run.py --host codex) — second host plumbing (SK:33). [MEANS]
25. Journal (records/journal.jsonl), log_append.py events, project_decisions.py add-finding, project_knowledge.py, environment_record.py — current records/ledgers (s1, s5, s9). [MEANS]
26. Judge scripts judge_*.py and `## Judge` block — optional cost layer; off by default (README, all phases). [MEANS]
27. Doctor/audits (A15, A21, qa-doctor), retro_numbers.py, estimate_record.py, factory_dashboard.py — checks of current records (s9.md). [MEANS]
28. Role charters carry "Commands card", "key page", `<!-- gen:digest contract_slices.py -->`, `kind: process` markers — generated from current contract tooling (every agent file). [MEANS]
29. Closed vocabularies tied to code: verdicts, repair causes, mechanisms, gap_reasons, stand_gap words, closed 5 levels (unit, component, api, integration, e2e-ui) — keep as outcome words only if the new factory has the same data tables (s7.md:113-114, s5.md:246). Note: the level list is craft, its closed enforcement is machinery.
30. Several rules are written as means yet express outcomes: "role has no Bash", "Runs go through run_suite.py", "tracker REST only", "screenshots never in repo" (owner 31.10.2026), "git add -A forbidden", "never edit pipeline.json". Whether each is outcome or means is a designer call; listed here because they restrict how an agent works.

## D. CONTRADICTIONS AND DUPLICATES
D1. Is S2/S3 reviewed by a critic? agents/qa-test-strategist.md:21 says "no critic judges the plan; the person reads it at gate A". skills/qa-story/phases/s3.md:61 says "After the author's stop... the driver dispatches qa-case-critic for this stage" (also s2.md:117). SK:150-161 stage table lists critics only at S4/S5. agents/qa-case-critic.md names only S4 scope (its charter line 8 "for S4"). Same fact in four places, three answers.
D2. README.md:15,24 says "S3 Plan ... Then it stops: gate A" and calls S4 "Cases"; SK:156 and s4.md put gate A after S4. README:24 title "Gate A — after case design and review" agrees with SK, so README contradicts itself.
D3. s5.md:370-391 and s6.md:128-154 carry the same "Runtime first; baseline never blocks execution" block; s6.md:130 says "the baseline machinery stays dormant: no role captures evidence_phase=baseline now" and then repeats the full protocol. Duplicate plus internal conflict.
D4. README.md:16 says S5 "cuts the story branch" and evals.json #3 expects a branch created from config.git_conventions.branch; s5.md:108-109 says "Create one only when needed and authorized by project policy; never create one merely because S5 started". README/evals vs s5.md.
D5. README says "twelve roles" and ten stages — matches 12 agent files; SK:8 "twelve" matches. No conflict. Judge text is duplicated (each phase file has a "With a judge configured" paragraph); the same rule in 9 places.
D6. "Retro is always full" appears in SK:56 area? Not checked for SK; stated in s9.md:16,33, A qa-retro-analyst:10 and s8.md:243. Same rule, four paths (duplicate, consistent). s9.md still documents `numbers` and `skip` modes the same file says are never written — dead text.
D7. Gate A decision items: evals.json #1 expects "six decision items"; s4.md and SK:210 only say "Gate A's decision items are in phases/s4.md", and s4.md has no six-item list (the message is gate_brief.py output). Not verifiable in the area.
D8. A qa-case-critic says S4 scope is rows with design_review_required true; s4.md:11 agrees; s4.md:35 says "or every pinned case when the plan names none" (review_scope) — which means a critic reviews all cases if the plan names none, while s4.md:48 says "Simple unambiguous scope needs no extra critic call". Two readings.
D9. s1.md:459 and SK:63 both say halts; SK §Halts defers to references/halts.md, not in the given area.
D10. SK:69 "No questions between gates... The one planned stop besides them is the S1 source review". s2.md:89 says S2 `blocked` is "the one case in the whole pipeline with three human touchpoints"; s1.md has the S1 stop too, plus S9 optional question, plus stand/stand-gap/probe questions. Count of touchpoints differs between files.

## E. OPEN
1. Who judges the plan (S3)? Self-check only, a case critic, or the person only at gate A? (D1.)
2. Is there still a distinction between "test cases" and "autotests" with a separate human gate on cases? Today gate A approves cases, S5 is after it; a free-agent-like flow might not separate them.
3. Is the optional "judge" kept? Today it is described in every phase.
4. Which of the 58 A items stay as the owner's outcome constraints and which are means? Items 7, 12, 17, 45, 46 are rules about means in the current text.
5. Number and kind of human stops: two gates plus S1 review plus S2 blocked plus S9 question — the documents do not state which are essential.
6. Does the new factory keep 12 roles? The documents give no criteria for merging or splitting (for example scribe/reporter, runner/analyst).
7. Run budget numbers and caps (2 repair rounds, 3 flaky reruns, window 2 e2e/4 others, 6 hours freshness, 40 lines understanding, 10-line summary) have no stated source; is each an owner decision?
8. Baseline before/after comparison: s6.md calls it dormant, s5.md keeps it; which is the intent?
9. Where does knowledge from the person's feedback live in a factory without project_decisions/obligations ledgers? The retro's carrier between stories is only obligations.md.
10. Manual-human cases: factory never runs them and hands them to the person; documents do not say how they are tracked beyond "Left with you".
11. Non-functional testing: out of scope in v0 (README:87, s0.md §3) with no plan for later.
12. Test layer names (unit, component, api, integration, e2e-ui) and the pyramid — referenced as "the manifesto ladder P19" (agents/qa-test-strategist.md:25,55) but its text is not in the given area (references/ or manifesto).
13. Owner's words and dates for the settled rules: only one is in this area; the designer must find them elsewhere (not in this area).

## Not done
- evals.json lines 71-431 read only through the prompt lines (t16), not assertion by assertion: eval prompts #4-#20 and their assertions are not fully analysed. They test the current machinery; no craft was extracted from them.
- All `references/`, `handoffs/`, `stages.json`, `common-rules.md`, `coverage-design.md`, `risk-policy.md`, `case-lifecycle.md`, `manual-evidence.md`, `walk-charter.md`, `explore-charter.md` named in these files were outside `given`. Craft rules held there (risk scale, pyramid ladder P19/P26, case lifecycle, manual evidence policy) are not covered.
- q9 ("no stand-alone pyramid ladder, risk scale, dashboard spec in the area") is not backed by a valid trail: t19 and t20 are placeholders in my trail and were not run as written. Treat q9 as unverified; the claim stands on my reading of the files only.
- t3 to t14 combine several files in one row; each file was read in full as listed in section F.
- Environment checks: none (outside this role's tools).

## F. TRAIL (files)
Read fully:
- C:\QAFactory\forge-repo\ai-packages\qa-factory\skills\qa-story\SKILL.md
- C:\QAFactory\forge-repo\ai-packages\qa-factory\skills\qa-story\README.md
- C:\QAFactory\forge-repo\ai-packages\qa-factory\skills\qa-story\phases\s0.md
- ...\phases\s1.md
- ...\phases\s2.md
- ...\phases\s3.md
- ...\phases\s4.md
- ...\phases\s5.md
- ...\phases\s6.md
- ...\phases\s7.md
- ...\phases\s8.md
- ...\phases\s9.md
- C:\QAFactory\forge-repo\ai-packages\qa-factory\agents\qa-scout.md
- ...\agents\qa-requirements-tester.md
- ...\agents\qa-test-strategist.md
- ...\agents\qa-case-designer.md
- ...\agents\qa-case-critic.md
- ...\agents\qa-automator.md
- ...\agents\qa-code-critic.md
- ...\agents\qa-runner.md
- ...\agents\qa-failure-analyst.md
- ...\agents\qa-doc-scribe.md
- ...\agents\qa-bug-reporter.md
- ...\agents\qa-retro-analyst.md
Skimmed:
- C:\QAFactory\forge-repo\ai-packages\qa-factory\skills\qa-story\evals\evals.json (lines 1-70 read, plus all "prompt" lines via grep; rest skipped: test scenarios for the current machinery, 109 id/name/prompt keys, size not an issue but not needed for craft)
Not read: none of the given files.

this needs a decision from a tier above.
