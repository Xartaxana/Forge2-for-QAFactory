# t-1972 -- critic, narrow re-review (logic): forge 2 spec part 8, card A29 after fix round r1

Reviewed: card A29 of `C:/QAFactory/forge2-repo/forge/specs/20261126-forge2-light-factory-spec-part8.md` (forge 2 commit 980a437, lines 58-81) and its hunks in `part8-fix-round.diff`, against verdict t-1965 (F13, F24-F27) and the plan record 26.11.2026 ≈ 01:58 section 3 (F24, F25 rows) with the batch acceptance ≈ 02:24. Cards A28, A30, B16 not reviewed (dispatch).

- A29: blocker

Verdict: REJECT, failure_class: spec. Four blocking findings (F1-F4), six fixes (F5-F10). The F24 decision is built as decided: under the locks only `resetting` and the claim, the reset with no lock held, the locks taken again, order record -> stand -> journal. The F25 decision is built for the case t-1965 named. All four blockers sit in the new lock and reset steps the fix round brought in. Each is a case those steps leave open.

## Findings

**F1 (A29 S5 (iv) + EDGES `free`, blocks): a reset starts while other launches are live on the stand.** S5 (i) checks busy by the sharing rule only. S5 (iv) then "set `resetting` ... and add this launch as the SOLE holder". Case 1, `walks:2`: walks W1 and W2 hold the stand. W1 is cut, so its return marks the state `unknown` and drops W1. W2 is still walking. Walk W3 arrives. Busy is no (1 walk < 2), the state is unknown and a reset command exists, so (iv) applies. W3 resets the stand under W2, and "SOLE holder" either drops W2's live lease without a word or contradicts it. Case 2, `free`: no holder is ever added, so a torn run's unknown state is reset by the next stand launch while other `free` launches are mid-run. Their runs started on `known`, so the card's invariant holds to the letter. But they are torn by the reset, and nothing marks them. Fix: (iv) only when no live holder remains. Otherwise busy, printed `stand unknown: reset waits for <holders> to return`. Under `free`, holders are recorded for counting only (no exclusion), so a reset waits for zero. Or name `free` mid-run resets as a residual with her word.

**F2 (A29 (b) S4, S5 (ii), (iv), blocks; the F25 class): a holder and a resetter are judged by the `next` pid alone, but the stand work runs in children.** S5 adds the holder before the spawn. No step later writes the child's pid into the lease file ("Other takes, each L2 alone" lists none), so a holder can name only `next`. The claim rule says the opposite: gone only when every named process is gone, so `next` dead with the child alive is live (K3). Case: story A's `next` (holding a `run` lease) is killed and its host child keeps running tests. A's claim stays live, so S2 does not fire. Story B, at S4, sees holder A "proven gone", marks it unknown, drops it and resets the stand while A's child is mid-suite. A's child then records greens from a run torn by B's reset. This is "a takeover while the old holder is alive after all". The same hole hits the resetter. `resetting` names "next pid + start". If `next` is killed during S6, the reset command's process can outlive it. S4 then reads the resetter as dead and sets unknown, and the next launch starts a second reset beside the orphan. Its S7 can set `known` while the orphan still changes the stand. Fix: a holder and a resetter are gone only when every process they name is gone (A29 (a) LIVENESS). After the spawn, L2 alone (allowed by the order) adds the host child's pid and start to the holder, and the reset child's pid to `resetting`.

**F3 (A29 S7, blocks): S7 writes its result without checking that it still owns the stand.** S7 takes L2 and sets `known` or `unknown`. Its record-busy fallback does the same. Neither checks that the state is still `resetting` by this launch. Case: A is in S6. B, waiting, reaches `stand_wait_s` and she answers the `stand_busy` question "the holder is gone: release". Her `stand.py release` clears every holder and marks the state unknown, since A's launch has not returned. B's next `next` takes S5 (iv) and B's reset starts. A's reset ends, and A's S7 sets `known` and launches while B's reset runs. A is not even a holder, so on a `one` stand two launches run. Fix: in S7, under L2, when the state is not `resetting` by this launch, keep the `runs` row, set nothing, journal `stand_reset: superseded` and `claim_broken: lease lost`, and launch nothing.

**F4 (A29 (c) INVARIANT vs A14, blocks; two accepted requirements conflict): the same launch keeps running tests on the stand it just marked unknown.** A29: `run_tests.py` marks unknown at its own timeout, and the amended C4-4 only "prints the stand state at start". A29 (c): "no green from a run started on a stand of unknown state". A14 (part4-2:62) asks for the diagnostic run next in the same launch, with "diagnostic green -> normal results". Case: suite 1 times out and the state becomes `unknown (S/run-1)`. The same launch still holds the lease and runs one test as A14's diagnostic, and it is green. That is a green from a run started on an unknown stand, which A29 forbids and A14 records as normal. The same happens to a live launch whose stand another story's S2 marks unknown (F7). Fix (a fork for the Lead): `run_tests.py`, starting on `unknown`, records its results `not_reached: stand unknown since <run>` (A14's diagnostic then reads as not reached, and the next launch resets). Or A14's diagnostic follows a reset inside the launch. Or narrow A29's invariant to runs started by another launch, with the residual named.

**F5 (A29 S7, fix): "L2 tried, as above" sends S7 back to S1.** The rule says busy -> "release L1, sleep 0.2 s, restart at S1". From S7 that means recomputing with this launch's own claim live and its own `resetting` held. It ends busy on itself, the reset result is lost, and the state stays `resetting` until this `next` exits. It is then read as dead and the stand is reset again. Fix: in S7, L2 busy -> release L1 (the `runs` row is written), take L2 alone (waited: nothing else is held) and go on as written. Never restart at S1.

**F6 (A29 LOCKS L3, fix; fact by trail): L3 is a waited lock.** The card says "`estimate`: C4-6 names its one writer, not its lock". C4-6 Delivers (part3b:71) reads "append to `<story>/runs/journal.jsonl`, lock as C3-1". So L3 waits up to 10 s and is then refused, while L1 and L2 are held in S2, S4, S5 and S7. The card handles only the claim's write failing in S5 (ii)/(iv). The other cases have no stated behaviour. S2 and S4 fail after the lease mark (safe, but `claim_broken` is lost, so S2 repeats). S5 (iv) fails on `stand_reset: start` after the claim is written. S7 fails on `stand_reset: <result>` after `known`. Fix: quote C4-6 and drop the estimate. State one rule: a failed L3 append after a lease change never reverts the mark toward `known`. The step goes on and prints `journal busy: <event> not written`. S2 marks only once (see F7).

**F7 (A29 S2, fix): S2 marks unknown again after the stand was taken over and reset.** S2 marks unknown and drops "that holder" whether or not the lease file still holds it. Case: story B's S4 already marked A's dead holder, dropped it, reset the stand (`known`) and is running. Later A's `next` runs S2 on A's broken claim and marks the state unknown under B's live run. Then F4 applies to B's next suite, and another reset follows B. This errs toward safety, but it violates the invariant and costs a reset. Fix: S2 marks only when the lease file still names that launch as a holder or as the resetter.

**F8 (A29 S7 record-busy fallback, fix): a torn run can be rerun silently.** With L1 still busy, the fallback sets the state (exit 0 -> `known`), writes no `runs` row and launches nothing. The next `next` sees `known` and launches with no block line "stand reset after torn run <id>: rerun <tests>". That breaks (c)'s "no torn run is rerun silently". Fix: in the fallback, set `unknown` whatever the result, so the reset is redone with its `runs` row and block line.

**F9 (A29 test line, fix; part-wide rule "every limit ... AT and BEYOND").** The L2 retry window (`record_lock_wait_s` 10 used as a new limit: "up to ... 10 in total, then `stand lock busy`") has no AT/BEYOND row. The `locks` row lists only "L2 busy while L1 held". Fix: add {L2 busy 9.8 s -> claimed; L2 busy past 10 s -> `stand lock busy`, nothing claimed, L1 released}.

**F10 (A29 WORLDS, fix; fact by trail): the A27 rule is misquoted.** WORLDS says "A27's amends line lands every other A-card with the host part it amends", and the r1 line quotes "every other A-card ... waits". A27 says neither. A27 (4) (part7:89) reads "the non-gate parts that wait land with the batch whose rows need them". No listed batch's rows need A29, and "C4-1's full node" is no batch. So A29's landing moment is unanchored. Fix: quote A27 (4) and name the batch A29 lands with (e.g. the batch carrying A9's G6.2 reading, `batch:report`, or `batch:tests` where groups run in parallel). Or leave it for the Lead to fix in `result.md`, and say so.

## Interleavings walked (dispatch list)

- Two launches racing for one stand. Holds. Two stories each take their own L1. One gets L2 and adds its holder (S5 (ii)). The other's try fails, so it releases L1 and retries, then finds the stand busy, prints busy and journals `stand_wait`. Within one story, L1 serializes the launches and the claim gives `claimed:`. Hole only under `walks:n`/`free` on an unknown stand (F1).
- Holder killed between S5 and S6. Holds. The state is `resetting` with a dead resetter. The next S4 sets `unknown` and journals `stand_reset: died`, and S2 breaks the claim. Exception: an orphaned reset child (F2).
- Holder killed between S6 and S7. Holds, toward safety. The reset result is lost, `resetting` with a dead resetter becomes `unknown` at the next S4, and the stand is reset again. Killed inside S7 after `known`: the holder is gone, S4 marks it unknown, and the stand is reset again.
- Holder killed during the reset. Hole when the reset command outlives `next`: a second reset runs beside the orphan, and `known` can be set while the stand still changes (F2).
- Reset that hangs. Holds. AT 600 s it is still waited for. At 601 s its tree is stopped and the state becomes `unknown`, with the question. Other launches are busy meanwhile, and 600 < `stand_wait_s` 1800, so no `stand_busy` comes from one reset. This is true while `next` lives. With `next` dead, see F2.
- Takeover while the old holder is alive after all. Hole: the holder names `next` only, so a live child is taken over and reset (F2). S7 also ignores a release that happened during the reset (F3). Takeover of a live `next`: pid + start time keep it, so it holds.
- Lock order inverted by any path. Holds: no deadlock. L1 is waited only with nothing held (S1, S7). L2 under L1 is tried once. Every L2-then-L1 need releases L2 first (S5 (iii), S7's `ask.py`). The other takes use L2 alone, and L3 takes nothing. Livelock is bounded by the 10 s window. S7's L2-busy text is contradictory (F5), but it causes no deadlock.
- Journal write fails while L1 + L2 are held. Partly a hole. S5 (ii)/(iv)'s claim write is handled. The others have no stated behaviour, and L3 is a waited lock against the card's own estimate (F6).
- Stand left resetting forever. Holds. A dead resetter becomes `unknown` at the next S4. An uncheckable resetter is kept until her release. Waiters reach `stand_busy` at 1801 s with the door "release" or "stop". In comparison/night the story is `stopped` and named. There is always a way out.

## t-1965 findings naming A29

- F13 (union of intervals): fixed in A29 amends (A1 `story_wall_s` minus the union of `test_run` and `stand_wait`), (b) last sentence, and K9.
- F20: names A29 only as the model for code-written `tried`. Nothing is owed by A29. A28 (b) now cites A29's `stand_unknown` among the code-raised questions.
- F24: fixed in (b) LOCKS AND ORDER S1-S7 and the INVARIANT, as decided at ≈ 01:58: under the locks only `resetting` and the claim (S5 (iv)), the reset unlocked (S6), the locks taken again in order (S7), order L1 -> L2 -> L3, and K10. Residual fixes: F5, F6, F9.
- F25: fixed for the named case in S2, S4, the (b) holder text, (c) and her release, with K6 and K11. Not fixed for the sibling: a holder whose `next` died while its child lives (F2). It is the same class as F25, read through the claim rule.
- F26: fixed in (a) LIVENESS. (1) The claim names `next`, `next` waits for its return, and the `launch` event carries the child's pid. (2) The last sign of life counts an open run's start + timeout. (3) A stale break keeps the lease, and the busy print names the story's own earlier launch. K3 covers it.
- F27: fixed in WORLDS. A27's thin `next` carries none of A29, matching part7:39 (C4-4 thin node keeps `status: timeout`) and the A27 C4-1 thin node. The quote and the landing anchor still need fixing (F10).
- t-1965 spot-check "A29's replays included": done. (c) now says "nothing here names replays" (A25 deferred, plan ≈ 01:38 p.3).

## Owner's yardstick (A29)

- Does a free agent's work and more: yes. A free agent would not guard two launches or a torn stand at all.
- A gate never hinders a right action: holds after F24 (K10). L2 under L1 is tried, never waited for.
- Never lets unfinished work through: not yet. F1, F2 and F3 each let a run start on, or continue on, a stand being reset. F4 lets a green come from a stand the launch itself tore.
- Told at entry: the busy, claimed and `stand lock busy` prints carry their doors, and `stand.md` is amended (`amend:A29`). It holds.
- Nothing useful of the old forge forgotten: the OLD MECHANISM section carries `stand_lease.py` line by line, with what changed and what was dropped and why. It holds.

## Spot-checks (facts by trail)

- Hold: C3-1 lock (part3:25: 0.2 s retry, `record_lock_wait_s` 10, a 60 s break with a dead pid); C4-1 "on return `exit_check`" (part3b:10); A1 `wall_s` 1200 s, and a run's interval bounded by its `--timeout` (part4:27-28); A14 timeout stops the tree, then the diagnostic (part4-2:62); A9 `stand.py` and `runs` rows `obtained_by: stand.py` (part4-2:22); A27 C4-4 thin node keeps `status: timeout` (part7:39); the plan ≈ 01:58 F24/F25 rows (plan:3429-3430) match S5 (iv)/S6/S7 and S2/S4.
- Do not hold: "C4-6 names its one writer, not its lock" (C4-6 reads "lock as C3-1": F6); "A27's amends line lands every other A-card with the host part" (A27 (4) reads otherwise: F10).

## Trail

- Read: part8 lines 1-95 (section 1; A29 whole; A28/A30 only as neighbours) and lines 143-160, 203-221 (choices, Fix round); diff lines 1-101 (the A29 hunks); t-1965 lines 1-140 (F13, F20, F24-F27, yardstick, spot-checks, json); plan lines 3380-3528 (≈ 01:58, ≈ 02:07, ≈ 02:13, ≈ 02:24); part3:25 (C3-1 lock); part3b:5-30 (C4-1), 50-56 (C4-4), 69-80 (C4-6); part4-2:19-30 (A9), 60-66 (A14); part4:26-36 (A1); part7:30-40, 86-89, 185.
- Commands: `git -C C:/QAFactory/forge2-repo log --oneline -1` -> `980a437 specs: parts 5-9 after the fix rounds; plan record on the batch acceptance`; `grep -n -E '^### ' part8` -> A29 at line 58, once; `wc -l diff` -> 257; `grep -n -E '^### 26.11.2026' plan` -> 13 records, ≈ 01:58 at 3380; `grep record_lock_wait_s|lock older` over specs -> part3:25 and part8:63 only; `sed -n '69,80p' part3b` -> C4-6 "lock as C3-1"; `grep -i 'A-card|lands with|IN column' part7` -> no "every other A-card"; A27 (4) at part7:89.
- No probe: plan gate, no code, no tree.

```json
{
  "verdict": "blocker",
  "blockers": [
    "F1: A29 S5 (iv) resets an unknown stand while other walk holders (walks:n) or free launches are live; SOLE holder contradicts a live walk holder",
    "F2: A29 holder and resetter judged by the next pid alone; next dead with child alive is taken over and reset mid-run; an orphan reset runs beside a second reset (F25 class)",
    "F3: A29 S7 sets the state without checking it still owns resetting; after her release during S6 and another launch's reset, it sets known and launches without a lease",
    "F4: A29 (c) invariant no green from a run started on an unknown stand conflicts with A14's diagnostic run in the same launch after its own timeout mark (diagnostic green -> normal results)"
  ],
  "fixes": [
    "F5: A29 S7 L2 busy must not restart at S1; release L1, take L2 alone (waited) and go on",
    "F6: A29 L3 is C4-6 'lock as C3-1' (waited 10 s), not an estimate; state the rule for a failed append after a lease change in S2, S4, S5 (iv), S7",
    "F7: A29 S2 marks unknown only when the lease file still names that launch as holder or resetter",
    "F8: A29 S7 record-busy fallback sets unknown whatever the result, so the torn run's rerun is not silent",
    "F9: A29 test line lacks AT and BEYOND rows for the 10 s L2 retry window",
    "F10: A29 WORLDS misquotes A27; A27 (4) lands non-gate parts with the batch whose rows need them; name A29's batch"
  ],
  "class_completeness": "Plan gate, narrow (A29 only). F25's class (a stand road that drops or overrides a holder without its launch's return) walked over every road in the card: S2, S4 holder, S4 resetter, S5 (iv) co-holders, S7 result write, the S7 fallback, her stand.py release, run_stage.py release, the return path, and run_tests.py's own timeout. Holes: F1, F2, F3, F4, F7. F24's class (a lock held across a wait) walked over S1, S2, S4, S5, S7, L3 and the other takes: F5, F6. SIBLING_MAP not applicable (forge 2, no package file).",
  "trail": {
    "read": [
      "C:/QAFactory/forge2-repo/forge/specs/20261126-forge2-light-factory-spec-part8.md (1-95, 143-160, 203-221)",
      "C:/Users/<user>/AppData/Local/Temp/claude/b3e3188b390a00d9/019810c0-e93d-4fda-81cb-1c435f3c0f3c/scratchpad/part8-fix-round.diff (1-101)",
      "C:/QAFactory/forge-repo/docs/tasks/specs/reviews/t-1965-forge2-plan-a27-a30.md (1-140)",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-plan.md (3380-3528)",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part3.md (25)",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part3b.md (5-30, 50-56, 69-80)",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4-2.md (19-30, 60-66)",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4.md (26-36)",
      "C:/QAFactory/forge2-repo/forge/specs/20261126-forge2-light-factory-spec-part7.md (30-40, 86-89, 185)"
    ],
    "reruns": [
      {"command": "git -C C:/QAFactory/forge2-repo log --oneline -1", "result": "980a437 specs: parts 5-9 after the fix rounds; plan record on the batch acceptance"},
      {"command": "grep -n -E '^### ' part8", "result": "A28 43, A29 58, A30 83, B16 96 -- A29 once"},
      {"command": "wc -l part8-fix-round.diff", "result": "257"},
      {"command": "sed -n '69,80p' part3b.md", "result": "C4-6 Delivers: journal.py write ... append to <story>/runs/journal.jsonl, lock as C3-1"},
      {"command": "grep -n -o -i -E 'A-card|lands? with|IN column' part7.md", "result": "no 'every other A-card'; part7:89 'the non-gate parts that wait land with the batch whose rows need them'"}
    ]
  },
  "mutants": [],
  "mutants_none": "plan gate on a spec card: no code, no tree named by the dispatch, no new behaviour to probe"
}
```
