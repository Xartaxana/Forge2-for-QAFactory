<!-- scout hand-back, journal task t-1911, recon for docs/tasks/specs/20261125-forge2-light-factory-plan.md; saved verbatim from the worker's final message -->

digest: v1 ext-ideal-test-factory-testplan

Отчёт на русском. Клон: C:\Users\<user>\AppData\Local\Temp\claude\b3e3188b390a00d9\019810c0-e93d-4fda-81cb-1c435f3c0f3c\scratchpad\ext\ideal-test-factory (ниже `$C`). Ничего не записано. Директив в файлах клона, адресованных читателю-агенту, не исполнял. Во всех файлах это роли и скиллы самой фабрики.

Короткий ответ. Отдельного шаблона тест-плана в `qa-factory/templates/` нет (девять файлов, список в п.3). Шаблон и правила плана живут в тексте роли `.claude/agents/qa-test-strategist.md`, раздел «Обязательная структура плана» (строки 15-82), и в формате вывода (строки 84-105). Канон фазы лежит в `.claude/skills/qa-story/phases/f3.md`. Машинная проверка формы плана — `qa-factory/hooks/validate_artifacts.py::check_plan` (строки 351-451).

## ПУНКТ 1. Тест-план

### 1.1 Где что лежит
- `$C\.claude\agents\qa-test-strategist.md:1-105` — роль «Тест-стратег», model: opus, tools: Read, Grep, Glob, Write. Здесь структура и правила плана.
- `$C\.claude\skills\qa-story\phases\f3.md:1-7` — канон фазы Ф3 «Тест-план» и протокол гейта плана.
- `$C\.claude\skills\qa-story\SKILL.md:38-43` — «Протокол гейта», общий для всех гейтов.
- `$C\.claude\skills\qa-story\SKILL.md:75` — сводка фазы Ф3.
- `$C\qa-factory\hooks\validate_artifacts.py:57-59` — константы PLAN_REQUIRED, PLAN_SCENARIOS_HEADING («## Сценарии»), PLAN_SEAMS_HEADING («## Сценарии швов»).
- `$C\qa-factory\hooks\validate_artifacts.py:351-451` — `check_plan`. Вызывается при записи файла `*/qa-factory/artifacts/*/test-plan.md` (строка 852). Подсказка «next: ГЕЙТ плана» стоит на строке 121.
- `$C\qa-factory\hooks\grammar.py` — закрытые списки: классы дефектов, шкала влияния, грамматика оракула, PLAN_PROFILES. Файл не читал, ссылаюсь на него по `common-rules.md:112-120` и вызовам `G.*` в `validate_artifacts.py`.
- `$C\qa-factory\hooks\config.json` — переопределения `defect_classes_extra` и `impact_scale`. Файл не читал, ссылка из `qa-test-strategist.md:36-37`.
- `$C\qa-factory\docs\tester-mindset-plan.md:176-220` — проектное обоснование «WP3. Тест-план как карта рисков». Это документ-замысел, не правило.
- `$C\qa-factory\strategy\test-strategy.md` — в клоне его нет. Это проектный файл, его создаёт онбординг (`qa-story/SKILL.md:36`: нет файла → стоп «сначала qa-onboarding»). В клоне есть только `strategy/common-rules.md` и `strategy/test-code-patterns.md`.
- Артефакт плана пишется в `qa-factory/artifacts/<task>/test-plan.md` (`qa-test-strategist.md:105`).

### 1.2 ПОЛНЫЙ список секций плана по порядку (`qa-test-strategist.md:101-103`)
Заголовки дословно, по одной строке на содержание.

Сначала YAML-frontmatter (строки 86-101) с полями: `task`, `created`, `profile: feature|parity`, `complexity: <XS..XL>`, `requirements_total`, `scenarios_total`, `smoke`, `by_defect_class`, `by_priority`, `na_requirements`, `channels: {auto, manual_agent, manual_human}`, `open_questions`, `nfr: {smoke, full, cases, unknown, not_ours}`. Обязательными для кода являются только `task, created, scenarios_total, smoke, by_defect_class, by_priority, requirements_total` (`validate_artifacts.py:57`).

1. `## Цель и глубина` — ссылка на intent-brief, подтверждённые цель и скоуп, глубина. Она идёт первой (строка 11).
2. `## Пирамида` — решение по КАЖДОМУ из 6 уровней: Unit, API, Интеграционные, E2E, Мануальные, Exploratory. Формула: «тестируем: <сценарии>» либо «N/A: <причина>» (строки 17-24).
3. `## Техники` — применённые техники тест-дизайна. В конце вопрос пользователю, какие ещё области и приёмы добавить (строка 27).
4. `## Сценарии` — таблица строк риска TS-n. Порядок первых восьми колонок фиксирован, его читает валидатор. Колонки: `TS · R · Что может пойти не так · Влияние · Приоритет · Эксперимент · Отличающее наблюдение · Основание · Уровень · Канал · Техника · Почему техника · Данные · Конфигурация` (строки 30-43, 103).
5. `## Сценарии швов` — по каждому ребру `seams_touched` реестра строка (класс `seam`) или явный N/A с причиной. Швов нет — одна строка «швов не найдено: <seams_search реестра>» (строка 50).
6. `## N/A по реестру` — R → причина (требования без строки; они же в `na_requirements`).
7. `## Нефункциональные` — таблица: тип · режим из стратегии · решение в плане · кто исполняет. По каждому применимому типу ровно одна ветка из пяти режимов: `not_ours`, `smoke`, `cases`, `full`, `unknown` (строки 62-69).
8. `## Blast radius и регрессия` — список «изменение → что задето → что проверить»; устаревшие кейсы `TC-id → что устарело`; затем набор регрессии с привязкой каждого кейса к пункту списка; затем пробелы (строки 52-60).
9. `## Вопросы к команде` — открытые вопросы (непроверяемые требования уходят сюда, строка 75).

Условные секции, не в основном списке, но названные в тексте роли:
- «Отклонение от ориентира» — заявка пересмотра размера, если сценариев больше верхней границы (строка 73).
- «Отклонение от профиля» — если blast radius показал смену поведения (строка 58).
- «Deferred» — срезанные P3/P2 при превышении границы (строки 73, 79).
- Строка «чувствительность регрессии» и строки characterization — только для `profile: parity` (строка 45).

### 1.3 Правила составления
Обязательно:
- План строится ТОЛЬКО в рамках подтверждённого понимания. Сценарии вне подтверждённого скоупа без вопроса не планируются. Blocked-аспекты readiness не планируются «на угад», только вопросом в батч (строка 11).
- Единица покрытия — требования реестра, все шесть источников: story, feature, assumption, discussion, ac, derived. AC не граница (строка 13).
- Решение по каждому из 6 уровней пирамиды: «тестируем» или «N/A: причина» (строка 18).
- Строка плана — строка риска. Гипотеза дефекта имеет вид `класс @ место`. Закрытый список классов: `boundary · state · order · concurrency · permission · data-loss · contract · seam · error-path`, плюс `regression:BUG-NNN`. Проект расширяет список через `hooks/config.json defect_classes_extra`. Строка без гипотезы — `smoke` (строка 36).
- Влияние — из шкалы `data-loss · money · access · blocked-flow · degraded · cosmetic · none` (переопределяется `impact_scale`). Приоритет ВЫВОДИТСЯ из влияния: data-loss/money/access → P0, blocked-flow → P1, degraded → P2, cosmetic/none → P3. Не назначается; расхождение — reject валидатора. Вероятность дефекта приоритет не меняет, она задаёт только порядок исполнения (строка 38).
- Отличающее наблюдение — по независимому каналу: повторное открытие, GET после POST, второй сеанс, чтение хранилища. «Ответ 200» и тост — это действие, не наблюдение (строка 40).
- Основание (оракул) фиксируется ДО прогона: `requirement:R-n · invariant:<id> · consistency:<…> · history:<baseline witness> · external:<норма>` (строка 41). Валидатор принимает также `impact:` (`validate_artifacts.py:404`).
- Канал строки: `auto` / `manual-agent` / `manual-human`. Тест, не нужный в регрессии, НЕ автоматизируется. Распределение подтверждает человек на гейте (строка 42).
- Перекличка по реестру: у каждого R есть строка или явный `N/A: <причина>` (frontmatter `na_requirements`). Из багов области, включая Closed, — регрессионная строка на КЛАСС дефекта, не на экземпляр (строка 47).
- Техника в строке — с одной фразой «почему именно она» (строка 27).
- Типы тестирования — строго из стратегии проекта: исключён стратегией → не покрывать, включён → на заданную глубину (строка 74).
- Для `nfr: unknown` вопрос в батч. Для `full` без документа нормы — строка с пометкой «норма не задана» (строка 67).
- Данные и конфигурации — из секции «Тестовые данные» project-profile. Данных нет или «неизвестно» → вопрос в батч, не предположение. Данные, которые трогать нельзя по профилю, строка не использует (строка 43).

Запрещено:
- «Добивать до нижней границы» ориентира сценариев. Обоснованных сценариев меньше нижней границы → заявить в секции отклонения, что размер завышен (строка 72).
- Резать скоуп молча под ориентир при превышении верхней границы. Нужно заявить пересмотр размера, решение принимает человек (строка 73; `f3.md:5`: «Резать скоуп под старую оценку молча — запрещено»). Резать в «Deferred» можно только с хвоста приоритетов и только внутри подтверждённого размера.
- Смоуков больше одного на требование (строка 47; код: `validate_artifacts.py:419-423`).
- Назначать приоритет вручную (строка 38).
- Молчаливый выбор версии при противоречии в матрице реестра: только вопрос в батч (строка 13).
- Строить регрессию «на угад» при отсутствии MR (`implementation.status: not_found`): фиксировать «не определён», вопрос в батч, секция «до появления MR» (строка 57).
- Писать юнит-тесты. Они живут в репозитории приложения, запись блокирует хук (P-00, строка 19).
- Расписывать методику полной NFR-проверки: она у специалиста (строка 67).
- Правка плана при смене профиля: после смены план пишется заново (`f3.md:5`).

Уровни тестирования (шесть, строки 17-24):
- Unit — не пишет фабрика; это аудит покрытия от разработчиков.
- API — эндпоинты изменённой области.
- Интеграционные — внешние сервисы, БД, очереди.
- E2E — немного, без дублирования нижних уровней.
- Мануальные — что проверяется руками и почему.
- Exploratory — чартер для значимых фич.

Как выбираются проверки (строки 26-27, 36-47, 55-60):
- Каждая строка выводится из пары «требование R + гипотеза дефекта». Техника — суждение стратега с обоснованием в строке.
- Регрессия: шаг 1 — blast radius по MR (`implementation.files`, `endpoints_or_screens`, `tech_signals`, `entities_touched`, `seams_touched`, плюс `blast_radius_hint` из readiness). Шаг 2 — набор регрессии как существующие кейсы по содержанию, не только по полю `area`. Каждый кейс привязан к пункту шага 1, кейс без привязки — «балласт».
- Профиль parity (рефакторинг, миграция, апгрейд): основание строк `history:` или `invariant:`; validator отклоняет план, где больше половины строк иначе (`validate_artifacts.py:408-417`). Набор регрессии `full` при изменении общего компонента.
- NFR берутся из таблицы «Нефункциональное тестирование» в test-strategy проекта (в клоне её нет).

Как пишутся риски, скоуп, out-of-scope, окружения, данные:
- Риски — колонки «Что может пойти не так» + «Влияние» + «Приоритет». Калибровка из стратегии (Fragile Areas, забагованные области) первична над интуицией стратега при выборе класса и места (строка 76).
- Скоуп и глубина — первая секция «Цель и глубина», из intent-brief. in_scope / out_of_scope / blast_radius_hint берутся из `requirements-readiness.json` (блок `depth`, `qa-requirements-tester.md:177`).
- Out-of-scope отдельной секции в плане не имеет. Он живёт в intent-brief / readiness. Критик проверяет, что кейсов вне скоупа нет без пометки (`qa-case-critic.md:22`).
- Окружения: отдельной секции нет. Конфигурации — колонка «Данные · Конфигурация» по правилу матрицы из project-profile: базовая ячейка по умолчанию, несколько ячеек только где правило требует (UI-изменение, локализация) (строка 43). Env-preflight делает раннер, не план (`qa-runner.md:12`).
- Данные — колонка «Данные · Конфигурация» (роль/учётка, сущности и состояния, откуда берутся: сид / генератор / builder / создаётся тестом). Данные в плане не изобретаются.

Размер:
- Ориентир числа сценариев по сложности: XS 1–2, S 2–5, M 5–10, L 10–18, XL 18–28 (строка 72). Ориентир берётся из теоретической оценки Ф1 и не потолок скоупа (строка 73).
- Слияние показывать как «кандидатов → после слияния» (строка 79).
- Сквозные заботы (auth, вьюпорт, a11y) — ассертами внутри строк или параметризацией, не строкой на требование (строка 80).
- «/» или «или» в названии строки — сигнал непокрытых режимов, одна строка = одно наблюдаемо различимое поведение (строка 81).
- Лимита на длину файла плана в строках, символах или КБ в прочитанных файлах не нашёл (см. Not done).

Язык: требований к языку артефакта плана не нашёл. Все роли, шаблоны и скиллы клона написаны по-русски, README на русском. Явного правила «писать план по-русски» не обнаружил (trail G7, G8).

### 1.4 Кто пишет и на каком шаге
- Пишет `qa-test-strategist` (диспатч оркестратора `qa-story`), Ф3, только при `requirements_ready`. Запись делает сам стратег: «Write дан решением командной калибровки 02.09.2026, FB-10» (`qa-test-strategist.md:105`).
- Вход: `requirements-register.md`, context-manifest, `intent-brief.md`, `requirements-readiness.json`, `strategy/test-strategy.md`, `state/seam-map.md`, прогноз сложности (строка 9). Порядок фаз: Ф2а (понимание, обязательна) → Ф2б (разведка, baseline) → Ф3 (план) → Ф4 (кейсы).
- Девиз: «Question first. Plan second. Code never».

### 1.5 Как человек одобряет план (`f3.md:5`, `SKILL.md:38-43`)
Гейт Ф3 обязательный:
- Первая строка гейта — «прочитайте: `artifacts/<task>/test-plan.md`». Артефакт первичен, пересказ его не заменяет.
- Выжимка при артефакте: таблица строк ИЗ файла (TS · R · что может пойти не так · влияние → приоритет · канал), плюс строка счёта «строк N, из них smoke k; классы дефектов: …; N/A по реестру: R-…».
- ОТДЕЛЬНЫЙ вопрос «Одобряете план? да / правки / вопросы». Одобрение не выводится из ответов на вопросы. Все пункты задаются ОДНИМ вызовом `AskUserQuestion`.
- Отдельные пункты гейта: батч вопросов плана («какие области/приёмы добавить?», «какие классы дефектов исключены и почему», распределение каналов); пересмотр размера, если заявлен; пересмотр профиля, если заявлено «Отклонение от профиля» (смена → `classification.json` с `revised`, событие gate, возврат на Ф2а, план пишется заново); пункт по `na_requirements` (каждое отложенное требование — осознанное решение человека).
- Два NFR-пункта: `unknown` непуст → вопросы в батч; `full` непуст → проверить нормы в стратегии, нет нормы → вопрос «какая норма?». `not_ours` и `smoke` на гейте не обсуждаются.
- Правки → повторный диспатч стратегу (1 раз), снова гейт.
- Решение дословно в журнал: `python qa-factory/hooks/log_append.py --event gate --decision <дословно>`. Правки по решению делаются ДО записи gate-события.
- Блок фабрики можно снять явным решением человека на гейте. Это не тихий пропуск: событие gate в журнал и принятый риск в PTR (`SKILL.md:18`).

### 1.6 Что проверяет план потом
- При записи — `validate_artifacts.py::check_plan` (хук; для планов с `created` после RULE_CUTOFF). Проверяет:
  - обязательные поля frontmatter;
  - секцию «## Сценарии» с строками TS-*;
  - минимум 8 колонок в строке;
  - колонка R из R-id реестра;
  - класс дефекта из списка или `smoke`;
  - влияние из шкалы;
  - приоритет равен выводимому из влияния;
  - наблюдение непусто;
  - основание по грамматике оракула;
  - parity-условие на основания;
  - число smoke не больше `requirements_total`;
  - frontmatter `smoke` равен числу smoke-строк в таблице;
  - монокласс при ≥5 требований без smoke → ошибка;
  - наличие секции «## Сценарии швов»;
  - перекличку R (строки или `na_requirements`).
- Самотест формы: `qa-factory/hooks/form_selftest.py:245-253` (кейсы plan ok / plan bad). Файл читал только по grep-строкам.
- Приёмка оркестратором (`f3.md:5`): секция «Цель и глубина», решения по 6 уровням, техники, каналы, «Сценарии швов», blast radius.
- Дальше — `qa-case-critic` (Ф5, блокирующий гейт), рубрика из 8 измерений (`qa-case-critic.md:11-22`):
  - покрытие;
  - атомарность;
  - однозначность;
  - edge-кейсы;
  - негативные сценарии;
  - трассируемость (кейс наследует `defect_class/priority/basis` из строки плана);
  - полнота против плана (перекличка каждой TS-строки и ребра швов);
  - соответствие подтверждённому пониманию и гипотезе дефекта.
- `qa-case-designer` наследует приоритет, класс и основание из плана и не переназначает (`qa-test-strategist.md:76`).
- Постфактум: `qa-failure-analyst` относит провалы к слою `plan` (`qa-failure-analyst.md:58`: «AC было, сценария на это поведение в плане нет»). `qa-doc-scribe` сверяет PTR «Покрытие проверок» по уровням пирамиды ИЗ плана (`qa-doc-scribe.md:18`).
- Детектор задним числом: при status Planned/InProgress/Done без `plan_review` — ошибка «СТАТУСНАЯ МАШИНА» (`validate_artifacts.py:527-529`). Это относится к чартерам exploratory, не к основному плану; указываю, чтобы не путали.

## ПУНКТ 2. Остальные документы

### 2.1 Понимание задачи со списком требований — есть
- `requirements-register.md` — реестр требований. Шаблон: `qa-factory/templates/requirements-register.md:1-59`. Структура (строки 1-59):
  - frontmatter: `task, created, profile, ids, by_source, derived_walked, seams_touched, seams_search, confidence`;
  - `## Реестр` — таблица `R | Требование | source | derived_from | verifiable | ac_ref`;
  - `## Матрица противоречий`;
  - `## Развилки чтения`.
  - source — закрытый список: story · feature · assumption · discussion · ac · derived. Клетки матрицы: `ok:<ref>` · `contradicts:<цитата>` · `silent` · `n/a:<причина>`.
- `intent-brief.md` — «паспорт понимания: цель, место в системе, техмодель, глубина» (`qa-requirements-tester.md:165`). Отдельного шаблона нет. Форма — только это однострочное описание.
- `requirements-readiness.json` — машинный контракт «вход плана». Схема в `qa-requirements-tester.md:166-182`: `verdict`, `confidence`, `goal_summary`, `register`, `profile_mismatch`, `aspects`, `contradictions`, `depth`, `baseline_needed`, `open_questions`, `trace`.
- `requirements-review.md` — frontmatter плюс секции `## Цель и техконтур (аудит фичи)`, `## Findings`, `## Матрица покрытия`, `## Предложения правок`, `## Вопросы владельцу` (`qa-requirements-tester.md:140-159`).
- Показ человеку — «ГЕЙТ понимания» (`phases/f2a.md:7`): «прочитайте: requirements-register.md и intent-brief.md»; строка счёта «реестр: N требований — story k, feature k, … ac k, derived k; швов задето: M; противоречий: C; развилок с вопросом: D»; паспорт «я понял так: цель X, вклад в фичу Y, техмодель Z, глубина W»; матрица аспектов; единый батч вопросов с owner_role (`po_ba | dev_arch | qa`).
- Отдельные пункты решения: родительская фича не аудирована; `verdict: blocked` (снятие блока — только решением человека); `confidence: low`; `profile_mismatch`.
- Проверка кодом: `validate_artifacts.py` на реестр и `check_witness.py` на readiness (блок `register` обязателен).

### 2.2 Отчёт о тестировании — есть (называется PTR)
- `qa-factory/artifacts/<task>/ptr.md`, пишет `qa-doc-scribe` на Ф11 (`qa-doc-scribe.md:18`). Отдельного шаблона в `templates/` нет, форма описана в тексте роли. Секции:
  - `## Смотреть в первую очередь` — человеческий бриф, идёт ПЕРВЫМ. Максимум 5 пунктов, сортировка по blast radius. Теги `[баг] [риск] [env] [хвост] [вопрос]`. Каждый пункт — суть в одну строку и кликабельный путь `файл:строка`. Обе секции вместе ≤ 2 КБ. Антипаддинг: меньше пяти — не добивать.
  - `## Также отмечено` — всё остальное.
  - `## Покрытие проверок` — обязательная. Таблица: уровень пирамиды × канал (auto / manual-agent / human), статус только из закрытого списка `✓ выполнено (N кейсов)` / `✗ есть красные (N)` / `○ не запускался — <причина>` / `— не планировался (<основание из плана>)`. Строки присутствуют ВСЕ и ВСЕГДА.
  - «Готовность в пределах проверенного» (п. 2а, `qa-doc-scribe.md:14`) — обязательна при наличии реестра. Таблица по КАЖДОМУ R со статусом `проверено` / `не проверено` / `отложено by design` / `отложено решением`. Вывод о готовности только в этих границах. Проверка кодом: `check_ptr_readiness` (`validate_artifacts.py:454`).
  - «Нефункциональные» — таблица тип · норма · meets/violates/not-measured · позитивный контроль.
  - «Не верифицировано» — при ENV_ISSUE с полем `unverified` (`qa-doc-scribe.md:29`).
- Правила PTR: числа только из файлов этого прогона; смягчающие формулировки при непроверенном — блокер приёмки; судьба каждого запланированного кейса и каждого R названа (`qa-doc-scribe.md:28-33`).
- Приёмка кода: `qa-factory/hooks/check_coverage.py` (на Ф11, `SKILL.md:19, 91`).
- Прогон: `run-report.json` (схема `qa-runner.md:35-47`), `triage.json`, `automation-manifest.json`, `actual-complexity.json`.
- Показ человеку — гейт закрытия цикла (`phases/f10.md:23-27`, `phases/f11.md` не читал): первой строкой пути к `ptr.md` и MR. Красные сверх `red_lock` — мерж запрещён. Одобрение `ptr.md` идёт одним вызовом с вопросами Ф10.
- Дополнительно: `qa-factory/templates/nfr-report.md` — отчёт специалиста NFR (см. п.3).

### 2.3 Отчёт мануальных проходов со скриншотами — отдельного документа нет
Есть как часть run-report.json и evidence:
- Мануальные проверки `channel: manual-agent` выполняет `qa-runner`. Результат — блоки `manual_checks` (`check`, `steps: ["шаг → факт"]`, `result: pass|fail|inconclusive`), `manual_skipped`, `env_blocked` в `run-report.json` (`qa-runner.md:14-20, 35-47`).
- Evidence-before-PASS: PASS невалиден без финального снапшота. Финальный скриншот ВСЕГДА (pass и fail) → `qa-factory/artifacts/<task>/evidence/` (`qa-runner.md:18, 20`).
- Канал `manual-human` — «нужен человеческий глаз». Для него отдельного отчёта нет, только строка в плане и PTR. `usability` — канал `manual-human`, «кто и когда» решается событием gate (`f3.md:7`).
- Скриншоты в MR / evidence pack: `phases/f10.md:7` («MR с отчётом, скриншотами, таблицей триажа, red_lock'ами НА ВИДУ… Репо нет → evidence pack в `artifacts/<task>/evidence/`»).
- Скриншоты специалистов NFR: `evidence/a11y/`, `evidence/l10n/<locale>/` (`qa-accessibility-specialist.md:37`, `qa-localization-specialist.md:34`).
- Скриншоты аудитора: `qa-factory/artifacts/audit/screenshots/audit-<page>-<date>.png` (`checklists/audit-methodology.md:15`).
- Скриншоты exploratory: `attachments/CH-NNN/` (`exploratory-tester.md:16`).
- Вывод: отдельного шаблона «отчёт ручных проходов» в клоне нет (поиск trail G6, G9).

### 2.4 Вопросы владельцу — есть
- Шаблон: `qa-factory/templates/questions-for-owner.md:1-35`. Заголовок `# <FEATURE-ID> «<название фичи>» — вопросы владельцу требований`.
  - Шапка: источник — аудит требований от <дата>; закрытые на гейте вопросы одной строкой «BLK-n/DEC-n решён: <решение>» и в документ не входят.
  - `## Сводная таблица`: колонки `№ | Вопрос | Варианты решения / рабочая трактовка | Ответ | Кто дал | Когда получен`. 🔴 — блокер. Адресаты по owner_role.
  - `## Подробности`: пункты `### Q1 (BLK-n) 🔴 — <заголовок>` с цитатами, фактами из кода `file:line`, почему блокер, что решить; `### Q2 (MJR-n) — …` с рабочей трактовкой.
  - `## Minor (ответа не ждём — к сведению и в бэклог правок)`: `- **MIN-n** — …`.
  - Блокеры: пока нет ответа, план по областям не строится. Majors: при молчании работаем по рабочей трактовке, но она становится решением только после подтверждения владельцем.
- Собирает `qa-requirements-tester` (эпик-воркфлоу `/qa-requirements`, `qa-requirements-tester.md:162`). В основном `/qa-story` вопросы идут батчем гейта Ф2а и Ф3 в чат; блокеры сначала в чат, остальное — в `requirements-review.md` (`README.md:68`).
- Для основного флоу `qa-story` отдельного файла вопросов, кроме батча гейта и секции плана «## Вопросы к команде», не нашёл.

## ПУНКТ 3. Файлы под `qa-factory/templates/` (полный список: 9 файлов)
Читает человек, если документ идёт на гейт или к владельцу. Агенты — это машинные и рабочие реестры, их читают роли на старте.

1. `charter.md` — шаблон exploratory-чартера (Миссия, Гипотезы, Seed-пути, Известные ловушки, Чек-лист охвата клеток матрицы, Протокол, Находки, Остаток миссии); пишут `charter-designer` и `exploratory-tester`, читают они же и человек на гейте чартера.
2. `factory-backlog.md` — реестр находок о самой фабрике (секции «Находки о фабрике», «Отложенные решения (онбординг/гейты)»); пишет `qa-doc-scribe`, читает в первую очередь оператор фабрики.
3. `metrics-catalog.md` — каталог метрик (пять комплектов) и контракт доски `metrics-board.md` для дашборда; читают `qa-metrics-analyst` и скрипт дашборда, оператор смотрит дашборд.
4. `nfr-report.md` — отчёт специалиста NFR (Позитивный контроль инструмента, Матрица нормы, Находки, Вердикт по строкам плана, Требования нормы вне реестра, Кандидаты в регрессию, Limitations); пишут специалисты Ф8н, читают `qa-doc-scribe`, `qa-bug-reporter` и человек.
5. `obligations.md` — формат реестра хвостов `state/obligations.md`; пишет `qa-doc-scribe` на Ф12, читают Ф0 `qa-story`, `qa-release`, `qa-requirements`; показывается пользователю до старта задачи.
6. `perturbations-seed.md` — библиотека возмущений для генерации exploratory-чартеров (Матрица возмущений, Пары фич без совместного прохождения, Оси-кандидаты); читает `charter-designer`, дополняют из escape-разборов.
7. `questions-for-owner.md` — вопросы владельцу требований (пункт 2.4); читает человек, владелец фичи.
8. `requirements-register.md` — реестр требований (пункт 2.1); пишет `qa-requirements-tester`, читают стратег, дизайнер, критик, писарь и человек на гейте понимания.
9. `seam-map.md` — карта швов «сущность/состояние → кто пишет → кто читает» (Рёбра, Швы без совместного прохождения); читают `qa-test-strategist`, `qa-requirements-tester`, `charter-designer`.

Шаблонов тест-плана, PTR, intent-brief, test-report и отчёта ручных проходов в `templates/` нет (Glob `qa-factory/templates/**/*`: найдено 9, перечислены все).

## Файлы, которые упоминают тест-план (DoD-перечень)
Выборка по grep `test plan|test-plan|тест-план|тест план` (-i, без html). Файлы с упоминанием плана и что в них сказано:
- `.claude/agents/qa-test-strategist.md` — основной источник (п.1).
- `.claude/skills/qa-story/phases/f3.md` — канон фазы и гейт (п.1.5).
- `.claude/skills/qa-story/SKILL.md:48, 75` — карта артефактов и сводка Ф3.
- `.claude/agents/qa-case-critic.md:3, 9` — рубрика критика сверяет кейсы с планом.
- `.claude/agents/qa-case-designer.md:3, 9` — разворачивает сценарии плана в кейсы.
- `.claude/agents/qa-automator.md:9` — берёт тест-план как вход.
- `.claude/agents/qa-runner.md:9` — берёт импакт-набор регрессии и manual-agent проверки из плана.
- `.claude/agents/qa-complexity-assessor.md:54` — читает `test-plan.md` как факт сценариев по уровням пирамиды.
- `.claude/agents/qa-failure-analyst.md:58` — слой `plan` в разборе сбежавших багов.
- `.claude/agents/qa-requirements-tester.md:11, 97, 165` — «Тест-план не может быть первым местом, где выясняется смысл задачи»; readiness как вход плана.
- `.claude/agents/qa-doc-scribe.md:18` — PTR сверяет покрытие с планом (в строке 18 вывод Grep пропустил длинную строку; содержание подтверждено чтением файла).
- `.claude/skills/qa-escape/SKILL.md:15` — упоминание плана (длинная строка Grep пропустил, содержание не читал, см. Not done).
- `README.md:3, 76` — план в конвейере; «Человеческие гейты: тип задачи, апрув тест-плана, опционально ревью кейсов, ревью MR».
- `qa-factory/docs/tester-mindset-plan.md:97, 176` — замысел «WP3. Тест-план как карта рисков».
- `qa-factory/hooks/form_selftest.py:245-253` — самотесты формы плана.
- `qa-factory/hooks/validate_artifacts.py:121, 852` — подсказка и вызов проверки.
- `qa-factory/templates/obligations.md:15` — пример хвоста со ссылкой на `test-plan.md, сценарий TP-03`.
- `qa-factory/templates/questions-for-owner.md:8` — «тест-план по соответствующим областям не строится» до ответа на блокер.
- Исключены как не относящиеся: `docs/test-factory-blueprint.html` (47 совпадений по полному набору паттернов) и `docs/test-factory-cross-section.html` (6) — HTML-схемы, содержимое не читал, исключены фильтром `glob=!*.html` и не просмотрены (см. Not done). `checklists/**`, `adapters/README.md`, `exploratory-charters/README.md` — совпадений по узкому набору «test plan|test-plan|тест-план|тест план» нет. По широкому набору со `strategy|checklist` они совпали (слово «checklist» — это чек-листы аудита, не тест-план).

## Объекты

| id | kind | gist | paths | status | owner | links | ev |
|---|---|---|---|---|---|---|---|
| q1a | template | Шаблона test-plan в templates/ нет; структура плана в тексте роли qa-test-strategist | .claude/agents/qa-test-strategist.md:15-105 | present | strategist | q1b | G1,R1 |
| q1b | rules | Девять секций плана, 6 уровней пирамиды, 14 колонок таблицы сценариев | .claude/agents/qa-test-strategist.md:101-103 | present | strategist | q1a | R1 |
| q1c | gate | Гейт плана: путь файла первой строкой, отдельное одобрение, один AskUserQuestion | .claude/skills/qa-story/phases/f3.md:5 | present | оркестратор | q1b | R2,R3 |
| q1d | detector | check_plan проверяет форму, вывод приоритета из влияния, перекличку R, smoke | qa-factory/hooks/validate_artifacts.py:351-451 | present | hook | q1b | R4 |
| q1e | absent | Требований к языку артефакта плана и лимита длины файла в прочитанном нет | README.md | absent | — | q1a | G7,G8 |
| q2a | doc | requirements-register — есть шаблон, intent-brief и readiness — только описание | qa-factory/templates/requirements-register.md:1-59 | present | requirements-tester | q1a | R5,R6 |
| q2b | doc | PTR — отчёт о тестировании, секции Смотреть в первую очередь, Покрытие проверок, Готовность | .claude/agents/qa-doc-scribe.md:18 | present | doc-scribe | — | R7 |
| q2c | absent | Отдельного отчёта ручных проходов нет; manual_checks в run-report.json и скриншоты в evidence | .claude/agents/qa-runner.md:14-20 | absent | — | q2b | G6,G9 |
| q2d | template | questions-for-owner — шаблон есть, Сводная таблица, Подробности, Minor | qa-factory/templates/questions-for-owner.md:1-35 | present | requirements-tester | — | R8 |
| q3 | list | В templates/ девять файлов, список в п.3 | qa-factory/templates | present | — | — | G1 |

## Trail

| tid | op | target | pattern / range | flags | result | control |
|---|---|---|---|---|---|---|
| G1 | glob | $C | `**/*` | — | found 100; показаны 100 из 138, 38 не показаны | — |
| G2 | grep | $C | `test plan\|test-plan\|тест-план\|тест план\|strategy\|стратег\|чек-лист\|checklist\|obligations\|requirements-register` | -i count | count 402; 75 файлов | — |
| G3 | glob | $C | `qa-factory/templates/**/*` | — | found 9 | — |
| G4 | glob | $C | `qa-factory/{strategy,docs,hooks,adapters}/**/*` | — | found 35 | — |
| G5 | grep | $C | `test plan\|test-plan\|тест-план\|тест план` | -i content glob=!*.html | found 43; строки в п. «Файлы, которые упоминают» | — |
| G6 | grep | $C | `скриншот\|screenshot` | -i content glob=!*.html | found 40; head_limit 40, список усечён | — |
| G7 | grep | $C\README.md | `язык\|language\|по-русски\|на русском\|английск` | -i content | absent | G10 |
| G8 | grep | $C\.claude | `язык[а-я]* (план\|отчёт\|артефакт\|документ)\|на русском\|по-русски\|английск\|language` | -i content | found 5; все из qa-localization-specialist.md, про локализацию продукта | — |
| G9 | grep | $C\.claude\skills\qa-story\SKILL.md | `def check_plan\|скриншот\|screenshot\|PTR\|ptr\.md\|test-report\|manual-report\|manual-pass\|evidence` | -i content | found 6; SKILL.md:15, 18, 50, 87, 89, 91 | — |
| G10 | grep | $C\README.md | `тест-план` | -i content | found 3; README.md:3, 76 | — |
| G11 | grep | $C\qa-factory\hooks\validate_artifacts.py | `def check_plan\|PLAN_\|plan_sections\|REQUIRED_PLAN\|Цель и глубина\|max_\|лимит` | -i content | found 12; строки 57-59, 326-327, 351-368, 405-436, 527-529 | — |
| G12 | grep | $C\qa-factory\templates | `^(#\|name:\|description:)` | content | found 60; заголовки всех 9 шаблонов | — |
| G13 | grep | $C\.claude\skills\qa-onboarding | `test-strategy\.md\|Нефункциональное тестирование\|Fragile Areas\|impact_scale` | content | found 4; все строки длинные, не показаны | — |
| G14 | grep | $C\.claude\agents\qa-case-critic.md | `^(#\|\*\*)\|тест-план\|вердикт` | -i content | found 12 | — |
| R1 | read | $C\.claude\agents\qa-test-strategist.md | 1-106 целиком | — | read $C\.claude\agents\qa-test-strategist.md:1-106 | — |
| R2 | read | $C\.claude\skills\qa-story\phases\f3.md | 1-8 целиком | — | read $C\.claude\skills\qa-story\phases\f3.md:1-8 | — |
| R3 | read | $C\.claude\skills\qa-story\SKILL.md | 1-100 | — | read $C\.claude\skills\qa-story\SKILL.md:1-100 | — |
| R4 | read | $C\qa-factory\hooks\validate_artifacts.py | 351-460 | — | read $C\qa-factory\hooks\validate_artifacts.py:351-460 | — |
| R5 | read | $C\qa-factory\templates\requirements-register.md | целиком, 1-60 | — | read $C\qa-factory\templates\requirements-register.md:1-60 | — |
| R6 | read | $C\.claude\agents\qa-requirements-tester.md | 140-199 | — | read $C\.claude\agents\qa-requirements-tester.md:140-199 | — |
| R7 | read | $C\.claude\agents\qa-doc-scribe.md | 1-39 целиком | — | read $C\.claude\agents\qa-doc-scribe.md:1-39 | — |
| R8 | read | $C\qa-factory\templates\questions-for-owner.md | целиком, 1-36 | — | read $C\qa-factory\templates\questions-for-owner.md:1-36 | — |
| R9 | read | $C\.claude\skills\qa-story\phases\f2a.md | 1-8 целиком | — | read $C\.claude\skills\qa-story\phases\f2a.md:1-8 | — |
| R10 | read | $C\.claude\skills\qa-story\phases\f8.md | 1-20 целиком | — | read $C\.claude\skills\qa-story\phases\f8.md:1-20 | — |
| R11 | read | $C\.claude\skills\qa-story\phases\f10.md | 1-28 целиком | — | read $C\.claude\skills\qa-story\phases\f10.md:1-28 | — |
| R12 | read | $C\.claude\agents\qa-runner.md | 1-60 | — | read $C\.claude\agents\qa-runner.md:1-60 | — |
| R13 | read | $C\qa-factory\strategy\common-rules.md | 1-120 | — | read $C\qa-factory\strategy\common-rules.md:1-120 | — |
| R14 | read | $C\qa-factory\docs\tester-mindset-plan.md | 170-219 | — | read $C\qa-factory\docs\tester-mindset-plan.md:170-219 | — |
| R15 | read | $C\.claude\agents\qa-case-critic.md | 11-24 | — | read $C\.claude\agents\qa-case-critic.md:11-24 | — |
| R16 | read | $C\README.md | 60-99 | — | read $C\README.md:60-99 | — |
| R17 | read | $C\qa-factory\templates\obligations.md | 1-11 | — | read $C\qa-factory\templates\obligations.md:1-11 | — |

## Not done
- Содержимое `qa-factory/checklists/**`, `adapters/README.md`, `exploratory-charters/README.md`, `federation.md` не читал. Они не про тест-план: в них слово checklist означает чек-листы аудита, а не план.
- `docs/test-factory-blueprint.html` и `docs/test-factory-cross-section.html` не читал (HTML-схемы, исключены из grep фильтром `glob=!*.html` в G5 и G6).
- В `.claude/agents/qa-doc-scribe.md:18` и `.claude/skills/qa-escape/SKILL.md:15` длинные совпавшие строки Grep пропустил («Omitted long matching line»). Первый файл прочитан целиком (R7), второй нет.
- `phases/f11.md`, `f12.md`, `f5.md`, `f1.md`, `f9.md`, `f8n.md`, `f2b.md`, `qa-onboarding/SKILL.md` (форма test-strategy.md) не читал. Для плана нужны только упомянутые в п.1.
- `grammar.py`, `config.json`, `exit_gate.py`, `check_witness.py`, `check_coverage.py` не читал, ссылаюсь на них по вызовам и комментариям в других файлах.
- Глобальный лимит строк плана не искал отдельным паттерном. Поиск `max_|лимит` шёл только по `validate_artifacts.py` (G11) и ничего про длину плана не дал. Поиск числовых лимитов по `.claude/**` не делал, поэтому «лимита нет» не утверждаю.
- G6 усечён head_limit 40: скриншотов в клоне больше, полный перечень не нужен для ответа.
- Окружение (выполнение хуков, работа фабрики вживую) — вне инструментов роли; всё выше относится к содержимому файлов.

## Analogs (rule 8, без расширения поиска)
- Шаблона PTR и intent-brief нет, хотя оба идут на гейты человека. Форма PTR задана только текстом роли `qa-doc-scribe.md:18`; форма intent-brief — одной фразой в `qa-requirements-tester.md:165`. Это тот же класс «шаблон артефакта живёт в тексте роли, а не в templates/», что и у тест-плана.
- `qa-factory/templates/obligations.md:1-11` задаёт правила файла тем же способом, что роли: правила и формат в одном файле шаблона.
