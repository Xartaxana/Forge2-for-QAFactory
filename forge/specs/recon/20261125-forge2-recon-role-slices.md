<!-- scout hand-back, journal task t-1892, recon for docs/tasks/specs/20261125-forge2-light-factory-plan.md; saved verbatim from the worker's final message -->

digest: v1 t-1882

Prefix: S/ = ai-packages/qa-factory/references/slices/ (repo root C:\QAFactory\forge-repo). The A-E blocks come before ## Objects because the form allows no other ## headings. No slice carries an owner's word or a date, so every "owner's word" cell below is "-". The one date, "2026-10-02", is a register cutoff in S/qa-requirements-tester/artifact-contract.md:51.

**A. CARRY OVER** (statement | path § heading | owner word | craft/process | outcome/means/knowledge)
A1 Every claim needs a witness: a path to recorded evidence plus minimal facts, never pasted stdout; an unwritten conclusion is an opinion | S/*/common-rules.md § The witness contract (all 12 roles) | - | craft | outcome
A2 The oracle is requirements or an approved decision; code and existing tests are observations only; current code never becomes the oracle for new behaviour | S/qa-case-critic/coverage-design.md § The oracle; S/qa-case-designer/vocabularies.md § Oracle basis (also scout, tester, case-critic copies) | - | craft | outcome
A3 Every numbered Then names where its expected value comes from (requirement/spec/precedent/person/unknown); an unknown oracle is asked, not guessed; "code" is not a source | S/qa-case-designer/artifact-contract.md § then_oracles form | - | craft | outcome
A4 A compound requirement is split into parts, each with its own evidence and gap; full only when every part is sufficient | S/qa-case-critic/coverage-design.md § Compound requirements and comparisons | - | craft | outcome
A5 Existing tests are judged by the assertions read, not by names, line coverage or an earlier green; prefer reuse, then extend/parameterize, then new | S/qa-case-critic/coverage-design.md § Reading existing candidates; S/qa-automator/test-code-patterns.md § Executable shape | - | craft | knowledge
A6 A level (unit/component/integration/api/e2e-ui) comes from the execution boundary, not from directory, language or page object | S/qa-case-critic/coverage-design.md § Levels by execution boundary | - | craft | knowledge
A7 "Nothing changed/leaked" claims need before-read, action, completion, after-read plus a separate mutating positive control; parity needs expected outcomes per input partition (equal 500s do not pass) | S/qa-case-critic/coverage-design.md § Observation contract; S/qa-test-strategist/handoff-keys-2.md § Not yet in rows | - | craft | knowledge
A8 Manual evidence: UI before+after images, API/CLI request+response+exit code; missing evidence is inconclusive, never pass; never fabricate screenshots; never weaken the policy after the run | S/qa-case-critic/coverage-design.md § Manual evidence policy; S/qa-runner/artifact-contract-run.md § run-report.json | - | craft | outcome
A9 A test creates and cleans its own data; "first available record" is an anti-pattern unless the project declared shared seeded data | S/qa-automator/common-rules.md § Your own test data (same in code-critic, case-critic, runner, failure-analyst) | - | craft | outcome
A10 A reviewed link is not verified until fresh execution evidence exists; stale or missing freshness is unverified, not green | S/qa-case-critic/coverage-design.md and S/qa-doc-scribe/coverage-design.md § Evidence freshness; S/qa-code-critic/execution-lifecycle.md § Requests, receipts and reuse | - | craft | outcome
A11 A value the requirement fixes is never changed after a red run; the test is handed over RED as contradicts_requirement; a value the author invented may change only with a recorded reason | S/qa-automator/handoff-keys-3.md § Not yet in rows; S/qa-code-critic/handoff-keys-2.md § Not yet in rows | - | craft | outcome
A12 Test-code design: a pattern answers a recurring symptom; decision ladder; symptom-to-pattern catalog; anti-pattern list (locators in test body, assertions in page objects, single-use abstraction, utils dump, retries in the test) | S/qa-automator/test-code-patterns.md § Principle/Decision ladder/Catalog/Anti-patterns; S/qa-code-critic/test-code-patterns.md (subset) | - | craft | knowledge
A13 The red line must name the Then (assert the count before unpacking); a relative result asserts both sides; cancelling actions assert after each action | S/qa-automator/test-code-patterns.md § The red line names the Then; § Executable shape | - | craft | knowledge
A14 A probe proves the check is live (assertion fails when made false); a deeper probe proves it catches a broken product; a probe whose mutation changes no behaviour is the probe's defect | S/qa-code-critic/execution-lifecycle.md § The probe is mechanical; S/qa-automator/artifact-contract-automation.md § Coverage v2 bindings | - | craft | knowledge
A15 FLAKY needs 3 or more isolated reruns and a mechanism; the fix targets the mechanism, never a retry; an unfixed flake is not verified and quarantine is the person's call | S/qa-failure-analyst/artifact-contract-run.md § FLAKY; S/qa-failure-analyst/handoff-keys-2.md § Not yet in rows | - | craft | knowledge
A16 ASSERT_STRICTER needs a control run of the action without the change; a verdict without evidence is invalid | S/qa-failure-analyst/artifact-contract-run.md § triage.json | - | craft | outcome
A17 A bug is a draft until someone reproduces it; it needs an oracle (else it is an observation), steps a person does, a red test, a confirmation level; severity derived from impact | S/qa-failure-analyst/artifact-contract-run.md § bug-drafts; S/qa-bug-reporter/handoff-keys.md § Not yet in rows; S/qa-failure-analyst/vocabularies.md § Bug confirmation | - | craft | outcome
A18 Report goes from the decision down for a reader who does not know the factory's words; an unverified green is "Left with you", not "Proven" | S/qa-doc-scribe/artifact-contract-results.md § test-report.md; S/qa-doc-scribe/handoff-keys-2.md § Not yet in rows | - | craft | knowledge
A19 Retro opens with 3-5 lines of number + diagnosis + change; unknown is written "unknown", never rounded; one fact belongs to one owning document | S/qa-retro-analyst/artifact-contract-results.md § retro.md; S/qa-retro-analyst/handoff-keys.md § Not yet in rows; S/qa-retro-analyst/artifact-contract.md § Strategy documents | - | craft | knowledge
A20 Empty is not clean: a zero run with preflight pass is refused; evidence is bound to the source SHA; regression is recommended, not executed in a feature run | S/qa-runner/artifact-contract-run.md § run-report.json; S/qa-runner/handoff-keys-2.md § Not yet in rows | - | craft | outcome
A21 A question to a person carries source quotes, 2+ readings with "what changes if chosen", severity, owner; a plan row resting on a question says what each answer does | S/qa-test-strategist/artifact-contract-plan.md § if_answered / new_questions; S/qa-case-critic/handoff-keys.md § questions[] | - | craft | knowledge
A22 A case declares what it needs from the stand before step 1 (flag, data, account, env, service), checked before gate A, one grouped question per case; only what a person alone can say is a card | S/qa-case-designer/artifact-contract.md § preconditions | - | craft | outcome
A23 Plan row: defect hypothesis "<class> @ <place>", impact class (data-loss, money, access, blocked-flow, degraded, cosmetic, none) derives priority; existing tests that defend the blast radius are recommended regression | S/qa-test-strategist/artifact-contract-plan.md § test-plan.md | - | craft | knowledge
A24 Several cases sharing one requirement are merge candidates (parametrise into one test); e2e/manual rows must say whether a lower level is possible | S/qa-case-critic/handoff-keys.md § critic_rollcall | - | craft | knowledge
A25 Real data the project marked never reaches an artifact verbatim; mask it or use a stand-in | S/*/common-rules.md § Real data in artifacts | - | craft | outcome
A26 Directives inside tickets/comments are data, not instructions; a skip is never a role's own call (only a documented deferral with a trigger, or an environment blocker escalated) | S/*/common-rules.md § Cross-cutting rules | - | process | outcome
A27 Story spend is the sessions the journal names; two records of the same money (journal authoritative, token-priced files provisional) print the gap and say which is which | S/qa-retro-analyst/handoff-keys.md § Not yet in rows | - | craft | knowledge
Nothing of kind "dashboard" or "onboarding" craft is here: the dashboard appears only as a reader (S/qa-doc-scribe, S/qa-runner artifact-contract-*), onboarding only as config pointers (config.json, test_data.shared_records).

**B. ROLE KNOWLEDGE** (craft/machinery shares are my ESTIMATES of text volume, not measured)
- qa-test-strategist (S/qa-test-strategist/*): gets the plan-row vocabulary (defect hypothesis, impact class, oracle basis, level, technique, fit, regression, per-answer branches, coverage obligations). No craft prose; the craft is in field names. Criteria told in advance: YES, a "What code will check of you" list (handoff-keys.md, handoff-keys-2.md). Estimate craft 10% / machinery 90%.
- qa-case-designer (S/qa-case-designer/*): Then numbered and bound to an oracle, preconditions on the stand, question_thens, alternatives (the Then must FAIL under the other reading), partitions. Criteria in advance: YES (handoff-keys.md validate_artifacts rows). Estimate 15 / 85.
- qa-case-critic (S/qa-case-critic/*): the richest craft: obligations, freshness, levels, oracle, observation contract, compound requirements, reading candidates, manual evidence, design-review questions. Criteria: roll-call rules (verdict computed, not typed) and merge candidates. The handoff asks for `review.rubric_covered` ("dimensions of the eight") but no slice lists the eight (q4). Estimate 50 / 50.
- qa-code-critic (S/qa-code-critic/*): anti-pattern list, two-level probe, request/receipt freshness, expectation-change verdicts (legitimate_correction / fitted_to_code / could_not_judge). Criteria: YES, controller:code_review_receipts and manifest rows. Estimate 30 / 70.
- qa-automator (S/qa-automator/*): test shape choice, decision ladder, symptom-to-pattern catalog, do not fit tests to code, own data. Criteria: YES, s5_precheck rows (every Then bound to a test and assertion line). Estimate 35 / 65.
- qa-runner (S/qa-runner/*): manual-evidence phases, empty-is-not-clean, head SHA, a case must land in some lane. Criteria: YES (check_run_report_* rows). Estimate 15 / 85.
- qa-failure-analyst (S/qa-failure-analyst/*): verdict taxonomy with evidence, control runs, FLAKY rule, bug-draft anatomy, one cause with several manifestations. Criteria: YES (check_triage_v0, binding). Estimate 35 / 65.
- qa-retro-analyst (S/qa-retro-analyst/*): findings first, numbers from code, unknown stays unknown, one fact one owner, knowledge fold. Criteria: little; retro.md "Validator none beyond language and size"; handoff claims only. Estimate 30 / 70.
- qa-doc-scribe (S/qa-doc-scribe/*): report order and reader-first rules, Proven vs Left with you. Criteria: YES, validator listed section by section (artifact-contract-results.md). Estimate 35 / 65.
- qa-bug-reporter (S/qa-bug-reporter/*): bug needs User impact + Initial state, oracle grammar, severity derived from impact. Criteria: YES (check_bug_form). Estimate 25 / 75.
- qa-requirements-tester (S/qa-requirements-tester/*): implementation-only requirement needs a before/now claim and a question, the answer (not the code) becomes the oracle; understanding.md at most 40 lines; register rules. Criteria: YES (exit_gate, check_register). Estimate 20 / 80.
- qa-scout (S/qa-scout/*): bounded coverage search that says it was bounded, source inventory with receipts, code/AC conflict decided by a person verbatim. Criteria: YES (check_context_manifest_v0). Estimate 10 / 90.
Across all roles: criteria ARE told in advance, but as validator/gate rows ("What code will check of you"), mixed with script names and field grammar. Only the strategist/designer/critic rows name outcomes in plain words (every requirement reaches a row, every Then has an oracle, verdict computed from roll-call). Role charters ("technique by its name in your charter") are not in the slices.

**C. MACHINERY-ONLY** (and means restrictions)
C1 Handoff form (`work/handoffs/<dispatch>.yaml`, handoff_check.py, values file, digest line shape) - exists for exit_gate code; in all handoff-keys*.md.
C2 Fixed artifact tree and names ("Names are fixed"), state/work/records split, cv_/ti_/TS-1-O1/OB-1 ids - serve contract.artifact() and validators; S/qa-case-designer/artifact-contract.md § Where artifacts live (6 copies).
C3 run_suite.py as the only way to run a test; direct pytest/npm test blocked; --mine/--request/--template/--recover; idempotency_key; profile_id; selector_args; fingerprint specs - S/qa-automator/execution-lifecycle.md, S/qa-code-critic/handoff-keys*.md. Restricts MEANS.
C4 manifest_put.py, s5_precheck.py, branch_accounting.py, critic_rollcall.py, case_versions.py pinning, probe_by_code.py, red_sandbox.py, report_facts.py rules - each exists to feed a checker.
C5 Role tool limits: "designer has no Bash", Edit of the form refused, whole read over 30 KB blocked, notice at 60 tool calls, "Bash only executes" - S/*/common-rules.md § Turn economy; S/qa-case-critic/case-lifecycle.md. Restrict MEANS.
C6 "Asks the human exactly twice per story" and "do not manufacture a question" - S/qa-case-critic/common-rules.md § Gates and halts (also automator, runner, retro, scribe, bug-reporter, failure-analyst, code-critic). Restricts MEANS (process shape).
C7 Absolute paths are a defect (audit A20); project root = nearest qa-factory/config.json; path frames table - S/*/common-rules.md § What a path is relative to.
C8 External writes only via proposal file + deterministic executor after gate B - S/qa-scout/common-rules.md, S/qa-requirements-tester/common-rules.md, S/qa-retro-analyst/common-rules.md, S/qa-bug-reporter/handoff-keys.md. Restricts MEANS for tracker writes.
C9 Pytest-specific rules (pytest.param markers, pytest.skip, collect-based node ids) - S/qa-automator/test-code-patterns.md; S/qa-code-critic/artifact-contract-automation.md § Typed ids.
C10 Size caps: understanding.md at most 40 lines, report prose under 6,144 bytes, status words closed in vocabularies.md - validator limits.
C11 Pre-checked counts of guard checks ("19 checks", "25 checks") - generated text.

**D. CONTRADICTIONS / DUPLICATES**
D1 Level vocabulary differs: plan table has unit/component/api/integration/e2e-ui (S/qa-test-strategist/artifact-contract-plan.md:34) while the strategist handoff form says unit|integration|api|e2e-ui|other (S/qa-test-strategist/handoff-keys.md:36); the traceability list adds manual-agent/manual-human (S/qa-doc-scribe/vocabularies.md:56).
D2 Triage verdicts: vocabularies list 10 values without NOT_EXECUTED (S/qa-failure-analyst/vocabularies.md:15, copies in retro/doc-scribe/bug-reporter) but check_triage_v0 and not_for_repair list NOT_EXECUTED (S/qa-failure-analyst/handoff-keys.md:47, handoff-keys-2.md:8).
D3 S/qa-case-critic/artifact-contract.md:118 says whether R supports a Then's value "is the case critic's call", but the then_oracles grammar is only in S/qa-case-designer/artifact-contract.md (lines 118-141): the critic is not given the rules it judges by.
D4 S/qa-code-critic/test-code-patterns.md says new patterns are "named from the vocabulary below", but this copy has no catalog (S/qa-automator/test-code-patterns.md has it): the critic counts anti-patterns without the vocabulary.
D5 Rule "asks the human exactly twice ... do not manufacture a question" (common-rules) against critics/strategist/designer writing questions[]/new_questions/raise_questions and gate_preflight asking "one grouped question per case" - tension, probably resolved by "questions surface at gate A"; the slices do not say so.
D6 Duplicated text: common-rules (12 copies, sections vary by role); Observable source vocabulary (scout, tester, designer, case-critic); Triage verdict vocabulary (failure-analyst, retro, doc-scribe, bug-reporter); Where artifacts live tree (designer, case-critic, tester, retro, doc-scribe, bug-reporter); test-code-patterns (automator, code-critic subset); artifact-contract-automation (automator, code-critic, failure-analyst subset); artifact-contract-run (runner, failure-analyst, doc-scribe); execution-lifecycle (automator, code-critic); coverage-design (case-critic, doc-scribe 619 B).
D7 index.md files list only artifact-contract*/vocabularies/coverage-design files, never handoff-keys*.md or common-rules.md, although those hold the "what code will check of you" criteria.

**E. OPEN (for a designer to ask the owner; no guess)**
E1 Where role charters live (technique names, "your charter") and the eight-dimension critic rubric: not in the slices.
E2 Whether two human gates stay, and how questions raised mid-story are held.
E3 Test pyramid targets: plan front matter has a "pyramid count" but no target proportion or rule appears in the slices.
E4 Cost: the plan "cap in work/sizing.json" and a case budget are mentioned; how a cap is set and what happens over it is not stated.
E5 Dashboard and onboarding content: only referenced.
E6 Who is "the person" (po_ba, dev_arch, qa) for each question class, and the severity thresholds blocker/major/minor.
E7 Whether manual-human and quarantine of flaky tests stay; the slices make both the person's call.
E8 Whether a role may run its own tests directly (the slices forbid it) and which stand/provenance checks are required.

## Objects
| id | kind | gist | paths | status | owner | links | ev |
|---|---|---|---|---|---|---|---|
| q1 | finding | Slices are 12 roles x 3-8 files; craft prose concentrated in coverage-design, test-code-patterns, artifact-contract-run | S/qa-case-critic/coverage-design.md:1-130 | found | — | q2 | t1,t2,t3 |
| q2 | finding | Every role slice ends with "What code will check of you": criteria told in advance, as gate rows | S/qa-test-strategist/handoff-keys.md:92-114 | found | — | q1 | t1,t4,t5 |
| q3 | finding | Only strategist/designer/critic criteria name outcomes in plain words; others are script/field names | S/qa-case-critic/handoff-keys.md:96 | found | — | q2 | t3,t4 |
| q4 | finding | Critic rubric of "eight" dimensions is referenced but not defined in any slice | S/qa-case-critic/handoff-keys.md:26 | absent | — | q5 | t6,t7 |
| q5 | analog | Strategist and designer charters ("technique by its name in your charter") also not in slices | S/qa-test-strategist/handoff-keys.md:76 | absent | — | q4 | t6,t7 |
| q6 | finding | No owner words or dated owner decisions appear in the slices | S/ | absent | — | — | t6,t7 |
| q7 | finding | Triage verdict vocabulary omits NOT_EXECUTED that triage checks use | S/qa-failure-analyst/vocabularies.md:15 | found | — | q8 | t4 |
| q8 | analog | Level vocabulary differs between plan table, handoff form and traceability | S/qa-test-strategist/handoff-keys.md:36 | found | — | q7 | t1 |
| q9 | finding | Critic copy of test-code-patterns lacks the catalog its rule points to | S/qa-code-critic/test-code-patterns.md:36 | found | — | q1 | t2 |

## Trail
| tid | op | target | pattern / range | flags | result | control |
|---|---|---|---|---|---|---|
| t1 | read | S/qa-test-strategist, qa-case-designer, qa-requirements-tester, qa-scout (all files, see F) | whole files | — | read S/qa-test-strategist/handoff-keys.md:1-114 | — |
| t2 | read | S/qa-code-critic, qa-automator (index, patterns, lifecycle, vocab, handoff-keys*) | whole files except tails, see F | — | read S/qa-automator/test-code-patterns.md:1-154 | — |
| t3 | read | S/qa-case-critic (index, common-rules, coverage-design, case-lifecycle, handoff-keys, artifact-contract 48-118) | see F | — | read S/qa-case-critic/coverage-design.md:1-131 | — |
| t4 | read | S/qa-failure-analyst, qa-runner (index, contracts, vocab, handoff-keys*) | see F | — | read S/qa-failure-analyst/handoff-keys.md:1-80 | — |
| t5 | read | S/qa-retro-analyst, qa-doc-scribe, qa-bug-reporter (see F) | see F | — | read S/qa-doc-scribe/artifact-contract-results.md:1-62 | — |
| t6 | grep | S/ | `owner|\b2026-\d\d-\d\d|[А-Яа-я]` | -i content glob=!**/handoff-keys*.md | found 29; S/qa-requirements-tester/artifact-contract.md:51 | — |
| t7 | grep | S/ | `rubric|eight dimensions|dimension` | -i content glob=!**/handoff-keys*.md | absent | t6 |
| t8 | glob | S/**/* | `ai-packages/qa-factory/references/slices/**/*` | files | found 76; 12 role folders | — |
| t9 | grep | S/**/common-rules.md | `^(#{1,4} |<!-- generated)` | count | count 139 | — |
| t10 | grep | S/qa-automator/artifact-contract-automation.md | `^#{1,3} ` | content | found 12; lines 2-162 | — |

## Forks
Whether the new factory keeps a roles-with-closed-forms model, or keeps the two-gate limit, or states criteria as outcomes instead of gate rows, is a design choice; the slices only supply the facts in A-E.
this needs a decision from a tier above.

## Not done
F. FILE TRAIL (all 76 files of the area; "full" = read to the end, "partial" = lines named, rest not read and presumed identical to a copy already read)
- qa-test-strategist: index, common-rules, artifact-contract-plan, handoff-keys, handoff-keys-2 - full.
- qa-case-designer: index, artifact-contract, common-rules, handoff-keys, vocabularies - full.
- qa-case-critic: index, common-rules, coverage-design, case-lifecycle, handoff-keys - full; artifact-contract lines 48-118 only (lines 1-47 skipped: same tree text as designer's); vocabularies - not read (listed by index at 1,443 B vs designer's 1,445 B; presumed same text).
- qa-code-critic: index, test-code-patterns, execution-lifecycle, artifact-contract-automation, handoff-keys, handoff-keys-2 - full; common-rules lines 1-70 only (tail is the shared handover/path/language block, seen in other copies).
- qa-automator: index, test-code-patterns, execution-lifecycle, vocabularies, handoff-keys-3 - full; common-rules 1-70 (tail shared); handoff-keys 1-75 (rest is generic gate rows seen elsewhere); handoff-keys-2 1-40 (the rest of its check rows not read); artifact-contract-automation: lines 118-167 read plus a heading grep, lines 1-117 not read (code-critic copy read instead; it ends at 160 not 167, so it is a near copy).
- qa-requirements-tester: all 6 files full.
- qa-scout: index, vocabularies, handoff-keys full; common-rules 1-60 (tail shared).
- qa-runner: index, artifact-contract-run, vocabularies, handoff-keys, handoff-keys-2 full; common-rules 1-60 (tail shared).
- qa-failure-analyst: index, artifact-contract-run, artifact-contract-automation, vocabularies, handoff-keys-2 full; handoff-keys 1-80 (generic rows after 80 not read); common-rules 28-67 only (lines 1-27 and 68+ not read).
- qa-retro-analyst: index, artifact-contract-results, vocabularies, handoff-keys full; artifact-contract lines 48-88 only (lines 1-47 skipped: tree text); common-rules 1-64 (tail shared).
- qa-doc-scribe: index, artifact-contract-results, coverage-design, vocabularies, handoff-keys-2 full; artifact-contract-run lines 40-87 only (1-39 is the run-report text read in runner copy); handoff-keys 1-70 (rest generic); artifact-contract lines 1-12 only (rest not read: tree and project-level text seen in other copies); common-rules 1-12 only.
- qa-bug-reporter: index, vocabularies, handoff-keys full; artifact-contract lines 46-68 only; common-rules 1-45 (tail shared).
Not done: generated/duplicate tails above were skipped to save budget, not for lack of it; the claim "identical" for them is by heading and size match, not line diff. Cyrillic absence (q6) rests on one case-folded grep with the alternation in t6 and the hook warned this tool does not fold Cyrillic reliably, so treat q6 as weak. Environment checks are outside this role's tools.
