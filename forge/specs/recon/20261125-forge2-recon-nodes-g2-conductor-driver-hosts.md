<!-- scout hand-back, journal task t-1899, recon for docs/tasks/specs/20261125-forge2-light-factory-plan.md; saved verbatim from the worker's final message; 1 dollar figures replaced by [price figure] (P18) -->

digest: v1 forge2-recon-pass2-problems-by-origin

PARTIAL REPORT. All 243 node rows were counted. Only 40 rows were read whole: codex/1 (20) and conductor/1 and conductor/2 (17), plus 3 more whole rows seen on the way. The other ~200 rows were read as excerpts of their first 300-420 characters, which is the "Что" cell. Their statuses (the last column) were NOT read, so item (6) is only partly done. The origin letters below are my reading of the node text. They are approximate counts, not exact. Nothing in the digest is advice about the new design.

## Objects
| id | kind | gist | paths | status | owner | links | ev |
|---|---|---|---|---|---|---|---|
| q1-rows | count | 243 node rows: conductor 72, driver-controller 30, driver-hosts 101, codex 40 | plans/piles | found | — | q1-table | t1,t2,t3,t4,t5 |
| q3T-1 | T | Manual case precondition must be made through the tester's real interface, not by shortcut | plans/piles/conductor/batch-3-vhodyashchie.md:52 | found | — | C3-28 | t8 |
| q3T-2 | T | Live evidence run (gate B on cmp3gb copy) with a red test and non-approval words, no oracle ready | plans/piles/conductor/batch-3-vhodyashchie.md:25 | found | — | C3-1 | t8 |
| q3T-3 | T | Refused manual case has no terminal outcome in traceability, so the third P21 verdict is unreachable | plans/piles/conductor/batch-5-vhodyashchie-3.md:19 | found | — | C5-4 | t9 |
| q3T-4 | T | Test run in 104-140 s for 5-13 s of tests; 27 pytest processes per S5 window | plans/piles/driver-hosts/batch-1-driver-hosts-sources.md:52 | found | — | SC5-7,EP1-23 | t11 |
| q3T-5 | T | A test with an empty assertion (`[:0]`); a test fixture not from a real retro | plans/piles/driver-hosts/batch-2-driver-hosts-sources-words.md:46 | found | — | CL3-12,CL3-6 | t12,t11 |
| q3T-6 | T | Tests red on main: test_gate_preflight 982/983; test_story_run_words 93/95 | plans/piles/conductor/batch-4-vhodyashchie-2.md:18 | found | — | C4-2,C4-11 | t8 |
| q3V-1 | V | Tests of the project ran under the factory's Python without the project's dependencies (cmp3, FB-10) | plans/piles/conductor/batch-3-vhodyashchie.md:42 | found | — | C3-18 | t8 |
| q3V-2 | V | Tracker-key shape was Jira-only (`BUG_TRACKER_ID_RE`, `KEY_RE`); a key from another tracker project read as a source | plans/piles/driver-hosts/batch-1-driver-hosts-sources.md:62 | found | — | SS1-16,SS1-10 | t10 |
| q3V-3 | V | Stand with a frontend proxy shown "alive" by doctor/readiness while stand_health says down | plans/piles/driver-hosts/batch-2-driver-hosts-sources-words.md:53 | found | — | SS1-9 | t12 |
| q3V-4 | V | Launch on Codex: tool surface differs (exec/js/shell/local_shell), no Bash, npm-based projects need an installed sandbox | plans/piles/codex/batch-1-overhead-fixes.md:83 | found | — | CX1-1,CX1-4,CX1-6 | t6 |
| q3V-5 | V | Windows: py launcher and long TEMP path break the qa-doctor smoke | plans/piles/codex/batch-3-doctor-smoke-windows.md:29 | found | — | CX3-1,CX3-2 | t13 |
| q3H-1 | H | Question to the person offered a road the factory had already found unreachable, or asked again per instance | plans/piles/conductor/batch-2-cmp3-classes.md:84 | found | — | C2-9,C5-10 | t7,t9 |
| q3H-2 | H | Person's words that were not approval, or the words themselves, were lost or not executed (gate A/B, token answer) | plans/piles/conductor/batch-1-p22-seams.md:57 | found | — | C1-4,C2-6,C2-7,DC1-19 | t7,t14 |
| q3H-3 | H | Conductor retelling changed the person's words in the summary at the gate | plans/piles/conductor/batch-5-vhodyashchie-3.md:24 | found | — | C5-9 | t9 |
| q3H-4 | H | Question text named a script or gave no price and no consequence per option ("What should happen?") | plans/piles/conductor/batch-1-p22-seams.md:54 | found | — | C1-1,C1-2,C5-2,C3-16 | t7,t9 |
| q3H-5 | H | Conductor/story ran into a question the person cannot answer: S1 attachments question asked about files of the same ticket 55 s later | plans/piles/conductor/batch-5-vhodyashchie-3.md:25 | found | — | C5-10 | t9 |
| q3C-1 | C | Rework dispatch for a second finding of the same plan line cost 39K tokens | plans/piles/driver-controller/batch-1-controller-seams.md:59 | found | — | DC1-18 | t14 |
| q3C-2 | C | Loop `report_check -> rebuild_report` called the retro analyst 7 times ([price figure], about 38 min) | plans/piles/driver-controller/batch-1-controller-seams.md:64 | found | — | DC1-23 | t14 |
| q3C-3 | C | S5 window cycle cost 25 minutes of management; dashboard refresh 2.4 s per commit; `--resume` 1.95x | plans/piles/driver-controller/batch-1-controller-seams.md:50 | found | — | DC1-9,SC2-46,SC5-14 | t14,t11 |
| q3C-4 | C | Conductor assembled routine moves by hand: 19 of 165 Bash calls; 22 form refusals per run (about 10 min) | plans/piles/driver-hosts/batch-1-driver-hosts-sources.md:46 | found | — | SC5-11,SC5-8 | t11,t12 |
| q3F-1 | F | Findings of a run notebook had no owner node until sorted (72 rows: A 41, A* 10, B 4, C 15) | plans/piles/conductor/batch-3-vhodyashchie.md:31 | found | — | C3-7 | t8 |
| q3F-2 | F | Live evidence line "gate A in prose" was not planned | plans/piles/conductor/batch-3-vhodyashchie.md:43 | found | — | C3-19 | t8 |
| q3F-3 | F | Another team's branch (dev2, 30 commits, 14 files in conflict) had to be carried over without breaking decisions | plans/piles/codex/batch-1-overhead-fixes.md:5 | found | — | CX1-17,CX1-18 | t6 |
| q3F-4 | F | Critic queues and "Остатки" lines moved to a new node because the original node was closed | plans/piles/conductor/batch-5-vhodyashchie-3.md:22 | found | — | C5-7,C5-8,CL3-1,CL3-2 | t9,t12 |
| q3F-5 | F | A run-notes text taught a free-form `--block`; skill text and driver diverged (SKILL.md vs driver) | plans/piles/codex/batch-2-leftovers-and-rollout-reader.md:36 | found | — | CX2-26,C3-10 | t13,t8 |
| q3M-top1 | M | Silent pass: a gate, guard or call passes on empty/broken input (manifest missing -> `{}`, bad pipeline.json, 63 `self.py(` without check) | plans/piles/conductor/batch-4-vhodyashchie-2.md:17 | found | — | C1-7,C4-1,C3-22 | t7,t9 |
| q3M-top2 | M | K1 "first of N": a refusal or reader shows one cause or a slice and hides the rest | plans/piles/conductor/batch-2-cmp3-classes.md:76 | found | — | C2-1,C2-2,C3-8,C3-11 | t7,t8 |
| q3M-top3 | M | Two or three readers/parsers of one fact disagree (prefix `stand gap:`, `executor unavailable:`, round verdict, time without zone, scope key) | plans/piles/conductor/batch-4-vhodyashchie-2.md:25 | found | — | C3-29,C4-9,CX2-12,CX2-25 | t8,t13 |
| q3M-top4 | M | No move: code ends in Stop/Refusal/raise to a person where no further move exists (class P22) | plans/piles/conductor/batch-1-p22-seams.md:54 | found | — | C1-1,C1-3,C1-5,C1-6 | t7 |
| q3M-top5 | M | Guard/tokenizer cuts a command finer or coarser than the shell does (quotes, `$( )`, PS here-string, `$var`) | plans/piles/codex/batch-1-overhead-fixes.md:101 | found | — | CX1-5,CX1-19,CX1-20,CX2-27 | t6,t13 |
| q3M-top6 | M | Identity/binding of a dispatch to an agent or story is lost, guessed or reused (resume by guess, bind, TURN BUDGET) | plans/piles/codex/batch-1-overhead-fixes.md:91 | found | — | CX1-9,DC1-11,DC1-16,DC1-30 | t6,t14 |
| q3E-1 | E | `sorted(Path)` and `Path.glob` differ between Windows and Linux (order, case) | plans/piles/conductor/batch-4-vhodyashchie-2.md:23 | found | — | C4-7,C4-12,C4-13 | t9 |
| q3E-2 | E | `os.chdir` in a harness into a deleted project breaks the next test on Linux | plans/piles/conductor/batch-4-vhodyashchie-2.md:22 | found | — | C4-6 | t9 |
| q3E-3 | E | Codex rollouts compressed to `.jsonl.zst` (107 on owner's machine), no decoder; hook order unknown | plans/piles/codex/batch-2-leftovers-and-rollout-reader.md:24 | found | — | CX2-13 | t13 |
| q6-again | analog | Return of a problem after a fix, by word in text | plans/piles/driver-controller/batch-1-controller-seams.md:60 | found | — | DC1-19,DC1-11,DC1-29 | t14,t15 |
| q4-misses | absent | Owner-word grep with a glob of 4 folders in braces returned nothing (miscall, see Trail) | plans/piles | absent | — | — | t16,t8 |

## Trail
| tid | op | target | pattern / range | flags | result | control |
|---|---|---|---|---|---|---|
| t1 | glob | C:\QAFactory\forge-repo\plans\piles | `{conductor,driver-controller,driver-hosts,codex}/batch-*.md` | — | found 11; plans\piles\codex\batch-1-overhead-fixes.md | — |
| t2 | grep | C:\QAFactory\forge-repo\plans\piles\conductor | `^\| [A-Z]+[0-9]*-[0-9]+[a-z]? \|` | count glob=batch-*.md | found 72; plans\piles\conductor\batch-3-vhodyashchie.md:31 | — |
| t3 | grep | C:\QAFactory\forge-repo\plans\piles\codex | `^\| [A-Z]+[0-9]*-[0-9]+[a-z]? \|` | count glob=batch-*.md | found 40; plans\piles\codex\batch-1-overhead-fixes.md:83 | — |
| t4 | grep | C:\QAFactory\forge-repo\plans\piles\driver-controller | `^\| [A-Z]+[0-9]*-[0-9]+[a-z]? \|` | count glob=batch-*.md | found 30; plans\piles\driver-controller\batch-1-controller-seams.md:42 | — |
| t5 | grep | C:\QAFactory\forge-repo\plans\piles\driver-hosts | `^\| [A-Z]+[0-9]*-[0-9]+[a-z]? \|` | count glob=batch-*.md | found 101; plans\piles\driver-hosts\batch-1-driver-hosts-sources.md:22 | — |
| t6 | read | C:\QAFactory\forge-repo\plans\piles\codex\batch-1-overhead-fixes.md | lines 1-158 whole (rows CX1-1..CX1-20 and the preamble) | — | read plans\piles\codex\batch-1-overhead-fixes.md:1-158 | — |
| t7 | read | C:\QAFactory\forge-repo\plans\piles\conductor\batch-1-p22-seams.md and batch-2-cmp3-classes.md | lines 54-61 and 76-84 whole | — | read plans\piles\conductor\batch-1-p22-seams.md:54-61 | — |
| t8 | grep | C:\QAFactory\forge-repo\plans\piles\conductor | `^\| [A-Z]+[0-9]*-[0-9]+[a-z]? \|.{0,420}` (excerpt of 420 chars per row; saved output re-read) | content -o glob=batch-[345]*.md | found 55; plans\piles\conductor\batch-3-vhodyashchie.md:25 | — |
| t9 | grep | C:\QAFactory\forge-repo\plans\piles\conductor | same pattern, rows of batch-4 and batch-5 (read from saved output) | content -o glob=batch-[345]*.md | found 24; plans\piles\conductor\batch-4-vhodyashchie-2.md:17 | — |
| t10 | grep | C:\QAFactory\forge-repo\plans\piles\driver-hosts | `^\| [A-Z]+[0-9]*-[0-9]+[a-z]? \|.{0,340}` | content -o glob=batch-1*.md | found 44; plans\piles\driver-hosts\batch-1-driver-hosts-sources.md:22 | — |
| t11 | grep | C:\QAFactory\forge-repo\plans\piles\driver-hosts | rows of batch-1, same call as t10 (rows SC5-7, EP1-23, SC5-11) | content -o glob=batch-1*.md | found 44; plans\piles\driver-hosts\batch-1-driver-hosts-sources.md:52 | — |
| t12 | grep | C:\QAFactory\forge-repo\plans\piles\driver-hosts | `^\| [A-Z]+[0-9]*-[0-9]+[a-z]? \|.{0,300}` (saved output read) | content -o glob=batch-2*.md | found 57; plans\piles\driver-hosts\batch-2-driver-hosts-sources-words.md:22 | — |
| t13 | grep | C:\QAFactory\forge-repo\plans\piles\codex | `^\| [A-Z]+[0-9]*-[0-9]+[a-z]? \|.{0,400}` | content -o glob=batch-[23]*.md | found 20; plans\piles\codex\batch-2-leftovers-and-rollout-reader.md:22 | — |
| t14 | grep | C:\QAFactory\forge-repo\plans\piles\driver-controller | `^\| [A-Z]+[0-9]*-[0-9]+[a-z]? \|.{0,400}` | content -o glob=batch-*.md | found 30; plans\piles\driver-controller\batch-1-controller-seams.md:42 | — |
| t15 | grep | C:\QAFactory\forge-repo\plans\piles\driver-controller | `.{0,40}(снова\|повторно\|Остаток\|остаток).{0,40}` | content -o glob=batch-*.md | found 4; plans\piles\driver-controller\batch-1-controller-seams.md:60 | — |
| t16 | grep | C:\QAFactory\forge-repo\plans\piles | `[Сс]лово владельца [0-9.]+[^\|;)]{0,90}` | -i content -o glob={conductor,driver-controller,driver-hosts,codex}/batch-*.md | absent | t17 |
| t17 | grep | C:\QAFactory\forge-repo\plans\piles\driver-controller | `[Сс]лово владельца [0-9.]+[^\|;)]{0,90}` | -i content -o glob=batch-*.md | found 12; plans\piles\driver-controller\batch-1-controller-seams.md:50 | — |

(t16 was a miscall: the braces glob in a multi-folder path matched no file. t17 is the working form. The owner-word search for the conductor and codex folders was NOT rerun; see Not done.)

## Answers by done-criterion

(1) Table: file | node rows in file | rows classified
Classified here means origin letters assigned from the excerpt or whole row. Rows counted by the pattern `^\| ID \|`.
| file | rows | classified |
|---|---|---|
| codex/batch-1-overhead-fixes.md | 20 | 20 (whole rows) |
| codex/batch-2-leftovers-and-rollout-reader.md | 17 | 17 (excerpt) |
| codex/batch-3-doctor-smoke-windows.md | 3 | 3 (excerpt) |
| conductor/batch-1-p22-seams.md | 8 | 8 (whole) |
| conductor/batch-2-cmp3-classes.md | 9 | 9 (whole) |
| conductor/batch-3-vhodyashchie.md | 31 | 31 (excerpt) |
| conductor/batch-4-vhodyashchie-2.md | 14 | 14 (excerpt) |
| conductor/batch-5-vhodyashchie-3.md | 10 | 10 (excerpt) |
| driver-controller/batch-1-controller-seams.md | 30 | 30 (excerpt) |
| driver-hosts/batch-1-driver-hosts-sources.md | 44 | 44 (excerpt) |
| driver-hosts/batch-2-driver-hosts-sources-words.md | 57 | 57 (excerpt) |
| sum | 243 | 243 |
No gap in the row counts. The driver-hosts rows include 58 rows carried over from other piles, with the text "перенесён из ..." (so repeats of the same problem exist in two piles; counted in both). The Грел-ID of the batch-1 table: line 64 of driver-hosts/1 is not a node row.

(2) Counts per origin letter per pile. Approximate; a row with two letters is counted under each, so sums exceed the row count.
| pile (rows) | T | V | H | M | E | C | F | none |
|---|---|---|---|---|---|---|---|---|
| conductor (72) | 5 | 1 | 14 | 57 | 5 | 3 | 5 | 0 |
| driver-controller (30) | 1 | 0 | 3 | 24 | 0 | 4 | 3 | 3 |
| driver-hosts (101) | 3 | 6 | 8 | 70 | 2 | 8 | 12 | 5 |
| codex (40) | 3 | 6 | 1 | 26 | 6 | 0 | 3 | 3 |
driver-hosts: 58 of the rows are transfers of nodes whose text I only read as a copy; origin follows the original text. Rows with only "перенесён"/"закрыта: перенесено" and no problem named were counted `none` only where the excerpt had no problem (a few); the rest got the origin of the carried text. About 20 rows in conductor/3 and driver-hosts/1-2 are plain residue lists ("остатки C2-x") that name code defects, so they are M.

(3) Distinct problems for T, V, H, C, F: see the Objects rows q3T-1..q3F-5, each with its node ids and a path:line. Only the ones seen are listed; the driver-hosts/2 tail (~25 collect/intake nodes CL3-x) names tool-code defects and is under M or F.

(4) M and E sub-kinds. Counts are of node rows, approximate.
| sub-kind | M count | 3 example ids |
|---|---|---|
| validator/gate verdict (silent pass, K1 first-of-N, wrong refusal) | ~60 | C2-1, C2-2, C4-1 |
| driver or conductor seam (no move, words not carried, fallback question) | ~45 | C1-1, C2-6, C2-8 |
| guard or hook refusal (tokenizer, scope, resume by guess) | ~25 | CX1-5, CX1-9, CX1-20 |
| form/hand-off shape (handoff fields, door text, card) | ~20 | C2-4, DC1-17, C3-31 |
| state/lock/staleness (receipt, stage record, window cap, rounds) | ~20 | C3-14, DC1-1, DC1-21 |
| generated text/doc drift (layer map, controller-blocks, texts) | ~12 | DC1-26, C4-4, GW1-17 |
| other (duplicate parsers, constants, test stubs) | ~30 | C4-9, C4-8, SC2-8 |
E has 13 rows: OS/path order (C4-7, C4-12, C4-13), harness chdir (C4-6), Windows launcher/TEMP (CX3-1, CX3-2), Codex rollout compression (CX2-13), git subfolder (DC1-7), network error reading (SS1-1).
Five problems that repeat most (by count of rows naming them; rough):
1. a gate or reader passes or refuses on one cause and hides the rest or a missing input (C2-1, C2-2, C4-1, C3-8, C3-11, CX2-16);
2. several readers of one fact diverge (C3-29, C4-9, C4-8, CX2-12, CX2-25, GW1-39, SC2-7);
3. state with no further move, ending in a question to the person (C1-1, C1-3, C1-5, C1-6, C2-8, DC1-21);
4. a guard cuts or reads a command differently from the shell (CX1-5, CX1-19, CX1-20, CX2-14, CX2-23, CX2-27);
5. identity of dispatch/agent/story/scope lost, guessed or compared by name (CX1-8, CX1-9, CX1-11, DC1-11, DC1-16, CX2-17).

(5) Owner's words inside nodes, VERBATIM, date as in the text. Not complete (see Not done). Each was read in the text itself:
- «перенести все её фиксы так, чтобы не нарушить нашу архитектуру и принятые решения, и исправить все найденные ей баги» — 19.10.2026, plans/piles/codex/batch-1-overhead-fixes.md:5
- «одна пачка codex на все узлы, предел L для неё не действует» — 19.10.2026 (14:4x), plans/piles/codex/batch-1-overhead-fixes.md:7-8
- «дирижёр сам не переделывает, а управляет фабрикой — вызывает агента, возвращает к стадии, просит человека» — 09.10 (no year), plans/piles/conductor/batch-1-p22-seams.md:55 (node C1-2)
- «класть сейчас» — 19.10.2026, plans/piles/conductor/batch-3-vhodyashchie.md:52 (node C3-28)
- «пачка закрывается доделкой, не переносом» — 08.10.2026, plans/piles/driver-hosts/batch-1-driver-hosts-sources.md:7 (preamble, not a node row)
- «переносим к нам в релиз все пункты… которые ускоряют работу» — 29.10.2026, plans/piles/driver-hosts/batch-1-driver-hosts-sources.md:54 (node EP1-23)
- «не в 0.10.5, в пачки» — 28.10.2026, plans/piles/driver-hosts/batch-1-driver-hosts-sources.md:62 (node SS1-10)
- «ок, добавляй» — 29.10.2026, plans/piles/driver-controller/batch-1-controller-seams.md:57 (node DC1-16)
- «чинить в ближайший релиз» — 30.10.2026, plans/piles/driver-controller/batch-1-controller-seams.md:60 (node DC1-19)
Dates only (text of the word cut off by my excerpt, not read): 25.10.2026 DC1-9 (driver-controller:50, the node gives the S5 form of the owner: plan for ALL cases, one code critic for the whole plan); 26.10.2026 DC1-10 (:51); 29.10.2026 DC1-11 (:52); 30.10.2026 DC1-20..21 (:83-84); 24.11.2026 (driver-hosts/1:43, driver-hosts/2:40 and :69); 28.10.2026 (driver-hosts/2:31,32,41,42; the words are the transfer of critic queues, C5-7, C5-8, CL3-1, CL3-2); 20.10 20:1x CX2-26 (driver-hosts/2:39: the story path is ONE on both hosts); 31.10.2026 C5-4 ("0.10.8"). Conductor/4, codex/2 (CX2-17 29.10.2026) not searched for the words.

(6) Nodes that name a problem coming back after a fix (read in text; not full):
- DC1-19 «на гейте B вопросы заданы снова» (driver-controller/batch-1-controller-seams.md:60)
- DC1-11 -> DC1-29 «Остаток DC1-11 (A2, критерии 1, 4, 5)» (:70)
- C3-17 «повтор B-177, FR-3» (conductor/batch-3:41)
- C3-13, C3-23, C3-24, C3-25, C3-26, C3-27 residues of closed nodes (conductor/batch-3:37, 47-51)
- C4-3 «закрывает остаток C3-10» (conductor/batch-4:19); C4-10, C4-12 residues of C4-4 and C4-7 (:26, :28); C4-14 analog at C2-7 (:30)
- C5-7, C5-8 critic queue transferred from conductor/1 «Остатки» (conductor/batch-5:22-23)
- CX2-11..CX2-26 are all residues of CX1-x (codex/batch-2); CX2-14 «остаток находки ... закрывается узлом CX1-20» (codex/batch-2:26); CX2-17 «остатки CX1-11» (:28)
- DC1-20 «Хвосты t-1603/t-1604 после починки блокера» (driver-controller:61)
- CX1-20 passed three rounds, two BLOCKER rechecks before acceptance (codex/batch-1:102)
- C3-14 and C3-20: the same class (`code_only` lost) in a second function, «аналог C3-14» (conductor/batch-3:38, :44)
- HF5-20 «после повторного открытия ... история снова закрывается» (driver-hosts/1:48)

## Not done
- Whole-row reading was done for codex/1 and conductor/1-2 only. All other rows were read as excerpts of 300-420 characters (tool output cut). The status column, the "Остатки" lines and the cell "Чтит" were not read for them; so the per-letter counts for those piles are approximate and (6) is partial.
- Preambles, the "Остатки", "Живые доказательства" and "Ход" sections of every batch were NOT read, except codex/1 lines 1-158. The unread tail of codex/1 (lines 159-294) is not read.
- Owner-word search (5) was not run for conductor and codex (the first attempt with a multi-folder braces glob returned nothing, a miscall; see t16/t17); it was run for driver-controller and driver-hosts, limited to 20-30 hits.
- The same-shape positive control for "nothing about X" claims: the only absent row (q4-misses) is a miscall, not a finding. No claim "nothing about X" is made.
- The 220K-token budget stopped me from rereading rows in full. About 200 rows should be reread whole before using the letter counts as exact.

this needs a decision from a tier above.
