# t-1966 -- critic on plan: forge 2 cards B14, B15, B16

Reviewed state: forge 2 `77eeb1a`. Cards as written, with the Architect's fork decisions (plan records 26.11 00:08, 00:54, 01:23, 01:38). Verdicts below are inputs to the Lead's acceptance, not acceptance itself.

- B14: blocker
- B15: blocker
- B16: blocker

Overall: REJECT (failure_class: spec). 5 blocking findings (F1, F9, F10, F20, F21); the rest are fixes to make before merge.

## B14 -- parallel sessions

Yardstick: told at entry holds (block (6) refusals line). A free agent in one session pays nothing for this card; the gates have doors. Red probe: n/a (forge-side). Old factory: the old forge's no-silent-reuse rule, ids never reused, and a collision counted as two tasks are carried. The old *destructive-command* guard is not carried (F1). F109 (a) agrees with the owner's «Нет, я одна» (22:12) and «не сейчас» (00:26).

**F1 (blocker) B14 rule 3 / C1-5 rule.** The card fixes one instance of "one checkout, shared by every session": sweeping `add`/`commit`. It misses the destructive commands on the same shared tree. Case: Lead A runs `git stash` (or `git reset --hard`, `git checkout -- .`, `git restore .`, `git clean -fd`, `git switch <branch>`) in `C:/QAFactory/forge2-repo` while Lead B has an uncommitted edit of `forge/BOOT.md` (rule 4 allows exactly that: edit, then commit). B's edit leaves the tree. B's next `git status --short` is clean, and nothing refuses or prints anything. The sweep door itself also passes: `git commit -m x -- .` and `git add forge/` satisfy the literal rule. The old forge refused `checkout`/`restore` on dirty paths (CLAUDE.md hygiene point 7(b)). Smallest fix: C1-5's one rule in the main checkout also refuses `stash` (any form but `list`/`show`), `reset --hard`, `checkout|restore` of `.` or of a directory, `clean`, and `switch`/`checkout <branch>`. It also refuses `commit -- .` and `add <directory>`. Door: "name your files" or "use your linked worktree". Indirect forms are a named residual, as now.

**F2 (fix) B14 rule 4, edges "run from a linked worktree".** The card does not say WHICH tree `git rev-parse --git-dir` vs `--git-common-dir` is run in: the process cwd, the `-C <dir>` / subshell target, or the tool's own root. Case 1: a worktree builder's B5 hook writes `cut`/`cap_warning` journal lines (B2 event list). The hooks run the main checkout's scripts (edge, estimate), but cwd is the worktree. With a cwd test the lines are refused and lost. Case 2: a builder runs `git -C C:/QAFactory/forge2-repo commit -m x` from its worktree. With a cwd test the C1-5 rule passes it. Fix: single-writer tools judge their own root (`--root` / script location). The C1-5 git rule judges the target tree (`-C`, a subshell `cd`, else the hook input's cwd). One sentence each.

**F3 (fix) block (6) neighbours.** `logs/journal/git-hooks.jsonl` (B9, part 4b-2: git hooks journal there) never writes `session_end`. After any push it shows as a live neighbour for 24 h, then as a permanent count. The same happens to a session whose harness id changes (`clear`, possibly `resume`). Its old file is a phantom neighbour, and its own B11 takes are now "held by another session": it must take itself over. Fix: exclude `git-hooks.jsonl` (C1-4 already excludes it in `pick_session`). State the id-change edge: the self-take-over with reason `id changed: <old>`, or B2 printing the previous id of the same process.

**F4 (fix) the old overlap check.** The edges ask what replaces dispatch_gate's refusal of two writing dispatches whose owns overlap. The card never says so. Case: two Lead sessions each dispatch a builder for card C1-5. Both get distinct issued ids and branches `w/t-12`, `w/t-13`. Nothing prints until the next start (block (6)) or a merge conflict, after two builds are paid for. Fix: name the replacement explicitly. Either (a) a residual: "seen at the next start and at the fast-forward", or (b) one advisory line from `journal.py --event dispatch`: `also open: t-12@<session> names <same card or L-id>`. That is presence only, no refusal.

**F5 (fix) B14 rule 6 / edge "the old holder, if alive after all".** A take-over refuses the old holder only at its next `set`. Its journal `accept` for the task already closed by `return ... died` is written silently, because `open_tasks` ignores a closing event after a close (journal.py `open_tasks`). Its branch can still fast-forward. That collision is silent, against the card's own invariant "a collision is always visible, never silent". Fix: a closing event on a task whose last event already closed it prints `already closed by <file>:<line>: <note>` (exit 0, or refused). One rule in `journal.py`.

**F6 (fix) rules 4 vs 6 conflict.** Rule 4: a dirty hand file means another session is mid-write: wait, never edit over it. Rule 6: the dead session's uncommitted main-checkout paths are read and committed by the Lead. In one shared checkout no dirty path carries its session. Case: neighbour B is alive and mid-edit on `forge/BOOT.md`, and session C died. The Lead commits B's half-edit as "C's leftovers". Fix: rule 6 applies to a dirty path only when block (6) shows no live neighbour, or when the person names the path's session. Otherwise rule 4 (wait).

**F7 (fix) rule 1, id issue.** (a) Empty or absent journal: "1 + the largest" has no largest, so the edge is silent. Forge 2 has no `logs/journal/` today (ls: empty), so the first issue is exactly this case. (b) Two issuers: the old forge still issues `t-` ids for forge 2 work (this task is t-1966; forge 2 specs cite 28 distinct old `t-` ids). A fresh forge 2 journal starts at `t-1` and later re-issues ids those documents cite. Fix: the first issue writes a seed line: n = 1 + the largest `t-<digits>` in the old forge journal and forge 2's tree at that moment. State the empty-journal behaviour.

**F8 (fix) pre-push in a shared dirty checkout.** C1-5's pre-push runs `ci.py` on the working tree, while B14 makes other sessions' uncommitted paths normal there. Case: A pushes its committed state, but `tests` reds on B's half-written tool. The right action is hindered. The opposite case is a local green on a tree that is not the pushed head (Actions still judges). Fix: one edge line. Either pre-push judges a clean checkout of the pushed head, or it prints `judged tree differs from pushed head: <dirty paths>` and leaves the verdict to Actions.

## B15 -- the carry ledger

Yardstick: the CI row's limit is stated honestly. FIDELITY says presence proves a decision exists, never that content survived, and names the second layer (code critic `there`/`not there` per row). Told at entry: the `carry:` dispatch line. Old factory: this card is the guard. F9 and F10 are where it leaks.

**F9 (blocker) no terminal state, so the check passes with nothing decided.** `not-found` is a legal end value of check (2), and nothing ever demands the final verdict. A row with `where: none` blocks no card, and `unplaced` has no reader with a duty. A row naming a card that was already dispatched never refuses again, and no code critic will ever receive it (FIDELITY fires only on future dispatches). That is exactly the F118 (a) world: piles last, so their cards are built first. Cases from practice: the six hooks ledgers hold 535 `not-found` rows (plan 01:38 table), 22 of them `where: none` (probe below). Under B15 they stay green forever once C1-5 and B2 are past dispatch. Likewise a performer can write every row `not-found` / `none`, or `carried` with `where` naming any built card and proof `<card> K1` (the key is not resolved). The check is green, and no critic will ever see those rows. This contradicts the plan's point 3 (00:26, «у каждой строки есть решение» checked by code) and the owner's «не "забыты"». Smallest fix, two keys: (1) `carry.py late` lists `not-found`/`waits-owner` rows whose `where` card is already accepted, and `carried` rows added after their card's acceptance. The Lead pastes it beside `dropped` at each phase close, and each group gets an `L-<n>` amendment record. (2) A CI flag at the last phase: zero `not-found` across all ledgers. Also resolve `K<n>` against the card's keys line.

**F10 (blocker) a theme verdict has no road into row verdicts.** B15 is silent on themes. Practice made them anyway: `package-agents-themes.md` (30 themes, Architect verdicts; the head says "a row inherits its theme's verdict at the ledger's migration (B15) unless the card ... says otherwise"), and t-1964 is writing forge-hooks themes now. A migration builder hits three questions about intent:
- Theme words (`carry`, `split`, `carried-differently -- ...`) are not B15's closed set. T5 is `split`, decided per row by nobody.
- The homes are cards A31-A35, not yet written. A `carried` row naming A32 is red (card not resolving), but staying `not-found` loses a decision the Architect already took.
- The decider cell has no form for a theme decision (`architect <date>` is reserved to `dropped`).

In addition, `topic` is B11's seven topics, but the plan's import of themes into the work list (00:08: «в список работы ввозятся темы») groups by themes, so there are two group vocabularies. Fix: one Delivers paragraph.
- Migration writes per-row verdicts from the theme, with decider `architect <date> T<n>` allowed on every verdict.
- A `split` theme is resolved row by row by the Architect before migration.
- A row whose home card is unwritten stays `not-found`, with `where` naming the existing card area and `note: theme T<n> -> <future card>`. It still blocks that area: correct, and visible.
- Add a `theme` cell, or say that `topic` holds the theme and the B11 topic is derived.

**F11 (fix) the hooks carrier is in no seed row and overlaps another.** The six hooks ledgers (42 files) are not in the seed table and not named in the migration. Their files are 37 under `tools/`, which is also FT's glob `tools/**` (218), and 5 under `.githooks/`, which is in no carrier. Their heads lack `glob:`, `blocks:` and a freeze block, so check (1) reds all six the day the CI row lands. B15 has no rule that a file belongs to one carrier, so FT's builder re-inventories 37 files, possibly with conflicting verdicts. Fix: add a seed row `forge-hooks (FH)` with its 42 frozen files and its `blocks`, name the six files in the migration, and add a check key: a frozen path in two carriers is red (FT's glob gets an exclusion).

**F12 (fix) prefix and id scope across parts.** HEAD says `prefix` is "unique across ledgers". The six hooks parts share `FH`, so check (1) reds them. Ids are said unique and increasing "in file order", with no scope across parts. Fix: the prefix is unique per carrier and shared by its parts, and ids are unique across all parts of a carrier. Check (5) looks across all ledgers, so a pilot split into parts does not red as "id gone".

**F13 (fix) proof `none -- <why>` is "the Architect's informed pass", but the performer writes it.** Practice: 82 of 162 carried rows in the hooks ledgers have `none --` (probe). WHO WRITES gives `carried` to the performer, and there is no decider for the proof. So half of the carried rows escape fidelity with no trace of whose pass it was. Fix: a `none` proof needs decider `architect <date>` (red otherwise), or the performer's `none` is legal and listed in `dropped` under "proof waived by performer" for the Architect.

**F14 (fix) the second layer of spec-copied drops and of card status.** (a) `dropped`, `decider: spec <key>` has no named reviewer. Code only resolves the key. In practice the Lead opened every such spec line (01:38, 111 rows). Name that step: the Lead at ledger acceptance. (b) A deferred card still resolves. A25 (deferred to the last phase, 01:38) is cited by 2 pilot rows, which read as carried in every view. Fix: rows naming a card with a deferred or withdrawn status line are listed apart in `dropped`/`waiting`. (c) `advice -- <page id>`: resolved against what, before the page exists? The behaviour is unstated.

**F15 (fix) an opposite: WHO WRITES contradicts MIGRATION.** WHO WRITES lets the performer write `dropped` only as a copy of an explicit spec drop. MIGRATION makes "the spec stating the OPPOSITE" a performer-written `dropped`. Practice is split 2 / 1: two `dropped` rows with an `opposite` note, and FH-3028 as `not-found` with an "opposite direction" note. An opposite is an implicit drop, possibly unknown to the spec's author, which is exactly where "forgotten" hides. Fix: an opposite is written as `not-found` with `note: opposite: <spec key>`, and the Architect decides.

**F16 (fix) the same behaviour in several files.** 14 rows in 14 files state the stdin 10-second deadline (probe). The builders flagged it as one theme (01:38). Coverage forces one row per file, so the Architect decides 14 times. Fix: a row whose note is `same as <id>` takes that row's verdict. The check verifies the id exists and the verdicts are equal.

**F17 (fix) the other recon ledgers.** B15 RELATIONS covers ideas-lessons, B11 and B7. It does not cover C1-1's carry map (fr:/fp: rows with carried/dropped verdicts, e.g. `dropped: fr:A14`, which B16 now moves) or C2-1's claim map. These are two existing ledgers of the same things the FR / PR carriers will hold, so there are two verdict records. Fix: one line. FR rows copy the map's verdicts (`decider: spec C1-1`), and the map stays the rule files' index, never a second verdict.

**F18 (fix) limits and worlds.** (a) "Never split inside a file", together with 300 rows per ledger: a single source over 300 rows has no way out. Practice max is 57 (`session_context.py`); `design/factory-rules.md` (504 lines) is unmeasured. State the behaviour (a file over the cap is its own part, with the cap lifted for it). (b) `topic` is `-` on all 808 hooks rows. The day `forge/worklist-rows.yaml` lands, check (2) reds every row, in a commit that only touches B11. State that `-` is `topic not set`, listed, not red, or name who fills it. (c) Check (5) "every id at base present at head": a mistaken or duplicate row has no door. State the door: `dropped`, `note: duplicate of <id>`, decider architect.

**F19 (fix, wording) what CI proves.** It is stated once, under FIDELITY. Repeat it in CHECK KEYS: "this row proves a decision exists, never fidelity; the second layer is the card critic's per-row answer". Readers of the CI row will not read FIDELITY.

Speed: about 1255 rows now, an estimated 6000 later, all text. No speed limit is stated, and none is needed. The 300-row cap is met by splitting (the pilot's 447 rows must split; the cap is stated, so this is not a finding).

## B16 -- forge rules

Yardstick: told at entry fails for builders (F24). A gate never hinders a right action: the mechanism count errs RED on a rename, with a door, so this holds. Old factory: the old third layer and fr:A14 return.

**F20 (blocker) phase unstated; deps tie (b) to phase 4.** B14 and B15 say "Phase 1", but B16 names no phase, and its deps include C4-6 (frame index: phase 4) and A30. Built as one card, it lands in phase 4. Then the PREDATES clause ("everything in the tree when B16 lands is the base (`born`)") exempts every tool, hook, data file and CI job of phases 1-3. The cost rule (b), the point of K2 / plan 00:54 row 5, protects nothing until most mechanisms exist. Fix: (a), (b) and (c) in phase 1 with deps C1-1, C1-2, C1-6 and B13. (d)'s `behaviour.json` and the C4-6 amendment land with C4-6 / A30, or (d) becomes its own card.

**F21 (blocker) a behaviour row can be silenced by nulling it, and "not set" has no end.** Unset rows are listed, never green, and excluded from the job's exit. Nothing forbids `measured: 12` going back to `null`. Case: `launches_per_story` measured 12 against ceiling 10 is red; the commit writes `measured: null`; the job is green. That is a silent escape from the card's own check line, "never raised silently". Nothing turns a row red that stays `not set` after its measuring task has produced a run, so it can stay unset forever. CI meanwhile shows `size` green with `not set` lines, and `all-green` green. Fix: set to unset is red against `--base`, like the `not_built` shrink-only rule (TESTING rule 6). A row whose named measuring task has an accepted run, or a phase close past it, may not be `null`: red `measure it or name why`.

**F22 (fix) the count is narrower than the rule's own text.** The rule says "a registry (a data file code reads), a hook". The count covers `forge/*.json` and `f/data/*.yaml` only. Missed: `forge/*.yaml` (B11 `worklist-rows.yaml`, B3 `owner-words.yaml`), B15's ledgers (read by `carry.py`), extensionless git hooks under `forge/hooks/git/` (only `*.py` directly under `forge/hooks` counts), and a hook registration in `.claude/settings.json` for an existing script. Fix: widen the globs, or list these in the error-direction line as named GREEN residuals.

**F23 (fix) a promise with no reader.** "`none -- prediction`, revisited at the first retro reading, B9": B9 is a dep but is not amended, and nothing makes B9 read commit `mechanism:` lines. Fix: amend B9 (the retro reading lists `none -- prediction` lines since the last reading), or drop the clause. Also say whether an accepted, unbuilt card's items may cite `card <id>`, instead of the builder inventing `origin`/`cost` that the spec card already holds.

**F24 (fix) told at entry: builders are refused by a rule they never read.** (b)'s rule text lives in `forge/COORDINATOR.md` (Lead/Architect). Builders read `CLAUDE.md` and commit the new tools, and CI reds their branch on a missing `mechanism:` line. Fix: one line in C1-1's builder hand-back duties in `CLAUDE.md`, or `dispatch.py new` printing `mechanism: owed for <counted paths in owns>`.

**F25 (fix) third layer: what stops growth.** The listed-function rule plus the reviewer is a judgment layer, and the card's check table says so. But (a) also allows "keep with a reason line under the rule" for a `none` table. That is an unbounded exemption list, against "Three, no fourth" and TESTING rule 2's "a test outside these layers is not written". Fix: the reason lines are a shrink-only grandfather list, counted by a `size_ratchet` row. Then neither the function list nor the exemptions grow silently (or state that only the reviewer stops growth, as a named residual).

**F26 (fix) `AGENTS.md` worlds.** The pointer to `forge/BOOT.md` (B1) is required content, and class (4) reds a pointer to a missing path. If C1-1 and B13 land before B1, CI is red. Only the `CLAUDE.md` world is stated. Fix: B1's builder adds the BOOT line, or class (4) prints `not judged: no forge/BOOT.md (B1)` until then.

**F27 (fix) (d) inputs.** (a) `behaviour.json` "absent at the named path -> exit 2". `measure/` reaches the remote only after F88's `measure_cleared` (B8), so a row set before that is red on Actions. Name the world and where the file lives. (b) "Rows per measuring task id": the key shape is unstated, and so is C1-2's scalar `stage_start_load: null` turning into `{ceiling, measured, run}` (amends names only its edge).

## Seam and class notes

- B14 and B15 both use B14 rule 4: the ledgers are hand files. With F1 unfixed, a `git stash` by one inventory session also removes another's ledger edit.
- F9 and F14(b) are one class: a row's validity depends on a card's lifecycle (accepted, deferred, amended), and none of the three cards models card status.

## Spot-checks (claims opened in their carriers)

- B14 amends C1-4 "the guess at the newest file withdrawn": holds. `journal.py::pick_session` falls back to the newest file, excluding `git-hooks.jsonl`.
- B14 "C1-1 carry map fr:A7-A11": holds (part 2, C1-1 `-> COORDINATOR.md: fr:A7-A11`).
- B16 "carry map `dropped: fr:A14`": holds (C1-1 `dropped: fr:A14, fp:A5 (replaced by plan 4.3)`).
- B16 "C1-2 edge `stage_start_load: null` -> exit 3" and TESTING rule 7 "exit 3 red on Actions": both hold.
- B15 `dispatch.py` `NAMES` and "gates nothing": holds (dispatch.py lines 10, 21).
- B15 `ci.py` `{base}` token and not_built shrink-only: holds (ci.py docstring; TESTING rule 6).
- B15 the 12-cell header: matches all six hooks ledgers. Heads lack glob/blocks/freeze (probe).
- B11 topics: seven (`stages` ... `hooks-ci`), with `in_work` a state: holds (part 4b-3).
- Negative "no B15 rule on themes": `grep -i theme` on B15's lines found two hits only: "the owner's view and the B11 import by theme group by it [topic]" and "a `waits-owner` row becomes a B11 `question` per theme". Neither says how a theme verdict becomes row verdicts. Positive control: the same grep counts 3 lines in `package-agents-themes.md`.

## Trail

- Read: part 5 sections 1-7 (B14 whole); part 6 section 1, B15 whole, sections 3-7; part 8 section 1, B16 whole, sections 3-7; the frame's index row for C4-6; part 2 C1-1, C1-2, C1-4, C1-5; part 4b B2; part 4b-2 B8, F86, F88, B9 line 27; part 4b-3 B11 (states, topics); plan records 26.11 00:08, 00:26, 00:54, 01:00, 01:04, 01:23, 01:38; `forge/TESTING.md`; `forge/tools/journal.py` whole; `forge/tools/dispatch.py` (grep); `forge/ci-jobs.json`; `forge-hooks.3.md` lines 1-40; `package-agents.md` head; `package-agents-themes.md` head and verdict lines; `code_ledger_check.py` whole. Not opened: `forge-hooks-themes.md` (in writing, excluded by the dispatch).
- Probe (scratchpad `t1966/probe.py`, read-only) over `forge-hooks.1..6.md`: 808 rows. No head has `glob:`, `blocks:` or a freeze block; all have `prefix: FH`. No limit breaches. 111 dropped, all `decider: spec`. 80 carried with a `K` proof, 82 with `none --`. 22 rows `not-found` + `where: none`. Opposite notes: 2 dropped, 1 not-found. 14 stdin-deadline rows in 14 files. Pilot: 447 rows; verdicts not-found 193, partly 143, found 98, spec-says-not-carried 13. Max rows per source: 57. Rows citing A25: pilot 2, hooks 0. Sources by folder: tools 37, .githooks 5.
- `git -C C:/QAFactory/forge2-repo log --oneline -1` -> `77eeb1a plan: six hooks ledgers accepted; ...`. `git worktree list` -> main only. `logs/journal/` in forge 2: absent.

```json
{
  "verdict": "blocker",
  "blockers": [
    "F1: B14 rule 3 / C1-5 -- destructive git commands on the shared main checkout (stash, reset --hard, checkout/restore of . or a dir, clean, switch) and the sweep through the door (commit -- ., add <dir>) are not refused; another session's uncommitted edit is lost silently",
    "F9: B15 -- not-found is a legal end state; rows with where none or naming already-dispatched cards are never forced to a verdict nor seen by a critic; K<n> unresolved; the check passes with nothing decided (535 not-found in the hooks ledgers)",
    "F10: B15 -- no road from a theme verdict to row verdicts: theme words outside the closed set, split themes, homes in unwritten cards A31-A35, no decider form; topic vs theme",
    "F20: B16 -- phase unstated; deps C4-6 (phase 4) and A30 delay the whole card, so PREDATES exempts every mechanism of phases 1-3; split (a)-(c) to phase 1",
    "F21: B16 -- a set behaviour row can be reset to null to silence a red; a not set row has no end"
  ],
  "fixes": [
    "F2: B14 -- state which tree the linked-worktree tests judge (tool root for single-writer tools; -C or subshell target for the git rule)",
    "F3: B14 -- exclude git-hooks.jsonl from neighbours; the session-id-change edge",
    "F4: B14 -- name what replaces the old overlap check of two writing dispatches",
    "F5: B14 -- a closing journal event on an already closed task prints the earlier close",
    "F6: B14 -- rule 6 commits dirty paths only with no live neighbour or the person's word",
    "F7: B14 -- empty-journal first id and a seed above the old forge's t-ids",
    "F8: B14 -- pre-push ci.py judging other sessions' uncommitted paths",
    "F11: B15 -- seed row for forge-hooks, its migration, one carrier per file (FT overlap 37 files, .githooks 5 in none)",
    "F12: B15 -- prefix per carrier shared by parts; id uniqueness across parts",
    "F13: B15 -- proof none written by performers (82 of 162) needs a decider or its own list",
    "F14: B15 -- reviewer of spec-copied drops; deferred cards (A25); advice page resolution",
    "F15: B15 -- opposite rows: WHO WRITES vs MIGRATION; the Architect decides",
    "F16: B15 -- same-as form for one behaviour in several files",
    "F17: B15 -- relation to C1-1 carry map and C2-1 claim map",
    "F18: B15 -- a file over 300 rows; topic dash after B11; door for a mistaken row under check (5)",
    "F19: B15 -- repeat the presence-not-fidelity sentence under CHECK KEYS",
    "F22: B16 -- the mechanism count misses forge/*.yaml, ledgers, extensionless git hooks, settings registrations",
    "F23: B16 -- B9 not amended to revisit prediction lines; card-cited lines for accepted cards",
    "F24: B16 -- builders are refused by a rule only in COORDINATOR.md; tell it in CLAUDE.md or dispatch.py",
    "F25: B16 -- kept none tables are an unbounded exemption list; make it shrink-only and counted",
    "F26: B16 -- AGENTS.md pointer to forge/BOOT.md before B1",
    "F27: B16 -- behaviour.json before measure/ is pushed (F88); row key shape and the stage_start_load scalar-to-object change"
  ],
  "class_completeness": "B14 fixes the sweeping add/commit instance of the shared-checkout surface but not the destructive siblings (F1). B15 and B16 both leave the card-lifecycle class (accepted, deferred, amended) unmodelled (F9, F14b, F20). Siblings outside the three cards are not judged (plan gate).",
  "trail": {
    "read": [
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part5.md",
      "C:/QAFactory/forge2-repo/forge/specs/20261126-forge2-light-factory-spec-part6.md",
      "C:/QAFactory/forge2-repo/forge/specs/20261126-forge2-light-factory-spec-part8.md",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part2.md (C1-1, C1-2, C1-4, C1-5)",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4b.md (B2)",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4b-2.md (B8, F86, F88)",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4b-3.md (B11 grep)",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-plan.md (records 26.11 00:08-01:38)",
      "C:/QAFactory/forge2-repo/forge/tools/journal.py",
      "C:/QAFactory/forge2-repo/forge/TESTING.md",
      "C:/QAFactory/forge2-repo/forge/ci-jobs.json",
      "C:/QAFactory/forge2-repo/forge/specs/recon/carry/forge-hooks.3.md (head)",
      "C:/QAFactory/forge2-repo/forge/specs/recon/carry/package-agents.md (head)",
      "C:/QAFactory/forge2-repo/forge/specs/recon/carry/package-agents-themes.md (head, verdicts)",
      "C:/Users/<user>/AppData/Local/Temp/claude/b3e3188b390a00d9/019810c0-e93d-4fda-81cb-1c435f3c0f3c/scratchpad/code_ledger_check.py"
    ],
    "reruns": [
      {"command": "python -B <scratchpad>/t1966/probe.py", "result": "808 rows; heads lack glob/blocks/freeze; prefix FH x6; dropped 111 all spec; carried proofs K 80, none 82; not-found where none 22; opposite dropped 2, not-found 1; stdin-deadline rows 14 in 14 files; pilot not-found 193 partly 143 found 98 spec-says-not-carried 13"},
      {"command": "git -C C:/QAFactory/forge2-repo log --oneline -1", "result": "77eeb1a plan: six hooks ledgers accepted; a stage is a role (themes T1, T6 corrected); card A25 deferred to the last phase"},
      {"command": "sources by folder over forge-hooks.[1-6].md", "result": "5 .githooks, 37 tools"}
    ]
  },
  "mutants": [],
  "mutants_none": "plan gate: no diff and no new behaviour to probe"
}
```
