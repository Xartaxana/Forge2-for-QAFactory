# t-1974 -- critic, plan gate: forge 2 spec part 9, cards B18, B20, B21 (topic 2)

Reviewed state: forge 2 `980a437` (git -C C:/QAFactory/forge2-repo log --oneline -1, clean tree). Frame: section 1 of part 9 and the owner's yardstick from the dispatch. The Lead's fork decisions (plan record 26.11.2026 ~02:24: F190-F196 (a)) are taken as given.

- B18: blocker -- F1, F2 block; F3-F7 fixes
- B20: blocker -- F8, F9 block; F10-F13 fixes
- B21: fit_with_fixes -- F14-F19 (F6 also touches B21 line 9)

Verdict line (rule 6): REJECT, failure_class: spec -- 4 blocking findings, 15 fixes. Each blocker has a one-paragraph fix. Accepting, or sending the cards back, is the Lead's decision.

Owner's yardstick, per card:
- B18: does more than a free agent (the witness is a run made by the tool, not a summary). But the gate lets unfinished work through on the usual road (F1, F2), and the held-owns check does not refuse and names no door (F3).
- B20: the shrink-only rule and named raises are carried. But a ratchet can still be passed by deleting rows while the scanner finds nothing (F8). Two of the card's own requirements leave a state with no way out (F9).
- B21: the rule lines are told at entry. Line 7 says what the owner's four points say, but it cites a record that holds the withdrawn reading and points at a door that B18 drops (F14). The useful rows of H20 are named in no card (F18).

## Findings

**F1 (B18 (a), blocker) -- the role is read from the LAST dispatch, so a builder's work reviewed by a critic is accepted with no witness.** Place: (a) "when the task's last `dispatch` note starts `role:builder` ... `--run` is required"; K1 "a critic task's accept without `--run` -> written". B14 rule 1 sends the critic under the same task id ("`--task` on a `dispatch` names an existing id only (a next attempt, a critic of the same task)"), and B18 (e) says the same ("a critic of the SAME task never flags"). Case: `dispatch t-5 role:builder` -> builder hands back -> `dispatch --task t-5 role:critic` -> critic returns -> `journal.py --event accept --task t-5` with no `--run`. The last note is `role:critic`, so the line is written with no witness. This is the normal road, because fr:A7 asks for critic input on acceptance. Smallest fix: `--run` is required when ANY `dispatch` of the task since its last closing event has a note `role:builder`, or has a note whose role cannot be read. Add a K1 row: builder, then critic, then accept with no `--run` -> refused.

**F2 (B18 (a) with B21 line 4, blocker) -- the witness runs in the wrong tree; the two cards disagree on when acceptance happens.** Place: B18 (a) "the tool runs the command (shell, cwd = `--root`)". B14 rule 4 makes `--root` the main checkout (a linked-worktree root is refused). B21 line 4 judges owns "at acceptance by `git diff --name-only main...w/<task>`", and B17's sweep keeps a worktree until its branch is in main. Both mean acceptance comes BEFORE the fast-forward. Case: builder t-5 commits `forge/tools/refs.py` on `w/t-5`. The Lead runs `accept --task t-5 --run "python -m pytest forge/tests/test_refs.py -q"`. The run happens in the main checkout, which does not hold the branch, so it tests the old main. It goes green (or "no tests"), and that becomes the witness: the stale-witness failure H27 names. If the Lead instead fast-forwards first, `main...w/t-5` is empty and line 4's owns check passes on nothing. Smallest fix: (1) B18 (a): run in the linked worktree of branch `w/<task>` when `git worktree list` holds one, else in `--root`. `witness` gains `tree` and `head` (the sha the run judged). (2) B21 line 4 states that acceptance comes before the fast-forward.

**F3 (B18 (e), fix) -- held owns: the verdict, the door and the comparison are left open.** (i) B18 says "flags `held: ...`"; B14 rule 3 says B18 "refuses it at dispatch". The exit code of `held` is not stated, and no door is named. Fix: exit 1, door "return or accept `<task>` if it is dead or done (B14 rule 6), or narrow your owns". (ii) "contains or lies inside" by string prefix flags `C:/r/forge/tools2/x.py` against owns `C:/r/forge/tools`. Fix: compare by path components (`os.path.commonpath`). (iii) A stored ` (new)` mark makes `x.py (new)` differ from `x.py`. Fix: strip the mark before comparing. (iv) Order: the edge "the dispatch already passed `check`'s 200" assumes check comes before the journal line. B14 rule 1 issues the id at `--event dispatch`, before the dispatch text exists. Fix: state journal first, then check. Then two sessions dispatching at once each see the other's line. (v) After `accept`, and before the fast-forward, the path is no longer held. Case: t-2 is accepted with CI pending; t-3 owns the same file and is cut from main without t-2's change, so the fast-forward conflicts. Fix: held = open, OR closed with branch `w/<task>` not yet in `refs/heads/main` (B17's "in main" test).

**F4 (B18 (d), fix) -- what counts as a given path, and the 200 limit.** (i) "an entry that ... holds `/` or `\`" is treated as a path. Cases: `given: https://github.com/o/r/pull/3`, and `given: C:/x/spec.md -- the frame` (a hand-written path plus a description). Both become `given missing`, a refusal of a right dispatch, and the exit code of `given missing` / `owns missing` is not stated either. Fix: an entry with `://` is not a path. Only the first whitespace-free word of an entry is the path. State exit 1 with the door "write the absolute path, or prose without a slash". (ii) Over 200 entries -> exit 1, with no door. FH-6046 said over 200 is a note and the dispatch goes out, so the row is "carried differently", not "carried". Fix: name the door ("own the directory, or split the dispatch") and relabel the row.

**F5 (B18 edges, fix) -- the trim claims do not hold.** (i) "each line cut to 200 characters with `...` ... C1-4's trim rule": C1-4 and the built `forge/tools/trim.py` cut no line by width, and the stated `trim_lines(lines, last=30, keep=())` has no width parameter. (ii) "1 GB output -> memory bounded": trim reads line by line (`for chunk in src`), so 1 GB on one line, such as a progress bar or binary output, is held whole in memory. (iii) Whether stderr is merged is not stated, and a red run's cause is often on stderr. (iv) A run longer than the harness call limit is killed and nothing is written, and no door is named. (v) A 1 GB test row breaks TESTING's 10 s file budget. Fix: read in fixed blocks and cut each line at 200 while reading; merge stderr into stdout; name the door "run the accept as a background call"; make the test row 10^6 short lines plus one 10 MB line.

**F6 (B18 (c), (f) and B21 line 9, fix) -- the three rule lines repeat rules that are already carried.** "A second reject ... moves it one tier up" is fr:A13 ("Two failed attempts move the work one tier up"), which C1-1 already carries to COORDINATOR. "Acceptance belongs to the Lead" is fr:A7, and B21 line 6 already extends fr:A7. The new wording also changes the meaning: "the Lead" lets the Lead accept its own main-checkout edit, while fr:A7 says no session certifies its own work. The cases are rows of the old rules (FH-1038 is "COORDINATOR rule 6"; FH-6111 is a refusal rule), not events. The B14 rule 3 sentence (FH-6064) repeats B14 rule 3's existing "push before a worktree launch", and its "or cut from local main" alternative drops that line's purpose ("a main the remote holds"). The reject count also mixes roles: a refused critic output under t-5 counts toward the builder's tier. Fix: add FH-1038 as a case of fr:A13; add FH-6111 to line 6's fr:A7 case, worded "a worker never writes accept or reject"; add FH-6064 as a case of B14's existing line and drop the new sentence; count only rejects whose closed dispatch is `role:builder`.

**F7 (B18 (a), fix) -- the witness command is not tied to the dispatched DoD.** Case: `--run "exit 0"`, or a narrower test than the dispatch's `DoD:`, gives a valid witness. Fix: store `dod` on the `dispatch` line (as `owns`), and at accept print `run differs from the dispatched DoD: <dod>` (a printed line, no refusal: the Lead's choice stays visible).

**F8 (B20 (c)/(d), blocker) -- a ratchet can be passed by deleting rows: the dead-scanner guard can never fire.** Place: (d) "found zero sites while its allow list holds rows it did not mark stale -> exit 2". Trace: zero sites means every row suppresses nothing, so (c) marks every row stale, so the set "rows it did not mark stale" is empty, so the condition is never true. The run is red `stale` x N with the door "`--update` shrinks it with no record". After the update the scanner is still dead, it still reads files, there are no rows left, and the result is green from then on. Case: a scope root that no longer exists in the real repository while the fixture tests stay green, or a scanner bug that the tests miss. Smallest fix: zero sites while at least one row exists -> exit 2 `cannot judge: scanner found nothing`, judged BEFORE the stale rule. The door for a real full clean-up is a seeded positive control: each tool's own sample must be found in the same run, or `--update` refuses to remove all rows of a file without a `ratchet-raise:`-style record.

**F9 (B20 (e) with (c), blocker) -- an absolute path leaves a state with no way out.** (e) says an absolute path outside the repo "exists on this machine or red (door: an `allow` row ... a path only CI lacks)". (c) says a row that suppresses nothing is red. Case: a rule file cites `C:/QAFactory/forge-repo/tools/lint_ratchet.py`. On the developer's machine the path exists, so the allow row suppresses nothing and is red; pre-push runs `ci.py` locally, so the push is refused. Without the row, CI on Linux is red. The same happens to an absolute path INTO the repo (`C:/QAFactory/forge2-repo/forge/BOOT.md`): on CI the checkout lives under another root, so it reads as "outside the repo". Fix: an absolute path whose root is the repository's local root is resolved repo-relative on every machine. Any other absolute path is printed `not judged: outside the repository` and never red, so no allow row is needed and no row goes stale.

**F10 (B20 (c), fix) -- B13's `legacy` rows have no `reason` field.** (c) applies "no `reason` -> red" to "B13 `refs.json` `allow` and `legacy`". B13's schema is `legacy` (`file`, `tokens`), so every legacy row would be red on the day B20 lands. Fix: the reason rule applies to `allow` and baseline rows only, or B20 amends B13 with a `reason` field.

**F11 (B20 (b)/(d), fix) -- narrowing the scope by editing code, and the basis door.** (i) "a scanned root removed" is detected only when the roots are data. C1-2 and C1-3 name their scopes inside the tools, so deleting `factory/hooks` from `universality.py`, or a directory from C1-3's scope, needs no raise line. Fix: the scan roots are a basis key (or a `roots` key in the data file), so narrowing them reads as a basis change. (ii) The basis door is "`--update` on the new basis with a record" (one record), but (d) asks for one `ratchet-raise:` line per added row, and a normaliser bump re-keys every clone row. Fix: one line `ratchet-raise: <file> basis -- <id>` covers the rows re-keyed in the same commit. (iii) A local run on another Python minor (CI pins 3.12 in `.github/workflows/ci.yml:29`) -> exit 3 `not judged here`, not exit 2, so pre-push is not stuck; Actions is the judge.

**F12 (B20 (e), fix) -- "a file suffix" is undefined, and bare file names go red.** Case: COORDINATOR writes `journal.py --event accept` or `BOOT.md`. These are neither repo-relative paths nor placeholders, so they are red and need an allow row per mention, a gate in the way of a right action. `3.1` or `e.g.` in backticks has a "suffix" too. Fix: a closed suffix list (`.md .py .json .jsonl .yaml .yml .ps1 .sh .toml .txt`). A token with no slash resolves by basename among tracked files (at least one match). For a token with spaces, only its path-shaped word is judged.

**F13 (B20 (d) and section 4, fix) -- three wording gaps.** (i) The `budget-raise:` alias is "kept ... for one release of the rule", but no tool reads the old keyword (`size_ratchet.py` is unbuilt in forge 2: `forge/tools/` holds ci, dispatch, journal, snapshot, trim) and nothing ends the window. Drop it. (ii) The residual "a W-id that exists but does not say this raise" is not named; B3 and B11 name the same residual. (iii) FH-6083 (diverged = green with a hint) is listed "carried" while (c) makes the row red. Say it is red `stale` with the hint, and mark it "carried differently".

**F14 (B21 line 7 and the tempo paragraph, fix) -- the tempo line.** The four points the dispatch names are present: six as the goal and no fewer with parallel work, a seventh through a door, never at the cost of efficiency, and a narrower limit for one session. Gaps: (i) the fallback "cites the plan record 01:58". That record says «больше шести разом не запускаем» (plan line 3397-3398), the reading withdrawn at ~02:24 item 3, so a reader following the citation gets the opposite of her words. Cite ~02:24 item 3. (ii) The world-1 wording is not given: the table text says "the owner's tempo word" even when there is no W-id. Fix: before the record exists the case reads `(case: plan 26.11 ~02:24 item 3 -- the owner's words await their record)`. Since B21 lands after B3, the simpler fix is that the Lead's `words.py add` is the first step of B21's landing. (iii) "Through a named door" names no door, and B18 drops FH-6053 (`budget-skip:`, "the counting code is dropped"). Name it, e.g. "the reason in the dispatch note `seventh: <why>`". (iv) Her clause «дизайнеры, критики и скауты в счёт не идут и слота не ждут» (PROJECT.md:186-187) is missing; add "readers are not counted and never wait for a slot". (v) B3's `date` holds one date, while the words carry 13.11 and 16.11. Fix: two records, or `date` = 2026-11-16 with the carrier line.

**F15 (B21 line 5 and amends, fix) -- the home of fr:B3.** Line 5's home is "CLAUDE.md critic section (fr:B3)", but C1-1's carry map sends fr:B3 to COORDINATOR.md (part2:88, "-> COORDINATOR.md: ... B1-B6"). C1-1 K2 wants each id in exactly one file. The amendment "fr:B3's 'verdict JSON' -> 'verdict lines (B21)'" changes a phrase that is not in C1-1: it is in the recon row (`recon/20261125-forge2-recon-forge-rules.md:43`). Fix: amend C1-1's carry map so that fr:B3 moves to CLAUDE.md (critics read CLAUDE.md), carried without "verdict JSON".

**F16 (B21 amends B1, fix) -- the BOOT pointer line conflicts with B1.** B1's line classes are closed: an owner word, a plan line, or one of the two lines exempt by name. B1 K2 reds any other uncited line, and an edit to a BOOT rule line reruns B1's six-run eval. Part 9 section 6 leaves this "to the Lead at the B1 pass", and B21's cost line ("rule text only") leaves out the eval rerun. Fix: drop the BOOT line, because line 4 already holds the diff command in COORDINATOR (H18 carried differently), or cite it as a plan line and state the eval rerun in the cost.

**F17 (B21 work-list records, fix) -- the records do not match B11's `add`.** (i) The title says "four work-list records", while Delivers has R1-R5 and K4 and section 5 say five; the title's theme list leaves out H30 (R4). (ii) B11's `add` needs `--kind --topic --text --source`. The source kinds are `retro | run | critic | owner | snag | session`, and none names a themes-file verdict. The promoting case fits B11's `held` with `probe {action, who}`, not free text. Fix: per record, `--kind task --topic hooks-ci` (R4: `forge-rules`), `--source session:<the landing session's stem>`, then `set --state held --probe-action "<promoting case>" --probe-who lead`, with the rows in `text` (<= 500 characters). (iii) FH-4047 and FH-4048 are "NOT TAKEN (go with R3 if promoted)" but are missing from R3's rows, so a promoted R3 would lose them. Fix: list them in R3.

**F18 (B21 rows and line 8, fix) -- H20's rows are named in no card.** Line 8 is H20's line (F194 (a)), but B21's rows line counts H1, H15, H18, H26, H27, H36 = 79. The 14 rows of H20 (FH-2083..2096, FH-4129) appear in no card of part 9 (Grep `FH-2083` over the specs: themes file and ledger only). Line 8's case, "main-red tracking dropped because main is protected", is the reason for dropping something, not a case of the rule. FH-6049 is listed "carried", but line 7 says its code is not carried. Fix: add `H20 14: carried differently 14 (line 8; B8 protects main)`. Make line 8's case FH-2093 (the old flaky queue). Relabel FH-6049 "carried differently (purpose as line 7)".

**F19 (B21 cases, fix) -- an FH ledger row is not one of C1-1's case carriers.** C1-1 defines a case as "(run, journal line, retro, owner's word)". Lines 1, 3, 4, 5 and 6 cite FH rows, which describe old-forge code. Fix: one sentence in C1-1 K3 that admits `FH-<n>` (the old forge's mechanism as precedent), or cite the theme's "what it was for". Ceilings: not judged, because C1-1's text is unbuilt. The table sums to 2310 B against "about 2.2 KB"; the edge (merge, never raise) covers an overrun.

## Seam and class notes

- F1 and F2 belong to one surface, the acceptance moment. Its neighbours: B17's sweep (accept before the fast-forward: consistent with F2's fix), B14 rule 6 (a late close is printed: unaffected), and B9's reject count (F6, roles mixed).
- F8's class is every allow list under the (c) rule: C1-3 baselines, `universality-names.json`, `refs.json`. The one-rule fix covers all of them.
- F9 belongs to the path-resolution surface. B13's class (2) also reads paths, but by line-reference tokens, not existence, so it is not affected.
- The dropped rows of H1, H2, H6, H8, H10, H15, H18, H21, H23, H26, H27, H30, H35-H37 and H40 that these cards name each carry a reason, with two exceptions: H20's rows (F18), and FH-6053, whose door B21 line 7 still needs (F14). H9 and H38 belong to B19 (topic 1) and were not judged here.

## Spot-checks (claims verified at their carriers)

- B18 counts: H6 20, H8 20, H23 10, H35 6, H36 5 (+FH-6049 in B21) and H40 4 rows, against the `rows not-found` lines of the themes file (lines 63, 81, 216, 324, 333, 369). Carried 21 + not taken 44 = 65, recounted by hand. Holds.
- B20 counts: 24 + 1 + 20 = 45, against the H10, H21, H30 and H37 lists (themes file lines 99, 198, 279, 342). Holds.
- B21 counts: 17 + 2 + 60 = 79 and H2 4 + 1 + 20 = 25. Holds.
- C1-3's edge "fixed offender -> `gone`, green, removed by `--update`" (part2:111) and C1-2's `budget-raise: <key> -- owner <date> «<words>»` (part2:99) exist as B20 quotes them.
- B2's note form "note starts `role:<role>`" (part4b:65). B14 sends a critic under the same task id (part5:70). The built `forge/tools/dispatch.py` has a `task:` header line (NAMES, line 21), so "the same task never flags" is buildable.
- The built `trim.py` has no line-width cut and reads line by line (lines 35-50).
- The built `ci.py` `resolve_base` falls back to the merge-base with `origin/<default>` for a zero `before` (ci.py:85-101), so B20's "no base" happens only on a local run without `--base`. No finding.
- The tempo words are at PROJECT.md:185-191 (item 12). The withdrawn reading is at plan line 3397-3398, and the correction at plan ~02:24 item 3 (line 3516-3520).
- Negative claim "FH-2083 named in no part-9 card": Grep `FH-2083|H20|FH-1059|FH-3045` over `forge/specs/*.md`. The positive control is the same call finding FH-1059 and FH-3045 in part 9 (lines 92, 115, 123); FH-2083 is found only in the themes file and ledger 2.

## Trail

- Read: part 9 lines 1-31, 48-64, 77-183 (B18, B20, B21, sections 1, 3-7); plan records 26.11.2026 ~01:45 to ~02:24 (lines 3320-3527); PROJECT.md:183-191; part 2 C1-1..C1-6 (lines 83-140); part 4b B1-B3, B5 (lines 51-81, 110-114); part 4b-3 B11 (41-49); part 4b-4 B13 (13-20); part 5 B14 (67-81); the themes file (verdict lines of all 40 themes, H36 and H7 whole); the ledger rows by id (Grep over `recon/carry/forge-hooks.*.md`); `recon/20261125-forge2-recon-forge-rules.md` rows A4, A7, A11, A13, A30, B1, B3; the built `forge/tools/trim.py` (whole), `dispatch.py`, `journal.py` (structure), `ci.py:1-30, 85-135`; `.github/workflows/ci.yml` (base and python-version lines).
- Commands: `git -C C:/QAFactory/forge2-repo log --oneline -1` -> `980a437 specs: parts 5-9 after the fix rounds; plan record on the batch acceptance`; `git -C ... status --porcelain` -> empty; `python --version` -> `Python 3.12.10`; grep `python-version` in ci.yml -> lines 29, 58 `"3.12"`.
- No probe: plan gate, no code under review.

```json
{
  "verdict": "blocker",
  "blockers": [
    "F1: B18 (a) reads the role from the last dispatch; a critic dispatched under the same task id makes a builder accept pass with no witness. Fix: --run required when any dispatch of the task since its last close is role:builder or has an unreadable role.",
    "F2: B18 (a) runs the witness with cwd = --root (the main checkout) while B21 line 4 and B17 put acceptance before the fast-forward; the run judges old main. Fix: run in the linked worktree of w/<task> when it exists, record tree and head sha in witness; B21 line 4 states acceptance precedes the fast-forward.",
    "F8: B20 (d) dead-scanner clause is unreachable (zero sites marks every row stale), so --update wipes the rows with no record and a dead scanner stays green. Fix: zero sites with at least one row -> exit 2 before the stale rule; a full clean-up needs a seeded positive control or a record.",
    "F9: B20 (e) with (c): an absolute path present locally and absent on CI needs an allow row that is stale locally; pre-push red either way, and repo-absolute paths read as outside on CI. Fix: resolve repo-root absolute paths repo-relative; any other absolute path printed not judged, never red."
  ],
  "fixes": [
    "F3: B18 (e) held owns: exit 1 with a door, component-wise comparison, strip the (new) mark, journal line before check, held also while closed and branch not in main.",
    "F4: B18 (d): URLs and path-plus-description entries are not paths; state exit codes and doors; the over-200 row is carried differently and needs a door.",
    "F5: B18 edges: per-line 200-char cut is not in C1-4 or trim.py; one huge line is unbounded; merge stderr; name the background door; shrink the 1 GB test row.",
    "F6: B18 (c), (f), B21 line 9: the tier and acceptance lines double fr:A13 and fr:A7; the B14 sentence doubles B14 rule 3; add the cases to the carried rules; count builder rejects only.",
    "F7: B18 (a): store the dispatched DoD and print a line when --run differs.",
    "F10: B20 (c): B13 legacy rows have no reason field; scope the reason rule or amend B13.",
    "F11: B20 (b)/(d): scan roots as a basis key; one basis raise line covers re-keyed rows; another local Python minor -> exit 3.",
    "F12: B20 (e): closed suffix list; bare names resolved by basename; only the path-shaped word of a spaced token judged.",
    "F13: B20: drop the budget-raise alias; name the W-id-does-not-say-it residual; FH-6083 red stale, carried differently.",
    "F14: B21 line 7: cite plan 02:24 item 3, not 01:58; give the world-1 wording or add the record first; name the seventh's door; add the readers-not-counted clause; two dates.",
    "F15: B21 line 5: move fr:B3 to CLAUDE.md in the C1-1 carry map; the verdict JSON phrase is in the recon row, not C1-1.",
    "F16: B21: the BOOT pointer line breaks B1's closed line classes and triggers B1's eval; drop it or state the cost.",
    "F17: B21 records: five not four; map kind, topic, source session stem, held with probe; add FH-4047 and FH-4048 to R3.",
    "F18: B21 rows: account H20's 14 rows; line 8 case FH-2093; FH-6049 carried differently.",
    "F19: B21 cases: admit FH rows in C1-1 K3 or cite the theme's incident; ceilings not judged (C1-1 unbuilt)."
  ],
  "class_completeness": "Acceptance moment (F1, F2) walked across B17 sweep, B14 rule 6, B9 counts; the stale rule (F8) applies to every allow list of B20 (c) and the fix is one rule; path resolution (F9) checked against B13 class (2), unaffected; the B11/B13 --base siblings checked against built ci.py resolve_base, no finding.",
  "trail": {
    "read": [
      "C:/QAFactory/forge2-repo/forge/specs/20261126-forge2-light-factory-spec-part9.md:1-31,48-64,77-183",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-plan.md:3320-3527",
      "C:/QAFactory/forge-repo/PROJECT.md:183-191",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part2.md:83-140",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4b.md:51-81,110-114",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4b-3.md:41-49",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4b-4.md:13-20",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part5.md:67-81",
      "C:/QAFactory/forge2-repo/forge/specs/recon/carry/forge-hooks-themes.md (verdict lines; H7, H36 whole)",
      "C:/QAFactory/forge2-repo/forge/specs/recon/carry/forge-hooks.1..6.md (rows by id)",
      "C:/QAFactory/forge2-repo/forge/specs/recon/20261125-forge2-recon-forge-rules.md rows A4,A7,A11,A13,A30,B1,B3",
      "C:/QAFactory/forge2-repo/forge/tools/trim.py, dispatch.py, journal.py, ci.py:1-30,85-135",
      "C:/QAFactory/forge2-repo/.github/workflows/ci.yml"
    ],
    "reruns": [
      {"command": "git -C C:/QAFactory/forge2-repo log --oneline -1", "result": "980a437 specs: parts 5-9 after the fix rounds; plan record on the batch acceptance"},
      {"command": "git -C C:/QAFactory/forge2-repo status --porcelain", "result": "(empty)"},
      {"command": "grep -n -i python-version .github/workflows/ci.yml", "result": "29: python-version: \"3.12\"; 58: python-version: \"3.12\""},
      {"command": "Grep FH-2083|H20|FH-1059|FH-3045 over forge/specs/*.md", "result": "FH-2083 only in themes file and forge-hooks.2.md; FH-1059 and FH-3045 found in part9 (positive control)"}
    ]
  },
  "mutants": [],
  "mutants_none": "plan gate: no code under review, no worktree named by the dispatch"
}
```
