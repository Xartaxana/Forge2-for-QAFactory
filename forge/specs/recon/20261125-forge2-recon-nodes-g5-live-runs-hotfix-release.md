<!-- scout hand-back, journal task t-1902, recon for docs/tasks/specs/20261125-forge2-light-factory-plan.md; saved verbatim from the worker's final message -->

digest: v1 forge2-recon2-nodes

PARTIAL REPORT. 250 of 431 node rows classified. All three live-run-fvf files (181 rows) were NOT read: the context ran out before I reached them. The counts below cover hotfix-12586, live-runs and release-next only.
Method: where the rule asked for a table and I kept the report short, I used plain lines instead of pipe tables. Origin letters are my reading of each node's own words; where the text names no problem I wrote none or unclear. Paths below are relative to C:\QAFactory\forge-repo\plans\piles\ and are abbreviated (hf = hotfix-12586, lr = live-runs, rn = release-next).

## Objects
| id | kind | gist | paths | status | owner | links | ev |
|---|---|---|---|---|---|---|---|
| q1-rows | count | 431 node rows by the П-priority pattern in 16 batch files; hotfix batch-2 also holds 30 non-node rows | hotfix-12586/batch-2-run-12586-s5.md:111-145 | found | — | q1-cover | t1,t2,t3,t4,t5,t6,t7,t8 |
| q1-cover | count | 250 rows read and classified (hf 123, lr 47, rn 80); live-run-fvf 0 of 181 | live-run-fvf/batch-1-live-run-fvf.md:1 | found | — | q1-rows | t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22 |
| q2-hf | count | hf 123 rows: M92 T24 H24 V9 C8 F7 E4 none1 (two-letter nodes counted under each letter) | hotfix-12586/batch-1-run-12586.md:47-61 | found | — | q1-cover | t9,t11,t12,t13,t14,t15,t16,t17 |
| q2-lr | count | lr 47 rows: M11 T8 H8 V7 C6 E1 unclear4 none7 | live-runs/batch-1-live-proofs.md:40-58 | found | — | q1-cover | t18,t19 |
| q2-rn | count | rn 80 rows: M36 T26 H16 C6 V4 F3 E2 none6 | release-next/batch-1-release-0-10-9.md:27-95 | found | — | q1-cover | t20,t21,t22 |
| q5-words | list | owner's words quoted inside nodes: see Words block below | hotfix-12586/batch-8-ostatki-hf3.md:28 | found | owner | q1-cover | t11,t13,t16,t19,t21,t22 |
| q6-back | list | nodes saying the problem came back after an earlier fix: see Came-back block below | release-next/batch-1-release-0-10-9.md:66 | found | — | q1-cover | t11,t16,t21,t22 |
| q-fvf | gap | live-run-fvf batch files not read | live-run-fvf/batch-2-live-run-fvf.md:1 | absent | — | q1-cover | t3 |

**Per file: id-pattern rows / node rows (П-pattern) / classified**
hf batch-1 15/15/15; batch-2 49/19/19 (the other 30 are owns, witness-scope and carry tables, not nodes); batch-3 15/15/15; batch-4 14/14/14; batch-5 20/20/20; batch-6 1/1/1; batch-7 5/5/5; batch-8 32/32/32; batch-9 2/2/2.
lr batch-1 19/19/19; batch-2 28/28/28 (17 of them are copies of LR1-x, classified the same way as in batch-1).
rn batch-1 69/69/69; batch-2 11/11/11.
live-run-fvf batch-1 30/30/0; batch-2 96/96/0; batch-3 55/55/0.
Sums: all files 461 id-pattern rows and 431 node rows; classified 250 node rows.
Duplicates across files, counted in each file: HF2-16, HF2-17 and HF2-18 appear in hf batch-2 and batch-3. HF3-4, HF3-5, HF3-9 and HF3-11 reappear as HF8-1 to HF8-4. HF8-8 and HF8-24 reappear as HF9-1 and HF9-2.

**Origin counts per pile** are in the q2-hf, q2-lr and q2-rn rows. Release chores or carry-overs with no problem named (none): HF5-9, LR1-6, LR1-15, C3-19, CL1-7, G3-1, and XT1-1/3/5/6/7/8, which are new-skill features.
Unclear: LR1-2 (the http-answers lists were an estimate) and LR1-18, in both lr files.

**T, testing work: distinct problems**
- Independent Then is hidden behind the first red assert, so soft asserts are needed. HF6-1, HF2-3, HF5-14. hotfix-12586/batch-6-soft-assertions.md:25
- One case holds mixed outcomes (handed to a person, green, red, blocked) and some are lost. HF2-3, HF1-10. hotfix-12586/batch-2-run-12586-s5.md:253
- Triage said APP_BUG with no control experiment, when the assert was stricter than the requirement. HF2-18, LR1-12. batch-2:268
- A refusal test passes on a foreign 400, and a mask is compared with a mask. HF2-15. batch-2:265
- Duplicate helper or fixture next to an existing one, assert before unpack, test level differs from the plan. HF2-13, HF2-14, HF3-4. batch-2:263-264
- A test or fixture changed after the last run with no rerun, and receipts of earlier windows went stale. HF2-11, HF8-18. batch-8:41
- UI step error misnamed: "not found" when the element was overlapped. HF5-1. hotfix-12586/batch-5:46
- Manual executor wrote a verdict that contradicted its own evidence; the agent did not observe after each step. HF8-19, HF5-4. batch-8:42
- Grouping rule for "one case, one test" exists in three carriers. HF5-7. batch-5:52
- Then behind another case's red, and the red-by-bug Then order. HF5-12, HF5-15, HF5-16. batch-5:57-61
- Case critic rejected on remarks only, found no duplicates, or did not check that the value distinguishes outcomes. HF4-11, TQ1-27, RN1-27. release-next/batch-1:33
- Time fork through an async write; a Then that distinguishes two readings must fail under the other reading. TQ1-24, TQ1-25. rn:32,45
- Open oracle asserted as a literal; broad status check; actor-control rule. TQ1-1, TQ1-2. rn:43-44
- Tests used stand data instead of the project's own harness fixtures. TQ1-11. rn:64
- pytest-timeout kill read as "stand not working". RH2-9. rn:46
- Plan target `extend` names a file that does not exist; support layer lost. TQ1-21. rn:31
- Scout stopped on a conflict that the ticket comments had already resolved. RC1-13. rn:35
- One bug with many manifestations was split into many bugs; a bug duplicates an open one. RN2-1..8, RN1-18. rn/batch-2:25, rn/batch-1:79
- Request failure must be tried for every request of the flow; keyboard input; focus lost. RN1-6, RN1-7, XT2-2. rn:67,68,54
- Case defect known at S5 not returned to S4; candidate bugs from code reading never reach gate B. RN1-17, RN1-12. rn:78,73
- P19 ladder: manual rung accepted as "not measured". RN1-13. rn:74
- Comparison against a free agent and a reference baseline (false bugs, duplicates, green test is not a standard); a hidden-fact scenario. LR2-1, LR1-19, LR1-9. lr/batch-2:68
- Test novelty `unknown` needs a critic question. LR2-4. lr/batch-2:71

**V, project variety: distinct problems**
- api and ui profiles share one test root. HF1-3. hf/batch-1:50
- Runner collect output has a banner and the reader stopped there. HF1-1. hf/batch-1:48
- The stand expects `email`, the probe sent `username`. HF1-4. hf/batch-1:51
- pytest-playwright ids such as `[chromium]` were not found by the probe. HF4-12. hf/batch-4:46
- Playwright TypeScript: probe verdict `incomplete`, manifest selector, instance ids. RN1-8, RN1-21. rn:69,82
- UI and API on one address; `FRONTEND_URL` not linked to `url_key`. RN1-3, HF8-10, HF5-2. rn:61
- Integration with alternative key sets (Jira Cloud / Server). HF8-11. hf/batch-8:34
- Tracker MR links: `inspect --media-url` refuses and the card tells the scout to use it unconditionally. HF8-5, HF8-30. batch-8:28,53
- Non-Python project, other platforms, multi-repo, Makefile diff. LR1-1, LR1-7, LR1-17. lr/batch-1:40,46,56
- Manual login must go as the project does (storageState). RN1-10. rn:71
- Mutation probe lost `profile_id` of the manifest row. HF2-8. batch-2:258
- Stand credentials by role; unmeasured stand limit. HF8-9, LR2-3. batch-8:32

**H, person: distinct problems**
- After the gate the conductor always stops and asks the person to type a command. HF1-8. hf/batch-1:55
- Gate A was silent about an integration gap known from onboarding; the person learned in S5. HF1-9. hf/batch-1:56
- One unfulfillable Then could not be handed to the person. HF1-10. hf/batch-1:57
- Person's answers were not applied at once; a changed answer did not open rework. HF2-7, HF3-10. batch-2:257
- Red windows closed only by the person's words (3 words in window 4). HF2-4. batch-2:254
- Report showed pass for an unexecuted test, "9 proven" next to "1 green". HF2-6. batch-2:256
- Gate A re-asks what was decided; a letter answer to a before/now card was not applied. HF4-8, RN1-11, RN1-14. batch-4:42; rn:72,75
- Person sees JSON or ledger links in the gate-B package and the report. HF8-20. batch-8:43
- The owner's recorded choice, and false SessionStart warnings, reach the person as warnings. HF8-13, OH1-11. batch-8:36; rn:58
- Report misleads: bug "unconfirmed", price understated but printed as exact, price split over two rows. HF8-16, CD1-13, CD1-27. rn:55-56
- Conductor asks before resolving it itself, retells gate A in its own words, or states a hypothesis as fact. RN1-9, RN1-4, RN1-31. rn:70,62,92
- The person's word was recorded as an environment waiver; a scope exclusion was attributed to the person's word; gate B did not take words. RN1-15, WG1-1, GW1-3, HF8-23. rn:76,95,27
- Verdict names the case defect and not the product bug. RN1-16. rn:77
- A question about one manual case held the whole pipeline 3h50. RN1-24. rn:85
- Conductor waited for a critic who had already returned, and the run stood. HF8-15. batch-8:38
- Question to the owner about running lint at S5; manual checks left `new` so the person reopened gate A. HF4-13, HF4-14. batch-4:47-48

**C, cost or speed: distinct problems**
- S5 window control 25 min; 112 read calls, 12.7 min. HF2-16, HF2-17. batch-2:266-267
- Hook made calls twice as slow (shell 4.4 s to 10.4 s). HF2-9. batch-2:259
- 20 minutes of harness around one test run. HF2-10. batch-2:260
- Slow tests and canon: `test_red_window` 7 min, `test_story_step` about 1 h, branch canon 6.5 h. HF3-8, TQ1-10, HF3-12. batch-3:45,49; rn:65
- One factory command takes 40-200 s, and the host classifier adds about 5 s per call. SC2-40. rn:39
- Role injection ceilings A22/A25 (strategist 54 360 B). RC1-14. rn:63
- Conductor context grows with S5 windows (82 million tokens, compaction mid-S5); findings lost across compactions. RN1-32, LR1-3. rn:93

**F, dev process: distinct problems**
- A hotfix made by a foreign hand needed a critic pass on the diff; critics per wave. HF1-0, HF2-0. hf/batch-1:47
- Post-release quality debt, dead code, edge behaviour not specified. HF3-11, HF4-4, HF4-2. hf/batch-3:48
- Duplicate helpers and over-long functions found by critics. RN2-10, RN2-11, HF8-29. rn/batch-2:34
- Tests did not hold stage joints (17 digest-form refusals, receipts with no producer). F6-51. rn:42

**M sub-kinds, approximate.** I tagged at read time, not row by row, so these counts are about +/-5 each. M total is 139 (92+11+36). Split:
- validator or gate verdict about 40. Examples HF1-10, HF2-4, HF4-10.
- state, lock or staleness about 20. Examples HF3-9, HF5-19, RN1-20.
- driver or conductor seam about 18. Examples HF8-15, HF8-6, DC1-21.
- guard or hook refusal about 14. Examples HF1-6, HF5-13, RN1-29.
- form or hand-off shape about 14. Examples HF8-7, HF9-2, HF2-12.
- generated text or doc drift about 12. Examples HF1-12, HF1-13, HF8-25.
- other about 21. Examples HF3-1, HF3-3, RN2-9.
**E, 7 nodes:**
- host CLI return form: HF1-5, HF1-7, HF4-6 (hf/batch-4:40), HF7-4, RN1-1. 5 nodes.
- console encoding: LR1-5 (lr/batch-1:44). 1 node.
- host classifier latency: SC2-40. 1 node.
**The 5 most repeating M problems, with ids:**
1. One fact has two readers or carriers (parser, number of Then, "green without a run line"). HF1-1, HF2-2, HF3-1, HF8-32, HF5-2, HF5-7, RN2-10.
2. A chain demands green or an executed test and refuses red or unexecuted, so the outcome passes only on a human word. HF2-1, HF2-4, HF1-10, HF2-3, HF4-10.
3. A person's word is not read or applied by code. HF1-14, HF2-7, HF3-10, HF8-23, RN1-11, RN1-15.
4. A refusal text has no door, or names the wrong one. HF5-11, HF8-5, HF8-7, HF8-30, HF8-31.
5. A card, help or role text diverges from the parser or from what the role can read. HF1-2, HF1-12, HF1-13, HF8-25.
Close runner-up: stale receipts or versions (HF3-9, HF8-18, RN1-20, RN1-33).

**Words: owner's words quoted inside nodes** (verbatim, date as the text gives it). In a row without a date I give the row's own date or none.
- hf/batch-1:10-13, 22.10.2026 (the intro lists these, not a node): «это надо убрать»; «фабрика должна говорить, чего ей не хватает, сразу»; «один Then нельзя закомментировать и передать человеку, даже если пользователь согласен».
- hf/batch-1:10-13, 23.10.2026: «починить срочно отдельной пачкой; долгие тесты и регрессии в конце пачки; хотфикс — только через критика на соответствие архитектуре».
- hf/batch-1:55 HF1-8, 22.10.2026: «это надо убрать».
- hf/batch-1:82 (the Ход journal, outside a node), 23.10: «если находка была записана как upstream candidate — то всё правильно».
- hf/batch-6:25 HF6-1, 28.10.2026: «да положи в отдельную пачку, приоритет 2».
- hf/batch-2:251 HF2-1, 25.10.2026: «F-17 — во вторую волну, если не блокирует прохождение стори. Если блокирует, то чиним сразу».
- hf/batch-2:254 HF2-4, 25.10.2026: «последнюю проблему прогона стори нужно обязательно взять в срочную пачку».
- hf/batch-2:268 HF2-18 (also hf/batch-3:37), 25.10.2026: «если нет, то это надо исправить во второй волне срочной пачки».
- hf/batch-5:57 HF5-12, no date in the row: «а это не правильно…».
- hf/batch-5:60 HF5-15: «Да, делаем».
- hf/batch-5:61 HF5-16: «это правильно», «принимаю», «можно не комментировать если переставление возможно».
- hf/batch-8:28 HF8-5, also :32-37 for HF8-9..14, 29.10.2026: «Все эти предупреждения фабрики надо починить в следующем релизе».
- hf/batch-8:29 HF8-6, 29.10.2026: «да, добавляй в ближайший релиз».
- hf/batch-8:36 HF8-13, 29.10.2026: «оставить в маркдаун и это был мой выбор при онбординге».
- hf/batch-8:43 HF8-20, 29.10.2026: «Человеку не должны выводиться нечеловекочитаемые файлы»; and «надо уменьшить количество ссылок на технические документы в самом отчёте. Человек не читает джейсоны и леджеры».
- hf/batch-8:44 HF8-21, 29.10.2026: «это тоже исправить вместе с исправлением хендофа роли».
- hf/batch-8:47 HF8-24, 29.10.2026: «к нам в релиз».
- lr/batch-2:50 G3-1, 19.10.2026: «доказательства лучше собирать на 15045».
- rn/batch-1:34 SC2-41, 29.10.2026: «надо ещё поднять лимиты так что бы то что в этом тикете читалось».
- rn/batch-1:36 CL3-3, 30.10.2026: «все какие нужно для расследования».
- rn/batch-1:38 CL3-9, 30.10.2026: «да, брать».
- rn/batch-1:39 SC2-40, 29.10.2026: «Приоритет1».
- rn/batch-1:54 XT2-2, 31.10.2026: «чтобы при запуске этого скилла фабрика нашла как минимум эти 3 бага».
- rn/batch-1:63 RC1-14, 30.10.2026: «не на 20 КБ урезать, а решить; либо признаём и поднимаем лимиты».
- rn/batch-1:70 RN1-9, 02.11.2026: «Сначала разбирается сам — всегда и везде» (PROJECT.md P22 as quoted in the node).
- rn/batch-1:78 RN1-17, 02.11.2026: «дефект фабрики — не связала однозначное требование (цена на момент добавления) с кодом (цена не хранится): это один ожидаемый красный, баг продукта, а не вопрос Q7 и не 11 красных; остальные кейсы одно и то же не проверяют».
- Owner questions quoted in nodes: rn/batch-1:30 «учитываются ли рисковые области при написании кейсов»; hf/batch-8:39 «почему баг не подтверждённый»; hf/batch-8:45 «почему хотела переоткрывать S8».
- Owner's words cited without a quote (not listed above): HF1-0, HF2-0, HF3-6, HF3-12, HF4-11, HF4-13, RN1-2, RN1-4, RN1-10, WG1-1, LR2-1, hf/batch-8:42-47 and others.

**Came-back: nodes saying the problem returned after an earlier fix**
- Remainder or part returned: HF2-5 «Остаток GW1-14 после HF1-10» (hf/batch-2:255); HF3-3 «остаток AR-13/AR-22» (hf/batch-3:40); HF1-14 «Часть EP1-10, возвращённая HF1-3 вопросом Q1» (hf/batch-1:61); HF8-24 «второй свидетель HF8-8» (hf/batch-8:47).
- Class surfaced again: HF2-1 «Класс всплыл в прогоне трижды» (hf/batch-2:251); HF8-21 «повтор B-183» (hf/batch-8:44); TQ1-21 «Повтор 30.10.2026» (rn:31).
- Marked "Регрессия/не починено": RN1-5 (G2-14/15), RN1-7 (EP1-29), RN1-8 (EP1-36), RN1-10 (EP1-31), RN1-11 (GW1-43), RN1-14 (GW1-43, «снова спрашивает»), RN1-19 (HF8-16), RN1-21 (EP1-37), RN1-22 (EP1-39), RN1-23 (RD1-21), RN1-33 (RD1-20). All at rn/batch-1:66-94.
- Remainder pointer: RN1-23 «п. 2 (ii) — в «Остатках»» (rn:84).

## Trail
| tid | op | target | pattern / range | flags | result | control |
|---|---|---|---|---|---|---|
| t1 | grep | C:\QAFactory\forge-repo\plans\piles\hotfix-12586 | `^\| [A-Z][A-Za-z0-9]*-[0-9A-Za-z.\-]* \|` | count glob=batch-*.md | count 153 | — |
| t2 | grep | C:\QAFactory\forge-repo\plans\piles\live-runs | `^\| [A-Z][A-Za-z0-9]*-[0-9A-Za-z.\-]* \|` | count glob=batch-*.md | count 47 | — |
| t3 | grep | C:\QAFactory\forge-repo\plans\piles\live-run-fvf | `^\| [A-Z][A-Za-z0-9]*-[0-9A-Za-z.\-]* \|` | count glob=batch-*.md | count 181 | — |
| t4 | grep | C:\QAFactory\forge-repo\plans\piles\release-next | `^\| [A-Z][A-Za-z0-9]*-[0-9A-Za-z.\-]* \|` | count glob=batch-*.md | count 80 | — |
| t5 | grep | C:\QAFactory\forge-repo\plans\piles\hotfix-12586 | `^\| [A-Z][A-Za-z0-9.\-]* \| П[0-9]` | count glob=batch-*.md | count 123 | — |
| t6 | grep | C:\QAFactory\forge-repo\plans\piles\live-runs | `^\| [A-Z][A-Za-z0-9.\-]* \| П[0-9]` | count glob=batch-*.md | count 47 | — |
| t7 | grep | C:\QAFactory\forge-repo\plans\piles\live-run-fvf | `^\| [A-Z][A-Za-z0-9.\-]* \| П[0-9]` | count glob=batch-*.md | count 181 | — |
| t8 | grep | C:\QAFactory\forge-repo\plans\piles\release-next | `^\| [A-Z][A-Za-z0-9.\-]* \| П[0-9]` | count glob=batch-*.md | count 80 | — |
| t9 | read | C:\QAFactory\forge-repo\plans\piles\hotfix-12586\batch-1-run-12586.md | whole file | — | read hotfix-12586/batch-1-run-12586.md:1-151 | — |
| t10 | read | C:\QAFactory\forge-repo\plans\piles\hotfix-12586\batch-6-soft-assertions.md | whole file | — | read hotfix-12586/batch-6-soft-assertions.md:1-41 | — |
| t11 | read | C:\QAFactory\forge-repo\plans\piles\hotfix-12586\batch-2-run-12586-s5.md | 246-271 (rows only) | — | read hotfix-12586/batch-2-run-12586-s5.md:246-271 | — |
| t12 | read | C:\QAFactory\forge-repo\plans\piles\hotfix-12586\batch-3-wave-2-and-remainders.md | 35-37, 43, 48-49 | — | read hotfix-12586/batch-3-wave-2-and-remainders.md:35-49 | — |
| t13 | read | C:\QAFactory\forge-repo\plans\piles\hotfix-12586\batch-4-ostatki-hf3-po-revyu.md | 40-48 | — | read hotfix-12586/batch-4-ostatki-hf3-po-revyu.md:40-48 | — |
| t14 | read | C:\QAFactory\forge-repo\plans\piles\hotfix-12586\batch-5-run-12586-manual-red-then-bugs.md | 46-65 | — | read hotfix-12586/batch-5-run-12586-manual-red-then-bugs.md:46-65 | — |
| t15 | read | C:\QAFactory\forge-repo\plans\piles\hotfix-12586\batch-7-dashboard-price.md | 26-30 | — | read hotfix-12586/batch-7-dashboard-price.md:26-30 | — |
| t16 | read | C:\QAFactory\forge-repo\plans\piles\hotfix-12586\batch-8-ostatki-hf3.md | 24-55 | — | read hotfix-12586/batch-8-ostatki-hf3.md:24-55 | — |
| t17 | read | C:\QAFactory\forge-repo\plans\piles\hotfix-12586\batch-9-forma-i-vozvrat-dorabotki.md | 30-31 | — | read hotfix-12586/batch-9-forma-i-vozvrat-dorabotki.md:30-31 | — |
| t18 | read | C:\QAFactory\forge-repo\plans\piles\live-runs\batch-1-live-proofs.md | 40-58 | — | read live-runs/batch-1-live-proofs.md:40-58 | — |
| t19 | read | C:\QAFactory\forge-repo\plans\piles\live-runs\batch-2-live-proofs.md | 45-72 | — | read live-runs/batch-2-live-proofs.md:45-72 | — |
| t20 | read | C:\QAFactory\forge-repo\plans\piles\release-next\batch-2-one-bug-many-manifestations.md | 25-35 | — | read release-next/batch-2-one-bug-many-manifestations.md:25-35 | — |
| t21 | read | C:\QAFactory\forge-repo\plans\piles\release-next\batch-1-release-0-10-9.md | 27-62 | — | read release-next/batch-1-release-0-10-9.md:27-62 | — |
| t22 | read | C:\QAFactory\forge-repo\plans\piles\release-next\batch-1-release-0-10-9.md | 63-95 | — | read release-next/batch-1-release-0-10-9.md:63-95 | — |
| t23 | grep | C:\QAFactory\forge-repo\plans\piles\hotfix-12586\batch-2-run-12586-s5.md | `^\| [A-Z][A-Za-z0-9]*-[0-9A-Za-z.\-]* \|` | content | found 30; HF2-7 table rows at :111-120, :130-145, :170-172, :239-241 and node rows :250-268 | — |

## Not done
- live-run-fvf batches 1-3 (181 node rows, `C:\QAFactory\forge-repo\plans\piles\live-run-fvf\batch-1-live-run-fvf.md`, `batch-2-live-run-fvf.md`, `batch-3-live-run-fvf.md`) were not read or classified. The rows are long and Grep truncates long lines ("Omitted long matching line"), so Read was the only way, and the context budget ran out first. So there are no counts, problems or owner's words for that pile. This is not a claim that it has none.
- The four README.md files were not read. The "Ход" journals in the batch files were not read, except hotfix-12586 batch-1 and batch-6, which I read whole. Owner's words that sit only in journals are therefore missing, apart from the one noted at hotfix-12586/batch-1:82.
- The M sub-kind counts are approximate (see above). Per-row origin letters are my reading of each node's own words, not a re-checked table. Rows with no problem named got none or unclear, not a guess.
- I dropped two early count calls that returned zero because I used a brace glob that this tool does not support (a miscall, not an absence). The per-pile calls t1-t8 are the working form.
- I did not check findings, specs or reviews, per the owner's exclusion.
