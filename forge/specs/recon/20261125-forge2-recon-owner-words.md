<!-- scout hand-back, journal task t-1884, recon for docs/tasks/specs/20261125-forge2-light-factory-plan.md; saved verbatim from the worker's final message -->

digest: v1 t-1884
Scope note: the form below is digest v1. Your sections A-F map to Objects by `kind`: `A ...` = CARRY OVER (kind reads `A <craft|process> <outcome|means|knowledge>`; the id is the P-n or D-nnnn; the carrier is in `paths`; the owner's word and date are in `owner`). `B-<topic>` = the owner's words by topic. `C` = machinery-only. `D` = contradictions. `E` = open questions. F = the Trail table. Files outside the 11 given were not opened.

## Objects
| id | kind | gist | paths | status | owner | links | ev |
|---|---|---|---|---|---|---|---|
| P1 | A craft means | Code helps the role, never replaces it; on the unforeseen, code reports and does not stop the factory | docs/OWNER_PRINCIPLES.md:7; docs/PROJECT_FULL.md:39 | live | 29.09.2026 collective (D-0009) | D3 | r1,r5 |
| P2 | A craft outcome | Factory is universal: do not hard-code into code what varies between projects | docs/OWNER_PRINCIPLES.md:9; docs/PROJECT_FULL.md:41 | live | 29.09.2026 collective | B-univ-1 | r1,r5 |
| P3 | A craft means | Conductor is a helper in trouble, not a command launcher; code runs commands on stage change or question | docs/OWNER_PRINCIPLES.md:10 | live, tension | 29.09.2026 collective | D2 | r1 |
| P4 | A craft means | Collected material is handed on in YAML so nothing is lost | docs/OWNER_PRINCIPLES.md:12 | live | 29.09.2026 collective | P27 | r1 |
| P5 | A craft outcome | Get task data by every road (API, SSH, browser); LLM agent is never a read source; ask only for access a person can give | docs/OWNER_PRINCIPLES.md:13-20; docs/PROJECT_FULL.md:45-55 | live, refined | «LLM-агент — не источник данных для чтения» 01.10; «заранее понятно что невозможно» 13.10 | D-0043,D-0047 | r1,r3,r5 |
| P6 | A craft knowledge | Rule on code vs LLM cost: take expensive actions off the LLM; the word «Джев» is not explained in these files | docs/OWNER_PRINCIPLES.md:21 | live, unclear | 29.09.2026 collective | E7 | r1 |
| P7 | A craft means | Factory runs on Sonnet or Terra, Haiku nowhere; «Terra» is defined in no given file | docs/OWNER_PRINCIPLES.md:22; docs/TWO_VOCABULARIES.md:11 | live, unclear | 29.09.2026 collective | D11,E7 | r1,r5,r6,g3,g4,g5 |
| P8 | A process outcome | Version-comparison experiments leave no trace in the project: no MR, no Jira comments, bugs only in md or chat | docs/OWNER_PRINCIPLES.md:23 | live, narrowed by D-0042 | 29.09.2026 collective | D-0042 | r1,r3 |
| P9 | A craft outcome | Every question to a person is in human language, never internal ids | docs/OWNER_PRINCIPLES.md:25 | live | 29.09.2026 collective | B-quest-1 | r1 |
| P10 | A craft outcome | Project map and symmetry axes: similar logic at different stages gets one approach | docs/OWNER_PRINCIPLES.md:29 | live | 29.09.2026 collective | P31,D-0055 | r1 |
| P11 | A process outcome | Measure role friction against our code; code that makes a stage dearer is a defect | docs/OWNER_PRINCIPLES.md:30 | live | 29.09.2026 collective | P12 | r1 |
| P12 | A process means | Any new code is checked for similar places and for friction | docs/OWNER_PRINCIPLES.md:31 | live | 29.09.2026 collective | P11 | r1 |
| P13 | A craft outcome | A person's word carries the factory through any gate; the pass is recorded in findings | docs/OWNER_PRINCIPLES.md:32 | live | 29.09.2026 collective | D-0037 | r1,r3 |
| P14 | A craft means | Roles get only the tools they need | docs/OWNER_PRINCIPLES.md:33 | live | 29.09.2026 collective | — | r1 |
| P15 | A craft outcome | A refusal says what is wrong and what is expected, never locks the role; every ban has a door | docs/OWNER_PRINCIPLES.md:34 | live | 29.09.2026 collective | — | r1 |
| P16 | A craft outcome | Pyramid: as few e2e cases as possible; merge cases by parameters; red line must name the case; same in TESTING.md | docs/OWNER_PRINCIPLES.md:36-40; docs/PROJECT_FULL.md:68-73; docs/TESTING.md:266-267 | live | 30.09 (review of 13797) and 04.11.2026 (−1, 0, 1.5, «абв» = ONE test) | D1 | r1,r4,r5 |
| P17 | A craft outcome | Case says WHAT, automator decides HOW; cases to autotests many-to-many; code checks only completeness; critic judges level choice | docs/OWNER_PRINCIPLES.md:41-47; docs/PROJECT_FULL.md:74-82 | live | 30.09.2026 | P19,P28 | r1,r5 |
| P18 | A craft outcome | One true cost per task incl. conductor and chat; equals sum by agents; if sources differ print a range; no money in repo files | docs/OWNER_PRINCIPLES.md:51-57; docs/PROJECT_FULL.md:83-92 | live | 30.09.2026 | B-cost-1 | r1,r5 |
| P19 | A craft outcome | Ladder bottom-up: API/component autotest, else e2e, else agent by hand with before/after, else human, else write and hand over | docs/OWNER_PRINCIPLES.md:58-64; docs/PROJECT_FULL.md:93-101 | live | 30.09.2026 | P17,P28 | r1,r5 |
| P20 | A craft outcome | Code is never the oracle; expectation comes from requirements; silence means ask the person with before/after; no answer means a gap | docs/OWNER_PRINCIPLES.md:65-71; docs/PROJECT_FULL.md:102-111 | live | 01.10.2026 (cmp2 vs MR 684) | P23 | r1,r5 |
| P21 | A craft outcome | Delivery has three outcomes: yes, no, and «ready after the person finishes checks»; Left with you names each item and regression scope | docs/OWNER_PRINCIPLES.md:72-79; docs/PROJECT_FULL.md:112-121 | live; replaced rule 0.7.9 | 02.10 and 03.10.2026 | D4,D5 | r1,r5 |
| P22 | A craft outcome | What the factory cannot handle goes to the conductor, with price and consequences per option; run never stalls; investigate first | docs/OWNER_PRINCIPLES.md:80-92; docs/PROJECT_FULL.md:122-143 | live | 09.10 (D-0039); «сам разбирается» 02.11.2026 | D2,D3 | r1,r3,r5 |
| P23 | A craft outcome | Work by REQUIREMENTS not AC; a task may have no AC; «каждый AC» in a rule is a carrier defect | docs/OWNER_PRINCIPLES.md:96-101; docs/PROJECT_FULL.md:144-150 | live | «Мы работаем по требованиям» 19.10.2026 | D-0049,D-0050 | r1,r3,r5 |
| P24 | A craft outcome | Factory FINDS regression and hands it over, never runs it; one run per story, so the list is right first time | docs/OWNER_PRINCIPLES.md:102-106; docs/PROJECT_FULL.md:151-156 | live | 30.10.2026 | P21,P28 | r1,r5 |
| P25 | A craft outcome | Host and gateway settings (e.g. prompt-cache TTL) are project givens; never propose them as a cure; no keep-alive polling | docs/OWNER_PRINCIPLES.md:107-110; docs/PROJECT_FULL.md:157-161 | live | 27.10 and 05.11.2026 | — | r1,r5 |
| P26 | A craft means | Agent walks a manual case live, code records evidence, conclusion accepted only if citing recorded evidence; analyst resolves every doubtful place | docs/OWNER_PRINCIPLES.md:111-124; docs/PROJECT_FULL.md:162-181 | live | 02.11, 04.11, 05.11.2026 («с одного прогона не 26, а 3–5») | P27 | r1,r5 |
| P27 | A craft means | Code owns data, role owns judgment and outcome, person owns intent; blast radius is a role judgment, not code | docs/OWNER_PRINCIPLES.md:128-137; docs/PROJECT_FULL.md:182-197 | live | «роли сами могли думать» 03.11; радиус 04.11.2026 | D-0060 | r1,r3,r5 |
| P28 | A craft outcome | Automate what will run many times and what is red; strategist decides per plan row; P19 only picks level | docs/OWNER_PRINCIPLES.md:138-142; docs/PROJECT_FULL.md:198-205 | live | 04.11.2026 | P19 | r1,r5 |
| P29 | A craft knowledge | Autotest: split independent from sequential checks; independent ones never hide each other; red probe per check | docs/OWNER_PRINCIPLES.md:143-146; docs/PROJECT_FULL.md:206-209 | live | 06.11.2026 | D6 | r1,r5 |
| P30 | A craft knowledge | Red probe substitutes the value a broken product would give; invert only if the role knows no other; any language | docs/OWNER_PRINCIPLES.md:147-150; docs/PROJECT_FULL.md:210-212 | live | 06.11.2026 | D-0062 | r1,r5 |
| P31 | A craft outcome | Different work roads for the same thing are a bug; no exceptions for languages or projects except by the owner's word | docs/OWNER_PRINCIPLES.md:151-152; docs/PROJECT_FULL.md:213-214 | live | «Нигде не должно быть таких исключений» 06.11.2026 | D-0063 | r1,r5 |
| D-0039 | A craft outcome | Unforeseen state calls conductor; never stall, never promise unkept; free text read by conductor, code reads closed options only | docs/DECISIONS_ARCHIVE.md:43,76,269 | live; carrier P22 | «чем-то помочь… с ценой и последствиями» 09.10.2026 | P22 | r3 |
| D-0043 | A craft outcome | Never ask about what the factory itself proved unreachable; one class decision covers all instances until run end | docs/DECISIONS_ARCHIVE.md:49,79,272 | live; refined by D-0047 | «фабрика не должна обещать… невозможное» 13.10.2026 | P5 | r3 |
| D-0047 | A craft outcome | Standing decision applied without new question but SAID aloud; report names a gap only where it changes what is left to the person | docs/DECISIONS_ARCHIVE.md:85,275 | live; refines D-0043 | «озвучить… Если промолчал, значит решение в силе» 16.10.2026 | P5 | r3 |
| D-0041 | A craft means | Question may be asked by code; an answer code cannot read goes to the AI conductor, always | docs/DECISIONS_ARCHIVE.md:70,136 | live | «вопрос может задавать код, читать непонятный ответ будет ИИ» 10.10.2026 | P22 | r3 |
| D-0049 | A craft outcome | Grounding: implementation checked against requirements before tests, by the test-plan writer, with blast radius; refactor over 30 percent reported, over 50 stop | docs/DECISIONS_ARCHIVE.md:91,280 | live | «Мы работаем по требованиям» 19.10.2026 | P23,P27 | r3 |
| D-0050 | A craft outcome | Ticket without AC does not stop S0; stop only for a read failure, named as the factory's own defect | docs/DECISIONS_ARCHIVE.md:94,283 | live | «Если AC нет, то это не блокирует работу» 19.10.2026 | P23,D3 | r3 |
| D-0051 | A craft outcome | Grounding forks: under 50 percent requirements implemented means stop; suspicious code becomes a candidate bug with a test; any agent can record a problem | docs/DECISIONS_ARCHIVE.md:97 | live | «не должна теряться» 19.10.2026 | D-0049,D3 | r3 |
| D-0052 | A craft outcome | Collect skill gathers everything since the last collect, code-driven; user adaptations always leave a finding trail | docs/DECISIONS_ARCHIVE.md:100,106 | live | 19.10.2026; 30.10.2026 «да, брать» | D-0053 | r3 |
| D-0055 | A process outcome | Four architecture goals A universality, B low friction, C one way everywhere, D continuity between stages; map AR-1..AR-28 | docs/DECISIONS_ARCHIVE.md:109 | live | «чтобы фабрика могла работать на разных проектах» 20.10.2026 | P10,P31 | r3 |
| D-0060 | A craft means | Roles think; scripts only ease; rules are tester experience; AR-29; experiment branch with charters | docs/DECISIONS_ARCHIVE.md:115 | live | «Именно так и было задуманно, но выродилось» 03.11.2026 | P27 | r3 |
| D-0062 | A craft knowledge | Red probe: one road for every language; forms are data rows; only our marker text proves a check fired | docs/DECISIONS_ARCHIVE.md:154 | live | six answers 06.11.2026 | P30,P31 | r3 |
| D-0010+D-0012+D-0028 | A craft outcome | Every NEW or changed test gets a live probe in any language; only a failed live check blocks delivery | docs/DECISIONS_ARCHIVE.md:238,239,248 | live | 29.09 and 06.10.2026 | D6 | r3 |
| D-0013 | A craft outcome | Critic `unverified` is its own word: no rejection; blocks the readiness verdict and goes to Left with you | docs/DECISIONS_ARCHIVE.md:240 | live | 29.09.2026 | P21 | r3 |
| D-0014 | A craft outcome | Project without confirmed stand is asked once before tests; one word passes S5 and S6 | docs/DECISIONS_ARCHIVE.md:241 | live | 29.09.2026 | D-0029 | r3 |
| D-0029+D-0032+D-0026+D-0034 | A craft outcome | Stand gap: say case or level; config-caused gap recorded once in environment record; file or machine fault never recorded | docs/DECISIONS_ARCHIVE.md:247,249,252,253 | live | 06.10 and 07.10.2026 «ок» | D-0014 | r3 |
| D-0030 | A craft outcome | Where a project keeps its tests is the project's word; marker list is not a gate | docs/DECISIONS_ARCHIVE.md:250 | live | 06.10.2026 | P2 | r3 |
| D-0031 | A craft means | Unreadable test report: code tries every reader, then conductor proposes a local data adaptation, person asked last | docs/DECISIONS_ARCHIVE.md:251 | live | 06.10.2026 | P22 | r3 |
| D-0018+D-0020+D-0017 | A craft means | Test-run budget per story: author one run, critic one red probe, no other runs; cosmetic edit keeps its proof | docs/DECISIONS_ARCHIVE.md:243,245,242 | live | 29.09.2026 | D6 | r3 |
| D-0023 | A craft means | Reporter proof is taken once at onboarding per project, profile and command; not per stand | docs/DECISIONS_ARCHIVE.md:40,121,246 | live | «ок» 04.10.2026 | D-0014 | r3 |
| D-0027 | A craft means | Ticket freshness is one command with one trigger on both skill and driver paths | docs/DECISIONS_ARCHIVE.md:228 | live | 06.10.2026 | P5 | r3 |
| D-0061 | A craft means | S5 automation runs in 3 parallel windows by default; one window stays byte-equal to the serial road | docs/DECISIONS_ARCHIVE.md:151 | live on experiment branch | Lead 10.11.2026 | P17 | r3 |
| B-purpose-1 | B purpose | The factory must test the ticket and account for what the person wants | docs/DECISIONS_ARCHIVE.md:43 | word | «чтобы протестировать тикет и учесть то, что хочет человек» 09.10.2026 | P22 | r3 |
| B-purpose-2 | B purpose | Goal: get ALL requirements that exist in the task; AC are one source among others | docs/DECISIONS_ARCHIVE.md:94 | word | «Цель получить все требования, что есть в задаче» 19.10.2026 | P23 | r3 |
| B-purpose-3 | B purpose | Factory must show what it copes with and what not (project passport collected) | docs/DECISIONS_ARCHIVE.md:100 | word | «с чем фабрика справляется, а с чем нет» 19.10.2026 | D-0052 | r3 |
| B-purpose-4 | B purpose | Roles keep flexibility and ability to think but get a direction that reaches a result faster | docs/PROJECT_FULL.md:185-186 | word | «найти все несоответствия, вопросы и баги» 03.11.2026 | P27 | r5 |
| B-univ-1 | B universality | Factory must work on different projects with less friction; later fixes must not break it | docs/DECISIONS_ARCHIVE.md:109 | word | «Нельзя допустить, чтобы дальнейшие изменения… сломали это» 20.10.2026 | D-0055 | r3 |
| B-univ-2 | B universality | A finding names a factory class, not one project's rule | docs/PROJECT_FULL.md:349-351 | word | 24.10.2026 | P2 | r5 |
| B-univ-3 | B universality | Blast radius cannot be solved by one universal script: it differs per language and repo layout | docs/PROJECT_FULL.md:192-197 | word | «в разных проектах… всегда по-разному» 04.11.2026 | P27 | r5 |
| B-univ-4 | B universality | Agent adapts live because projects are many: «заранее не угадаешь, как всё пойдёт» | docs/PROJECT_FULL.md:162-164 | word | 02.11.2026 | P26 | r5 |
| B-pyr-1 | B pyramid | No dated owner word on pyramid or case-vs-autotest beyond P16, P17, P19, P28; only a passing e2e mention in D-0060 | docs/DECISIONS_ARCHIVE.md:115 | absent-beyond-P | — | P16 | r3,g7 |
| B-pyr-2 | B pyramid | Critic rule «один кейс — один сценарий» produced four cases and contradicts P16; to be fixed in the charter | docs/PROJECT_FULL.md:72-73 | word | 04.11.2026 | D1 | r5 |
| B-req-1 | B requirements | Forge side: forge has no requirements, its spec is the requirement; expectation from spec, never from code output | docs/TESTING.md:67-72 | word, forge only | «у нас в фордже и требований нет. Или вместо них у нас спека?» 17.11.2026 | P20 | r4 |
| B-rep-1 | B report | Only P18 mentions a dashboard; no owner word defines dashboard content in the given files | docs/PROJECT_FULL.md:83 | open | — | E2 | r5,g6 |
| B-rep-2 | B report | Report says the provenance of a standing decision and mentions a gap only where it changes what is left | docs/DECISIONS_ARCHIVE.md:85 | word | «Если эта информация нужна, то появляется, если нет, то нет» 16.10.2026 | D-0047 | r3 |
| B-rep-3 | B report | Wrong MR or under-implemented requirements are a plan line the person cannot miss | docs/DECISIONS_ARCHIVE.md:97 | word | «подсвечиваем… так, чтобы пользователь точно увидел» 19.10.2026 | D-0051 | r3 |
| B-quest-1 | B questions | A question is asked by code, an unreadable answer is read by the AI | docs/DECISIONS_ARCHIVE.md:70 | word | «вопрос может задавать код, читать непонятный ответ будет ИИ» 10.10.2026 | D-0041 | r3 |
| B-quest-2 | B questions | Silence on a voiced standing decision keeps it in force | docs/DECISIONS_ARCHIVE.md:85 | word | «Если промолчал, значит решение в силе» 16.10.2026 | D-0047 | r3 |
| B-quest-3 | B questions | Show before/after to a person; unclear requirement is a question to the owner, not a technical choice | docs/PROJECT_FULL.md:434-435 | word | 01.10.2026 (P20) | P20 | r5 |
| B-cost-1 | B cost | Five token-cost measures: worker context cap, fresh fix worker, one witness run, one critic pass per topic | docs/DECISIONS_ARCHIVE.md:61 | word, forge only | «чтобы вся дальнейшая разработка была дешевле» 07.10.2026 | D-0035 | r3 |
| B-cost-2 | B cost | Tests in CI not on the owner's machine; canon always CI within 60 minutes | docs/DECISIONS_ARCHIVE.md:148 | word, forge only | «Канон всегда на CI» 03.11.2026 | D-0059 | r3 |
| B-cost-3 | B models | No Haiku anywhere; scout is Sonnet | docs/DECISIONS_ARCHIVE.md:260 | word | 29.09.2026 | P7 | r3 |
| B-code-1 | B code versus role | Rule 7 in D-0060 analysis: 94 code checks judge by shape, none by meaning; craft is about 1:29 of role text | docs/DECISIONS_ARCHIVE.md:115 | fact | 03.11.2026 | P27 | r3 |
| B-code-2 | B code versus role | What code can do, code does (coordinator offload); journal written by code | docs/DECISIONS_ARCHIVE.md:294 | word, forge only | «это было правило для экономии токенов модели» 14.11.2026 | D-0066 | r3 |
| B-forge-1 | B forge process | Tests: «Покрыть тестами всё нельзя»; three layers, a case comes from a defect | docs/TESTING.md:38-41,59-63 | word | 10.11.2026 | D-0059 | r4 |
| B-forge-2 | B forge process | Test files: decided by the goal, not by the owner's word; builder must know the test budget in advance | docs/TESTING.md:230-233,219-223 | word | 17.11 and 18.11.2026 | B-forge-1 | r4 |
| B-forge-3 | B forge process | A test file is red-checked by one probe, no mutant sets: «не вернуться к куче мутантов» | docs/TESTING.md:155-156 | word | 17.11.2026 | D7 | r4 |
| B-forge-4 | B forge process | One dry story through the real driver; a real run holds neither node nor batch | docs/TESTING.md:49-52,252-254 | word | 14.11 and 24.11.2026 | D-0059 | r4 |
| B-forge-5 | B forge process | Residuals ideally none; live runs move to pile live-runs and never hold a batch | docs/PROJECT_FULL.md:381-392 | word | 21.10 and 11.11.2026 | — | r5 |
| B-forge-6 | B forge process | New-idea order: lead understands, scouts, questions, short plan to the owner, designer, critic on plan, streams, code, critic | docs/PROJECT_FULL.md:281-301 | word | 11.11.2026 | — | r5 |
| B-forge-7 | B forge process | Owner asleep means no blocking questions; decide technical forks and mark «решила сама» | docs/PROJECT_FULL.md:429-441 | word | 27.10.2026 | — | r5 |
| B-forge-8 | B forge process | Knowledge lives in the project not in machine memory; nodes written for a weaker model | docs/PROJECT_FULL.md:393-403 | word | 30.10.2026 | — | r5 |
| B-forge-9 | B forge process | Ladder: Lead opus, Architect fable above Lead, owner-summoned; D-0067 | docs/DECISIONS_ARCHIVE.md:166 | word | 16-17.11.2026 | — | r2,r3 |
| B-forge-10 | B forge process | Goal-document yardstick of this dispatch (free agent, light factory, forge2) is in none of the given files | docs/RELATED_WORK.md:221-239 | open | — | E1 | r7,g9 |
| C-env | C machinery | D-0001/D-0064 repo names; D-0007 plugin off in forge; D-0008 FR walk; D-0009 principles to FR | docs/DECISIONS_ARCHIVE.md:213,266,216,219 | live; carrier PROJECT | 29.09.2026 | — | r3 |
| C-tier | C machinery | D-0002/D-0003/D-0004/D-0005/D-0006/D-0016: model bindings, exam skips, contour; D-0067 supersedes lead binding | docs/DECISIONS_ARCHIVE.md:260,263,11,14,17,222 | live or built-not | 29.09-17.11.2026 | D-0067 | r3 |
| C-exam | C machinery | D-0037/D-0058/D-0063: exam deferrals recorded as passes for critic.md edits | docs/DECISIONS.md:16-17 | live | 09.10.2026 | — | r2,r3 |
| C-cost | C machinery | D-0035/D-0038/D-0040/D-0054: worker caps, parallel cap 6, fresh worker remainder; process cost control | docs/DECISIONS_ARCHIVE.md:124,130,133,103 | live | 07.10-21.10.2026 | — | r3 |
| C-piles | C machinery | D-0036/D-0044/D-0048/D-0065: piles, batches, finding-to-batch, hot files, PILES.md retired | docs/DECISIONS_ARCHIVE.md:127,142,88,291 | live | 08.10-13.11.2026 | D8 | r3 |
| C-test | C machinery | D-0056/D-0057/D-0059/D-0033: batch canon in CI, ratchets; builder narrow witness | docs/DECISIONS_ARCHIVE.md:112,145,148,158 | live; partly superseded | 06.10-03.11.2026 | D7 | r3 |
| C-gates | C machinery | D-0021/D-0022/D-0025/D-0066: designer edge rule, dispatch manifest, owner-word attribution, coordinator offload | docs/DECISIONS_ARCHIVE.md:34,37,225,294 | live | 30.09-16.11.2026 | — | r3 |
| C-cmp | C machinery | D-0011/D-0015/D-0019/D-0042: comparison-run plans and answer files | docs/DECISIONS_ARCHIVE.md:20,23,31,73 | live or archived | 29.09-10.10.2026 | P8 | r3 |
| C-skills | C machinery | D-0053/D-0046: collect-skill design forks; fix-round recording (D-0046 replaced by COORDINATOR rule 12, 17.11.2026) | docs/DECISIONS_ARCHIVE.md:106,55,297 | replaced for D-0046 | 19.10, 17.11.2026 | D-0052 | r3 |
| C-docs | C machinery | ADOPTION_LEDGER, CLAUDE_HOST_ADAPTATIONS_FULL, provenance, FINDINGS F-1..F-3, TWO_VOCABULARIES serve the delegation kit and history only | docs/ADOPTION_LEDGER.md:81; docs/provenance.md:13; docs/FINDINGS.md:8; docs/TWO_VOCABULARIES.md:9 | live | — | — | r6,r8,r9,r10,r11 |
| C-research | C machinery | RELATED_WORK covers external tools (DMtools, Testing Factory, crapper, mocks); owner words only as orders to research | docs/RELATED_WORK.md:8,68,221,241,268 | candidates open | 01.10, 21.10, 24.11.2026 | E8 | r7 |
| D1 | D contradiction | P16 «one behaviour per case is unit-level» vs critic rule «one case — one scenario» (named by owner) | docs/PROJECT_FULL.md:71-73 | fix recorded as to be done; done-state not in files | 30.09 vs 04.11.2026 | P16 | r5 |
| D2 | D contradiction | P3 conductor is no command launcher vs P22/D-0039: conductor executes choices and dispatches via controller | docs/OWNER_PRINCIPLES.md:10 vs :84-86; docs/DECISIONS_ARCHIVE.md:76 | later word 09.10 lifts ban | 29.09 vs 09.10.2026 | P3,P22 | r1,r3 |
| D3 | D contradiction | P1 and P22 «never stall» vs D-0050/D-0049/D-0051 stops (read failure, under 50 percent implemented, over 50 percent refactor) | docs/OWNER_PRINCIPLES.md:7-8,87 vs docs/DECISIONS_ARCHIVE.md:91,94,97 | tension; stops are closed questions | 09.10 vs 19.10.2026 | P1,P22 | r1,r3 |
| D4 | D replaced | P21 third verdict replaces 0.7.9 rule «handed_to_person → delivery_ready: no» | docs/PROJECT_FULL.md:121 | replaced | 02.10-03.10.2026 | P21 | r5 |
| D5 | D contradiction | D-0025 voids «owner's decision» dated 02.10, 03.10, 06.10 in branch dev2/codex-fixes-migration; P21 is dated 02.10 and 03.10 in main | docs/DECISIONS_ARCHIVE.md:225 vs docs/OWNER_PRINCIPLES.md:79 | unresolved provenance question | 06.10.2026 | P21,E9 | r1,r3 |
| D6 | D contradiction | D-0018 «one critic red probe per story, no other runs» vs P29/P30 red probe per check and D-0010 probe on every test | docs/DECISIONS_ARCHIVE.md:243,238 vs docs/OWNER_PRINCIPLES.md:143-150 | later word 06.11 wins by date; no file says D-0018 is replaced | 29.09 vs 06.11.2026 | P29 | r1,r3 |
| D7 | D replaced | D-0056 (2) builder names mutants vs TESTING: builder neither runs nor lists mutations | docs/DECISIONS_ARCHIVE.md:112 vs docs/TESTING.md:128-130,155-156 | partly replaced | 21.10 vs 28.10-17.11.2026 | B-forge-3 | r3,r4 |
| D8 | D replaced | PROJECT_FULL still says PILES.md is generated by `piles.py board` and the GitLab mirror exists; D-0065 retires it, word 04.11 turns the board off | docs/PROJECT_FULL.md:331,372 vs docs/DECISIONS_ARCHIVE.md:291 | PROJECT_FULL stale | 08.10 vs 13.11.2026 | C-piles | r3,r5 |
| D9 | D chain | Replaced or refined: D-0043 by D-0047; D-0035(5) cap 4 by D-0054 6 by D-0066; D-0056(3) docker by D-0059; D-0033 clause by D-0057; D-0003 lead by D-0067; D-0001 by D-0064; D-0024 by D-0026, D-0027, D-0028; D-0023 amends D-0019(2); D-0034 amends D-0026 | docs/DECISIONS_ARCHIVE.md:49,85,61,103,112,148,158,145,263,213,286,25,246,253 | replaced | 29.09-17.11.2026 | — | r3 |
| D10 | D tension | P7 «Sonnet or Terra, no Haiku» vs D-0067 Lead on opus and Architect on fable; scope (factory or forge) not stated | docs/OWNER_PRINCIPLES.md:22; DECISIONS.md:18 | unclear scope | 29.09 vs 16-17.11.2026 | P7,E7 | r1,r2 |
| D11 | D id clash | PROJECT_FULL P5 cites «D-06» (a backlog id of 01.10) while D-0006 is the contour decision; OWNER_PRINCIPLES P5 cites 01.10 and 13.10 but not 16.10 (D-0047) | docs/PROJECT_FULL.md:47; docs/OWNER_PRINCIPLES.md:20 | cosmetic | — | P5 | r1,r5 |
| E1 | E open | What «light factory» and «forge2» mean; which of stages S0-S9 survive: no owner word in given files | docs/RELATED_WORK.md:221 | open | — | B-forge-10 | r7,g9 |
| E2 | E open | Dashboard content and who reads it: P18 only says cost sits on dashboard and retro | docs/PROJECT_FULL.md:83 | open | — | B-rep-1 | r5,g6 |
| E3 | E open | Which pyramid levels a new factory has besides API, component, e2e; unit-level role of the factory | docs/OWNER_PRINCIPLES.md:36-47 | open | — | P16,P19 | r1 |
| E4 | E open | Onboarding for a new project: only stand ask-once, reporter proof, test locations; nothing says what a new factory asks first | docs/DECISIONS_ARCHIVE.md:241,246,250 | open | — | D-0014,D-0023,D-0030 | r3 |
| E5 | E open | Evidence rules beyond manual cases (P26): what evidence an autotest verdict carries is not in these files | docs/OWNER_PRINCIPLES.md:111-115 | open | — | P26 | r1 |
| E6 | E open | Thresholds 30 and 50 percent are «data»: values for a new project type or language not stated | docs/DECISIONS_ARCHIVE.md:91 | open | — | D-0049 | r3 |
| E7 | E open | Meaning of «Джев» (P6) and «Terra» (P7); no definition in any given file or in DECISIONS.md | docs/OWNER_PRINCIPLES.md:21-22; DECISIONS.md:15 | absent | — | P6,P7,D10 | r1,g3,g4,g5,g6 |
| E8 | E open | Candidates K1-K11 from Testing Factory review stand undecided; mock ideas wait for internal recon | docs/RELATED_WORK.md:172-200,268-279 | open | — | C-research | r7 |
| E9 | E open | Whether P21 (02.10, 03.10) stands as an owner word given D-0025 | docs/DECISIONS_ARCHIVE.md:225 | open | — | D5 | r3 |
| E10 | E open | What the goal document replaces: whether P1-P31 are carried unchanged or reopened for a new factory | docs/OWNER_PRINCIPLES.md:3 | open | — | — | r1 |

## Trail
| tid | op | target | pattern / range | flags | result | control |
|---|---|---|---|---|---|---|
| r1 | read | docs/OWNER_PRINCIPLES.md | 1-152 | — | read docs/OWNER_PRINCIPLES.md:1-152 | — |
| r2 | read | DECISIONS.md | 1-18 | — | read DECISIONS.md:1-18 | — |
| r3 | read | docs/DECISIONS_ARCHIVE.md | 1-297 | — | read docs/DECISIONS_ARCHIVE.md:1-297 | — |
| r4 | read | docs/TESTING.md | 1-311 | — | read docs/TESTING.md:1-311 | — |
| r5 | read | docs/PROJECT_FULL.md | 1-457 | — | read docs/PROJECT_FULL.md:1-457 | — |
| r6 | read | docs/TWO_VOCABULARIES.md | 1-25 | — | read docs/TWO_VOCABULARIES.md:1-25 | — |
| r7 | read | docs/RELATED_WORK.md | 1-284 | — | read docs/RELATED_WORK.md:1-284 | — |
| r8 | read | docs/ADOPTION_LEDGER.md | 1-153 | — | read docs/ADOPTION_LEDGER.md:1-153 | — |
| r9 | read | docs/FINDINGS.md | 1-101 | — | read docs/FINDINGS.md:1-101 | — |
| r10 | read | docs/CLAUDE_HOST_ADAPTATIONS_FULL.md | 1-72 | — | read docs/CLAUDE_HOST_ADAPTATIONS_FULL.md:1-72 | — |
| r11 | read | docs/provenance.md | 1-232 | — | read docs/provenance.md:1-232 | — |
| g1 | grep | DECISIONS.md | `^#+ ` | content | found 1; DECISIONS.md:1 | — |
| g2 | grep | docs/DECISIONS_ARCHIVE.md | `^#+ ` | content | found 80; docs/DECISIONS_ARCHIVE.md:1 | — |
| g3 | grep | DECISIONS.md | `Terra\|дашборд\|dashboard\|универсальн\|free agent` | -i count | count 0 | g4 |
| g4 | grep | DECISIONS.md | `ladder\|opus` | -i count | count 1 | — |
| g5 | grep | DECISIONS.md | `Sonnet` | -i count | count 0 | g4 |
| g6 | grep | docs | `Terra\|дашборд\|dashboard\|свободн\w+ агент\|free agent\|универсальн` | -i content glob=given10 | found 9; docs/OWNER_PRINCIPLES.md:22, docs/PROJECT_FULL.md:83 | — |
| g7 | grep | docs | `пирамид\|pyramid\|уровн\w+ API\|e2e` | -i count glob=given8 | count 1 | — |
| g8 | grep | docs/TESTING.md | `дашборд\|dashboard\|отчёт\|report` | -i count | count 12 | — |
| g9 | grep | docs | `лёгк\|легк\|light\|forge2\|free agent\|свободн\w+ агент\|один промпт\|one prompt` | -i content glob=given10 | found 5; docs/ADOPTION_LEDGER.md:96, docs/FINDINGS.md:50 | — |

## Forks
- OWNER_PRINCIPLES.md (153 lines) and PROJECT_FULL.md hold the same P1-P31 but differ in length. PROJECT_FULL carries extra owner text: P16 context 04.11 (line 71-73), P19 closing sentence (line 99-101), P22 verbatim quote 02.11 (line 138-143), P26 detail 05.11 (line 169-181). OWNER_PRINCIPLES carries shortened forms. Which file is the carrier of record is stated in neither, so a goal document must pick which one it cites.
- Many P-lines (P10, P11, P12, P14) are mixed: they bind the factory and also the dev process; the files do not label which side is meant.
this needs a decision from a tier above.

## Not done
- Line numbers in `paths` come from the Read output; the 80-heading count (g2) was counted by hand from its output.
- The omitted long matches in g6 and g9 (archive lines 40, 100, 103, 106, 121) were not opened one by one. g9 hits are incidental substrings (e.g. `calibration`, `widening`), none concern a «light» factory.
- P1–P15 have no individual owner dates in these files; D-0009 gives only a collective date, 29.09.2026. Their per-word dates sit in files outside the given set.
- Files beyond the 11 given (`docs/OWNER_PRINCIPLES_INDEX.md`, `docs/tasks/specs/...`, `design/factory-rules.md`, `design/architecture.md`) were not opened.
- Reading stayed far below the 220K token stop; nothing is left unread.
- The Objects table uses `owner` for the dated word, so some cells hold Russian quotes. The A lines of the DoD (statement, path, word, craft or process, outcome or means or knowledge) are spread over the columns gist, paths, owner, kind.
