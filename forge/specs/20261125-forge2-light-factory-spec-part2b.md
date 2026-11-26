Frame spec part 2b: card bodies of phase 2 (C2-1..C2-8), forge 2 and the light QA factory (t-1918, F19; 25.11.2026). Split from part 2 r1 by the Lead's script (fork F52 (a)); the bodies are byte-equal to the designer's text. Read with part 2 = `docs/tasks/specs/20261125-forge2-light-factory-spec-part2.md`: its sections 1 (scope, order, rules before the skeleton, common), 3 (forks F15-F23, F50-F52), 4 (small choices) and 5 (trail) hold for these bodies. Frame = `docs/tasks/specs/20261125-forge2-light-factory-spec.md`; plan = `...-plan.md`. `owns:` paths are absolute; other paths are relative to `C:/QAFactory/forge2-repo/` as in part 2.

## 2. Cards

### C2-1 Craft page form, index, page check
- amended by: A21, A26, A32, A33, A34 (cards whose `amends:` line names this card; read them with it)
- Delivers: page `factory/craft/<id>.md`, English: `## Outcome` (what the stage must leave), `## Craft` (each rule once, followed by its ids, e.g. `(refs:A17, slices:A14)`; a closed vocabulary cited from its data file, never copied), `## How checked` (F12 (a): generated from gate rows naming this page + authored critic criteria), `## Examples` (a language, runner or tracker only as an example, never a branch -- AR-1, AR-2, P31), `## Seeded tasks` (set id). Index `factory/data/craft-pages.yaml`: `id`, `file`, `title`, `stages` (empty allowed before C3-2), `statements`, `critic_criteria`, `seeded_set`; `not_carried` rows (`id`, `reason`). `pages_check.py`: page<->row both ways; sections present; each mapped id in exactly one page or `not_carried`; `--write-how-checked` (the one road for that section).
- Statement map (`refs:` = `...-recon-references.md` A1-A38, `slices:` = `...-recon-role-slices.md` A1-A27):
  - requirements (C2-2): refs:A3, A4, A5, A6, A7, A38; slices:A2, A3, A4, A26
  - questions (C2-2): refs:A24, A25, A26, A27; slices:A21
  - report (C2-2): refs:A2, A22, A23; slices:A1, A10, A18
  - check-selection (C2-3): refs:A8, A12, A15; slices:A23 (regression clause stated in `regression`)
  - levels (C2-3): refs:A11; slices:A6, A24
  - automate (C2-3): refs:A9, A10, A14
  - regression (C2-3): no digest row; rests on P24; states the regression clauses of slices:A20, A23
  - test-code (C2-4): refs:A1, A13, A16, A17; slices:A5, A12, A13, A14, A20
  - manual-pass (C2-4): refs:A18, A19, A21; slices:A7, A8
  - exploration (C2-4): refs:A20
  - stand (C2-4, F22): refs:A29, A30; slices:A9, A22, A25
  - red-analysis (C2-5): refs:A31 (vocabulary home `factory/data/red-causes.yaml`, C3-3); slices:A11, A15, A16
  - bug (C2-5): refs:A32; slices:A17
  - not carried: refs:A28 (home C3-5 templates, part 1 2d); refs:A33 (AR-28, part 1 2f, C4-6); refs:A34 (plan: 48 metrics not carried); refs:A35, slices:A19 (retro, F3 (a)); refs:A36, A37 (onboarding, cross-story state: phase 5); slices:A27 (spend: part 1 2f, F7).
  - digest D rows by one home: refs:D2 -> questions (no proposed default); refs:D4 -> check-selection defines `impact`; refs:D5-D7, slices:D6 -> one page each; refs:D1, D3, D8 -> F3, F1/F2, F4; slices:D1 -> `levels` cites the one level list of `record-schema.yaml` (C3-1); slices:D2 -> `red-causes.yaml`; slices:D3, D4 -> the critic reads the same page (C4-2, F12).
- owns: C:/QAFactory/forge2-repo/factory/data/craft-pages.yaml, C:/QAFactory/forge2-repo/factory/tools/pages_check.py, C:/QAFactory/forge2-repo/factory/tests/test_pages_check.py
- deps: C1-3, C1-6 (code, part 1 section 6); F12, F22.
- keys: K1 the 65 ids each in one place; K2 an id in two pages -> exit 1 naming both; K3 a missing section -> exit 1; K4 How checked equals its regeneration.
- edges: `gate-rules.yaml` absent (before C3-3, part 3) -> How checked holds critic criteria and `gate rows: none yet`, green (a page check is no exit) -- after C3-3 it must equal regeneration; page without row or row without page -> red; an id not in its digest -> red (an invented home never counts); a language outside `## Examples` -> C1-2's counter, not repeated.
- test: `factory/tests/test_pages_check.py` one table: one home / twice / none / unknown id / missing section / missing file / gate rows absent / present | expected from: plan 1.2; F12; this map.

### C2-2 Pages: requirements, questions, report (owner reads pages)
- amended by: A10, A21, A31, A35 (cards whose `amends:` line names this card; read them with it)
- Delivers: `factory/craft/requirements.md`, `questions.md`, `report.md` in the C2-1 form with their mapped ids; rules as outcomes, no field, script or old stage name (refs:A25); written from the source lines (`C:/QAFactory/forge-repo/ai-packages/qa-factory/references/`), not the digest gist.
- owns: C:/QAFactory/forge2-repo/factory/craft/requirements.md, C:/QAFactory/forge2-repo/factory/craft/questions.md, C:/QAFactory/forge2-repo/factory/craft/report.md
- deps: the C0-2 and C0-3 freeze commits (F5); C2-1 form (text may precede its code); C2-6 sets; the owner's reading (plan «Цена»).
- keys: K1 `pages_check.py` green; K2 a critic compares each rule with its source lines (nothing lost, nothing added); K3 the owner's read recorded in her words; K4 each page's seeded set run with the page.
- edges: a rule naming a tracker or route -> example row or performer judgment (AR-1, AR-2); sources disagree (refs:D2) -> one rule, the commit names the dropped reading; a gate's job -> How checked only (one home); no freeze commit yet -> the page is not written (part 1 section 6).
- test: none -- judgment text; witness: pages check, critic verdict, seeded run, owner's read.

### C2-3 Pages: check selection + techniques, levels, automate, regression
- amended by: A4, A7, A8, A15, A25, A26, A31, A32, A33 (cards whose `amends:` line names this card; read them with it)
- Delivers: `factory/craft/check-selection.md`, `levels.md`, `automate.md`, `regression.md`; owner's words: pyramid levels, case and autotest not one-to-one (part 1 section 5); regression handed over, never run (P24).
- owns: C:/QAFactory/forge2-repo/factory/craft/check-selection.md, C:/QAFactory/forge2-repo/factory/craft/levels.md, C:/QAFactory/forge2-repo/factory/craft/automate.md, C:/QAFactory/forge2-repo/factory/craft/regression.md
- deps: as C2-2 (incl. the C0-2/C0-3 freeze).
- keys: as C2-2; K5 `levels.md` holds no level list of its own (slices:D1).
- edges: as C2-2; a case ceiling by story size -> not carried (plan В5).
- test: none -- as C2-2.

### C2-4 Pages: test code, manual pass + evidence, exploration, stand (F22)
- amended by: A4, A7, A24, A25, A26, A28, A29, A32, A33, A35 (cards whose `amends:` line names this card; read them with it)
- Delivers: `factory/craft/test-code.md`, `manual-pass.md`, `exploration.md`, `stand.md` (F22 (a): stage 2 product, smoke, stands and test data; refs:A29, A30; slices:A9, A22, A25); the probe rule once in test-code (refs:A17, slices:A14), read by the critic's probe (G4.C).
- owns: C:/QAFactory/forge2-repo/factory/craft/test-code.md, C:/QAFactory/forge2-repo/factory/craft/manual-pass.md, C:/QAFactory/forge2-repo/factory/craft/exploration.md, C:/QAFactory/forge2-repo/factory/craft/stand.md
- deps: as C2-2 (incl. the C0-2/C0-3 freeze); F22.
- keys: as C2-2.
- edges: as C2-2; runner-only forms of the source (slices C9) -> not carried; a runner named -> example only.
- test: none -- as C2-2.

### C2-5 Pages: red analysis, bug
- amended by: A16, A25, A26, A28, A31, A33, A35 (cards whose `amends:` line names this card; read them with it)
- Delivers: `factory/craft/red-analysis.md`, `bug.md`; how to choose and evidence a cause; the cause list stays in `red-causes.yaml` (C3-3, part 3).
- owns: C:/QAFactory/forge2-repo/factory/craft/red-analysis.md, C:/QAFactory/forge2-repo/factory/craft/bug.md
- deps: as C2-2 (incl. the C0-2/C0-3 freeze); C3-3 for the vocabulary file.
- keys: as C2-2.
- edges: as C2-2; `red-causes.yaml` absent (before C3-3) -> the page names it as the list's home, no copy (one home).
- test: none -- as C2-2.

### C2-6 Seeded-defect sets and runner
- amended by: A27, B4 (cards whose `amends:` line names this card; read them with it)
- Delivers: `measure/seeded/<page>/<task>/`: `task.md` (the stage's ask as the performer gets it), `input/` (frozen files authored for the set: a requirement text, a test, a case list, a red run output, or a small static fixture product), `key.yaml` (written BEFORE any run: defect ids, class, place, `judged_by: run | critic`; `run` -> a command exiting non-zero when caught; `critic` -> the catch described; `expected from:` a source rule or plan example, never the implementation or a truth card). Seeded defect = one planted fault of the page's class with a known answer, planted by the set author in the set's own input (F50 (a)); NEVER a bug, root or card of either truth table (MyBooks, ao3-wrapper) and never a measuring project's source -- else the measurement trains on its own test (part 1 F5 (a); plan v1.3 extends it to both projects). Catch = the keyed command fails, or a fresh-context critic holding the key and only the agent's output says `caught` for that id; `unsure` apart; an unkeyed find = `extra`, hand-checked. Sets at least (plan 3.2): a test that cannot fail (test-code), duplicate cases (check-selection), one bug with two manifestations (bug), a fixture product with three planted bug roots (manual-pass/exploration). `seeded.py run --page <id> --arm with|without` copies each task's input to a temp folder (key never) and launches it ONLY through `arm.py launch --task <folder>` (one launcher, P31; one call per task); `score` (task, arm, defect, catch, judge, tokens and wall from the arm's run row; no money key).
- owns: C:/QAFactory/forge2-repo/measure/seeded/, C:/QAFactory/forge2-repo/measure/tools/seeded.py, C:/QAFactory/forge2-repo/forge/tests/test_seeded.py
- deps: C0-2, C0-3 (freeze commits, F5); C0-4 (`launch --task`); C2-1 field `seeded_set`; F50.
- keys: K1 every indexed page has a set or `seeded_set: none -- <why>`; K2 discrimination first: the `without` arm does not catch all (fp:A1: a set the control saturates does not rank); K3 the key's commit precedes the first run row; K4 no key byte in the input folder; K5 each key row names the nearest card of both frozen truth tables and why it differs, the critic confirms; K6 `seeded.py` starts no process but `arm.py`.
- edges: key in the agent's context -> run void, recorded (a catch on a leaked key never counts); `run` judge cannot start -> `unmeasured`, not missed; asking is right (owner-decides class) -> `asked` is the catch (fp:A4); agent call fails -> rerun, both rows kept; `arm.py` absent or refusing -> `unmeasured`, never a direct harness call (one road); a seed found equal to a truth card -> set void, rewritten, void rows kept (a seed from the test never ranks).
- test: `forge/tests/test_seeded.py` one table: run-judged caught/missed/unstartable, critic rows from a fixture verdict, key leak, launch only through `arm.py` (refusal -> unmeasured), score without money | expected from: plan 3.2, 4.6; part 1 section 1 P31; this card.

### C2-7 Free agent with pages vs without, MEASURING RUN closing phase 2
- amended by: A30, B4 (cards whose `amends:` line names this card; read them with it)
- Delivers: arm `free+pages` = C0-5's prompt + all accepted pages, appended by `arm.py` (same launcher, `mode: comparison`); two runs per project, comparable with C0-5 in every fingerprint field but the prompt; blind evaluation as LR2-1 (mybooks `factory-vs-free-agent.md:44-54`: one outcome form, arm words neutral, X/Y by lot, critic judges, Lead opens the key); seeded sets `with`/`without`; run folder `measure/runs/craft-pages/` (F21 (a)): `result.md` (rows per arm, spread, catches, wall, tokens, verdict), judgment files, run rows, operator answers; money keys stripped; raw logs in `copies_root`. Acceptance (F23 (a)): no worse than the baseline's worse run on every countable row; at least as many seeded catches as `without`, no more false alarms, on every set; wall and tokens within 5x baseline (over 2x a finding).
- owns: C:/QAFactory/forge2-repo/measure/runs/craft-pages/
- deps: C2-1..C2-6, C0-5; F21, F23.
- keys: K1 four `free+pages` runs comparable to baseline but the prompt; K2 seeded rows per set, both arms; K3 the verdict names each worse row and the page owning its rule; K4 no money figure.
- edges: baseline field drifted (model, harness version, stand build) -> baseline rerun first, never compared across it; worse on any row -> pages not accepted, the page goes back (plan 4.1); unmeasured run -> rerun; folder absent -> created by `collect` (C0-5 must exist, part 1 section 6).
- test: none -- measuring run; witness score rows and verdict line.

### C2-8 Stage-chain cost spike, MEASURING, before phase 3 (verdict fix 18)
- amended by: A30, B4 (cards whose `amends:` line names this card; read them with it)
- Delivers: the six-stage chain (part 1 section 3, G1-G6) walked BY HAND (no phase 3-4 code) on a stub record of the MyBooks story: a hand-written `record.yaml` in the part 1 2a shape, header `mode: comparison`, kept in `copies_root`; each stage is a FRESH context started by `arm.py launch --task` (one launcher, P31) with the stage's outcome and gate rows, its accepted pages, and the record; plus the critic contexts at G3, G4, G6 (F51 (a)); the stage writes its rows into the stub by hand; the operator answers stop questions only, from `answers/` as in C0-5. `measure/runs/stage-chain-spike.md` holds: fingerprint vs the C0-5 MyBooks baseline; per context and in total `wall_s`, `turns`, `tokens` (in, out, cache read, cache write); total / baseline mean for wall and for summed tokens, with the baseline spread; the costliest stage; unmeasured contexts by name; fix rounds and refusal relaunches named as not walked (the ratio is a floor); the outcome line. No money figure.
- owns: C:/QAFactory/forge2-repo/measure/runs/stage-chain-spike.md
- deps: C0-4, C0-5 (MyBooks baseline); F51.
- keys: K1 every context has a run row in the file or `unmeasured: <why>`; K2 both ratios computed against the baseline, `compare` equal in every field but the prompt; K3 the outcome: both ratios <= 2 and nothing unmeasured -> `within: phase 3 goes`; a ratio over 2 -> `over: finding to the Lead naming the costliest stage`, phase 3 waits for the Lead's decision (plan «Цена»: stages merge as data rows); K4 money grep 0 hits.
- edges: C0-5 baseline absent or MyBooks runs `unmeasured` -> the spike is not run (no ratio without its denominator); a stage that cannot be walked on a stub (e.g. stand down at G2) -> named, counted unmeasured, never as zero, outcome `incomplete: finding to the Lead`, phase 3 waits as for `over` (an unmeasured stage never makes the chain look cheap); fingerprint field differs (model, harness version) -> rerun, never compared across it; no page accepted yet -> stages run on gate rows only, `pages: none` written (page cost unmeasured, named); a context over the host window -> that stage `unmeasured: no_move` (part 1 2a).
- test: none -- measuring run, no code; witness: run rows, `compare` output, outcome line.
