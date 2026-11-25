<!-- scout hand-back, journal task t-1887, recon for docs/tasks/specs/20261125-forge2-light-factory-plan.md; saved verbatim from the worker's final message -->

digest: v1 t-1887
Scope: A-C-D-E rows below are Objects; the id prefix is the DoD section. In A rows `kind` = `A:<craft|process>:<outcome|means|knowledge>`. Every number carries its counting carrier in the cited path; "undated" = the source line gives no date (MEASUREMENTS.md re-states archived plans, dates mostly lost). F = Trail.

## Objects
| id | kind | gist | paths | status | owner | links | ev |
|---|---|---|---|---|---|---|---|
| A01 | A:craft:knowledge | Context cost is quadratic: token at request i paid (N-i) times; 472 requests, mid-context token ~$72/Mtok (undated) | plans/MEASUREMENTS.md:13 | found | - | A02 | T1 |
| A02 | A:craft:knowledge | Cost = turns x average context; orchestrator money is turns between dispatches (509 turns x 261K), not prompt size (undated) | plans/MEASUREMENTS.md:17,27 | found | - | A01 | T1 |
| A03 | A:craft:knowledge | Output tokens 0.4% of tokens, 11% of money; cache read 62% of $109 judge-off (undated) | plans/MEASUREMENTS.md:16,22 | found | - | A01 | T1 |
| A04 | A:craft:knowledge | Orchestrator+S5 = 75% of money in MR !666 ($80.97) and !667 ($141.57); !667 context 73K to 405K (undated) | plans/MEASUREMENTS.md:26 | found | - | A02 | T1 |
| A05 | A:craft:knowledge | Scout fixed prompt 36,700 tokens (own text 7,133 = 19%); one tool schema ~10K; ~25K without Bash (undated) | plans/MEASUREMENTS.md:15; plans/RULES-PROPOSAL.md:109 | found | - | A02 | T1,T3 |
| A06 | A:craft:knowledge | S5 wall time: tests 2-5% (8 of 332 min, 16 of 186, 5 of 129); rest is role turns; 17 of 29 judge-off runs ran zero tests (undated) | plans/MEASUREMENTS.md:34 | found | - | C07 | T1 |
| A07 | A:craft:knowledge | TP1-13797 chain: judge-off $109.00, driver $100.75, driver2 $62.08 (-43%), driver3 $128.53 (driver3 was defect hunting; undated) | plans/MEASUREMENTS.md:53-61 | found | - | A08 | T1 |
| A08 | A:process:knowledge | 58% of driver run (prog 3) money went to factory reconciling itself; 65 of 85 conductor entries were form refusals | plans/MEASUREMENTS.md:59,141 | found | - | B03 | T1 |
| A09 | A:craft:knowledge | Resumed role turn $0.0812 vs fresh $0.0416 = 1.95x (driver3, run 5; undated) | plans/MEASUREMENTS.md:82 | found | - | A07 | T1 |
| A10 | A:craft:outcome | driver3 delivery: 76 reasons delivery_ready:no, 43 of 52 product ones ours; role named AC7, code did not see it | plans/MEASUREMENTS.md:87 | found | - | B06 | T1 |
| A11 | A:craft:knowledge | S5 on 0.7.6 (TP1-15045): 127 of 1668 calls (7.6%) refused by factory hooks; $99.80, 12.5 h; 20 pytest runs vs 2 needed | plans/MEASUREMENTS.md:40,111-112 | found | - | C08 | T1 |
| A12 | A:craft:knowledge | Friction with own code, run 5: 15.5% of turns, 44.2% for code critic (the FR-55 measurer) | plans/RULES-PROPOSAL.md:105 | found | - | C08 | T3 |
| A13 | A:process:knowledge | Refusal count is not defect count: of 45 prohibition refusals only 10 were defects; reads missed 11 to 129 after a fix | plans/MEASUREMENTS.md:101-102 | found | - | E05 | T1 |
| A14 | A:craft:knowledge | Run 5 conductor: 76 sessions, 25 ask_person (16 empty), 21 sessions $9.01 parsing a person's words; 8 of first 9 questions were our gaps | plans/MEASUREMENTS.md:123-124 | found | - | C11 | T1 |
| A15 | A:process:knowledge | Measurement errors: operator session booked as story money ($1,911 vs $128.57); 15045 real ~$28.5 vs $9.23 on dashboard | plans/MEASUREMENTS.md:41,63 | found | - | B01 | T1 |
| A16 | A:process:knowledge | "-50%" forecast was a model, not a measurement; actual 0.7.6 ran $35-45 | plans/MEASUREMENTS.md:44 | found | - | A15 | T1 |
| A17 | A:craft:knowledge | Cost-lever list (undated): critic return via SendMessage ~$0.20 vs $0.75-3.89 new round; read-whole champions: manifest 32 reads/806,531 chars | plans/MEASUREMENTS.md:29,31 | found | - | A02 | T1 |
| A18 | A:process:means | Owner decision, undated: no cheap model for roles; do not cut turns.window; do not add precheck rules | plans/MEASUREMENTS.md:32 | found | «не давать ролям дешёвую модель (решение владельца)» - undated | A22 | T1 |
| A19 | A:craft:knowledge | CI measurement 11.11.2026: 16 slow test files cost 1,242 s on CI, not ~3,000 s dev estimate; world-sharing ceiling ~370 s | plans/MEASUREMENTS.md:258-296 | found | - | B12 | T1 |
| A20 | A:process:knowledge | Selftest 24.09 (Windows, 8 CPU): ~12.5 min; "40 min" was contention of three worktrees; rule: never two full selftests at once | plans/MEASUREMENTS.md:165 | found | - | B12 | T1 |
| A21 | A:craft:knowledge | Baseline TP1-12586, plugin 0.10.2, 27.10.2026: 1,139 requests, cache_read 273,431,414, peak context 639,254 (conductor) | plans/MEASUREMENTS.md:45 | found | - | A02 | T1 |
| A22 | A:process:knowledge | Process tax since 26.09: 399 docs/plans commits per 285 package commits = 1.4; 1,818 journal events; 432 backlog rows, 282 open | plans/forge-metrics.md:51-56 | found | - | B10 | T4 |
| A23 | A:process:knowledge | Dispatcher defects: 12 journal rejections, 8 spec-class; t-023 rejected 3 times, all traced to Lead's own amendments | plans/feature-fragility-2026-10-02.md:17,388-391 | found | - | B11 | T2 |
| A24 | A:craft:knowledge | jev: $0.011 for 855 records while story rose +$11 on the model side; judge by LLM spend removed (FR-51) | plans/MEASUREMENTS.md:140; plans/RULES-PROPOSAL.md:76 | found | - | C05 | T1,T3 |
| A25 | A:craft:means | jev must not get case atomicity, counts/dates/thresholds, any gate or safety refusal; it is injectable | plans/MEASUREMENTS.md:132,147 | found | - | C05 | T1 |
| A26 | A:craft:knowledge | Contract check on real data: 81 fields, 24 red; 9 of 12 critic findings the same defect (probe_by_code) | plans/MEASUREMENTS.md:107 | found | - | B05 | T1 |
| A27 | A:process:knowledge | Gate is the last stop: after "approve" factory stopped 4 times; five causes computable before the gate | plans/MEASUREMENTS.md:204 | found | - | B03 | T1 |
| A28 | A:craft:knowledge | Heredoc ate \b/\n 8 times in 27-28.09; 4th recurrence "not today"; closed by build check; defects found only on foreign OS | plans/MEASUREMENTS.md:155,161; plans/feature-fragility-2026-10-02.md:815 | found | - | B14 | T1,T2 |
| A29 | A:process:outcome | Owner 02.10 10:24: stop and fix every bug that must be fixed before a run or release, not merely stop | plans/factory-fixes.md:82-84 | found | «Останавливаем и чиним все проблемы. Надо было чинить баги, которые в любом случае надо чинить до прогона или до релиза, а не просто останавливаться» - 02.10 10:24 | B10 | T5 |
| A30 | A:process:outcome | Owner 02.10 10:50: analyse all fixes since the yaml run, find architecturally wrong places, split into features, metric per feature | plans/factory-fixes.md:84-87 | found | «проанализируй все фиксы и проблемы с момента прогона с yaml, выдели места, которые часто ломались — архитектурно неверные» - 02.10 10:50 | B15 | T5 |
| A31 | A:process:means | Owner 02.10 11:45: redesign before full run; manual experiment first; designers of redesign start now | plans/factory-fixes.md:91-93 | found | «имеет ли смысл прогонять фабрику, которую переделаем? Сначала эксперимент с мануальным тестом ..., потом большая переделка, потом полный прогон» - 02.10 11:45 | E09 | T5 |
| A32 | A:process:means | Owner 02.10 13:05: ONE runtime for test runs and real work; no orchestrator, conductor + driver (B-261) | plans/factory-fixes.md:100-102 | found | «код тестовых прогонов и реальной работы не должен отличаться; оркестратора нет — есть дирижёр и драйвер» - 02.10 13:05 | C11 | T5 |
| A33 | A:craft:outcome | Owner 30.09 P18: task price must be TRUE, equal to the sum of agent costs from two independent sources; a gap is a defect | plans/factory-fixes.md:1194-1204 | found | - 30.09 (principle P18, text in plans/factory-fixes.md) | B01 | T5 |
| A34 | A:craft:means | Owner 30.09 P19: a case goes down the ladder API, e2e, agent by hand with before/after, person; code checks rung+reason recorded | plans/factory-fixes.md:1212-1222 | found | - 30.09 | E06 | T5 |
| A35 | A:craft:outcome | Owner 01.10 P20: code is never an oracle (FR-58); D-06: Jira agent is not a data source; factory runs on ANY project | plans/factory-fixes.md:173-175,226-231,307 | found | «ничего не теряем при входе» paraphrase only; D-06 19:35 01.10 | B09 | T5 |
| A36 | A:process:means | Owner 29.09: roles run on Sonnet or Terra, never Haiku (FR-52); a fix holding only on a stronger model is not a fix | plans/RULES-PROPOSAL.md:82-86 | found | - 29.09 (standing design rule) | A18 | T3 |
| A37 | A:craft:means | FR-47: code is an instrument a role calls, never a substitute for judgment; scout ~40% of turns matched our script forms; 11 helper scripts, 12 tracebacks in one S1 | plans/RULES-PROPOSAL.md:42-50 | found | - 29.09 (P1) | C08 | T3 |
| A38 | A:craft:means | FR-57: a ban is never bypassed and never a dead end; every ban names its door and the person's word that passes it | plans/RULES-PROPOSAL.md:114-129 | found | - 29.09, corrected on owner's remark | B03 | T3 |
| A39 | A:craft:means | Owner 02.10: stand build identity is a question, not a blocker; mismatched is a message to the person (redeploy / test what is there / stop) | plans/factory-fixes.md:87-91 | found | - 02.10 11:05, 11:40 | E10 | T5 |
| B01 | failure-class | Wrong measurement/cost: F14 13 rows, F19 6; fixed by per-row patches plus later design rule P18 (two sources) | plans/feature-fragility-2026-10-02.md:481,486; plans/factory-fixes.md:1194 | found | - | A33 | T2,T5 |
| B02 | failure-class | Silent loss: F06 8, F05 3, F07 3, F11 3, F02/F01 2 each; each fixed per site (e.g. 1df9fcc, c406b0a); no design change recorded | plans/feature-fragility-2026-10-02.md:468-474,478 | found | - | A13 | T2 |
| B03 | failure-class | Refusal without door / no way out / no zero outcome: F06 5+3, F07 4, F12 3+3, F13 3, F16 3; recurred after FR-40/42 walk | plans/feature-fragility-2026-10-02.md:473,479,480; :811 | found | - | A38 | T2 |
| B04 | failure-class | Text to a person: F07 9, F08 4, F06 4; fix = FR-6 human_text.py (0febcf7) + patches; reappeared rehearsal-13, B-171, B-253д | plans/feature-fragility-2026-10-02.md:474,812,431 | found | - | B03 | T2 |
| B05 | failure-class | Second copy/twin: F06 5, F04 4, F16 3, F01 3; design answer FR-54 map; journal notes "sibling" 42, "twin" 23 | plans/feature-fragility-2026-10-02.md:468,473,619; plans/RULES-PROPOSAL.md:94 | found | - | A26 | T2,T3 |
| B06 | failure-class | False pass / false ok: F11 8, F08 5, F10 3; ex. skipped blocks nothing (B-061), window accepted with no results (B-179) | plans/feature-fragility-2026-10-02.md:89,171,475-478 | found | - | A10 | T2 |
| B07 | failure-class | Role fights the code: F12 3, F02 2, F08 2; ex. $16.53 for two booleans (fd9584f); fix = field-wise edit (patch), FR-47 (rule) | plans/feature-fragility-2026-10-02.md:454,469,475,479 | found | - | A37 | T2,T3 |
| B08 | failure-class | Repeat spend / slow: F19 8, F02 5, F11 5, F05 4, F15 4; partly closed by PROJECT.md rule 2 (B-156/159/160) | plans/feature-fragility-2026-10-02.md:148-152,469,486 | found | - | A19 | T2 |
| B09 | failure-class | Project-specific / absolute path / code reads prose: FR-13 "variety lives in data" itself contradicts P2 (open variety needs a role) | plans/RULES-PROPOSAL.md:140-147; plans/feature-fragility-2026-10-02.md:109-118 | found | - | D01 | T2,T3 |
| B10 | failure-class | Fix-of-fix across 308 items: yes 15, sib 37, rec 5, self 5; top fix-of-fix feature F15 (13 in forge-metrics) | plans/feature-fragility-2026-10-02.md:488,515-520; plans/forge-metrics.md:44 | found | - | A22 | T2,T4 |
| B11 | failure-class | Dispatcher spec defects (silent edge, Lead amendment): 8 of 12 rejections spec-class; fix = rule 11 edges, dispatch_gate (patch + gate) | plans/feature-fragility-2026-10-02.md:17,394 | found | - | A23 | T2 |
| B12 | failure-class | Slow/flaky tests under load: B-082, B-155, B-214; selftest ratchets, split into 11 files (21e2e74) | plans/feature-fragility-2026-10-02.md:105,145-146,406; plans/MEASUREMENTS.md:165-173 | found | - | A19 | T1,T2 |
| B13 | failure-class | Race / block-buffered stdout: B-178 (cmp1), B-253г and rehearsal-12 same defect again, "FR-43 B-line" | plans/feature-fragility-2026-10-02.md:170,278,345,813 | found | - | B14 | T2 |
| B14 | failure-class | Same rule fixed twice: 1556e9b and 7f84cb1 (answered boundary re-asked); eaten-escape byte 4 times; no design change | plans/feature-fragility-2026-10-02.md:814-816 | found | - | A28 | T2 |
| B15 | failure-class | Most fragile features by forge-metrics index: F07 79.0, F06 76.5, F15 71.0, F03 69.0; story_run.py 77 commits | plans/forge-metrics.md:32-36 | found | - | B10 | T4 |
| C01 | code-vs-role | S0 by code: 1 min vs 4 by role, snapshot 13 criteria vs 0 (saved time, richer) | plans/MEASUREMENTS.md:106 | found | - | A06 | T1 |
| C02 | code-vs-role | Brief by code: plugin-file reads 124 to 1, grep 219 to 37 (saved turns) | plans/MEASUREMENTS.md:106 | found | - | C01 | T1 |
| C03 | code-vs-role | Conductor control layer by code: $24 vs $41-60 (saved money) | plans/MEASUREMENTS.md:106 | found | - | C01 | T1 |
| C04 | code-vs-role | Critic probes by code $7.93 vs $8.85 / $16.25 (saved) | plans/MEASUREMENTS.md:106 | found | - | C01 | T1 |
| C05 | code-vs-role | jev answers: $0.00002/step vs conductor session ~$0.45; but model-side +$18.78 reading judge files (net cost) | plans/MEASUREMENTS.md:140,58 | found | - | A24 | T1 |
| C06 | code-vs-role | S0 by REST in seconds, 0 LLM tokens; nothing lost vs judge-off/judge-on/cmp1 (4 tickets, 8 comments, MR 4243) | plans/factory-fixes.md:193-199 | found | - | C01 | T5 |
| C07 | code-vs-role | Test running moved to code: the nearest measures are A06 (tests 2-5% of S5) and A11 (20 pytest runs, hook refusals); no per-role token number | plans/MEASUREMENTS.md:34,111-112 | partial | «мы сделали запуск кодом так как агент на запуск тратил много токенов.» - undated, experiments/ao3-wrapper/factory-vs-free-agent/notebook.md:505 (outside given) | E01 | T1,T6,T7 |
| C08 | code-vs-role | Code hurt: hook refusals 7.6% of calls; friction 15.5% (critic 44.2%); repair cause always test_defect decided by code | plans/MEASUREMENTS.md:111; plans/RULES-PROPOSAL.md:42-50,105 | found | - | B07 | T1,T3 |
| C09 | code-vs-role | 40 run_suite calls were not 40 test runs: 8 discovery, 8 help, 1 wait, 23 launch forms; 21 summaries (10 passed, 5 failed) | plans/MEASUREMENTS.md:42 | found | - | C07 | T1 |
| C10 | code-vs-role | Moved back to role: mechanical fix closed by author's green run, not a code "bytes bridge" (e5e828fd); idea never built | plans/MEASUREMENTS.md:236 | found | owner decided simpler (undated) | A37 | T1 |
| C11 | code-vs-role | Conductor called for a problem, never to run a command (FR-48); headless driver has no ticket re-read on resume (B-259), two heads | plans/RULES-PROPOSAL.md:52-58; plans/factory-fixes.md:108-110 | found | - | A32 | T3,T5 |
| C12 | code-vs-role | Mutation-probe tests wiped a parallel builder's edit twice (t-287); rule: probes only on scratch copy | plans/feature-fragility-2026-10-02.md:767; plans/factory-fixes.md:145,216-218 | found | - | B14 | T2,T5 |
| D01 | contradiction | FR-13 "variety lives in data files, never in code" contradicts owner principle P2 (universality); proposal rewrites FR-13 | plans/RULES-PROPOSAL.md:140-147 | found | - | B09 | T3 |
| D02 | contradiction | Lead interim F-1 (unmeasured green tests a separate group) reversed by owner 30.09: counted as proven | plans/factory-fixes.md:861,1270-1275 | found | «soon there will be none, everyone will update the factory» - 30.09 | A34 | T5 |
| D03 | contradiction | Retro money: owner said no money in repository (test report) vs retro.md committed with money | plans/factory-fixes.md:1116,1121-1124,1180 | found | - 30.09 | A33 | T5 |
| D04 | contradiction | Scribe card says ledger table pasted verbatim, scribe charter says ledger files never shown (Lead cross-spec decision 1) | plans/factory-fixes.md:782-791 | found | - | A33 | T5 |
| D05 | contradiction | Backlog counts: fragility 217 parent rows/308 items (window 26.09-02.10) vs forge-metrics 432 rows/282 open (later window); F01-F20 vs F01-F21 | plans/feature-fragility-2026-10-02.md:9,488; plans/forge-metrics.md:51 | found | - | A22 | T2,T4 |
| D06 | contradiction | Run total driver prog 3: $100.75 vs $100.78 in two sources; judge-on total "not named" in digests | plans/MEASUREMENTS.md:58-59 | found | - | A07 | T1 |
| D07 | duplicate | $99.80 / 12.5 h / 127 refusals of 15045 S5 stated in two archived plans, kept as one fact twice in the same file | plans/MEASUREMENTS.md:40,111-112 | found | - | A11 | T1 |
| D08 | duplicate | Heredoc eaten-escape count 8 in 27-28.09: both MEASUREMENTS.md and fragility | plans/MEASUREMENTS.md:155; plans/feature-fragility-2026-10-02.md:815 | found | - | A28 | T1,T2 |
| D09 | contradiction | Fragility status column unreliable: B-007 closed by 1df9fcc but row not moved; "closed" table empty | plans/feature-fragility-2026-10-02.md:10,26 | found | - | D05 | T2 |
| E01 | open | Tokens an agent spent running tests (the owner's stated reason for code runs): no per-role number in the five files | plans/MEASUREMENTS.md:34 | open | - | C07 | T1 |
| E02 | open | Free-agent one-prompt baseline cost/quality is not in the five files; notebook outside given holds the factory-vs-free-agent study | experiments/ao3-wrapper/factory-vs-free-agent/notebook.md:505 | open | - | C07 | T6 |
| E03 | open | Paired measurement protocol (12+ pairs, sum(new)/sum(base) <= 0.50) only designed; benchmark_compare.py is the comparator | plans/MEASUREMENTS.md:224 | open | - | A16 | T1 |
| E04 | open | Cost of sequential S5 on a big story unmeasured; condition for returning to parallel windows (decision 20.09) | plans/MEASUREMENTS.md:39 | open | - | A04 | T1 |
| E05 | open | Before/after of rules walk (FR-47..57) on fix-of-fix rate never measured; bases named: read_misses 20.0%, spend_by_dispatch | plans/MEASUREMENTS.md:93,101 | open | - | B10 | T1 |
| E06 | open | Whether every ladder rung (3 and 5 especially) has an executor today: backlog B-227 | plans/factory-fixes.md:1221-1222 | open | - | A34 | T5 |
| E07 | open | Owner-level forks left with interim choices: F1 contract prices, F3, F8 thresholds numbers, F12 "Fact" size, F18 sections | plans/factory-fixes.md:939-957,1104-1129 | open | - | D03 | T5 |
| E08 | open | 85 backlog rows undated (n/d); 82 rows name no file; classification of 20 items listed as ambiguous | plans/feature-fragility-2026-10-02.md:13,776-802 | open | - | D05 | T2 |
| E09 | open | Name Forge unconfirmed by owner; whether redesign R-1..R-7 and full run on new factory happened: not in the five files | plans/factory-fixes.md:104,142-143 | open | - | A31 | T5 |
| E10 | open | Stand identity registry (stands x builds x methods) and S0 identity probe designed, live proof pending | plans/factory-fixes.md:87-91,405-411 | open | - | A39 | T5 |
| E11 | open | Judge-on vs base comparison incomparable (0.7.4 vs 0.7.6: $49.85 vs $21.27); no clean judge on/off pair | plans/MEASUREMENTS.md:135 | open | - | A24 | T1 |
| E12 | open | Golden/driver tests untested live: FR-33 unproven live for gate_repair; 27-28.09 fixes never passed a living role | plans/MEASUREMENTS.md:93; plans/factory-fixes.md:486 | open | - | E05 | T1,T5 |

## Trail
| tid | op | target | pattern / range | flags | result | control |
|---|---|---|---|---|---|---|
| T1 | read | C:\QAFactory\forge-repo\plans\MEASUREMENTS.md | whole file | — | read plans/MEASUREMENTS.md:1-296 | — |
| T2 | read | C:\QAFactory\forge-repo\plans\feature-fragility-2026-10-02.md | whole file | — | read plans/feature-fragility-2026-10-02.md:1-821 | — |
| T3 | read | C:\QAFactory\forge-repo\plans\RULES-PROPOSAL.md | whole file | — | read plans/RULES-PROPOSAL.md:1-161 | — |
| T4 | read | C:\QAFactory\forge-repo\plans\forge-metrics.md | whole file | — | read plans/forge-metrics.md:1-67 | — |
| T5 | read | C:\QAFactory\forge-repo\docs\tasks\factory-fixes.md | whole file | — | read docs/tasks/factory-fixes.md:1-1276 | — |
| T6 | grep | C:\QAFactory\forge-repo | `на запуск тратил\|запуск тестов кодом\|тестов кодом\|тратил много токенов` | -i content glob=*.md | found 2; experiments/ao3-wrapper/factory-vs-free-agent/notebook.md:403, :505 (search hit time limit, results incomplete) | — |
| T7 | grep | C:\QAFactory\forge-repo\experiments\ao3-wrapper\factory-vs-free-agent\notebook.md | `тратил много токенов` | content | found 1; notebook.md:505 | — |
| T8 | grep | five given files | `^#{1,3} ` heading count (MEASUREMENTS 41, fragility 17, RULES-PROPOSAL 4, forge-metrics 4, factory-fixes 28) | count | count 94 | — |

## Not done
- F. TRAIL: all five given files read fully (T1-T5). Sizes were under limits; none skimmed. factory-fixes.md (1,276 lines) is a status/decision log: lessons are in the "State at ..." headers and owner words; I used them, not the per-task tables.
- MEASUREMENTS.md cites archived plans (`factory-plans/` in branch experiment/qa-factory-driver); I did not open them, so its numbers are second-hand and mostly undated: A01-A04, A06-A09, A11, A13-A18 carry "undated" in the gist or the source line.
- The five files hold no measurement of per-role token spend on running tests (E01). I have no zero-grep with control for that, so it is stated as "not in the five files read", not as absence across the repo. T6 hit time limit: further matches may exist outside notebook.md. The owner's quote at notebook.md:505 is undated and was not read beyond a 4-line window.
- Class counts in B01-B09 are per-feature counts from Table B (fragility:468-486), not summed across features; "patch vs design" is the source's own wording (commit subjects, FR rules, owner words), not my judgment.
- Analog (rule 8): the same defect class "fixed once per site, recurring elsewhere" appears across B03, B04, B13, B14; forge-metrics counts window commits so the same class may be undercounted for F06 (story_run.py touched 77 times).
- Environment checks (live service state, CI) are outside this role's tools.
## Forks
- Whether "tests run by code" is an outcome or a means in the factory design, and whether to re-measure the owner's token claim (E01) before building: both are decisions, not facts.
- this needs a decision from a tier above.
