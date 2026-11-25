<!-- scout hand-back, journal task t-1909, recon for docs/tasks/specs/20261125-forge2-light-factory-plan.md; saved verbatim from the worker's final message -->

digest: v1 t-forge2-recon3-b11-b22

Scope. V11-V22 only (В with Cyrillic В). Root C:\QAFactory\forge-repo, P = ai-packages/qa-factory/. Branch-row columns: `owner` holds the owner's word with date or `—`, `gist` holds what the current factory does (or `nothing`), `links` holds node ids or `file:line`, and the narrow open question is in "Forks / Open" below, keyed by the same id. An owner's word counts only where the text marks it as hers. Rule text without that mark is in `gist`. Money figures: none copied.

## Objects
| id | kind | gist | paths | status | owner | links | ev |
|---|---|---|---|---|---|---|---|
| q11a | branch working framework | Onboarding infers conventions from real test files; automator ladder step 1: use the project's embodiment | P references/test-code-patterns.md:33-34; P skills/qa-onboarding/phases/p1-discovery.md:174-196 | present | — (D-0030 06.10.2026: where tests live is the project's word; no quote) | — | t3,t9 |
| q11b | branch stub or abandoned set | Onboarding runs one existing test per profile and proposes a cure only if it ran green; nothing else restores a dead set | P skills/qa-onboarding/phases/p4-generate.md:191-241 | present | — | experiments/ao3-wrapper/factory-vs-free-agent/runs/factory-out/at-s5-before-stop/LOCAL-1/state/driver-tmp/S2-qa-requirements-tester-1.system.md:416 (template stubs read as "no framework") | t3,t25 |
| q11c | branch no framework | Onboarding writes config.json only and says bootstrap is "planned for v1"; test-code-patterns rung 5 says factory builds one from scratch | P skills/qa-onboarding/phases/p4-generate.md:77-88; P references/test-code-patterns.md:45 | present | — | contradiction: the two carriers differ | t25,t9 |
| q12a | branch full or partial access | Scout decides every source; an unavailable source is shown and passes only on a person's accept-gap | P skills/qa-story/phases/s1.md:164,257-259,295 | present | «нет доступа — спросить человека с вариантами «не нужно / как получить / вот текст»» (P5, 01.10 и 13.10.2026) | SS1-1,SS1-10,SS1-13,SS1-14 | t5,t37 |
| q12b | branch person can grant access | Gate card offers "get me access, or tell me to go on without it" while something is still asked | P skills/qa-story/phases/s1.md:212,227 | present | same P5 quote | SS1-10 | t37 |
| q12c | branch unreachable by probe | Rule text: probe-proven unreachable source is a default gap and a named report line, no question; code not checked | docs/OWNER_PRINCIPLES.md:17-20 | rule-text-only | «недостижимое, установленное пробой самой фабрики … — пробел по умолчанию и строка отчёта по имени, без вопроса» (P5, 13.10.2026, D-0043/D-0047) | — | t5 |
| q13a | branch stand ready | Stand chosen explicitly, probed in three lines (liveness, login, keys); blocked area is marked blocked_by_env at once | P references/environments.md:28-36; docs/tasks/handoffs/20261125-forge2-recon-story-roles.md:65 | present | — | RH1-7,SS1-7,SS1-9 | t8,t1 |
| q13b | branch factory prepares | Authorized preparation of the chosen stand allowed, minimal update only; no app-code patches | P references/environments.md:18-26 | present | — | EP1-26 | t8 |
| q13c | branch only a person can prepare | ENV owner:user becomes a gate B item with a list of what is needed from whom; never silently worked around | P references/environments.md:83-95 | present | — | — | t8 |
| q13d | branch only another environment | Test is written, hand-over card says "run it where the prerequisite exists"; this covers the admin-on-stage example | P agents/qa-automator.md:41; P references/environments.md:51-52 | present | «тест пишется, человек прогоняет его на другой среде» (P19 п.5, 30.09.2026) | EP1-15 | t6,t11,t8 |
| q13e | branch remember environment | Accepted stand gap kept once in records/environment-properties.json; what the person taught about the stand is not saved to config | P references/environments.md:98-107 | present | «стенды накопятся постепенно … уточняем, на каком стенде тестить и можно ли его ломать» (10.11.2026, plan, not built) | SS1-11 | t8,t3,t16 |
| q14a | branch data ready | Onboarding asks four test-data questions (accounts and datasets, PII, cleanup, shared records); strategy recorded | P skills/qa-onboarding/phases/p2-interview.md:236-250; P references/environments.md:68-74 | present | — | TQ1-11 | t8,t3,t17 |
| q14b | branch factory creates data | Automator: own data, unique per run, cleaned up, project's fixtures/factories/admin API; run-unique tag where no cleanup | P agents/qa-automator.md:54 | present | — | TQ1-6,EP1-34,TQ1-11 | t11,t17 |
| q14c | branch complex state history | No dedicated rule; nearest: strategist rows for undo, leftovers, "what a walk changes" | P agents/qa-test-strategist.md:41-43,65 | absent | — | FV3-5,FV3-17,FV3-33 (dry-world seeds, factory's own test world) | t10,t36,t38 |
| q14d | branch data from a person | Human-prepared data is a recorded strategy; role without account is a question; accounts kept as roster by role (plan) | P references/environments.md:70-72; plans/project-knowledge-plan.md:33 | present | «эти данные тоже надо накапливать … 4 роли. Тогда при составлении тест-плана это надо учесть» (10.11.2026, plan, not built) | — | t8,t3 |
| q14e | branch old data after migration | Only a strategist hint "records written before the change meet the new code" and migration as automation signal; no step | P agents/qa-test-strategist.md:39; P references/automation-candidacy.md:41 | present | — | — | t10,t12,t26 |
| q15a | branch one configuration | Default; no matrix is built | — | present | — | — | t10 |
| q15b | branch several browsers, platforms, locales, tariffs | Strategist: pairwise, "name the pairs you left out"; no list of supported browsers/locales exists; onboarding asks mobile platforms only | P agents/qa-test-strategist.md:58; P skills/qa-onboarding/phases/p2-interview.md:218-227 | present | «варианты мобильных девайсов … операционные системы, языки» (10.11.2026, plan, growable lists, not built) | — | t10,t28,t3 |
| q15c | branch functionality behind a flag | Strategist: "each switch doubles the paths"; scout records flags/locale/tenant as requirements; precondition kind feature_flag | P agents/qa-test-strategist.md:40; P agents/qa-scout.md:39,41; P references/artifact-contract.md:84 | present | — | — | t10,t25 |
| q16a | branch partner test system available | Integration readiness scoped per obligation: env_probe reads credential_alternatives and declared prerequisites with owners | P references/environments.md:31-33,109-119 | present | — | — | t8 |
| q16b | branch emulator only | Each test declares per side real, substituted or absent; a mock lives in the project's mock place with a qa-provisional marker | P agents/qa-automator.md:56; P agents/qa-code-critic.md:40,62 | present | — | — | t11,t27 |
| q16c | branch own side of contract only | "A green on a mock proves the mock"; Then must name every side it speaks about | P agents/qa-code-critic.md:40 | present | «проверять интеграцию когда ответ отрицательный вообще невозможно. Очень большой баг автотестов» (29.10.2026) | TQ1-18 | t22,t27 |
| q16d | branch integration unavailable | Becomes blocked_by_env with remedy, or a recorded environment property "on this environment X cannot be checked" | P references/environments.md:40-56,100-104 | present | — | — | t8 |
| q17a | branch default principles | Four inputs to automate plus ladder; automate what runs many times and what is red; never by priority alone | P references/automation-candidacy.md:29-51; P agents/qa-test-strategist.md:55 | present | «Автоматизируется то, что будет гоняться много раз, и то, что красное.» (P28, 04.11.2026) | — | t7,t12,t10 |
| q17b | branch project changes them | Project DoD answer from onboarding is input 1; framework-rules.md carries project rules; plan key automation.selection (always/never) | P references/automation-candidacy.md:34-37; plans/project-knowledge-plan.md:122,309-313 | partly-built | «Оба — да; первый превращается в ключ `automation.selection`» (10.11.2026, plan B6 reply) | — | t12,t3 |
| q18a | branch automate with no manual pass | Strategist plans from register and diff; first look is optional; automator may look at the stand itself when selectors are missing | P skills/qa-story/phases/s3.md:12; P agents/qa-automator.md:55 | present | «он может сам посмотреть на стенд» (13.11.2026, live-run-fvf finding) | FV1-5 | t34,t11,t20 |
| q18b | branch one manual pass for recon | First look: one walk per requirement before the plan, evidence not oracle; one-off checks walked by agent by hand | P agents/qa-test-strategist.md:55-56; P skills/qa-story/phases/s3.md:40; docs/OWNER_PRINCIPLES.md:138-142 | present | «Место прохода — между S2 и S3 … Один проход — четыре читателя» (10.11.2026); «у нас есть "первый взгляд" это как раз то же что делал агент должно быть» (13.11.2026) | FV1-5,FV1-15,FV1-28 | t19,t20 |
| q19a | branch level choice | Lowest rung that observes it; strategist picks level, automator HOW; critic judges level; closed five levels | P agents/qa-test-strategist.md:57; P agents/qa-automator.md:48; docs/OWNER_PRINCIPLES.md:36-47,58-64 | present | «e2e-кейсов как можно меньше»; «Кейс говорит, ЧТО проверить; автоматор решает, КАК» (P16/P17, 30.09 и 04.11.2026) | TQ1-3,TQ1-17 | t6,t10,t11 |
| q19b | branch parametrised | Same setup and action is one parametrised test, parameter id names the case | P agents/qa-automator.md:50 | present | «ввод −1, 0, 1.5, «абв» … — ОДИН тест с параметрами» (P16, 04.11.2026) | — | t6,t11 |
| q19c | branch soft assert or stop at first red | Non-stopping form where the framework has one; else move independent Thens before the red one | P agents/qa-automator.md:62,73 | present | «Независимые не останавливают друг друга: одно падение не прячет остальные.» (P29, 06.11.2026) | HF6-1,HF2-3,TQ1-14 | t7,t11,t18 |
| q19d | branch mixed result in one test | Ledger, report and S9 verdict tell outcomes per Then and partition; Then the red stops is blocked_by_check; S5 gate once refused partial-green | P agents/qa-automator.md:73; plans/piles/gates-and-words/findings/20261024-smeshannye-iskhody-v-odnom-keyse.md:12-13 | present | «… в одном кейсе есть и отданная человеку, и проходящая, и упавшая (из-за кода), и заблокированная проверки?» (24.10.2026) | HF2-3,GW1-22 | t18,t11 |
| q19e | branch stopped in preparation | Run outcome closed list includes env_blocked and broken_run; per-Then reporting of unreached Thens not seen | P references/environments.md:58-66 | present | — | — | t8 |
| q20a | branch update existing test (step or assert) | Embedding ladder: reuse, else extend assertion/parameters, else new; automator searches the old test first | P references/automation-candidacy.md:67-80; P agents/qa-automator.md:49 | present | «дополняет старые тесты, параметризует, объединяет проверки» (P17, 30.09.2026) | TQ1-21,TQ1-19,TQ1-26 | t7,t12,t11 |
| q20b | branch change or retire existing case and test | Gate A proposes adapt, migrate or retire with pins; a removed component alone never authorizes deleting a test | P references/case-lifecycle.md:54-56; P agents/qa-automator.md:43 | present | — | EP1-15 | t24,t11 |
| q21a | branch isolated | Own data per run, wait for events not time, find by role/label | P agents/qa-automator.md:33-34,53-54,58 | present | — | TQ1-6,EP1-34 | t11 |
| q21b | branch shared data | Shared records only if project declared; strategist plans "shared mutable state" and un-resettable data | P agents/qa-test-strategist.md:35,42; P references/environments.md:72-74 | present | — | TQ1-11 | t10,t8 |
| q21c | branch order matters | Split independent from sequential checks; sequential only where dependent | docs/OWNER_PRINCIPLES.md:143-146 | present | «Последовательные — только зависимые друг от друга.» (P29, 06.11.2026) | — | t7 |
| q21d | branch several users at once | Strategist row "double submit, two tabs, a retry"; no rule on writing concurrency tests, no cleanup/parallel split | P agents/qa-test-strategist.md:37; P agents/qa-failure-analyst.md:34 | present | «У нас стенд один (слово владельца): параллельно только кейсы с независимыми данными по полю плана» (driver-hosts finding, SC5-5) | SC5-5,SC5-1 | t10,t27,t16 |
| q22a | branch exploratory in story | Strategist plans time-boxed charters; runner explores at S6 with a perturbation matrix and a tried.md table | P agents/qa-test-strategist.md:62; P references/explore-charter.md:11-60; P references/perturbations.json:4-33 | present | «чтобы при запуске этого скилла фабрика нашла как минимум эти 3 бага» (31.10.2026); Playwright allowed for the S6 charter, every step through the recorder (P26, 04.11.2026) | XT2-2,EP1-41 | t13,t15,t6 |
| q22b | branch stand-alone qa-explore skill | Scripts exist (exploration.py, explore_step.py, references/exploration.json); skills/qa-explore folder does not | P scripts/exploration.py:1; P scripts/explore_step.py:1 | contradictory | «Слово владельца на открытие кучки: 31.10.2026, «да»» (exploratory README) | XT1-1..XT2-2,XT3-1,RN1-6 | t14,t30,t32 |
| q22c | branch charter mechanism | Hypothesis, oracle and refuting observation written before each capture; "nothing broke" needs the tried table; charter-form.md is about role charters, a homonym | P references/explore-charter.md:20-31; P references/charter-form.md:1-49 | present | — | — | t13,t4 |
| q99 | analog | Same carrier-contradiction class: "S3 critic yes/no" and "S3 stops at gate A" differ across README, SKILL, role file | docs/tasks/handoffs/20261125-forge2-recon-story-roles.md:229-231 | present | — | D1,D2 | t1 |

## Trail
| tid | op | target | pattern / range | flags | result | control |
|---|---|---|---|---|---|---|
| t1 | read | docs/tasks/handoffs/20261125-forge2-recon-story-roles.md | 1-250 | — | read docs/tasks/handoffs/20261125-forge2-recon-story-roles.md:1-250 | — |
| t2 | read | docs/tasks/handoffs/20261125-forge2-recon-owner-words.md | 1-162 | — | read docs/tasks/handoffs/20261125-forge2-recon-owner-words.md:1-162 | — |
| t3 | read | docs/tasks/handoffs/20261125-forge2-recon-onboarding-knowledge.md | 1-113 | — | read docs/tasks/handoffs/20261125-forge2-recon-onboarding-knowledge.md:1-113 | — |
| t4 | read | docs/tasks/handoffs/20261125-forge2-recon-references.md | 1-152 | — | read docs/tasks/handoffs/20261125-forge2-recon-references.md:1-152 | — |
| t5 | read | docs/OWNER_PRINCIPLES.md | 12-21 | — | read docs/OWNER_PRINCIPLES.md:12-21 | — |
| t6 | read | docs/OWNER_PRINCIPLES.md | 34-73 | — | read docs/OWNER_PRINCIPLES.md:34-73 | — |
| t7 | read | docs/OWNER_PRINCIPLES.md | 96-153 | — | read docs/OWNER_PRINCIPLES.md:96-153 | — |
| t8 | read | ai-packages/qa-factory/references/environments.md | 1-120 | — | read ai-packages/qa-factory/references/environments.md:1-120 | — |
| t9 | read | ai-packages/qa-factory/references/test-code-patterns.md | 25-85 | — | read ai-packages/qa-factory/references/test-code-patterns.md:25-85 | — |
| t10 | read | ai-packages/qa-factory/agents/qa-test-strategist.md | 1-90 | — | read ai-packages/qa-factory/agents/qa-test-strategist.md:1-90 | — |
| t11 | read | ai-packages/qa-factory/agents/qa-automator.md | 1-89 | — | read ai-packages/qa-factory/agents/qa-automator.md:1-89 | — |
| t12 | read | ai-packages/qa-factory/references/automation-candidacy.md | 1-91 | — | read ai-packages/qa-factory/references/automation-candidacy.md:1-91 | — |
| t13 | read | ai-packages/qa-factory/references/explore-charter.md | 1-75 | — | read ai-packages/qa-factory/references/explore-charter.md:1-75 | — |
| t14 | read | plans/piles/exploratory/README.md | 1-71 | — | read plans/piles/exploratory/README.md:1-71 | — |
| t15 | read | plans/piles/exploratory/batch-2-charters-and-exploration.md | 1-45 | — | read plans/piles/exploratory/batch-2-charters-and-exploration.md:1-45 | — |
| t16 | read | plans/piles/stand-and-sources/README.md | 1-110 | — | read plans/piles/stand-and-sources/README.md:1-110 | — |
| t17 | read | plans/piles/test-code-quality/README.md | 1-102 | — | read plans/piles/test-code-quality/README.md:1-102 | — |
| t18 | read | plans/piles/gates-and-words/findings/20261024-smeshannye-iskhody-v-odnom-keyse.md | 1-40 | — | read plans/piles/gates-and-words/findings/20261024-smeshannye-iskhody-v-odnom-keyse.md:1-40 | — |
| t19 | read | plans/piles/pre-code/findings/20261110-pervyj-vzglyad-mezhdu-s2-i-s3.md | 1-22 | — | read plans/piles/pre-code/findings/20261110-pervyj-vzglyad-mezhdu-s2-i-s3.md:1-22 | — |
| t20 | read | plans/piles/live-run-fvf/findings/20261113-pervyj-vzglyad-ne-dohodit-do-avtomatora.md | 18-27 | — | read plans/piles/live-run-fvf/findings/20261113-pervyj-vzglyad-ne-dohodit-do-avtomatora.md:18-27 | — |
| t21 | read | plans/piles/live-run-fvf/findings/20261113-avtomatoru-ne-dan-hodok-po-stendu.md | 20-30 | — | read plans/piles/live-run-fvf/findings/20261113-avtomatoru-ne-dan-hodok-po-stendu.md:20-30 | — |
| t22 | read | plans/piles/test-code-quality/findings/20261029-orakul-kak-do-na-otricatelnom-otvete.md | 1-18 | — | read plans/piles/test-code-quality/findings/20261029-orakul-kak-do-na-otricatelnom-otvete.md:1-18 | — |
| t23 | read | ai-packages/qa-factory/agents/qa-runner.md | 10-49 | — | read ai-packages/qa-factory/agents/qa-runner.md:10-49 | — |
| t24 | read | ai-packages/qa-factory/references/case-lifecycle.md | 36-62 | — | read ai-packages/qa-factory/references/case-lifecycle.md:36-62 | — |
| t25 | grep | ai-packages/qa-factory | `no framework\|without a framework\|bootstrap\|abandoned\|scaffold\|no test (framework\|repo\|suite)\|greenfield` | -i content glob=*.md | found 25; skills/qa-onboarding/phases/p4-generate.md:77-86, references/test-code-patterns.md:45 | — |
| t26 | grep | ai-packages/qa-factory/agents | `migrat\|old data` | -i content | found 2; agents/qa-scout.md:57, agents/qa-test-strategist.md:39 | — |
| t27 | grep | ai-packages/qa-factory/agents | `partner\|third.party\|emulator\|stub\|sandbox\|contract test\|mock\|external integration\|external service` | -i content | found 11; agents/qa-automator.md:36,56, agents/qa-code-critic.md:40,62 | — |
| t28 | grep | ai-packages/qa-factory/skills | `cross-browser\|locale\|tariff\|supported (browser\|platform\|configuration)\|configuration matrix\|browser matrix` | -i content glob=*.md | absent | t29 |
| t29 | grep | ai-packages/qa-factory/skills | `mobile_surface\|integrations` | -i count glob=*.md | count 13 | — |
| t30 | glob | ai-packages/qa-factory/skills | `qa-explore/**` | — | absent | t31 |
| t31 | glob | ai-packages/qa-factory/skills | `qa-story/**` | — | found 13; skills/qa-story/SKILL.md, phases/s0.md..s9.md | — |
| t32 | grep | ai-packages/qa-factory | `qa-explore` | -i files | found 7; scripts/exploration.py, scripts/explore_step.py, scripts/stage_guard.py, references/exploration.json | — |
| t33 | grep | ai-packages/qa-factory/skills/qa-story/phases/s3.md | `integration\|partner\|third-party\|external service` | -i content | absent | t34 |
| t34 | grep | ai-packages/qa-factory/skills/qa-story/phases/s3.md | `First look` | -i content | found 3; s3.md:12,18,40 | — |
| t35 | grep | ai-packages/qa-factory/skills/qa-story/phases/s1.md | `unavailable\|accept.gap\|unreachable\|no access\|cannot (read\|open)` | -i content | found 12; s1.md:34,164,212,227,257-259,295 | — |
| t36 | grep | docs/tasks/handoffs | `flak\|framework\|bootstrap\|staging\|test data\|fixture\|matrix\|stub\|emulator\|partner\|soft assert\|isolation\|concurren\|existing test\|extend` | -i content glob=20261125-forge2-recon-nodes-g*.md | found 28; g4:113-124 (TQ1-6, TQ1-11, EP1-15, HF6-1, TQ1-21), g5:32-47, g8:52-66 | — |
| t37 | read | ai-packages/qa-factory/skills/qa-story/phases/s1.md | via t35 lines only | — | read ai-packages/qa-factory/skills/qa-story/phases/s1.md:34,164,212,227,257-259 | — |
| t38 | grep | ai-packages/qa-factory/agents | `state history\|complex state\|history of states\|long history\|seed(ed)? (data\|history)` | -i content | absent | t26 |

## Forks
Settled, carry over without asking (rule text unless marked her word):
- S1. Ladder bottom-up, five rungs incl. "write it, a person runs it on another environment" (her word P19, 30.09.2026) — covers the admin-on-stage example in V13.
- S2. Automate what runs many times and what is red; one-off new-feature checks are walked by the agent by hand; strategist decides per plan row (her word P28, 04.11.2026).
- S3. Pyramid, merge by parameters when the red line names case and branch; a case says WHAT, automator says HOW; many-to-many (her word P16/P17).
- S4. Independent checks never hide each other; sequential only where dependent (her word P29, 06.11.2026); mixed per-Then results in one case must be representable (her word 24.10.2026).
- S5. Source access: ask only what a person can grant, probe-proven unreachable is a named gap with no question (her word P5, 01.10/13.10.2026).
- S6. Exploratory: must find the three MyBooks cart bugs; any project, not only browser (her word 31.10.2026); MCP Playwright only through the recorder (her word P26, 04.11.2026).
- S7. First look exists, sits between S2 and S3, one pass for four readers; automator may look at the stand itself when selectors are missing (her words 10.11.2026 and 13.11.2026).
- S8. Project can extend automation principles through a key automation.selection and a DoD answer (her word 10.11.2026, plan only, code absent).
- S9. Stands accumulate across stories and users as a roster of roles; lists (devices, OS, languages) grow without a package edit (her words 10.11.2026, plan only).
- S10. Integration check on a negative base is "impossible" and a major autotest bug (her word 29.10.2026, TQ1-18).
- S11. Single stand: parallel only cases with independent data by plan field (marked "слово владельца" inside a finding row, driver-hosts/findings/20261030-chuzhie-fabriki-stlc-i-tcc-rychagi-skorosti-dlya-0-11-0.md:23).

Open, narrowest question per branch:
- q11a no owner word found; q11b: when a stub or abandoned test set is found, restore it, extend it, or start a new base beside it?
- q11c: does the new factory build a framework from scratch itself (test-code-patterns.md:45 says yes, onboarding says "planned for v1") or stop and hand over?
- q12c: is "unreachable by probe, no question" implemented or only written? (not checked in code)
- q13b/q13c: may the factory bring a stand up unasked in any case (current rule: only the selected stand, with authorization)?
- q14c: is there a rule for data that needs a long state history, or does it go to the person?
- q14e: should a check on pre-migration data be a mandatory plan row when a migration is in the diff?
- q15b/q15c: who supplies the list of supported browsers, platforms, locales, tariffs: onboarding question or first need? Where do unchecked configurations appear in the report?
- q16a-d: does each integration branch get its own stated proof boundary in the report?
- q17b: is automation.selection asked at onboarding or at first need (plan says "решает владелец")?
- q18a/q18b: is the first look mandatory or optional (s3.md:12 says optional)? Her question 12.11.2026 "что такое S2 по замыслу: «первый взгляд, смоук» или «реестр требований и размер»" has no recorded answer in what I read.
- q19e: how is a test stopped in preparation reported per Then?
- q20b: when a requirement changes in a re-run, is an existing test updated or a new one added beside it?
- q21d: should the factory write concurrency tests, and with which cleanup/parallel rule?
- q22b: is there a stand-alone exploration skill now? Carriers disagree (exploratory/README.md:25-26 "закрыта" with MR; release-next/README.md:18 "не начата: нет scripts/exploration.py"; release-next/README.md:24 pack 1 closed with "исследовательский прогон"; scripts exist, skill folder absent).
- Two carriers contradict (not resolved): q11c (p4-generate.md:82 "planned for v1" vs test-code-patterns.md:45 rung 5 "builds from scratch"); q22b (above); q19d (finding 24.10 says "no carrier" for assert order/soft asserts, automator.md:62,73 now carries it).
this needs a decision from a tier above.

## Not done
- Maps role-slices.md and package-design.md were not read (only a count grep on role-slices); facts from them are not used.
- design/architecture.md, design/factory-rules.md, qa-onboarding p0-p4 bodies (used through the onboarding map, t3) and qa-story s0-s9 bodies (through the story-roles map, t1; only s1/s3 greps run directly) were not read in full.
- plans/exploratory-charters-proposal.md: the file was not found by a Glob (no control run), so the "Уточнения владельца 31.10" text itself is unread.
- Node digests were searched by word (t36), not read through; "nodes" cells hold ids that those lines and the three pile READMEs name. Node ids for V11, V15 and V17 were not found (t36 control: same grep found rows for flaky/fixture/extend; not a separate negative per word).
- Control t29 uses the `count` flag while t28 uses content, so its shape differs; treat q15b "no browser/locale list in skills" as weakly controlled. The earlier brace-glob calls (matched nothing) were discarded and are not in the Trail.
- Findings files under plans/piles were used only where they carry her quoted word (t16-t22), against the non-goal on history; each is marked.
- Dates for P-items come from OWNER_PRINCIPLES lines; D-0030 (06.10.2026) is cited through the owner-words map only, no quote.
