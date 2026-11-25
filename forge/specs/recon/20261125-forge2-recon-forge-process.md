<!-- scout hand-back, journal task t-1886, recon for docs/tasks/specs/20261125-forge2-light-factory-plan.md; saved verbatim from the worker's final message -->

digest: v1 t-1886

## Objects
| id | kind | gist | paths | status | owner | links | ev |
|---|---|---|---|---|---|---|---|
| q1 | absent | PROCESS holds no scout golden set and no critic exam file; README says both are generated at onboarding | C:\QAFactory\forge-repo\PROCESS | absent | — | q9 | r14,r15,r16,r1 |
| q2 | absent | No PROCESS text or calibration check names CRAP, lint ratchet, dup/clone ratchet. They live in SIBLING_MAP axes 6/18/34 and RUNBOOK §7 | C:\QAFactory\forge-repo\PROCESS | absent | — | q11 | r32,r33,r20,r22,r25,r31 |
| q3 | fact | Weekly protocol has 52 numbered checks (1-52); 39 and 40 exist; weekly, run by an Architect session | PROCESS/WEEKLY_CALIBRATION_PROTOCOL.md:1-1214 | present | owner's word 17.11.2026 (who runs it) | — | r2,r3 |
| q4 | fact | SIBLING_MAP holds 42 axes; axes 41-42 sit after the «Keeping the map up to date» section | docs/SIBLING_MAP.md:691-725 | present | — | — | r17,r26 |
| q5 | fact | Lead ranking exam (6 cases, 12 points) has an empty Runs log; trigger is manual | PROCESS/LEAD_RANKING_EXAM.md:168-174 | present | — | — | r6 |
| q6 | fact | Deployment economy exam (3 arms A/B/C) has an empty Runs table; small exam each cycle, large per release | PROCESS/DEPLOYMENT_ECONOMY_EXAM.md:294-298 | present | — | — | r7 |
| q7 | analog | WEEKLY numbering note calls checks 15/17 "reserved placeholders"; check 41 says 39/40 "reserved, not on main". All four exist as full checks | PROCESS/WEEKLY_CALIBRATION_PROTOCOL.md:716-719,1163 | present | — | q3 | r3 |
| q8 | analog | Check 31 says the owner reads the pipeline "on GitLab, project 100001"; RUNBOOK §7 says CI is GitHub Actions; check 33(f) says the GitLab board is off | PROCESS/WEEKLY_CALIBRATION_PROTOCOL.md:1025-1027,1081-1085 | present | owner's word 04.11.2026 (board off) | — | r3,r33,r29 |
| q9 | analog | Check 14 demands Runs-log lines in the scout/critic exam files for role-file edits; Axis 2 says those exams are "not registered in this deployment" | PROCESS/WEEKLY_CALIBRATION_PROTOCOL.md:456-477; docs/SIBLING_MAP.md:49-50 | present | — | q1 | r2,r19 |
| q10 | analog | Judge protocol (13/13 bar) is intact while check 20 says rule 13 is "not used in this deployment" (owner's word 11.11.2026) | PROCESS/JUDGE_CALIBRATION_PROTOCOL.md:77-111; PROCESS/WEEKLY_CALIBRATION_PROTOCOL.md:725-732 | present | owner's word 11.11.2026 | — | r3,r4 |
| q11 | fact | CRAP ratchet: one predicate `crap_ratchet.complexity_offenders`; nightly job `crap-measure` plus a branch step in forge-check; baseline file born by the Lead's `--update` | docs/SIBLING_MAP.md:173,402,608 | present | — | q2 | r20,r22,r25 |
| q12 | analog | RUNBOOK §9.1(i) runs the full `selftest.py` locally ("integration run"); CLAUDE.md hygiene pt.1 says full sets run on CI, never on this machine | docs/RUNBOOK.md:268-273 | present | — | — | r29 |

## Trail
| tid | op | target | pattern / range | flags | result | control |
|---|---|---|---|---|---|---|
| r1 | read | C:\QAFactory\forge-repo\PROCESS\README.md | 1-100 | — | read C:\QAFactory\forge-repo\PROCESS\README.md:1-100 | — |
| r2 | read | C:\QAFactory\forge-repo\PROCESS\WEEKLY_CALIBRATION_PROTOCOL.md | 1-621 | — | read C:\QAFactory\forge-repo\PROCESS\WEEKLY_CALIBRATION_PROTOCOL.md:1-621 | — |
| r3 | read | C:\QAFactory\forge-repo\PROCESS\WEEKLY_CALIBRATION_PROTOCOL.md | 622-1214 | — | read C:\QAFactory\forge-repo\PROCESS\WEEKLY_CALIBRATION_PROTOCOL.md:622-1214 | — |
| r4 | read | C:\QAFactory\forge-repo\PROCESS\JUDGE_CALIBRATION_PROTOCOL.md | 1-112 | — | read C:\QAFactory\forge-repo\PROCESS\JUDGE_CALIBRATION_PROTOCOL.md:1-112 | — |
| r5 | read | C:\QAFactory\forge-repo\PROCESS\ARCHITECT_START.md | 1-63 | — | read C:\QAFactory\forge-repo\PROCESS\ARCHITECT_START.md:1-63 | — |
| r6 | read | C:\QAFactory\forge-repo\PROCESS\LEAD_RANKING_EXAM.md | 1-175 | — | read C:\QAFactory\forge-repo\PROCESS\LEAD_RANKING_EXAM.md:1-175 | — |
| r7 | read | C:\QAFactory\forge-repo\PROCESS\DEPLOYMENT_ECONOMY_EXAM.md | 1-307 | — | read C:\QAFactory\forge-repo\PROCESS\DEPLOYMENT_ECONOMY_EXAM.md:1-307 | — |
| r8 | read | C:\QAFactory\forge-repo\PROCESS\PATCH_PROTOCOL.md | 1-32 | — | read C:\QAFactory\forge-repo\PROCESS\PATCH_PROTOCOL.md:1-32 | — |
| r9 | read | C:\QAFactory\forge-repo\PROCESS\BOOT_REPORT_PROTOCOL.md | 1-68 | — | read C:\QAFactory\forge-repo\PROCESS\BOOT_REPORT_PROTOCOL.md:1-68 | — |
| r10 | read | C:\QAFactory\forge-repo\PROCESS\DOCUMENTATION_PROTOCOL.md | 1-11 | — | read C:\QAFactory\forge-repo\PROCESS\DOCUMENTATION_PROTOCOL.md:1-11 | — |
| r11 | read | C:\QAFactory\forge-repo\PROCESS\PRE_COMMIT_PROTOCOL.md | 1-38 | — | read C:\QAFactory\forge-repo\PROCESS\PRE_COMMIT_PROTOCOL.md:1-38 | — |
| r12 | read | C:\QAFactory\forge-repo\PROCESS\SESSION_PROTOCOL.md | 1-28 | — | read C:\QAFactory\forge-repo\PROCESS\SESSION_PROTOCOL.md:1-28 | — |
| r13 | read | C:\QAFactory\forge-repo\PROCESS\ZERO_CONTEXT_PROTOCOL.md | 1-29 | — | read C:\QAFactory\forge-repo\PROCESS\ZERO_CONTEXT_PROTOCOL.md:1-29 | — |
| r14 | glob | C:\QAFactory\forge-repo | `PROCESS/**/*` | — | found 12; PROCESS\README.md, PROCESS\WEEKLY_CALIBRATION_PROTOCOL.md | — |
| r15 | glob | C:\QAFactory\forge-repo | `PROCESS/*GOLDEN*` | — | absent | r16 |
| r16 | glob | C:\QAFactory\forge-repo | `PROCESS/*EXAM*` | — | found 2; PROCESS\DEPLOYMENT_ECONOMY_EXAM.md, PROCESS\LEAD_RANKING_EXAM.md | — |
| r17 | grep | C:\QAFactory\forge-repo\docs\SIBLING_MAP.md | `^#{1,3} ` | content | found 44; docs/SIBLING_MAP.md:1, docs/SIBLING_MAP.md:24 | — |
| r18 | read | C:\QAFactory\forge-repo\docs\SIBLING_MAP.md | 1-120 | — | read C:\QAFactory\forge-repo\docs\SIBLING_MAP.md:1-120 | — |
| r19 | read | C:\QAFactory\forge-repo\docs\SIBLING_MAP.md | 116-145 | — | read C:\QAFactory\forge-repo\docs\SIBLING_MAP.md:116-145 | — |
| r20 | read | C:\QAFactory\forge-repo\docs\SIBLING_MAP.md | 164-187 | — | read C:\QAFactory\forge-repo\docs\SIBLING_MAP.md:164-187 | — |
| r21 | read | C:\QAFactory\forge-repo\docs\SIBLING_MAP.md | 188-199 | — | read C:\QAFactory\forge-repo\docs\SIBLING_MAP.md:188-199 | — |
| r22 | read | C:\QAFactory\forge-repo\docs\SIBLING_MAP.md | 398-411 | — | read C:\QAFactory\forge-repo\docs\SIBLING_MAP.md:398-411 | — |
| r23 | read | C:\QAFactory\forge-repo\docs\SIBLING_MAP.md | 480-487 | — | read C:\QAFactory\forge-repo\docs\SIBLING_MAP.md:480-487 | — |
| r24 | read | C:\QAFactory\forge-repo\docs\SIBLING_MAP.md | 574-591 | — | read C:\QAFactory\forge-repo\docs\SIBLING_MAP.md:574-591 | — |
| r25 | read | C:\QAFactory\forge-repo\docs\SIBLING_MAP.md | 601-612 | — | read C:\QAFactory\forge-repo\docs\SIBLING_MAP.md:601-612 | — |
| r26 | read | C:\QAFactory\forge-repo\docs\SIBLING_MAP.md | 691-712 | — | read C:\QAFactory\forge-repo\docs\SIBLING_MAP.md:691-712 | — |
| r27 | grep | C:\QAFactory\forge-repo\docs\RUNBOOK.md | `^#{1,4} ` | content | found 30; docs/RUNBOOK.md:1, docs/RUNBOOK.md:5 | — |
| r28 | read | C:\QAFactory\forge-repo\docs\RUNBOOK.md | 1-190 | — | read C:\QAFactory\forge-repo\docs\RUNBOOK.md:1-190 | — |
| r29 | read | C:\QAFactory\forge-repo\docs\RUNBOOK.md | 190-436 | — | read C:\QAFactory\forge-repo\docs\RUNBOOK.md:190-436 | — |
| r30 | read | C:\QAFactory\forge-repo\docs\RUNBOOK.md | 437-516 | — | read C:\QAFactory\forge-repo\docs\RUNBOOK.md:437-516 | — |
| r31 | read | C:\QAFactory\forge-repo\docs\RUNBOOK.md | 580-681 | — | read C:\QAFactory\forge-repo\docs\RUNBOOK.md:580-681 | — |
| r32 | grep | C:\QAFactory\forge-repo\PROCESS | `crap|lint_ratchet|dup_ratchet|clone ratchet` | -i content | absent | r33 |
| r33 | grep | C:\QAFactory\forge-repo\PROCESS | `GitLab` | -i content | found 4; PROCESS\WEEKLY_CALIBRATION_PROTOCOL.md:1026, PROCESS\WEEKLY_CALIBRATION_PROTOCOL.md:1082 | — |
| r34 | grep | C:\QAFactory\forge-repo\PROCESS | `dry.story|dry_story|сухая стори|сухая история` | -i content | found 1; PROCESS\WEEKLY_CALIBRATION_PROTOCOL.md:1183 | — |
| r35 | grep | C:\QAFactory\forge-repo\docs\SIBLING_MAP.md | `слово владельца|owner's word|owner's words` | -i count | count 8 | — |

## Forks
E. OPEN: what a forge2 designer would have to ask the owner (no answers guessed).
1. The documents never sort the 52 checks into "protects an outcome" and "polices a tool". Which of them forge2 carries is not stated anywhere I read.
2. The scout and critic exams are generated, not registered here (q1, q9). The Lead-ranking and economy exams have empty run logs (q5, q6). Whether forge2 has role exams at all, and whether "evals" means these exams, is not settled.
3. The judge path (rule 13, `gateway/judge_calibration.json`) is dormant by the owner's word of 11.11.2026 (q10). The documents do not say whether it is dropped or kept.
4. The CRAP, lint and clone ratchets are described only as mechanisms (SIBLING_MAP axes 6/18/34, RUNBOOK §7). No threshold value or "which tool" decision is in my files. The CRAP baseline file is "born by the Lead's `--update` (card B3), absent before" (axis 18). Whether it exists now is not stated.
5. The 60-minute canon norm is "measured in the first week on GitHub (FK-4)" (RUNBOOK §7). No result is recorded in my files.
6. The Architect tier (Fable) is named as the calibrator (checks 49, 52, ARCHITECT_START). Whether forge2 keeps a third tier is not settled.
7. RUNBOOK §9.1(i) allows a full local `selftest.py` integration run. CLAUDE.md pt.1 forbids full local sets (q12). Which rule governs forge2 is not settled.
8. Several RUNBOOK §9 steps are marked "не проверено на живом прогоне": the `Start-Process` form, the `recover` restart, `Get-Process`. The live-run procedure is partly unverified.
9. A release needs "сухая стори зелёная" and `scoreboard.py release-check`. The PROJECT.md «Релиз» line is "NOT written yet (held for the owner: boot budget)" (check 47). The release gate is therefore not fully written down.
this needs a decision from a tier above.

## Not done
- The dispatch's sections A-D are below; the form has no section for them. Their pipe lines sit outside the Objects and Trail tables on purpose.
- F (trail by file): every PROCESS file was read fully (r1-r13). The weekly protocol was read in two pages, lines 1-621 and 622-1214.
- `docs/RUNBOOK.md` was read in full, except lines 517-579 (§10.4 tail and §10.5, a cache-measurement printout) and lines 682-end, which do not exist (the file ends at 681). §10.5 was skimmed by its heading (r27) only.
- `docs/SIBLING_MAP.md` was read as headings (r17), intro and axes 1, 5-7, 18, 31-32, 34 and the maintenance section.
- Axes 2-4 and 8-17, 19-30, 33, 35-42 were not read row by row, as the dispatch allowed; their gist comes from heading titles only. Hence D's grouping rests on the headings alone for those axes.
- Not checked because outside the given files: the CLAUDE.md-side texts, `tools/*` code, PROJECT.md, `docs/TESTING.md`. I did not verify that any tool, workflow or job named below exists; every carrier is quoted from the documents. I did not verify the "dry-story.yml" or "nightly.yml" job lists beyond what RUNBOOK §7 and axis 6 say.
- Context stayed well under the 220K stop.

### A. CARRY OVER (lesson | path § / check | owner's word + date, or - | craft/process | outcome/means/knowledge)
1. A new exam, judge or metric is calibrated on a known-tier control first; saturation by a lower tier means it does not rank | JUDGE_CALIBRATION rule 7; LEAD_RANKING rule 4 and K4 | - | process | outcome
2. An exam that needs the host's own material ships as a generator; with too little material it is deferred (visible), not faked | PROCESS/README § Delivery form; § Empty project | - | process | outcome
3. The delivery policy is measured against a clean model and a "good prompt" arm; price per accepted task; keys pinned at intent level before the run | DEPLOYMENT_ECONOMY_EXAM § Three arms, § Metrics | - | process | outcome
4. Underspecified exam tasks; a clarifying question back to the user counts as a positive | DEPLOYMENT_ECONOMY_EXAM § Tasks req. 2 | - | craft | knowledge
5. A mechanism that promises detection registers its detector in the same commit, else it is a wish | WEEKLY intro; check 8 | - | process | outcome
6. Calibration cannot detect its own absence, so an external line flags it OVERDUE after 7 days | BOOT_REPORT rule 5; WEEKLY § Closing out a run | - | process | outcome
7. Acceptance rests on the real output of a verification run; builder has no exam set, by design | check 13(a); SIBLING_MAP axis 2 | - | process | outcome
8. A doc-only witness (key presence) needs a negative control | check 13(k) | - | craft | outcome
9. A test must be able to fail: the builder's red-before line and the critic's probe; the expected value never comes from the code | check 50; RUNBOOK §9.1(a), §7 «Что остаётся локально» | owner's words 17.11.2026 (check 50); P20 | craft | outcome
10. An empty search is no proof of absence without a positive control; an environment-negative claim needs a canonical check | check 6; check 27(d) | - | craft | outcome
11. A live run does not stop for the owner: it answers from the ticket, takes the most conservative reading, marks it «мои», and never passes it off as the owner's word | RUNBOOK §9.1(a),(e); §9.6 | «Ценность ночного прогона в том, что он не останавливается без меня, а делает всё, что нужно, сам: отвечает фабрике по данным из тикета, чинит блокеры, другие проблемы записывает и т. д.» 02.10.2026 | craft | outcome
12. A factory blocker is fixed in the package with root cause and test, never by a patch in the project copy | RUNBOOK §9.1(b), §9.6 | - | craft | outcome
13. Every live run has a scoreboard file; norms only tighten; a red or "worse" row has a finding or the owner's pass; release-check runs before a release | check 47; RUNBOOK §9.5, §4.1 | owner's word 13.11.2026 (cited, not quoted) | process | outcome
14. A green dry story before the release PR and before closing a batch | RUNBOOK §4.1, §7 | - | process | outcome
15. The batch canon always runs on CI, within about an hour | RUNBOOK §7; check 40 | «Канон всегда на CI» 03.11.2026; «Когда всё реализовано, конечные проверки пачки должны занимать не больше часа и всё что возможно идти в CI» 28.10.2026 | process | outcome (the 60-minute norm is a number, "measured in the first week")
16. The release copy equals the package, with deletions mirrored; the release fingerprint is checked last; no plugin update under a live story; publication only on the owner's word | RUNBOOK §4, §4.1, §6 | - | process | outcome (steps are means)
17. Old tests go to a watched quarantine; a real catch is landed and told to the owner at once; purge only on the owner's word after READY TO DELETE | check 43; RUNBOOK §7 | owner's words 10.11.2026 (cited) | process | outcome
18. Shrink-only ratchets: any raise is named row by row in the critic verdict, because a diff that adds a site and raises the row is green in-tree | SIBLING_MAP axis 18; checks 35(b), 47(b) | - | process | outcome
19. Fix the class, not the instance: walk the sibling axes of a defect | SIBLING_MAP intro; check 9 | - | process | outcome
20. One road for one action: a language or project is a data row, never a branch in a consumer | SIBLING_MAP axis 34; check 42 | owner's words 06.11.2026 (P31) | craft | outcome
21. Judgment lives in the role, not in code that halts it; a census counts the code checks | SIBLING_MAP axis 32; check 41 | D-0060 (cited, not quoted) | process | outcome
22. A silent gate is not a clean bill: an independent trigger proves gate-code liveness | check 19(a) | - | process | outcome
23. Measure the cost of the machinery itself: routing overhead, warn density (a dense warn trains the reader to ignore it) | checks 11, 17, 18 | - | process | outcome
24. The conductor investigates before asking a person; every question carries a class and what was read | check 38 | owner's word 02.11.2026 (P22) | craft | outcome
25. One experiment before machinery on an unknown environment property | RUNBOOK §10.4 | «сначала замер» 27.10.2026 | process | outcome
26. A new session recovers from the repository alone; if it fails, improve the repo, not the prompt | ZERO_CONTEXT_PROTOCOL | - | process | outcome
27. Session retros are reduced weekly into classes | check 52 | owner's word 24.11.2026 | process | outcome
28. Background waits are bounded (loop form, ceiling 3600 s) | RUNBOOK §9.8 | owner's word 17.11.2026 | process | means

### B. PROTECTION KIT ALREADY PRESENT (what it catches | frequency | carrier)
Calibration checks. Frequency: weekly, by an Architect session; overdue after 7 days. Carrier: `PROCESS/WEEKLY_CALIBRATION_PROTOCOL.md`. Purposes:
- 1 silent self-exclusion, designer threshold, resubmission leak. 2 critic skipped on large diffs. 3 missing escalation after two rejects. 4 self-declared model vs usage.
- 5 silent degradation. 6 acceptance from above, spot-check of scout claims. 7 journal vs transcripts. 8 four questions per mechanism. 9 sibling-map completeness.
- 10 growth of live files. 11 routing overhead, hook output, warn density. 12 map liveness. 13 evidence-based acceptance (a)-(m): witness, false-accept rate, task ids, timestamps, doc witness, merge acks.
- 14 role-prompt edits need an exam run. 15 recurring critic findings codified. 16 two-pass external recon. 17 cost gates (a)-(h). 18 economic trend.
- 19 policy-as-code gates plus liveness probe. 20 judge acceptance (dormant). 21 accepted work exists in HEAD. 22 ledger drift, install parity. 23 closing the previous run.
- 24 gate walk per `defect_found`. 25 escalation cost crossover. 26 freshness of navigation docs. 27 permission and hygiene audit. 28 hand-back completeness.
- 29 upgrade delivery (not applicable here). 30 delegation opportunity scan (every 4th run). 31 feature attribution and fragility. 32 compact snapshot. 33 piles and batches.
- 34 exchange form (digest v1, hop metrics). 35 package detectors (A27). 36 architecture kept. 37 worktrees removed after merge. 38 conductor investigates before asking a person.
- 39 «Остатки» executor. 40 batch canon within the hour, in CI. 41 where judgment lives. 42 one road for one action. 43 test quarantine watched.
- 44 stories with a non-real side never delivered as yes. 45 worktree base differs. 46 task id race. 47 run scoreboard. 48 journal by code, one merge road.
- 49 Architect tier. 50 test discipline. 51 told-before-work. 52 retros reduced.

Role exams:
- Lead ranking: 6 vignettes K1-K6, 12 points, threshold >=10 with no zero. Manual, at selection time. Log empty (q5). Carrier `PROCESS/LEAD_RANKING_EXAM.md`.
- Deployment economy: arms A/B/C, per-task matrix, quality vector on 5 axes. Small exam each cycle, large per release. Table empty (q6). Carrier `PROCESS/DEPLOYMENT_ECONOMY_EXAM.md`, runner `tools/exam_runner.py`.
- Judge calibration: 13 pairs, full agreement required. Dormant (q10). Carrier `gateway/judge_calibration.json`.
- Scout golden set and critic exam: generated, not present (q1).
- Builder and designer: no set, by design (axis 2).

Live runs:
- The overnight run in the copy of a target project, procedure RUNBOOK §9. The morning step assembles the scoreboard (check 47).
- Comparison run: the `factory-vs-free-agent` notebook under `experiments/mybooks/` (RUNBOOK §11, check 47) plus the measurers in `experiments/measurers/` (RUNBOOK §9.7).
- I did not open the notebook.

Dry story: `dry-story.yml` is reached through `nightly.yml` (job `full`) or the separate run `ci_read.py start --var dry_only=true`. Required green for closing a batch and before a release PR. Check 51(d) reads its "told walk". Carrier RUNBOOK §7 and §4.1.

CI jobs (RUNBOOK §7, axis 6):
- `forge-check` runs on push to main and on every PR. It is the required check.
- `nightly.yml` carries `crap-measure` and `quarantine-check`. `canon.yml` ends with `canon-clock`, red after 60 minutes.
- `dry-story.yml`. `quarantine-watch.yml`, cron Monday and Thursday 03:00 UTC.
- `driver-golden.yml`, run by hand.

Quality ratchets. Frequency is at commit or nightly, as the carrier says; the calibration check that reads each one is in brackets. None of these has its own check in PROCESS (q2).
- Lint: `tools/lint_ratchet.py --check`, a pre-push quick check (RUNBOOK §7).
- Clone: `tools/dup_ratchet.py` with `tools/dup-baseline.json` (axis 6).
- CRAP: `tools/crap_ratchet.py` and `crap_report.py` (axis 6, 18, 34).
- Test quarantine: `test-layers.json` (check 43).
- Judgment census (check 41). `norms.json` (check 47). A27 (check 35). Language sites (check 42).

### C. MACHINERY-ONLY ([MEANS] = restricts an agent's means)
- Journal and routing checks 1-7, 13(e)-(i),(l),(m), 46, 48: they police the coordinator's own routing, ids, timestamps and merge acks. [MEANS] for 1(b)-(d), 7 ("Read COORDINATOR.md before the first dispatch").
- Checks 8, 9, 12 and the axis labels (the gate refuses unlabelled axis lines): the map polices its own maintenance. [MEANS]
- Checks 10, 11, 17 (400K worker context, at most 6 writers), 18(e) (one-call-turn share): they police size and cost of the machinery. [MEANS]
- Check 19: the hook list and liveness probe. Checks 22 and 29: ledger and kit snapshot (29 is "not applicable"). Check 20: judge, "not used in this deployment" (one line, dormant).
- Checks 26, 28, 34: hand-back and digest form, with a 2000-character cap and 8-line brief. [MEANS]
- Checks 31, 32, 33, 37, 39, 45, 49, 52: features, compact snapshots, piles, worktree sweep, «Остатки», base mismatch, Architect tier, retros.
- PROCESS files: PATCH_PROTOCOL (install-parity record for policy carriers), PRE_COMMIT and SESSION and BOOT_REPORT (a Boot Report, then STOP; [MEANS]), ARCHITECT_START (four-layer commit review).
- Axes tying tools to tools: 9, 10, 11, 14, 15, 16, 17, 19, 20, 21, 22, 29, 30, 33, 37. Axes 1, 3, 12, 13, 31 tie documents and roles. These exist to keep the current code and dispatch texts consistent.
- RUNBOOK items serving current tooling: §4 fingerprint, `git add -N`, long-path notes; §10 cache TTL (the owner cancelled the experiment); §12 host quirks.

### D. SIBLING MAP IN SHORT
42 axes. Axes 41 and 42 follow the «Keeping the map up to date» section. Grouping by what they tie (axes 2-4, 8-17, 19-30, 33, 35-42 rest on heading titles only, per F).
- Policy, roles, exams, rules and principles: 1, 2, 4, 31, 32, 34.
- Package, release copy, installed plugin; hosts and receipts: 3, 19, 20, 22.
- Stage twins and story records inside the package: 5, 7, 8, 23-28, 30, 35, 36, 38-41, 42.
- Measurement tools vs the package: 6; shrink-only ratchets: 18.
- Forge-tool readers (shell recognizers, git-top, transcripts, console, JSON, tables, append-only jsonl): 9, 10, 11, 14, 15, 16, 17, 21, 29, 33.
- Work-plan carriers (piles, backlog): 12; the dispatch text: 13.

D2. Contradictions and duplicates, both paths:
- WEEKLY numbering note and check 41 call 15/17/39/40 "reserved" though all exist (q7).
- WEEKLY check 31 says GitLab, RUNBOOK §7 says GitHub (q8).
- Check 14 and axis 2 disagree on the scout and critic exams (q9).
- Judge protocol vs check 20 (q10).
- RUNBOOK §9.1(i) vs CLAUDE.md pt.1 on a local full run (q12).
- SIBLING_MAP intro says "keep the map small", and check 10 treats growth as a violation. The file is ~192 KB (the dispatch's figure; I did not measure it) with 42 axes.
- Duplicates in RUNBOOK:
  - Fingerprint step: §4 lines 33-44 and §4.1 line 54.
  - Integrator sentence: line 120, said twice in the same paragraph.
  - Local docker run being fallback only: line 145 and line 146.
- Duplicate across files: the hand-back cap in check 28 and check 34, and the 8-line brief target (also in CLAUDE.md).
