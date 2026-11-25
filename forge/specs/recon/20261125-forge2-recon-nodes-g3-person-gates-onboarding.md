<!-- scout hand-back, journal task t-1901, recon for docs/tasks/specs/20261125-forge2-light-factory-plan.md; saved verbatim from the worker's final message -->

digest: v1 forge2-recon-pass2-problems

Read this first (outside the tables):
- Coverage: 435 node rows in 22 files, all 435 classified. Row counts by the row pattern equal the rows I read in every file. batch-10 uses ids like HP1-H1a that the generic pattern misses, so I counted it separately (10).
- Classification is a single pass by my own reading of each row. A two-letter row is counted under both letters in the per-origin counts. Totals by origin letter (letter-counts): T 26, V 14, H 81, M 271, E 33, C 17, F 43, none 15, unclear 24.
- The per-node classification table (435 lines) is NOT in this report. I had no tool to write a file, and 435 lines would not fit in 220. The per-pile counts, problem lists and sub-kind counts below come from it.
- M and E sub-kind counts are approximate, from my tagging as I read. I did not recount node by node.
- Counting caveat: words-gates and onboarding-forge re-list nodes that also appear in gates-and-words and onboarding-hooks (see analog rows). The pile counts add them twice, but the DISTINCT lists below merge them.

## Objects
| id | kind | gist | paths | status | owner | links | ev |
|---|---|---|---|---|---|---|---|
| f01 | filecount | gates-and-words batch-1: rows 54, classified 54 | plans/piles/gates-and-words/batch-1-words-and-gates.md:40-93 | found | — | — | c1,r01 |
| f02 | filecount | words-gates batch-1: rows 47, classified 47 | plans/piles/words-gates/batch-1-slova-i-gejty.md:26-73 | found | — | — | c1,r02 |
| f03 | filecount | onboarding-forge b1: rows 44, classified 44 | plans/piles/onboarding-forge/batch-1-onboarding-roles-forge.md:31-74 | found | — | — | c1,r03 |
| f04 | filecount | onboarding-forge b2: rows 56, classified 56 | plans/piles/onboarding-forge/batch-2-onboarding-roles-forge-p3.md:31-86 | found | — | — | c1,r04 |
| f05 | filecount | onboarding-forge b3: rows 6, classified 6 | plans/piles/onboarding-forge/batch-3-znaniya-o-proekte-fazy-1-6.md:27-32 | found | — | — | c1,r05 |
| f06 | filecount | onboarding-forge b4: rows 30, classified 30 | plans/piles/onboarding-forge/batch-4-hvosty-onbordinga-i-forzha.md:31-60 | found | — | — | c1,r06 |
| f07 | filecount | onboarding-forge b5: rows 14, classified 14 | plans/piles/onboarding-forge/batch-5-ostatki-hf8-4-i-oh3-42.md:28-41 | found | — | — | c1,r07 |
| f08 | filecount | onboarding-hooks b1: rows 11, classified 11 | plans/piles/onboarding-hooks/batch-1-guard-and-install.md:40-50 | found | — | — | c1,r08 |
| f09 | filecount | onboarding-hooks b2: rows 6, classified 6 | plans/piles/onboarding-hooks/batch-2-risk-areas-readers.md:25-30 | found | — | — | c1,r09 |
| f10 | filecount | onboarding-hooks b3: rows 42, classified 42 | plans/piles/onboarding-hooks/batch-3-common-layer-and-readers.md:32-73 | found | — | — | c1,r10 |
| f11 | filecount | onboarding-hooks b4: rows 1, classified 1 | plans/piles/onboarding-hooks/batch-4-hvosty-oh1-11.md:29 | found | — | — | c1,r11 |
| f12 | filecount | onboarding-hooks b5: rows 15, classified 15 | plans/piles/onboarding-hooks/batch-5-nerazlozhennye-nakhodki.md:33-47 | found | — | — | c1,r12 |
| f13 | filecount | onboarding-hooks b6: rows 6, classified 6 | plans/piles/onboarding-hooks/batch-6-ostatki-t-203-i-t-227.md:31-36 | found | — | — | c1,r13 |
| f14 | filecount | onboarding-hooks b7: rows 5, classified 5 | plans/piles/onboarding-hooks/batch-7-ostatki-t-263.md:29-33 | found | — | — | c1,r14 |
| f15 | filecount | onboarding-hooks b8: rows 7, classified 7 | plans/piles/onboarding-hooks/batch-8-ostatki-t-282-t-254-t-287.md:32-38 | found | — | — | c1,r15 |
| f16 | filecount | onboarding-hooks b9: rows 9, classified 9 | plans/piles/onboarding-hooks/batch-9-perepis-podklassov-oh8-7b-h.md:25-33 | found | — | — | c1,r16 |
| f17 | filecount | onboarding-hooks b10: rows 10 (ids HP1-H*), classified 10 | plans/piles/onboarding-hooks/batch-10-profil-khosta-faza-1.md:23-32 | found | — | — | c2,r17 |
| f18 | filecount | project-knowledge b1: rows 9, classified 9 | plans/piles/project-knowledge/batch-1-odin-fakt-naskvoz.md:29-37 | found | — | — | c1,r18 |
| f19 | filecount | project-knowledge b2: rows 22, classified 22 | plans/piles/project-knowledge/batch-2-usloviya-zamena-oglavlenie.md:22-43 | found | — | — | c1,r19 |
| f20 | filecount | told-before-work b1: rows 18, classified 18 | plans/piles/told-before-work/batch-1-finish.md:28-45 | found | — | — | c1,r20 |
| f21 | filecount | roles-context b1: rows 15, classified 15 | plans/piles/roles-context/batch-1-role-texts.md:38-52 | found | — | — | c1,r21 |
| f22 | filecount | roles-context b2: rows 8, classified 8 | plans/piles/roles-context/batch-2-slova-cheloveka-v-brife.md:28-35 | found | — | — | c1,r22 |
| f23 | filecount | Sum of rows 435 equals classified 435; no gap | plans/piles | found | — | f01,f22 | c1,c2 |
| p01 | pile-counts | gates-and-words (54): T3 V0 H30 M32 E2 C1 F3 none0 unclear0 | plans/piles/gates-and-words/batch-1-words-and-gates.md:40 | found | — | f01 | r01 |
| p02 | pile-counts | words-gates (47): T6 V1 H13 M33 E3 C1 F1 none0 unclear0 | plans/piles/words-gates/batch-1-slova-i-gejty.md:26 | found | — | f02 | r02 |
| p03 | pile-counts | onboarding-forge (150): T9 V6 H15 M95 E10 C7 F32 none2 unclear1 | plans/piles/onboarding-forge/batch-1-onboarding-roles-forge.md:31 | found | — | f03-f07 | r03-r07 |
| p04 | pile-counts | onboarding-hooks (112): T5 V7 H11 M84 E17 C3 F5 none9 unclear0 | plans/piles/onboarding-hooks/batch-3-common-layer-and-readers.md:32 | found | — | f08-f17 | r08-r17 |
| p05 | pile-counts | project-knowledge (31): T0 V0 H11 M13 E0 C0 F2 none3 unclear3 | plans/piles/project-knowledge/batch-2-usloviya-zamena-oglavlenie.md:22 | found | — | f18,f19 | r18,r19 |
| p06 | pile-counts | told-before-work (18): E1 none1 unclear16 (rows name only ids on refusals, counters, census; no failure stated) | plans/piles/told-before-work/batch-1-finish.md:28 | found | — | f20 | r20 |
| p07 | pile-counts | roles-context (23): T3 H1 M14 C5 unclear4 (RC1-7, RC2-4, RC2-5, RC2-6) | plans/piles/roles-context/batch-1-role-texts.md:38 | found | — | f21,f22 | r21,r22 |
| tT01 | problem-T | One unfulfillable Then, or mixed outcomes in one case (green, red by bug, blocked), cannot be handed to the person: GW1-14, GW1-22 | plans/piles/gates-and-words/batch-1-words-and-gates.md:53 | found | — | — | r01 |
| tT02 | problem-T | Requirement lands in "Not planned" with no plan row; scope exclusion credited to a person's word: GW1-41, WG1-1 | plans/piles/gates-and-words/batch-1-words-and-gates.md:80 | found | — | — | r01,r02 |
| tT03 | problem-T | Story size and case ceiling wrong (XXL for an M task; 12 cases vs ceiling 10): SC5-6, OH3-15 | plans/piles/words-gates/batch-1-slova-i-gejty.md:55 | found | — | — | r02,r10 |
| tT04 | problem-T | Bug description in ticket Context taken for a requirement (state BEFORE the fix read as AC): RC1-12 | plans/piles/roles-context/batch-1-role-texts.md:49 | found | — | — | r21 |
| tT05 | problem-T | Scout stops on requirement/code conflict that ticket comments already resolve: RC1-13 | plans/piles/roles-context/batch-1-role-texts.md:50 | found | — | — | r21 |
| tT06 | problem-T | Plan does not put what an existing autotest already covers first; retests covered areas: G2-6 | plans/piles/words-gates/batch-1-slova-i-gejty.md:57 | found | — | — | r02 |
| tT07 | problem-T | Manual case precondition has no recipe or stand record; not made via tester's real interface: C3-28 | plans/piles/words-gates/batch-1-slova-i-gejty.md:61 | found | — | — | r02 |
| tT08 | problem-T | Cases lack test-design technique (class/boundary) so inputs go unchecked: G2-7 | plans/piles/words-gates/batch-1-slova-i-gejty.md:63 | found | — | — | r02 |
| tT09 | problem-T | Wrong test level: unverifiable rows and API test-harness surface not routed to manual-human (P16): RC1-2 | plans/piles/onboarding-forge/batch-1-onboarding-roles-forge.md:44 | found | — | — | r03 |
| tT10 | problem-T | Flaky or environment-dependent tests: wall-clock pins, warn_once masking stderr, .pytest_cache on Linux: PC1-7, PC1-12, F6-48, OH5-8 | plans/piles/onboarding-forge/batch-1-onboarding-roles-forge.md:53 | found | — | — | r03,r04,r12 |
| tT11 | problem-T | Tests that cannot fail: mutation keys kill no mutant; reader test table blind; selftest green on wrong header: TQ1-29, OF5-3, OH3-34 | plans/piles/onboarding-forge/batch-2-onboarding-roles-forge-p3.md:66 | found | — | — | r04,r07,r10 |
| tT12 | problem-T | Weak evidence: verification level static/simulated/live not marked; evidence files dropped from delivery: F6-32, OH3-33 | plans/piles/onboarding-forge/batch-2-onboarding-roles-forge-p3.md:75 | found | — | — | r04,r10 |
| tT13 | problem-T | Obsolete or low-value test pins: 8 of 10 red canon cases were stale pins, 0 of 8 critic blockers caught by tests: F6-52 | plans/piles/onboarding-forge/batch-1-onboarding-roles-forge.md:54 | found | — | — | r03 |
| tT14 | problem-T | Runner probe shape not checked against the SDK/API contract (full_reindex sent as request params): EP1-19 | plans/piles/onboarding-forge/batch-2-onboarding-roles-forge-p3.md:45 | found | — | — | r04 |
| tT15 | problem-T | Requirement sources outside the ticket (Confluence, docs in git) invisible to the factory: OH3-39 | plans/piles/onboarding-hooks/batch-3-common-layer-and-readers.md:70 | found | — | — | r10 |
| tV01 | problem-V | Probe or scan assumed pytest or Python only ("not checked"; Python-only env loader scan): EP1-5, OF5-6 | plans/piles/words-gates/batch-1-slova-i-gejty.md:41 | found | — | — | r02,r07 |
| tV02 | problem-V | Nested or monorepo project: git root differs from project root; story path by depth: OH3-5, OF4-19, DC1-7 | plans/piles/onboarding-hooks/batch-3-common-layer-and-readers.md:36 | found | — | — | r10,r06,r03 |
| tV03 | problem-V | Configured artifact root ignored; literal qa-factory/artifacts paths in code and texts: OF4-21, OF4-22, OF5-13 | plans/piles/onboarding-forge/batch-4-hvosty-onbordinga-i-forzha.md:51 | found | — | — | r06,r07 |
| tV04 | problem-V | Login probe assumed {username,password}; stand wants email (422, probe error logged to project backlog): OH3-10 | plans/piles/onboarding-hooks/batch-3-common-layer-and-readers.md:41 | found | — | — | r10 |
| tV05 | problem-V | Onboarding wrote profiles in the wrong form for a Playwright project; capabilities not per adapter: OH3-26, OH3-30 | plans/piles/onboarding-hooks/batch-3-common-layer-and-readers.md:57 | found | — | — | r10 |
| tV06 | problem-V | Test-path markers differ per project (__test__, testing, integration, fixtures, _tests): OH5-14 | plans/piles/onboarding-hooks/batch-5-nerazlozhennye-nakhodki.md:46 | found | — | — | r12 |
| tV07 | problem-V | Host variety: Claude, Codex and unknown hosts need hook events and answers as per-host data: HP1-H1a | plans/piles/onboarding-hooks/batch-10-profil-khosta-faza-1.md:23 | found | — | — | r17 |
| tH01 | problem-H | Person asked what code already knows (keys, integrations, derivables, file deletion): OH3-8, OH3-9, OH3-35 | plans/piles/onboarding-hooks/batch-3-common-layer-and-readers.md:39 | found | — | — | r10 |
| tH02 | problem-H | Person asked again what was already answered (re-asks): GW1-26, GW1-37, GW1-43, PK2-21 | plans/piles/gates-and-words/batch-1-words-and-gates.md:65 | found | — | — | r01,r19 |
| tH03 | problem-H | Person's word lost: free answer unread, not carried to new key, accept not reaching late S5 line: GW1-34, GW1-40, GW1-36, C5-10 | plans/piles/gates-and-words/batch-1-words-and-gates.md:73 | found | — | — | r01,r02 |
| tH04 | problem-H | Person's "yes" or approve recorded nothing (approve plus item answers; sealed proposal refused after the yes): GW1-33, OF1-2 | plans/piles/gates-and-words/batch-1-words-and-gates.md:72 | found | — | — | r01,r03 |
| tH05 | problem-H | Person asked to type commands or script lines (gate B wants waiver.py; doctor and readiness give *.py steps): GW1-3, OH3-6, OF5-9 | plans/piles/onboarding-forge/batch-1-onboarding-roles-forge.md:33 | found | — | — | r01,r03,r07 |
| tH06 | problem-H | Texts misled the person (summary rewords them, "strategist judged so", doctor says healthy, env.example shown as .env): C5-9, GW1-48, OF1-4, OF1-1 | plans/piles/words-gates/batch-1-slova-i-gejty.md:27 | found | — | — | r02,r01,r03 |
| tH07 | problem-H | False warnings and stale paths reach the person (installed 0.10.3 while running 0.10.5; dashboard shows old path): OH1-11, DC1-10 | plans/piles/onboarding-hooks/batch-1-guard-and-install.md:50 | found | — | — | r08,r04 |
| tH08 | problem-H | Gate A hands the person technical phrases or walls (skip row, five answer forms, 14 key questions, 67 KB gate B packet): GW1-28, GW1-32, GW1-31, GW1-35 | plans/piles/gates-and-words/batch-1-words-and-gates.md:67 | found | — | — | r01 |
| tH09 | problem-H | Factory-owned or factory-fixable items offered to the person as a choice (stand fix, dirty branch, factory_fixable): GW1-24, GW1-30, C3-17 | plans/piles/gates-and-words/batch-1-words-and-gates.md:63 | found | — | — | r01,r02 |
| tH10 | problem-H | Integration gap named late (known from onboarding, silent at gate A); Q7 variants swapped; account asked without role: GW1-13, GW1-25, PK0-4 | plans/piles/gates-and-words/batch-1-words-and-gates.md:52 | found | — | — | r01,r18 |
| tH11 | problem-H | Interview too long (about 20 questions, 12 human turns, 7+5 repeated yes); default account asked, accounts are per role: OF3-4, PK2-6, PK0-5 | plans/piles/onboarding-forge/batch-3-znaniya-o-proekte-fazy-1-6.md:30 | found | — | — | r05,r19,r18 |
| tH12 | problem-H | Doctor retells its kitchen; vcs_api 401 without host or step: OH3-12, OH3-11 | plans/piles/onboarding-hooks/batch-3-common-layer-and-readers.md:42 | found | — | — | r10,r03 |
| tH13 | problem-H | Person's key names not matched to the role record; automator ran as admin: OH3-40 | plans/piles/onboarding-hooks/batch-3-common-layer-and-readers.md:71 | found | — | — | r10 |
| tH14 | problem-H | Gate shows no "what you approve" line (gate B); gate A names four documents while the rule says two: GW1-50, GW1-11 | plans/piles/gates-and-words/batch-1-words-and-gates.md:89 | found | — | — | r01 |
| tH15 | problem-H | What the person taught about the stand not saved (28 min of the person, then night run waited 180 s again): SS1-11 | plans/piles/onboarding-forge/batch-2-onboarding-roles-forge-p3.md:39 | found | — | — | r04 |
| tH16 | problem-H | "No chosen stand" refusal heard by the person as "no keys"; stand-gap cards lack price lines: PK2-16, PK2-7 | plans/piles/project-knowledge/batch-2-usloviya-zamena-oglavlenie.md:37 | found | — | — | r19 |
| tH17 | problem-H | Answers to S2-S4 questions not applied at once; risk-areas question missing from onboarding: GW1-21, OH1-10 | plans/piles/gates-and-words/batch-1-words-and-gates.md:60 | found | — | — | r01,r08 |
| tC01 | problem-C | Role start load over ceilings A22/A25 (strategist 54,360 B vs 37,507 pass): RC1-1, RC1-14, OH3-1 | plans/piles/roles-context/batch-1-role-texts.md:51 | found | — | — | r21,r10 |
| tC02 | problem-C | Extra turns from forms (about 370 of about 1225 turns of run 12586); procedure in start text: RC1-11, RC2-7, RC1-8 | plans/piles/roles-context/batch-1-role-texts.md:48 | found | — | — | r21,r22 |
| tC03 | problem-C | Test and canon wall time (canon 6.5 h; one file 7 min; 9 false timeouts): SC2-35, SC2-34, F6-50 | plans/piles/onboarding-forge/batch-1-onboarding-roles-forge.md:47 | found | — | — | r03,r04 |
| tC04 | problem-C | Extra dispatch of 39K tokens because the S3 gate finds one row's problems in two passes: DC1-18 | plans/piles/words-gates/batch-1-slova-i-gejty.md:53 | found | — | — | r02 |
| tC05 | problem-C | Cost of calling run-py.cmd; why so many tests per change; slowest test files: OH5-1, F6-42, PC1-4 | plans/piles/onboarding-hooks/batch-5-nerazlozhennye-nakhodki.md:33 | found | — | — | r12,r03 |
| tF01 | problem-F | Role carriers, navigation and SIBLING_MAP contradict or lag: F6-33, F6-10, F6-41 | plans/piles/onboarding-forge/batch-1-onboarding-roles-forge.md:58 | found | — | — | r03,r04 |
| tF02 | problem-F | Pile leftovers without executor; id closed in another pile; no status command: F6-30, F6-40, F6-13 | plans/piles/onboarding-forge/batch-1-onboarding-roles-forge.md:57 | found | — | — | r03,r04 |
| tF03 | problem-F | BATCH CANON lives in prose, hides later reds, CRLF breaks docker copy: F6-34, F6-47, F6-43 | plans/piles/onboarding-forge/batch-1-onboarding-roles-forge.md:59 | found | — | — | r03 |
| tF04 | problem-F | Builder worktree cut from main not from pile branch; stale worktrees: F6-35, F6-39 | plans/piles/onboarding-forge/batch-1-onboarding-roles-forge.md:60 | found | — | — | r03,r04 |
| tF05 | problem-F | A found problem can be lost because the role has nowhere to write it: G2-4 | plans/piles/onboarding-forge/batch-1-onboarding-roles-forge.md:45 | found | — | — | r03 |
| tF06 | problem-F | Journal: no door for id range of a parallel branch; two clones of a journal file: F6-58, F6-59 | plans/piles/onboarding-forge/batch-2-onboarding-roles-forge-p3.md:83 | found | — | — | r04,r03 |
| tF07 | problem-F | Critic, scout and Lead exams not run after role-file edits: F3-1, F3-2, F3-3 | plans/piles/onboarding-forge/batch-2-onboarding-roles-forge-p3.md:67 | found | — | — | r04 |
| tF08 | problem-F | Duplicated test fixtures (13 files write the register inline; 43 manual markers): OH3-25, F6-17, SC2-26 | plans/piles/onboarding-forge/batch-2-onboarding-roles-forge-p3.md:65 | found | — | — | r04,r10 |
| tF09 | problem-F | Machine pause leaves a journal gap with no event; release without bot; docstring lies; globs overlap: F6-2, F6-31, F6-46, F6-49 | plans/piles/onboarding-forge/batch-2-onboarding-roles-forge-p3.md:70 | found | — | — | r04 |
| tF10 | problem-F | Tests missing, stale or red on release base; rubric wording; long functions grown by a fix: GW1-20, GW1-53, TQ1-28, OF5-4 | plans/piles/gates-and-words/batch-1-words-and-gates.md:59 | found | — | — | r01,r04,r07 |
| tF11 | problem-F | Spec contradictions and doc debts in knowledge pile; rule D-0052 trace in texts: PK2-15, PK0-6, OH1-9 | plans/piles/project-knowledge/batch-2-usloviya-zamena-oglavlenie.md:36 | found | — | — | r19,r18,r08 |
| mM01 | M-subkind | Generic reader/copy duplication, census and ratchets (other); about 130 of 271; e.g. OH1-3, OF4-14, OH9-1 | plans/piles/onboarding-forge/batch-4-hvosty-onbordinga-i-forzha.md:44 | found | — | — | r06,r16 |
| mM02 | M-subkind | Guard or hook refusal and shell parsing; about 28; e.g. SC5-9, OH3-22, CX2-14 | plans/piles/words-gates/batch-1-slova-i-gejty.md:48 | found | — | — | r02,r10 |
| mM03 | M-subkind | State, lock, staleness; about 25; e.g. PC1-3, PK2-18, OH5-7 | plans/piles/onboarding-forge/batch-1-onboarding-roles-forge.md:50 | found | — | — | r03,r19,r12 |
| mM04 | M-subkind | Driver or conductor seam; about 20; e.g. GW1-8, GW1-12, DC1-25 | plans/piles/gates-and-words/batch-1-words-and-gates.md:47 | found | — | — | r01,r02 |
| mM05 | M-subkind | Validator or gate verdict (fail-open, crash read as no errors); about 25; e.g. GW1-9, GW1-52, OH7-3 | plans/piles/gates-and-words/batch-1-words-and-gates.md:48 | found | — | — | r01,r14 |
| mM06 | M-subkind | Generated text or doc drift (door text, texts lag the rule); about 20; e.g. GW1-17, OH7-5, SC5-4 | plans/piles/onboarding-hooks/batch-7-ostatki-t-263.md:33 | found | — | — | r01,r14,r02 |
| mM07 | M-subkind | Form or hand-off shape; about 14; e.g. SC2-42, RC1-11, RC2-8 | plans/piles/roles-context/batch-2-slova-cheloveka-v-brife.md:35 | found | — | — | r04,r21,r22 |
| mE01 | E-subkind | Windows path length, NTFS aliases, CRLF, console encoding, PowerShell; about 14 of 33; e.g. OH3-36, OH8-2, F6-43 | plans/piles/onboarding-hooks/batch-3-common-layer-and-readers.md:67 | found | — | — | r10,r15,r03 |
| mE02 | E-subkind | BOM and encoding readers; about 4; e.g. GW1-19, GW1-38, OF4-26 | plans/piles/gates-and-words/batch-1-words-and-gates.md:58 | found | — | — | r01,r06 |
| mE03 | E-subkind | Host CLI or plugin form (Claude, Codex, ${CLAUDE_PLUGIN_ROOT}, SubagentHandback); about 12; e.g. OH3-13, OH5-2, OH8-4 | plans/piles/onboarding-hooks/batch-3-common-layer-and-readers.md:44 | found | — | — | r10,r12,r15 |
| mE04 | E-subkind | Auth, Linux/posix, machine sleep; about 5; e.g. OH3-11, OF5-14, F6-2 | plans/piles/onboarding-hooks/batch-3-common-layer-and-readers.md:42 | found | — | — | r10,r07,r04 |
| rep01 | M-repeat | Top M problem 1: several readers or copies of one rule or literal (about 22 copies of one predicate): OF4-14, OH1-3, OH6-1 | plans/piles/onboarding-forge/batch-4-hvosty-onbordinga-i-forzha.md:44 | found | — | — | r06,r13 |
| rep02 | M-repeat | Top M problem 2: person's word or answer held in state no reader reads or carries: GW1-34, GW1-45, GW1-36 | plans/piles/gates-and-words/batch-1-words-and-gates.md:73 | found | — | — | r01 |
| rep03 | M-repeat | Top M problem 3: guard misreads shell text as command (heredoc, quotes, PowerShell assignment): SC5-9, OH3-32, CX2-23 | plans/piles/onboarding-hooks/batch-3-common-layer-and-readers.md:63 | found | — | — | r02,r10 |
| rep04 | M-repeat | Top M problem 4: refusal or door text names a dead door or lags the rule: SC5-4, OF4-9, OH7-5 | plans/piles/onboarding-forge/batch-4-hvosty-onbordinga-i-forzha.md:39 | found | — | — | r02,r06,r14 |
| rep05 | M-repeat | Top M problem 5: detector fails open or crashes on odd input (list in field, non-dict file): GW1-9, GW1-49, OH7-3 | plans/piles/onboarding-hooks/batch-7-ostatki-t-263.md:31 | found | — | — | r01,r14 |
| q01 | owner-word | GW1-12, 22.10.2026: «это надо убрать» | plans/piles/gates-and-words/batch-1-words-and-gates.md:51 | found | — | — | r01 |
| q02 | owner-word | GW1-41, 31.10.2026: «очень большой баг, надо поставить забор» | plans/piles/gates-and-words/batch-1-words-and-gates.md:80 | found | — | — | r01 |
| q03 | owner-word | SC5-6, 30.10.2026: «это уже чинится в пачке большого релиза» | plans/piles/words-gates/batch-1-slova-i-gejty.md:55 | found | — | — | r02 |
| q04 | owner-word | G2-6, C3-28, G2-7, 19.10.2026: «класть сейчас» (lines 57, 61, 63) | plans/piles/words-gates/batch-1-slova-i-gejty.md:57 | found | — | — | r02 |
| q05 | owner-word | RC1-12, 28.10.2026: «не в 0.10.5, в пачки» | plans/piles/words-gates/batch-1-slova-i-gejty.md:59 | found | — | — | r02,r21 |
| q06 | owner-word | OH3-35, OH3-39, 31.10.2026: «запиши как баг» | plans/piles/onboarding-forge/batch-1-onboarding-roles-forge.md:36 | found | — | — | r03,r10 |
| q07 | owner-word | G2-4, D-0051 (4), no date given: «если любой агент нашёл проблему, то она не должна теряться только потому, что он не может никуда её записать» | plans/piles/onboarding-forge/batch-1-onboarding-roles-forge.md:45 | found | — | — | r03 |
| q08 | owner-word | OF3 batch header, 12.11.2026: «все фазы хранилища знаний сложи в кучку онбординга» | plans/piles/onboarding-forge/batch-3-znaniya-o-proekte-fazy-1-6.md:5 | found | — | — | r05 |
| q09 | owner-word | OH2 journal, 20.10 (no year): «всё возможное в параллель» | plans/piles/onboarding-hooks/batch-2-risk-areas-readers.md:35 | found | — | — | r09 |
| q10 | owner-word | OH2-4 carry-over, 21.10.2026 (chat 13:1x): «да» | plans/piles/onboarding-hooks/batch-2-risk-areas-readers.md:58 | found | — | — | r09 |
| q11 | owner-word | OH3-8, 29.10.2026: «в онбординге так же не должно быть этого вопроса про ключи… добавь в следующий релиз» | plans/piles/onboarding-hooks/batch-3-common-layer-and-readers.md:39 | found | — | — | r10 |
| q12 | owner-word | OH3-15, 29.10.2026: «добавь ещё в пачку следующего релиза проблему оценки стори» (longer quote at :88) | plans/piles/onboarding-hooks/batch-3-common-layer-and-readers.md:46 | found | — | — | r10 |
| q13 | owner-word | OH3-32, 29.10.2026: «переносим к нам в релиз все пункты… которые ускоряют работу» (also :92) | plans/piles/onboarding-hooks/batch-3-common-layer-and-readers.md:63 | found | — | — | r10 |
| q14 | owner-word | OH3-33, 29.10.2026: «в репозитории не нужны скриншоты их смотрит тестировщик» | plans/piles/onboarding-hooks/batch-3-common-layer-and-readers.md:64 | found | — | — | r10 |
| q15 | owner-word | OH3-34 owner question, via Lead decision 30.10.2026: «учитываются ли рисковые области при написании кейсов» | plans/piles/onboarding-hooks/batch-3-common-layer-and-readers.md:65 | found | — | — | r10 |
| q16 | owner-word | OH3-4, RC1-7, RC1-8, 21.10.2026: «ставь в кучки, сейчас ничего не берём» | plans/piles/onboarding-hooks/batch-3-common-layer-and-readers.md:78 | found | — | — | r10,r21 |
| q17 | owner-word | HP1 header, 24.11.2026: «значит делаем первую фазу» | plans/piles/onboarding-hooks/batch-10-profil-khosta-faza-1.md:7 | found | — | — | r17 |
| q18 | owner-word | HP1 journal, 25.11 (no year): «больше субагентов не запускай» | plans/piles/onboarding-hooks/batch-10-profil-khosta-faza-1.md:39 | found | — | — | r17 |
| q19 | owner-word | PK2 journal, 23.11 (no year): answer «ок» to option (б); PK2-6 row (:27) quotes only «учётку по умолчанию» | plans/piles/project-knowledge/batch-2-usloviya-zamena-oglavlenie.md:52 | found | — | — | r19 |
| q20 | owner-word | TBW header, 17.11.2026, Q-O1: «не в ущерб правилам. Если не влезет можно поднять» | plans/piles/told-before-work/batch-1-finish.md:8 | found | — | — | r20 |
| q21 | owner-word | RC1-14, 30.10.2026: «не на 20 КБ урезать, а решить; либо признаём и поднимаем лимиты» | plans/piles/roles-context/batch-1-role-texts.md:51 | found | — | — | r21 |
| q22 | owner-word | RC1-14, 30.10.2026: «это зависит от того, сможем мы ужать то, что есть, или нет» | plans/piles/roles-context/batch-1-role-texts.md:64 | found | — | — | r21 |
| q23 | owner-word | RC1-11, 26.10.2026: «запиши только (а)» | plans/piles/roles-context/batch-1-role-texts.md:59 | found | — | — | r21 |
| q24 | owner-word | RC2-4, 12.11.2026: «проверь все ли фазы … если не сделаны, то лежат в соответствующих кучках» (full at :48) | plans/piles/roles-context/batch-2-slova-cheloveka-v-brife.md:31 | found | — | — | r22 |
| q25 | owner-phrase | F6-52, 28.10.2026, no quote marks in text: слово владельца «рекомендацию по анализу лишних тестов принимаю» | plans/piles/onboarding-forge/batch-1-onboarding-roles-forge.md:54 | found | — | — | r03 |
| q26 | owner-phrase | OH1-11, 29.10.2026, in parentheses without quote marks: все ложные предупреждения — в 0.10.7; OH1-10 (:49): «вернуть вопрос о рисковых областях» (20.10) | plans/piles/onboarding-hooks/batch-1-guard-and-install.md:50 | found | — | — | r08 |
| rc01 | recurrence | Words «повтор B 177 (закрытая строка бэклога)», «снова», «второй раз»: C3-17, OH1-10, SS1-11, PK2-21, OF1-2 | plans/piles/words-gates/batch-1-slova-i-gejty.md:26 | found | — | — | r02,r08,r04,r19,r03,w1,w3,w4 |
| rc02 | recurrence | Re-ask or repeat of an answered question: GW1-26, GW1-37, GW1-43, OH3-35 (7 + 5 repeated yes), OH5-3 (rerun polls tracker) | plans/piles/gates-and-words/batch-1-words-and-gates.md:65 | found | — | — | r01,r10,r12 |
| rc03 | recurrence | «остаток/остатки» of an earlier fix: GW1-4, GW1-6, GW1-14, GW1-22, GW1-36, CX2-14, RD1-5, F6-28, F6-39, SC2-23 | plans/piles/gates-and-words/batch-1-words-and-gates.md:43 | found | — | — | r01,r02,r03,r04,w1,w2,w3 |
| rc04 | recurrence | Remainder of an earlier fix, continued: SC2-29, F6-12, F6-13, F6-17, HF8-28, OF3-5, OF5-6, OF5-12, OF5-13, RC2-7, OH5-13 | plans/piles/onboarding-forge/batch-2-onboarding-roles-forge-p3.md:42 | found | — | — | r04,r05,r07,r12,r22,w3 |
| rc05 | recurrence | Earlier fix made a new defect: OH8-3 (OH6-1 turned traceback into silent skip); OF5-4 (six long functions grown by HF8-4) | plans/piles/onboarding-hooks/batch-8-ostatki-t-282-t-254-t-287.md:34 | found | — | — | r15,r07 |
| an01 | analog | Duplicate rows inflate pile counts: 11 GW1-n rows in both gates-and-words and words-gates; OH1/OH3/RC1 rows re-listed in onboarding-forge | plans/piles/words-gates/batch-1-slova-i-gejty.md:29 | found | — | f01,f02,f03 | r01,r02,r03 |
| an02 | analog | Keyword grep «снова» also matches inside «обоснование» and «основа»; not every hit is a recurrence | plans/piles/gates-and-words/batch-1-words-and-gates.md:114 | found | — | rc01 | w1 |

## Trail
| tid | op | target | pattern / range | flags | result | control |
|---|---|---|---|---|---|---|
| g0 | glob | plans/piles/{gates-and-words,words-gates,onboarding-forge,onboarding-hooks,project-knowledge,told-before-work,roles-context}/batch-*.md | batch-*.md | — | found 22 | — |
| c1 | grep | plans/piles | `^\| [A-Za-z0-9]+-[0-9]+[a-z]? \|` | count glob=**/batch-*.md | count 2089 | — |
| c2 | grep | plans/piles/onboarding-hooks/batch-10-profil-khosta-faza-1.md | `^\| HP1-H\w+ \|` | count | count 10 | — |
| r01 | read | plans/piles/gates-and-words/batch-1-words-and-gates.md | 1-131 | — | read plans/piles/gates-and-words/batch-1-words-and-gates.md:1-131 | — |
| r02 | read | plans/piles/words-gates/batch-1-slova-i-gejty.md | 20-99 | — | read plans/piles/words-gates/batch-1-slova-i-gejty.md:20-99 | — |
| r03 | read | plans/piles/onboarding-forge/batch-1-onboarding-roles-forge.md | 18-94 | — | read plans/piles/onboarding-forge/batch-1-onboarding-roles-forge.md:18-94 | — |
| r04 | read | plans/piles/onboarding-forge/batch-2-onboarding-roles-forge-p3.md | 20-108 | — | read plans/piles/onboarding-forge/batch-2-onboarding-roles-forge-p3.md:20-108 | — |
| r05 | read | plans/piles/onboarding-forge/batch-3-znaniya-o-proekte-fazy-1-6.md | 1-46 | — | read plans/piles/onboarding-forge/batch-3-znaniya-o-proekte-fazy-1-6.md:1-46 | — |
| r06 | read | plans/piles/onboarding-forge/batch-4-hvosty-onbordinga-i-forzha.md | 14-78 | — | read plans/piles/onboarding-forge/batch-4-hvosty-onbordinga-i-forzha.md:14-78 | — |
| r07 | read | plans/piles/onboarding-forge/batch-5-ostatki-hf8-4-i-oh3-42.md | 14-66 | — | read plans/piles/onboarding-forge/batch-5-ostatki-hf8-4-i-oh3-42.md:14-66 | — |
| r08 | read | plans/piles/onboarding-hooks/batch-1-guard-and-install.md | 16-83 | — | read plans/piles/onboarding-hooks/batch-1-guard-and-install.md:16-83 | — |
| r09 | read | plans/piles/onboarding-hooks/batch-2-risk-areas-readers.md | 14-62 | — | read plans/piles/onboarding-hooks/batch-2-risk-areas-readers.md:14-62 | — |
| r10 | read | plans/piles/onboarding-hooks/batch-3-common-layer-and-readers.md | 20-111 | — | read plans/piles/onboarding-hooks/batch-3-common-layer-and-readers.md:20-111 | — |
| r11 | read | plans/piles/onboarding-hooks/batch-4-hvosty-oh1-11.md | 14-51 | — | read plans/piles/onboarding-hooks/batch-4-hvosty-oh1-11.md:14-51 | — |
| r12 | read | plans/piles/onboarding-hooks/batch-5-nerazlozhennye-nakhodki.md | 18-76 | — | read plans/piles/onboarding-hooks/batch-5-nerazlozhennye-nakhodki.md:18-76 | — |
| r13 | read | plans/piles/onboarding-hooks/batch-6-ostatki-t-203-i-t-227.md | 14-59 | — | read plans/piles/onboarding-hooks/batch-6-ostatki-t-203-i-t-227.md:14-59 | — |
| r14 | read | plans/piles/onboarding-hooks/batch-7-ostatki-t-263.md | 14-55 | — | read plans/piles/onboarding-hooks/batch-7-ostatki-t-263.md:14-55 | — |
| r15 | read | plans/piles/onboarding-hooks/batch-8-ostatki-t-282-t-254-t-287.md | 14-61 | — | read plans/piles/onboarding-hooks/batch-8-ostatki-t-282-t-254-t-287.md:14-61 | — |
| r16 | read | plans/piles/onboarding-hooks/batch-9-perepis-podklassov-oh8-7b-h.md | 12-55 | — | read plans/piles/onboarding-hooks/batch-9-perepis-podklassov-oh8-7b-h.md:12-55 | — |
| r17 | read | plans/piles/onboarding-hooks/batch-10-profil-khosta-faza-1.md | 1-46 | — | read plans/piles/onboarding-hooks/batch-10-profil-khosta-faza-1.md:1-46 | — |
| r18 | read | plans/piles/project-knowledge/batch-1-odin-fakt-naskvoz.md | 10-55 | — | read plans/piles/project-knowledge/batch-1-odin-fakt-naskvoz.md:10-55 | — |
| r19 | read | plans/piles/project-knowledge/batch-2-usloviya-zamena-oglavlenie.md | 10-55 | — | read plans/piles/project-knowledge/batch-2-usloviya-zamena-oglavlenie.md:10-55 | — |
| r20 | read | plans/piles/told-before-work/batch-1-finish.md | 1-63 | — | read plans/piles/told-before-work/batch-1-finish.md:1-63 | — |
| r21 | read | plans/piles/roles-context/batch-1-role-texts.md | 12-87 | — | read plans/piles/roles-context/batch-1-role-texts.md:12-87 | — |
| r22 | read | plans/piles/roles-context/batch-2-slova-cheloveka-v-brife.md | 10-56 | — | read plans/piles/roles-context/batch-2-slova-cheloveka-v-brife.md:10-56 | — |
| w1 | grep | plans/piles/gates-and-words | `(снова|повторно|остаток|остатк|опять|again|remainder|вернул)` | -i content glob=batch-*.md | found 15; plans/piles/gates-and-words/batch-1-words-and-gates.md:43, :45, :53, :61, :75 | — |
| w2 | grep | plans/piles/words-gates | `(снова|повторно|остаток|остатк|опять|again|remainder|вернул)` | -i content glob=batch-*.md | found 7; plans/piles/words-gates/batch-1-slova-i-gejty.md:30, :35, :50, :66 | — |
| w3 | grep | plans/piles/onboarding-forge | `(^|[^а-яё])(снова|повторн|опять|остаток|again|remainder)` | -i content glob=batch-*.md | found 14; plans/piles/onboarding-forge/batch-2-onboarding-roles-forge-p3.md:39, :40, :76 | — |
| w4 | grep | plans/piles/onboarding-hooks | `(^|[^а-яё])(снова|повторн|опять|остаток|again|remainder)` | -i content glob=batch-*.md | found 7; plans/piles/onboarding-hooks/batch-1-guard-and-install.md:49, :50, :56 | — |
| w5 | grep | plans/piles/project-knowledge | `(^|[^а-яё])(снова|повторн|опять|остаток|again|remainder)` | -i content glob=batch-*.md | found 2; plans/piles/project-knowledge/batch-2-usloviya-zamena-oglavlenie.md:42 | — |
| w6 | grep | plans/piles/roles-context | `(^|[^а-яё])(снова|повторн|опять|остаток|again|remainder)` | -i content glob=batch-*.md | found 3; plans/piles/roles-context/batch-2-slova-cheloveka-v-brife.md:34 | — |

## Not done
- Per-node classification table (435 rows) is not delivered; there was no tool to write a file and it would not fit 220 lines. Only counts, merged problem lists and sub-kind counts are given. In the problem lists most ids are examples, not all members.
- M and E sub-kind counts (mM*, mE*) are approximate, from my tagging as I read. The top-5 repeating M problems are by my impression of frequency, not an exact recount.
- Recurrence (item 6) was found by keyword grep (w1 to w6) plus my reading. The first w3/w4 grep passes without the Cyrillic left boundary hit «обоснование» and were discarded. Two brace-glob greps (`{a,b}/batch-*.md`) returned nothing; I treated that as a miscalled glob and did not report it as absence. Told-before-work was never grepped for recurrence words. In reading I noticed none, but that is not a verified negative.
- Preamble lines (before the first table) of several files were not read: gates-and-words lines 1-39 were read, but onboarding-forge b1 1-17, b2 1-19, b4 1-13, b5 1-13, onboarding-hooks b1 1-15, b2 1-13, b3 1-19, b4 1-13, b5 1-17, b6 1-13, b7 1-13, b8 1-13, b9 1-11, project-knowledge 1-9, roles-context b1 1-11 and b2 1-9 were skipped. Row counts from the row pattern (c1, c2) equal the rows I read, so no node row is missing.
- Origin is "unclear" for 24 rows because the row text names no failure: TBW1-2 to TBW1-13 and TBW1-15 to TBW1-18, OF3-5, PK0-2, PK2-3, PK2-5, PK2-8, RC1-7, RC2-4 to RC2-6. 15 rows are "none" (pointers or chores).
- Environment checks were not part of the question; none made.
