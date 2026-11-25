<!-- scout hand-back, journal task t-1889, recon for docs/tasks/specs/20261125-forge2-light-factory-plan.md; saved verbatim from the worker's final message -->

digest: v1 t-1889

## Objects
| id | kind | gist | paths | status | owner | links | ev |
|---|---|---|---|---|---|---|---|
| a01 | A:craft:outcome | Factory, knowing nothing of the project, passes every stage without getting stuck; role goes first, person gets only the remainder; blocking never acceptable | docs/tasks/specs/20261117-u7-pass-without-stuck-spec-r3.md:10-13 | carry | goal text "verbatim in the brief" 17.11.2026 (the Russian original was not opened; spec gives it in English) | c01 | T44 |
| a02 | A:craft:outcome | Second instance of stand/device: not authorized by default, asked once at first need, answer recorded, never re-asked | docs/tasks/specs/20261117-u7-pass-without-stuck-spec-r3.md:71-77 | carry | «спросить один раз, но не на онбординге, а тогда когда это понадобится» 17.11.2026 | c01 | T44,T38 |
| a03 | A:craft:outcome | Factory must be better than a free agent, not worse; must not stand at the unfamiliar, lets the agent work | experiments/ao3-wrapper/factory-vs-free-agent/notebook.md:17-19 | carry | «мы до этого обсуждали что фабрика должна быть лучше свободного агента, а не хуже и даже создали кучку универсальность и делали фиксы что бы фабрика не вставала когда видит что-то незнакомое, а давала работать агенту» 24.11.2026 | c01 | T43 |
| a04 | A:craft:outcome | More reliable than an agent, may be a bit slower because its result is checked | docs/tasks/specs/20261113-plan-fabrika-ne-huzhe-agenta.md:9 | carry | «Фабрика должна быть надёжнее агента, работать не хуже, но может быть чуть медленнее, так как мы проверяем её результат.» 13.11.2026 | d06 | T53 |
| a05 | A:process:outcome | Live runs are the last stage like UAT; blockers must not reach them | docs/tasks/specs/20261113-plan-fabrika-ne-huzhe-agenta.md:8 | carry | «Живые прогоны дороги и очень долгие, это последний этап тестирования, как UAT. До них не должно доходить блокеров.» 13.11.2026 | — | T53 |
| a06 | A:process:outcome | Fix errors by cause, collect all places where it can surface, one mechanism not patches | docs/tasks/specs/20261113-told-before-work-mechanism-spec.md:9-10 | carry | «Эту причину мы уже фиксили много много раз. Надо собрать все места где она может всплыть и пофиксить. И не заплатками, а единым механизмом, чтобы следующими фиксами снова не наплодить такой проблемы» 13.11.2026 | c04 | T49 |
| a07 | A:process:outcome | Fix the whole class of a finding, not the one place caught | plans/piles/conductor/batch-2-cmp3-classes.md:8-13 | carry | «Мы должны чинить весь класс таких проблем, а не одно место где мы поймали прицедент» 13.10.2026 20:58 | c09 | T57 |
| a08 | A:craft:outcome | Factory must not promise or try what is known in advance to be impossible; no question for it | plans/piles/conductor/batch-2-cmp3-classes.md:9-11 | carry | «Фабрика не должна обещать или пытаться сделать что-то что заранее понятно что невозможно» 13.10.2026 20:58 | a15 | T57 |
| a09 | A:craft:outcome | Calling a role only for bureaucratic procedure is too expensive | plans/piles/conductor/batch-2-cmp3-classes.md:13 | carry | «Вызывается роль только для каких-то бюрократических процедур? Это слишком дорого» 13.10.2026 20:20 | — | T57 |
| a10 | A:craft:outcome | P1: code helps the role, never replaces it; on the unforeseen code reports, does not stop the factory | docs/OWNER_PRINCIPLES.md:7-8 | carry | P1, no date in text | a01 | T47 |
| a11 | A:craft:means | P2: factory is universal; do not turn into code what meets project variety | docs/OWNER_PRINCIPLES.md:9 | carry | P2, no date | a01 | T47 |
| a12 | A:craft:outcome | P22: factory cannot cope -> calls conductor, options with price and consequences; worst allowed is unplanned spend, never a stall; self-investigate before asking | docs/OWNER_PRINCIPLES.md:80-92 | carry | 09.10 (D-0039) and 02.11.2026 | c09 | T47 |
| a13 | A:craft:outcome | P13: a person's word passes any gate, recorded as a finding | docs/OWNER_PRINCIPLES.md:32 | carry | P13, no date | — | T47 |
| a14 | A:craft:outcome | P15: refusal says what is wrong and what is expected; every ban has a door; trapped role writes a finding | docs/OWNER_PRINCIPLES.md:34-35 | carry | P15, no date | c04 | T47 |
| a15 | A:craft:outcome | P5: unreachable (probe-established) is a default gap and report line, no question; one decision covers its class | docs/OWNER_PRINCIPLES.md:13-20 | carry | 01.10 and 13.10 (D-0043, D-0047) | a08 | T47 |
| a16 | A:craft:outcome | P20: code is never the oracle; expectation from requirements; silent requirements -> question, until then unresolved | docs/OWNER_PRINCIPLES.md:65-71 | carry | 01.10 (FR-58) | — | T47 |
| a17 | A:craft:means | P27: code owns data, role owns judgement, person owns intent | docs/OWNER_PRINCIPLES.md:128-134 | carry | 03.11.2026 | — | T47 |
| a18 | A:craft:outcome | P31: different work paths for the same thing is a bug; exception only by owner word | docs/OWNER_PRINCIPLES.md:151-152 | carry | 06.11.2026; also «надо что бы всё было единообразно» (plans/piles/thinking-roles/README.md:90) | d02 | T47,T02 |
| a19 | A:craft:outcome | P21: delivery has three outcomes; third is ready after the person finishes checks, with a Left-with-you section | docs/OWNER_PRINCIPLES.md:72-79 | carry | 02.10 and 03.10 | — | T47 |
| a20 | A:craft:knowledge | P16/P17: fewest e2e, parameterize; case says WHAT, automator decides HOW; many-to-many | docs/OWNER_PRINCIPLES.md:36-47 | carry | 30.09, 04.11.2026 | c08 | T47 |
| a21 | A:craft:knowledge | P26: agent walks manual case, code records evidence, verdict must cite recorded evidence; analyst walks every doubtful place | docs/OWNER_PRINCIPLES.md:111-124 | carry | 02.11, 04.11, 05.11.2026 | c02 | T47 |
| a22 | A:craft:knowledge | P29/P30: independent checks do not hide each other; red probe substitutes the broken product's value | docs/OWNER_PRINCIPLES.md:143-150 | carry | 06.11.2026 | c06 | T47 |
| a23 | A:craft:outcome | P24: regression is found and handed over, not run; list correct on the first and only run | docs/OWNER_PRINCIPLES.md:102-106 | carry | 30.10.2026 | — | T47 |
| a24 | A:craft:outcome | Page size limit: requirements told before work may exceed it if rules demand | plans/piles/told-before-work/README.md:69 | carry | «не в ущерб правилам. Если не влезет можно поднять» 17.11.2026 | d04 | T04 |
| a25 | A:craft:outcome | Onboarding asks at most 10 core questions; rest at first need once; answers remembered; new knowledge kind is a row | plans/project-knowledge-plan.md:4-7 | carry | owner 10.11.2026 (paraphrase in plan, verbatim not opened) | c03 | T50,T24 |
| a26 | A:craft:means | Run in parallel by default, sequential only if impossible; parallel_windows 3 | plans/piles/thinking-roles/README.md:124 | carry | «По умолчанию запускаем в параллели и только если это не возможно, то последовательно» 06.11.2026 | c02 | T02 |
| a27 | A:craft:outcome | Typed input as a human types (char by char) so the factory itself finds such bugs | plans/piles/execution-probes/README.md:130 | carry | «чтобы фабрика сама нашла все эти 3 бага» 31.10.2026 | c06 | T58 |
| a28 | A:craft:outcome | One architecture for no-code and one-side runs, not different implementations in different places | docs/tasks/specs/t-2181-pre-code-and-one-side-runs.md:16-18 | carry | owner 10.11.2026 (English in spec) | c07 | T51 |
| a29 | A:process:means | New owner idea order: lead understands, scouts, mismatch questions, short plan to owner, designer, plan critic, parallel streams, code critic | PROJECT.md:112-133 | carry | owner 11.11.2026 | — | T46 |
| a30 | A:craft:outcome | Run-honesty: unknown is never counted as pass; one broken module must not stop collection; no release with red canon | plans/piles/run-honesty/README.md:7 | carry | owner 27.10.2026 (assembled batch) | c05 | T05,T59 |
| c01 | pile-depth | universality: role-first; one predicate per place (triageable_not_executed, run_witness_excused, executor_install); 12 of 14 nodes accepted; live proofs L1-L6 still waiting | plans/piles/universality/README.md:1-77 | batch 1 of 1; README row says ожидает | owner 17.11.2026 | a01,a02,d05 | T01,T38,T43 |
| c02 | pile-depth | thinking-roles: roles think right, our code hinders; walker verdicts, probes into target, parallel windows 3; batches 1-4 closed, 5-6 waiting; TR5-5 fork open | plans/piles/thinking-roles/README.md:1-126 | 6 batches: 4 закрыта, 2 ожидает | owner 05-06.11.2026 | a21,a26,d02 | T02 |
| c03 | pile-depth | project-knowledge: one catalog row per fact (key, about, store, ask_when, derive); batch 1 closed, batch 2 in work, phases 1-6 moved to OF3 | plans/piles/project-knowledge/README.md:1-91 | batch 1 закрыта; batch 2 в работе (dev1, 19.11.2026) | owner 10-11.11.2026 | a25 | T03,T50 |
| c04 | pile-depth | told-before-work: every refusal names its requirement row id, role sees it before work; 119 unsited rows; M9 resume experiment not run | plans/piles/told-before-work/README.md:1-70 | 1 batch, в работе (dev1, 19.11.2026), 15 nodes | owner 13.11 and 17.11.2026 | a06,a24 | T04,T48,T49 |
| c05 | pile-depth | run-honesty: unknown never pass, broken module no longer stops collection, red canon fixed; open moved 01.11.2026 to four other piles | plans/piles/run-honesty/README.md:1-68 | 2 batches, both закрыта (0fa13e6e, 855d4e5c) | owner 27.10.2026 | a30,d01 | T05,T59 |
| c06 | pile-depth | execution-probes: one runner predicate, probe for any language/runner, config_sha by profile projection; batches 1-3 closed, batch 4 waiting | plans/piles/execution-probes/README.md:1-70 | 4 batches: 3 закрыта, 1 ожидает | owner 28-31.10.2026 | a22,a27 | T06,T58 |
| c07 | pile-depth | pre-code: one scheme for no-code, one-side, as-before; assumptions A1..An in one register; batch 4 (12 nodes) in work | plans/piles/pre-code/README.md:1-70 | 4 batches: 1-2 закрыта, 3 ожидает, 4 в работе (24.11.2026) | owner 10.11.2026 | a28 | T07,T51,T52 |
| c08 | pile-depth | test-code-quality: 17 Codex review points to 8 classes K1-K8, one mechanism per class; rules existed, execution did not | plans/piles/test-code-quality/README.md:1-70 | 2 batches: 1 закрыта (855d4e5c), 2 ожидает | owner 20.10.2026 | a20 | T08 |
| p01 | pile | universality: factory passes all stages unstuck; idea role-first plus one question with doors; top file README | plans/piles/universality/README.md | 1 batch, README ожидает, batch file nodes mostly принято | — | c01 | T01 |
| p02 | pile | thinking-roles: manual walk and analyst remainders, probes, parallel windows; idea: roles right, code hinders | plans/piles/thinking-roles/README.md | 6 batches, 4 закрыта | — | c02 | T02 |
| p03 | pile | project-knowledge: one scheme ask-at-first-need and remember; idea: catalog row per knowledge kind | plans/piles/project-knowledge/README.md | 2 batches: 1 закрыта, 2 в работе | — | c03 | T03 |
| p04 | pile | told-before-work: refusals name requirement row id; idea single told mechanism | plans/piles/told-before-work/README.md | 1 batch в работе | — | c04 | T04 |
| p05 | pile | run-honesty: next release after 0.10.3, unknown not pass; idea named-remainder to human | plans/piles/run-honesty/README.md | 2 batches закрыта | — | c05 | T05 |
| p06 | pile | execution-probes: probe works in any language, one runner definition | plans/piles/execution-probes/README.md | 4 batches: 3 закрыта | — | c06 | T06 |
| p07 | pile | pre-code: runs without code, one side, as before; assumptions register | plans/piles/pre-code/README.md | 4 batches: 2 закрыта, 1 в работе | — | c07 | T07 |
| p08 | pile | test-code-quality: tests factory writes must discriminate; class-level code gates | plans/piles/test-code-quality/README.md | 2 batches: 1 закрыта | — | c08 | T08 |
| p09 | pile | conductor: P22 principle, call conductor with options and prices at any unforeseen state; no silent pass | plans/piles/conductor/README.md | 5 batches, all закрыта | owner 09.10, 13.10.2026 | a12 | T09 |
| p10 | pile | codex: port dev2 branch fixes so Codex runs do not stall; batch 3 doctor smoke Windows waiting | plans/piles/codex/README.md | 3 batches: 2 закрыта, 1 ожидает | owner 19.10.2026 (one pile, no L cap) | — | T10 |
| p11 | pile | collect: project data back to factory developers in one redacted archive; no design idea beyond that | plans/piles/collect/README.md | 4 batches: 3 закрыта, 1 ожидает | — | — | T11 |
| p12 | pile | cost-dashboard: one true task price (P18), no $0 as fact | plans/piles/cost-dashboard/README.md | 2 batches закрыта | — | a23 | T12 |
| p13 | pile | driver-controller: headless run must not lose work at seams; correct next controller step | plans/piles/driver-controller/README.md | 1 batch закрыта; open moved 01.11.2026 | — | — | T13 |
| p14 | pile | driver-hosts: remnants of driver seams, collector intake, gate texts; rebuilt from 97 old nodes | plans/piles/driver-hosts/README.md | 2 batches, both ожидает | owner 01.11.2026 (backlog rebuild) | — | T14 |
| p15 | pile | execution-report: execution, proofs, delivery report from one carrier; 53 plus 55 nodes | plans/piles/execution-report/README.md | 2 batches, both ожидает | owner 29.10 and 01.11.2026 | — | T15 |
| p16 | pile | exploratory: qa-explore skill finds requirements and code of a feature, coverage matrix, charters | plans/piles/exploratory/README.md | 3 batches: 2 закрыта, 1 ожидает | — | — | T16 |
| p17 | pile | gates-and-words: person answers at gates in words; words reach all readers equally | plans/piles/gates-and-words/README.md | 1 batch закрыта | — | a13 | T17 |
| p18 | pile | github-move: forge to private GitHub, release to public, one clean commit | plans/piles/github-move/README.md | 3 batches закрыта | — | — | T18 |
| p19 | pile | grounding: MR vs requirements and blast radius before first test; code gives clues, role judges | plans/piles/grounding/README.md | 3 batches (batch 3 закрыта; others not read) | — | a17 | T19,T62 |
| p20 | pile | hotfix-12586: urgent repair of run TP1-12586 on 0.10.0 | plans/piles/hotfix-12586/README.md | 9 status cells, batch 1 закрыта; rest not read | owner 23.10.2026 | — | T20 |
| p21 | pile | kb: knowledge-base pages updated to current factory state | plans/piles/kb/README.md | 2 batches закрыта | owner 13.10.2026 | — | T21 |
| p22 | pile | live-run-fvf: findings of live run factory vs free agent (13 min vs 1.5 h, 10+ stops) | plans/piles/live-run-fvf/README.md | 3 batches: 1-2 ожидает, 3 в работе | owner: «создай кучку находок по живому прогону… пополняй по мере прохождения прогона» | a03 | T22 |
| p23 | pile | live-runs: live proofs on unfamiliar projects and non-Python | plans/piles/live-runs/README.md | 2 batches: 1 закрыта, 2 ожидает | — | — | T23 |
| p24 | pile | onboarding-forge: onboarding, role context readers, forge process; batch 3 = project-knowledge phases | plans/piles/onboarding-forge/README.md | 5 batches: 1-4 в работе, 5 ожидает | owner 01.11.2026 | c03 | T24 |
| p25 | pile | package-ci: package green on Linux and second Windows, stable tests in time limit | plans/piles/package-ci/README.md | 4 batches: 1-2 закрыта, 3-4 ожидает | owner 12.11.2026 (TD-15 quarantine deletion) | — | T25 |
| p26 | pile | proposals: receiving pile for suggestions and foreign adaptations; no code zone | plans/piles/proposals/README.md | 1 batch закрыта | — | — | T26 |
| p27 | pile | regression: correct regression list from the first run (P24) | plans/piles/regression/README.md | 1 batch закрыта | owner 30.10.2026 | a23 | T27 |
| p28 | pile | release-next: queue for release 0.10.9; batch 2 one bug N1-N8 waits for live rerun | plans/piles/release-next/README.md | 2 batches: 1 закрыта, 2 ожидает | owner 01.11.2026 | — | T28 |
| p29 | pile | report-delivery: report must not show pass on red; delivery reasons have owners | plans/piles/report-delivery/README.md | 2 batches: 1 закрыта, 2 ожидает | — | a19 | T29 |
| p30 | pile | roles-context: roles read less and more precisely; P16/P17 into role charters | plans/piles/roles-context/README.md | 2 batches: 1 закрыта, 2 ожидает | — | d04 | T30 |
| p31 | pile | speed-cost: S0-S4 twice cheaper and faster; one true price | plans/piles/speed-cost/README.md | 6 batches: 1-5 закрыта, 6 ожидает | — | d06 | T31,T63 |
| p32 | pile | stand-and-sources: HTTP errors read correctly, one stand identity, Jira via API | plans/piles/stand-and-sources/README.md | 1 batch закрыта | — | — | T32 |
| p33 | pile | _template: pile card template (title, zone grammar, Зачем) | plans/piles/_template/README.md | template | — | — | T33 |
| p34 | pile | words-gates: person's words reach every reader; gate cards do not hand the person factory's choices | plans/piles/words-gates/README.md | 1 batch ожидает (41 nodes) | — | a13 | T34 |
| p35 | pile | rules-debt: 14 gates in gate-registry.json move to converted so unknown does not pass | plans/piles/rules-debt/README.md | 1 batch ожидает (24 nodes) | — | d01 | T35 |
| p36 | pile | forge: dev system, teamwork, piles and batches, critic checks, CI reading | plans/piles/forge/README.md | 7 batches: 1-6 закрыта, 7 ожидает | owner 09.10, 14.10.2026 | — | T36 |
| p37 | pile | onboarding-hooks: guard knows shell bypasses and hard links; one test-file and artifact-root definition | plans/piles/onboarding-hooks/README.md | 10 status cells; 1-3 закрыта, 4-5 в работе; rest not read | — | — | T37 |
| p38 | meta | Glob found 37 README folders (36 piles plus _template) while the dispatch says 34 piles; no pile without a top file | plans/piles | found 37 | — | — | T40 |
| d01 | contradiction | run-honesty and rules-debt refuse unknown as pass; universality says blocking never acceptable, role goes on; reconciled only by wording | plans/piles/run-honesty/README.md:7 ; plans/piles/universality/README.md:9-11 | open | — | p35 | T05,T01,T35 |
| d02 | contradiction | thinking-roles TR5-5 recommends keeping two roads to one registry; owner principle P31 calls different paths a bug | plans/piles/thinking-roles/README.md:122 ; docs/OWNER_PRINCIPLES.md:151 | open, pile asks owner | — | a18 | T02,T47 |
| d03 | contradiction | roles-context: prompt diet, ceilings A22/A25 only go down; told-before-work adds rows to pages and lets limit rise | plans/piles/roles-context/README.md:14-18 ; plans/piles/told-before-work/README.md:69 | open | — | a24 | T30,T04 |
| d04 | contradiction | Status lag: universality README says U1-1 в работе, U1-8 в работе and batch ожидает; batch file shows them принято | plans/piles/universality/README.md:34,57-67 ; plans/piles/universality/batch-1-pass-without-stuck.md:27-40 | open | — | c01 | T01,T38 |
| d05 | contradiction | speed-cost target is twice faster and cheaper (26.10); owner 13.11 allows factory to be slower for checking | plans/piles/speed-cost/README.md:7-10 ; docs/tasks/specs/20261113-plan-fabrika-ne-huzhe-agenta.md:9 | open | — | a04 | T31,T53 |
| e01 | open | CLI-only or desktop-only project: recorder cannot reach the surface, manual case reads «нет» (walked false); no owner word | plans/piles/universality/batch-1-pass-without-stuck.md:45-46 | open | — | c01 | T38 |
| e02 | open | TR5-5: two roads to the observation registry or one (about six nodes); owner word missing | plans/piles/thinking-roles/README.md:122 | open | — | d02 | T02 |
| e03 | open | Live proofs L1-L6 and E-7 wait for a stand; ao3 run 24-25.11 reached only L1 and L5, stopped at S5 | plans/piles/universality/batch-1-pass-without-stuck.md:58-64 ; experiments/ao3-wrapper/factory-vs-free-agent/notebook.md:27-34 | open | — | c01 | T38,T43 |
| e04 | open | Three forks of pre-code PC2-1 (first look) marked open; owner decided only place A and two dead-feature outcomes | plans/piles/pre-code/README.md:56 | open | owner 10.11.2026 | c07 | T07 |
| e05 | open | project-knowledge PK2-7, PK2-8: text to the person and price of the default-login question need an owner weighing | plans/piles/project-knowledge/README.md:52-53 | open | — | c03 | T03 |
| e06 | open | config_sha by profile: enabling waits for owner word (EP2-1 release after 0.10.4) | plans/piles/execution-probes/README.md:43 | open | — | c06 | T06 |
| e07 | open | No measurable threshold for beat the free agent was found in the lines read of the plan (numbers only as facts) | docs/tasks/specs/20261113-plan-fabrika-ne-huzhe-agenta.md:17-26 | not found in 1-70 | — | a04 | T53 |
| e08 | open | Which of P1-P31 apply to a light factory is not marked anywhere in the file read | docs/OWNER_PRINCIPLES.md:1-153 | not marked | — | — | T47 |

## Trail
| tid | op | target | pattern / range | flags | result | control |
|---|---|---|---|---|---|---|
| T01 | read | plans/piles/universality/README.md | 1-77 | — | read plans/piles/universality/README.md:1-77 | — |
| T02 | read | plans/piles/thinking-roles/README.md | 1-126 | — | read plans/piles/thinking-roles/README.md:1-126 | — |
| T03 | read | plans/piles/project-knowledge/README.md | 1-91 | — | read plans/piles/project-knowledge/README.md:1-91 | — |
| T04 | read | plans/piles/told-before-work/README.md | 1-70 | — | read plans/piles/told-before-work/README.md:1-70 | — |
| T05 | read | plans/piles/run-honesty/README.md | 1-68 | — | read plans/piles/run-honesty/README.md:1-68 | — |
| T06 | read | plans/piles/execution-probes/README.md | 1-70 | — | read plans/piles/execution-probes/README.md:1-70 | — |
| T07 | read | plans/piles/pre-code/README.md | 1-70 | — | read plans/piles/pre-code/README.md:1-70 | — |
| T08 | read | plans/piles/test-code-quality/README.md | 1-70 | — | read plans/piles/test-code-quality/README.md:1-70 | — |
| T09 | read | plans/piles/conductor/README.md | 1-35 | — | read plans/piles/conductor/README.md:1-35 | — |
| T10 | read | plans/piles/codex/README.md | 1-35 | — | read plans/piles/codex/README.md:1-35 | — |
| T11 | read | plans/piles/collect/README.md | 1-35 | — | read plans/piles/collect/README.md:1-35 | — |
| T12 | read | plans/piles/cost-dashboard/README.md | 1-35 | — | read plans/piles/cost-dashboard/README.md:1-35 | — |
| T13 | read | plans/piles/driver-controller/README.md | 1-35 | — | read plans/piles/driver-controller/README.md:1-35 | — |
| T14 | read | plans/piles/driver-hosts/README.md | 1-35 | — | read plans/piles/driver-hosts/README.md:1-35 | — |
| T15 | read | plans/piles/execution-report/README.md | 1-35 | — | read plans/piles/execution-report/README.md:1-35 | — |
| T16 | read | plans/piles/exploratory/README.md | 1-35 | — | read plans/piles/exploratory/README.md:1-35 | — |
| T17 | read | plans/piles/gates-and-words/README.md | 1-30 | — | read plans/piles/gates-and-words/README.md:1-30 | — |
| T18 | read | plans/piles/github-move/README.md | 1-30 | — | read plans/piles/github-move/README.md:1-30 | — |
| T19 | read | plans/piles/grounding/README.md | 1-30 | — | read plans/piles/grounding/README.md:1-30 | — |
| T20 | read | plans/piles/hotfix-12586/README.md | 1-30 | — | read plans/piles/hotfix-12586/README.md:1-30 | — |
| T21 | read | plans/piles/kb/README.md | 1-30 | — | read plans/piles/kb/README.md:1-30 | — |
| T22 | read | plans/piles/live-run-fvf/README.md | 1-30 | — | read plans/piles/live-run-fvf/README.md:1-30 | — |
| T23 | read | plans/piles/live-runs/README.md | 1-30 | — | read plans/piles/live-runs/README.md:1-30 | — |
| T24 | read | plans/piles/onboarding-forge/README.md | 1-30 | — | read plans/piles/onboarding-forge/README.md:1-30 | — |
| T25 | read | plans/piles/package-ci/README.md | 1-30 | — | read plans/piles/package-ci/README.md:1-30 | — |
| T26 | read | plans/piles/proposals/README.md | 1-30 | — | read plans/piles/proposals/README.md:1-30 | — |
| T27 | read | plans/piles/regression/README.md | 1-30 | — | read plans/piles/regression/README.md:1-30 | — |
| T28 | read | plans/piles/release-next/README.md | 1-30 | — | read plans/piles/release-next/README.md:1-30 | — |
| T29 | read | plans/piles/report-delivery/README.md | 1-30 | — | read plans/piles/report-delivery/README.md:1-30 | — |
| T30 | read | plans/piles/roles-context/README.md | 1-30 | — | read plans/piles/roles-context/README.md:1-30 | — |
| T31 | read | plans/piles/speed-cost/README.md | 1-30 | — | read plans/piles/speed-cost/README.md:1-30 | — |
| T32 | read | plans/piles/stand-and-sources/README.md | 1-30 | — | read plans/piles/stand-and-sources/README.md:1-30 | — |
| T33 | read | plans/piles/_template/README.md | 1-12 | — | read plans/piles/_template/README.md:1-12 | — |
| T34 | read | plans/piles/words-gates/README.md | 1-30 | — | read plans/piles/words-gates/README.md:1-30 | — |
| T35 | read | plans/piles/rules-debt/README.md | 1-30 | — | read plans/piles/rules-debt/README.md:1-30 | — |
| T36 | read | plans/piles/forge/README.md | 1-30 | — | read plans/piles/forge/README.md:1-30 | — |
| T37 | read | plans/piles/onboarding-hooks/README.md | 1-30 | — | read plans/piles/onboarding-hooks/README.md:1-30 | — |
| T38 | read | plans/piles/universality/batch-1-pass-without-stuck.md | 1-68 | — | read plans/piles/universality/batch-1-pass-without-stuck.md:1-68 | — |
| T39 | glob | plans/piles/universality | `plans/piles/universality/**` | files | found 2; plans/piles/universality/README.md, plans/piles/universality/batch-1-pass-without-stuck.md | — |
| T40 | glob | C:\QAFactory\forge-repo | `plans/piles/*/README.md` | files | found 37; plans/piles/conductor/README.md | — |
| T41 | glob | C:\QAFactory\forge-repo | `plans/piles/*` | files | absent | T40 |
| T42 | grep | C:\QAFactory\forge-repo | `не вставала` | -i content glob=*.md | found 2; experiments/ao3-wrapper/factory-vs-free-agent/notebook.md:18 | — |
| T43 | read | experiments/ao3-wrapper/factory-vs-free-agent/notebook.md | 1-60 | — | read experiments/ao3-wrapper/factory-vs-free-agent/notebook.md:1-60 | — |
| T44 | read | docs/tasks/specs/20261117-u7-pass-without-stuck-spec-r3.md | 1-90 | — | read docs/tasks/specs/20261117-u7-pass-without-stuck-spec-r3.md:1-90 | — |
| T45 | read | PROJECT.md | 58-63 | — | read PROJECT.md:58-63 | — |
| T46 | read | PROJECT.md | 112-133 | — | read PROJECT.md:112-133 | — |
| T47 | read | docs/OWNER_PRINCIPLES.md | 1-153 | — | read docs/OWNER_PRINCIPLES.md:1-153 | — |
| T48 | read | docs/tasks/specs/20261117-told-before-work-finish-spec.md | 1-50 | — | read docs/tasks/specs/20261117-told-before-work-finish-spec.md:1-50 | — |
| T49 | read | docs/tasks/specs/20261113-told-before-work-mechanism-spec.md | 1-45 | — | read docs/tasks/specs/20261113-told-before-work-mechanism-spec.md:1-45 | — |
| T50 | read | plans/project-knowledge-plan.md | 1-60 | — | read plans/project-knowledge-plan.md:1-60 | — |
| T51 | read | docs/tasks/specs/t-2181-pre-code-and-one-side-runs.md | 1-45 | — | read docs/tasks/specs/t-2181-pre-code-and-one-side-runs.md:1-45 | — |
| T52 | read | docs/tasks/specs/20261124-assumptions-spec-r2.md | 1-40 | — | read docs/tasks/specs/20261124-assumptions-spec-r2.md:1-40 | — |
| T53 | read | docs/tasks/specs/20261113-plan-fabrika-ne-huzhe-agenta.md | 1-70 | — | read docs/tasks/specs/20261113-plan-fabrika-ne-huzhe-agenta.md:1-70 | — |
| T54 | grep | experiments/mybooks/thinking-roles/walker-vs-plain-agent.md | `«` | content | found 25; experiments/mybooks/thinking-roles/walker-vs-plain-agent.md:7 | — |
| T55 | grep | plans/piles | `«[^»]{30,}»` | content glob=**/README.md | found 50; plans/piles/collect/README.md:20 | — |
| T56 | grep | plans/piles | `«[^»]{30,}»` | content glob=**/batch-*.md | found 70; plans/piles/codex/batch-1-overhead-fixes.md:79 | — |
| T57 | read | plans/piles/conductor/batch-2-cmp3-classes.md | 5-16 | — | read plans/piles/conductor/batch-2-cmp3-classes.md:5-16 | — |
| T58 | read | plans/piles/execution-probes/README.md | 112-135 | — | read plans/piles/execution-probes/README.md:112-135 | — |
| T59 | read | plans/piles/run-honesty/batch-1-run-honesty.md | 1-30 | — | read plans/piles/run-honesty/batch-1-run-honesty.md:1-30 | — |
| T60 | glob | C:\QAFactory\forge-repo | `plans/piles/{thinking-roles,project-knowledge,told-before-work,run-honesty,execution-probes,pre-code,test-code-quality}/*.md` | files | found 28; plans/piles/execution-probes/batch-1-one-runner.md | — |
| T61 | grep | plans/piles | `\| (закрыта\|ожидает\|в работе\|сдано\|принято) \|` | count glob=**/README.md | count 118 | — |
| T62 | grep | plans/piles/grounding/README.md | `^\| [0-9]+ \| .*\| (закрыта\|ожидает\|в работе\|сдано\|принято) \|` | content | found 3; plans/piles/grounding/README.md:80-82 | — |
| T63 | grep | plans/piles/speed-cost/README.md | `^\| [0-9]+ \| .*\| (закрыта\|ожидает\|в работе\|сдано\|принято) \|` | content | found 6; plans/piles/speed-cost/README.md:26-31 | — |

## Forks
Whether the built part of each of the eight piles is a design change or a set of patches is a judgement and is not given. Facts for the decider. Pile's own wording: told-before-work, project-knowledge, pre-code and test-code-quality call themselves a mechanism, scheme or "one mechanism per class" (T04, T03, T07, T08). Node shapes: told-before-work batch 1 is 15 nodes cut per refusal family (T48); universality is 14 nodes cut per flow of one spec (T38); thinking-roles and run-honesty are per-defect findings with a few consolidation nodes such as TR4-2 and TR4-14 (T02, T05). Built-versus-open state is in rows c01-c08. Also open for the owner: d01-d03 and d05 above.
this needs a decision from a tier above.

## Not done
- Of ~1344 files, opened: 37 README files (partly: only the first 30-35 lines of the 29 piles outside the eight, first 70 lines of execution-probes, pre-code and test-code-quality, whole file for the other five named piles), 1 universality batch file, 1 conductor batch file (12 lines), 1 run-honesty batch file (30 lines).
- Not opened: the batch files of thinking-roles, project-knowledge, told-before-work, execution-probes, pre-code, test-code-quality (list in T60), every `findings/` folder, and the `Содержание` tables of 29 piles. The batch files named in the question for the eight piles were therefore NOT read (the briefs were read only as README `Бриф пачки` text).
- Per-pile file counts were not measured. Piles with batch rows beyond the lines read: grounding (only batch 3 status read), hotfix-12586 (9 status cells, only batch 1 read), onboarding-hooks (10 cells, batches 1-5 read), speed-cost (6 batches read from the table).
- Owner's quoted words were taken from README/batch/spec text; most of the owner statements outside the eight piles (forge, grounding, hotfix, collect and others) were not extracted. T55 and T56 hit the head limits (50 and 70), so more quotes exist. The long A-lines for P1-P31 carry the principle text, not a date unless the file gives one.
- The Russian original of the 17.11.2026 universality goal ("verbatim in the brief") was not located: `docs/tasks/specs/20261117-u7-pass-without-stuck-brief.md` was not opened. The 24.11.2026 notebook states that the factory-vs-free-agent plan sits in `docs/tasks/specs/20261124-mocks-plan.md` (answers 7 and 11), also not opened.
- Two Grep calls with `glob=*/README.md` and `glob=*/batch-*.md` returned nothing (miscall: the glob form) and were rerun with `**/` (T55, T56). A Grep with a braces glob on five READMEs also returned nothing and was replaced by T61-T63. The T42 search stopped at a time limit, so more matches may exist.
- Stray or number-named entries in pile folders were not checked: only README and the glob in T60 and T39 were listed.
- Analogs (rule 8): status lag of the d04 kind (a README table behind its batch file) was not looked for in other piles; the README of gates-and-words:18 says "проверить по коду" about a closed finding, unresolved there.
