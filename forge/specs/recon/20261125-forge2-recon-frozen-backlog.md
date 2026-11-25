<!-- scout hand-back, journal task t-1896, recon for docs/tasks/specs/20261125-forge2-light-factory-plan.md; saved verbatim from the worker's final message -->

digest: v1 t-1888

Counting basis. Rows are `^\| B-` lines of `C:\QAFactory\forge-repo\plans\BACKLOG.md`. The file has 432 B-rows. There are no per-row status cells. Status is the section: open sections run from line 58 to 446, and "Закрыто" runs from line 448 to 587. The 18 theme counts below are rows that carry a marker string. They overlap and are not exclusive. I did not hand-assign rows. "Patch or design" is read from the sampled rows. Only the first 200-230 characters of most section 12 rows were read.

## Objects
| id | kind | gist | paths | status | owner | links | ev |
|---|---|---|---|---|---|---|---|
| A01 | carry-over | Every test gets a "check is live" receipt (probe_by_code); breaking the product only by critic's doubt [craft/outcome] | plans/BACKLOG.md:259 | decided | Решено 29.09: вариант C (D-01) | B-002 | t4,t9 |
| A02 | carry-over | Jira agent is not a data source; read by REST in lean format; agent only for writes [craft/means] | plans/BACKLOG.md:264 | decided | «(а) оставляем D-06 как есть, но проверяем, что никакие источники не теряем» 01.10 23:50 | D-06 | t4 |
| A03 | carry-over | Unknown stand build version is a question to the human, not a blocker; many ways to deploy [craft/outcome] | plans/BACKLOG.md:198 | decided | «автоматизация на uitest не должна блокироваться — неизвестно, как в проектах ставятся обновления на стенд, фабрика не ограничивается одним путём» 02.10 | B-257 | t14 |
| A04 | carry-over | One execution environment: the driver; test runs and real work must not differ [process/means] | plans/BACKLOG.md:200 | decided | «код тестовых прогонов и реальной работы не должен отличаться; оркестратора нет — есть дирижёр и драйвер» 02.10 | B-261 | t14 |
| A05 | carry-over | Factory runs as long as possible without bothering the human; stop only on human word or defect with a door [craft/outcome] | plans/BACKLOG.md:202 | decided | Владелец 02.10 13:50 (no quote) | B-264 | t14 |
| A06 | carry-over | Deliver with full report; third verdict: ready after human finishes checks (Left with you) [craft/outcome] | plans/BACKLOG.md:574 | decided | «доставляем; отчёт со всеми разделами, человек знает, что ему осталось допроверить» 02.10 12:50; verdict decision 14:00 | B-266 | t7 |
| A07 | carry-over | Restarting a stage of a closed story needs the human's word with reasons [craft/outcome] | plans/BACKLOG.md:560 | decided | «человеку обязательно нужно рассказать: вот из-за того-то нам нужны такие-то доработки; перезапустить стадию или оставить как есть? (человек может решить, что ему самому доделать проще)» 09.10 | B-331 | t7 |
| A08 | carry-over | Case-to-test form (fit column) is a hint; automator decides shape; checked: completeness and price [craft/outcome] | plans/BACKLOG.md:170 | decided | «снято владельцем (P17): `fit` — подсказка, форму решает автоматор» 30.09 | B-190,B-191 | t14 |
| A09 | carry-over | Ladder of verification ways: API, e2e, agent by hand, human, test written run elsewhere [craft/means] | plans/BACKLOG.md:179 | decided | Владелец 30.09, принцип P19 | B-227 | t14 |
| A10 | carry-over | Toolchain/reporter answer executed at onboarding (probe, propose, apply on approval); gate A is insurance [craft/means] | plans/BACKLOG.md:177 | decided | Решение владельца 03.10 | B-220 | t14 |
| A11 | carry-over | Onboarding finds project's own rules but asks human first; nothing pulled without confirmation [craft/outcome] | plans/BACKLOG.md:182 | open | Владелец, 01.10 | B-234 | t14 |
| A12 | carry-over | Fix a repeated rule in one place only; measure duplication [process/outcome] | plans/BACKLOG.md:239 | decided | «починим в одном месте, а в другом забудем» 04.10 | B-309 | t14 |
| A13 | carry-over | Dev system: critic gets only finished chunks, never unfinished work [process/means] | plans/BACKLOG.md:215 | open | Слово владельца 30.09 | B-202 | t14 |
| A14 | carry-over | Retro always full; the human's choice of retro removed [craft/outcome] | plans/BACKLOG.md:227 | decided | «ретро всегда полное» 03.10 | B-285 | t14 |
| A15 | carry-over | On any resume of the same task, check whether source data changed [craft/outcome] | plans/BACKLOG.md:531 | decided | «при любом возобновлении по той же задаче проверяем, изменились ли исходные данные» 02.10 | B-259,B-364 | t7 |
| A16 | carry-over | Manual route (no automation) first-class; not before comparison run [craft/outcome] | plans/BACKLOG.md:79 | open | решение владельца 29.09: не до сравнительного прогона | B-006 | t3 |
| A17 | carry-over | Baseline "before": think through all scenarios; not before release, does not block [craft/outcome] | plans/BACKLOG.md:206 | open | «продумать все сценарии, когда нужен бейзлайн, и как его получить» 02.10 16:20; «до релиза не делаем» 17:25 | B-269 | t14 |
| A18 | carry-over | Stand-gap answer carried from gate A to gate B; asked again only on change [craft/outcome] | plans/BACKLOG.md:391 | decided | Слово владельца — D-0026 (06.10) | B-361 | t7 |
| A19 | carry-over | Unreadable test report not shown to human first; code tries all readers; test places are project word [craft/outcome] | plans/BACKLOG.md:406-408 | decided | владелец 06.10.2026 (D-0029, D-0030, D-0031) | B-414,B-415,B-416 | t16 |
| A20 | carry-over | Owner principles P1-P15 (code helps the role; universality; human words pass any gate; failure says what is expected) | plans/BACKLOG.md:31-37 | decided | Принципы владельца (full text in project CLAUDE.md, not read) | B-051 | t2 |
| A21 | carry-over | Technical data of the factory deleted on reinstall; task data stays; unknown to retired/<date> [craft/means] | plans/BACKLOG.md:512 | decided | Решения владельца 01.10 14:00 | B-233 | t7 |
| A22 | carry-over | Dashboard accumulates; old artifacts visible on a copy are not a defect; per-agent and per-stage tabs wanted [craft/outcome] | plans/BACKLOG.md:106-107,167 | open | идея владельца, 29.09; Владелец 30.09 | B-084,B-085,B-187 | t3,t14 |
| TH01 | theme | Same rule/reader copied in many places (twins); 71 rows with FR-17 or "близнец"; closed by patch plus ratchet tool | plans/BACKLOG.md:239 | open | — | B-309,B-405,B-427,B-437,B-447 | t21 |
| TH02 | theme | One language/tool/project hardcoded (pytest, ticket-key form, glab, build-sha path); 67 rows P2/FR-12/FR-13; part design (to data) | plans/BACKLOG.md:113,399 | open | — | B-090,B-337,B-404,B-406,B-407 | t22 |
| TH03 | theme | Unknown or unverified read as pass or silent None; 45 rows FR-41; gate-by-gate patch with debt_ref | plans/BACKLOG.md:218-223 | open | — | B-173,B-278,B-279,B-282,B-283 | t24 |
| TH04 | theme | Raw script names, flags, ids shown to human; 33 rows FR-6/P9; per-text patches | plans/BACKLOG.md:156,233 | open | — | B-061,B-122,B-171,B-292,B-414 | t23 |
| TH05 | theme | Absolute paths and state layout literal in code; 31 rows FR-37/FR-15/A20; patch plus census | plans/BACKLOG.md:212,195 | open | — | B-166,B-249,B-251,B-275,B-298 | t25 |
| TH06 | theme | LLM calls/context spent where code suffices; 39 rows P6/FR-51; mix, B-274 moves work to code | plans/BACKLOG.md:95-106 | open | — | B-020,B-070,B-073,B-237,B-274 | t26 |
| TH07 | theme | Human word not honoured at a gate, or asked again; 49 rows P13/FR-4/FR-57; patches (waivers, exact match) | plans/BACKLOG.md:199,289 | open | — | B-004,B-131,B-258,B-343,B-361 | t27 |
| TH08 | theme | Test suite slow or flaky under load, timeouts raised, files split; 29 rows FR-31; patch | plans/BACKLOG.md:238,334 | open | — | B-082,B-214,B-297,B-326,B-460 | t28 |
| TH09 | theme | Liveness, stale revision, locks, projection staleness; 37 rows; patches one case at a time | plans/BACKLOG.md:77,205 | open | — | B-048,B-268,B-311,B-330,B-366 | t29 |
| TH10 | theme | Measurers and metrics wrong, hardcoded or showing 0 for unknown; 65 rows FR-24..28/P11; patch | plans/BACKLOG.md:136-139 | open | — | B-138,B-140,B-141,B-162,B-173 | t30 |
| TH11 | theme | Test proves nothing (check cannot tell good from broken product); 25 rows FR-18; design D-01 plus tails | plans/BACKLOG.md:166,174 | open | — | B-002,B-185,B-217,B-218,B-337 | t31 |
| TH12 | theme | Stand identity, login, build version, baseline; 25 rows "стенд"; B-257 ladder is design, rest patches | plans/BACKLOG.md:196-198 | open | — | B-145,B-252,B-257,B-269,B-414 | t32 |
| TH13 | theme | Guards and hooks block wrongly or miss bypasses; 61 rows guard/гард/хук; patch | plans/BACKLOG.md:173,352,396 | open | — | B-126,B-200,B-349,B-404,B-433 | t33 |
| TH14 | theme | Windows, CRLF, console encoding, 8.3 paths; 22 rows; patch | plans/BACKLOG.md:401,405 | open | — | B-326,B-378,B-386,B-409,B-413 | t34 |
| TH15 | theme | Handoff forms between roles missing, dead or unchecked; 24 rows FR-49/FR-11/FR-5; patch | plans/BACKLOG.md:165,228 | open | — | B-161,B-183,B-218,B-284,B-286 | t35 |
| TH16 | theme | Manual and baseline route not first-class; 19 rows; open, design deferred | plans/BACKLOG.md:79,206 | open | — | B-006,B-170,B-182,B-269,B-288 | t36 |
| TH17 | theme | Closed row leaves remainders; critics add new rows (B-421..B-453); 50 rows "остатки"; patch chain | plans/BACKLOG.md:413-446 | open | — | B-421,B-423,B-424,B-438,B-453 | t38 |
| TH18 | theme | Facts written without a read: 20 rows "needs a read: could not tell"; and decisions credited to owner but made by branch author (D-0025) | plans/BACKLOG.md:391-392 | open | — | B-123,B-173,B-236,B-361,B-373 | t37 |
| M01 | missing | Live acceptance of Android/iOS adapters, playwright-cli install, OS/host matrix, multi-repo wrong base | plans/BACKLOG.md:130 | open | — | B-104 | t3 |
| M02 | missing | Automation layer not tied to pytest (adapter_id, test_marker) | plans/BACKLOG.md:113 | open | — | B-090 | t3 |
| M03 | missing | "Check is live" for non-Python tests; JUnit failure site unreadable for Jest/Java/.NET | plans/BACKLOG.md:344,392 | open | — | B-337,B-373 | t15,t16 |
| M04 | missing | Non-pytest run: node id vs rootdir, runner guard knows only pytest | plans/BACKLOG.md:349,396 | open | — | B-345,B-404 | t15 |
| M05 | missing | Run on unknown project without onboarding | plans/BACKLOG.md:115 | open | — | B-092 | t3 |
| M06 | missing | Export of cases in project's own format after gate B (cases_export) | plans/BACKLOG.md:117 | open | — | B-094 | t3 |
| M07 | missing | Build as witness: probe.build, no commit on red build | plans/BACKLOG.md:116 | open | — | B-093 | t3 |
| M08 | missing | Several stories at once in one project (branch/worktree per story) | plans/BACKLOG.md:120 | open | — | B-097 | t3 |
| M09 | missing | Preparatory-story mode (no implementation yet), asked at gate A | plans/BACKLOG.md:89 | open | — | B-064 | t3 |
| M10 | missing | Monorepo: project in git subfolder, nested red-probe sandbox | plans/BACKLOG.md:329,404 | open | — | B-412,B-321 | t16,t17 |
| M11 | missing | Ticket key forms beyond Jira letters-dash-digits; delivery only glab/gh | plans/BACKLOG.md:397-398 | open | — | B-405,B-406 | t15 |
| M12 | missing | CI-triggered run with per-story concurrency; second-run lock and label | plans/BACKLOG.md:186,191 | open | — | B-244,B-239 | t13 |
| M13 | missing | Jira wiki markup on write; attachment/image policy; VCS auth-loss twin | plans/BACKLOG.md:188,187,192 | open | — | B-241,B-240,B-246 | t13,t14 |
| M14 | missing | Project-to-team report skill; weekly cross-project analytics (deferred); KB publication by REST | plans/BACKLOG.md:180,131,190 | open | — | B-229,B-105,B-243 | t13,t3 |
| M15 | missing | Human manual verification producer (run-report.manual_human has no writer) | plans/BACKLOG.md:230 | open | — | B-288 | t13 |
| M16 | missing | Codex host: native context and liveness remainders | plans/BACKLOG.md:333,342 | open | — | B-325,B-335 | t17,t15 |
| M17 | missing | Unbuilt jev judgments (only if enabled): ticket_degenerate, PII and others | plans/BACKLOG.md:251-253 | open | — | B-110,B-111,B-112 | t4 |
| M18 | missing | No row asks for TestRail, Xray, Allure, Zephyr or Qase export; Android appears only in B-104 | plans/BACKLOG.md:1-587 | absent | — | — | t19 |
| S01 | structure | 432 B-rows; closed section holds 136 (lines 452-587); open sections hold 296; plus 6 D-rows | plans/BACKLOG.md:452-587 | open | — | — | t6,t11 |
| S02 | structure | Header says open=343 closed=84 as of 08.10; closed grew by 52 since (B-row count: 136 vs 84) | plans/BACKLOG.md:3 | open | — | S01 | t2,t11 |
| S03 | structure | 132 rows carry the word "закрыто", 131 carry a closed marker phrase; no status column, no row says "no status" | plans/BACKLOG.md:450 | open | — | S01 | t10,t12 |
| E01 | open-question | D-02 managing-layer threshold 0.35, D-03 cost target, D-04 data to api.typesafe.ai, D-05 component tests in UI repo: no answer | plans/BACKLOG.md:260-263 | open | — | — | t4 |
| E02 | open-question | Test-path marker list (`__test__`, `testing`, `integration`) "decision with owner"; B-415 says it is project's word | plans/BACKLOG.md:355,407 | open | — | B-355,B-415 | t15,t16 |
| E03 | open-question | What may leave a project in a factory report (secrets, product data) "decides owner" | plans/BACKLOG.md:180 | open | — | B-229 | t13 |
| E04 | open-question | Whether a "waiting" label may be set in Jira (needs owner word) | plans/BACKLOG.md:186 | open | — | B-239 | t13 |
| E05 | open-question | Owner decision R-2 Q10 (live check without novelty key) not recorded | plans/BACKLOG.md:219 | open | — | B-279 | t14 |
| E06 | open-question | Which platforms and trackers are in scope (Android/iOS, GitHub/Azure ids, Jira Automation trigger) | plans/BACKLOG.md:130,191,397 | open | — | B-104,B-244,B-405 | t13,t15 |
| E07 | open-question | Which past "owner decisions" were the branch author's; only some re-opened (D-0025 to D-0028) | plans/BACKLOG.md:391-392,407 | open | — | B-361,B-373,B-415 | t7,t16 |
| E08 | open-question | Is the stage set S0-S9, the 12 roles, and gates A/B kept; the file does not say | plans/BACKLOG.md:41-447 | open | — | — | t1 |
| E09 | open-question | Baseline scenarios A-F and the ladder of obtaining "before" (post-release, designer after a manual experiment) | plans/BACKLOG.md:206 | open | — | B-269 | t14 |
| E10 | open-question | Team: 2-3 developers; GitLab version unverified; forks of team plan wait owner word | plans/BACKLOG.md:544 | open | — | B-230 | t7 |
| AN01 | analog | Decisions in the file cite D-0010, D-0017, D-0018, D-0025..D-0033; the decision register is not in this file and not read | plans/BACKLOG.md:141,391-392 | open | — | TH18 | t7 |

## Trail
| tid | op | target | pattern / range | flags | result | control |
|---|---|---|---|---|---|---|
| t1 | grep | plans/BACKLOG.md | `^#{1,3} ` | — | found 16; plans/BACKLOG.md:1,22,41,49,54,68,82,91,109,122,247,255,266,297,303,448 | — |
| t2 | read | plans/BACKLOG.md | 1-40 | — | read plans/BACKLOG.md:1-40 | — |
| t3 | read | plans/BACKLOG.md | 41-130 | — | read plans/BACKLOG.md:41-130 | — |
| t4 | read | plans/BACKLOG.md | 247-302 | — | read plans/BACKLOG.md:247-302 | — |
| t5 | grep | plans/BACKLOG.md | `владел\|слово человека\|«.{3,200}»` | -i count | count 300 | — |
| t6 | grep | plans/BACKLOG.md | `^\| B-\d+ ` | count | count 432 | — |
| t7 | grep | plans/BACKLOG.md | `.{0,160}(владельц\|«[^»]{0,40}владел\|слово владельца\|идея владельца\|по слову).{0,260}` | -i content | found 81; plans/BACKLOG.md:107,131,141,531,560 | — |
| t8 | read | plans/BACKLOG.md | 303-314 | — | read plans/BACKLOG.md:303-314 | — |
| t9 | read | plans/BACKLOG.md | 448-455 | — | read plans/BACKLOG.md:448-455 | — |
| t10 | grep | plans/BACKLOG.md | `^\| B-\d+ .*закрыто ` | -i count | count 132 | — |
| t11 | grep | plans/BACKLOG.md | `^\| B-\d+ ` (offset 290, head 142; closed ids) | content | found 142; plans/BACKLOG.md:441,452,587 | — |
| t12 | grep | plans/BACKLOG.md | `закрыто (кодом\|\d\|по слову\|пачкой)\|closed by code` | -i count | count 131 | — |
| t13 | read | plans/BACKLOG.md | 131-188 | — | read plans/BACKLOG.md:131-188 | — |
| t14 | read | plans/BACKLOG.md | 189-246 | — | read plans/BACKLOG.md:189-246 | — |
| t15 | grep | plans/BACKLOG.md | `^\| B-\d+ \| .{0,230}` (offset 196, head 100) | content | found 100; plans/BACKLOG.md:338,446 | — |
| t16 | read | plans/BACKLOG.md | 399-408 | — | read plans/BACKLOG.md:399-408 | — |
| t17 | grep | plans/BACKLOG.md | `^\| B-3(1[1-9]\|2\d) \| .{0,200}` | content | found 19; plans/BACKLOG.md:316,337,514 | — |
| t18 | grep | plans/BACKLOG.md | `.{0,90}(не-pytest\|не-Python\|android\|\bios\b\|testrail\|xray\|allure\|azure devops\|монорепо\|нагрузочн\|accessib\|a11y\|visual diff\|кросс-?проектн\|Codex).{0,110}` | -i content | found 33; plans/BACKLOG.md:130,131,344 | — |
| t19 | grep | plans/BACKLOG.md | `testrail\|xray\|allure\|zephyr\|qase` | -i count | count 0 | t20 |
| t20 | grep | plans/BACKLOG.md | `android\|playwright\|cases_export` | -i count | count 4 | — |
| t21 | grep | plans/BACKLOG.md | `^\| B-\d+ .*(FR-17\|близнец)` | count | count 71 | — |
| t22 | grep | plans/BACKLOG.md | `^\| B-\d+ .*(P2\b\|FR-13\|FR-12)` | count | count 67 | — |
| t23 | grep | plans/BACKLOG.md | `^\| B-\d+ .*(FR-6\b\|P9\b)` | count | count 33 | — |
| t24 | grep | plans/BACKLOG.md | `^\| B-\d+ .*FR-41` | count | count 45 | — |
| t25 | grep | plans/BACKLOG.md | `^\| B-\d+ .*(FR-37\|FR-15\|A20)` | count | count 31 | — |
| t26 | grep | plans/BACKLOG.md | `^\| B-\d+ .*(P6\b\|FR-51)` | count | count 39 | — |
| t27 | grep | plans/BACKLOG.md | `^\| B-\d+ .*(P13\|FR-4\b\|FR-57)` | count | count 49 | — |
| t28 | grep | plans/BACKLOG.md | `^\| B-\d+ .*FR-31` | count | count 29 | — |
| t29 | grep | plans/BACKLOG.md | `^\| B-\d+ .*(FR-40\|FR-42\|живост)` | -i count | count 37 | — |
| t30 | grep | plans/BACKLOG.md | `^\| B-\d+ .*(FR-28\|FR-24\|FR-25\|FR-26\|P11\b)` | count | count 65 | — |
| t31 | grep | plans/BACKLOG.md | `^\| B-\d+ .*FR-18` | count | count 25 | — |
| t32 | grep | plans/BACKLOG.md | `^\| B-\d+ .*стенд` | -i count | count 25 | — |
| t33 | grep | plans/BACKLOG.md | `^\| B-\d+ .*(guard\|гард\|хук)` | -i count | count 61 | — |
| t34 | grep | plans/BACKLOG.md | `^\| B-\d+ .*(Windows\|CRLF\|кодировк)` | -i count | count 22 | — |
| t35 | grep | plans/BACKLOG.md | `^\| B-\d+ .*(FR-49\|FR-11\b\|FR-5\b)` | count | count 24 | — |
| t36 | grep | plans/BACKLOG.md | `^\| B-\d+ .*(бейзлайн\|ручн)` | -i count | count 19 | — |
| t37 | grep | plans/BACKLOG.md | `^\| B-\d+ .*needs a read: could not tell` | count | count 20 | — |
| t38 | grep | plans/BACKLOG.md | `^\| B-\d+ .*(остатки\|остаток\|остались)` | -i count | count 50 | — |

## Forks
- Whether a rebuilt factory keeps the section-9 decisions made before the D-0025 reopening is not stated in the file.
- The file's own frozen notice (lines 5-10) says it is archive-only, and the open rows live in `plans/piles/<slug>/`. That folder was not read, so row statuses may have moved since 08.10.

this needs a decision from a tier above.

## Not done
- Section-by-section coverage (every heading is listed):
  - Header, lines 1-40: read fully.
  - Sections 0 and 1 (lines 41-53): read fully. Both tables are empty.
  - Sections 2-6 (lines 54-121): read fully.
  - Section 7 (lines 122-246): read fully.
  - Sections 8-11 (lines 247-302): read fully.
  - Section 12 (lines 303-447): lines 303-314 read fully, and lines 399-408 read in full.
    - Rows B-311 to B-329 (lines 316-337) and the other section 12 rows (lines 338-446, 100 rows): read only the first 200-230 characters by grep. About 118 rows were sampled this way, plus 10 read in full.
    - Lines 409-412 not read.
  - "Закрыто" (lines 448-587): 4 rows read fully (B-001 to B-004), and all 136 ids listed.
    - About 45 further rows were seen only as owner-word fragments from t7.
    - The other 85 or so were not read. Reason: they are closed, and the owner words in them were taken by grep.
- Not checked:
  - `plans/piles/`, the decision register (D-0010, D-0017, D-0018, D-0025 to D-0033), the project CLAUDE.md that holds the full principle texts, and the P16-P21 texts. Reason: outside the given file.
  - Whether open rows were closed after 08.10 elsewhere.
- Theme counts are marker proxies. Rows can sit in several themes, and the 18 counts sum to more than 432.
- Environment checks (live state of piles, CI) are outside this role's tools — a tier with Bash is needed.
