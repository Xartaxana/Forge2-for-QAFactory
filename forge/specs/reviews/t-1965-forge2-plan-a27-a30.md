# t-1965 -- critic on plan: forge 2 cards A27 (part 7), A28, A29, A30 (part 8)

Reviewed state: forge 2 `77eeb1a`. Frame: spec section 1 and the owner's yardstick from the dispatch. B16 not judged (another critic). Verdicts are an input to the Lead's acceptance; the decision is the Lead's.

## Verdict lines

- A27: blocker
- A28: blocker
- A29: blocker
- A30: blocker
- link F3+F9: hole -- the decided link (plan 26.11 ~01:23 p.2) is written in no card, and as A26's X4 reads today a handed place has no debtor at `reds` (cases at F30).
- gate-row recount: 39, the designer is right. Frame section 3 has X1-X6 (6), G1.x-G6.x (29), D1-D3 (3), W1 (1). The frame's "section 3: 40" (F9) and part 4's "Gate rows 40 -> 45" are both off by one: the true count is 39 -> 44, one row under F9's 45. A side effect: part 5 (A24) chose an X1 filter over a new row because "F9's 45 rows are reached", which was not true. The Lead may reopen that.

Blocking findings: F1, F2, F11, F18, F24, F25, F28, F29, F30a (nine). The rest are fixes, to land before the card is built.

## Findings

### A27

**F1 (A27 (4) ONE BATCH, blocks): batch deltas add up over batches.** Each batch run is compared "vs the thin pair", but batches land one after another (each commit adds rows). Case: the thin pair spends 100k/104k tokens. Batch 1 adds 30k, so its run is 134k: dearer. Batch 2 adds nothing, and its run is 134k again: also "dearer" against the thin pair. If batch 2 has no `caught` row, its `idle` rows go to F131 for rework or drop, at zero cost of their own. Fix: the delta of batch n is taken against the last accepted run (thin pair for batch 1, batch n-1's run after that). The thin spread stays the noise measure.

**F2 (A27 (4) per-row classes, blocks): `caught` can hold by construction, and some rows have no class.** (a) The thin record is written under the thin schema: C3-1 thin node with W1, where a field whose reader is unbuilt is not written. Replaying a batch row over the KEPT thin record therefore refuses every row whose `over` fields first exist in that batch. Case: the G5.3 fields steps / expectation + source / repro have no built reader in the thin pass. G5.3 refuses on the thin record and is met in the batch run, so it is `caught` without having caught anything. A dear batch then always escapes F131. (b) `exit_check.py` runs only `when: exit|after_critic` (frame 2c). G1.P-G6.P (intent), G3.C/G4.C/G6.C (critic) and D3 (`ask`) therefore get none of the four classes. Every row of `batch:person` and `batch:critic` then lands in F131 by default. Fix: a row whose `over` fields are absent from the thin schema is `not comparable on thin`, and its class comes from the batch run's labelled refusals only. Name the class source for rows that are not `exit`/`after_critic` (critic findings for critic rows; stop answers for person rows).

**F3 (A27 (3), fix): the factory side of every bar is unstated, and so is the outcome over two runs.** Case: the factory runs find 5 and 3 truth bugs and the best free run finds 4. Is the bar met? The same question applies to the wall and token ratios ("`wall_full_s` / free mean": whose `wall_full_s`?). And if run 1 is `reached, seed caught` while run 2 is `not reached at tests: cut`, which outcome line goes into `result.md`? Fix: each bar is judged per factory run and the worse run decides. The outcome line is per run; the pass outcome is the worse of the two; batches start only when both runs reach the report.

**F4 (A27 (4) spread, fix): no edge for a wide thin spread.** "A delta inside the thin pair's spread = no measured change". Case: one thin run takes a cut and a relaunch, so the two runs are 100k and 220k. Every later batch is then `no measured change`, F131 never fires, and gates land unmeasured. Fix: a thin spread above a stated share of the mean (data row, temporary) leads to a third thin run before batch 1, and the yardstick is the two closest runs. Alternatively name the residual.

**F5 (A27 (2), fix): the seeded-vs-unseeded control has no outcome BEYOND.** "C0-5's unseeded runs are the control that the seed did not move the free cost outside C0-5's spread". Nothing says what happens when the seed does move it. Fix: outside the spread -> finding to the Lead, and the ratios are read against `free-seeded` only, with the shift named in `result.md`.

**F6 (A27 (2) story, fix): F123 is now the owner's word, and the card does not say so.** Plan 01:23 p.1 records MyBooks as the owner's word and the story as hers, to be asked for before the run. `LOCAL-1` is only the designer's fallback. The card still fixes `story/LOCAL-1.md`, writes the seed "in a requirement the story states", and claims "the C2-8 story" as a shared floor. Fix: the story is the owner's, asked before the seed is written. If it differs from C2-8's story, the `result.md` line says the floor and the thin ratio sit on different stories (the plan's own words).

**F7 (A27 (2) arms, fix): "the SAME seeded clone" conflicts with C0-4.** C0-4 clones per run into `<copies_root>/<run>/<arm>/`. If one directory is reused, run 2 sees run 1's tests, notes and commits; a free agent may even have fixed the seed. Folding the patch into HEAD with `commit --amend` also gives a new sha on every prepare (committer date), so "the new HEAD recorded" differs run to run. Fix: "same seeded bytes": every run prepares its own clone with the same patch, fingerprint `seed` equal, the source commit (pre-seed) compared, and the folded HEAD sha recorded but not compared, or dates pinned.

**F8 (A27 small choices, fix): the fold into HEAD can still point at the seed.** "Folded into HEAD ... not a commit of its own: either would point an agent at the seed". Case: the patch touches `src/shelf.js`, which HEAD's own commit did not change. `git show HEAD --stat` then lists a file the commit message does not explain. Batch `plan` (G3.5 `diff_hunks`, `change_ref`) reads exactly these hunks. Fix: the seed patch touches only files HEAD already changes, or the card names the exposure as equal for both arms (a residual).

**F9 (A27 (3) NOT REACHED, fix): pages are fixed by someone who knows the seed.** F132 writes the seed after the pages are accepted "so no page trains on them". But after `not reached` "the Lead fixes ... page text", and the Lead holds `key.yaml` (C2-6 K3) and labels the refusals. The pages can then train on the seed and the free prompt cannot (C0-5 frozen), so the comparison can be gamed. Fix: the Lead does not open `key.yaml` before the outcome line (as C2-7's blind form: "Lead opens the key"). Otherwise a page edit made after the key exists means a new seed by a writer who did not make the edit.

**F10 (A27 (3) loss, fix): a loss to the free agent goes back to the Lead only.** Plan 01:23 p.7 returns "the result of the thin pass against the free agent" to the Architect. The card sends `result.md` to "the Lead (outcome, order of batches)", and fewer truth bugs or a factory question only make "a finding" while batches still go. Fix: any bar beyond target -> `result.md` goes to the Architect before batch 1. This is the frame's escalation, not a new gate.

**F11 (A27 (4) batch list vs A25 deferral, blocks): `batch:tests` holds A25.** It also holds the C4-4 IN row "A25 replay (batch:tests)". A25 is deferred to the last phase (plan 01:38 p.3), while C4-7 (phase 4) depends on "A27's last batch closed". As written, either `batch:tests` waits for the last phase and C4-7 with it, or the batch lands without the part it names. Per the 01:38 record, G4.2 keeps its old meaning without A25. Fix: drop A25 from `batch:tests`, and say A25 lands in the last phase as its own measured batch.

**F12 (A27 (4), fix): W1 never gets its row.** The batches take "every gate row ... except X1 and W1", and the thin file holds X1 only. C3-3 Delivers "one row per id of frame 3" and its K1, "every frame-3 id has one row", is placed "at the last batch". Both are red at the last batch, with 43 rows of 44. Fix: W1's row (`when: ci`) goes into the thin node, or the card states W1 is no row of `gate-rules.yaml` and amends C3-3 K1.

**F13 (A27 counted, also A30 (a), fix): overlapping test runs are counted twice.** `wall_minus_tests_s` is "minus the `test_run` intervals", and A30's "of which <h:mm> in test runs" sums the same intervals. `tests` runs groups in parallel (`parallel_max` 2). Case: g1 and g2 both test from 10:00 to 10:20, so 40 minutes are subtracted from a 20-minute span. The same holds for A29's `stand_wait` subtraction when it overlaps a test run. Fix: subtract (and show) the union of the intervals.

**F14 (A27 K8 vs A30, fix): the money grep hits A30's own line.** K8 greps `usd|cost|price` (-i) over `measure/runs/thin-pass/`, and that folder keeps `test_report.md` per run. Once A30's line `Cost: <n> launches, ...` reaches the template (from batch `report` on), K8 is red by construction. Fix: rename the line (e.g. `Spend:`) or scope K8 to money forms (currency signs, `usd`, `price`, a `cost` key).

**F15 (A27 (4), fix): "the KEPT thin record" is singular, but there are two thin runs.** Fix: name it. Classes are computed over both records, and `caught` needs a refusal on both.

**F16 (A27 seed walk vs A28 (d), fix): a seed caught as a `no_test` bug has no stated outcome.** With A28, `product` may draft a `no_test` bug for the seed before any red. The seed check needs "a red test, cause `product_bug`, a bug draft". Fix: state whether a `no_test` draft naming the seed is `caught` (and walk trace "red: absent"), or say the seed is chosen so that a test can show it and a `no_test` catch reads `unsure` for the Lead.

### A28

**F17 (A28 (a), fix): A28 silently needs A25.** "Non-blocking questions (`beyond`, `proposed_tests`, `new_requirements`, `unclear`)": section `unclear` exists only with A25 (part 5:48; plan 01:38 p.3, "раздела вопроса `unclear` до A25 нет"). Fix: drop `unclear`, or add "(with A25)".

**F18 (A28 (d) with C3-2, blocks): `product` and `tests` write `bugs` rows they were never told how to write.** F140 adds `bugs` to their optional leaves, but the `bug` page is in `reds`' craft set only, and G5.3 is in `reds`' exit column only (part3:41-44; neither is amended). G5.3 is a shape rule, so its debtor is the row's stage. Case: `product` writes a `no_test` draft with an agent-attached file. Nothing is asked at `product`'s exit. At `reds`' exit G5.3 refuses with debtor `product` (exited), so a shortfall relaunches `product` for a rule it was never told (AR-10). K7 "at `product` ... G5.3 met / debt" cannot hold as written. Fix: A28 amends C3-2. `bug` joins the craft sets of `product` and `tests`, and G5.3 joins their exit columns (due there, How checked generated).

**F19 (A28 (b) in comparison mode, fix): a factory cause offers "pass" where no pass may exist.** The options of a factory cause are "pass, filed as a factory defect" or "stop". In `mode: comparison` a `passes` row unscores the run (C0-4 edge; frame 2a). A27 builds form `critical` in its thin node, so this reaches the measuring run. Fix: in comparison/night, factory-cause options are "stop" only, or the question stays open and non-blocking as A27 states; the page says so.

**F20 (A28 (b), fix): no one is named to write `tried` for cause `cut`.** The `cut` question is raised by `run_stage.py` at A1's 3rd rung, not by a performer, yet `ask.py` refuses it without `tried` (`relaunch`, `conductor`). Fix: as A29 does for `stand_unknown`, code writes `tried` from rungs 1 and 2 (`relaunch: <result>`, `conductor: <result>`).

**F21 (A28 (c), fix): "WHICH APPLIES" is neither enforced nor defined for every question.** It is not listed among the refusals, so it is unclear whether `--follows` on a settled answer is refused (the error direction suggests not). For non-blocking questions, (a) journals no target, so "found its move" is undefined. Separately, `answered: <qid>` is printed even when a named row changed after the answer. Case: REQ-2 is revised after `is_requirement` and the performer re-asks: it gets `answered: q7`, exit 0, and may read it as settled. Fix: say WHICH APPLIES is page guidance (not a refusal) with "move" defined for non-blocking questions. Make the `answered:` line name rows changed since (`seq` > answer).

**F22 (A28 (a), fix): "per original question" does not say how a chain is counted.** A follow-up has the same identity, so it may follow the original or the 1st follow-up. Fix: `follows` always names the root `qid`, and the count is per root.

**F23 (A28 (d) vs the decided link, fix, seam): A28 (d) still uses the old suspicion rule.** It says "A suspicion stays a `findings` row (`outcome: open` ... or `bug_or_not` section `beyond`)". The Lead's link adds a third road (hand to `reds`). The card text must gain the hand word, and it is the natural home (see F30).

### A29

**F24 (A29 (c), blocks): a reset of up to 600 s runs while the record lock is held.** "The next stand launch of ANY story, in its locked step: ... `stand.py reset` runs it (timeout 600)". The record lock waits at most `record_lock_wait_s` 10, then "record busy" (C3-1). Case: `tests` g1 is running and its performer's `record.py add` comes during g2's reset. After 10 s the write is refused, so a running performer loses writes for up to 10 minutes. Fix: under the locks, mark `resetting` and the claim; run the reset unlocked; re-take the locks to record the result. Also state the lock order record -> stand -> journal (the card names only record -> journal).

**F25 (A29 (b)+(c), blocks): a dead holder is dropped without a torn mark.** A holder proven gone is dropped at the next take (`stand_takeover`, carried), with no torn mark. Case: the `next` process holding a `tests` launch (stand `run`) is killed (terminal closed). No return, no cut, so no `mark unknown` by `run_stage.py`, and `run_tests.py` died with no end event. Another story takes over the lease with the state still `known` and reports greens on a stand left mid-run. That breaks the card's own INVARIANT. Fix: a takeover of a dead holder whose launch was `stand: run`, and a `claim_broken: process gone` on a stand launch, both mark the state `unknown` before the take.

**F26 (A29 (a), fix): claim liveness has three holes.** (1) "pid, process start time": of `next` or of the host child? The child does not exist when the claim is written, and if `next` exits after spawning, the claim reads "process gone" at once and a second `next` launches the same work again. Fix: the claim names the `next` process, which waits for the launch's return (state it), or records the child pid under the lock after spawn. (2) `claim_stale_s` 7200 against real time: A1's `wall_s` excludes test runs, so a live `tests` launch with three 1-hour suites runs over 3 h. At 7201 an uncheckable claim is broken and the work launched twice. Fix: the invariant "`claim_stale_s` > `wall_s` + the sum of its runs' timeouts", or refresh the claim on each `test_run_start`. (3) A claim broken as stale keeps its lease (an unknown holder keeps), so the relaunch of the same work finds itself `stand busy`. State it, and make the busy print name its own story.

**F27 (A29 WORLDS, fix): A29 misdescribes A27.** It calls A27 "a hand walk ... one context at a time by its operator" with "no `next`". A27's thin node of C4-1 holds `start`, `next`, `resume`. Fix: name which of claim / lease / torn mark the thin `next` carries. A27 sec. 6 says a part 8 key enters only if it is in the IN column, and the claim is a `next` key.

### A30

**F28 (A30 (c), blocks; VARIETY): a red closes only on an identified build, for every cause.** Before, G5.2 asked a later run for cause `test`. The product is untouched by a test fix, so a fixed test's green on the same stand proves the fix whatever the build identity. Case: a project whose key `stand` has no build-identity command (`unmeasured: no build-identity command`, A9). Every test-cause red fixed and rerun green stays a G5.2 debt. The door is a key that cannot be added at launch in comparison/night (N9) or a pass, which does not exist there. The stage stops, while a free agent would just rerun. Fix: the identified-build condition applies to closing a `product_bug` red (a product change). `test` and `environment` reds keep G5.2's "a later run".

**F29 (A30 (d), blocks): the "best run" bar is moved onto the wrong row.** Plan 00:54 table row 9 says «планка по пойманным багам — не хуже ЛУЧШЕГО прогона». A30 instead puts "the baseline's BETTER run" on C2-7's seeded-catch row and leaves the other countable rows (truth bugs found) at "no worse than the worse run". This fails three ways. (1) C2-7's seeded sets run `with|without` arms (C2-6 `seeded.py`). C0-5's baseline runs no seeded set, so "the baseline's better run on every set" names no measurement (the digest K12 bullet: "the seeded-catch bar is against the `without` arm"). (2) Truth bugs stay on the worse run, against the plan row. (3) It contradicts A27 F129: "truth bugs found >= the BEST free run ... one reference with part 8". Fix: in C2-7, truth-bug `found` >= the baseline's better run; seeded catches stay >= `without`; the other rows stay at the worse run.

**F30a (A30 (b) with D1, blocks): showing every decision row breaks D1.** "Decision rows alone exceed the budget: all of them whole" -- but D1 (frame 3, `after_critic`) still checks the line and byte budgets. Case: 20 decision rows of 400 B make 8000 B > 6144 B. That is a D1 debt the performer cannot clear (the rows may not be cut): refused twice, then `no_move`. Fix: A30 amends D1's reading. A document whose surplus is decision rows only is met, with the `over budget` line.

**F31 (A30 (b), fix): the `bug_or_not` form still cuts bugs she must decide.** The cut rule covers "person documents", but `bug_or_not` is a form (frame 2d: "5 bugs then `and N more`"). Case: 7 drafts await G5.P and 2 are hidden in the form she answers. Fix: extend "never cut" to the `bug_or_not` body (and its D1 form budget).

**F32 (A30 (a), fix): one data row per figure, but values set per project.** The spend warn rows live in `factory/data/launches.yaml` (one value each) yet are "set from C0-5's baseline at 2x its mean per project". Case: MyBooks mean 1.2M and ao3 3M: one row cannot hold both. Fix: rows keyed by project, or a knowledge key. A new project stays `not set` (no default), which is right.

**F33 (A30 (d), fix): runs older than `variant` have no stated reading.** Case: C2-8 `plain` against a C0-5 row with no `variant` makes `compare` refuse, naming `variant`, and C2-8 K2 fails. A27 states it for `seed` ("absent -> `none`"). Fix: absent -> `plain`.

**F34 (A30 (a) vs A27, fix): two definitions share the name `wall_full_s`.** A27 measures to the test_report build. A30 measures "from `start` WITH test runs, minus her waits" with no end. Fix: one definition, end = test_report build, `stop_wait` subtracted (0 in comparison).

## F30 -- link F3+F9 (decided, not yet in a card): hole

Decided: the stage that saw a confirmed breach writes the draft (A28 (d), F140). A suspicion a stage cannot settle is handed to `reds` by an answer word: the handing stage's X4 is closed by it, `reds`' X4 owes an answer per handed place, and an unanswered one shows as "left open" at the report. Cases:
- **No red at all.** `reds` runs anyway (no skip rule; t-1949 F10), so handed places give it a subject: good. But A26 EXIT (2) makes the debtor "the row's stage", and the handed row keeps `stage: tests`, so `reds`' X4 ("among the stage's rows") never sees it. Hole: X4 must read live handed rows of any stage with debtor `reds`. The X1 filter at `reds` must say whether answering a handed place counts as `reds`' beyond row (as F5 of t-1949 scoped empties to the exiting stage, it should not).
- **Handed after `reds` is over.** A stale relaunch of `tests` after `reds` exited, or `report` handing backwards: debtor `reds` has exited, so a shortfall relaunch? Unstated. Also unstated: whether `report`, or the explore launch (A24: "a launch never owes for another"), may hand at all. Hole: only `product` and `tests` hand; a hand after `reds` exited opens a `reds` shortfall.
- **Handing everything to close cheaply.** The word alone closes the hander's X4, with no reason and nothing tried, so `product` can hand 30 places at no cost. Nor is `reds` told at entry what was handed (no `context.py` line). Hole: the hand word needs `--why` with what was tried (presence only, AR-29), and `reds`' context prints "handed to you: <ids>" (AR-10).
- **Answered by nobody at the report.** An unanswered handed place is an open X4 debt, and G6.3 "no open gate debt" refuses the report. "Left open" is reachable only through a cut, and A26 states that only for explore. Hole: state the road, i.e. after `reds`' refusal max or cut, a handed place becomes `left open: handed, not answered` (a report line, not a G6.3 debt). Otherwise say it blocks.
- **Error direction.** Handing errs toward work going on. The residual: `reds`' caps bound the handed load. Name it.

## Yardstick, per card (short)
- A27: the comparison is the right one (the same story and seeded bytes, both arms before any gate). It can be skewed by F1, F2, F4 and F9, and a loss is not escalated (F10). No probe writes product code (the `outward_write` hook is IN). Told at entry holds (`context.py`, How checked in every batch commit).
- A28: told at entry is broken for `product`/`tests` bug drafts (F18). Doors exist for every refusal. The 3rd follow-up leads to `stopped: unsettled` with `resume` as the way out.
- A29: the gate hinders right work while a reset runs (F24) and lets an unknown stand pass (F25).
- A30: hinders right work on projects with no build identity (F28) and on documents over their budget (F30a). Nothing of the old factory is lost (`stand_lease.py` is carried line by line in A29).

## Spot-checks (facts by trail)
- Holds: C4-1 K2 (third refusal -> `no_move`) and K5 (conductor twice); C2-6 K3-K5; C3-1 lock (10 s, 60 s break); A9 `product_build` `unmeasured: no build-identity command` (part4-2:22); A1 `wall_s` excludes test runs (part4:28); C2-8 K3 `over`; `decide_later` is A3's (part4:51), not A25's.
- Does not hold: A27 "the same seeded clone" vs C0-4 (F7); A30 "the baseline's better run" on sets (F29); A29 WORLDS on A27 (F27); A28 `unclear` (F17); C3-3 K1 vs W1 left out of every batch (F12).
- A25 dependencies found: A27 `batch:tests` (F11) and A28 `unclear` (F17). A29's "replays included" is the torn-replay edge the 01:38 record lets wait.

## Trail
- Read: part 7 whole; part 8 lines 1-75 (A28-A30, not B16); part 6 A26 (24-50); frame 2b-3 (123-206) and F9/F30; part 3 C3-2 table (40-45), C3-1 lock (25), C3-3 (56-80); part 3b C4-1, C4-2 probe; part 2 C0-4, C0-5; part 2b C2-6-C2-8; part 4 section 1 and A1 lines; part4-2 A9 (21-23); part 5 A25 lines 48-54; the digest K10-K14; plan records 26.11 01:00, 01:04, 01:23, 01:38 (lines 3111-3318), and plan row 9 (3086); t-1949 findings F1-F14.
- Commands: `sed -n '164,205p' spec.md | grep -c -E '^\| (X|G|D|W)[0-9]'` -> 39; id list printed (X1..W1). `grep` of `G[1-6]\.\w+|X\d|D\d` over parts 2-6 -> new ids G3.5, G4.6, G5.4, G6.4, D4 (part4:13 "40 -> 45"). `grep -c decide_later` -> part4 7, part5 1, part8 1. `grep '`unclear`'` -> part 5 only + part 8:39. No file under `experiments/**/runs/` opened; no spec or plan file changed.

```json
{
  "verdict": "blocker",
  "blockers": [
    "F1: A27 batch deltas measured vs the thin pair accumulate over batches; measure each batch against the last accepted run",
    "F2: A27 per-row class caught holds by construction over a thin record lacking the batch fields; rows not exit/after_critic get no class",
    "F11: A27 batch:tests holds A25, deferred to the last phase, while C4-7 waits for the last batch",
    "F18: A28 product/tests write bugs rows with no bug page and no G5.3 in their exit column; G5.3 debt arrives as a shortfall untold at entry",
    "F24: A29 stand reset up to 600 s runs inside the record-locked step; record_lock_wait_s 10 refuses running performers' writes",
    "F25: A29 a dead holder is taken over without marking the stand unknown; greens on a stand torn mid-run",
    "F28: A30 closing any-cause red needs an identified build; projects without build identity stop on test-cause reds in comparison",
    "F29: A30 moves the best-run bar onto seeded sets the baseline never runs and leaves truth bugs on the worse run, against plan row 9 and A27 F129",
    "F30a: A30 decision rows shown whole break D1's budget gate with no door"
  ],
  "fixes": [
    "F3 factory side of each bar and outcome over two runs; F4 wide thin spread; F5 seeded control BEYOND; F6 story is the owner's; F7 same seeded bytes, per-run clone; F8 seed visible in HEAD stat; F9 key hidden from the page fixer; F10 loss goes to the Architect; F12 W1 row; F13 union of intervals; F14 K8 vs Cost line; F15 which kept record; F16 no_test seed catch",
    "F17 unclear needs A25; F19 no pass option in comparison; F20 code writes tried for cut; F21 WHICH APPLIES and answered line; F22 follow-up root; F23 hand word in A28 (d)",
    "F26 claim pid, stale vs real duration, stale claim keeps lease; F27 A29 WORLDS vs A27 thin next",
    "F31 bug_or_not form cut; F32 per-project warn rows; F33 variant birth rule; F34 one wall_full_s",
    "F30 link F3+F9: X4 debtor for handed rows, hand after reds exited, hand needs why and is told at reds entry, unanswered handed place road at report"
  ],
  "class_completeness": "Plan gate: siblings walked across the four cards and their amended cards -- interval subtraction (A27, A29, A30: F13), A25 dependency (A27, A28: F11, F17), comparison-mode pass options (A28 F19 vs A30 (c) states it), money grep vs Cost line (F14), definitions shared by A27 and A30 (F34). SIBLING_MAP not applicable (forge 2, no package file).",
  "trail": {
    "read": [
      "C:/QAFactory/forge2-repo/forge/specs/20261126-forge2-light-factory-spec-part7.md",
      "C:/QAFactory/forge2-repo/forge/specs/20261126-forge2-light-factory-spec-part8.md:1-75",
      "C:/QAFactory/forge2-repo/forge/specs/20261126-forge2-light-factory-spec-part6.md:24-50",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec.md:123-206,340,352",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part3.md:25,40-45,56-80",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part3b.md:5-36",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part2.md:62-96",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part2b.md:66-95",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4.md:10-37",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4-2.md:21-23",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part5.md:48-54",
      "C:/QAFactory/forge2-repo/forge/specs/recon/20261126-forge2-recon-outside-audit-claims.md:100-125",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-plan.md:3086,3111-3318",
      "C:/QAFactory/forge-repo/docs/tasks/specs/reviews/t-1949-forge2-plan-two-looks.md:9-40"
    ],
    "reruns": [
      {"command": "sed -n '164,205p' spec.md | grep -c -E '^\\| (X|G|D|W)[0-9]'", "result": "39"},
      {"command": "grep -c decide_later over spec parts", "result": "part4 7, part4-3 1, part5 1, part8 1, others 0"},
      {"command": "git -C C:/QAFactory/forge2-repo log --oneline -3", "result": "77eeb1a plan: six hooks ledgers accepted; ..."}
    ]
  },
  "mutants": [],
  "mutants_none": "plan gate on spec cards: no code, no worktree, no new behaviour to probe"
}
```
