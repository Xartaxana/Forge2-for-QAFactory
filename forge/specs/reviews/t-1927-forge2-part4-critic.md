# t-1927 -- critic on the plan: spec part 4 (cards A1-A23, forks F70-F76) at 6799870b6

Spec under review: `docs/tasks/specs/20261125-forge2-light-factory-spec-part4.md`. DoD: plan v1.9 plus the owner's records of 25.11 ~20:50, ~20:56, ~21:01 and (Lead's addition mid-task) ~21:13. Plan gate (rule 24). Every card was covered; nothing was left out for lack of budget.

## Card by card

- A1: findings F2, F3, F4. The token measure is not named, so the 300000 cap may fire in a few turns. The 1200 s wall cap is below the 1800 s test timeout. The story cap counts the person's wait at stops.
- A2: finding F5. Tests that sit next to product code (same directory, or inside the source file) cannot be written without opening the product directory. F71's "folded into the plan" has no carrier anywhere. By default there is no `tests` root, so the first test write of every story is refused.
- A3: findings F1, F6. G6.4 has no `when` and no debtor. At `exit` or `after_critic` it deadlocks against the report stop that asks its question. It counts "answered", not "confirmed".
- A4: findings F7, F8, F17. K1 is a mid-stage refusal of a row a later answer makes valid, and omitting `found_while` bypasses it. The `explore` launch of F74 has no move in C4-1 and no tools. The "proposed test" question of ~21:13 is missing.
- A5: findings F9, F10, F17. There is no assumptions list (~21:13). When `chat_language` is absent the chat silently falls back to the repository language. The stage-1 `--rows <file>` has no `write` tool kind (A12).
- A6: finding F11. "Every chat message incl. questions in the person's language" has no carrier in C4-3 or C3-5, and C4-3 is not in the section-4 index for A6. `source_must_be` bypass: see F12.
- A7: finding F1. G4.6 never falls due (exit column), and it has no predicate. Otherwise ok.
- A8: findings F1, F13. Every hunk must be named by id, never by pattern: thousands of lockfile or generated hunks against the A1 token cap. Hunk id stability is not stated. G3.5 never falls due.
- A9: finding F14. `product_build` is copied from the latest probe, not measured at the run, so a redeployed stand gives greens with a stale identity that count.
- A10: finding F12. `source_must_be: person` is enforced only against the literal `found:` prefix: any other string passes as "the person's words". The refusal names no door (AR-9).
- A11: ok
- A12: findings F9, F15. Tools are per stage only. The critic, conductor, explore and fix-round launch kinds carry none, although the A22 probes need `write`. Stage 1 has no `write`, yet A5 needs a rows file.
- A13: ok
- A14: finding F3. The default timeout of 1800 s exceeds the stage wall cap of 1200 s, so the "second timeout" move is unreachable and a 25-minute suite is cut every time.
- A15: ok
- A16: findings F1, F16. The `tests_commit` base misses uncommitted test files, so every stage-4 file shows as "changed after the red". The file-to-red pairing is not scoped. A fix through a revised `expectations` row (cause `case_or_expectation_error`) has no label. The reds stage pays for files changed by the tests stage's late-requirement shortfall.
- A17: ok
- A18: ok (seam with B2 below)
- A19: finding F18 (non-blocking). The question goes outside `ask.py` (AR-16) without naming the exception, and the "yes" cannot be recorded with no Python.
- A20: ok
- A21: ok
- A22: finding F19. The shared probe run has no rule for cross-attribution: a substitution in a shared helper or a shared mock, or one collection error, turns every probe of the run into a false kill. An inversion is not marked apart from a value substitution in the report (owner ~21:01: "not enough"). The C4-2 edge text still speaks of a "broken product".
- A23: finding F20 (non-blocking). It removes `lower_seq`, but its own edge keeps the order for G5.4 `new_expectation` without naming the predicate that now does that (`later_row` or a new one).

## Findings in full

**F1 (blocks; A3, A7, A8, A16; Q3 + Q1).** The four new gate rows never fall due, and they are never told at entry. Part 3 C3-2 (part3:45): "The `exit` column is the one source of where a rule falls DUE." None of A3, A7, A8, A16 amends the C3-2 `exit` column. The section-4 index lists C3-2 only for A3, A4, A8, A10, A12, and section 6 says `stages.yaml` changes in "A3, A8, A12 only" (leaves and tools). Two consequences:
- `exit_check.py` never computes G3.5, G4.6, G5.4 or G6.4.
- `## How checked` is generated from the rules the stage's exit names (part2b:6; frame 2c has no `page` field). So the section-1 promise "every new gate row names its stage's page" has no mechanism.

Second half: C3-3's predicate list is CLOSED (part3:74; an unknown predicate is W1/CI red). The rows need predicates the list lacks:
- G4.6: a path under `mock_base`.
- G5.4: reads the `world.py test-diff` output.
- G6.4: an answered question naming a row.
- G3.5: might reuse `xref_both_ways`, but no card says so.

A23 edits that same list, which shows it was known. Fix: amend the C3-2 exit column (G3.5 at `plan`, G4.6 at `tests`, G5.4 at `reds`, G6.4 at `report`, with `when`) and the C3-3 predicate list, and add both to section 4.

**F2 (blocks; A1; Q6, Q2).** "300000 tokens" names no measure. Claude Code's per-message usage carries `cache_read_input_tokens`. A cumulative sum over 80 turns with a 40-60 KB context passes 300000 in about 6-10 turns. B5 in part 4b measures the CONTEXT SIZE from the transcript (`agent_budget.py:46-47`), and that is the measure the carried numbers were set for. A1 reads a "usage stream". Concrete case: an ordinary stage-4 launch is cut at turn 8, three times, and the person is asked. That refuses a correct action. Fix: name the measure (context size, as B5, or in+out without cache reads) in the profile row `usage_stream`.

**F3 (blocks; A1 x A14 x C4-4).** Data rows conflict. The stage `wall_s` is 1200, while `test_timeout_s` is 1800 (part3:191, part3b:53) and A14 says "default 1800 s". A14 also says "a launch cap during a run -> the cut wins". Concrete case: a 25-minute suite is cut at 20 minutes on every relaunch, the third cut puts a question to the person, and A14's diagnostic road never runs. Fix: an invariant `test timeout < wall_s of the launching kind`, checked by `rows.py`, or a wall cap that excludes the wait for a `run_tests.py` child (the timeout already bounds it).

**F4 (blocks; A1, F70).** The story wall cap (2 h) is measured by the wall clock. Nothing excludes `at_stop`/`held` time, which is the person's time: `stop_wait` is a separate field in 2f. Concrete case: the person answers the understanding stop after 3 hours, and the story cap fires before stage 2 begins. Fix: the story wall excludes `stop_wait`; state it as an edge.

**F5 (blocks; A2, F71; Q2, VARIETY axis 1).**
- (a) "Longest matching root" assumes tests live in their own directory. Go `_test.go` files share the product package directory. Rust unit tests sit inside the product source file. JS/TS `*.spec.ts` and `__tests__` sit beside components. Registering such a directory as a `tests` root opens product code for writing, and not registering it refuses every test write. Either way the invariant of A2 breaks for a whole language family. Fix: a data row by test-file form (the runner-forms glob, already the axis 3 carrier) applied inside a product root. A path matching a test-file form is writable, the rest stays closed; for a source file that holds inline tests, the permission door is named as the known cost.
- (b) F71 was decided as "folded into the test-plan approval (the plan names the tests root)". No card carries it: no C3-5 test_plan section, no G-row, no `knowledge.py set repositories` road from the approval answer. Meanwhile the C3-6 default is "project root, product", so there is no `tests` root at all, and the first test write of every story is refused mid-stage. Fix: a card line naming the section, the writer and the source (the approve answer id; see F12).

**F6 (blocks; A3; Q1, Q2, FR-59).**
- (a) G6.4 has no `when`, and the debtor for a missing question is not named. ORDER (frame 2c) is: exit rules, then after_critic, then the person stop. A3 says the late-requirement question is asked "at `report` batched with its stop", and that stop comes after the exit rules are met. With `when: exit` or `after_critic`, G6.4 is unmet until a stop that cannot come. The path is refused, relaunched `refusal_relaunch_max` times, then goes to the conductor, then to a question. This happens on every story with a late requirement and no bug draft: C4-3 skips `bug_or_not` when there are no bug drafts, so the reds stop never asks it. That is an extra round the owner's yardstick forbids.
- (b) "Answered" is not "confirmed". The answer "not sure, later" or "not a requirement" is an answered question, so G6.4 is met. The staling on "not a requirement" is the performer's step, and nothing checks it. The invariant "no late requirement reaches delivery unconfirmed" is not held. Fix: the `bug_or_not` options for "new requirements" carry closed option ids, G6.4 reads the option id (data), and free words go through the conductor's V4 class. The question goes out at the stage's own exit preview, not at the stop, or G6.4 becomes `when: stop` evaluated by `ask.py`.

**F7 (blocks; A4 K1; AR-2, C3-1 edge).** C3-1: "`add` refuses only what no later row can make valid ... no mid-stage block for incompleteness". A later answer row makes a requirement that cites an unanswered question valid, so K1 contradicts the accepted edge. It is also scoped to an optional field: omitting `found_while`, or choosing `red_analysis`, passes. The refusal guards nothing that G6.4 (after approval) or G3.P (before) does not already guard. Fix: drop K1, or turn it into a G-row debt at exit.

**F8 (blocks; A4, A1, F74; Q3).** F74 (a) makes the product look and the exploration "their own launch, caps row `explore`". No card adds that launch to C4-1: who starts it, when, what it receives, what it returns, its stage and group for `FACTORY_*`, its `tools` (A12). Section 4 lists C4-1 for A1, A3, A14, A19 only. Owner ~20:50 Q9 "не увлекается" is then held by nothing. Fix: the C4-1 move and launch block.

**F9 (blocks; A5 x A12).** Stage `sources` gets `read+exec+web`. `docs_build.py --chat --rows <file>` needs a file the performer writes, and so does `ask.py --batch <file>`. On a restricting profile the performer has to write it by shell redirection under `exec`. Either the restriction is nominal (`exec` writes anything), or a correct action is refused. Fix: `write` limited to `work_root` for every stage, or stdin for `--rows` as `record.py add --batch -` already has.

**F10 (fix before merge; A5, FR-59; owner Q1/Q3).** "`chat_language` absent -> repository language". The owner said the chat is in the person's language. A missed field sends the Russian-speaking person an English chat silently. Fix: absent means the language of the person's first message (the stage-1 performer judges) and a journal `unknown`, or an X1-class presence debt at stage 1.

**F11 (fix before merge; A6; Q3).** "Everything shown in chat in the person's language (A5's road, for every chat message incl. questions)" is carried only for `understanding`. `ask.py` forms (C4-3), the `bug_or_not` body and the test_report chat text get no `--rows` road. Section 4 leaves A6 out of C4-3 and C3-5. Fix: amend C4-3 (`ask.py` takes `--lang` and rows) and the C3-5 forms, or state that only the understanding is translated.

**F12 (blocks; A10, A6, A1 raise; AR-9, safety).** `knowledge.py` refuses only `--source found:<x>`. `--source "yes"` typed by an injected performer passes for `raise_permission`, `repositories`, `caps` and `doc_language`. This is a paired claim (key needs person AND words are the person's) checked on one carrier only, the literal prefix. Frame 2a already has the right shape for `passes` (a `stop` naming a question whose tool-written answer holds the words). Fix: for `source_must_be: person` keys, `--source` must name an answered question id, and `knowledge.py` checks the answer row is tool-written and holds the words. The refusal door is "ask the person (ask.py)", and `context.py` prints which keys need the person's words (told at entry).

**F13 (fix before merge; A8; Q2, Q6).** "A row may name many ids, never a pattern" plus "binary or generated files listed and tied like any hunk". A change with a regenerated lockfile or vendored code yields thousands of ids to type under the A1 cap, and the cut ladder ends in a question. The id rule is not stated: if it is positional, every push re-ids every hunk and stales every row. Fix: a file-level id (all hunks of one file) as a legal name, and ids derived from content (path + hunk sha256).

**F14 (fix before merge; A9).** `product_build` is the "latest probe's identity". A stand redeployed after the probe gives a green recorded under the old build, and G6.2 counts it. Fix: run the build-identity command at each `run_tests.py` run (one cheap command, no extra test run), and fall back to the probe only with `unmeasured`.

**F15 (fix before merge; A12; Q3).** Launch kinds `critic`, `conductor`, `explore` and `fix_round` (A1) have no `tools`. The A22 critic writes test and mock files, so it needs `write`, and the G3 critic does not. Fix: tools per launch kind x stage, in the same table as caps.

**F16 (blocks; A16; Q2, Q6, rule 15).**
- (a) The base is `tests_commit`, "tests root VCS head at start". Tests written in stage 4 are usually uncommitted when the red run happens. `test-diff --since` against HEAD then lists every new test file as "changed after the red", which gives a debt on every red for files nobody changed after it. C3-4's snapshot already hashes dirty and untracked files; the base should be that snapshot at the red's run.
- (b) "Each test file changed after its red": the pair (file changed, red) is not scoped to the red's own test. A file holding tests of three reds owes three entries. A file changed for an unrelated reason owes an entry on some red.
- (c) A correct action with no legal label: cause `case_or_expectation_error`. The `expectations` row is revised (it gets a new seq after the red), then the test is brought to it. `to_approved` needs a row "existed before the red", and `new_expectation` needs a requirement row or a person's answer. The only fit is `other`, and the G6 critic then raises "expectation changed without a ground". That is an extra round.
- (d) The A3 path sends a late requirement to `tests` by shortfall after the reds. The tests stage writes into test files, and the reds stage (the debtor: `test_changes` is its field) owes entries for changes it did not make and could not foresee. Fix: `to_approved` names any live `expectations` row, its `seq` irrelevant. Changes whose writer launch is not the red's analysis are attributed by `group`/launch, not by the red.

**F17 (blocks; A4, A5, F73; owner ~21:13; Lead's addition).** Part 4 predates the record and does less than it says:
- (1) The understanding has no section "Agent's assumptions": a line each with its reason ("I read it so"; "the code does X, I assume it is intended, not a bug"), approve all at once or strike lines. A5 amends the C3-5 understanding row with Sources and Contradictions only. A4's page rule "no requirement is held as an assumption" stays true, but the frame-2a section `assumptions` needs a `reason` field and a place in the understanding. "Partial" strikes lines (V4: returned rows staled).
- (2) An approved assumption is a confirmed reading. Its expectation source should be `person_word` naming the approve question id: this fits F73 (a) and the C3-8 edge "`person_word` without its question id -> G3.1 debt". An unapproved or struck one gets no autotest. Name that as an edge of A4/A5 with G3.1 as the guard.
- (3) "Not only what failed": a test the agent thinks is needed for a rule nobody stated is a question with its reason, and no autotest is written before the answer. A4 has only "should it be so" on a mismatch. Before approval, the road is the test_plan "Questions to the team" section approved at G3.P. After approval it is the A3 "new requirements" section of `bug_or_not` with its own option set. The page rule goes into `check-selection.md`/`automate.md` (told at entry).

**F18 (fix before merge; A19).** The Python question cannot go through `ask.py` (AR-16), and the install permission cannot be recorded (there is no record writer yet). Both are inevitable. Name them as the one exception, and record the words in the first record once Python exists.

**F19 (fix before merge; A22; Q6).**
- A shared run proves only probes whose failure is attributed to their own function by the failing assertion. A collection, import or setup error, a substitution in a shared helper, or a changed mock answer used by several functions makes every failure in the run invalid. Then rerun separately. State that as an edge.
- Step 3 (inversion) is allowed by P30 (`docs/OWNER_PRINCIPLES.md:147-150`), but the owner said at ~21:01 that inversion alone is "not enough". Its probe row needs its own mark, shown in the report apart from a value substitution, and not presented as equal proof.
- The C4-2 edge "(a broken product never stays broken silently)" should read "test or mock file".

**F20 (fix before merge; A23).** The A23 edge "G5.4 `new_expectation` keeps its order" needs an order predicate once `lower_seq` leaves the list. Name `later_row` or add one (part of F1's predicate list).

## Questions of the brief

1. **Told at entry.**
   - G3.5, G4.6 and G5.4 are not told, because they are not due at all (F1).
   - G6.4's payer is not named (F6).
   - The reds stage pays G5.4 for tests-stage changes it could not foresee (F16 d).
   - `knowledge.py` keys that need the person's words are not printed in the context (F12).
   - The `record.py` refusals are told: A4 K1 on its page (but see F7); A7 K2 and A17 through `enum_from` data.
   - The A1 caps are told through `context.py`.
   - A demand nobody could foresee: G4.6 when `mock_base` defaults to none. Any substituted side owes a debt until F75's question; that is foreseeable only if the page says so (A7 page rule; acceptable).
2. **Yardstick.** Correct actions refused: F2, F3, F5 (a, b), F6 (a), F9, F13, F16 (a, c, d). Unfinished work that passes: F6 (b), F12, F14, F19 (shared-run false kills). A3's shortfall to `plan`: legal, but it costs a plan critic and a G4 critic per late requirement; no finding beyond F6.
3. **amends.** The facts reproduce (trail). Keys and lines not named: the C3-2 exit column and the C3-3 predicate list (F1); C4-1 for F74 (F8); C4-3 for A6 (F11); C4-2 for A1's "probe open at the cut" edge.
4. **AR/FR/P.**
   - AR-9: F12.
   - FR-59: F10 (silent default).
   - AR-29: G6.4 judges presence where meaning matters; fixed by option ids (F6 b).
   - AR-14 and AR-18: none found. Each new store has one writer; the new refusals use the 2c shape.
   - AR-1, AR-2: A2 vs language forms (F5 a). A4's "prices, limits, access rights" is page craft, not code.
   - FR-58, P20: A15 ("never from current code") and A22 step 1 hold.
5. **Owner's words.** A3 holds 20:50 Q8 but G6.4 does not enforce "confirmed" (F6 b). A4 and A5 do less than ~21:13 (F17). A5's chat-language default goes against Q1/Q3 (F10). A6 holds Q3. A9 holds the "no extra run" word, but see F14. A19 holds Q6. A22 holds ~21:01 except for the inversion mark (F19). A23 holds ~20:56.
6. **Feasibility.** The cut ladder works as a child process with a wall clock on any host. The token measure must be named (F2). The 80 % warning arrives only on the next tool call: a launch thinking without tools gets no warning. That is accepted by the edge ("the cut never depends on the warning"). `world.py hunks`: F13. `world.py test-diff`: F16 (a). Shared probe runs: F19.

**Seams with 4b (headings and the named lines only).**
- A1 vs B5: the subjects are disjoint (factory launches vs forge workers), but the token MEASURE differs. B5 measures context size, A1 is unnamed (F2). The event names also diverge: factory `cap_warning`/`cut` vs forge `cap_warn`/`cap_stop`, in two separate journals. That is a consistency note, not a blocker.
- A18 vs B2: the factory point `after_compaction` maps to the host's compaction event in the project profile, and B2 is the forge's SessionStart `compact`. They do not collide in forge2-repo; a measuring clone gets the factory hook from `arm.py`. Not checkable from the files whether a clone under `measure/` inherits the forge's `.claude/settings.json`.
- C4-6: A1 adds event kinds and views, while B4 rewords the rate line (part3b:65). Different lines, no conflict.
- C4-7: part 4 says "unchanged", and B4 amends C4-7 Delivers/K3. No overlap.

## Standing questions (plan gate)

- Q13 (a) EDGES: findings F3, F4, F6, F10, F13, F16, F19.
- Q13 (b) MEANING: G6.4 restated as "each late REQ has an answered question" contradicts the A3 invariant "confirmed" (F6 b).
- Q13 (c) PREMISES: reran 5 facts, all reproduce (trail).
- Q13 (d) READERS: no `owns_readers.py` block (forge2 files do not exist). Section 6 says so and marks it an estimate. Answer: "n/a: the target repo is not built; the Lead runs it once files exist".
- Q13 (e) FORKS:
  - F70: a decision, with the breakage F4 (person's wait).
  - F71: decided, but the decision has no carrier (F5 b).
  - F73 (a): consistent with ~21:13 if approved assumptions use `person_word` with the approve id (F17).
  - F74 (a): no launcher move (F8).
  - F75 and F76: ok.
- Q4 class-wide: the defect class "a new gate row without its due stage, predicate and page" covers all four rows (F1), as does "a new launch kind without caps, tools and a move" (F8, F15).
- Q6 DUPLICATION AND CONSISTENCY: the A1 cap token measure duplicates the B5 measure but differs (F2). Change detection for A16 should reuse the C3-4 snapshot, not a second base (F16 a). The passes-style answer-id check should be reused for knowledge (F12).
- Q12 ONE ROAD: A2 leaves the inline-test language family outside the shared write mechanism with no data row (F5 a). A19 is an unnamed exception to AR-16 (F18). Searched: part 4 for "language", "runner" and "only"; no other exclusion found.
- VARIETY: on a Go, Rust or colocated-spec project the stage-4 test write is blocked (F5 a). On a host without a live usage stream the wall cap still holds (A1 edge ok).

## Verdict

NEEDS WORK, with blocking findings F1, F2, F3, F4, F5, F6, F7, F8, F9, F12, F16, F17 and fix-before-merge findings F10, F11, F13, F14, F15, F18, F19, F20. The JSON verdict is `blocker` per rule 23 (a finding blocks). This is not a REJECT of the frame: every finding is a card-level fix. Accepting the fix round is the Lead's decision.

## Trail

- Read: part 4 whole; frame spec whole; part 3 whole; part 3b whole; part 2b 5-56; part 4b 38-85, 134-158; plan 914-999, 1500-1615, 772-785, 2087-2136, 2150-2168; `docs/OWNER_PRINCIPLES.md` 145-150; `tools/critic_verdict.schema.json`.
- Not read: the ideas audit, the mocks plan and `architecture.md` (AR-n taken from the frame's invariant list); part 2. The claims about them are cited through the frame or part 4.
- Reruns:
  - `git log --oneline -1` -> 6799870b6.
  - `git diff --stat 481d9dfb4 6799870b6 -- <frame, parts 2-3b>` -> empty.
  - `grep -n -E 'lower.?.?seq|earlier requirement|G4.1 order'` -> spec:52, spec:184, part3:64, part3:74, part3:79.
  - `sed -n 30p part3b` -> "(product code or stub)".
  - `wc -c part4` -> 39985.
  - `grep -n 1800 part3*` -> part3:191, part3b:53.

```json
{
  "verdict": "blocker",
  "blockers": [
    "F1: new gate rows G3.5, G4.6, G5.4, G6.4 never fall due -- C3-2 exit column and C3-3 closed predicate list not amended; How checked therefore never tells them",
    "F2: A1 token cap names no measure; cumulative usage with cache reads passes 300000 in a few turns (B5 measures context size)",
    "F3: A1 wall_s 1200 below test_timeout_s 1800 (part3:191, A14) -- a long suite is cut every relaunch, A14 move unreachable",
    "F4: A1/F70 story wall cap counts the person's stop wait",
    "F5: A2 longest-root rule cannot express tests colocated with product code (Go, Rust inline, spec files); F71 folded decision has no carrier, default config has no tests root",
    "F6: A3 G6.4 has no when/debtor and deadlocks against the report stop; counts answered, not confirmed",
    "F7: A4 K1 is a mid-stage refusal of a row a later answer makes valid (contradicts C3-1 edge) and is bypassed by omitting found_while",
    "F8: F74 explore launch has no C4-1 move, block or tools",
    "F9: A12 gives stage sources no write while A5 needs a rows file",
    "F12: A10 source_must_be enforced only against the found: prefix; any typed words pass; refusal has no door",
    "F16: A16 base tests_commit misses uncommitted files; file-red pairing unscoped; revised expectation fix has no label; reds stage pays for tests-stage changes",
    "F17: A4/A5/F73 lack the owner's 21:13 assumptions list at the first stop and the proposed-test question"
  ],
  "fixes": [
    "F10: A5 chat_language absent must not silently fall back to the repository language",
    "F11: A6 every-chat-message translation needs a C4-3/C3-5 carrier or a narrowed statement",
    "F13: A8 allow file-level hunk ids; ids derived from content",
    "F14: A9 measure build identity at each run",
    "F15: A12 tools per launch kind, incl. critic write for probes",
    "F18: A19 name the AR-16 exception and record the install words later",
    "F19: A22 shared-run attribution edge; distinct mark for inversion; C4-2 edge wording",
    "F20: A23 name the order predicate kept for G5.4"
  ],
  "class_completeness": "Classes walked: a new gate row without due stage, predicate and page (all four rows, F1); a new launch kind without caps, tools and move (explore, critic, conductor, fix_round: F8, F15); keys needing the person's words (all four keys of A10: F12). Seams with part 4b checked by heading: A1/B5, A18/B2, C4-6, C4-7.",
  "trail": {
    "read": [
      "docs/tasks/specs/20261125-forge2-light-factory-spec-part4.md",
      "docs/tasks/specs/20261125-forge2-light-factory-spec.md",
      "docs/tasks/specs/20261125-forge2-light-factory-spec-part3.md",
      "docs/tasks/specs/20261125-forge2-light-factory-spec-part3b.md",
      "docs/tasks/specs/20261125-forge2-light-factory-spec-part2b.md:5-56",
      "docs/tasks/specs/20261125-forge2-light-factory-spec-part4b.md:38-85,134-158",
      "docs/tasks/specs/20261125-forge2-light-factory-plan.md:772-785,914-999,1500-1615,2087-2168",
      "docs/OWNER_PRINCIPLES.md:145-150"
    ],
    "reruns": [
      {"command": "git log --oneline -1", "result": "6799870b6 plan: forge 2 and the light factory, v1.9"},
      {"command": "git diff --stat 481d9dfb4 6799870b6 -- frame and parts 2-3b", "result": "empty"},
      {"command": "grep -n -E 'lower.?.?seq|earlier requirement|G4.1 order' spec.md part3.md", "result": "spec:52, spec:184, part3:64, part3:74, part3:79"},
      {"command": "sed -n 30p part3b.md", "result": "substitute the value a broken product gives (product code or stub)"},
      {"command": "wc -c part4.md", "result": "39985"},
      {"command": "grep -n 1800 part3*.md", "result": "part3:191 test_timeout_s 1800; part3b:53 timeout default test_timeout_s (data, 1800)"}
    ]
  },
  "mutants": [],
  "mutants_none": "plan gate: no diff, no new behaviour in code, no tree named"
}
```
