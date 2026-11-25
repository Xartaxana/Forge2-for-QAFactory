<!-- scout hand-back, journal task t-1898, recon for docs/tasks/specs/20261125-forge2-light-factory-plan.md; saved verbatim from the worker's final message; 1 dollar figures replaced by [price figure] (P18) -->

digest: v1 forge2-recon2-problems
## Objects
| id | kind | gist | paths | status | owner | links | ev |
|---|---|---|---|---|---|---|---|
| q1-forge | coverage | forge: 7 files, 235 rows by row pattern (8, 11, 4, 4, 12, 59, 137); all 235 classified | plans/piles/forge/batch-7-vhodyashchie-4.md:26 | found | — | q2-forge | t1,t2,t3,t4,t5,t6,t7,t8,t9,t10 |
| q1-ghmove | coverage | github-move: 3 files, 22 rows (11, 7, 4); all classified | plans/piles/github-move/batch-1-chistka-vne-paketa.md:23 | found | — | q2-ghmove | t1,t11,t12,t13 |
| q1-kb | coverage | kb: 2 files, 9 rows (5, 4); all classified | plans/piles/kb/batch-1-kb-update.md:56 | found | — | q2-kb | t1,t15,t16 |
| q1-prop | coverage | proposals: 1 file, 1 row; classified none | plans/piles/proposals/batch-1-predlozheniya.md:28 | found | — | q2-prop | t1,t14 |
| q1-pkgci | coverage | package-ci: 4 files, 49 rows (12, 7, 6, 24); all classified | plans/piles/package-ci/batch-4-dieta-testov-td-11-td-15.md:22 | found | — | q2-pkgci | t1,t17,t18,t19,t20 |
| q1-rules | coverage | rules-debt: 1 file, 45 rows; all classified | plans/piles/rules-debt/batch-1-phase-2.md:29 | found | — | q2-rules | t1,t21 |
| q1-total | coverage | 18 files, 361 rows, 361 classified; grep count and my read agree per file (forge-6 rows all in lines 16-74) | plans/piles/forge/batch-6-vhodyashchie-2.md:16 | found | — | q1-forge | t1,t7 |
| q2-forge | letters | forge letter occurrences: M 137, F 61, C 35, E 16, T 14, V 5, H 3, unclear 4, none 0 (two-letter rows count twice) | plans/piles/forge/batch-7-vhodyashchie-4.md:26 | found | — | q1-forge | t2,t3,t4,t5,t6,t7,t8,t9,t10 |
| q2-ghmove | letters | github-move: none 13, V 5, T 2, M 1, E 1, C 1; none = move chores with no problem named | plans/piles/github-move/batch-2-paket-i-pereezd.md:23 | found | — | q1-ghmove | t11,t12,t13 |
| q2-kb | letters | kb: F 6 (stale pages, page outside registry), H 1 (KB2-3), none 2 | plans/piles/kb/batch-2-kb-user-guide.md:19 | found | — | q1-kb | t15,t16 |
| q2-prop | letters | proposals PR1-1: none (carry-over, closed by owner word 01.11) | plans/piles/proposals/batch-1-predlozheniya.md:28 | found | — | q1-prop | t14 |
| q2-pkgci | letters | package-ci: C 14, T 14, M 13, E 3, V 1, F 1, unclear 4 (PC4-2..5 name no problem) | plans/piles/package-ci/batch-4-dieta-testov-td-11-td-15.md:23 | found | — | q1-pkgci | t17,t18,t19,t20 |
| q2-rules | letters | rules-debt: M 36, V 6, T 2, H 2, F 2, E 1, unclear 1 (RD1-16); some rows hold two letters | plans/piles/rules-debt/batch-1-phase-2.md:44 | found | — | q1-rules | t21 |
| q2-all | letters | all piles: M 187, C 50, F 70, T 32, E 21, V 17, H 6, none 16, unclear 9 (occurrences, not rows) | plans/piles/forge/batch-7-vhodyashchie-4.md:26 | found | — | q2-forge | t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t15,t17,t21 |
| rule-clone | method | I put copies of one reader or helper in package or tools under M (other): the text names code that needed repair | plans/piles/forge/batch-7-vhodyashchie-4.md:26 | found | — | fork-1 | t8 |
| T1 | problem-T | A test pins a measured constant (brief ceiling, ratchet number, hard counter) and floats with every byte: PC2-1, PC3-4, F6-52 | plans/piles/package-ci/batch-2-potolki-brief-pack.md:24 | found | — | — | t18 |
| T2 | problem-T | Wall-clock assertions flake under CI load: PC1-7, PC1-12, PC4-21 | plans/piles/package-ci/batch-1-green-ci.md:49 | found | — | — | t17 |
| T3 | problem-T | A test cannot fail or reads the wrong thing: PC2-2 (non-empty CHANGELOG), PC1-9 (docstring not ast), RD1-45, RD1-40 | plans/piles/package-ci/batch-2-potolki-brief-pack.md:25 | found | — | — | t18 |
| T4 | problem-T | A marker or mock hides a defect: empty-stderr tests masked by warn_once (F6-48), mocks swallow pytest report (FG7-101) | plans/piles/forge/batch-6-vhodyashchie-2.md:63 | found | — | — | t7 |
| T5 | problem-T | Test inputs rot after code changes (fixture stale, SimpleNamespace missing field): PC2-5, PC3-5, GM3-1 | plans/piles/package-ci/batch-3-khrapovik-doors-only.md:29 | found | — | — | t19 |
| T6 | problem-T | Tests do not hold the joins between stages (run 12586: 17 digest-form refusals, receipts with no producer): F6-51 | plans/piles/forge/batch-6-vhodyashchie-2.md:66 | found | — | — | t7 |
| T7 | problem-T | Node witness too narrow, late defects found only by canon or nightly: FG7-19, FG7-63, FG7-92, F6-44 | plans/piles/forge/batch-7-vhodyashchie-4.md:44 | found | — | — | t8,t9 |
| T8 | problem-T | Test volume exceeds code and many pins low-value (8 of 10 red canon were stale pins): F6-42, F6-52, FG7-65 | plans/piles/forge/batch-6-vhodyashchie-2.md:67 | found | — | — | t7,t9 |
| T9 | problem-T | Evidence level unlabelled or synthetic standing in for live (static, simulated, live): F6-32, FG7-39, FG7-103, PC4-16 | plans/piles/forge/batch-6-vhodyashchie-2.md:47 | found | — | — | t7,t8,t10 |
| T10 | problem-T | Red kept in quarantine unexamined, replacement of a detector unproven: PC3-5, PC4-17, PC4-18 | plans/piles/package-ci/batch-3-khrapovik-doors-only.md:29 | found | — | — | t19,t20 |
| T11 | problem-T | Dry-story known-red seeds fail with an unknown cause ("driver exited with no new question"): FG7-129 | plans/piles/forge/batch-7-vhodyashchie-4.md:154 | found | — | — | t10 |
| V1 | problem-V | Code bound to GitLab as host and tracker met GitHub: GM1-1, GM1-4, GM1-5, FG7-10, FG7-69, FG7-80 | plans/piles/github-move/batch-1-chistka-vne-paketa.md:26 | found | — | — | t11,t8,t9 |
| V2 | problem-V | Paths and stand of the first developer or owner baked in: F0-6, GM1-2 | plans/piles/forge/batch-1-foundation.md:30 | found | — | — | t2,t11 |
| V3 | problem-V | Languages other than Python lack a probe row or frame reader (JVM Calc.kt, TRX): RD1-15, RD1-22, RD1-24, RD1-37, RD1-39 | plans/piles/rules-debt/batch-1-phase-2.md:52 | found | — | — | t21 |
| V4 | problem-V | No CI job compiled the package on Python 3.10; an f-string broke: PC4-22 | plans/piles/package-ci/batch-4-dieta-testov-td-11-td-15.md:43 | found | — | — | t20 |
| V5 | problem-V | Product lacks a surface the skip word names ("no such surface for the product"): RD1-20 | plans/piles/rules-debt/batch-1-phase-2.md:48 | found | — | — | t21 |
| H1 | problem-H | A report misleads the person: savings shown as 100% at zero prices (F6-21); gate A preview erases the "new since" line (F6-57) | plans/piles/forge/batch-6-vhodyashchie-2.md:36 | found | — | — | t7 |
| H2 | problem-H | The person's word is recorded but not read at the review gap: RD1-17; word-covers-next-time: RD1-11 | plans/piles/rules-debt/batch-1-phase-2.md:45 | found | — | — | t21 |
| H3 | problem-H | Restarting an open stage of a closed story needs a question to the person (B-331): F5-12 | plans/piles/forge/batch-5-vhodyashchie.md:35 | found | — | — | t6 |
| H4 | problem-H | KB pages told the driver path while the person works through skills: KB2-3 | plans/piles/kb/batch-2-kb-user-guide.md:19 | found | — | — | t16 |
| H5 | problem-H | Owner asked to check nothing was lost when backlog rules moved into one home: RD1-43 | plans/piles/rules-debt/batch-1-phase-2.md:71 | found | — | — | t21 |
| C1 | problem-C | Boot and context size over budget (imports uncounted, role load, boot rebuild): F0-5, F6-27, FG7-62, FG7-51, FG7-125, PC2-6 | plans/piles/forge/batch-6-vhodyashchie-2.md:42 | found | — | — | t2,t7,t8,t9,t10,t18 |
| C2 | problem-C | Prices unknown or wrong, so money reads [price figure] or wrong per request: F6-6, F6-23, F6-24; node cost with rework: FG7-5 | plans/piles/forge/batch-6-vhodyashchie-2.md:21 | found | — | — | t7,t8 |
| C3 | problem-C | Wall time: canon over 60 minutes, serial CI steps, queue waits, files near the 300 s cap: F6-50, PC4-24, FG7-90, FG7-91, PC3-2 | plans/piles/forge/batch-6-vhodyashchie-2.md:65 | found | — | — | t7,t9,t19,t20 |
| C4 | problem-C | Coordinator turns: 85% of turns carry one call, runs with no time limit: FG7-114, FG7-112, FG7-47 | plans/piles/forge/batch-7-vhodyashchie-4.md:139 | found | — | — | t10 |
| C5 | problem-C | Scout exchange 8k tokens against a 2k goal; Lead context without compaction: F5-2, FG7-29, FG7-25 | plans/piles/forge/batch-7-vhodyashchie-4.md:54 | found | — | — | t6,t8 |
| F1 | problem-F | Findings, remainders and debts pile up with no home or executor: F5-3, F6-30, F3-1..F3-4 | plans/piles/forge/batch-6-vhodyashchie-2.md:45 | found | — | — | t4,t6,t7 |
| F2 | problem-F | Dispatch spec omits neighbours, readers, designer threshold or producer node: FG7-18, FG7-20, FG7-40, FG7-113 | plans/piles/forge/batch-7-vhodyashchie-4.md:138 | found | — | — | t8,t10 |
| F3 | problem-F | Rule text copied in many places, stale or contradicting: F6-33, FG7-50, FG7-52, F6-41, F6-53 | plans/piles/forge/batch-6-vhodyashchie-2.md:48 | found | — | — | t7,t9 |
| F4 | problem-F | Worktrees pile up (261) or are cut from main, not the pile branch: F6-38, F6-35, FG7-4, FG7-66 | plans/piles/forge/batch-6-vhodyashchie-2.md:53 | found | — | — | t7,t8,t9 |
| F5 | problem-F | Two sessions collide: same node numbers, second session in one root: FG7-109, FG7-115 | plans/piles/forge/batch-7-vhodyashchie-4.md:140 | found | — | — | t10 |
| F6 | problem-F | Registry errors caught only before merge, main red, no single fixer: FG7-92, FG7-93, FG7-94, FG7-9 | plans/piles/forge/batch-7-vhodyashchie-4.md:119 | found | — | — | t8,t9 |
| F7 | problem-F | Worker reports lost or rewritten by Lead; coordinator rules read only via a hook line: F5-1, FG7-89 | plans/piles/forge/batch-5-vhodyashchie.md:24 | found | — | — | t6,t9 |
| F8 | problem-F | Architecture invariants not written down, fixes break accepted decisions: F6-29; BATCH CANON only in prose: F6-34 | plans/piles/forge/batch-6-vhodyashchie-2.md:44 | found | — | — | t7 |
| F9 | problem-F | KB pages stale against the factory (127 claims, 80 stale), page outside the registry: KB1-1, KB2-1 | plans/piles/kb/batch-1-kb-update.md:56 | found | — | — | t15,t16 |
| M-form | sub-M | form or hand-off shape: about 19 rows; FG7-14 (label carries model), FG7-130 (form missing key accepted), F2-7 (prose line read as owns) | plans/piles/forge/batch-7-vhodyashchie-4.md:39 | found | — | — | t3,t8,t10 |
| M-guard | sub-M | guard or hook refusal or blindness: about 23; FG7-102 (wrappers), FG7-104 (returned lost), F6-9 (SyntaxError drops hook) | plans/piles/forge/batch-7-vhodyashchie-4.md:127 | found | — | — | t7,t10 |
| M-state | sub-M | state, lock or staleness: about 12; FG7-71 (task number collision), FG7-70 (row without feature blocks merges), FG7-82 (rename race) | plans/piles/forge/batch-7-vhodyashchie-4.md:96 | found | — | — | t9,t10 |
| M-seam | sub-M | driver or conductor seam: about 15; FG7-76 (probe anchor), FG7-124 (check id from field path), F5-11 | plans/piles/forge/batch-7-vhodyashchie-4.md:101 | found | — | — | t6,t9,t10 |
| M-verdict | sub-M | validator or gate verdict: about 52; RD1-3 (acceptable predicate), RD1-12 (uncheckable asks person), FG7-32 (old journal rows) | plans/piles/rules-debt/batch-1-phase-2.md:31 | found | — | — | t9,t21 |
| M-drift | sub-M | generated text or doc drift: about 19; F6-4 (parity ledger), FG7-79 (named_by pointer), F6-46 (docstring lies) | plans/piles/forge/batch-6-vhodyashchie-2.md:19 | found | — | — | t7,t10 |
| M-other | sub-M | other: about 47, mostly copies and long functions; FG7-1 (nine copies), F4-3 (read_json), B-455 (dup ratchet) | plans/piles/forge/batch-7-vhodyashchie-4.md:26 | found | — | rule-clone | t5,t8 |
| M-note | method | M sub-kind counts are my hand tally of node text: exact for forge-7 (78 rows), by my reading elsewhere, not machine-counted | plans/piles/forge/batch-7-vhodyashchie-4.md:26 | found | — | — | t8,t9,t10 |
| M-top1 | repeat-M | Copies of one reader or helper diverge (one_line x9+10, ASCII sanitizer x7, read_json x4+16, project root x6): FG7-1, FG7-75, FG7-56, F4-2 | plans/piles/forge/batch-7-vhodyashchie-4.md:26 | found | — | rule-clone | t5,t8,t9 |
| M-top2 | repeat-M | A gate decides from prose or a fragment, not structure ("owns" word, "0 failed" read as red, "not a mechanism" trusted): F6-1, FG7-110, FG7-72 | plans/piles/forge/batch-6-vhodyashchie-2.md:16 | found | — | — | t7,t10 |
| M-top3 | repeat-M | A hook fails open silently or falls whole on unreadable or unknown input: F6-9, F6-20, FG7-104, FG7-126, FG7-128 | plans/piles/forge/batch-6-vhodyashchie-2.md:24 | found | — | — | t7,t10 |
| M-top4 | repeat-M | Pointers, anchors and lists stale after a split or move: F6-4, F6-22, FG7-76, FG7-79, FG7-81, FG7-23 | plans/piles/forge/batch-6-vhodyashchie-2.md:19 | found | — | — | t7,t10 |
| M-top5 | repeat-M | Journal writer and validator disagree or collide: FG7-70, FG7-71, FG7-111, FG7-32, F6-58, F6-59 | plans/piles/forge/batch-7-vhodyashchie-4.md:95 | found | — | — | t7,t10 |
| E-os | sub-E | OS and Windows: 12 rows; file replace or rename races (FG7-82, FG7-84, PC3-3), CRLF (PC1-2, GM1-8, F6-43), .exe (RD1-18) | plans/piles/package-ci/batch-3-khrapovik-doors-only.md:27 | found | — | — | t3,t7,t10,t11,t17,t19,t21 |
| E-host | sub-E | host CLI or harness: 5 rows; F5-1 (empty transcripts), F6-35 (worktree base), FG7-24 (permissions), FG7-55, FG7-106 | plans/piles/forge/batch-5-vhodyashchie.md:24 | found | — | — | t6,t7,t10 |
| E-cloud | sub-E | cloud, network or machine: 4 rows; FG7-64 (shallow clone, TZ), FG7-68 (git proxy 403), F6-2 (machine sleep), F6-50 (bind mount) | plans/piles/forge/batch-7-vhodyashchie-4.md:89 | found | — | — | t7,t10 |
| E-top | repeat-E | Windows file replace or rename races: FG7-82, FG7-84, FG7-85, PC3-3, PC1-3; second repeat is CRLF in five nodes | plans/piles/forge/batch-7-vhodyashchie-4.md:107 | found | — | E-os | t10,t17,t19 |
| ow-1 | owner-word | F6-27 (19.10): «это тоже бут-бюджет» | plans/piles/forge/batch-6-vhodyashchie-2.md:42 | found | владелец | C1 | t7 |
| ow-2 | owner-word | F6-29 (20.10 18:5x): «изменения и починки не ломают архитектуру и принятые решения» | plans/piles/forge/batch-6-vhodyashchie-2.md:44 | found | владелец | F8 | t7 |
| ow-3 | owner-word | F6-52 (28.10.2026), no quote marks in source: рекомендацию по анализу лишних тестов принимаю; делать после релиза 0.10.5 | plans/piles/forge/batch-6-vhodyashchie-2.md:67 | found | владелец | T8 | t7 |
| ow-4 | owner-word | FG7-38 (24.11): «если это вообще нужно» | plans/piles/forge/batch-7-vhodyashchie-4.md:63 | found | владелец | — | t8 |
| ow-5 | owner-word | FG7-42 (24.11.2026): «мы это убирали так как журнал теперь пишет код» | plans/piles/forge/batch-7-vhodyashchie-4.md:67 | found | владелец | — | t8 |
| ow-6 | owner-word | FG7-44 (24.11.2026): «закрывай, доделывать не нужно» | plans/piles/forge/batch-7-vhodyashchie-4.md:69 | found | владелец | — | t8 |
| ow-7 | owner-word | FG7-53 (16.11): «нам нужно закрывать эту дыру?» | plans/piles/forge/batch-7-vhodyashchie-4.md:78 | found | владелец | — | t9 |
| ow-8 | owner-word | FG7-54 (16.11): «запиши как узел П3. Когда-нибудь прогоним» | plans/piles/forge/batch-7-vhodyashchie-4.md:79 | found | владелец | — | t9 |
| ow-9 | owner-word | FG7-65 (18.11.2026): «ок, но билдер должен знать заранее» | plans/piles/forge/batch-7-vhodyashchie-4.md:90 | found | владелец | T8 | t9 |
| ow-10 | owner-word | FG7-132 (24.11.2026): «его надо внедрить, если у нас есть что-то дополнительное, то добавить в этот» | plans/piles/forge/batch-7-vhodyashchie-4.md:157 | found | владелец | — | t10 |
| ow-11 | owner-word | FG7-133, FG7-134, FG7-135 (24.11.2026): «как и когда мы будем чинить всё плохое что он нашёл?» — «Да, оформляй» | plans/piles/forge/batch-7-vhodyashchie-4.md:158 | found | владелец | — | t10 |
| ow-12 | owner-word | FG7-90..FG7-93 (18.11), no quote marks: ошибки реестров ловятся только перед слиянием, пятый случай в соседней сессии, E7-3b | plans/piles/forge/batch-7-vhodyashchie-4.md:115 | found | владелец | F6 | t9 |
| ow-13 | owner-word | FG7-66 (18.11.2026) and FG7-67, no quote marks: всё нужное запушено, ненужное удаляется после слияния; при слиянии сначала коммит | plans/piles/forge/batch-7-vhodyashchie-4.md:91 | found | владелец | F4 | t9 |
| ow-14 | owner-word | RD1-4 (17.11): «да»; RD1-8 (17.11): «да» | plans/piles/rules-debt/batch-1-phase-2.md:32 | found | владелец | — | t21 |
| ow-15 | owner-word | RD1-24 (17.11.2026): «Отдельный П1 на потом» | plans/piles/rules-debt/batch-1-phase-2.md:52 | found | владелец | V3 | t21 |
| ow-16 | owner-word | RD1-43 (18.11 и 23.11): «Мы выносили правила беклога из разных мест в одно. Проверь что ничего не потерялось» | plans/piles/rules-debt/batch-1-phase-2.md:71 | found | владелец | H5 | t21 |
| ow-17 | owner-word | PC4-1 (12.11.2026): «не сейчас»; PC4-2 (12.11.2026): «не сейчас: волна 1 спеки B не стартует» | plans/piles/package-ci/batch-4-dieta-testov-td-11-td-15.md:22 | found | владелец | — | t20 |
| ow-18 | owner-word | PC4-14 (12.11.2026): «да», вариант (a) | plans/piles/package-ci/batch-4-dieta-testov-td-11-td-15.md:35 | found | владелец | — | t20 |
| ow-19 | owner-word | Dated owner words with no wording quoted inside the row: F6-24, F6-25, F6-38, F6-42, F6-50, F6-51, FG7-4..7, FG7-14, FG7-24, FG7-39, FG7-47..51, FG7-63, FG7-64, FG7-94, GM3-3, GM3-4 | plans/piles/forge/batch-7-vhodyashchie-4.md:29 | found | владелец | — | t7,t8,t9,t13 |
| ow-20 | owner-word | Owner words in batch headers and Ход (forge-5:5, forge-2:11, kb-1:9, github-move-3:7) are not node rows and are not catalogued | plans/piles/forge/batch-5-vhodyashchie.md:5 | found | — | — | t6,t5,t15,t13 |
| back-1 | came-back | Remainder or same class after an earlier fix: F6-19 (after F6-7), F6-39 (after F6-38), F6-12, F6-13, F6-11, F6-17, F6-21, FG7-73, FG7-119, FG7-124 | plans/piles/forge/batch-6-vhodyashchie-2.md:34 | found | — | — | t7,t10 |
| back-2 | came-back | More copies of an already-fixed class: FG7-74 (after FG7-37), FG7-75 (ten after FG7-1), FG7-77 (fourth stamp loop after FG7-3), FG7-61, FG7-60 | plans/piles/forge/batch-7-vhodyashchie-4.md:99 | found | — | M-top1 | t8,t9,t10 |
| back-3 | came-back | Follow-ups of a node: FG7-84 and FG7-85 (after FG7-82), FG7-107, FG7-108, FG7-118, FG7-119 (after FG7-102), FG7-130 ("снова красный") | plans/piles/forge/batch-7-vhodyashchie-4.md:155 | found | — | — | t10 |
| back-4 | came-back | Remainders in package-ci and rules-debt: PC4-8 (tails), PC1-10, PC1-12, PC2-3 (tails of GM3-2), RD1-34, RD1-37 (remainder of B-337), RD1-40 | plans/piles/rules-debt/batch-1-phase-2.md:65 | found | — | — | t17,t18,t20,t21 |
| back-5 | came-back | Remainders in forge-2 to forge-5: F5-7 (red CI after F4-2), F5-9 (merge remainders), F5-10 (critic queue), F6-9 (same class as t-757) | plans/piles/forge/batch-5-vhodyashchie.md:30 | found | — | — | t6,t7 |
## Trail
| tid | op | target | pattern / range | flags | result | control |
|---|---|---|---|---|---|---|
| t1 | grep | C:\QAFactory\forge-repo\plans\piles | `^\| [A-Z][A-Za-z0-9]*-[0-9A-Za-z.-]+ \|` | count glob=batch-*.md | count 2114 | — |
| t2 | read | C:\QAFactory\forge-repo\plans\piles\forge\batch-1-foundation.md | whole file | — | read plans/piles/forge/batch-1-foundation.md:1-63 | — |
| t3 | read | C:\QAFactory\forge-repo\plans\piles\forge\batch-2-critic-measurers.md | whole file | — | read plans/piles/forge/batch-2-critic-measurers.md:1-119 | — |
| t4 | read | C:\QAFactory\forge-repo\plans\piles\forge\batch-3-exam-debts.md | whole file | — | read plans/piles/forge/batch-3-exam-debts.md:1-47 | — |
| t5 | read | C:\QAFactory\forge-repo\plans\piles\forge\batch-4-package-clones.md | whole file | — | read plans/piles/forge/batch-4-package-clones.md:1-133 | — |
| t6 | read | C:\QAFactory\forge-repo\plans\piles\forge\batch-5-vhodyashchie.md | whole file | — | read plans/piles/forge/batch-5-vhodyashchie.md:1-126 | — |
| t7 | read | C:\QAFactory\forge-repo\plans\piles\forge\batch-6-vhodyashchie-2.md | lines 1-115 of 140 | — | read plans/piles/forge/batch-6-vhodyashchie-2.md:1-115 | — |
| t8 | read | C:\QAFactory\forge-repo\plans\piles\forge\batch-7-vhodyashchie-4.md | lines 1-60 | — | read plans/piles/forge/batch-7-vhodyashchie-4.md:1-60 | — |
| t9 | read | C:\QAFactory\forge-repo\plans\piles\forge\batch-7-vhodyashchie-4.md | lines 61-130 | — | read plans/piles/forge/batch-7-vhodyashchie-4.md:61-130 | — |
| t10 | read | C:\QAFactory\forge-repo\plans\piles\forge\batch-7-vhodyashchie-4.md | lines 131-192 | — | read plans/piles/forge/batch-7-vhodyashchie-4.md:131-192 | — |
| t11 | read | C:\QAFactory\forge-repo\plans\piles\github-move\batch-1-chistka-vne-paketa.md | whole file | — | read plans/piles/github-move/batch-1-chistka-vne-paketa.md:1-47 | — |
| t12 | read | C:\QAFactory\forge-repo\plans\piles\github-move\batch-2-paket-i-pereezd.md | whole file | — | read plans/piles/github-move/batch-2-paket-i-pereezd.md:1-47 | — |
| t13 | read | C:\QAFactory\forge-repo\plans\piles\github-move\batch-3-pervyj-reliz.md | whole file | — | read plans/piles/github-move/batch-3-pervyj-reliz.md:1-48 | — |
| t14 | read | C:\QAFactory\forge-repo\plans\piles\proposals\batch-1-predlozheniya.md | whole file | — | read plans/piles/proposals/batch-1-predlozheniya.md:1-41 | — |
| t15 | read | C:\QAFactory\forge-repo\plans\piles\kb\batch-1-kb-update.md | whole file | — | read plans/piles/kb/batch-1-kb-update.md:1-98 | — |
| t16 | read | C:\QAFactory\forge-repo\plans\piles\kb\batch-2-kb-user-guide.md | whole file | — | read plans/piles/kb/batch-2-kb-user-guide.md:1-48 | — |
| t17 | read | C:\QAFactory\forge-repo\plans\piles\package-ci\batch-1-green-ci.md | whole file | — | read plans/piles/package-ci/batch-1-green-ci.md:1-81 | — |
| t18 | read | C:\QAFactory\forge-repo\plans\piles\package-ci\batch-2-potolki-brief-pack.md | whole file | — | read plans/piles/package-ci/batch-2-potolki-brief-pack.md:1-57 | — |
| t19 | read | C:\QAFactory\forge-repo\plans\piles\package-ci\batch-3-khrapovik-doors-only.md | whole file | — | read plans/piles/package-ci/batch-3-khrapovik-doors-only.md:1-49 | — |
| t20 | read | C:\QAFactory\forge-repo\plans\piles\package-ci\batch-4-dieta-testov-td-11-td-15.md | whole file | — | read plans/piles/package-ci/batch-4-dieta-testov-td-11-td-15.md:1-58 | — |
| t21 | read | C:\QAFactory\forge-repo\plans\piles\rules-debt\batch-1-phase-2.md | whole file | — | read plans/piles/rules-debt/batch-1-phase-2.md:1-86 | — |
## Forks
- fork-1: copies of one reader or helper (about 30 nodes, M-top1) were put under M (other) because the text names code that needed repair. The same rows could be read as F (dev process: no one-reader rule). Counts M 187 and F 70 move by that choice.
- fork-2: rows that only say what was built (F0-1, F0-2, PC4-2..5, FG7-132, FG7-133, RD1-16) got `unclear`; GitHub-move chores and PR1-1 got `none`. The origin rule says to use `unclear` when the text does not tell and `none` for chores, so the line between them is a reading call.
this needs a decision from a tier above.
## Not done
- Letter assignment for every row is my reading of the node's own words, done by hand; there is no per-row machine list. Per-row labels exist only in my working notes, not in this report (no file written; role is read-only).
- batch-6-vhodyashchie-2.md lines 116-140 (Ход tail, Живые доказательства, Остатки) were not read; all 59 node rows are in lines 16-74 and were read whole. Owner words that appear only in that tail are not catalogued.
- README.md files of the piles were not read. Sub-kind counts for M and E outside forge-7 are by my reading, not exact.
- My first count grep (brace glob over six piles) returned nothing and was repeated with `glob=batch-*.md` over plans/piles (t1, 110 files, includes piles outside the six); the per-file numbers in q1 come from that run restricted to the 18 given files and match my reading of each file.
- Context use at report time was about 200K tokens, under the 220K stop.
