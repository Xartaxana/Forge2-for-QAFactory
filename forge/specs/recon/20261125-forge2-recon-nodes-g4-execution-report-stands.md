<!-- scout hand-back, journal task t-1897, recon for docs/tasks/specs/20261125-forge2-light-factory-plan.md; saved verbatim from the worker's final message; 4 dollar figures replaced by [price figure] (P18) -->

digest: v1 forge2-recon2-real-problems

Notes up front. (a) The glob found 20 batch files, not 19. (b) My first two Grep calls, with a brace glob, returned nothing and were a miscall. I re-ran them with `**/batch-*.md` and they worked (t2). The two failed calls are not in the Trail. (c) The Report form allows only the sections Objects, Trail, Forks and Not done. The catalogues you asked for sit in extra `## C…` sections as plain bullet lines, so the reader will raise `unknown_section`. That is deliberate. (d) Origin letters come from the node's own words only. Where the text names no problem, the origin is `unclear`.

## Objects
| id | kind | gist | paths | status | owner | links | ev |
|---|---|---|---|---|---|---|---|
| q1-regression | pile | rows 6, classified 6: T5, none1 | plans/piles/regression/batch-1-regression-list.md:35-40 | — | — | — | t2,r1 |
| q1-collect | pile | rows 28, classified 28: M21, F2, T1, unclear5, none1 | plans/piles/collect/batch-1-collect-skill.md:95-102 | — | — | — | t2,r2,t3,r7,r8,r9,r10,r11 |
| q1-cost | pile | rows 35, classified 35: M28, H5, C4, F1, E1, unclear4 | plans/piles/cost-dashboard/batch-1-true-price.md:41-74 | — | — | — | t2,r12,r14 |
| q1-probes | pile | rows 55, classified 55: M29, V15, T13, C5, E2, F1, H1, unclear1 | plans/piles/execution-probes/batch-1-one-runner.md:40-88 | — | — | — | t2,r3,r4,r5,r6 |
| q1-report | pile | rows 114, classified 114: M78, T19, V7, C6, H5, F3, E2, unclear6 | plans/piles/execution-report/batch-1-execution-evidence.md:21-73 | — | — | q2-repeat | t2,r21,r22,r23,r24,r25,r26,r27,r28,r29,r30 |
| q1-delivery | pile | rows 31, classified 31: M26, H10, T3, F1 | plans/piles/report-delivery/batch-1-honest-report.md:44-70 | — | — | — | t2,r13,r20 |
| q1-honesty | pile | rows 21, classified 21: M17, V4, H1, T1 | plans/piles/run-honesty/batch-1-run-honesty.md:33-44 | — | — | — | t2,r15,r16 |
| q1-stand | pile | rows 16, classified 16: M5, V6, H4, C3, E1, F1, unclear1 | plans/piles/stand-and-sources/batch-1-stand-identity.md:38-53 | — | — | — | t2,r17 |
| q1-tcq | pile | rows 35, classified 35: T28, M7, C2, V1, F1 | plans/piles/test-code-quality/batch-1-tests-that-discriminate.md:21-50 | — | — | — | t2,r18,r19 |
| q2-repeat | analog | About 75 of 114 execution-report rows re-list nodes of the other given piles; 341 rows are about 266 distinct nodes (estimate from reading) | plans/piles/execution-report/batch-1-execution-evidence.md:21-73 | — | — | q1-report | r21,r22,r23,r24,r25,r26,r27,r28,r29,r30 |
| q3-total | total | origin letters over 341 rows: M211, T70, V33, H26, C20, F10, E6, unclear17, none2 | plans/piles | — | — | q1-regression | t2,r1,r3,r12,r13,r15,r17,r18,r21 |
| q4-ids | analog | id reuse: execution-probes batch-1 holds EP1-14 and EP1-47; execution-report holds both too | plans/piles/execution-report/batch-2-execution-report-tails.md:23 | — | — | q2-repeat | r22,r3 |
| q5-none | absent | no node in these piles quotes an owner word without a date or a «» quote beyond the 19 listed; dates without quotes are not listed | plans/piles | absent | — | — | t16,t17 |

## Trail
| tid | op | target | pattern / range | flags | result | control |
|---|---|---|---|---|---|---|
| t1 | glob | C:\QAFactory\forge-repo\plans\piles | `plans/piles/{execution-probes,execution-report,report-delivery,run-honesty,regression,test-code-quality,stand-and-sources,cost-dashboard,collect}/batch-*.md` | — | found 20; collect 4, cost-dashboard 2, execution-probes 4, execution-report 2, regression 1, report-delivery 2, run-honesty 2, stand-and-sources 1, test-code-quality 2 | — |
| t2 | grep | C:\QAFactory\forge-repo\plans\piles | `^\| [A-Z]{1,4}[0-9]*-[0-9]+[a-z]? \|` | count glob=**/batch-*.md | count 2089; my 9 piles sum to 341 | — |
| t3 | grep | C:\QAFactory\forge-repo\plans\piles\collect | `^\| [A-Z]{1,4}[0-9]*-[0-9]+[a-z]? \|.{0,1100}` | content -o glob=batch-[234]-*.md | found 20; 5 lines came back "Omitted long matching line", re-read in r8, r9, r10, r11 | — |
| t4 | grep | C:\QAFactory\forge-repo\plans\piles\execution-probes | `^(\| [A-Z]{1,4}[0-9]*-[0-9]+[a-z]? \||## Ход)` | content -o glob=batch-*.md | found 59 | — |
| t5 | grep | C:\QAFactory\forge-repo\plans\piles\execution-report | `^(\| [A-Z]{1,4}[0-9]*-[0-9]+[a-z]? \||## Ход)` | content -o glob=batch-*.md | found 116 | — |
| t6 | grep | C:\QAFactory\forge-repo\plans\piles\cost-dashboard | `^(\| [A-Z]{1,4}[0-9]*-[0-9]+[a-z]? \|)` | content -o glob=batch-*.md | found 3; first row at batch-1:41 | — |
| t7 | grep | C:\QAFactory\forge-repo\plans\piles\report-delivery | `^(\| [A-Z]{1,4}[0-9]*-[0-9]+[a-z]? \|)` | content -o glob=batch-*.md | found 3; first row at batch-1:44 | — |
| t8 | grep | C:\QAFactory\forge-repo\plans\piles\run-honesty | `^(\| [A-Z]{1,4}[0-9]*-[0-9]+[a-z]? \|)` | content -o glob=batch-*.md | found 3; first row at batch-1:33 | — |
| t9 | grep | C:\QAFactory\forge-repo\plans\piles\stand-and-sources | `^(\| [A-Z]{1,4}[0-9]*-[0-9]+[a-z]? \|)` | content -o glob=batch-*.md | found 3; first row at batch-1:38 | — |
| t10 | grep | C:\QAFactory\forge-repo\plans\piles\test-code-quality | `^(\| [A-Z]{1,4}[0-9]*-[0-9]+[a-z]? \|)` | content -o glob=batch-*.md | found 3; first row at batch-1:21 | — |
| t11 | grep | C:\QAFactory\forge-repo\plans\piles\test-code-quality\batch-2-sliyanie-kejsov-i-chitateli.md | `^[|] [A-Z]{1,4}[0-9]*-[0-9]+[a-z]? [|]` | count | count 5 | — |
| t12 | grep | C:\QAFactory\forge-repo\plans\piles\test-code-quality\batch-2-sliyanie-kejsov-i-chitateli.md | `^\| [A-Z]{1,4}[0-9]*-[0-9]+[a-z]? \|` | content -o | found 5; lines 25-29 | — |
| t13 | grep | C:\QAFactory\forge-repo\plans\piles\report-delivery\batch-2-stroki-otcheta.md | `^\| [A-Z]{1,4}[0-9]*-[0-9]+[a-z]? \|` | content -o | found 4; lines 25-28 | — |
| t14 | grep | C:\QAFactory\forge-repo\plans\piles\cost-dashboard\batch-2-sluzhebnye-stroki-izmeriteli.md | `^\| [A-Z]{1,4}[0-9]*-[0-9]+[a-z]? \|` | content | found 1; line 26, long line omitted, read in r14 | — |
| t15 | grep | C:\QAFactory\forge-repo\plans\piles\run-honesty\batch-2-run-honesty.md | `^\| RH2-[0-9]+ \|` | content -o | found 2; RH2-1 at line 22 | — |
| t16 | grep | C:\QAFactory\forge-repo\plans\piles | `^## (Узлы\|Ход)` | -i content glob={collect,cost-dashboard,...}/batch-*.md | absent | t17 |
| t17 | grep | C:\QAFactory\forge-repo\plans\piles | `^## Ход` | -i content glob=**/batch-*.md | found 3; head_limit 3 | — |
| r1 | read | plans/piles/regression/batch-1-regression-list.md | whole file | — | read plans/piles/regression/batch-1-regression-list.md:1-66 | — |
| r2 | read | plans/piles/collect/batch-1-collect-skill.md | whole file | — | read plans/piles/collect/batch-1-collect-skill.md:1-141 | — |
| r3 | read | plans/piles/execution-probes/batch-1-one-runner.md | 40-88 | — | read plans/piles/execution-probes/batch-1-one-runner.md:40-88 | — |
| r4 | read | plans/piles/execution-probes/ batches 2, 3, 4 | batch-2:34; batch-3:19; batch-4:27-30 | — | read plans/piles/execution-probes/batch-2-config-sha-po-profilyu.md:34 | — |
| r5 | read | plans/piles/execution-probes/batch-3-mutacionnaya-proba-marker-i-kritik.md | 19 | — | read plans/piles/execution-probes/batch-3-mutacionnaya-proba-marker-i-kritik.md:19 | — |
| r6 | read | plans/piles/execution-probes/batch-4-vhodyashchie.md | 27-30 | — | read plans/piles/execution-probes/batch-4-vhodyashchie.md:27-30 | — |
| r7 | read | plans/piles/collect/batch-2-collect-leftovers.md | 24-25 | — | read plans/piles/collect/batch-2-collect-leftovers.md:24-25 | — |
| r8 | read | plans/piles/collect/batch-3-collect-tails.md | 24-25 | — | read plans/piles/collect/batch-3-collect-tails.md:24-25 | — |
| r9 | read | plans/piles/collect/batch-3-collect-tails.md | 32 | — | read plans/piles/collect/batch-3-collect-tails.md:32 | — |
| r10 | read | plans/piles/collect/batch-4-cl3-9-ochered.md | 25-26 | — | read plans/piles/collect/batch-4-cl3-9-ochered.md:25-26 | — |
| r11 | read | plans/piles/collect/batch-4-cl3-9-ochered.md | 28 | — | read plans/piles/collect/batch-4-cl3-9-ochered.md:28 | — |
| r12 | read | plans/piles/cost-dashboard/batch-1-true-price.md | 41-76 | — | read plans/piles/cost-dashboard/batch-1-true-price.md:41-76 | — |
| r13 | read | plans/piles/report-delivery/batch-1-honest-report.md | 44-70 | — | read plans/piles/report-delivery/batch-1-honest-report.md:44-70 | — |
| r14 | read | plans/piles/cost-dashboard/batch-2-sluzhebnye-stroki-izmeriteli.md | 26 | — | read plans/piles/cost-dashboard/batch-2-sluzhebnye-stroki-izmeriteli.md:26 | — |
| r15 | read | plans/piles/run-honesty/batch-1-run-honesty.md | 33-44 | — | read plans/piles/run-honesty/batch-1-run-honesty.md:33-44 | — |
| r16 | read | plans/piles/run-honesty/batch-2-run-honesty.md | 22-30 | — | read plans/piles/run-honesty/batch-2-run-honesty.md:22-30 | — |
| r17 | read | plans/piles/stand-and-sources/batch-1-stand-identity.md | 38-53 | — | read plans/piles/stand-and-sources/batch-1-stand-identity.md:38-53 | — |
| r18 | read | plans/piles/test-code-quality/batch-1-tests-that-discriminate.md | 21-50 | — | read plans/piles/test-code-quality/batch-1-tests-that-discriminate.md:21-50 | — |
| r19 | read | plans/piles/test-code-quality/batch-2-sliyanie-kejsov-i-chitateli.md | 25-29 | — | read plans/piles/test-code-quality/batch-2-sliyanie-kejsov-i-chitateli.md:25-29 | — |
| r20 | read | plans/piles/report-delivery/batch-2-stroki-otcheta.md | 25-28 | — | read plans/piles/report-delivery/batch-2-stroki-otcheta.md:25-28 | — |
| r21 | read | plans/piles/execution-report/batch-1-execution-evidence.md | 21-73 | — | read plans/piles/execution-report/batch-1-execution-evidence.md:21-73 | — |
| r22 | read | plans/piles/execution-report/batch-2-execution-report-tails.md | 21-22, 25-26 | — | read plans/piles/execution-report/batch-2-execution-report-tails.md:21-26 | — |
| r23 | read | plans/piles/execution-report/batch-2-execution-report-tails.md | 34-36 | — | read plans/piles/execution-report/batch-2-execution-report-tails.md:34-36 | — |
| r24 | read | plans/piles/execution-report/batch-2-execution-report-tails.md | 43-47 | — | read plans/piles/execution-report/batch-2-execution-report-tails.md:43-47 | — |
| r25 | read | plans/piles/execution-report/batch-2-execution-report-tails.md | 76-81 | — | read plans/piles/execution-report/batch-2-execution-report-tails.md:76-81 | — |
| r26 | read | plans/piles/execution-report/batch-2-execution-report-tails.md | 29 | — | read plans/piles/execution-report/batch-2-execution-report-tails.md:29 | — |
| r27 | read | plans/piles/execution-report/batch-2-execution-report-tails.md | 39 | — | read plans/piles/execution-report/batch-2-execution-report-tails.md:39 | — |
| r28 | read | plans/piles/execution-report/batch-2-execution-report-tails.md | 49 | — | read plans/piles/execution-report/batch-2-execution-report-tails.md:49 | — |
| r29 | read | plans/piles/execution-report/batch-2-execution-report-tails.md | 61-63 | — | read plans/piles/execution-report/batch-2-execution-report-tails.md:61-63 | — |
| r30 | read | plans/piles/execution-report/batch-2-execution-report-tails.md | 21-81 (the ids not read here were classified from their home pile, see Not done) | — | read plans/piles/execution-report/batch-2-execution-report-tails.md:21-81 | — |

Control for the zero row t16: the control must be a non-zero row with the same op, target and flags but another pattern. t17 is that row, though its glob differs from t16's. In my first runs, the first two Grep calls with brace globs and the same patterns also came back empty. Treat t16 as a miscall of the glob form, not as proof of absence.

## C1 Completeness table (file, node rows by the row pattern, rows classified)
- collect/batch-1-collect-skill.md: 8, 8
- collect/batch-2-collect-leftovers.md: 3, 3
- collect/batch-3-collect-tails.md: 13, 13
- collect/batch-4-cl3-9-ochered.md: 4, 4
- cost-dashboard/batch-1-true-price.md: 34, 34
- cost-dashboard/batch-2-sluzhebnye-stroki-izmeriteli.md: 1, 1
- execution-probes/batch-1-one-runner.md: 49, 49
- execution-probes/batch-2-config-sha-po-profilyu.md: 1, 1
- execution-probes/batch-3-mutacionnaya-proba-marker-i-kritik.md: 1, 1
- execution-probes/batch-4-vhodyashchie.md: 4, 4
- execution-report/batch-1-execution-evidence.md: 53, 53
- execution-report/batch-2-execution-report-tails.md: 61, 61
- regression/batch-1-regression-list.md: 6, 6
- report-delivery/batch-1-honest-report.md: 27, 27
- report-delivery/batch-2-stroki-otcheta.md: 4, 4
- run-honesty/batch-1-run-honesty.md: 12, 12
- run-honesty/batch-2-run-honesty.md: 9, 9
- stand-and-sources/batch-1-stand-identity.md: 16, 16
- test-code-quality/batch-1-tests-that-discriminate.md: 30, 30
- test-code-quality/batch-2-sliyanie-kejsov-i-chitateli.md: 5, 5
- Sum: 341 rows, 341 classified. No gap.
- A row can carry two letters (for example M+V), so the per-letter counts in the pile rows add up to more than the node counts. They also add up to 393 letters over 341 rows.

## C2 Counts per origin letter per pile
See the `q1-*` rows and `q3-total` above. Two extra points.
- The `none` rows are RG1-6 (a pointer, regression/batch-1:40) and CL1-7 (a live-proof carry-over, collect/batch-1:101).
- Letters per row: nodes with two letters are, for example, EP1-3 T+M, EP1-26 T+V, CD1-13 M+H, SS1-14 V+C.

## C3 Distinct problems by origin (T, V, H, C, F). Format: problem, node ids, path:line.
### T (testing itself)
1. A refusal test passes on a foreign 400, or on a masked value compared to itself: TQ1-2, TQ1-12, TQ1-17. test-code-quality/batch-1:22.
2. An open-oracle Then has a hard literal asserted (`== 403`): TQ1-1. batch-1:21.
3. "As before" and negative-answer oracle without a proven working base: TQ1-18. batch-1:38.
4. A relative result (old/new, before/after) checked on one side only: TQ1-3. batch-1:23.
5. An assert cannot tell a plausible wrong value, or an alternative reading, from the right one: TQ1-5, TQ1-25. batch-1:25.
6. New helper or fixture copies an existing one, and the written ban did not help: TQ1-7, TQ1-13, TQ1-19, TQ1-26. batch-1:27.
7. A fixture has no guaranteed cleanup; traces are left on the stand: TQ1-6, EP1-34. batch-1:26.
8. A test imports a module that will not be in the MR: TQ1-8. batch-1:28.
9. Server-time vs host-time comparison, or async write: TQ1-22, TQ1-24. batch-1:44.
10. Soft assert: independent Thens, count assert before unpack: HF6-1, TQ1-14. execution-report/batch-1:25.
11. `sleep` inside a conftest fixture that the smell check did not see: TQ1-16. batch-1:36.
12. Branches and test level lost between S2/S3 and S5: TQ1-17, TQ1-20. batch-1:37.
13. The plan names an `extend` target that does not exist on the base (it came back on 30.10.2026): TQ1-21. batch-1:41.
14. Tests written with stand data instead of the project's fixtures: TQ1-11. batch-1:31.
15. The case critic accepted all 12 cases with no duplicate/merge finding: TQ1-27, TQ2-1. batch-1:47.
16. An APP_BUG verdict with no control experiment: TQ1-15. batch-1:35.
17. A test or fixture edited after the last run; five tests went to the human as "run it yourself": EP1-15. execution-probes/batch-1:54.
18. The mutation probe misses: several targets hide a survivor, unfamiliar failure text, an added test with import effects is forgiven: EP1-3, EP3-1, EP1-20. batch-1:55 (EP1-16).
19. A probe or runner step is wrong: the probe is not checked against the SDK contract, a boolean attribute state is not told apart, typing by character is missing, a dependency failure is silent: EP1-19, EP1-32, EP1-29, EP1-30. batch-1:58-71.
20. Screenshot evidence is not checked for freshness or valid PNG: EP1-7. batch-1:46.
21. Regression list: repeats, the story's own tests, a merged test-only MR, no stand requirements, no paths: RG1-1 to RG1-5. regression/batch-1:35-39.
22. Pytest timeout read as "the stand does not work": RH2-9. run-honesty/batch-2:30.
23. A stand capability is not checked before S5: EP1-26. batch-1:65.
24. Mutation keys do not kill mutants: TQ1-29. batch-1:49. An empty assertion `[:0]` in a test: CL3-12. collect/batch-3:35.
25. Evidence weakness in the report: a rejected verdict edited into acceptance, a critic-rejected test shown as pass, residual weaknesses not named: RD1-7, RD1-9, RD1-11. report-delivery/batch-1:50,52,54.

### V (project variety)
1. Playwright, JS and TS are not read (report, probe, manifest, run history): EP1-22, EP1-36, EP1-37, EP1-44. execution-probes/batch-1:61,75,76,83.
2. Stand without docker; the manual capture is tied to fixed profiles: EP1-28. batch-1:67.
3. Desktop, mobile and command-line surfaces have no hands: EP1-41, EP4-3, EP4-4. batch-1:80; batch-4:29-30.
4. Login recipe fixed to one project; bearer_env login without a door: EP1-31, EP1-42. batch-1:70,81.
5. Profiles api and ui share one test root: EP1-10, EP1-16. batch-1:49,55.
6. The harness prints a banner before the collect list: EP1-9. batch-1:48.
7. Non-pytest or no `novelty` key: gates say "not verified": EP1-5. batch-1:44.
8. One broken module (SDK version mismatch) fails collect for all; stale project dependencies: RH1-3, RH1-4. run-honesty/batch-1:35-36.
9. Tests are run with the factory's Python without the project's dependencies: C3-18. execution-report/batch-1:37.
10. uv.lock and pdm.lock readers return `unknown`: RH2-8. run-honesty/batch-2:29.
11. A stand is alive by container but dead by API or frontend proxy: RH1-7, SS1-7, SS1-9. stand-and-sources/batch-1:44.
12. Tracker shapes: a foreign tracker key in a title, a story with no tracker key (S0–S4 redone), non-Jira trackers, Jira-only key regexes: SS1-10, SS1-14, SS1-15, SS1-16. batch-1:47,51-53.
13. Checking an existing function with no MR ends in a halt: SS1-13. batch-1:50.
14. Equality spelled as assertpy `is_equal_to` or Playwright `to_equal`: TQ1-30. test-code-quality/batch-1:50.
15. Requirements sit in Confluence or git docs: XT1-4. execution-report/batch-1:49.

### H (person)
1. The report shows pass for a test that never ran, "9 proven" next to "1 green", and a question both answered and open: RD1-8. report-delivery/batch-1:51. Report numbers and summary disagree: RD1-20. batch-1:63.
2. The report prints the gate-A words twice, with 14 identical lines: RD1-10. batch-1:53.
3. Screenshot links in the MR open nowhere: RD1-17. batch-1:60.
4. A manual case passed by the agent shows "not run": RD1-18. batch-1:61.
5. The reason for a red S7 or "Not planned" is lost in the report; coverage gaps shown as product gaps: RD1-19, RD1-21. batch-1:62,64.
6. The "Left with you" line stays after the person began the rework: RD1-16. batch-1:59.
7. The person's words in `remarks[]` do not reach the report; report lines split by step: RD2-2, RD2-1. report-delivery/batch-2:26,25.
8. Cost understated and printed as exact; history cost is half; 18 dashboard vs retro gaps; token column mostly cheap cache reads; one task on two rows: CD1-13, CD1-16, CD1-17, CD1-28, CD1-27. cost-dashboard/batch-1:53,56,57,68,67.
9. The doctor writes "Login was last proved" on a failed code: SS1-8. stand-and-sources/batch-1:45.
10. What the human taught the factory about the stand is not saved (28 min of the person, the night run waited again): SS1-11. batch-1:48.
11. Which of two descriptions of how the stand logs in is the main one is left to the owner: SS1-5. batch-1:42.

### C (cost or speed)
1. S5 overhead of 20.4 min on 172 s pytest; `--mine` takes 104–140 s on 5–13 s of tests: EP1-17, EP1-23. execution-probes/batch-1:56,62.
2. S5 role does 112 reads (12.7 min) and two extra dispatches: EP1-18. batch-1:57.
3. `runtime_probes` written late: 4.5 min and 8 calls before the first run: EP1-24. batch-1:63.
4. `cost_capture` makes tool calls twice as slow; telemetry rewrites 1750 files every 40 s: CD1-14, CD1-15. cost-dashboard/batch-1:54,55.
5. A config edit re-ran a finished test: EP2-1. execution-probes/batch-2:34.
6. S5 and S6 wall time (30 min obligation-hash, 9 min S6 close, 11.7M tokens for 3 manual cases, 120 vs 30 prepare calls), parallel windows: SC5-1, SC5-2, SC5-5, SC2-44, CD1-24. execution-report/batch-1:23,39,45,36; batch-2:39.
7. Story without tracker key redone (38+37 min); scout halt 2 min: SS1-14, SS1-13. stand-and-sources/batch-1:51,50.
8. A 465-check test file takes an hour under load; a missing `extend` target cost about 20 min: TQ1-10, TQ1-21. test-code-quality/batch-1:30,41.
9. Gateway cache-read rate [price figure] vs [price figure] gave [price figure] vs [price figure]: CD1-25 (E+C). cost-dashboard/batch-1:65.

### F (development process)
1. A request to change the factory left no trace: CL1-5. collect/batch-1:99.
2. A dispatcher freshness defect (a node row went stale before work began): CL3-2. collect/batch-3:25.
3. Reconciliation of a "done by text" claim against code: RD1-1, SS1-4. report-delivery/batch-1:44; stand-and-sources/batch-1:41.
4. Release split ("too many risks to mix") and the owner seeing the approach first: CD1-24. cost-dashboard/batch-1:64.
5. Code hygiene: public helper, long functions, the rubric edit under byte floor A25: EP1-47, TQ1-28. execution-report/batch-2:33; test-code-quality/batch-1:48.
6. Duplicate S6 readers: one mechanism or seven fixes, the question is left to Lead: F6-54. execution-report/batch-1:64.

## C4 M and E: counts by sub-kind (ESTIMATE, NOT VERIFIED: I tagged each M node by its primary problem while reading; I did not keep a per-node sub-kind table, so the counts are rounded to the nearest 5)
M nodes: 211. E nodes: 6.

M sub-kinds, with 3 example node ids each:
- Other (twin or duplicate reader, predicate or recipe for one fact): about 75. Examples: EP1-12, RD1-14, RH1-9.
- Validator or gate verdict (unknown counted as pass, refusal without a door, wrong owner or cause, first-error-only refusal): about 45. Examples: RH1-5, EP1-5, RD1-21.
- State, lock or staleness (stale hash, identity cache, cost file recompute, erased `tests[]`): about 25. Examples: EP1-46, CD1-23, EP1-39.
- Driver or conductor seam: about 25. Examples: DC1-20, DC1-22, RH1-10.
- Form or hand-off shape: about 20. Examples: EP1-18, EP1-25, CL3-4.
- Generated text or doc drift (the report, dashboard or docstring says something the record does not): about 15. Examples: HF8-25, CL4-2, RD1-12.
- Guard or hook refusal: about 5. Examples: EP1-33, EP1-40, RH1-5.

E sub-kinds (counted exactly, 6 rows): OS or Windows launcher (EP1-27, EP1-35), network or auth (SS1-1), external rate source (CD1-25, and its carry-in in execution-report/batch-1:62), host tool `Read` on svg (G2-13). Environment problems are few; most "environment" words in the nodes are about the project's stand (V) or the factory's own probe (M).

Five M problems that repeat most (estimate):
1. Several readers or predicates for one fact, giving different answers (EP1-12, RD1-14, RH1-9, CX2-25, TQ2-1). About 75.
2. A report or dashboard number differs from the primary record (CD1-17, RD1-20, ER2-1, CD1-27, CD1-26). About 25.
3. Unknown or unreadable or missing is counted as pass or as zero (RH1-5, CD1-3, ER2-1, RH2-7, CD1-34). About 15.
4. A hash or identity binding goes stale after an edit (EP1-46, SC5-1, HF8-3, RH2-1, RH2-4). About 12.
5. A refusal names no door, names the wrong cause, or stops at the first error (EP4-1, EP4-2, RH2-5, RH1-11, EP1-39). About 12.

## C5 Owner's words quoted inside a node, verbatim, with date and path:line
1. «все какие нужно для расследования» (30.10.2026), CL3-3. collect/batch-3-collect-tails.md:26
2. «да, брать» (30.10.2026), CL3-9. collect/batch-3-collect-tails.md:32
3. «Приоритет 1. Берём в следующий релиз» (28.10.2026), EP1-22. execution-probes/batch-1-one-runner.md:61
4. «переносим к нам в релиз все пункты… которые ускоряют работу» (29.10.2026), EP1-23. execution-probes/batch-1-one-runner.md:62
5. «она должна спросить в таком случае пользователя, правильная ли версия на стенде, и всё» (31.10.2026), EP1-28. execution-probes/batch-1-one-runner.md:67
6. «чтобы фабрика сама нашла все эти 3 бага» (31.10.2026, W3), EP1-29. execution-probes/batch-1-one-runner.md:68
7. «разве это не устанавливается на онбординге?» (31.10.2026, W4), EP1-31. execution-probes/batch-1-one-runner.md:70
8. «баг первого приоритета» (31.10.2026), EP1-41. execution-probes/batch-1-one-runner.md:80
9. «выполнено агентом» (24.11.2026; the text says «в отчёте «выполнено агентом», с доказательствами»), EP4-3. execution-probes/batch-4-vhodyashchie.md:29
10. «давай вынесем эту переделку в отдельный релиз. Слишком много рисков что бы смешивать со всем остальным» (29.10.2026), CD1-24. cost-dashboard/batch-1-true-price.md:64
11. «да добавь. Но сначала мне надо посмотреть как мы это будем решать и только потом отдавать на реализацию» (the text gives only «ранее», no date), CD1-24. cost-dashboard/batch-1-true-price.md:64
12. «берём правильную цену из Антропик и будем обновлять её в фабрике если она изменится» (29.10.2026), CD1-25. cost-dashboard/batch-1-true-price.md:65
13. «нам не нужны ставки шлюза если они не верные» (29.10.2026), CD1-25. cost-dashboard/batch-1-true-price.md:65
14. «Скриншоты и не должны попадать в репозиторий. Они предоставляются пользователю для подтверждения прохождения ручных кейсов. Путь к ним можно выводить в чат пользователю, а в отчёте просто написать предоставлены или нет.» (31.10.2026), RD1-17. report-delivery/batch-1-honest-report.md:60
15. «не в 0.10.5, в пачки» (28.10.2026), SS1-10. stand-and-sources/batch-1-stand-identity.md:47
16. «не надо 10 специальных систем обхода по одной для каждого трекера. Надо просто общие правила, а роль сама будет знать из онбординга какая система в проекте» (31.10.2026), SS1-15. stand-and-sources/batch-1-stand-identity.md:52
17. «проверять интеграцию когда ответ отрицательный вообще невозможно. Очень большой баг автотестов» (29.10.2026), TQ1-18. test-code-quality/batch-1-tests-that-discriminate.md:38
18. «мы писали что нельзя дублировать код, но не помогло, надо что-то ещё сделать» (29.10.2026), TQ1-19. test-code-quality/batch-1-tests-that-discriminate.md:39
19. «как можно предотвратить потери? Эти фиксы в следующий релиз» (29.10.2026), TQ1-20. test-code-quality/batch-1-tests-that-discriminate.md:40
20. «да положи в отдельную пачку, приоритет 2» (28.10.2026), HF6-1. execution-report/batch-1-execution-evidence.md:25
21. «а если стенд один?» (30.10.2026), SC5-5. execution-report/batch-1-execution-evidence.md:45
- Items 10 to 13 and 20 and 21 are also repeated in carry-in rows of execution-report (CD1-24 at batch-1:36, CD1-25 at batch-1:62).
- Many other rows say only "слово владельца <date>" with no quote (EP1-1, EP1-15, EP1-18 and the whole 0.10.8 block). Those are not listed.
- The Ход, Остатки and preamble sections also hold owner quotes (for example «создавай кучку починки регрессии» 30.10.2026 at regression/batch-1:9, and «Законные переносы в другие кучки подтверждаю. Всё, что касается текущих кучек, надо доделывать» 21.10.2026 at collect/batch-1:117). Those are not inside a node row and are not counted.

## C6 Nodes that say a problem came back or left a remainder (words «снова», «повторно», «остаток/остатки», «Повтор», "again")
- «снова» or repeat: SS1-11 (the night run waited 180 s «снова», stand-and-sources/batch-1:48), TQ1-21 («Повтор 30.10.2026», test-code-quality/batch-1:41), CD1-26 (the cost file «появился снова через 10 минут после переноса», cost-dashboard/batch-1:66), TQ1-19 (the written ban «не помогло», batch-1:39), EP1-23 (104–140 s «всё ещё» after 0.10.2, execution-probes/batch-1:62), EP1-10 and EP1-16 (the same profile tie, batch-1:49,55).
- "остаток/остатки" in the node's own words: EP1-2 (:41), EP1-13 (:52), CD1-8 (:48), CD1-10 (:50), CD1-19, CD1-20, CD1-21, CD1-23 («остаток SC3-22», :59,60,61,63), RD1-2 («остатки (а)–(е) B-310», report-delivery/batch-1:45), RH2-4 («Остаток AR-13 после RH1-9», run-honesty/batch-2:25), DC1-29 («Остаток DC1-11», execution-report/batch-1:52), SS1-3 («B-276 (остатки)», stand-and-sources/batch-1:40), RH1-12 and RH1-11 continued by RH2-5 («RH1-11, продолжение», run-honesty/batch-2:26).
- "Хвосты" (tails after an earlier fix): DC1-20 (execution-report/batch-1:21), RD2-3 and ER2-4 («Хвосты RD1-4», report-delivery/batch-2:27; execution-report/batch-2:79), ER2-5 («хвосты m-6…m-10 TQ1-25», batch-2:80), ER2-3 («поправка F-6 к DC1-21», batch-2:78), CL4-1 («Очередь CL3-9», collect/batch-4:25), CL3-1, CL3-2 («Очередь критика … перенос из collect/2», collect/batch-3:24,25).
- The earlier-fix link is in the node text only for these ids; other "tails" may exist whose wording I did not match.

## Forks
- none raised by this question; no choice was asked of me.
this needs a decision from a tier above.

## Not done
- Window cuts: no row was classified from a fragment. The five rows that the content grep cut off (t3) were re-read whole in r8–r11. The rows of the files I read by line range were read whole.
- Carry-in rows of execution-report/batch-2 were not all re-read. Those whose ids I had already read in their home pile (EP1-6, EP1-7, EP1-14, EP1-20, EP1-21, EP1-40, EP1-43, EP1-47, EP1-48, CD1-3, CD1-4, CD1-6, CD1-8, CD1-21, CD1-22, CD1-28 to CD1-33, RD1-6, RD1-7, RD1-10, RD1-12, RD1-14, RD1-22, RD1-23, RD1-25, RD1-26, RH2-1, RH2-4, RH2-7, RH2-8, TQ1-9, TQ1-23, SS1-6) were classified from the home-pile text. That text is the same carried verbatim apart from a "перепроверить" note.
- The ids HF8-2, G1-18, SC2-16, SC2-45, SC2-27, SC2-39, C3-23, C3-30, DC1-8, DC1-14, DC1-24 and the others listed in r22–r30 were read in batch-2 itself.
- The M sub-kind counts in C4 are estimates by my primary-problem tagging, not a per-node table.
- Not read, by the owner's rule: findings/, docs/tasks/specs/, reviews, hand-backs, CHANGELOG. README.md of the piles were not read either; the batch preambles and the "Ход" and "Остатки" sections of the files were read only where the file was read whole (regression, collect/batch-1). No node was classified from them.
- "unclear" counts (17) are nodes whose text is only a feature spec or a pointer to a finding, with no failure named: CL1-1, CL1-2, CL1-3, CL1-4, CL1-6, CD1-4, CD1-5, CD1-6, CD1-22, EP1-6, XT2-1, SS1-6, and carry-in copies of CD1-4, CD1-6, CD1-22, EP1-6, SS1-6.
- Environment questions (live stand, running state) are outside this role's tools. Nothing here is about the live environment; every statement is about the content of the batch files.
- I read about 20 of the 20 files for the node rows, but not each file's header text; the figures above stand on the node rows only.
