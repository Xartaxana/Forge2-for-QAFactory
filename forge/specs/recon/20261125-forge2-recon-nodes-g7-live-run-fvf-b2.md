<!-- scout hand-back, journal task t-1904, recon for docs/tasks/specs/20261125-forge2-light-factory-plan.md; saved verbatim from the worker's final message -->

digest: v1 forge2-recon-pass2-batch2-live-run-fvf

All 96 node rows of the file were classified. The rows are on lines 28-123 of C:\QAFactory\forge-repo\plans\piles\live-run-fvf\batch-2-live-run-fvf.md (written B2: below). Almost every node comes from the factory's own code (M). The per-node map is under Not done. The node texts name no price figures, so none are withheld.

## Objects

| id | kind | gist | paths | status | owner | links | ev |
|---|---|---|---|---|---|---|---|
| q1-count | count | rows by pattern 96, rows classified 96, gap 0; table runs lines 28-123 | B2:28-123 | — | — | — | g1,g2,r1,r2,r3,r4,r5,r6,r7,r8 |
| q2-letters | count | Nodes with the letter (two-letter nodes counted in both): M 86, H 9, V 7, C 7, F 5, T 3, E 1, none 1 | B2:28-123 | — | — | q1-count | r1,r2,r3,r4,r5,r6,r7,r8 |
| q2-pureM | count | Pure M 65 nodes. M with a second letter 21: M+V 6, M+H 7, M+C 6, M+T 1, M+E 1 | B2:28-123 | — | — | q2-letters | r1,r2,r3,r4,r5,r6,r7,r8 |
| q3-T1 | problem | A test pins source text (reads role_cli.py for a literal) instead of behaviour. Nodes FV2-80. | B2:107 | — | — | — | r6 |
| q3-T2 | problem | Negative control sits inside the test itself, a spec defect. Nodes FV2-81. | B2:108 | — | — | — | r6 |
| q3-T3 | problem | Bug drafts and APP_BUG triage rows name an unconfirmed requirement, which gives a bug on an unconfirmed oracle. Nodes FV2-49 (also FV2-45, FV2-46). | B2:76 | — | — | — | r4 |
| q3-V1 | problem | Test selection by id exists only for pytest and playwright; jest, vitest and dotnet-test are always no_selection_form. Nodes FV2-9; py.test alias split, FV2-3. | B2:36 | — | — | — | r1 |
| q3-V2 | problem | A code_repos root can contain the project itself (.., disk root) and declares everything. Nodes FV2-30. | B2:57 | — | — | — | r3 |
| q3-V3 | problem | A stand with an unset build is refused for survey. Nodes FV2-55. | B2:82 | — | — | — | r4 |
| q3-V4 | problem | A stand with form_login (cookie session) is refused by the walker, which knows only a token. Onboarding phase 4 routes form_login to the token question. Nodes FV2-60, FV2-63. | B2:87 | — | — | — | r5 |
| q3-V5 | problem | The secret guard ignores the project's own secret_keys and secret_content_patterns. Nodes FV2-74. | B2:101 | — | — | — | r5 |
| q3-H1 | problem | The login retry variant asks the person to name the sign-in, while the owner gave that to the role. Nodes FV2-38. | B2:65 | owner word 13.11 | — | — | r3 |
| q3-H2 | problem | Text "Did not answer" says a stand was dead when login was merely not tried. Nodes FV2-39. | B2:66 | — | — | — | r3 |
| q3-H3 | problem | After a conductor Stop the answers row is not written, so the same question is asked again without the FR-7 block. Nodes FV2-16, FV2-19. | B2:43 | — | — | — | r1 |
| q3-H4 | problem | The person gets two questions where one is enough: requirement_silent row and claim question; a claim answer must confirm the requirement. Nodes FV2-47, FV2-46. | B2:74 | — | — | — | r4 |
| q3-H5 | problem | The gate B package does not show the source of the expectation next to the bug row. Nodes FV2-48. | B2:75 | — | — | — | r4 |
| q3-H6 | problem | The repair_limit question lists all cases with no ceiling and no "and N more". Nodes FV2-65. | B2:92 | — | — | — | r5 |
| q3-H7 | problem | The conductor "## The refusal" section is cut at 6000 characters and loses the person's choice and the gate prices. Nodes FV2-94. | B2:121 | — | — | — | r7 |
| q3-C1 | problem | Role-page size (native_headroom rows, KR price): temporary headroom row, duplicate verdict sentences (196 B in 12 roles), no code detector. Nodes FV2-79, 87, 90, 91, 92. | B2:106 | — | — | — | r6,r7 |
| q3-C2 | problem | The provocation-line fixture for two refusal sites needs a live probe or a whole run; the role page costs bytes. Nodes FV2-86. | B2:113 | — | — | — | r6 |
| q3-C3 | problem | told_world scans the package twice. Nodes FV2-20. | B2:47 | — | — | — | r2 |
| q3-F1 | problem | A spec phrase is wrong, so the spec is changed or the choice moves to a table. Nodes FV2-11. | B2:38 | — | — | — | r1 |
| q3-F2 | problem | Lead debts left at merge (rows for axes 18/34/17, critic Q9, the quarantine path) are carried as a node. Nodes FV2-14. | B2:41 | — | — | — | r1 |
| q3-F3 | problem | Calibration notes: the commit axis block is not an enumeration, and the owner of cmd_archive is wrong in a report. Nodes FV2-27. | B2:54 | — | — | — | r2 |
| q3-F4 | problem | Live evidence of the ER/RS refusal count on a main run is a Lead chore, with a live-runs row. Nodes FV2-42. | B2:69 | — | — | — | r3 |
| q3-E1 | problem | On Windows the code_repos root differs by letter case and is recorded as a second row of one file. Nodes FV2-32. | B2:59 | — | — | — | r3 |
| q3-none | problem | An observation with no code: a red canon row is an expected consequence of C1. Origin none. Nodes FV2-77. | B2:104 | — | — | — | r6 |
| q4-M-form | subkind | M form/hand-off shape, 9 nodes. Examples FV2-1, FV2-66, FV2-96. | B2:28 | — | — | — | r1,r5,r7 |
| q4-M-guard | subkind | M guard or hook refusal, 7 nodes. Examples FV2-45, FV2-53, FV2-72. | B2:72 | — | — | — | r4 |
| q4-M-state | subkind | M state/lock/staleness, 8 nodes. Examples FV2-16, FV2-34, FV2-57. | B2:43 | — | — | — | r1,r3,r4 |
| q4-M-seam | subkind | M driver or conductor seam, 8 nodes. Examples FV2-17, FV2-18, FV2-95. | B2:44 | — | — | — | r1,r7 |
| q4-M-verdict | subkind | M validator/gate verdict, 18 nodes. Examples FV2-4, FV2-21, FV2-40. | B2:31 | — | — | — | r1,r3 |
| q4-M-drift | subkind | M generated text/doc drift, 6 nodes. Examples FV2-7, FV2-39, FV2-82. | B2:34 | — | — | — | r1,r3,r6 |
| q4-M-other | subkind | M other (two readers or copies of one fact, wrong carrier), 30 nodes. Examples FV2-3, FV2-10, FV2-52. Total 86. | B2:30 | — | — | — | r1,r2,r4 |
| q4-E-sub | subkind | E has only one node (FV2-32); sub-kind other. Examples: that node only. | B2:59 | — | — | q3-E1 | r3 |
| q4-top1 | repeat | Two readers, parsers, regexes or copies of one fact diverge (AR-13/FR-54/P31). About 20 nodes by my hand tally: FV2-3, 10, 35, 52. | B2:62 | — | — | q4-M-other | r1,r3,r4 |
| q4-top2 | repeat | One recorded sign-in with several roads (probe, walker, brief, card, skill, driver). About 9 nodes: FV2-54, 56, 57, 58. | B2:81 | — | — | — | r4,r5 |
| q4-top3 | repeat | A reader treats an unreadable or absent carrier as empty, "no requirement", or silently loses it. About 6 nodes: FV2-21, 40, 83. | B2:48 | — | — | — | r2,r3,r6 |
| q4-top4 | repeat | The reader and the contract or page text diverge. About 6 nodes: FV2-1, 2, 71. | B2:28 | — | — | — | r1,r7 |
| q4-top5 | repeat | A refusal or print site lacks the registry id or bypasses refusal(), or a secret guard is incomplete. About 5 nodes each: FV2-15, 43, 44 and FV2-53, 72, 73. | B2:71 | — | — | — | r3,r4,r5 |
| q5-quote | owner-word | «ок, оставляем» (владелец, 14.11.2026), about S1, node FV2-79. | B2:106 | owner 14.11.2026 | — | — | r6 |
| q5-ref | owner-word | Node text refers to the owner's word without quoting it: "слово владельца 13.11" (FV2-38); "решение владельца 14.11.2026: да, после двух починок…" (FV2-92, a paraphrase). | B2:65 | owner 13.11, 14.11 | — | — | r3,r7 |
| q5-none | owner-word | No other verbatim owner quote in node rows. FV2-48 and FV2-93 say "до слова владельца", with no words given. | B2:75 | — | — | — | r4,r7 |
| q6-again | repeat | Problem back after an earlier fix or merge, from words in the node: FV2-7 (stale after FV1-19), FV2-39 ("осталось в двух носителях"), FV2-41 ("если класс B1 повторился"), FV2-45 (K1 gives the same findings), FV2-58 ("остаток FV1-28f"), FV2-67 ("C1 сделал L-2 срочнее"), FV2-77 (consequence of C1). FV2-16 only repeats a question. | B2:34 | — | — | — | r1,r3,r4,r6 |

## Trail

| tid | op | target | pattern / range | flags | result | control |
|---|---|---|---|---|---|---|
| g1 | grep | C:\QAFactory\forge-repo\plans\piles\live-run-fvf\batch-2-live-run-fvf.md | `^\|---` | — | found 2; B2:27, B2:145 | — |
| g2 | grep | C:\QAFactory\forge-repo\plans\piles\live-run-fvf\batch-2-live-run-fvf.md | `^\| [A-Z0-9-]+ \| П\d` | count | count 96 | — |
| r1 | read | C:\QAFactory\forge-repo\plans\piles\live-run-fvf\batch-2-live-run-fvf.md | 27-41 | — | read C:\QAFactory\forge-repo\plans\piles\live-run-fvf\batch-2-live-run-fvf.md:27-41 | — |
| r2 | read | C:\QAFactory\forge-repo\plans\piles\live-run-fvf\batch-2-live-run-fvf.md | 42-56 | — | read C:\QAFactory\forge-repo\plans\piles\live-run-fvf\batch-2-live-run-fvf.md:42-56 | — |
| r3 | read | C:\QAFactory\forge-repo\plans\piles\live-run-fvf\batch-2-live-run-fvf.md | 57-71 | — | read C:\QAFactory\forge-repo\plans\piles\live-run-fvf\batch-2-live-run-fvf.md:57-71 | — |
| r4 | read | C:\QAFactory\forge-repo\plans\piles\live-run-fvf\batch-2-live-run-fvf.md | 72-86 | — | read C:\QAFactory\forge-repo\plans\piles\live-run-fvf\batch-2-live-run-fvf.md:72-86 | — |
| r5 | read | C:\QAFactory\forge-repo\plans\piles\live-run-fvf\batch-2-live-run-fvf.md | 87-101 | — | read C:\QAFactory\forge-repo\plans\piles\live-run-fvf\batch-2-live-run-fvf.md:87-101 | — |
| r6 | read | C:\QAFactory\forge-repo\plans\piles\live-run-fvf\batch-2-live-run-fvf.md | 102-116 | — | read C:\QAFactory\forge-repo\plans\piles\live-run-fvf\batch-2-live-run-fvf.md:102-116 | — |
| r7 | read | C:\QAFactory\forge-repo\plans\piles\live-run-fvf\batch-2-live-run-fvf.md | 117-131 | — | read C:\QAFactory\forge-repo\plans\piles\live-run-fvf\batch-2-live-run-fvf.md:117-131 | — |
| r8 | read | C:\QAFactory\forge-repo\plans\piles\live-run-fvf\batch-2-live-run-fvf.md | 132-145 | — | read C:\QAFactory\forge-repo\plans\piles\live-run-fvf\batch-2-live-run-fvf.md:132-145 | — |

## Not done

- Reads r7 and r8 also pulled lines 125-145 (the "Ход" section and the live-evidence header) by window overshoot. Nothing from them is classified or quoted. Node rows end at line 123 (FV2-96). No unread range remains. The README and the "Остатки" section were not opened.
- No row was cut by a read window.
- Origin letters are my reading of each node's own words. Where the text only names a pointer or a design choice, I picked the nearest origin and may be off by one letter. The about-N counts in q4-top1..q4-top5 are my hand tally from node text, not a script count. q2-letters is exact by my map below.
- No "nothing about X" claim is made, so no zero search or control is needed. The count in g2 gave 96 and matches the 96 rows I read.
- Observed analog (rule 8), not expanded: the Ход lines I saw name the same family as in other batches (told-before-work, FV1-xx). I did not read them.

Per-node map (id = origin letters; FV2-n):
1 M · 2 M · 3 M+V · 4 M · 5 M · 6 M · 7 M · 8 M · 9 V+M · 10 M · 11 F · 12 M · 13 M · 14 F · 15 M · 16 M+H · 17 M · 18 M · 19 M · 20 M+C · 21 M · 22 M · 23 M · 24 M · 25 M · 26 M · 27 F · 28 M · 29 M · 30 V+M · 31 M · 32 E+M · 33 M · 34 M · 35 M · 36 M · 37 M · 38 H · 39 H+M · 40 M · 41 M · 42 F · 43 M · 44 M · 45 M · 46 M+H · 47 H+M · 48 H+M · 49 T+M · 50 M · 51 M · 52 M · 53 M · 54 M · 55 V+M · 56 M · 57 M · 58 M · 59 M · 60 V+M · 61 M · 62 M · 63 H+V · 64 M · 65 H+M · 66 M · 67 M · 68 M · 69 M · 70 M · 71 M · 72 M · 73 M · 74 M+V · 75 M · 76 M · 77 none · 78 M · 79 C+M · 80 T · 81 T+F · 82 M · 83 M · 84 M · 85 M · 86 M+C · 87 C+M · 88 M · 89 M · 90 C+M · 91 M+C · 92 C · 93 M · 94 M+H · 95 M · 96 M

M sub-kind assignment (ids FV2-n; 86 in total):
- form/hand-off, 9: 1, 2, 66, 70, 71, 76, 78, 93, 96
- guard/hook, 7: 6, 45, 53, 68, 72, 73, 74
- state/staleness, 8: 16, 19, 34, 54, 55, 57, 61, 62
- driver/conductor seam, 8: 13, 15, 17, 18, 35, 75, 94, 95
- validator/gate verdict, 18: 4, 5, 8, 20, 21, 22, 24, 25, 36, 40, 43, 44, 49, 84, 86, 88, 89, 91
- doc/text drift, 6: 7, 39, 79, 82, 87, 90
- other, 30: 3, 9, 10, 12, 23, 26, 28, 29, 30, 31, 32, 33, 37, 41, 46, 47, 48, 50, 51, 52, 56, 58, 59, 60, 64, 65, 67, 69, 83, 85

Origin letters per node (the 96 rows are all of FV2-1 to FV2-96):
- 65 nodes are M alone.
- 21 nodes are M with a second letter (list above).
- 10 nodes have no M: F (11, 14, 27, 42), H (38), H+V (63), T (80), T+F (81), C (92) and none (77).

There are no forks, so there is no Forks section.
