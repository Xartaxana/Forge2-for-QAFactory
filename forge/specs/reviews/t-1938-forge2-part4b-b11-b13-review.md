# t-1938 -- plan-gate critic pass on forge 2 part 4b, cards B11, B12, B13 (at 777fb4a53)

- B11: fit_with_fixes
- B12: fit_with_fixes
- B13: fit_with_fixes

Overall: NEEDS WORK. Fixes F1, F2, F3, F8, F9, F10 must land before a builder is dispatched (without them the builder either has to ask a question or builds a stated invariant that does not hold). F4-F7 and F11-F12 are fix lines for the same round. Whether to accept is the Lead's decision (rule 6).

Spec/intent read: plan records 25.11 22:20, 22:25, 22:40, 22:50 (plan heading greps: each time occurs exactly once); RELATED_WORK section 8; file 3 (whole) and file 4 (whole) of part 4b. Accepted cards were read only where B11-B13 amend them or call them: B2 (K5 and its cut order), B3 (`words.py add` writer, plan id), B4 (`compute` signature), B8 (range), B9 (quoted lines), C1-5 (`foreign_write.py` matchers).

## Findings

### F1 (B11, blocks dispatch) -- `reseal` and an unkeyed seal let an agent record a value as hers
File 3, B11 edges: "a hand edit breaks the seal (invariant: no value of hers changes, and none is recorded as hers, without her recorded word or her press in the pane)".
What is wrong: the seal is "sha256 of the records' canonical JSON". Anyone can recompute it, so it catches careless edits, not deliberate ones. And `reseal --reason` is an ordinary subcommand that any agent can run; nothing in it compares the owner fields. Walk it through: an agent edits `forge/worklist.yaml` by hand and changes `priority` to P1 with `owner_source: pane 2026-...Z`, appends the matching `history` entry, then runs `reseal`. `check --base` goes red only on "a field that held an `owner_source` at the base and differs now with no newer `owner_source`". Here a newer `owner_source` is present, so the check is green. The r0b invariant this card claims fails through two roads (`reseal`, and a recomputed seal), and the card does not name this as a residual. It names only the C1-5 indirect-call residual.
Smallest fix line (B11 `reseal` and edges): "`reseal` refuses when any `priority`/`release` value or `owner_source` differs from the last sealed state: `owner fields changed: use owner-set` (exit 2). A hand edit that writes an owner field with a recomputed seal errs GREEN, a residual named beside F106 (a): the seal is not a secret. The trace stays as the `history` entry shown in the pane."

### F2 (B11, blocks dispatch) -- after a release passes, an agent-set mark can be carried or cleared silently
File 3, B11 RELEASE PASSED: "only her answer through `owner-set` (`--release yes` refreshes `marked_after_tag`; `--release no` unmarks) clears it", and edges: "never unmarked by code (invariant: only her answer moves the mark)".
What is wrong: r0b lets `set --release yes|no` write "ONLY while the field holds no `owner_source`". A mark that an agent set has no owner source. So after the release passes, an agent can run `set --release yes`, which refreshes `marked_after_tag` and carries the record into the next release silently. Plan 22:40 forbids exactly that ("не переносится молча; владельцу один вопрос"). The agent can also run `set --release no` and unmark the record without her. Two of the card's own rules conflict, and the builder must ask which one wins.
Smallest fix line: "`set --release` on a record that is `release passed` is refused, `release passed <tag>: ask the owner`, door `owner-set`, whoever set the mark (K15 gains the agent-marked case)."

### F3 (B11, blocks dispatch) -- `check` with no base, and the first push, are silent on the r0b rule
File 3, B11 CHECK: "`check [--base <ref>]` ... with `--base`, a field that held an `owner_source` at the base ... -> red" and "the base without the file -> `born`, green".
What is wrong: the card says what `check` does with no `--base` only by omission: the owner-value rule and the history-prefix rule do not run, and the result is green. B8's range says "the first push: all history", so there is no base commit. What `worklist` receives for `<base>` on a first push, and from pre-push via `ci.py`, is never stated. Rule r0b asks what happens at the first commit and with no base. Both answers are "her value can change unnoticed", and the card neither says so nor names it. An unknown here is read as a pass, against FR-41.
Smallest fix line: "`check` without `--base` (or B8's first push) prints `no base: owner-value and history rules not judged` and exits 0 with that line, never a bare green. With a base where the file is absent: `born`, owner values judged for source form only (named)."

### F4 (B11) -- the duplicate-id door drops her value with no road back
File 3, B11 edges: "duplicate ids after a merge of two branches -> ... door: the Lead keeps one and re-adds the other through `add` (new id), then `reseal`".
What is wrong: `add` cannot write an `owner_source`. If the re-added record carried her pane-pressed P1, her value is lost, and the only roads back are her new press or a new word. Otherwise the Lead copies it as `agent_source`, which turns her word into an agent's suggestion, or writes it by hand, which is F1. The card says nothing about this.
Smallest fix line: "the re-added record's owner fields are listed in the `reseal` reason and put to the owner as one question; until she answers they are unset (never copied as an agent value)."

### F5 (B11) -- section 4 and F106 still carry the line that plan 22:50 retracted
File 4, section 4: "`priority` and `release` are hers (only `owner-set`)". File 4, F106: "an agent ... never touches the field". File 3, intent paragraph: lists only records 22:20, 22:25 and 22:40.
What is wrong: plan 22:50 retracts "Эти два поля ставит только владелец". A builder who reads section 4 gets the opposite of r0b. The decided F106 (a) does still fit 22:50.
Smallest fix line: section 4 -> "`priority` and `release`: an agent sets them through `add`/`set` where she set nothing; her value only through `owner-set` (r0b)". Add "22:50" to the intent record list of file 3. Mark F106's premise "(22:40, retracted in part by 22:50)".

### F6 (B11) -- "newest `v*` tag" and `marked_after_tag: none` have no order
File 3, B11: "whose `marked_after_tag` is older than the newest `v*` tag" and edges: "no `v*` tag ... `marked_after_tag: none`".
What is wrong: the card does not say what "newest" means (version sort, tag date, or ancestry of HEAD). It also does not say whether `none` counts as older once the first tag appears. If it does not, a record marked before the first release never becomes `release passed`: an unknown read as "not passed".
Smallest fix line: "newest = first of `git tag --list 'v*' --sort=-v:refname`; `none` is older than any tag."

### F7 (B11) -- a malformed list refuses with no door
File 3, B11 edges: "list malformed (broken YAML, ... conflict markers after a merge, a record missing a field) -> exit 2 naming the line, `add`, `repeat`, `set` refuse to write".
What is wrong: the refusal names no door that its receiver can use. `reseal` is named only for a seal mismatch.
Smallest fix line: "door in the refusal: `fix the named line by hand, then worklist.py reseal --reason` (the F1 limits apply)."

### F8 (B12, blocks dispatch) -- the `compute` call does not match B4, and tokens are kept without the model
File 3, B12 Delivers: "`price` = `price.compute(tokens_by_bucket)`" and "per scope `main` and `sub` ... the tokens per bucket", "`model` (of the last main-session answer)".
What is wrong: B4 (part4b, accepted) defines "`compute(tokens_by_model, harness_cost=None, at=None)`". B12 keeps tokens per scope and bucket only. In a session whose subagents run another model, or after a model switch, either every bucket is priced with one model's rate (a wrong figure shown as known: the hazard B12 exists to remove) or the builder has to invent the grouping. The old counter prices per usage line per model (`tally.mjs` `addUsage(e.totals, m.model, m.usage)`, `byModel`). The `price.bucket(model, speed, prompt_tokens)` that B12 adds to B4 also needs speed and prompt size for each call, and the band.py Delivers never collects them. So the edge "a fast-mode usage or a long prompt with no matching bucket row -> ... `unknown rate`" cannot be built from the card. Also missing: a key for a two-model session.
Smallest fix line: "band.py keeps tokens per model per F102 bucket: for each usage line, `price.bucket(model, usage.speed, input+cache_read+cache_write)` (fields carried from `tally.mjs`); it calls `price.compute(tokens_by_model)`; scopes are kept for display only. K2 gains: main on `model-a`, a subagent on `model-b` with no row -> `unknown_rate: [model-b]`, no total."

### F9 (B13, blocks dispatch) -- the legacy ceiling can be raised silently, and a count cannot tell new from old
File 4, B13: "lowered in any commit, never raised: AR-20" and "invariant: a NEW line reference is always red, an old one never blocks a fix"; K4: "a row whose `max` is above the count -> green with the line `can be lowered`".
What is wrong: (a) `refs.py check` takes no base. A commit that raises `max`, or that adds the first-edit row with any `max`, is green, and a `max` above the count is explicitly green. "Never raised" has no checker. (b) A per-file count cannot see a swap. Delete one old `part2:126`, add a new `part3:40`: the count is unchanged and the job is green, so the stated invariant fails by construction. First-edit deadlock (the edge asked about): none for (2), because the door "add the row with the printed count" exists in the same commit. See F10 for (1).
Smallest fix line: "the row holds `tokens` (the old references found at first edit, from the copy's bytes at the recorded sha) instead of `max`; in an edited copy, a line reference not in `tokens` is red (`new line reference`); `check --base <B8 range>` is red when a row's `tokens` at head is not a subset of the base's, or when a new row lists a token absent from the frozen bytes; with no base: `legacy rows not judged against base` printed."

### F10 (B13, blocks dispatch) -- the first edit of three copies turns rule (1) KEYS red; the ceiling covers (2) only
File 4, B13: "A copy whose bytes no longer match ... is scanned for (1) and (3) like any file; for (2) its old line references are LEGACY".
What is wrong, measured here: these card-id tokens match the card's own `card_id` form and resolve to no `### <id> ` heading across all 14 spec files. Plan: 7 (`A38`, `C3-17`, `C5-7`, ...). Part 2: 14 (`A25`-`A32`, ...). Part 2b: 23. Part 4-2: 1 (`A99`). File 4 itself: 1 (`B99`, B13's own K1 text). The probe found 73 headings and no duplicate (control: `B11` resolved once). The first one-byte fix of the plan or part 2/2b copy is red on dozens of old tokens, and the only door is one `allow` row per token. This is the same class the Lead's mark fixed for (2), left open on (1).
Smallest fix line: "the legacy row of F9 also lists the copy's unresolved card-id tokens found at first edit; in an edited copy they are legacy under (1) as under (2); a new unresolved id is red."

### F11 (B13) -- the card line goes into live hook files with no `.next` road
File 4, B13 owns: "the card line in every existing code file of forge 2 and the factory at landing (a one-line comment per file, added by this card's builder in the same branch)".
What is wrong: "every code file" includes `forge/hooks/*.py` and `forge/hooks/git/*`, which are self-activating enforcement files. B11 sends its hook edits as `.next` placed by the Lead ("comes as `foreign_write.py.next`, placed by the Lead"). B13 is silent on this, so its builder would edit live hooks, against the enforcement-file rule that both forges hold.
Smallest fix line: "files under `forge/hooks/` get their card line as `<file>.next`, placed by the Lead at acceptance (C1-5 edge)."

### F12 (B11 x B13) -- a line reference inside the work list has a door only through `allow`
File 4, B13 `scan`: "`forge/worklist.yaml`"; file 3, B11 `add` battery (empty, 500/501, newline, control char, non-UTF-8).
What is wrong: `add`/`set --note` accept `foo.py:12`, and then the `refs` job turns red. No subcommand edits `text`, and a `history` note can never be removed: `worklist check --base` requires "every base `history` a prefix of head's". So the only way out is an `allow` row, a door that B13 defines for look-alikes. Two CI jobs disagree about one store.
Smallest fix line (B13 edge): "a line reference in `forge/worklist.yaml` -> red, door an `allow` row (history is append-only)". (B11 battery, optional): "once `refs.py` exists, `add`/`set` refuse a text or note holding a line-reference token by importing its pattern (one road)."

## Standing questions (plan gate)

- Q13 (a) EDGES: findings F3, F4, F6, F7, F10, F12. Otherwise the edges are stated with their invariants (absent list, rows file, lock, 500/501, 366/367, unreadable tags, commit not local, no transcript, state-file rescan, plan copy absent).
- Q13 (b) MEANING: `priority`/`release` mean different things in r0b and in section 4 (F5). "Release passed" contradicts `set` (F2). "A NEW line reference is always red" does not match its checker (F9).
- Q13 (c) PREMISES: re-ran two. B9's quoted lines exist ("gets no node until it repeats", `fix: <node>`, `already fixing: <node>` in part4b-2): reproduced. B12's premise "`price.compute(tokens_by_bucket)` ... B4's one source": B4's signature is `compute(tokens_by_model, ...)`, which does NOT reproduce (F8). The `tally.mjs` "Longest prefix wins" premise: reproduced (header comment).
- Q13 (d) READERS: no `owns_readers.py` block. The cards say why (forge 2 holds no files). Not re-run, because the tool cannot see the forge 2 tree. Section 6's reader list was read; the missing reader is `foreign_write.py` -> live hooks for B13 (F11).
- Q13 (e) FORKS: F101 (a) fits (B6's `friction:` kept). F102 (a) fits only with F8, because without per-call buckets the columns are unused. F103 (b) fits P31. F104 (a) fits. F105 (a) fits the owner's question about clutter, and a door is named for her items. F106 (a) still fits 22:50, but its premise is stale (F5), and its residual list lacks the reseal road (F1).
- Q4 CLASS: F10 is the sibling of the Lead's (2) fix on rule (1). F2 is the sibling of the r0b rule on the release-passed state. F1 covers both roads of the same class (reseal, recomputed seal). No other siblings found inside these cards.
- Q6 DUPLICATION: none found. B12 prices only through `price.compute`/`bucket` (one source; K5 greps for a second table). B13 resolves plan keys through B3's resolver and L-ids through `worklist.py ids`. `owner` sources resolve through `words.py`. Grepped: `compute(`, `foreign_write.py`, `words.py add` across the spec files.
- Q12 ONE ROAD: none found. No language, project or case is taken out of a shared mechanism. The pane road and the chat road both go through `owner-set`.
- VARIETY: forge-side only. No factory axis is held. The factory's `factory/` code files gain a comment that no factory code reads. Agreed: no project shape is affected.
- AR-29: no code judges meaning ("same or new" stays the Lead's; refs resolves existence, not fit). CI red with no repository change: none found (`check` reads no clock and no tags; release-passed is view-only; `cards` never red).
- r0b write roads, one by one: `add` -- writes only `agent_source`, cannot record a value as hers. `set` -- refused on her field; hole on the release-passed agent mark (F2). `repeat` -- touches neither field. `owner-set --word` -- the Lead can run it after writing a `word` record through B3: her value rests on the Lead's transcription, the B3 paraphrase residual, named. `owner-set --by pane` -- literal agent call refused, indirect call errs GREEN, named. `reseal` -- launders a forged owner source (F1, not named). Hand edit -- the seal can be recomputed (F1). `check` at the first commit / with no base -- the owner rule is not run and nothing says so (F3).
- B13 legacy ceiling: it can be raised silently (F9). The first edit does not deadlock for (2); for (1) it floods red, measured (F10).
- B12: a second price source -- none. A model matched by prefix -- none (exact match amended into B4, K2 row). The per-model grouping is missing (F8).

## Trail
- Read: part4b-3 (whole), part4b-4 (whole); plan records at 22:20, 22:25, 22:40, 22:50 to end of file; RELATED_WORK section 8 (whole); grep windows of part4b (B2 K5 and cut order, B3 writer and plan id, B4 `compute` signature), part4b-2 (B8 range, B9 lines), part2 (C1-5 `foreign_write.py` matchers: "PreToolUse on Write/Edit/Bash"); `tools/claude-mods/cost-band/tally.mjs` (grep: prefix rule, per-model `addUsage`, `u.speed`, homedir root).
- Probe (python over the 14 spec files, read-only): card headings 73, duplicates none; unresolved card-id tokens per file -- plan 7, part2 14, part2b 23, part4-2 1, part4b-4 1, others 0; control `B11` heading count 1; each of the four plan times is one heading.
- No price figure was copied. Nothing was written outside this file.

```json
{
  "verdict": "fit_with_fixes",
  "blockers": [],
  "fixes": [
    "F1: B11 reseal refuses changed owner fields; recomputed-seal residual named (blocks dispatch)",
    "F2: B11 set --release refused on a release-passed record whoever marked it (blocks dispatch)",
    "F3: B11 check without base or on first push prints owner rule not judged (blocks dispatch)",
    "F4: B11 duplicate-id door: her owner values become one question, never copied as agent values",
    "F5: file 4 section 4 and F106 premise updated to plan 22:50; 22:50 added to file 3 intent list",
    "F6: B11 newest v-tag order and none older than any tag",
    "F7: B11 malformed-list refusal names its door",
    "F8: B12 band.py tokens per model per bucket via price.bucket per usage line, compute(tokens_by_model); two-model key (blocks dispatch)",
    "F9: B13 legacy row holds the old tokens, base comparison for raises, swap red (blocks dispatch)",
    "F10: B13 legacy treatment extended to rule (1) unresolved card ids of an edited copy (blocks dispatch)",
    "F11: B13 card lines in forge/hooks files go as .next placed by the Lead",
    "F12: B13 edge for a line reference in worklist.yaml; optional B11 refusal at write"
  ],
  "class_completeness": "F10 extends the Lead's rule-(2) legacy fix to rule (1); F2 extends r0b to the release-passed state; F1 closes both laundering roads (reseal, recomputed seal). No further sibling inside B11-B13; accepted cards not re-reviewed per non-goals.",
  "trail": {
    "read": [
      "docs/tasks/specs/20261125-forge2-light-factory-spec-part4b-3.md",
      "docs/tasks/specs/20261125-forge2-light-factory-spec-part4b-4.md",
      "docs/tasks/specs/20261125-forge2-light-factory-plan.md (records 22:20-22:50 to end)",
      "docs/RELATED_WORK.md section 8",
      "docs/tasks/specs/20261125-forge2-light-factory-spec-part4b.md (grep: B2 K5, B3, B4 compute)",
      "docs/tasks/specs/20261125-forge2-light-factory-spec-part4b-2.md (grep: B8 range, B9)",
      "docs/tasks/specs/20261125-forge2-light-factory-spec-part2.md (grep: foreign_write.py)",
      "tools/claude-mods/cost-band/tally.mjs (grep)"
    ],
    "reruns": [
      {"command": "grep compute( over the spec files", "result": "part4b B4: compute(tokens_by_model, harness_cost=None, at=None); part4b-3 B12: price.compute(tokens_by_bucket)"},
      {"command": "grep B9 quoted lines over the spec files", "result": "gets no node until it repeats, fix: <node>, already fixing: <node> present in part4b-2"},
      {"command": "python probe: card headings and unresolved card-id tokens over 14 spec files", "result": "73 headings, no duplicates; unresolved plan 7, part2 14, part2b 23, part4-2 1, part4b-4 1; control B11 heading 1; plan times 22:20/22:25/22:40/22:50 one heading each"},
      {"command": "grep tally.mjs prefix/speed/model", "result": "Longest prefix wins; model.startsWith; addUsage per model; u.speed fast; root homedir .claude/projects"}
    ]
  },
  "mutants": [],
  "mutants_none": "plan gate: no code exists, no new behaviour to break"
}
```
