# Forge 2 recon: the 14 factual claims of an outside audit, checked against the spec and the old forge (t-1953)

Accepted by the Architect 26.11: coverage K1-K14 one verdict each; negative claims K3, K5, K6, K7 re-run with same-shape positive controls (0 hits; controls hit); K4c hits read (another matter); quotes K8, K10, K11 found at the cited lines.

digest: v1 t-1953

## Claims

- K1 holds
  - Spec: `forge/TESTING.md:5` "2. Layers. Two, no third: stories run on real run artifacts once such artifacts exist, and data joints (one data file read against the file or tool that consumes it)." (T2)
  - Old: `docs/TESTING.md:43` "Что пишется — три слоя, и только они". Line 55: "3. **Таблица случаев для настоящей комбинаторики**: разбор идентификаторов, ключи и хэши записей, ... деньги". (T3, T4)
  - Small difference: the old third layer lists money where the audit says "calculations". The meaning matches.

- K2 partly
  - Does not hold: C1-1 contains no justification rule and no replacement text of its own.
    - It only drops the old rule. `part2.md:90` "dropped: fr:A14, fp:A5 (replaced by plan 4.3)". (T7)
    - fr:A14 is the old rule 10 in the recon map: "A mechanism ships with its compliance cost, a registered detector..." (T16)
    - Old text, `COORDINATOR.md:246-247`: "10. Four questions for every mechanism ... (a) what compliance costs and who pays for it". (T6)
  - Holds: what replaces it is a justification, and for gates it is concrete.
    - Plan 4.3, `plan.md:1108`: "Каждая новая проверка называет исход, который она защищает, и прогон, где без неё случилась беда." (T19) The plan says "check", not "gate".
    - The gate row carries it. `spec.md:130` "`protects` + `origin` (plan 4.3)". (T20)
  - Does not hold in full: a panel, registry or hook is not left with nothing.
    - B5 K3 measures per-call hook overhead: "over 100 ms -> a finding to the Lead". (T13)
    - Plan 4.5, `plan.md:1112-1114`: friction is measured every run, and "Инструмент, с которым дороже, чем без него, — дефект". (T19)
    - No card asks "who pays for compliance" of a new mechanism. Searches for "four questions|compliance|justif|what it costs" found nothing in the spec. (T10, control T11)
    - No `panel`-specific check was searched for. That half rests on those words only.

- K3 holds
  - C1-1 `part2.md:85`: "Delivers: `CLAUDE.md` (...) and thin `.claude/agents/{scout,builder,critic,designer}.md`". Line 91, owns: `CLAUDE.md`, `forge/COORDINATOR.md`, `.claude/agents/`. (T7)
  - `AGENTS.md` appears in no spec file. Words searched, all case-insensitive: `AGENTS\.md` (T8, control T9: the same form finds `CLAUDE\.md`), `codex`, and `harness-neutral|entry point|rule entry`.
  - The `AGENTS` count of 15 (T23) comes from `.claude/agents` and not from the file name.
  - Codex appears once: `spec.md:359` "first harness Claude Code (Codex phase 9)". (T24)
  - `spec.md:267` has "harness-neutral". (T47b)

- K4 holds, for the acceptance keys named
  - C4-1 keys are K1..K5 (`part3b.md:25`). C4-3 keys are K1..K4 (`part3b.md:46`). None of them states (a), (b) or (c). (T26)
  - (a) After an answer the work moved on: no other card has an explicit check.
    - The nearest are C4-1's move table (`part3b.md:14-15`: `at_stop` answer -> `exited`/`fix_round`; `held`: answer -> `open`) and K1 "12 states yield its move". This is a state table, not a check that the work advanced.
    - A3, `part4.md:51`, makes the new-requirements question "non-blocking ... the stage moves on". That concerns a different question.
  - (b) Factory-owned failure exhausts automatic ways out before a person is asked: partly, in other places.
    - C4-1 K2: "the third identical refusal goes to `no_move`".
    - C4-1 K5: "conductor returning nothing twice -> `ask.py` form `conductor` to the person (never a dead end)".
    - A1 `part4.md:30,36`: cut ladder of 1st relaunch, 2nd conductor, 3rd `critical` question. Key K2.
    - C4-3 `part3b.md:42`: the common field `tried`, and form `critical` (why it blocks, tried).
    - No key covers a factory-owned failure in general, such as an unreadable source before asking.
  - (c) A repeated question names what the earlier answer did not settle: no card has it.
    - C4-3 edge `part3b.md:47` goes the other way: "the same question already answered -> not asked, the answer cited".
    - `part4b-2.md:32` is a retro counter for repeated questions, not a rule.
    - Words searched: `settle|repeated question|same question|asked again|re-ask`. (T27)
    - The `.{200}...answer.{200}` form returned nothing. (T29, control T27)

- K5 partly
  - A road to a bug exists where a manual run fails.
    - `part5.md:49` (A25): "the feature does not work -> the manual result is revised red and the red becomes `product_bug`". (T35)
    - `spec.md:141`: "manual fails attach `manual_pass_report` (F2)". (T33b)
    - Gate G5.3 is "bug draft: steps, expectation + source, fact, evidence, repro". (`spec.md:194`, T32)
  - No scenario or key says that a confirmed breach reaches report and bug draft when nothing can be run.
    - Old FR-22, `factory-rules.md:332`: "A discrepancy with a requirement has a road to a bug even when no test can fail." (T50)
    - Words searched: `FR-22|confirmed (breach|violation)|violation` (T33, control T27) and `no test possible|no test can|even when no test|requirement unmet|unmet requirement|cannot be tested|not testable|untestable|breach` (T34).
    - T34 gave only `spec.md:354` "untestable", about a packaged binary, which is irrelevant.

- K6 holds
  - C3-1 `part3.md:25`: "Lock (F11 (a)): `record.yaml.lock` created exclusively, holding pid + time; retry every 0.2 s ..." Key K4: "two concurrent `add` calls both land with distinct `seq`". (T42)
  - C4-1 `part3b.md:26` (edge) is the nearest text: "record changed by another writer between compute and move -> recompute once, then move". It says nothing about who launches. (T26)
  - No card says who gets the right when two `next` commands see the same ready work.
    - Words searched: `two next|simultaneous|same moment|same ready|already (running|launched|taken)|launch (right|token|claim)|next.{0,60}(lock|twice|again|concurrent)`. (T38)
    - The one hit, `part4b.md:100`, is "per-launch tokens", unrelated.
    - A1 amends C4-1 and was read (T28). It has no launch-claim rule.

- K7 holds
  - `stand_lease.py` in two lines (T39):
    - A project-level lease on a stand that cannot take two runs. It is one record per environment name in `state/stand-lease.json`, under an OS file lock. It allows one `exclusive` holder or up to `max_shared` `walk` holders, never both.
    - A second request waits in line (`waited_s`) and gives up with `StandBusy` after `wait_s`, having launched nothing. Dead holders are dropped. A person's `--release --reason` clears all holders. Origin: TP1-15045, five UI runs started in two seconds.
  - No factory card has a checkable scenario for two stories on one shared mutable stand.
    - Words searched: `same stand|one stand|shared stand|two stories|both stories|another story|other stories|stand.{0,30}(locked|busy|one at a time|occupied)`. (T54, control T41)
    - Also `one run at a time|exclusive|run.parallel|serial|sequential`. (T37b)
    - Hits are only about the measuring arms.
      - `part2.md:55`: "arms in sequence (one emulator)".
      - `part2.md:76` (C0-5): runs "sequential, stand reset/seed before each".
    - `parallel_max` 2 for `tests` (`part3.md:198`) concerns groups inside one story.
  - C4-4 and A25 are silent on a replay after a partly executed operation.
    - A25 `part5.md:53`, nearest edges: "a replay that changes stand data -> as the manual pass did; its run row is referenced (X3)"; "a replay timeout -> A14 (status `timeout`, results `not_reached`...)"; missing `needs_env` -> `setup_stopped`.
    - C4-4 `part3b.md:57`, edges: 0 bytes, huge output, non-UTF-8, exit 0 with failures, no parse, timeout.
    - Words searched in part5 and part3b: `partly|partially|half-done|half done|interrupted|mid-operation|part executed|half-executed|crash(ed)? (mid|in the middle)`. (T52)

- K8 holds (all three parts)
  - A1 `part4.md:28`: "`tokens` = the launch's CONTEXT SIZE: input + cache-write + cache-read tokens of its latest model call (the B5 measure ...), never a sum over calls". (T28)
  - B5 `part4b.md:110`: "TOKENS = the launch's context size from its transcript ... not total spend". `main`: "warn at 300000 and again at each further 50000 ..., never stopped". Rows at start: "`main` tokens warn 300000, stop `null`, wall `null`". (T31)
  - A1 `part4.md:28`: "`wall_s` = the launch's wall clock MINUS the intervals of its `run_tests.py` children". `story_wall_s` also excludes them, and also the person's `stop_wait` intervals. (T28)

- K9 holds
  - A24 r2 edge, `part5.md:44`: "a trivial look (\"looked, all fine\") -> met by code; its meaning is a residual named: stage 2 has no critic (frame 3), the G6 critic reads the report section and the person reads it". (T35)
  - Report: `part5.md:40` prints "at stage 2 (each beyond row of `product` with outcome and reason, or the `nothing_beyond` reason ...)".
  - A4 edge, `part4.md:66`: "a look finds nothing -> row `outcome: matched` (empty is a row, AR-23), listed in the report".
  - So the report does show such an outcome, as a row with `matched` and its reason, with no marker that the look was trivial.

- K10 holds
  - `part3.md:95`: "a list over its row budget shows the first rows then `and N more (ask to see them)`".
  - Table row `understanding`, `part3.md:99`: "40 lines; requirement rows 15 then \"and N more\"". (T43)
  - Same pattern for `test_plan` (15 check rows) and `q-bug-or-not` (5 bugs).
  - The cut applies only when the list exceeds its budget.

- K11 holds
  - A9 `part4-2.md:24`: "a green on an unmeasured build -> counted, named \"build not identified\" (an unknown build cannot prove a difference)". The same edge says "greens count and the report says \"build not identified\"". (T40)

- K12 holds
  - C2-7 `part2b.md:75`: "Acceptance (F23 (a)): no worse than the baseline's worse run on every countable row; at least as many seeded catches as `without`, no more false alarms, on every set; wall and tokens within 5x baseline". (T44)
  - The seeded-catch bar is against the `without` arm, not the worst run.
  - C2-8 `part2b.md:83`: "fix rounds and refusal relaunches named as not walked (the ratio is a floor)". The spec says "floor", not "lower bound". The meaning is the same. (T44)
  - C2-8 K3 gates phase 3 on "both ratios <= 2 and nothing unmeasured".

- K13 partly
  - Holds: counts only. C1-2 `part2.md:99`: "factory tool code 6000 non-blank lines of `factory/tools/**/*.py` + `factory/hooks/**/*.py`, gate rules 45 rows, `stage_start_load: null`", plus `CLAUDE.md` + agents 12288 B and `COORDINATOR.md` 20480 B. (T7)
  - Does not hold in full: the budget file has a slot for what an agent receives, `stage_start_load`.
    - Edge `part2.md:103`: "`stage_start_load: null` -> `not set: first measured run (F9)`, exit 3, never a pass". F9 is `spec.md:340`; AR-11 is `spec.md:41`: "stage start load one number under F9". (T45, T46, T47)
    - No tool or key of C1-2 measures it. It is unset until a first measured run.
  - Launches and returns per story, and tokens to reach the report: nothing in C1-2.

- K14 holds, with a nuance
  - Plan phases, `plan.md:1208-1212` (T48):
    - Phase 0: measure + free-agent baseline.
    - Phase 1: skeleton.
    - Phase 2: craft pages. Its first measure is free agent with pages vs without, and its second is the hand-walked six-stage chain before phase 3.
    - Phase 3: record + gates, "after phase 1 and the trial pass of the chain".
    - Phase 4: whole route. "Главное измерение" is the comparison run on `ao3-wrapper` and MyBooks. It is here, after the gates.
  - `spec.md:251`: "C2-8 before phase 3".
  - Nuance: two measuring steps do sit before phase 3, but neither is a minimal end-to-end pass to a report with a failure included. What each gives instead:
    - C0-4: the arm launcher plus scorer (`arm.py`, `score.py`: cells, `passes`, `compare`). It is a measuring tool with no pass of its own. (T7)
    - C0-5: two free-agent runs per project with `result.md` (wall, turns, tokens, human count, spread). It is the baseline that closes phase 0. (T7)
    - C2-7: a free-agent arm plus craft pages against that baseline. It closes phase 2, with seeded sets. Its bars: no worse than the worse baseline run per row, and wall/tokens within 5x. (T44)
    - C2-8: the chain walked by hand on a stub record, with no phase 3-4 code. Refusals and fix rounds are not walked, so the ratio is a floor. An unwalkable stage gives `incomplete`. (T44)
    - W1 walk: gate row W1, `spec.md:204`: "each read and typed-field reader has a producer, each leave a reader (CI)". It is a static CI check of the stage table (`rows.py walk`, `part3.md:74`). It runs no story. (T49)

## Trail

| tid | op | target | pattern / range | flags | result | control |
|---|---|---|---|---|---|---|
| T1 | glob | C:/QAFactory/forge2-repo/forge/specs | `forge/specs/*` | — | found 17; the 13 files named *spec*.md, plus the overview html, SOURCES.md and the plan | — |
| T2 | read | C:/QAFactory/forge2-repo/forge/TESTING.md | 1-25 | — | read C:/QAFactory/forge2-repo/forge/TESTING.md:1-25 | — |
| T3 | grep | C:/QAFactory/forge-repo/docs/TESTING.md | `^(##\|###) ` | content | found 13; docs/TESTING.md:43 | — |
| T4 | read | C:/QAFactory/forge-repo/docs/TESTING.md | 36-64 | — | read C:/QAFactory/forge-repo/docs/TESTING.md:36-64 | — |
| T5 | grep | forge2 specs, glob `*spec*.md` | `^### (C1-1\|C1-2\|C3-1\|C3-5\|C4-1\|C4-3\|C4-4\|A1\|A9\|A24\|A25\|B5\|C2-7\|C2-8\|C0-4\|C0-5)\b` | content glob=*spec*.md | found 17; part2.md:62, :75, :83, :97 and 13 more | — |
| T6 | grep | C:/QAFactory/forge-repo/COORDINATOR.md | `^10\. ` | content | found 1; COORDINATOR.md:246 | — |
| T7 | read | C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part2.md | 55-123 | — | read part2.md:55-123 | — |
| T8 | grep | forge2 specs | `AGENTS\.md` | -i content glob=*spec*.md | absent | T9 |
| T9 | grep | forge2 specs | `CLAUDE\.md` | -i content glob=*spec*.md | found 15; part2.md:23, :85, :87 | — |
| T10 | grep | forge2 specs | `four questions\|compliance\|justif\|what it costs\|four-questions` | -i content glob=*spec*.md | absent | T11 |
| T11 | grep | forge2 specs | `rule 10\|fr:A8\|fr:A9\|fr:A10\|fr:A11` | -i content glob=*spec*.md | found 4; spec.md:136, :275, :352 | — |
| T12 | grep | forge2 specs | `amends:.*C1-1` | -i content glob=*spec*.md | found 9; part4b-2.md:5, :38, part4b.md:109, :119 | — |
| T13 | read | C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4b.md | 112-125 | — | read part4b.md:112-125 | — |
| T14 | grep | forge2 specs | `mechanism` | -i -o content glob=*spec*.md | found 1; part4b-2.md:58 | — |
| T15 | read | C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4b-2.md | 56-58 | — | read part4b-2.md:56-58 | — |
| T16 | grep | C:/QAFactory/forge2-repo/forge/specs/recon/20261125-forge2-recon-forge-rules.md | `four questions\|compliance` | -i content | found 1; recon-forge-rules.md:22 | — |
| T18 | grep | C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-plan.md | `^#{1,4} ` | content | found 100; plan.md:1098, :1202 | — |
| T19 | read | C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-plan.md | 1098-1123 | — | read plan.md:1098-1123 | — |
| T20 | grep | forge2 specs | `protects\|outcome it` | -i content glob=*spec*.md | found 4; spec.md:130, part3.md:80, part4-2.md:77, part4-3.md:5 | — |
| T21 | read | C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part3.md | 56-77 | — | read part3.md:56-77 | — |
| T23 | grep | forge2 specs | `AGENTS` | -i count glob=*spec*.md | count 15 | — |
| T24 | grep | forge2 specs | `codex` | -i count glob=*spec*.md | count 1 | — |
| T26 | read | C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part3b.md | 5-64 | — | read part3b.md:5-64 | — |
| T27 | grep | forge2 specs | `settle\|moved on\|exhaust\|repeat(ed)? question\|re-ask\|asked again\|same question\|progress after` | -i -o -n content glob=*spec*.md | found 9; part3.md:185, part3b.md:47, part4.md:51, part4b-2.md:32 | — |
| T28 | read | C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4.md | 24-84 | — | read part4.md:24-84 | — |
| T29 | grep | forge2 specs | `.{200}(after (the\|an\|her\|a person's) answer\|answer did not\|answer moved\|no progress\|unchanged after).{200}` | -i -o content glob=*spec*.md | absent | T27 |
| T31 | read | C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4b.md | 107-111 | — | read part4b.md:107-111 | — |
| T32 | grep | C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec.md | `G5\.[0-9]\|bug draft\|no failing test\|cannot (be )?run\|breach\|not executable\|manual.{0,20}(bug\|breach)` | -i -o -n content | found 4; spec.md:192, :193, :194, :326 | — |
| T33 | grep | forge2 specs | `FR-22\|confirmed (breach\|violation)\|violation` | -i -o -n content glob=*spec*.md | absent | T27 |
| T33b | grep | forge2 specs | `executed by agent, no evidence\|bug draft\|bug-draft\|manual (fail\|red)\|manual verdict revised\|revised red` | -i -o -n content glob=*spec*.md | found 25; spec.md:141, part5.md:49 | — |
| T34 | grep | forge2 specs | `no test possible\|no test can\|even when no test\|requirement unmet\|unmet requirement\|cannot be tested\|not testable\|untestable\|breach` | -i -o -n content glob=*spec*.md | found 1; spec.md:354 | — |
| T35 | read | C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part5.md | 26-61 | — | read part5.md:26-61 | — |
| T37b | grep | forge2 specs | `one run at a time\|exclusive\|run\.parallel\|parallel: false\|serial\|sequential\|data independ\|independent (data\|of)\|shared account` | -i -o -n content glob=*spec*.md | found 5; part2.md:76, :116, part3.md:25 | — |
| T38 | grep | forge2 specs | `two next\|simultaneous\|same moment\|same ready\|already (running\|launched\|taken)\|launch (right\|token\|claim)\|claims? the launch\|next.{0,60}(lock\|twice\|again\|concurrent)` | -i -o -n content glob=*spec*.md | found 1; part4b.md:100 (irrelevant: "per-launch tokens") | — |
| T39 | read | C:/QAFactory/forge-repo/ai-packages/qa-factory/scripts/stand_lease.py | 1-60 | — | read stand_lease.py:1-60 | — |
| T40 | read | C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4-2.md | 19-30 | — | read part4-2.md:19-30 | — |
| T41 | grep | forge2 specs | `parallel\|at the same time\|several stories\|another story\|other story\|two groups` | -i -o -n content glob=*spec*.md | found 25; part2.md:21, part3.md:10, part5.md:56 | — |
| T42 | read | C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part3.md | 17-32 | — | read part3.md:17-32 | — |
| T43 | read | C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part3.md | 93-106 | — | read part3.md:93-106 | — |
| T44 | read | C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part2b.md | 74-89 | — | read part2b.md:74-89 | — |
| T45 | grep | forge2 specs | `stage_start_load` | -o -n content glob=*spec*.md | found 2; part2.md:99, :103 | — |
| T46 | grep | C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec.md | `\*\*F9\*\*.*` | content -n | found 1; spec.md:340 | — |
| T47 | grep | forge2 specs | `start load\|start-load\|startload\|stage start\|context bytes\|bytes read` | -i -o -n content glob=*spec*.md | found 5; spec.md:41, :340, part4b.md:55 | — |
| T47b | grep | forge2 specs | `harness-neutral\|entry point\|entry-point\|rule entry` | -i -o -n content glob=*spec*.md | found 1; spec.md:267 | — |
| T48 | read | C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-plan.md | 1202-1228 | — | read plan.md:1202-1228 | — |
| T49 | grep | C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec.md | `^\| W1 .*` | content -n | found 1; spec.md:204 | — |
| T50 | read | C:/QAFactory/forge-repo/ai-packages/qa-factory/design/factory-rules.md | 332-336 | — | read factory-rules.md:332-336 | — |
| T51 | read | C:/Users/<user>/Documents/Codex/2026-11-25/c-qafactory-forge-repo-docs-tasks/outputs/forge2-migration-audit.md | 1-47 | — | read forge2-migration-audit.md:1-47 | — |
| T52 | grep | forge2 specs, glob `*spec-part{5,3b}.md` | `partly\|partially\|half-done\|half done\|interrupted\|mid-operation\|part executed\|half-executed\|crash(ed)? (mid\|in the middle)` | -i content glob=*spec-part{5,3b}.md | absent | T53 |
| T53 | grep | forge2 specs, glob `*spec-part{5,3b}.md` | `replay` | -i content glob=*spec-part{5,3b}.md | found 18; part5.md only (T53 was run in count mode, a shape difference; the brace glob matched part5 but not part3b, which may hold no "replay") | — |
| T54 | grep | forge2 specs | `same stand\|one stand\|shared stand\|two stories\|both stories\|another story\|other stories\|stand.{0,30}(locked\|busy\|one at a time\|occupied)` | -i -o -n content glob=*spec*.md | absent | T41 |

(Trail ids are not contiguous. Where a tid is missing, e.g. T17, T22, T25 and T30, that search was dropped from the table or merged into another row.)

## Not done

- No file under any `experiments/**/runs/` was opened, and no price figure is quoted.
- `ci-jobs.json` and `docs/TESTING.md` beyond lines 36-64 were not read, and `COORDINATOR.md` only at rule 10. `factory-rules.md` was read only at FR-22 (lines 332-336). FR-3, FR-7 and FR-50 were not read in the old rules. K4 compares the spec only with the audit's description of them.
- Plan sections "Цена" (`plan.md:1323`) and the plan's own text about the W1 walk were not read. K14 rests on `plan.md:1098-1123` and `:1202-1228` plus the cards.
- K2: no search ran for the word "panel" on its own. The "panel/registry/hook has no check" half rests on the justification and compliance words in T10 and T11 and on the B5 and plan 4.5 hits.
- K7: the brace glob in T52 and T53 matched part5 and not part3b (T53). So the zero for "partly" words covers part5 for certain and part3b only if the glob matched that file.
- Noticed on the way, not researched:
  - The audit's item 1 and item 5 cite cards B15 and A26 as absent, and `ci-jobs.json` with 13 `not_built`. That is outside K1..K14.
  - `forge/TESTING.md:23` ("`tests` job stays `not_built` until the first file under `forge/tests/` lands") is the rule the audit contrasts with.
