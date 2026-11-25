<!-- scout hand-back, journal task t-1912, recon for docs/tasks/specs/20261125-forge2-light-factory-plan.md; saved verbatim from the worker's final message -->

digest: v1 t-docs-for-person
Пути относительно C:\QAFactory\forge-repo\ai-packages\qa-factory\ (сокращение P/). Шаблоны: P/references/templates/ (T/). Скрипты: P/scripts/. Формат: ключ v1 + Objects/Trail, затем блоки a-f по просьбе диспетчера (раздел "Details" ниже Not done; вне grammar v1, флаг unknown_section ожидаем). Денег в тексте нет.

## Objects
| id | kind | gist | paths | status | owner | links | ev |
|---|---|---|---|---|---|---|---|
| d1 | doc | understanding.md: 6 секций в шаблоне, валидатор требует 5, лимит 40 строк, содержит список R-n | T/understanding.md:1-48 | present | — | d1v | r1,g16 |
| d1v | validator | check_understanding: лимит 40 строк, 5 секций, каждый R-n в verify или not verify | P/scripts/validate_artifacts.py:1767-1772,1950-1972 | present | — | d1 | r13 |
| d2 | doc | test-plan.md: отдельного шаблона нет, контракт в artifact-contract-plan.md; таблица ## Plan из 12 колонок | P/references/artifact-contract-plan.md:38-96 | present | — | d2n | r2,g6 |
| d2n | doc | шаблон test-plan в templates/ отсутствует; рядом есть plan-brief.md (<=15 строк) | P/references/templates/ | absent | — | d2 | g32,g33 |
| d3 | doc | test-report.md: шаблон с фактовыми блоками code-owned, 6144 байт на авторский текст | T/test-report.md:1-194 | present | — | d3v | r3,g17 |
| d3v | validator | check_test_report: порядок секций, трассируемость, Left with you, запрещённые формы, блоки; report_facts --check | P/scripts/validate_artifacts.py:1120-1156,1407-1420 | present | — | d3 | r13,r14 |
| d4 | doc | отчёта ручных проходов отдельного файла нет: блок Checked by hand в test-report + список скриншотов в пакете gate B | T/test-report.md:58-69; P/scripts/report_facts.py:1322-1364 | present | owner 24.11.2026, 31.10.2026 | d3 | r3,r12 |
| d5 | doc | retro.md: 6 секций, первые 3-5 строк "что пошло не так", числа считает код | T/retro.md:1-60 | present | owner 30.09 (деньги в ретро) | d5v | r4,g20 |
| d5v | validator | на retro.md нет проверки заголовков в validate_artifacts; есть required_outputs (файл существует) и аудиты A15/A21 | P/skills/qa-story/phases/s9.md:3-9; P/scripts/validate_artifacts.py:157 | present | — | d5 | r8,g20 |
| d6 | list | прочие документы человеку: см. блок (6) | — | present | — | — | r5,r6,r7 |
| d7 | rule | общее правило текста человеку: human-questions.md + human_text.py (FR-6) | P/references/human-questions.md:1-160; P/design/factory-rules.md:135-144 | present | — | d1,d3,d5 | r9,r10 |
| d8 | rule | язык: всё пишется по-английски независимо от языка тикета | P/references/common-rules.md:148-151 | present | — | d7 | r11 |

## Trail
| tid | op | target | pattern / range | flags | result | control |
|---|---|---|---|---|---|---|
| g1 | glob | C:\QAFactory\forge-repo | `ai-packages/qa-factory/**/*` | files | found 100 | — |
| g2 | glob | C:\QAFactory\forge-repo | `ai-packages/qa-factory/references/templates/*` | files | found 11 | — |
| g3 | glob | C:\QAFactory\forge-repo | `ai-packages/qa-factory/skills/*/SKILL.md` | files | found 4 | — |
| g4 | glob | C:\QAFactory\forge-repo | `ai-packages/qa-factory/scripts/*{understanding,plan,report,retro,render,brief,human,gate,question,manual,walk}*` | files | found 27 | — |
| g5 | grep | P/scripts/gate_brief.py | `GATE_A_DOCUMENTS\|GATE_B_DOCUMENTS\|^GATE_` | -i content | found 7; gate_brief.py:1920 | — |
| g6 | grep | P/references/artifact-contract-plan.md | `^#{1,3} ` | content | found 7; artifact-contract-plan.md:38 | — |
| g7 | grep | P/ (md,yaml) | `test-plan\.md` | -i files glob=*.{md,yaml} | found 40 | — |
| g8 | grep | P/ (py,md) | `the owner'?s word\|owner's word\|слово владельца\|owner said\|owner wrote` | -i content glob=*.{py,md} | found 60; gate_brief.py:1917, grammar.py:246 | — |
| g9 | grep | P/skills/qa-story/phases/s4.md | `^#{1,3} ` | content | found 3 | — |
| g10 | grep | P/skills/qa-story/phases/s9.md | `^#{1,3} ` | content | found 10 | — |
| g11 | grep | P/skills/qa-story/phases/s8.md | `^#{1,3} ` | content | found 11 | — |
| g12 | grep | P/scripts/gate_brief.py | `"## [A-Z][^"]*"\|'## [A-Z][^']*'\|f"## ` | content | found 29; gate_brief.py:3186 | — |
| g13 | grep | docs/PROJECT_FULL.md | `understanding\|test-plan\|test plan\|test report\|test-report\|retro\|screenshot\|скриншот\|понимани\|ретро\|отчёт\|отчет` | -i content | found 10; PROJECT_FULL.md:109-117 | — |
| g14 | grep | plans/piles | `понимани\|скриншот\|тест-план\|план тест\|ретро\|отчёт о тест\|отчет о тест\|understanding\|screenshot` | -i content | found 50; piles/execution-probes/findings/20261124-...md:3 | — |
| g15 | grep | docs/OWNER_PRINCIPLES.md | `understanding\|test plan\|test-plan\|test report\|retro\|screenshot\|скриншот\|понимани\|ретро\|отчёт\|отчет\|план тест` | -i content | found 5; OWNER_PRINCIPLES.md:55,71,75-77 | — |
| g16 | grep | P/scripts/validate_artifacts.py | `understanding\|retro\|test-report\|test-plan\|MAX_LINES\|line cap\|40 lines\|≤ ?40` | -i content | found 27; validate_artifacts.py:1767 | — |
| g17 | grep | P/scripts | `^(REPORT_SECTIONS\|REPORT_BLOCKS\|REPORT_[A-Z_]+\|RETRO_[A-Z_]+)\b.*=` | content glob=*.py | found 32; grammar.py:114 | — |
| g18 | grep | P/scripts | `^def (check_report\|check_retro\|check_test_report\|check_.*retro\|check_.*report)\w*` | content glob=*.py | found 19; validate_artifacts.py:1120 | — |
| g19 | grep | P/scripts | `TEST_REPORT_MAX_BYTES\|What went wrong, and what to do\|what went wrong` | -i content glob=*.py | found 8; validate_artifacts.py:1768 | — |
| g20 | grep | P/scripts | `retro\.md` | content glob={validate_artifacts,exit_gate,stage_done,retro_numbers,controller,grammar}.py | found 11; retro_numbers.py:3025 | — |
| g21 | grep | P/design/factory-rules.md | `^#{1,3} .*(B\b\|text shown\|person\|human)\|^## B` | -i content | found 1; factory-rules.md:133 | — |
| g22 | grep | P/agents/qa-retro-analyst.md | `retro\|Retro` | content | found 15; qa-retro-analyst.md:22 | — |
| g23 | grep | P/scripts/exit_gate.py | `retro\|exit_gate\|RETRO_HEADINGS\|required_outputs` | -i content | found 20; exit_gate.py:926 | — |
| g24 | grep | docs/tasks/handoffs/20261125-forge2-recon-story-roles.md | `understanding\|retro\|screenshot\|test report\|test plan\|owner` | -i content | found 40; story-roles.md:11 | — |
| g25 | grep | docs/tasks/handoffs/20261125-forge2-recon-questions-v23-v29.md | `understanding\|retro\|screenshot\|test report\|test plan\|requirements list` | -i content | found 8; questions-v23-v29.md:39 | — |
| g26 | grep | P/scripts/report_facts.py | `def screenshot_section\|## Screenshots of the manual checks\|def screenshot_groups` | content | found 3; report_facts.py:1322 | — |
| g27 | grep | P/references/manual-evidence.md | `^#{1,3} ` | content | found 2 | — |
| g28 | grep | P/scripts/gate_brief.py | `def _head_lines\|def _after_approval\|def _tail_sections` | content | found 3; gate_brief.py:3095 | — |
| g29 | grep | P/skills/qa-story/phases/s2.md | `understanding\.md\|interim-report\|blocked.*brief\|brief.*alone` | -i content | found 5; s2.md:85 | — |
| g30 | grep | P/skills/qa-story/phases/s1.md | `interim-report\.md\|source review\|## .*(person\|human)` | -i content | found 7; s1.md:182 | — |
| g31 | grep | P/CHANGELOG.md | `gate-a-message\|the owner's word of 22\.10\|variant \(a\)\|size limits\|40 lines\|one screen` | -i content | found 1; CHANGELOG.md:783 | — |
| g32 | glob | C:\QAFactory\forge-repo | `ai-packages/qa-factory/references/templates/test-plan*` | files | absent | g33 |
| g33 | glob | C:\QAFactory\forge-repo | `ai-packages/qa-factory/references/templates/*plan*` | files | found 1; templates/plan-brief.md | — |
| g34 | grep | P/agents/qa-doc-scribe.md | `report\|plain\|words\|jargon` | -i content | found 17; qa-doc-scribe.md:15 | — |
| r1 | read | T/understanding.md | whole | — | read T/understanding.md:1-48 | — |
| r2 | read | P/references/artifact-contract-plan.md | 1-112 | — | read P/references/artifact-contract-plan.md:1-112 | — |
| r3 | read | T/test-report.md | whole | — | read T/test-report.md:1-194 | — |
| r4 | read | T/retro.md | whole | — | read T/retro.md:1-60 | — |
| r5 | read | T/plan-brief.md | whole | — | read T/plan-brief.md:1-32 | — |
| r6 | read | T/questions-for-owner.md | whole | — | read T/questions-for-owner.md:1-65 | — |
| r7 | read | P/skills/qa-story/phases/s3.md | whole | — | read P/skills/qa-story/phases/s3.md:1-189 | — |
| r8 | read | P/skills/qa-story/phases/s9.md | 1-230 | — | read P/skills/qa-story/phases/s9.md:1-230 | — |
| r9 | read | P/references/human-questions.md | whole | — | read P/references/human-questions.md:1-160 | — |
| r10 | read | P/design/factory-rules.md | 133-192 | — | read P/design/factory-rules.md:133-192 | — |
| r11 | read | P/references/common-rules.md | 144-153 | — | read P/references/common-rules.md:144-153 | — |
| r12 | read | P/skills/qa-story/phases/s8.md | 37-262 | — | read P/skills/qa-story/phases/s8.md:37-262 | — |
| r13 | read | P/scripts/validate_artifacts.py | 1120-1180,1405-1455,1760-1990 | — | read P/scripts/validate_artifacts.py:1120-1990 | — |
| r14 | read | P/scripts/grammar.py | 80-298 | — | read P/scripts/grammar.py:80-298 | — |
| r15 | read | P/scripts/gate_brief.py | 55-84,1900-2029,3095-3194,3348-3402,4028-4227,5110-5206 | — | read P/scripts/gate_brief.py:55-5206 (ranges) | — |
| r16 | read | P/skills/qa-story/phases/s4.md | 25-164 | — | read P/skills/qa-story/phases/s4.md:25-164 | — |
| r17 | read | P/skills/qa-story/phases/s2.md | 80-130 | — | read P/skills/qa-story/phases/s2.md:80-130 | — |
| r18 | read | P/skills/qa-story/phases/s1.md | 182-211 | — | read P/skills/qa-story/phases/s1.md:182-211 | — |
| r19 | read | P/references/manual-evidence.md | whole | — | read P/references/manual-evidence.md:1-126 | — |
| r20 | read | plans/piles/execution-probes/findings/20261124-keys-bez-drayvera-vypolneno-agentom-s-dokazatelstvami.md | whole | — | read plans/piles/execution-probes/findings/20261124-keys-bez-drayvera-vypolneno-agentom-s-dokazatelstvami.md:1-73 | — |
| r21 | read | P/scripts/retro_numbers.py | 1380-1391,2660-2680 | — | read P/scripts/retro_numbers.py:1380-2680 (ranges) | — |
| r22 | read | docs/OWNER_PRINCIPLES.md | 50-81 | — | read docs/OWNER_PRINCIPLES.md:50-81 | — |
| r23 | read | docs/tasks/handoffs/20261125-forge2-recon-references.md | 1-150 | — | read docs/tasks/handoffs/20261125-forge2-recon-references.md:1-150 | — |
| r24 | read | P/scripts/report_facts.py | 1315-1384 | — | read P/scripts/report_facts.py:1315-1384 | — |

## Not done
- Слова владельца именно о структуре understanding.md, test-plan и retro (в частности «в понимании есть список требований») с датой я не нашёл в прочитанных носителях; поиск по docs/OWNER_PRINCIPLES.md, PROJECT_FULL.md и plans/piles шёл по словам выше (g13-g15), нулевой результат с контролем не получен, поэтому "нет" не утверждаю. Список требований в understanding есть по шаблону (T/understanding.md:25-28), это факт файла, не слова владельца.
- Не читал целиком: gate_brief.py (читал диапазоны), report_facts.py (только 1315-1384), human_text.py и human-text.json (названы по docs human-questions.md:134-150), traceability.py render, delivery_summary.py, ticket_adapter.py review, skills/qa-onboarding, qa-doctor, qa-collect SKILL.md (как документы человеку в (6) не проверены), агентские карточки кроме qa-retro-analyst и qa-doc-scribe (grep), CHANGELOG вокруг 783.
- Не проверял, где человек видит retro.md физически (S9 final summary называет путь, s9.md:221), и не искал, показывается ли test-plan.md через gate_brief документ-ссылкой (documents(), gate_brief.py:1938-1954: показывается путь).
- Сами тексты слов владельца в кодовых комментариях (22.10, 31.10, 03.10 и т. п.) — пересказ автора кода, не дословная цитата; дословные цитаты только в п. f ниже, где помечено.

## Details

### (1) understanding.md — файл понимания
a. Носители: шаблон T/understanding.md:1-48 (комментарий :3-10 — кто пишет, кому показывают); контракт P/references/artifact-contract-plan.md:29-35; фаза P/skills/qa-story/phases/s2.md:82-130 (halt blocked, размер); список «что человек одобряет» P/scripts/gate_brief.py:1915-1920 (GATE_A_DOCUMENTS = understanding.md + test-plan.md).
b. Секции шаблона по порядку (T/understanding.md:12-42, прочитано 1-48), заголовки дословно:
 1. `# <TICKET-ID> — understanding` (титул)
 2. `## Why this change` — одно-два предложения: что меняет тикет и для кого.
 3. `## Size` — одна строка из work/sizing.json (размер, функции, потолок тестов, бюджет, перебор, число непроверяемых), считает sizing.py, не руками.
 4. `## What we verify` — строки `- R-n — <одна строка проверяемого утверждения>` (это и есть список требований).
 5. `## What we do not verify, and why` — `- R-n — <причина: вне границ / покрыто / отложено>`.
 6. `## What else the change may touch` — 3-7 пунктов: смежные области/швы, не покрытые R.
 7. `## Questions without which testing is pointless` — только настоящие блокеры, `- Q1 — <одна строка; подробности в questions-for-owner.md>`.
 Расхождение: валидатор знает 5 секций (Why, What we verify, What we do not verify, What else, Questions) — P/scripts/validate_artifacts.py:1770-1771; `## Size` валидатор не требует.
c. Правила: <=40 строк (шаблон :3; validate_artifacts.py:1767; текст отказа :1954-1955 «the scope card is one screen; move detail into requirements-register.md»); каждый R из реестра обязан стоять в verify или not verify (:1960-1972); по строке на R, не весь текст требования; blocking Q должен существовать в матрице противоречий реестра (шаблон :6-8); язык — английский (common-rules.md:148-151); id-правила для текста человеку: human-questions.md:46-55 (row id вроде TS-14 объяснять при первом упоминании) — к этому файлу применимость как к «тексту человеку» не подтверждена проверкой human_text, см. ниже. Пустое/неизвестное значение: для Size в шаблоне формулировки нет; для вопросов «только блокеры, остальное — строка плана» (шаблон :44-46).
d. Пишет qa-requirements-tester на S2 (шаблон :3; artifact-contract-plan.md:32); размер считает сам роль через sizing.py (s2.md:121-127). Человек видит на gate A как один из двух документов к одобрению (gate_brief.py:1920, первая строка сообщения gate A: `**Approve: ...`, :1930-1935); при `verdict: blocked` — отдельно, до плана (третье касание человека), s2.md:82-103: строка путей, бриф <=40 строк, блокирующие вопросы с чтениями, фраза «There is no plan yet — it is built after these answers.»
e. Проверяет: validate_artifacts.py::check_understanding (:1950-1972) — отказывает при >40 строк, отсутствии любой из 5 секций, R без места; S2 exit detector (branch_accounting.py, повторный sizing.py, s2.md:121-129); case critic читает реестр на S4 (по story-roles digest, не перепроверял).
f. Слова владельца: дословной цитаты об этом файле не найдено (см. Not done). Косвенно: 22.10.2026, GW1-11 — вариант (a): человек одобряет ровно два документа, бриф — сводка (пересказ в комментарии gate_brief.py:1915-1917, не цитата).

### (2) test-plan.md — план тестов
a. Носители: отдельного шаблона нет (P/references/templates/ содержит plan-brief.md, но не test-plan*: g32 absent, контроль g33). Контракт: P/references/artifact-contract-plan.md:37-96; фаза P/skills/qa-story/phases/s3.md:1-189 (форма записи :149-152, 160-189); краткая версия: T/plan-brief.md:1-32.
b. Структура test-plan.md (artifact-contract-plan.md:40-71, прочитано 1-112): frontmatter `task, created, rows_total, candidates, planned` + счёт пирамиды; затем `## Plan` — таблица, колонки: `TS`, `what we verify`, `R`, `defect hypothesis`, `impact class`, `priority`, `observable`, `oracle`, `disposition + reason`, `fit`, `level`, `technique` (по строке на проверку; что в каждой — в таблице :44-57); затем `## Recommended regression` (`Command: ...`, пункты `- <path> (blast:B-n) - stand: ...`, `Developers: ...`, или `No regression: <reason>`). Дополнительно в файл встраиваются тексты кейсов через `render_case_appendix.py` (s4.md:108; «Case appendix», упомянут в test-report.md:34).
 Секции plan-brief.md (T/plan-brief.md:1-32, части gate A по шаблону): таблица `| Row | What we verify | What can break | How painful | Disposition + why | Fit |` (<=15 строк, иначе группировка с `+N more, see test-plan.md`) и `## Recommended regression` (`Command:`, пути, `Developers:`). Замечание: комментарий шаблона :4-5 называет бриф «part two of the gate-A message», а gate_brief.py:1915-1917 называет бриф сводкой, не документом к одобрению.
c. Правила: `|` внутри ячейки пишется `\|`, голый отказ (s3.md:152); диспозиции закрытый список automate · manual-agent · manual-human · skip · unverifiable (plan-brief.md:16-17); impact class закрытый список data-loss · money · access · blocked-flow · degraded · cosmetic · none; приоритет выводится, руками не ставится (plan-brief.md:18-22; contract :50); JSON-ключ `impact_class`, не `impact`; уровень unit · component · api · integration · e2e-ui, обязателен на automate, неизвестный — gap (contract :56); evidence_policy manual-agent строки — одно слово api|cli|no_write|static|ui (:67); у строки на открытом вопросе `if_answered` с ключом на каждое чтение + `not_needed` (:73-80); каждый R реестра получает строку (s3.md:141); план пишется частями (первые строки Write, остальные Edit, s3.md:132-139); автоматизация по «видимость/заголовок/URL/первая запись» запрещена (validate_artifacts.py:1930-1936); язык английский.
 Пустое/неизвестное: `fit` пустой вне automate; `Fit`/`—` в brief для не-automate; неизвестный уровень — gap; `oracle_unknown: true` вместо значения из кода (s3.md:125-127); нет регрессии — `No regression: <reason>`.
d. Пишет qa-test-strategist на S3 (в два окна при diff: разметка work/grounding.yaml, затем план; s3.md:63-65); case-critic проверяет после; человек видит на gate A как второй документ к одобрению (gate_brief.py:1920). Gate A message строится кодом (`write_gate_message`, gate_brief.py:3557), включает сводку «Plan — N rows…», пирамиду, число кейсов, вердикт критика.
e. Проверяет: validate_artifacts.py::check_plan_v0 (:1857-1945: пустая таблица, дубль TS, строка без R, класс гипотезы, диспозиция и причина, источник наблюдаемого, oracle-префикс, уровень, anti-pattern, new-behaviour с `history:`); planning_contract.validate_plan на work/test-plan.json в момент записи (s3.md:165-169); exit gate S3 (повтор того, что потребует controller gate-inputs, s3.md:181-189); branch_accounting.py (ветви, кандидаты); gate_preflight.py --gate A (репетиция, s4.md:132+).
f. Слова владельца: дословно об этом документе не найдено. P19 (30.09) о лестнице проверки — OWNER_PRINCIPLES.md:58-64 (русский): «(3) автоматизировать нельзя или не нужно (кейс не входит в регрессию) — агент проверяет вручную и показывает человеку «было / стало»».

### (3) test-report.md — отчёт о тестировании
a. Носители: шаблон T/test-report.md:1-194; константы P/scripts/grammar.py:92-298; валидатор P/scripts/validate_artifacts.py:1120-1156; фаза P/skills/qa-story/phases/s8.md:57-87, s9.md:154-198; карточка роли P/agents/qa-doc-scribe.md.
b. Секции шаблона в порядке (T/test-report.md:18-194, прочитано 1-194), заголовки дословно; [code] = блок между `facts:` маркерами, пишет `report_facts.py`:
 1. `# <TICKET-ID> — test report`
 2. `**The change.**` — один абзац в словах продукта (пишет scribe).
 3. [code verdict] `**Verdict: ...**` абзац: ready to ship | ready once you finish the checks left with you | not ready to ship as is; счёт багов, доказанных/недоказанных/ждущих/отложенных требований; строка `delivery_ready: yes | after_checks — ... | no — ...`.
 4. `Notation:` строка (R-n, id кейса, TS-n, BUG-n) — пишет scribe.
 5. [code] `## Proven — <N> green tests` — по областям: R-n словами, id кейса, слова критика, уровень проверки.
 6. [code] `## Checked by hand — <n> of <m>` — по строке на кейс ручной проверки (см. (4)).
 7. [code] `## Product bugs — ...` — нумерованный список: серьёзность · R-n · кейс — что сломано — файл:строки; или `none found`.
 8. [code] `## Review gaps — <n> tests the code critic rejected` — тесты, отклонённые критиком при исчерпанном лимите; или `None: ...`.
 9. `## Left with you` — по пункту на каждую проверку, оставленную человеку: `To check:` + (тест есть/нет) + `Needed:` или `How:` + желаемый ответ (fix now · other stand · defer with a reminder · accept the risk). В конце два [code] блока: `### Added after gate B (from your answers)` (только после gate B) и `### Regression to run (from the plan approved at gate A)`.
 10. [code] `## Open questions — <N>` — в блоке кода: `<owner role> · <question>` или `none`.
 11. [code] `## Skipped by the plan (approved at gate A)` — R-n, причина плана или слова человека дословно, риск в проде.
 12. [code] `## Not proven, and what it costs` — R-n, что остановило проверку, риск.
 13. [code] `## Decided at gate A` — authorization_source дословно, оверрайды стадий со словами человека.
 14. [code, только после gate B] `## Decided at gate B (<date>)` — слова человека дословно, куда ушли баги, что ушло наружу или «not recorded».
 15. `## Factory defects — nothing is wanted from you` — не более двух абзацев словами; scribe.
 16. [code] `## Size` — Forecast / Fact / Difference.
 17. [code] `## Where to look` — список документов (understanding.md, test-plan.md, retro.md, приложение).
 18. `## Appendix — traceability` — вывод `traceability.py --task <T> --render` дословно (строка на пару требование × кейс, результаты pass · bug · wait · blocked · not run · unreachable · deferred · not planned: s8.md:50-52).
 Плюс по необходимости: `## Exploratory findings and unresolved questions`, `### Branches left with you`, `## Branches not proven` (grammar.py:196). Порядок секций, которые требует валидатор (REPORT_SECTIONS): Proven, Product bugs, Left with you, Open questions, Not proven, Decided at gate A, Decided at gate B (после gate B), Factory defects, Size, Where to look, Appendix (grammar.py:103-116, 123).
c. Правила: пишется «сверху вниз от решения» (шаблон :3-9); читатель не знает слов фабрики; запрещено: путь `work/`, хэши `cv_`, `ti_`, фрагмент `<!-- factory-summary`, голый `S5-160` без текста (grammar.py:278-286; validate_artifacts.py:1407-1420); в шаблоне :8-9 также: без backlog id, без имён состояний леджера, без имён файлов в Factory defects (проверка human_text, validate_artifacts.py:1431-1452); авторский текст (вне блоков, вне приложения) <=6144 байта (validate_artifacts.py:1768, :2004-2005); счета и статусы пишет только код, руками не правятся (шаблон :11-16); скриншоты не вставляются: в отчёте только `provided` / `not provided` (grammar.py:251-253; s8.md:85-87); тест, который критик не смог проверить, не считается доказанным и стоит под Left with you (шаблон :44-56); Left with you обязан иметь пункт на каждую проверку, оставленную человеку (шаблон :101-103; grammar.py:273-276); деньги в отчёт не пишутся (OWNER_PRINCIPLES P18, :55); язык английский. Пустое: `none found`, `None: ...`, `No regression: ...`, `Nothing to show: ...`, `Forecast: unknown — ...`, `not recorded by the requirements`, `not recorded`; блок «Proven» при нуле читается `## Proven — 0 green tests`, не опускается (шаблон :44-46).
d. Пишет qa-doc-scribe на S8: сначала `report_facts.py --write` (код), затем проза, затем `report_facts.py --check` (s8.md:75-83); после gate B и ретро отчёт перестраивается кодом (`## Decided at gate B`, s9.md:154-182). Человек видит на gate B: сообщение — короткая форма, содержит вердикт, таблицу трассируемости, разделы Product bugs / Left with you / Skipped by the plan / Not proven, остальное — путь к файлу (s8.md:152-175).
e. Проверяет: validate_artifacts.py::check_test_report (:1120-1156): check_report_ledger_and_readiness (вердикт = леджер, :1993+, лимит байт), check_report_sections, check_report_traceability, check_report_left_with_you, check_report_test_marks, check_report_forbidden, check_report_gate_b, check_report_blocks; check_report_human_text для Factory defects (при записи); report_facts.py --check (exit 0 обязателен); check_traceability.py, ledger.py, check_delivery.py (s8.md:41-46); S9 report_check→rebuild (s9.md:184-191).
f. Слова владельца (дословно, русский, носитель OWNER_PRINCIPLES.md): P18, 30.09 — «Деньги в файлы репозитория (отчёт) не пишутся.» (:55-57). P21, 02.10 и 03.10 — «Тогда раздел отчёта «Left with you» называет каждый такой пункт с командой или шагами **и регрессионное тестирование с его скоупом по мнению фабрики**. Пропущенный пункт блокирует ОТЧЁТ (код сверяет раздел с леджером и отказывает), не вердикт» (:75-77). P20, 01.10 — «нет ответа — **пробел** в отчёте, а не зелёный или красный результат» (:71). 03.10, «owner amendment» о делении на skipped-by-plan и not-proven — только пересказ в grammar.py:164-167 (не цитата).

### (4) Отчёт ручных проходов агентом (со скриншотами)
Отдельного документа нет. Есть два носителя и одно правило слов.
a. Носители: блок `## Checked by hand` в test-report (T/test-report.md:58-69; grammar.py:148-152, 173); раздел пакета gate B `## Screenshots of the manual checks` (P/scripts/report_facts.py:1322-1364, вставляется gate_brief.py:5187-5195); ledger-строка Manual evidence (grammar.py:246-248); записи доказательств P/references/manual-evidence.md:1-126.
b. Секции/строки: в отчёте блок `## Checked by hand — <n> of <m>`: строка по кейсу `- **<case id>** (R-n) — "<the Then, quoted>" — before: <value · where it comes from | not recorded by the requirements> — now: <what the runner saw> — result: <passed | failed | inconclusive> — screenshots: <provided | not provided (why)>`; не проверенный кейс: `- **<case id>** (R-n) — "<the Then, quoted>" — not checked: <why, in words>`; нет кейсов: `Nothing to show: no case was planned for a manual check.` (шаблон :63-69). В пакете gate B: заголовок `## Screenshots of the manual checks`, фраза «Screenshots of the manual checks, for you to confirm the cases (they stay on this machine, not in the repository or the merge request):», далее `- <кейс (Then)>: <абсолютные пути>` (report_facts.py:1322-1324,1364). Нет картинок — раздела нет и ничего не обещается (:1356-1363).
c. Правила: блок пишет только код, scribe не правит (шаблон :58-62; s8.md:78-80); кейс без валидной записи — «not checked», никогда не под Proven; inconclusive не засчитывается; «Before» берётся из реестра требований (Behaviour claims), иначе `not recorded by the requirements` (manual-evidence.md:107-109); слова о скриншотах единственные: `screenshots: provided` | `screenshots: not provided (none were taken for this check)` | `screenshots: not provided (no copy on this machine)` (grammar.py:251-253), «provided» только для картинок из списка gate B (grammar.py:249); путь к скриншоту не печатается в отчёте и MR (s8.md:85-87); список не режется (report_facts.py:1331); агент-запись: вердикт агента не меняется кодом, pass требует `--then-quote` на каждый Then и completion-capture (manual-evidence.md:76-85,119); UI требует визуальное/trace-доказательство до и после (:113-114).
d. Проход делает qa-runner на S6 через manual_capture.py (запись) и manual_evidence.py build (сборка, manual-evidence.md:1-6, 76-78); отчёт-блок строит report_facts.py на S8; человек видит блок в отчёте и список скриншотов в пакете gate B; по запросу `report_facts.py --task <T> --screenshots` (s8.md:86-88).
e. Проверяет: manual_evidence.py validate/write-block (validate_manual_current: хэши, пины, источник, диспетчер S6; manual-evidence.md:122-126); report_facts.py --check; ledger/check_delivery (формулировка состояния); гард на «большой файл» и запись скриншота — известная проблема в piles (execution-probes/README.md:134, строка найдена grep g14, не читал).
f. Слова владельца: 24.11.2026, дословно (carrier plugins: plans/piles/execution-probes/findings/20261124-keys-bez-drayvera-vypolneno-agentom-s-dokazatelstvami.md:5-8): «там не должно быть "не выполнено", а должно быть "выполнено агентом" а почему доказательств нет? Агент может сделать скриншот экрана?» Статус по тому же файлу: «Решение владельца нужно: нет (слово дано)» (:3). 31.10.2026 (пересказ, не цитата): скриншоты — человеку, не в репозиторий, в доставляемом тексте только provided / not provided (grammar.py:246-248; s8.md:85). P19, 30.09 — OWNER_PRINCIPLES.md:61: агент «показывает человеку «было / стало»». P20, 01.10 — :66-70: показывают «как было ДО» и «как есть сейчас».

### (5) retro.md — ретро
a. Носители: шаблон T/retro.md:1-60; фаза P/skills/qa-story/phases/s9.md (1-230); карточка P/agents/qa-retro-analyst.md (:15-25, 53-67); числа P/scripts/retro_numbers.py (render :2661+).
b. Секции шаблона (T/retro.md:11-60, прочитано 1-60), заголовки дословно:
 1. `# <TICKET-ID> — retro`
 2. `## What went wrong, and what to do about it` — 3-5 строк простым языком, первое в файле: что случилось — число из retro-numbers.json — что менять; если ничего — одна строка об этом.
 3. `## The numbers` — вставка work/retro-numbers.md без изменений (расход и доля оркестратора, по стадиям и ролям, три самых дорогих запуска, переделки, отказы и блоки gate, остановки и ожидание человека, время до первого теста, оценка против факта); при INCOMPLETE слово повторяется.
 4. `### Marathons` — по дорогим запускам: роль, запросы, 2-3 доминирующих инструмента, механизм.
 5. `## Rejects and overrides` — отказы по семействам причин; число оверрайдов диспозиций на gate A.
 6. `## Estimate vs fact` — прогноз против факта, одна строка (+ запись в estimation-ledger).
 7. `## The human's answer` — ответ на единственный вопрос дословно или `declined to answer`.
 8. `## Findings → factory-backlog.md` — `FB-n — <одна строка>`.
c. Правила: числа считает только retro_numbers.py, не пересчитывать из journal/cost (шаблон :3-5, qa-retro-analyst.md:55); ретро всегда полное (`retro_mode: full`; `numbers`/`skip` не пишутся с 0.10.9, s9.md:16,31-48) — шаблон :6-9 ещё описывает три режима (расхождение с s9.md); никогда не выдавать счётчик токенов за стоимость, не публиковать долю оркестратора при INCOMPLETE (шаблон :27-30); один вопрос человеку дословно: «One question for the retro: what did you dislike in this session, what should change? (optional — reply 'skip')» — «That is the whole message. No preamble…» (s9.md:91-96); `skip`/молчание = declined; ответ копируется строкой в factory-backlog (`scope: local-calibration`, шаблон :51-54); деньги в ретро остаются (retro_numbers.py:2669-2672, ссылка на слово владельца 30.09 F11); язык английский. Пустое: «declined to answer»; нечего сказать — одна строка «ничего не сломалось».
d. Пишет qa-retro-analyst на S9 (диспатч после того, как gate B исполнен, `controller next` = closed; s9.md:44-48); числа code раньше; ответ человека спрашивается до диспатча (s9.md:87-89). Человек видит: единственный вопрос и последнюю сводку <=10 строк со ссылкой на `retro.md` (s9.md:211-226); сам файл — через `## Where to look` отчёта (шаблон :187-188).
e. Проверяет: нет проверки секций retro.md в validate_artifacts.py (grep g16/g20: единственная ссылка :157 — подсказка «next»); required_outputs: [retro.md] проверяется при сдаче роли (s9.md:5-9; exit_gate.py:926); estimate_record.py связывает байты retro.md (retro_numbers.py:3049); аудиты A15, A21 (qa-doctor, по story-roles digest); приём collect читает ретро по точному заголовку (piles driver-hosts/findings/20261030-priem-chitaet-retro-po-tochnomu-zagolovku.md:1, по grep, не читал).
f. Слова владельца: 30.09, F11 (пересказ автора кода, retro_numbers.py:2669-2670): ретро хранит свои деньги, «no money in the repository» — про тест-репорт. 29.10.2026 дословно из кода (retro_numbers.py:1382-1383): «5 tests, run 31 times, now for the environment, now for the factory's errors» — и ретро не сказало ни того ни другого (SC2-37). D-0052, 19.10.2026, п. 4 (plans/piles/collect/README.md:38, строка найдена grep, не читал целиком): «качество — из ретро». 20.10 о тарифах в ретро: retro_numbers.py:481 — только упоминание в grep g8, не читал.

### (6) Прочие документы и пакеты перед человеком (по строке; носитель)
- Source review S1 (таблица источников + вопрос про стенд, один показ): P/skills/qa-story/phases/s1.md:182-211; формирует `ticket_adapter.py review`.
- Понимание-бриф при `blocked` (понимание + блокирующие вопросы, без плана): P/skills/qa-story/phases/s2.md:82-103.
- questions-for-owner.md (сводная таблица, детали по каждому Q: «The source says», «Readings», требования без наблюдаемого в коде): T/questions-for-owner.md:1-65; идёт частью gate A, не отдельным раундом (:3-4). Внутреннее противоречие по "proposed working interpretation" (:9-12 против :47-49) — в references digest D2.
- Gate A message (файл work/gate-a-message.md, строится кодом): P/scripts/gate_brief.py:3557 (write_gate_message), :1925; render :4028-4085; секции по заголовкам g12: `# Gate A — <task>`, строка `**Approve: ...**`, Plan/Pyramid/Cases/Critic/Size (gate_brief.py:3095-3161), `## After your approval` (:3186), `## Open questions (n)` (:3208), `## Stand gaps (n)` (:1829), `## Attachments: not turned into requirements ({n})` (:3397), `## Tickets you kept: no requirement taken from their text ({n})` (:3651), `## What the factory adapted by itself` (:595), `## Already decided by you — repeated, not re-asked` (:3309), `## Left out by your words — ...` (:3270), `## Not reachable by the factory - recorded without asking you` (:3332), `## Warnings the factory is carrying` (:3345), `## Sources found after the S1 review — new to you` (:3356), `## e2e rows without a highest-risk field (n), for your information` (:3361), `## Not readable by this brief — say so rather than guess` (:3375), `## Judge` (:114), `## The long documents (paths, not summaries)` (:3380), `## How to answer` (:3073). Лимит: MAX_LINES = 41, поднят 17.11.2026 «on the owner's word about size limits» (gate_brief.py:63-65); карточки вопросов и ответные блоки в лимит не входят (:4057-4080), при обрезке строка `_(brief truncated at N lines; ...)_` (:4083).
- Reference behaviours (старая версия как эталон): work/reference-behaviours.md, gate_brief.py:1926,1957-1966; `## The old version as the reference (<env>)` (:3972).
- Gate B message (7 пунктов в фиксированном порядке): P/skills/qa-story/phases/s8.md:150-261: вердикт; таблица трассируемости; Product bugs · Left with you · Skipped by the plan · Not proven; `## Run these yourself (n)` (gate_brief.py:5135); `## Stand gaps`; решение по каждому пробелу (fix now / verify on another environment / defer with a reminder / accept the risk); элементы доставки (Bugs to file нумерованный список MAX_BUGS=15 gate_brief.py:69, MR, TMS-квитанции, что не коммитить); `## Open before the MR (n)` / `## Open items (n)` (gate_brief.py:5162-5163); `## Judge`; `## Screenshots of the manual checks`; `## The long documents (paths, not summaries)`; `## One bug or several` (:4908) и `## What each answer costs and does` (:4935) — карточки решений.
- Карточка стенда (stand gap card): gate_brief.stand_gap_card_lines, одна на оба гейта (s8.md:181-185).
- Вопросы человеку любого вида (границы driver: s1_review, s1_gap, gate_A, gate_B, halt, retro, conductor), halt роли, закрывающий вопрос S9: правила P/references/human-questions.md:1-160; проверка human_text.py; цена вариантов `the factory:` / `you:` / `the story:` (:38).
- Единственный вопрос ретро (фиксированный текст): s9.md:91-92.
- Финальная сводка <=10 строк: s9.md:211-226.
- Interim-report (пакет await при stop first_look): s3.md:57 (имя файла в карточке, содержание не читал).
- delivery-summary.md (лежит в work/, по пути показывается в gate B «The long documents»): s8.md:48-53, gate_brief.py:5198-5200.
- Сообщение о возвращённом стенде/репозитории (`config-restore`, `repo_words --reminder`): s9.md:25,156-161 (строка `line` сообщается человеку как есть).
- Жалобы/halts конструктора: «Factory defects» в отчёте (см. (3)).
- Документы онбординга и qa-doctor: не проверял (Not done).

Что для разных обязанностей общее: правило текста человеку (P/references/human-questions.md:13-62): читатель знает продукт и историю, не знает внутренностей фабрики; запрещены имена полей схемы, имена скриптов и отказов вне блока «How to answer», пути внутри плагина, id диспатчей, сырые HTML/stack trace, голые id строк (TS-14, OBL-7, SURF-, SRC-, REQ-, TC-) без объяснения, ключи конфигурации и команды `/qa-factory:`, имена внутренних файлов (JSON/YAML/JSONL/текст, леджер), внутренние названия стадий без пояснения, необработанный текст отказа; два измеренных провала TP1-13797 (:64-71); показывает текст, даже если он нарушает правила (human-questions.md:146-150, число нарушений пишется в state/driver-questions.jsonl). Проверка: human_text.py + references/human-text.json (:134-145).

needed beyond the manifest: P/scripts/gate_brief.py, validate_artifacts.py, grammar.py, report_facts.py, retro_numbers.py, plans/piles/execution-probes/findings/20261124-keys-bez-drayvera-vypolneno-agentom-s-dokazatelstvami.md, P/skills/qa-story/phases/s1-s4,s8,s9.md, P/agents/qa-retro-analyst.md, qa-doc-scribe.md — выходят за указанный given (skills/references/templates/scripts/design/OWNER_PRINCIPLES/PROJECT_FULL/piles), все нужны были для carriers.

this needs a decision from a tier above.
