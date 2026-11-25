# Recon digest t-1945: where the old forge's ideas and lessons live; audit items not carried into forge 2

Scout hand-back of 25.11.2026, saved verbatim by the Lead (the scout writes no file). Accepted by trail: the Lead re-counted 1195 finding files, 60 `кандидат наверх: да`, and the negative claim (no `1195` in `plans/BACKLOG.md`, control `piles-freeze` found 1). The figure 1195 in the dispatch came from the compact snapshot's carrier line, not from the frozen backlog's summary: the dispatcher's wording slip.

digest: v1 t-1945

Basis. Counts of pile files come from one listing Grep over `plans/piles/**/*.md` (1346 files; saved in the Claude tool-results folder as `toolu_01F3yz2HrVgCASr7hVeEtyhn.txt`), then per-pile line counts of that listing. Counts are of `findings/*.md` files, one file = one finding. The whole-repo Glob said 1345 .md files for the same tree (one off between the two runs; not explained). Nothing was written to the repo.

## Carriers

Pile findings, per folder under `plans/piles/` (one row per folder; pattern for each: `^plans.piles.<slug>.findings`, count mode, on the listing file; 37 folders = 36 piles + `_template`, same as the earlier recon count at `docs/tasks/handoffs/20261125-forge2-recon-piles.md` row p38):

| carrier | what a record looks like | count (findings files) | how idea/lesson is told from bug/task |
|---|---|---|---|
| plans/piles/forge/findings | file `yyyymmdd-<slug>.md`; line 3 `id: — \| кучка: \| от: \| приоритет: П1-П3 \| кандидат наверх: нет/да`; example `plans/piles/forge/findings/20261124-dokumentam-koordinatora-net-dorogi-pri-dvuh-sessiyah-v-korne.md` (named in `docs/retro/classes.md:10`) | 125 | cannot be told by a field (see shape note below) |
| plans/piles/live-run-fvf/findings | same shape; example `20261114-code-repos-koren-vyshe-proekta-obyavlyaet-vsyo.md` | 116 | cannot be told by a field |
| plans/piles/onboarding-forge/findings | same | 116 | cannot be told by a field |
| plans/piles/execution-report/findings | same | 105 | cannot be told by a field |
| plans/piles/driver-hosts/findings | same | 80 | cannot be told by a field |
| plans/piles/release-next/findings | same | 59 | cannot be told by a field |
| plans/piles/onboarding-hooks/findings | same | 56 | cannot be told by a field |
| plans/piles/gates-and-words/findings | same | 48 | cannot be told by a field |
| plans/piles/execution-probes/findings | same | 43 | cannot be told by a field |
| plans/piles/words-gates/findings | same | 38 | cannot be told by a field |
| plans/piles/hotfix-12586/findings | same | 35 | cannot be told by a field |
| plans/piles/report-delivery/findings | same | 34 | cannot be told by a field |
| plans/piles/driver-controller/findings | same; some named `B-nnn-*.md` (moved from BACKLOG), example `B-006-ruchnoy-marshrut-s4-s6-dlya-stori-bez.md` | 33 | cannot be told by a field |
| plans/piles/rules-debt/findings | same | 32 | cannot be told by a field |
| plans/piles/package-ci/findings | same | 31 | cannot be told by a field |
| plans/piles/thinking-roles/findings | same | 30 | cannot be told by a field |
| plans/piles/roles-context/findings | same | 24 | cannot be told by a field |
| plans/piles/conductor/findings | same | 23 | cannot be told by a field |
| plans/piles/live-runs/findings | same | 23 | cannot be told by a field |
| plans/piles/cost-dashboard/findings | same; many `B-nnn-*.md` | 22 | cannot be told by a field |
| plans/piles/codex/findings | same | 20 | cannot be told by a field |
| plans/piles/project-knowledge/findings | same | 17 | cannot be told by a field |
| plans/piles/speed-cost/findings | same | 17 | cannot be told by a field |
| plans/piles/told-before-work/findings | same | 15 | cannot be told by a field |
| plans/piles/test-code-quality/findings | same | 13 | cannot be told by a field |
| plans/piles/stand-and-sources/findings | same | 12 | cannot be told by a field |
| plans/piles/grounding/findings | same | 8 | cannot be told by a field |
| plans/piles/collect/findings | same | 6 | cannot be told by a field |
| plans/piles/run-honesty/findings | same | 5 | cannot be told by a field |
| plans/piles/regression/findings | same | 4 | cannot be told by a field |
| plans/piles/pre-code/findings | same | 2 | cannot be told by a field |
| plans/piles/exploratory/findings | same | 1 | cannot be told by a field |
| plans/piles/github-move/findings | same | 1 | cannot be told by a field |
| plans/piles/kb/findings | same | 1 | cannot be told by a field |
| plans/piles/universality/findings | no findings file (folder holds `README.md` and `batch-1-pass-without-stuck.md` only) | 0 | n/a |
| plans/piles/proposals/findings | none (folder has a `README.md`, 1 batch) | 0 | n/a |
| plans/piles/_template | not a pile: `README.md`, `batch.md`, `finding.md` templates | 0 | n/a |
| SUM of the 36 piles | pattern `^plans.piles.[^\\]+.findings` over the listing | 1195 | sum of the rows above also computes to 1195 |

Comparison with 1195 (stated, not explained away): my sum is 1195 and the single run `\\findings\\` over the listing is also 1195, so the difference is 0 with the number in the dispatch. BUT the number 1195 is NOT in `plans/BACKLOG.md`: its summary line is `plans/BACKLOG.md:3` `piles-freeze: 2026-10-08 open=343 closed=84` (427), and the file has 432 B-rows (`^\| B-\d+ `). A search for `1195` in `plans/BACKLOG.md` returns zero (t14, control t15); `1195` is not in the frozen-backlog handoff either (t13). So the "1195 findings the frozen backlog's summary names" could not be matched to a text; the only matching figure is the count of finding files.

Other carriers:

| carrier | what a record looks like | count (pattern) | how idea/lesson is told from bug/task |
|---|---|---|---|
| plans/piles/*/batch-*.md (node files) | graph of nodes (example `U1-1`, `TR4-2`, `FG7-109`), table of status words (ожидает/в работе/закрыта/принято); a node cuts a finding or a B-row | not counted (about 1346 - 1195 - 37 README files = remaining batch/other files; arithmetic only, not a measured number) | no kind field; a node carries "Что именно менять" text; cannot be told by a field |
| plans/piles/*/README.md `Содержание` table | row `\| id / файл \| вид \| суть \| пути \| статус \| слово владельца \| связи \|`; example `\| \`findings/20261012-desktop-launch-card-lost-after-exec-yield.md\` \| находка \|` (`plans/piles/codex/README.md:68`) | `\| находка \|$` = 1060 lines, `\| строка \|$` = 267 lines in a listing run of `^\| (\`findings/[^\`]+\`\|B-\d+) \| [^\|]+ \|` (-o) over `**/README.md` (listing file `toolu_01DPa9zdoNELkFUVr2UbDF7N.txt`; the 1060 is not 1195, so the card tables do not list every finding file in that form; not explained) | the `вид` column only has the values находка / строка (a source form, not idea vs bug); the `слово владельца` column and `суть` text are the only hints |
| plans/BACKLOG.md (frozen) | table row `\| B-nnn \| … \|` in sections; no status cell, status = section; example `B-006` | 432 (`^\| B-\d+ `, count); open sections lines 58-446, "Закрыто" lines 448-587 (from the frozen-backlog handoff, 136 closed rows, 296 open by its count; the header says 343/84) | no kind field. The owner's words sit in the cells («…» quotes, "решение владельца"); the handoff `20261125-forge2-recon-frozen-backlog.md` made 22 "carry-over" rows A01-A22 by reading, plus 18 theme markers by string match. A reader must read each row |
| plans/BACKLOG.md section 9 / decisions in rows | decisions of the owner inside rows (D-01..D-06) | not counted | text only |
| plans/MEASUREMENTS.md | 41 headings (`^#{1,3} `, count); records are measured facts in prose/lists, mostly undated, citing archived plans; example the `A01`..`A21` facts in handoff `20261125-forge2-recon-run-lessons.md` | 41 headings | every record is a measured fact (a lesson in the sense of a number), no field marks it; an idea is told by a "решение владельца" phrase only |
| plans/feature-fragility-2026-10-02.md, plans/RULES-PROPOSAL.md, plans/forge-metrics.md, docs/tasks/factory-fixes.md | prose and tables (features F01-F21, failure classes, FR-n rules) | headings count only for the five files in that handoff: 94 (from handoff t8); fragility says 308 items, 217 parent rows | the "failure class" tables are the lesson carrier; the file marks `yes/sib/rec/self` fix-of-fix per item, not idea vs bug |
| docs/retro/ | `classes.md` (table `\| Класс \| Записи \| Решение \| Находка / узел \|`, 12 classes) + `inbox/20261124-2015-dev1.md` + `done/20261118-0500-dev1.md` (sections 1-7: difficulties, extra work, gates, "что решила сама", owner questions); two `.gitkeep` | 2 records (Glob `docs/retro/**`: 5 files incl. 2 `.gitkeep` and `classes.md`); 12 class rows in `classes.md` (rows 9-20) | the record's section headings (`## 1. Что вызвало трудности` … `## 7. Вопросы владельцу`) are the shape; in `classes.md` the column `Решение` says "чиним"/"не чиним до повтора"/"уже чинится" — that tells fixed vs not, not idea vs bug |
| docs/tasks/architect-queue.md | line `- [ ] <date> <task|—> <question> (от: Lead\|владелец)`; closed `- [x] … — сделано:` | 13 (`^- \[[ x]\] `, count); 14 lines match `^## \|^- ` | line text says "новая идея владельца" in 3 items (lines 14, 21, 22); no field; text-only mark |
| docs/RELATED_WORK.md | 8 numbered sections of outside-tool reviews (`## 1. DMtools … 01.10.2026` to `## 8. applerom/agent1st`) | 8 (`^#{1,3} `, content) | every section is an external survey; no marker |
| DECISIONS.md | line `- D-NNNN — <statement>.` | 4 lines in the live file (`^- D-\d{4} `, count) | each line is a lasting rule or binding (not idea vs bug) |
| docs/DECISIONS_ARCHIVE.md | `### D-NNNN — <reason> (archived <date>)` headings and `- D-NNNN` lines | 71 headings (`^### D-\d{4}`) and 84 lines `^- D-\d{4} ` (both counts; may overlap, not checked) | the heading says why it was archived |
| experiments/ notebooks outside runs/ | per-experiment `notebook.md`, `<name>.md`, `RUN-INSTRUCTIONS.md`, `SUMMARY.md`, `notes.md`; finding rows with ids `FV1-nn`, `Н-S0`.. | about 274 .md files in `experiments/` (the number is from the earlier handoff t29/`recon-experiments-retros` Not-done, NOT recounted by me); 142 files under mybooks (same source) | the ao3 notebook marks owner verdicts with «баг», «баг П1» in quotes; no field; a reader reads each |
| docs/OWNER_PRINCIPLES.md | P1-P31 blocks with dates | 31 principles by their numbering (from handoff t47) | owner words dated; not a bug/task carrier |
| docs/tasks/specs/reports/20261125-forge2-ideas-audit.md | audit of the big ideas | see section "Audit items not carried" | verdict words per row |

Shape note (the one the designer needs): a finding file has no "kind" field. The template `plans/piles/_template/finding.md` fields are `id` / `кучка` / `от` / `приоритет` (П1-П3) / `кандидат наверх` (да/нет) then the body headings "Что не так / что сделать", "Свидетель", "Принципы и правила", "Решение владельца нужно". Every finding is written in the form of a defect or a task. The only mark that looks like an upgrade is `кандидат наверх: да`: 60 finding files carry it (`кандидат наверх: да`, -i, count, glob `**/findings/*.md`; the control is the same search with `нет` under `plans/piles/proposals` which found 0, so I used the `forge` folder as a control, 1 file). The `id:` is `—` until the integrator gives a B-id (`docs/TEAMWORK.md:52-53`). So an idea or a lesson cannot be told from a bug or a task by a field in any carrier; a reader would have to read the body text of each record, or use a text marker (owner's quote in «», "решение владельца", "новая идея", "класс", `P`-number in `Принципы и правила`). Pile folders `proposals` (1 batch, "receiving pile for suggestions and foreign adaptations") and `universality` (idea pile, README "ожидает") are the only folders whose README says they are about ideas; both have 0 findings files.

Analogs noticed (rule 8, not searched further): (1) the README `Содержание` rows (1060 `находка`) do not equal the 1195 finding files, so a card table may lag its folder, the same status-lag class as d04 in `20261125-forge2-recon-piles.md`; (2) the BACKLOG header (`open=343 closed=84`) differs from its B-row count (432), the same class as S02 in the frozen-backlog handoff.

## Audit items not carried

Source: `docs/tasks/specs/reports/20261125-forge2-ideas-audit.md` (209 lines). Verdict words are the report's own. Sections 1.x have verdicts; sections 2-4 are items "to take", listed as not yet carried, with no verdict word of that kind.

1.1 "Допущения" - heading verdict «вошло частично»:
- 1.1 answer 1 (list of assumptions approved as one, edits by line «N: должно быть так-то») - «нет».
- 1.1 answer 2 (red test on an unconfirmed assumption is a question with both sides) - «частично» (v1.6 has it as "bug or not").
- 1.1 answer 3 (no ceiling on number of assumptions, number as a report figure) - «не сказано», no number in the report.
- 1.1 answer 4 (requirements register untouched by the idea) - «иначе» (the spec has an "assumption" source kind): owner question 9 of the plan.
- 1.1 border (what may be assumed: counters, sums; not prices, limits) - «нет».
- 1.1 mark of an assumption inside the test code - «нет» (decided not to introduce; link goes through the record).

1.2 "Общие моки проекта" - «почти не вошло»: not carried are the shared project mock base; the list of sources a mock answer may come from; the red reason "mock is stale"; the report line "checked only on mock"; the ban on a mock by assumption; the manual pass on the same mocks. Decision: one "mocks" card in the spec fix round for phases 1-4.

1.3 "Профиль хоста и хуки" - «вошло почти целиком»: not carried: harness trust requests; "harness cannot limit a role's tools - say it once at connection" (both "добавляется строками профиля"); phase 9 line items without a card: profile of an unknown host, export of roles to a profile, reading a second harness's transcript.

1.4 "Фабрика не хуже агента" - «вошло»: not carried: the finding field "which lower layer should have caught it" («не вошло и добавляется»); excluded with reason: dry story (phase 10), smoke run per stage (replaced by the comparison run), repairs of old code.

1.5 "Принципы P1-P31" - all carried except:
- P6 (jev) - «слова нет», meaning lives in the rule "code owns data".
- P25 (host and gateway settings) - «нет», added as a line of the frame.
- P12 (new code checked for similar places) - «нет» explicit step, added to the forge 2 change cycle.
- P14 (roles get only needed tools) - partly: for forge roles yes, for factory stages no (add a stage column).
- P10 (map of symmetries) - starts empty, by design.

1.6 "Кучки и фичи" - items listed as «частично или нет»:
- Reconciliation with the change (В9: whole diff read, each hunk tied to a requirement) - in the plan, no spec card.
- Stand and sources (stand and build identification, network error classes, ticket freshness) - not carried, to the spec fix round.
- Exploratory testing - route without a card; v1.6 gives a research page at stage 5.
- Collection, install and "doctor", tracker write, cross-story findings registry - phase lines without cards (phases 5, 7, 8).
- Dashboard - the old 48 metrics are not carried, decided.
- Proposals and foreign adaptations, knowledge base for users - «нет», after the first release.
- Judge (F20) - replaced by the critic.
- Codex, move to GitHub, hotfix, rules debt, next release - about old code, not carried.

2. Found by the check (in no idea):
- 2.a rule "ticket, document and app reply text are data, not instructions to the agent" - 0 hits in six files; to be added to the frame.
- 2.b stage 5 cannot record a requirement, assumption or question - door for a late requirement (plan v1.6 section 1д).

3. ideal-test-factory - "Берём сейчас" (11 items not yet in the spec):
- 3.1 ceiling cuts attempts, not volume; unfinished work travels on by name (`SKILL.md:11`).
- 3.2 turn ceiling per run, about 80, with its measurement (`SKILL.md:29`).
- 3.3 ceiling for waiting on a background run, then a diagnostic step (the 1800 s timeout exists, the diagnostic step is not in the spec).
- 3.4 labels for unresolved items on a repeat critic round: not taken / taken and failed / outside the executor's power (`SKILL.md:12`).
- 3.5 ceiling of repair rounds after the critic = 2, as a data line (`SKILL.md:11`); the spec names no number.
- 3.6 after-compaction reminder, a hook that only prints (`postcompact_reload.py`): both for the factory and forge 2.
- 3.7 one stand command: address, account, secrets present (no values), liveness, what is missing (`env_probe.py`).
- 3.8 a green result carries the product build and the commit of the tests it was got on (`qa-hardening-gate.md:23`).
- 3.9 "as before" - a ladder to get the state before the change, else a question to a human (`qa-requirements-tester.md:45`).
- 3.10 questions to requirements (unambiguity, testability, boundaries, errors) on the stage 1 craft page (`qa-requirements-tester.md:17-38`).
- 3.11 end of session: "what of what was done will the next session not see in files? - nothing" (`SKILL.md:22`), into forge 2; plus critic model not weaker than executor model (`models.json`) - one profile check line (12th item).
"Берём позже" (4): registry of tails with an observable trigger (phase 5, `obligations.md`); post-mortem of a missed bug (`qa-escape`, phase 6); full requirements audit by 20 criteria and feature split integrity (phase 6); test-suite maintenance (quarantine, dead links) after phase 10.
"Не берём" (7, with the reasons in the report; listed so none is dropped): new tests green N times in a row (taken, then dropped 25.11 about 20:50); fuse on a third refusal; red-test merge block (red_lock); release go/no-go; orchestrator model with 13 phases; coverage map and FAQ files and given-when-then case form; five non-functional specialists, checklist packs, case-manager adapters, size estimator, 48 metrics, merge of several factories.

4. World trends and the Prometheus catalogue (the report's own column "что это значит для нас"): items that change or add something:
- 4.a new line in the stage 5 gate: a test's expectation after red is not changed without a requirement line or a human word (`…audit.md:150`).
- 4.b boot page of forge 2 short (up to 4 KB), its use measured by an eval (`…audit.md:151`).
- 4.c skill to set up CI (phase 9) with the system's own linter where it exists (`…audit.md:158`).
- 4.d exploration with a one-line goal and a time ceiling; a finding without evidence does not count (`…audit.md:157`).
4.1 (transcripts of four talks): not carried / open:
- 4.1 "meta-circle" outside the work (reads agent logs, human remarks, corrections and returns them to rules) - not in the forge 2 spec: owner question 11 of the plan.
- 4.1 sentinels (separate model call woken by events) - «сейчас не берём»; return if the first comparison run shows drift the numbers do not see.
- 4.1 plan depth by "expected pain" - not taken as a rule.
- 4.1 open lint rule sets (~100 rules; code-vs-pre-AI comparison set) - candidate for the forge 2 linter set, phase 1, "не проверено".
Section 5 of the report lists what was not checked: `docs/DECISIONS_ARCHIVE.md` not opened; part of the files named by the copy's README absent; foreign numbers are guides only.

## Trail

| tid | op | target | pattern / range | flags | result | control |
|---|---|---|---|---|---|---|
| t01 | read | docs/tasks/specs/reports/20261125-forge2-ideas-audit.md | 1-209 | — | read docs/tasks/specs/reports/20261125-forge2-ideas-audit.md:1-209 | — |
| t02 | read | docs/tasks/handoffs/20261125-forge2-recon-frozen-backlog.md | 1-148 | — | read docs/tasks/handoffs/20261125-forge2-recon-frozen-backlog.md:1-148 | — |
| t03 | read | docs/tasks/handoffs/20261125-forge2-recon-piles.md | 1-177 | — | read docs/tasks/handoffs/20261125-forge2-recon-piles.md:1-177 | — |
| t04 | read | docs/tasks/handoffs/20261125-forge2-recon-run-lessons.md | 1-118 | — | read docs/tasks/handoffs/20261125-forge2-recon-run-lessons.md:1-118 | — |
| t05 | read | docs/tasks/handoffs/20261125-forge2-recon-experiments-retros.md | 1-173 | — | read docs/tasks/handoffs/20261125-forge2-recon-experiments-retros.md:1-173 | — |
| t06 | read | plans/piles/_template/finding.md | 1-14 | — | read plans/piles/_template/finding.md:1-14 | — |
| t07 | read | plans/piles/_template/README.md | 1-55 | — | read plans/piles/_template/README.md:1-55 | — |
| t08 | read | docs/TEAMWORK.md | 1-60 | — | read docs/TEAMWORK.md:1-60 | — |
| t09 | read | docs/retro/classes.md | 1-28 | — | read docs/retro/classes.md:1-28 | — |
| t10 | read | plans/BACKLOG.md | 1-40 | — | read plans/BACKLOG.md:1-40 | — |
| t11 | read | docs/tasks/architect-queue.md | 1-30 | — | read docs/tasks/architect-queue.md:1-30 | — |
| t12 | read | DECISIONS.md | 1-25 | — | read DECISIONS.md:1-25 | — |
| t13 | grep | docs/tasks/handoffs | `1195` | -i content | found 0 | — |
| t14 | grep | plans/BACKLOG.md | `1195` | -i count | absent | t15 |
| t15 | grep | plans/BACKLOG.md | `piles-freeze` | -i count | found 1; plans/BACKLOG.md:3 | — |
| t16 | glob | plans/piles | `plans/piles/**` | files | found 100; plans/piles/codex/batch-1-overhead-fixes.md (1345 matches, 100 shown) | — |
| t17 | grep | plans/piles | `^` | count glob=**/*.md | found 1346; plans/piles/_template/README.md:55 | — |
| t18 | grep | listing toolu_01F3yz2HrVgCASr7hVeEtyhn.txt | `\\findings\\` | count | found 1195 | — |
| t19 | grep | listing toolu_01F3yz2HrVgCASr7hVeEtyhn.txt | `^plans.piles.[^\\]+.findings` | count | found 1195 | — |
| t20 | grep | listing toolu_01F3yz2HrVgCASr7hVeEtyhn.txt | `^plans.piles.thinking-roles.findings` | count | found 30 | — |
| t21 | grep | listing toolu_01F3yz2HrVgCASr7hVeEtyhn.txt | `^plans.piles.universality.findings` | -i count | absent | t20 |
| t22 | grep | listing toolu_01F3yz2HrVgCASr7hVeEtyhn.txt | `^plans.piles.proposals.findings` | -i count | absent | t20 |
| t23 | grep | listing toolu_01F3yz2HrVgCASr7hVeEtyhn.txt | `^plans.piles.<slug>.findings` for the other 34 slugs (34 calls: project-knowledge 17, told-before-work 15, run-honesty 5, execution-probes 43, pre-code 2, test-code-quality 13, conductor 23, codex 20, collect 6, cost-dashboard 22, driver-controller 33, driver-hosts 80, execution-report 105, exploratory 1, gates-and-words 48, github-move 1, grounding 8, hotfix-12586 35, kb 1, live-run-fvf 116, live-runs 23, onboarding-forge 116, package-ci 31, regression 4, release-next 59, report-delivery 34, roles-context 24, speed-cost 17, stand-and-sources 12, words-gates 38, rules-debt 32, forge 125, onboarding-hooks 56) | count | found 1165; sums with t20 to 1195 | — |
| t24 | grep | plans/piles | `^\| (\`findings/[^\`]+\`\|B-\d+) \| [^\|]+ \|` | content -o glob=**/README.md | found 1327; plans/piles/_template/README.md:46 | — |
| t25 | grep | listing toolu_01DPa9zdoNELkFUVr2UbDF7N.txt | `\| находка \|$` | count | found 1060 | — |
| t26 | grep | listing toolu_01DPa9zdoNELkFUVr2UbDF7N.txt | `\| строка \|$` | count | found 267 | — |
| t27 | grep | plans/piles | `кандидат наверх: да` | -i count glob=**/findings/*.md | found 60; plans/piles/codex/findings/20261013-binding-readers-writers.md | — |
| t28 | grep | plans/piles/proposals | `кандидат наверх: нет` | -i count | absent | t29 |
| t29 | grep | plans/piles/forge | `кандидат наверх: да` | -i files | found 1; plans/piles/forge/findings/20261009-b-331-zakryt-kommentariem.md | — |
| t30 | grep | plans/BACKLOG.md | `^\| B-\d+ ` | count | found 432; plans/BACKLOG.md | — |
| t31 | grep | plans/MEASUREMENTS.md | `^#{1,3} ` | count | found 41; plans/MEASUREMENTS.md | — |
| t32 | glob | docs/retro/** | `docs/retro/**` | files | found 5; docs/retro/classes.md | — |
| t33 | grep | docs/tasks/architect-queue.md | `^- \[[ x]\] ` | count | found 13; docs/tasks/architect-queue.md | — |
| t34 | grep | docs/RELATED_WORK.md | `^#{1,3} ` | content | found 9; docs/RELATED_WORK.md:1 | — |
| t35 | grep | DECISIONS.md | `^- D-\d{4} ` | count | found 4; DECISIONS.md | — |
| t36 | grep | docs/DECISIONS_ARCHIVE.md | `^### D-\d{4}` | count | found 71; docs/DECISIONS_ARCHIVE.md | — |
| t37 | grep | docs/DECISIONS_ARCHIVE.md | `^- D-\d{4} ` | count | found 84; docs/DECISIONS_ARCHIVE.md | — |
| t38 | grep | docs/TEAMWORK.md | `^#{1,3} \|находк\|findings` | content | found 15; docs/TEAMWORK.md:1 | — |
| t39 | glob | repo root | `DECISIONS*.md`, `docs/DECISIONS*.md`, `docs/tasks/architect-queue.md`, `docs/RELATED_WORK.md` | files | found 4; DECISIONS.md, docs/DECISIONS_ARCHIVE.md, docs/tasks/architect-queue.md, docs/RELATED_WORK.md | — |

## Not done
- Experiment notebooks outside `runs/`: no recount; "about 274 .md files in experiments/ and 142 in mybooks" are the earlier handoff's numbers (`20261125-forge2-recon-experiments-retros.md` t29 and Not-done). Folders `experiments/**/runs/` were not opened, as the non-goals say.
- Batch files (`batch-*.md`) were not counted per pile; no per-pile batch counts or per-node counts. A rough remainder (1346 - 1195 - 37) is arithmetic, not a measurement.
- The 1060 `находка` rows in the card tables against the 1195 finding files: the 135 difference is stated, not explained (not checked which files lack a card row).
- Ideas and lessons inside finding bodies were not sampled; the statement "no field tells idea from bug" rests on the template `plans/piles/_template/finding.md`, the sample of 25 finding header lines (`^id: `, offset 600, live-run-fvf) and the 60-file `кандидат наверх: да` count, not on reading each body.
- `docs/DECISIONS_ARCHIVE.md` 71 vs 84 counts may overlap; not checked. The `docs/OWNER_PRINCIPLES.md` count (31) is from the earlier handoff, not recounted.
- Environment state is outside this role's tools. Prices and spend figures were not quoted by choice; the forge 2 repository was not read.
- Rows t13, t14, t21, t22, t28 are zero results with controls; the earlier zero greps without `-i` (`1195` in BACKLOG, the universality and proposals counts) were rerun with `-i` and give the same zero.
