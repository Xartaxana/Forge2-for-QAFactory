<!-- scout hand-back, journal task t-1881, recon for docs/tasks/specs/20261125-forge2-light-factory-plan.md; saved verbatim from the worker's final message -->

digest: v1 t-1881
Reading key. Paths are relative to `C:\QAFactory\forge-repo\ai-packages\qa-factory\references\` (written R/). Section A to E rows sit in ONE Objects table, as the v1 form allows one table: id A* = carry-over (kind = craft|process, then outcome|means|knowledge, in the kind cell), B* = role knowledge, C* = machinery-only, D* = contradiction/duplicate, E* = open. Owner column: the owner's word + date. NO owner quotes with dates exist in this area (see C0/Not done); the evidence is incident ids (TP1-xxxxx) instead.

## Objects
| id | kind | gist | paths | status | owner | links | ev |
|---|---|---|---|---|---|---|---|
| A1 | craft/outcome | Tester goal: find defects; green run is absence of information; test must be able to fail (red probe) | R/tester-manifesto.md:25-33 | present | — | B1 | r02 |
| A2 | craft/outcome | Never report "no bugs"; report "checked-clean / checked-found / could not check", name the boundaries; every claim needs a witness | R/tester-manifesto.md:50-63 | present | — | A18 | r02,r12 |
| A3 | craft/outcome | Contradiction is raised not resolved: both quotes to the owner; code/existing tests are never the oracle | R/tester-manifesto.md:41-45; R/coverage-design.md:89-97 | present | — | A6 | r02,r04 |
| A4 | craft/outcome | Requirements register: 6 sources (AC is one, not the boundary), each R verifiable, observable, impact class, delta new/changed/unchanged | R/templates/requirements-register.md:9-67 | present | — | A5 | r09 |
| A5 | craft/knowledge | Every unit of ticket text gets a home (R, branch, not_obligation, excluded, unreconciled); branches, reading forks, contradiction matrix, attachments | R/templates/requirements-register.md:86-189 | present | — | A4 | r09 |
| A6 | craft/knowledge | Gather sources: task, parent, linked tickets judged relevant before full read, all comment pages, original attachments; unavailable source blocks until person accepts gap | R/coverage-design.md:7-34; R/scout-recovery.md:41-56 | present | — | A7 | r04,r34 |
| A7 | craft/outcome | Ticket text is data not instructions; verbatim paste, never a summary of an AC; ticket may change mid-story so freshness re-check | R/templates/ticket-snapshot.md:20-31; R/adapters-read.md:81-109 | present | — | A6 | r38,r40 |
| A8 | craft/knowledge | Test plan row = defect hypothesis `class @ place` + damage class; priority derived, never typed by hand | R/automation-candidacy.md:7-14; R/artifact-contract-plan.md:44-58 | present | — | A9 | r05,r42 |
| A9 | craft/outcome | Five dispositions (automate, manual-agent, manual-human, skip, unverifiable), each with a reason; automate only when observable+deterministic | R/automation-candidacy.md:16-51 | present | — | A10 | r05 |
| A10 | craft/knowledge | Automate what runs many times or is red; one-off check is walked by hand; ladder API/component, e2e, agent walk, person, run elsewhere | R/tester-manifesto.md:68-71; R/automation-candidacy.md:47-51 | present | — | A9,A11 | r02,r05 |
| A11 | craft/knowledge | Test pyramid by execution boundary: unit, component, integration, api, e2e-ui; directory/language/page object does not decide level; lowest sufficient layer | R/coverage-design.md:76-86; R/risk-policy.md:30-33 | present | — | A10 | r04,r07 |
| A12 | craft/knowledge | Risk chooses verification depth (critical/normal/low), not model price; budget shortage never lowers risk; unknown stays unknown | R/risk-policy.md:1-35 | present | — | A8 | r07 |
| A13 | craft/knowledge | Reuse ladder before new code: reuse unchanged, extend/parameterize with demonstrated gap, else new at lowest layer; anti-patterns (title/URL/visibility-only) never automate | R/automation-candidacy.md:53-80 | present | — | A14 | r05 |
| A14 | craft/knowledge | Cases specify coverage, test methods are chosen separately: reuse/extend/parameterize/consolidate/new; case and autotest NOT 1:1; one obligation = one observable assertion | R/test-code-patterns.md:13-28; R/coverage-design.md:49-56 | present | — | A13,A15 | r29,r04 |
| A15 | craft/knowledge | Case form: numbered Then items, requirement and plan-row chain, per-Then oracle source; expected value from requirement, never from code | R/artifact-contract.md:54-78,127; R/vocabularies.md:38-56 | present | — | A14 | r43,r39 |
| A16 | craft/knowledge | Test-code craft: patterns only on a recurring symptom; refusal test must discriminate cause; assert both sides of relative results; no retries around asserts | R/test-code-patterns.md:7-160; R/code-review-rubric.md:42-84 | present | — | A17 | r29,r30 |
| A17 | craft/outcome | Every new/changed test is probed: assertion must fail for the intended reason; masking (skip, weakened assert, fit to code) is a fail | R/code-review-rubric.md:1-10,76-84 | present | — | A1 | r30 |
| A18 | craft/outcome | Evidence: a measured current-attempt record, before/after + completion proof, verbatim Then quotes from captures; missing evidence = inconclusive, never pass | R/manual-evidence.md:3-125; R/coverage-design.md:155-179 | present | — | A19 | r10,r04 |
| A19 | craft/outcome | Evidence policy per manual obligation: ui, api, cli, no_write (before and after state), static; never weakened after the run; never fabricate screenshots | R/coverage-design.md:155-172 | present | — | A18 | r04 |
| A20 | craft/knowledge | Exploration: hypothesis + oracle + refuting observation written BEFORE capture; one cell per call with a control; "nothing broke" needs the tried table | R/explore-charter.md:11-60 | present | — | B5 | r15 |
| A21 | craft/knowledge | Manual walk: type as a person types; stop on first deviation, look before acting; never resend unchanged steps; focus loss is a finding | R/walk-charter.md:14-27 | present | — | A20 | r17 |
| A22 | craft/outcome | Report written from the decision down: verdict, proven, bugs, left with you, skipped by plan, not proven + cost; code owns counts; no factory words | R/templates/test-report.md:3-34,91-170 | present | — | A23 | r08,r44 |
| A23 | craft/outcome | Report distinguishes proven vs reviewed-only vs not proven; a green test the critic could not verify is left with the person, never counted | R/templates/test-report.md:44-56 | present | — | A22 | r08 |
| A24 | craft/outcome | Question to a person: what was decided, why not derivable, ONE question, closed answers, how-to-answer block last, price per option (factory/you/story) | R/human-questions.md:20-40 | present | — | A25 | r03 |
| A25 | craft/knowledge | Person is told in the story's words: no field names, script names, plugin paths, row ids unexplained; measured failure TP1-13797 | R/human-questions.md:13-16,42-72 | present | — | A24 | r03 |
| A26 | craft/knowledge | Asking policy: ask only what a person owns (8 classes); between gates only halt on real blockers, otherwise decide and record reasoning | R/person-owned.json:4-13; R/common-rules.md:59-67; R/conductor.md:65-79 | present | — | A24 | r47,r12,r32 |
| A27 | craft/outcome | Questions list with sources quoted, >=2 readings each, what each answer does; a single reading is a decision not a question; no proposed default (TP1-15045) | R/templates/questions-for-owner.md:28-49 | present | — | D5 | r19 |
| A28 | craft/outcome | Plan view for the person: understanding.md (<=40 lines: verify / not verify / may touch / blocking questions) + plan brief (<=15 rows, grouped with "+N more") | R/templates/understanding.md:3-48; R/templates/plan-brief.md:3-33 | present | — | A22 | r18,r20 |
| A29 | craft/outcome | Stands: unsafe unless marked safe; env block owned by factory or user; every block carries a remedy (names only); no silent skip, only the person's "defer" | R/environments.md:12-16,40-52,76-95 | present | — | A30 | r13 |
| A30 | craft/knowledge | Own test data, deterministic and cleaned up; shared records only if project declared; real data masked in artifacts | R/common-rules.md:39-56; R/environments.md:68-74 | present | — | A29 | r12,r13 |
| A31 | craft/knowledge | Triage vocabulary APP_BUG/TEST_BUG/ENV_ISSUE/FLAKY etc.; FLAKY needs >=3 isolated runs + mechanism; bug draft carries red test + manual steps; confirmation levels | R/vocabularies.md:84-104; R/artifact-contract-run.md:62-124 | present | — | A32 | r39,r46 |
| A32 | craft/outcome | Bug is a draft until gate B; red test travels with the bug; factory never changes app code (P-00); never writes to trackers directly | R/tester-manifesto.md:5-17; R/external-writes.md:38-72 | present | — | A31 | r02,r41 |
| A33 | craft/knowledge | Metrics honesty: missing data never means zero/success; formula version, n, status on every value; red probes are proof not failures | R/metrics-contract.md:8-27; R/metrics/testing.md:5-115 | present | — | A34 | r26,r22 |
| A34 | craft/knowledge | Dashboard-side numbers: T01-T14 testing, A01-A10 automation, C01-C15 cost (tokens, USD, human wait, band vs actual, ROI), F01-F09 factory health | R/metrics/testing.md; R/metrics/automation.md; R/metrics/cost.md; R/metrics/factory.md | present | — | A33 | r22,r23,r24,r25 |
| A35 | craft/knowledge | Retro opens with 3-5 lines "what went wrong and what to do", numbers computed by code; one closing question to the human, quoted verbatim | R/templates/retro.md:11-56 | present | — | A34 | r21 |
| A36 | craft/outcome | Onboarding stores project answers (stands, test data strategy, DoD "when is a story tested"); unanswered topics become deferred decisions with `asked` text | R/templates/factory-backlog.md:35-58; R/automation-candidacy.md:34-37 | present | — | A29 | r37,r05 |
| A37 | craft/knowledge | Obligations ledger: what stays open between stories, concrete trigger event, status changes only with a witness | R/templates/obligations.md:9-34 | present | — | A36 | r36 |
| A38 | craft/knowledge | Oracle word list (requirement, spec, precedent, person, unknown); "code" is not an oracle word; unknown Then is never asserted, listed in "Left with you" | R/vocabularies.md:38-56 | present | — | A3 | r39 |
| B1 | role | All qa-* roles: manifesto + witness contract + closed vocabularies; checked by validators on write and by next role | R/tester-manifesto.md; R/common-rules.md:21-28; R/README.md:20-28 | present | — | A1 | r02,r12,r01 |
| B2 | role | qa-scout: source discovery, relevance before full read, MR evidence by route ladder; checked by person source review and S1 gate | R/coverage-design.md:7-44; R/mr-access-routes.md:7-27 | present | — | A6 | r04,r51 |
| B3 | role | qa-requirements-tester / strategist / case-designer / case-critic: register, plan rows, cases; critic roll-call must cover every row | R/artifact-contract-plan.md; R/case-lifecycle.md:12-28 | present | — | A8 | r42,r06 |
| B4 | role | qa-automator / qa-code-critic: reuse ladder, patterns, nine-dimension rubric, probe of every changed test | R/test-code-patterns.md; R/code-review-rubric.md:42-84 | present | — | A16 | r29,r30 |
| B5 | role | qa-runner / failure-analyst / bug-reporter / doc-scribe / retro-analyst: capture, triage, draft, report, retro | R/manual-evidence.md; R/artifact-contract-run.md:62-124; R/artifact-contract-results.md:20-90 | present | — | A18 | r10,r46,r44 |
| C0 | absent | NO owner quotes with dates anywhere in the .md files of this area; Cyrillic search found nothing (language rule: package is English) | R/ | absent | — | A1 | g3,g4 |
| C1 | machinery | Slice injection by role marker lines and 12 000-byte cap: serves the hook, not craft | R/README.md:3-18,48-56 | present | — | — | r01 |
| C2 | machinery | Handover forms, handoff_check/help, digest line, retry_reason vocabulary: role-to-role plumbing | R/handoffs.md; R/common-rules.md:70-92; R/vocabularies.md:127-145 | present | — | — | r35,r12,r39 |
| C3 | machinery | Controller/idempotency/expected_revision/dispatch liveness/Codex launch card: lifecycle writer internals | R/controller-api.md:5-30; R/codex-host.md:1-29; R/judge.md:6-52 | present | — | — | r53,r50,r27 |
| C4 | machinery | Artifact paths, fixed file names, work/ vs state/ vs records/, ledger.json owners, case-version pins | R/artifact-contract.md:10-46; R/artifact-contract-ledger.md:7-52; R/case-lifecycle.md:5-40 | present | — | — | r43,r48,r06 |
| C5 | machinery | Means-prescribing: all test launches via run_suite.py, manual_capture.py step list, pytest-flavoured markers; restricts HOW an agent tests | R/common-rules.md:31-37; R/manual-evidence.md:10-20; R/test-code-patterns.md:124-134 | present | — | A18 | r12,r10,r29 |
| C6 | machinery | Means-prescribing: ticket only via ticket_adapter.py, tracker write only via proposal file + executor, SSH vs API routes | R/adapters-read.md:8-80; R/external-writes.md:38-72; R/jira-direct-access.md:1-30 | present | — | A32 | r40,r41,r52 |
| C7 | machinery | Execution fingerprints, leases, scheduler, receipt import, runtime provenance probe: freshness plumbing | R/execution-lifecycle.md:64-150; R/environment-preparation.md:1-79 | present | — | A29 | r31,r28 |
| C8 | machinery | Conductor move table, halts table, waiver.py, words-file; stage S0-S9 + gates A/B state machine | R/conductor.md:15-45; R/halts.md:11-30; R/stage-model.md:7-31 | present | — | A26 | r32,r33,r14 |
| C9 | machinery | Judge (System One model) registry, shadow/on modes, typesafe provider: optional cost cutter | R/judge.md:55-145 | present | — | — | r27 |
| C10 | machinery | Closed ledger/traceability states, report facts markers, `report_facts.py` spans, cost-file fields, Jira createmeta | R/templates/test-report.md:20-31; R/metrics-contract.md:51-100; R/vocabularies.md:107-124 | present | — | — | r08,r26,r39 |
| C11 | machinery | Role charter form (6 sections, <=150 lines, kind markers, audit A19): how roles are authored | R/charter-form.md:1-49 | present | — | — | r16 |
| D1 | contradiction | Retro: conductor says retro always full, `retro_mode numbers\|skip` refused; templates/retro and results contract still offer numbers/skip | R/conductor.md:25; R/templates/retro.md:6-9; R/artifact-contract-results.md:67-70 | present | — | — | r32,r21,r44 |
| D2 | contradiction | Questions file: "silence adopts proposed working interpretation" vs "do not propose a working interpretation (TP1-15045)" in same file | R/templates/questions-for-owner.md:9-12,47-49 | present | — | A27 | r19 |
| D3 | contradiction | "Asks human exactly twice (gate A, gate B)" vs source review at S1, build/stand questions, S9 closing question | R/common-rules.md:59-62; R/coverage-design.md:23; R/templates/retro.md:51-54 | present | — | A26 | r12,r04,r21 |
| D4 | contradiction | Word `impact`: register column holds damage classes; risk-policy `impact` is low/moderate/severe; plan JSON key must be `impact_class` | R/templates/requirements-register.md:20,41; R/risk-policy.md:11-14; R/artifact-contract-plan.md:50 | present | — | A12 | r09,r07,r42 |
| D5 | duplicate | Evidence-policy list (ui/api/cli/no_write/static) stated in coverage-design, artifact-contract-plan and manual-evidence | R/coverage-design.md:155-172; R/artifact-contract-plan.md:67; R/manual-evidence.md:111-119 | present | — | A19 | r04,r42,r10 |
| D6 | duplicate | `execution_status` vocabulary identical in environments.md and vocabularies.md; "Degradation" section identical in adapters-read and external-writes | R/environments.md:58-66; R/vocabularies.md:74-79; R/adapters-read.md:159-166; R/external-writes.md:121-125 | present | — | — | r13,r39,r40,r41 |
| D7 | duplicate | Rules for questions to a person: human-questions.md and conductor.md item 4 both state them; regression "recommendation only" repeated in 4 files | R/human-questions.md:20-40; R/conductor.md:75-79; R/risk-policy.md:45; R/execution-lifecycle.md:157-161 | present | — | A24 | r03,r32,r07,r31 |
| D8 | contradiction | Language: references say everything written is English even for Russian tickets; chat with owner is Russian (CLAUDE.md) so owner-facing text rule is unspecified | R/common-rules.md:148-151 | present | — | E8 | r12 |
| E1 | open | Dashboard design is NOT in this area: README sends dashboard contracts to ../design/; only metric definitions here | R/README.md:57-59; R/metrics-contract.md:3-6 | absent | — | A34 | r01,r26,g5 |
| E2 | open | Documents do not say how many human gates a LIGHT factory keeps (twice vs fewer) nor which of S0-S9 stay | R/stage-model.md:7-18 | present | — | D3 | r14 |
| E3 | open | No stated default for owner-facing language of questions/reports (English-only rule vs owner chat in Russian) | R/common-rules.md:148-151 | present | — | D8 | r12 |
| E4 | open | Starter risk policy `factory-starter-v1` is named but its content lives elsewhere; which risk scale the new factory uses undecided | R/risk-policy.md:3-5 | present | — | A12 | r07 |
| E5 | open | Is red-probe/mutation proof of every test required in a light factory, or only for critical depth (risk-policy says critical mandatory)? | R/risk-policy.md:18-22; R/code-review-rubric.md:1-10 | present | — | A17 | r07,r30 |
| E6 | open | Which stands/surfaces (web, API, device) and which trackers/TMS the new factory must support; documents cover Jira, GitLab, Xray, TestRail, Zephyr | R/adapters-read.md:41-45; R/manual-evidence-app.md:1-6 | present | — | C6 | r40,r11 |
| E7 | open | Cost metrics (ROI, tokenomics bands, MMRE) need owner-supplied baselines; whether the new factory reports money at all is undecided | R/metrics/cost.md:109-123 | present | — | A34 | r24 |
| E8 | open | Test-report appendix (traceability per requirement x case) and "Left with you" form: keep verbatim or simplify - no owner statement found | R/templates/test-report.md:192-194 | present | — | A22 | r08 |

## Trail
| tid | op | target | pattern / range | flags | result | control |
|---|---|---|---|---|---|---|
| g1 | glob | ai-packages/qa-factory/references | `**/*.md` | glob=**/*.md | found 100; first 100 of 131 listed (rest via 2nd call) | — |
| g2 | grep | ai-packages/qa-factory/references | `.` | count glob=*.md | count 8577 | — |
| g3 | grep | ai-packages/qa-factory/references | `[а-яё]` | -i files glob=*.md | absent | g4 |
| g4 | grep | ai-packages/qa-factory/references | `gate a` | -i files glob=*.md | found 3; slices/qa-scout/handoff-keys.md | — |
| g5 | grep | ai-packages/qa-factory/references | `dashboard` | -i files glob=*.md | found 15; controller-api.md | — |
| g6 | grep | ai-packages/qa-factory/references | `^#{1,3} ` | content glob={artifact-contract*.md,controller-api.md,jira-direct-access.md,mr-access-routes.md,codex-host.md} | found 190; headings of contracts | — |
| g7 | grep | ai-packages/qa-factory/references | `owner'?s? (word\|said)\|the owner\|\b(TP1-\d+)\b.*(measured\|incident)` | -i count glob=*.md | count 7 | — |
| r01 | read | R/README.md | whole | — | read R/README.md:1-68 | — |
| r02 | read | R/tester-manifesto.md | whole | — | read R/tester-manifesto.md:1-81 | — |
| r03 | read | R/human-questions.md | whole | — | read R/human-questions.md:1-161 | — |
| r04 | read | R/coverage-design.md | whole | — | read R/coverage-design.md:1-198 | — |
| r05 | read | R/automation-candidacy.md | whole | — | read R/automation-candidacy.md:1-91 | — |
| r06 | read | R/case-lifecycle.md | whole | — | read R/case-lifecycle.md:1-62 | — |
| r07 | read | R/risk-policy.md | whole | — | read R/risk-policy.md:1-47 | — |
| r08 | read | R/templates/test-report.md | whole | — | read R/templates/test-report.md:1-195 | — |
| r09 | read | R/templates/requirements-register.md | whole | — | read R/templates/requirements-register.md:1-201 | — |
| r10 | read | R/manual-evidence.md | whole | — | read R/manual-evidence.md:1-127 | — |
| r11 | read | R/manual-evidence-app.md | whole | — | read R/manual-evidence-app.md:1-59 | — |
| r12 | read | R/common-rules.md | whole | — | read R/common-rules.md:1-181 | — |
| r13 | read | R/environments.md | whole | — | read R/environments.md:1-120 | — |
| r14 | read | R/stage-model.md | whole | — | read R/stage-model.md:1-31 | — |
| r15 | read | R/explore-charter.md | whole | — | read R/explore-charter.md:1-116 | — |
| r16 | read | R/charter-form.md | whole | — | read R/charter-form.md:1-50 | — |
| r17 | read | R/walk-charter.md | whole | — | read R/walk-charter.md:1-38 | — |
| r18 | read | R/templates/understanding.md | whole | — | read R/templates/understanding.md:1-49 | — |
| r19 | read | R/templates/questions-for-owner.md | whole | — | read R/templates/questions-for-owner.md:1-66 | — |
| r20 | read | R/templates/plan-brief.md | whole | — | read R/templates/plan-brief.md:1-33 | — |
| r21 | read | R/templates/retro.md | whole | — | read R/templates/retro.md:1-61 | — |
| r22 | read | R/metrics/testing.md | whole | — | read R/metrics/testing.md:1-116 | — |
| r23 | read | R/metrics/automation.md | whole | — | read R/metrics/automation.md:1-84 | — |
| r24 | read | R/metrics/cost.md | whole | — | read R/metrics/cost.md:1-124 | — |
| r25 | read | R/metrics/factory.md | whole | — | read R/metrics/factory.md:1-76 | — |
| r26 | read | R/metrics-contract.md | whole | — | read R/metrics-contract.md:1-101 | — |
| r27 | read | R/judge.md | whole | — | read R/judge.md:1-147 | — |
| r28 | read | R/environment-preparation.md | whole | — | read R/environment-preparation.md:1-119 | — |
| r29 | read | R/test-code-patterns.md | whole | — | read R/test-code-patterns.md:1-161 | — |
| r30 | read | R/code-review-rubric.md | whole | — | read R/code-review-rubric.md:1-127 | — |
| r31 | read | R/execution-lifecycle.md | whole | — | read R/execution-lifecycle.md:1-168 | — |
| r32 | read | R/conductor.md | whole | — | read R/conductor.md:1-100 | — |
| r33 | read | R/halts.md | whole | — | read R/halts.md:1-31 | — |
| r34 | read | R/scout-recovery.md | whole | — | read R/scout-recovery.md:1-57 | — |
| r35 | read | R/handoffs.md | whole | — | read R/handoffs.md:1-45 | — |
| r36 | read | R/templates/obligations.md | whole | — | read R/templates/obligations.md:1-34 | — |
| r37 | read | R/templates/factory-backlog.md | whole | — | read R/templates/factory-backlog.md:1-64 | — |
| r38 | read | R/templates/ticket-snapshot.md | whole | — | read R/templates/ticket-snapshot.md:1-61 | — |
| r39 | read | R/vocabularies.md | whole | — | read R/vocabularies.md:1-146 | — |
| r40 | read | R/adapters-read.md | whole | — | read R/adapters-read.md:1-166 | — |
| r41 | read | R/external-writes.md | whole | — | read R/external-writes.md:1-157 | — |
| r42 | read | R/artifact-contract-plan.md | 1-112 | — | read R/artifact-contract-plan.md:1-112 | — |
| r43 | read | R/artifact-contract.md | 1-130 | — | read R/artifact-contract.md:1-130 | — |
| r44 | read | R/artifact-contract-results.md | whole | — | read R/artifact-contract-results.md:1-91 | — |
| r45 | read | R/artifact-contract-first-look.md | 1-70 | — | read R/artifact-contract-first-look.md:1-70 | — |
| r46 | read | R/artifact-contract-run.md | 60-124 | — | read R/artifact-contract-run.md:60-124 | — |
| r47 | read | R/person-owned.json | 1-60 | — | read R/person-owned.json:1-16 | — |
| r48 | read | R/artifact-contract-ledger.md | whole | — | read R/artifact-contract-ledger.md:1-53 | — |
| r49 | read | R/artifact-contract-reference.md | whole | — | read R/artifact-contract-reference.md:1-29 | — |
| r50 | read | R/codex-host.md | whole | — | read R/codex-host.md:1-30 | — |
| r51 | read | R/mr-access-routes.md | 1-30 | — | read R/mr-access-routes.md:1-30 | — |
| r52 | read | R/jira-direct-access.md | 1-30 | — | read R/jira-direct-access.md:1-30 | — |
| r53 | read | R/controller-api.md | 1-30 | — | read R/controller-api.md:1-30 | — |
| r54 | read | R/artifact-contract-grounding.md | whole | — | read R/artifact-contract-grounding.md:1-34 | — |

## Not done
- NOT READ (data/schema, not craft): all `*.json` except person-owned.json (adapter-forms, agent-labels, ..., judgments*.json, record-schemas.json, tokenomics-baseline.json, verification-levels.json, manual-policy-by-level.json, report-cures.json, risk/question thresholds ...). The given scope was .md; about 55 json files, one C-class line: they are data shapes serving the scripts. Names such as `question-thresholds.json`, `report-cures.json`, `manual-policy-by-level.json` may hold craft numbers; a follow-up read is needed if the owner wants them.
- SKIMMED by headings only (g6, no bodies): `artifact-contract-json.md`, `artifact-contract-automation.md` (headings + slice copies), `artifact-contract.md` lines 130-end, `artifact-contract-plan.md` 112-139, `artifact-contract-run.md` 1-59 and 125-end, `artifact-contract-first-look.md` 70-end, `controller-api.md` 30-end, `mr-access-routes.md` 30-end, `jira-direct-access.md` 30-end. Reason: schema/plumbing; they only restate fields. Not read in any form: `halts` beyond table is fully read; `references/handoffs/` folder etc. is outside references.
- Not read: the `slices/` subfolder (another scout), subfolders `templates/config.json`, `templates/readiness.json`, `external-dependencies/playwright-cli.json`, `judgments.d/*.json`, `metrics/catalogue.json` (json; the glob listing was cut at 100 of 234, a second `.md` glob shows 31 md files unlisted; the remaining md names came from grep g2 and were read or are slices). I did not open `README.md`-named `templates/config.json` to check it exists.
- Not covered: the dashboard (design/ folder, README says so); `ai-packages/qa-factory/design/factory-rules.md` (FR-1..FR-44) and the agent charters `agents/*.md` hold the rest of the role craft; the owner's words and dates are not in this area (g3 empty; control g4 differs in pattern, and `-i` may not fold Cyrillic: weak negative, hence also read in files: no Russian text seen in any of 54 files read).
- Fix-the-class (rule 8) analogs seen near the question: duplicates D5-D7 are the same class (a rule stated in 2-4 files; README claims "one owner per fact, audit A21"). No further search was run.
