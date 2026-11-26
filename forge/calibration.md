# Calibration carry list

One row per old weekly calibration check (PROCESS/WEEKLY_CALIBRATION_PROTOCOL.md, 52 measured by `grep -cE '^[0-9]+\. \*\*' PROCESS/WEEKLY_CALIBRATION_PROTOCOL.md`; sub-letters stay inside the row). Carried = a caught case opens to a journal line or a retro file. Journal = `C:/QAFactory/forge-repo/logs/journal/dev1.jsonl`.

| check | caught case (path:line) | outcome protected | how it runs now |
|---|---|---|---|
| 1 | dropped: machinery -- routing/journal check on the coordinator itself (recon C: checks 1-7) | - | - |
| 2 | dropped: machinery -- routing check on the coordinator itself (recon C: 1-7) | - | - |
| 3 | dropped: machinery -- routing check on the coordinator itself (recon C: 1-7) | - | - |
| 4 | none yet in forge 2; kept because forge/COORDINATOR.md Tiers and roles ("reconciled at calibration", FR-1060) relies on it (old check 4) | a role's self-declared model differs from the model that actually ran, and its result counts as that tier's word | weekly reading: each dispatch's recorded model (journal) against the actual execution models in the transcripts; a discrepancy is itself a calibration event (tool: none yet) |
| 5 | dropped: machinery -- routing check on the coordinator itself (recon C: 1-7) | - | - |
| 6 | dropped: machinery -- routing check on the coordinator itself (recon C: 1-7) | - | - |
| 7 | dropped: machinery -- routing check on the coordinator itself (recon C: 1-7) | - | - |
| 8 | dropped: machinery -- the map polices its own maintenance (recon C: 8, 9, 12) | - | - |
| 9 | dropped: machinery -- the map polices its own maintenance (recon C: 8, 9, 12) | - | - |
| 10 | dropped: machinery -- size of the machinery (recon C: 10, 11, 17, 18(e)) | - | - |
| 11 | dropped: machinery -- size of the machinery (recon C: 10, 11, 17, 18(e)) | - | - |
| 12 | dropped: machinery -- the map polices its own maintenance (recon C: 8, 9, 12) | - | - |
| 13 | C:/QAFactory/forge-repo/logs/journal/dev1.jsonl:804 (names: `can only pass`) | a pin whose expected value is computed by the code under test passes by construction (false accept) | acceptance question: where did the expected value come from, outside the code under test? |
| 14 | dropped: no caught case -- search `grep -ciE 'role-prompt edit|exam run' <journal>` found no line naming a catch (positive control, same shape: grep -ciE 'second road|duplicate row' <journal> (finds journal line 4721, count 4)). | - | - |
| 15 | dropped: no caught case -- search `grep -ciE 'recurring critic|repeated critic finding' <journal>` found no line naming a catch (positive control, same shape: grep -ciE 'second road|duplicate row' <journal> (finds journal line 4721, count 4)). The one hit (line 3286) is a Lead re-check of a finding, not a codification catch. | - | - |
| 16 | dropped: no caught case -- search `grep -ciE 'two-pass|external recon' <journal>` found no line naming a catch (positive control, same shape: grep -ciE 'second road|duplicate row' <journal> (finds journal line 4721, count 4)). Hits 221 and 4725 are the calibration run itself and a path note, not catches. | - | - |
| 17 | dropped: machinery -- size and cost of the machinery (recon C) | - | - |
| 18 | 18(a)-(d) dropped: machinery -- economic trend (recon C); 18(e) kept because CLAUDE.md Worker duties ("read at calibration", FR-5) relies on it (old check 18(e)) | independent calls go out in one message, in a worker and in the Lead alike | weekly reading 18(e): for the Lead and each worker role, the share of turns carrying one tool call and the share repeating the kind of the one-call turn before them, against the baseline of old check 18(e), 17-23.11.2026 (one-call turns: coordinator 85 %, builder 77 %, critic 95 %, designer 66 %, scout 22 %); a role whose share does not fall is a finding (tool: none yet) |
| 19 | dropped: machinery -- hook list and liveness probe (recon C) | - | - |
| 20 | dropped: machinery -- judge, dormant, not used (recon C) | - | - |
| 21 | dropped: no caught case -- search `grep -ciE 'not in HEAD|never reached main|accepted work missing' <journal>` found no line naming a catch (positive control, same shape: grep -ciE 'second road|duplicate row' <journal> (finds journal line 4721, count 4)). | - | - |
| 22 | dropped: machinery -- ledger and kit snapshot (recon C) | - | - |
| 23 | dropped: no caught case -- search `grep -ciE 'previous run not closed|closing out the previous' <journal>` found no line naming a catch (positive control, same shape: grep -ciE 'second road|duplicate row' <journal> (finds journal line 4721, count 4)). | - | - |
| 24 | C:/QAFactory/forge-repo/logs/journal/dev1.jsonl:893 (names: `no lint run in builder/integrator witness`) | a defect found twice by canon in two waves becomes a gate step, not a one-off fix | acceptance question: which gate would have caught this defect, and did the fix add it? |
| 25 | dropped: no caught case -- search `grep -ciE 'crossover' <journal>` found no line naming a catch (positive control, same shape: grep -ciE 'second road|duplicate row' <journal> (finds journal line 4721, count 4)). | - | - |
| 26 | dropped: machinery -- hand-back and digest form (recon C: 26, 28, 34) | - | - |
| 27 | dropped: no caught case -- search `grep -ciE 'permission audit found|hygiene audit found' <journal>` found no line naming a catch (positive control, same shape: grep -ciE 'second road|duplicate row' <journal> (finds journal line 4721, count 4)). | - | - |
| 28 | dropped: machinery -- hand-back and digest form (recon C: 26, 28, 34) | - | - |
| 29 | dropped: machinery -- kit snapshot, not applicable here (recon C) | - | - |
| 30 | dropped: no caught case -- search `grep -ciE 'opportunity scan' <journal>` found no line naming a catch (positive control, same shape: grep -ciE 'second road|duplicate row' <journal> (finds journal line 4721, count 4)). | - | - |
| 31 | dropped: machinery -- features and attribution (recon C: 31, 32, 33, 37, 39, 45, 49, 52) | - | - |
| 32 | dropped: machinery -- compact snapshots (recon C) | - | - |
| 33 | 33(a)-(g) dropped: machinery -- piles and batches (recon C); 33(h) kept: old check 33(h), boot form (FG7-51), and `.claude/skills/boot-diet/SKILL.md` relies on it | a rule restated outside its home, an overgrown section or a boot heading nothing routes to costs every session its context | weekly reading 33(h): sample CLAUDE.md, forge/COORDINATOR.md and forge/BOOT.md for a rule restated outside its home, a section over 50 lines and a boot heading with no contents line; each is a finding (tool: none yet; B13 `refs` not built) |
| 34 | dropped: machinery -- hand-back and digest form (recon C: 26, 28, 34) | - | - |
| 35 | dropped: the catch lives only in the frozen package (A27 detectors; no package code in forge 2) | - | - |
| 36 | dropped: no caught case -- search `grep -ciE 'architecture kept|AR-[0-9]+ broken' <journal>` found no line naming a catch (positive control, same shape: grep -ciE 'second road|duplicate row' <journal> (finds journal line 4721, count 4)). | - | - |
| 37 | dropped: machinery -- worktree sweep (recon C) | - | - |
| 38 | dropped: no caught case -- search `grep -ciE 'asked a person before|investigate before ask' <journal>` found no line naming a catch (positive control, same shape: grep -ciE 'second road|duplicate row' <journal> (finds journal line 4721, count 4)). | - | - |
| 39 | dropped: machinery -- remainder executor (recon C) | - | - |
| 40 | C:/QAFactory/forge-repo/logs/journal/dev1.jsonl:179 (names: `BATCH CANON`) | a red the narrow witness missed is caught by the full run on Linux within the hour | tool: CI full run on the merge (ci.py job list) |
| 41 | dropped: machinery -- the judgment census is old-package machinery; forge 2 has no census test (ci-jobs.json carries none) | - | - |
| 42 | C:/QAFactory/forge-repo/logs/journal/dev1.jsonl:4721 (names: `second road`) | two roads for one action (a hook loading its own copy) split the verdict | acceptance question: is there a second road for this action? |
| 43 | dropped: machinery -- no old tests in forge 2 (C1-1 carry map, fp:A17) | - | - |
| 44 | dropped: no caught case -- search `grep -ciE 'delivered as .yes|non-real side' <journal>` found no line naming a catch (positive control, same shape: grep -ciE 'second road|duplicate row' <journal> (finds journal line 4721, count 4)). | - | - |
| 45 | dropped: machinery -- worktree base mismatch (recon C) | - | - |
| 46 | dropped: machinery -- task id race, routing ids (recon C: 46, 48) | - | - |
| 47 | dropped: no caught case -- search `grep -ciE 'scoreboard missing|scoreboard' <journal>` found no line naming a catch (positive control, same shape: grep -ciE 'second road|duplicate row' <journal> (finds journal line 4721, count 4)). The 8 hits place or draft the scoreboard carrier; none is a defect it caught. | - | - |
| 48 | dropped: machinery -- journal by code, merge road (recon C: 46, 48) | - | - |
| 49 | dropped: machinery -- Architect tier (recon C) | - | - |
| 50 | C:/QAFactory/forge-repo/logs/journal/dev1.jsonl:1948 (names: `depended on the temp story path length`) | a row whose result depends on the environment (path length, case folding) is red on the other OS | acceptance question: can this test fail, and for the stated reason, on the CI platform? |
| 51 | C:/QAFactory/forge-repo/logs/journal/dev1.jsonl:5754 (names: `never told at plan/tests/reds`) | a requirement discovered only at the report, never told before the work | weekly reading: the told-before-work walk of the window |
| 52 | dropped: machinery -- retro reduction (recon C) | - | - |
| B1 | forge/owner-words.yaml W-102 (boot page: minimal vs grown) | the boot page grows session by session until it costs more than it saves, or loses what the owner already explained | weekly reading: compare the page at its first size with its current size -- owner repeats and forgotten explanations in the window vs bytes added; a line nobody needed is cut |
| B9 | owner 25.11 ~21:22 (plan:2261-2264) | what got in the agents' way reaches a fix | weekly: `retro.py sum --since <last reading>`; reasons read; per class `fix: <node>` / `already fixing: <node>` / `not fixing: <reason>`; `retro.py missing` count written; the row ends `read through <date>`; the class lines persist between readings in the `B9 classes` list under this table, so a `not fixing` class stays on record and its next entry raises the class's count instead of reopening the analysis |

B9 classes: none yet.

carry: FS-48, FS-204
