<!-- scout hand-back, journal task t-1905, recon for docs/tasks/specs/20261125-forge2-light-factory-plan.md; saved verbatim from the worker's final message -->

digest: v1 forge2-recon-pass2-live-run-fvf

Method. Node rows lie at batch-1 lines 34-63 and batch-3 lines 30-84. Each was read whole, and no row was cut by a read window. The 4-column "Живые доказательства" table (batch-1:103, batch-3:98) is not a node table and was not read. Paths are relative to C:\QAFactory\forge-repo. B1 means plans/piles/live-run-fvf/batch-1-live-run-fvf.md. B3 means plans/piles/live-run-fvf/batch-3-live-run-fvf.md. Letters are the origin rule; a double letter counts once for each letter, so letter counts exceed row counts.

Counts in the owner's table (1) are given as Objects rows c1 to c3.

## Objects
| id | kind | gist | paths | status | owner | links | ev |
|---|---|---|---|---|---|---|---|
| c1-b1 | count | B1: 30 node rows in file, 30 classified, gap 0 | B1:34-63 | — | — | — | t3,t4 |
| c1-b3 | count | B3: 55 node rows in file, 55 classified, gap 0 (7 none, 2 unclear) | B3:30-84 | — | — | — | t5,t6,t7,t8,t9 |
| c1-sum | count | Total 85 rows read, 85 classified; sum 30+55=85, equals given counts | B1:34-63 | — | — | c1-b1,c1-b3 | t3,t4,t5,t6,t7,t8,t9 |
| c2-M | count | Origin M: 66 rows (B1 24, B3 42) | B1:34-63 | — | — | — | t3,t4,t5,t6,t7,t8,t9 |
| c2-H | count | Origin H: 15 rows (B1 11, B3 4); no H-only rows except FV1-26 | B1:34-63 | — | — | — | t3,t4,t5,t6,t7,t8,t9 |
| c2-V | count | Origin V: 8 rows (B1 5, B3 3) | B1:34-63 | — | — | — | t3,t4,t5,t6,t7,t8,t9 |
| c2-T | count | Origin T: 6 rows (all B1: FV1-10,20,23,24,25,29) | B1:34-63 | — | — | — | t3,t4 |
| c2-E | count | Origin E: 2 rows (B3: FV3-39, FV3-35d), both with M | B3:71,84 | — | — | — | t8,t9 |
| c2-C | count | Origin C: 1 row (B3: FV3-43) | B3:76 | — | — | — | t8 |
| c2-F | count | Origin F (dev process): 0 rows; no node names dispatch, acceptance, journal or merge as the problem | B1:34-63 | — | — | — | t3,t4,t5,t6,t7,t8,t9 |
| c2-none | count | Origin none: 7 rows: FV3-1,4,6,7,8,9,10 (landing, CI job, walk-row chores) | B3:30-40 | — | — | — | t5 |
| c2-unclear | count | Origin unclear: 2 rows FV3-13, FV3-13b (text names no problem, only a mechanism) | B3:43,67 | — | — | — | t5,t6,t7 |
| cls-b1 | classification | B1 per node: 1M 2HM 3HM 4HM 5VM 6M 7MH 8HM 9HM 10TM 11VM 12M 13HM 14M 15VM 16HM 17V 18M 19VM 20TM 21M 22M 23TH 24T 25T 26H 27M 28M 29T 30HM | B1:34-63 | — | — | — | t3,t4 |
| cls-b3a | classification | B3 per node: 1none 15M 2M 3M 4none 5M 6-9none 10none 11V 12V 13unclear 14M 16HM 17M 18M 19M 20M 21HM 22M 23M | B3:30-52 | — | — | — | t5,t6 |
| cls-b3b | classification | B3 per node: 24M 25M 26M 27M 28M 29M 30M 31M 32M 33M 34HM 35M 36M 37HM 13b-unclear 35b2M 35b3M 38M 39ME 40M 41M | B3:53-73 | — | — | — | t6,t7,t8 |
| cls-b3c | classification | B3 per node: 11bV 42M 43C 44M 45M 26bM 26cM 26dM 26nM 26s9M 35dME | B3:74-84 | — | — | — | t8,t9 |
| T-1 | problem-T | S1 did not take an export named in the story text | B1:43 | — | — | FV1-10 | t4 |
| T-2 | problem-T | Code critic closed review with no sensitivity probes; conductor then falsely said the factory cannot make probes | B1:51 | — | — | FV1-20 | t4 |
| T-3 | problem-T | Product docs from the app repo missing from the requirements registry | B1:52 | — | — | FV1-23 | t4 |
| T-4 | problem-T | Manual-pass bug drafts not brought to a verdict; draft rests on a derived expectation, no question | B1:53 | — | — | FV1-24 | t4 |
| T-5 | problem-T | No automated test fails on a bug found by the manual pass; no path from bug to failing test | B1:54 | — | — | FV1-25 | t4 |
| T-6 | problem-T | Automator has no way to look at the stand when first look is empty or wrong; selector shortage stalls it | B1:62 | — | — | FV1-29 | t4 |
| V-1 | problem-V | Stand login is a page where POST /login gives 405; probe says stand not responding, onboarding records "login by code impossible" | B1:38,47,49 | — | — | FV1-5,FV1-15,FV1-17 | t4 |
| V-2 | problem-V | Ticket without a "# " heading stops S0 | B1:44 | — | — | FV1-11 | t4 |
| V-3 | problem-V | Obligation marker is read only from Python, so a .spec.ts cannot produce obligation_refs | B1:58 | — | — | FV1-19 | t4 |
| V-4 | problem-V | Dry story covers one runner and few project types; TS/Playwright row and more types come as projects arrive | B3:41,42,74 | — | — | FV3-11,FV3-12,FV3-11b | t6,t7,t8 |
| H-1 | problem-H | A person's word has no executor in the conductor: S5 scope, "go on", 7 precheck families not passable by word, "без стенда" | B1:35,45,63; B3:50 | — | — | FV1-2,FV1-13,FV1-30,FV3-21 | t4,t6,t7 |
| H-2 | problem-H | Free answer, or chosen variant, does not reach the role or conductor; the question is asked again (third time in FV1-13) | B1:36,45; B3:45,63,66 | — | — | FV1-3,FV1-13,FV3-16,FV3-34,FV3-37 | t4,t6,t7 |
| H-3 | problem-H | Brief cut on the fly cuts the person's words | B1:37 | — | — | FV1-4 | t4 |
| H-4 | problem-H | Question pack has repeats, no sources of options, and shows "cannot answer as is" to the person | B1:42 | — | — | FV1-9 | t4 |
| H-5 | problem-H | Gate A shown before ready ("S5 can start: no"); gate A demands an answer deferred "until report" | B1:40,41 | — | — | FV1-7,FV1-8 | t4 |
| H-6 | problem-H | Person asked what could be found: whether the stand runs the test-repo commit; owner asked about what is recorded | B1:48,52 | — | — | FV1-16,FV1-23 | t4 |
| H-7 | problem-H | "Could not verify" mixes real impossibility with the factory's own unfinished work | B1:55 | — | — | FV1-26 | t4 |
| C-1 | problem-C | Dry-story part s5 outgrew its CI time limit (30 to 54 min), and the log has no time per row | B3:76 | — | — | FV3-43 | t8 |
| ME-k1 | M-subkind | form/hand-off shape: 9 rows; examples FV1-1 (P-n vs TS-n), FV1-19, FV3-19 | B1:34 | — | — | FV1-1,FV1-14,FV1-19,FV1-28,FV1-4,FV3-19,FV3-20,FV3-31,FV3-32 | t3,t6,t7 |
| ME-k2 | M-subkind | guard or hook refusal: 3 rows; examples FV1-18, FV1-27, FV3-41 | B1:50 | — | — | FV1-18,FV1-27,FV3-41 | t4,t8 |
| ME-k3 | M-subkind | state/lock/staleness: 4 rows; examples FV1-15, FV3-15, FV3-2 (FV3-35b2 lost round) | B3:31 | — | — | FV1-15,FV3-15,FV3-2,FV3-35b2 | t4,t5,t8 |
| ME-k4 | M-subkind | driver or conductor seam: 24 rows; examples FV1-2, FV1-22, FV3-22 | B1:35 | — | — | FV1-2,FV1-3,FV1-6,FV1-13,FV1-20,FV1-22,FV1-30,FV3-16,FV3-21,FV3-22,FV3-24,FV3-26,FV3-29,FV3-34,FV3-35,FV3-37,FV3-35b3,FV3-26b,FV3-26c,FV3-26d,FV3-26n,FV3-26s9,FV3-39,FV3-35d | t4,t5,t6,t7,t8,t9 |
| ME-k5 | M-subkind | validator or gate verdict: 11 rows; examples FV1-5, FV1-21, FV3-44 | B1:38 | — | — | FV1-5,FV1-7,FV1-8,FV1-16,FV1-21,FV3-14,FV3-18,FV3-30,FV3-40,FV3-44,FV3-45 | t4,t5,t6,t7,t8 |
| ME-k6 | M-subkind | generated text/doc drift: 1 row, FV1-12 (S2 card and stage registry disagree) | B1:59 | — | — | FV1-12 | t4 |
| ME-k7 | M-subkind | other: 14 rows; examples FV1-9, FV1-10, FV3-3, FV3-5, FV3-17, FV3-33 (dry-world stub/walker/seed gaps) | B3:33 | — | — | FV1-9,FV1-10,FV1-11,FV3-3,FV3-5,FV3-17,FV3-23,FV3-25,FV3-27,FV3-28,FV3-33,FV3-36,FV3-38,FV3-42 | t4,t5,t6,t7,t8 |
| ME-E | E-subkind | host CLI: 2 rows (FV3-39, FV3-35d): `claude -p --resume` may end on a tool call, and resume_with writes an empty success over a saved result. No other E sub-kind occurs | B3:71,84 | — | — | FV3-39,FV3-35d | t8,t9 |
| top-1 | top-M | Person's words or chosen variant never reach an executor in driver/conductor (8 rows) | B1:35 | — | — | H-1,H-2 | t4,t6,t7 |
| top-2 | top-M | Dry-world stub, seeds or walker cannot reach a state, so rows stay red or unreachable (about 14 rows: FV3-5,17,20,23,25,28,33,35,36,38,40,42,44,45) | B3:35,49,52,62,64,65,75 | — | — | FV3-5,FV3-20,FV3-23,FV3-33,FV3-36,FV3-42 | t5,t6,t7,t8 |
| top-3 | top-M | Skill road and Driver close stages through duplicate code, or a skill-road step is missing (10 rows: FV3-22,24,26,26b,26c,26d,26n,26s9,29,41) | B3:51,53,55,58,73,79-83 | — | — | FV3-22,FV3-24,FV3-26 | t6,t7,t8 |
| top-4 | top-M | Producer and reader disagree on a form, id or field: P-n vs TS-n, obligation_hash, probes.records, inputs_read (about 10 rows) | B1:34,46,56; B3:47,48,60 | — | — | FV1-1,FV1-14,FV1-22,FV3-18,FV3-19,FV3-31 | t4,t6,t7 |
| top-5 | top-M | Ledgers, labels and counters wrong against main or the judge: stale labels, double count, C2/C3 false red (7 rows) | B3:31,32,44,72,77,78 | — | — | FV3-15,FV3-2,FV3-14,FV3-40,FV3-44,FV3-45 | t5,t7,t8 |
| ow-1 | owner-word | FV3-12: «пока так» (13.11) and «да, будем дополнять по мере поступления» (23.11) | B3:42 | — | owner | FV3-12 | t7 |
| ow-2 | owner-word | No other owner quotes. B1:59 (FV1-12) says only «замысел S2 — слово владельца», no quote. "Lead 17.11/19.11/20.11" in B3 are Lead decisions, not owner words | B3:50-84 | — | — | FV1-12 | t4,t6,t7,t8,t9 |
| rec-1 | recurrence | FV1-18 «Регрессия: ... (раньше работало)» | B1:50 | — | — | FV1-18 | t4 |
| rec-2 | recurrence | FV3-29 «Остаток R2-F2 карточки FV3-22 r2» | B3:58 | — | — | FV3-29 | t7 |
| rec-3 | recurrence | Repeats in one run: FV1-13 «спросил в третий раз»; FV1-22 «трижды повторил»; FV1-27 «три новых экземпляра» | B1:45,56,60 | — | — | FV1-13,FV1-22,FV1-27 | t4 |
| rec-4 | recurrence | A fix gave a new stop: FV3-20 «по новой причине» after N2h; FV3-23 after FV3-21; FV3-42 at S8; FV3-35 «не сработала за раунды 6-7»; FV3-36 «причина другая» | B3:49,52,64,65,75 | — | — | FV3-20,FV3-23,FV3-42,FV3-35,FV3-36 | t6,t7,t8 |
| rec-5 | recurrence | Twin or sibling of an earlier node: FV3-35d «близнец FV3-35c»; FV3-39 same resume_with defect; FV3-26b..s9 «так же, как S6» | B3:55,71,84 | — | — | FV3-35d,FV3-39,FV3-26 | t6,t8,t9 |
| an-1 | analog | The stub-hole class from FV3-20/23/42 (dry-world has no row for a role) repeats at S5, S6, S7 and S8 in one chain | B3:49,52,75 | — | — | FV3-20,FV3-23,FV3-42 | t6,t8 |
| an-2 | analog | Class "person's words written or routed without a file or executor" appears in B1 and B3 (FV1-4, FV3-37) | B1:37; B3:66 | — | — | FV1-4,FV3-37 | t4,t6 |

Remarks (ties, uncertainties). A node's own words tell the origin; where they name the mechanism but no failure, the row is `none` or `unclear` and was not guessed. FV3-11 and FV3-11b are V on the strength of the runner name alone. FV1-20 also touches H (conductor's false statement to the person); it is counted T+M. FV1-21 could be H (a misleading price label); it is counted M.

## Trail
| tid | op | target | pattern / range | flags | result | control |
|---|---|---|---|---|---|---|
| t1 | grep | plans/piles/live-run-fvf/batch-1-live-run-fvf.md | `^\|---` | content | found 2; plans/piles/live-run-fvf/batch-1-live-run-fvf.md:33, plans/piles/live-run-fvf/batch-1-live-run-fvf.md:103 | — |
| t2 | grep | plans/piles/live-run-fvf/batch-3-live-run-fvf.md | `^\|---` | content | found 2; plans/piles/live-run-fvf/batch-3-live-run-fvf.md:29, plans/piles/live-run-fvf/batch-3-live-run-fvf.md:98 | — |
| t3 | read | plans/piles/live-run-fvf/batch-1-live-run-fvf.md | 32-43 | — | read plans/piles/live-run-fvf/batch-1-live-run-fvf.md:32-43 | — |
| t4 | read | plans/piles/live-run-fvf/batch-1-live-run-fvf.md | 44-73 (rows 44-63; 64-73 are Ход, not used) | — | read plans/piles/live-run-fvf/batch-1-live-run-fvf.md:44-73 | — |
| t5 | read | plans/piles/live-run-fvf/batch-3-live-run-fvf.md | 27-41 | — | read plans/piles/live-run-fvf/batch-3-live-run-fvf.md:27-41 | — |
| t6 | read | plans/piles/live-run-fvf/batch-3-live-run-fvf.md | 42-55 | — | read plans/piles/live-run-fvf/batch-3-live-run-fvf.md:42-55 | — |
| t7 | read | plans/piles/live-run-fvf/batch-3-live-run-fvf.md | 56-69 | — | read plans/piles/live-run-fvf/batch-3-live-run-fvf.md:56-69 | — |
| t8 | read | plans/piles/live-run-fvf/batch-3-live-run-fvf.md | 70-83 | — | read plans/piles/live-run-fvf/batch-3-live-run-fvf.md:70-83 | — |
| t9 | read | plans/piles/live-run-fvf/batch-3-live-run-fvf.md | 84-98 (rows 84; 86-98 are Ход and the evidence table header, not used) | — | read plans/piles/live-run-fvf/batch-3-live-run-fvf.md:84-98 | — |

## Not done
- The "Ход" and "Живые доказательства" sections were not used for classification, per the dispatch. Their lines entered the read windows because the row tables end just above them (batch-1 lines 64-73; batch-3 lines 86-98).
- The README and the other batch files were not read. Nothing was cut by the context limit; every row was read whole.
- The pattern-count of node rows (30 and 55) was taken from the dispatch. Cross-checked by line span: batch-1 lines 34-63 give 30 rows, batch-3 lines 30-84 give 55 rows. No Grep for the count pattern was run, so there is no search-based control for it.
- Node text names no money figures that were copied. FV1-21 (B1:57) contains a price figure; it is omitted.
- The origin letters rest on each row's own wording only. Nodes with a mechanism name and no failure were marked none or unclear.
