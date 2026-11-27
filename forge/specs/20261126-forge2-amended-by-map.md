# Forge 2: the true "amended by" map (t-1980, F19)

Designer draft for the Lead. A MAP only: no spec part, plan or ledger is edited here. Spec parts below are identified by their part names and named cards or sections; the frame is `20261125-forge2-light-factory-spec.md`.

How it was judged. An id counts as amended when the amends entry changes that card's text, list, rows, fields, rule,
edge, key or owns, or names the card as its target "by pointer". It does not count when the id sits in a parenthesis
naming the owner or user of something, in a quoted range bound (`A1-A24`), in a carry-map id (`fr:A7-A11`, `fp:A6`,
`fr:A14`, `fr:B3`), in an intent or source pointer, or when the entry names the card as "unchanged" / "NOT amended". A
card amending itself is not listed. Ties go toward listing.

Two facts outside the brief (measured, see the trail):
1. All 51 `- amends:` entries are ONE line each, so no entry continues past the script's read (each is followed by a
   top-level `- ` line: 51 of 51).
2. Nine MORE amends entries exist in forms the script's `l.startswith("- amends:")` does not take: `- amends (...)`
   with sub-bullets, or `- amends C1-4 ...` with no colon. They are B2 part4b B2 `amends C1-4` entry, B4 part4b B4 amends entry, B8 part4b-2 B8 amends entries for C1-5, C1-6 and Order, A24 r2 part5 A24 (two looks) amends entry, A26 part6 A26 amends entry, A27 part7 A27 amends entry and B18 part9 B18 amends entry. Their targets are written below as
   `added:` lines. Four cards amended only by them are missing from the naive keys ("Extra keys" below).

Historical t-1980 counts before the A24/A36 split: not an amendment 42, added 43, stale 16, dangling 0. Keys: 78 (63 `amended by`, 15 `none`). Extra keys: 4.

## Map (historical 78 keys, in the naive map's order, plus A36)

- A1: amended by A12, A14, A24, A36, A27, A29
  - not an amendment: A25 -- part5 A25 amends entry names A1 only as the low bound of A21's quoted edge range "A1-A24" -> "A1-A25"
  - not an amendment: A28 -- part8 A28 amends entry, the same range form "A1-A26" -> "A1-A30"
  - not an amendment: A31 -- part10 A31 amends entry, the same range form "A1-A26" -> "A1-A35"
  - added: A27 -- part7 A27 amends entry "A1: IN for the `performer` row of every stage (caps, measures, cut rung 1); rung 2 -> conductor seam -> absent -> `stopped` ..." (A27's `- amends (...)` entry; part7 section 5, Accepted cards whose keys or lines change, lists A1)
  - note: A12 stays: part4-2 A12 amends entry points the `tools` column to A1's `launches.yaml`, and A12 Delivers (part4-2 A12 Delivers) adds that column to A1's file
- A10: none -- each naming is the parenthesis "`source_must_be: person`, A10", which cites A10 as the home of that column. The value lands in C3-6, not in A10's text
  - not an amendment: A2 -- part4 A2 amends entry "C3-6 `repositories` meaning (...; `source_must_be: person`, A10)"
  - not an amendment: A6 -- part4 A6 amends entry "C3-6 `doc_language`: `asked_when: never` kept, `source_must_be: person` (A10)"
  - not an amendment: A7 -- part4-2 A7 amends entry "C3-6 key `mock_base` (`source_must_be: person`, A10)"
  - stale: A2 -- held by the current line (part4-2 A10); an owner citation only, as above
  - stale: A6 -- held by the current line; an owner citation only
  - stale: A7 -- held by the current line; an owner citation only
- A11: none -- named only inside B14's `fr:A7-A11` (part5 B14 amends entry), a carry-map id range of C1-1, not card ids
  - not an amendment: B14 -- "the parallel-writers rule of the carry map (fr:A7-A11)"
- A12: amended by A24, A36, A35
- A13: amended by A34
- A14: none -- named only as the carry-map id `fr:A14` (B16, part8 B16 amends entry). A27's "A14's move waits" (part7 A27 amends entry) is a portion order with C4-4's stand-in, and A27's own list (part7 5. Accepted cards whose keys or lines change) leaves A14 out
  - not an amendment: B16 -- "carry map `dropped: fr:A14` -> `-> COORDINATOR.md: fr:A14 (as B16's cost rule)`" is a C1-1 row
- A15: amended by A31
- A16: none -- A9 names A16 only as the partner of field `tests_snapshot` ("`tests_snapshot` (A16)", part4-2 A9 amends entry). Both cards add that field to C3-1
  - not an amendment: A9 -- part4-2 A9 amends entry
  - stale: A9 -- held by the current line (part4-2 A16); a partner citation only
- A21: amended by A24, A25, A26, A27, A28, A31
  - added: A24 -- part5 A24 (two looks) amends entry "A21: X1's generated How checked line names the stage's required leaves with their filters." (A24 r2's `- amends (r1 -> r2 ...)` entry)
  - added: A26 -- part6 A26 amends entry "A21 edge "`amend:` ids valid only for A1-A25" -> "A1-A26"" (A26's `- amends (...)` entry)
  - added: A27 -- part7 A27 amends entry "A21: the generated How checked lists the implied rows PRESENT in `gate-rules.yaml` ..."
- A22: none -- A34 cites A22's counting as precedent ("unchanged code: `observed_red` counts as inversion does, A22", part10 A34 amends entry). The new method lands in C3-1 `probes.method`, and A22's ladder is unchanged (F218, part10 3. Forks: a waiver record, not a rung)
  - not an amendment: A34 -- part10 A34 amends entry
- A24: amended by A26
  - not an amendment: A25 -- part5 A25 amends entry, the high bound of the quoted range "A1-A24" in A21's edge
  - added: A26 -- part6 A26 amends entry the A36 explore-launch sentence "X2, X4 and X6 are asked of them at no exit" -> ... and part6 A26 amends entry "A24 r2 (part 5, by pointer; ...)"
  - note: A26 amends both A24 (two looks) and A36 (explore launch); the historical F6 treated them as two A24 headings.
- A36: amended by A24, A26
  - added: A24 -- part5 A24 (two looks) revises the explore launch, now A36
  - added: A26 -- part6 A26 amends the explore launch, now A36
- A26: amended by A24, A28, A33
  - not an amendment: A31 -- part10 A31 amends entry "with A26's and A33's changes the sets read" (cites whose changes the C3-2 sets add up) and "`amend:` ids "A1-A26" (A26)" (names who set the old bound)
  - added: A24 -- part5 A24 (two looks) amends entry A36's goal row and A26's X4 line, amended by pointer (t-1949 F4)
  - note: A28 stays for part8 A28 amends entry "A26 X4 (part 6, a sibling's file), by pointer". Its "enum `outcome` (A26)" is an owner citation. A33 stays for part10 A33 amends entry "A26 L19 by pointer ...; A26 L4 by pointer"
- A27: amended by A30
- A28: amended by A29
- A30: amended by B16
  - not an amendment: A28 -- part8 A28 amends entry, the high bound of the quoted range "A1-A26" -> "A1-A30"
  - note: B16 stays for part8 B16 "Part (d) ... is an AMENDMENT to C4-6 and A30, built with them"
- A31: none -- A33 names A31 only as the place where the full sets are written ("the full sets in A31's amends", part10 A33 amends entry)
  - not an amendment: A33 -- part10 A33 amends entry
- A33: none -- each naming cites A33's set change or one of its lines. None changes A33's text
  - not an amendment: A31 -- part10 A31 amends entry "with A26's and A33's changes the sets read" (a sum written into C3-2)
  - not an amendment: A34 -- part10 A34 amends entry "(L1, L3, L5's line; A33 L14's and A35 L12's lines)": the `common` entry is C2-1 data, and A33 itself adds L14 to it (part10 A33 amends entry)
  - not an amendment: A35 -- part10 A35 amends entry "(`stand` reaches `tests` and `reds` by A33's set change, F215 (a))"
- A35: none -- each naming is a range bound or a content citation
  - not an amendment: A31 -- part10 A31 amends entry, the high bound of the quoted range "A1-A35" in A21's edge
  - not an amendment: A34 -- part10 A34 amends entry "A35 L12's lines", held in the C2-1 `common` entry
- A6: none -- B2 names `fp:A6`, a carry-map id of C1-1 (part4b B2 `amends:` entry "dropped "fp:A6 (... no SessionStart hook, plan 3.5)""), not card A6
  - not an amendment: B2 -- part4b B2 `amends:` entry
  - stale: B2 -- held by the current line (part4 A6); a carry-map id, not the card
- A7: none -- named only inside B14's `fr:A7-A11` (part5 B14 amends entry)
  - not an amendment: B14 -- a carry-map id range
- A8: amended by A31
- A9: amended by A29, A30
  - not an amendment: A16 -- part4-2 A16 amends entry "`runs` field `tests_snapshot` (A9)", the partner of the field (both add it to C3-1)
  - stale: A16 -- held by the current line (part4-2 A9); a partner citation only
- B1: amended by B16
  - not an amendment: B11 -- part4b-3 B11 amends entry "BOOT's line classes (B1, B3) admit no count line ..., so B1 is NOT changed"
  - not an amendment: B13 -- part4b-4 B13 amends entry names "B1's class 2 lines" as a user of B3's plan-id resolver. The change lands in B3
  - not an amendment: B21 -- part9 B21 amends entry "B1's line classes are closed and a BOOT rule line reruns B1's eval" (why no BOOT line is added)
  - stale: B11 -- held by the current line (part4b B1); explicitly not changed
  - stale: B13 -- held by the current line; a user citation only
- B10: amended by B11, B13
  - note: B11 stays by the tie rule: part4b-3 B11 amends entry "B10 (a large idea keeps its goal document; the list holds one pointer record of kind `idea` with `goal: <path>`)"
- B11: amended by B12, B14, B15, B21
- B12: none -- B11 names B12 only in a frame section 1 layout row, "`forge/mods/` | forge | B11, B12" (part4b-3 B11 amends entry), which cites a co-owner
  - not an amendment: B11 -- part4b-3 B11 amends entry
  - stale: B11 -- held by the current line (part4b-4 B12); a co-owner citation only
- B13: amended by B15, B16, B20
- B14: amended by B18, B19
  - not an amendment: B17 -- part9 B17 amends entry "B14 rule 6 and section 1: NOT amended -- B14 r1 already points at this sweep"
  - added: B18 -- part9 B18 amends entry "B14 rule 3's existing line "push before a worktree launch" + `(case: FH-6064, workers lacked unpushed commits)`" (B18's `- amends C1-4 AS BUILT ... Also amends` entry)
- B17: amended by B14
  - not an amendment: B19 -- part9 B19 amends entry "(one step, B17 (b)'s order)": B17 (b) already writes B19's step into its order (part9 B17 Delivers "... -> `local/` refs, local-only history and old roots (B19) -> ...")
  - not an amendment: B21 -- part9 B21 amends entry "B17's pointer goes to CLAUDE.md per F197" (says where B17's line lives)
  - note: B14 stays by the tie rule (fork F2): part5 B14 amends entry "the sibling cards by pointer, nothing doubled: B17 (the session-start sweep of worktrees, rule 6)"
- B18: amended by B14
  - note: by pointer, tie rule (fork F2): part5 B14 amends entry "B18 (the owns overlap of open dispatches, rule 3)"
- B19: amended by B14
  - note: by pointer, tie rule (fork F2): part5 B14 amends entry "B19 (its rollback half points to rule 3's one rule)"
- B2: amended by B7, B11, B14, B17
  - not an amendment: B1 -- part4b B1 amends entry "B2 prints "not written yet (B1)"" (a frame section 6 row) and "B2 reads it" (C0-4 `launch`). B2's own text already holds both (part4b B2 keys K6, part4b B2 edges)
  - not an amendment: B5 -- part4b B5 amends entry "C1-5 K3 and owns (as B2)" and "C1-4 events ... (the list in B2)". B2's list already holds those events (part4b B2 `amends C1-4` entry)
  - not an amendment: B9 -- part4b-2 B9 amends entry "C1-4 event list (B2) gains ..." (the brief's own example). B2's list already says "B9 adds `refuse` and `ask_owner`" (part4b B2 `amends C1-4` entry)
  - stale: B1 -- held by the current line (part4b B2); see above
  - stale: B5 -- held by the current line; see above
  - stale: B9 -- held by the current line; see above (fork F4)
- B21: none -- B17 names B21 only as the table that holds its two C1-1 lines ("written in B21's table as rows 11 and 10", part9 B17 amends entry). B21's table already holds them (part9 B21 Delivers); B18's rows 6 and 9 likewise (part9 B21 Delivers)
  - not an amendment: B17 -- part9 B17 amends entry
- B3: amended by B13, B14, B20
  - not an amendment: B11 -- part4b-3 B11 amends entry "BOOT's line classes (B1, B3)" (a citation) and "B3 COORDINATOR rule applies unchanged"
  - not an amendment: B21 -- part9 B21 amends entry "fr:B3 moves from ..." names a carry-map id of C1-1
  - stale: B11 -- held by the current line (part4b B3); explicitly unchanged
- B4: amended by B12
- B5: amended by A30, B18
  - not an amendment: B2 -- part4b B2 `amends:` entry "+ the budget hook (B5)" and "`budget.py` (B5)": owner citations inside C1-5's K3 and owns
  - added: B18 -- part9 B18 amends entry "B5 TOKENS "the last usage line" -> "the newest transcript line that holds usage; ...""
  - stale: B2 -- held by the current line (part4b B5); an owner citation only
- B6: none -- B11 says "B6's `friction:` line is unchanged" (part4b-3 B11 amends entry)
  - not an amendment: B11 -- part4b-3 B11 amends entry
  - stale: B11 -- held by the current line (part4b B6); explicitly unchanged
- B7: amended by B9, B11, B14
- B8: amended by B19
  - not an amendment: B11 -- part4b-3 B11 amends entry "(row `worklist`, `state: not_built` until this card lands, B8)": B8 is named as the home of the `state` form, and the row lands in C1-6
  - not an amendment: B16 -- part8 B16 amends entry "C1-6/B8 `forge/TESTING.md` rule 2": `forge/TESTING.md` is C1-6's file (part2 C1-6 owns), and B8 holds no TESTING.md text
  - stale: B11 -- held by the current line (part4b-2 B8); a citation of a form's home only
- B9: amended by B11
- C0-1: amended by B13
- C0-2: amended by A27, B13
  - added: A27 -- part7 A27 amends entry "C0-2: + `measure/mybooks/seeds/`, `answers/tests-root.md` (F127 (a)) and the owner's story file ..."
- C0-3: amended by B13
- C0-4: amended by A27, A30, B1, B4, B12
  - added: A27 -- part7 A27 amends entry "C0-4 (F124 (a); t-1965 F7): `arm.py prepare --seed <...>` applies `patch.diff` to the run's OWN clone ..."
  - added: B4 -- part4b B4 amends entry "C0-4 (...) run row `tokens` (in, out, cache read, cache write) -> `tokens` per model ..." (B4's `- amends (text replaced -> new):` entry at part4b B4 amends entry, whose sub-bullets the script did not read)
  - note: B12 stays by the tie rule: part4b-4 B12 amends entry "used by every caller that holds per-call usage (B12 here; C0-4 `collect` when its harness output carries per-call usage)"
- C1-1: amended by B1, B2, B3, B5, B6, B7, B9, B10, B11, B13, B14, B15, B16, B17, B18, B21
  - added: B18 -- part9 B18 amends entry "Also amends (t-1974 F6: no new rule text): C1-1 COORDINATOR -- cases added to the carried rules fr:A13 (FH-1038) and fr:A7 (FH-6111)"
- C1-2: amended by B1, B16, B20
- C1-3: amended by B20
- C1-4: amended by B2, B5, B7, B9, B14, B15, B17, B18
  - added: B2 -- part4b B2 `amends:` entry "- amends C1-4 (...) -> THE WHOLE CLOSED EVENT LIST, stated here once (F12)" (B2's second amends entry, with no colon)
  - added: B18 -- part9 B18 amends entry "- amends C1-4 AS BUILT (`forge/tools`), each line once, nothing doubled: `journal.py` -- `--run "<cmd>"` ..."
- C1-5: amended by B2, B5, B8, B9, B11, B14, B17, B19
  - added: B8 -- part4b-2 B8 amends entry "- amends C1-5 (...): pre-push, before `ci.py`, scans the WHOLE pushed range ..."
- C1-6: amended by B3, B4, B8, B11, B13, B15, B16
  - not an amendment: B19 -- part9 B19 amends entry names C1-6 only inside B8's quoted Delivers text "(... no Actions run exists until C1-6's `ci.yml` is pushed)"
  - added: B4 -- part4b B4 amends entry "C1-6 job list (...): row `rates` -> `price.py check --base <ref>`."
  - note: B8 stays, but its carrier is part4b-2 B8 amends entry "- amends C1-6 (...): job row `secrets` -> ...". The naive source part4b-2 B8 amends entry "(C1-6)" is only a pointer
- C1-7: amended by B9
- C2-1: amended by A21, A26, A32, A33, A34
  - added: A26 -- part6 A26 amends entry "C2-1's map line refs:A20 -> `deep-look`" and part6 A26 amends entry "C2-1 `craft-pages.yaml`: row `deep-look`; new column `data` ..."
- C2-2: amended by A10, A21, A31, A35
- C2-3: amended by A4, A7, A8, A15, A25, A26, A31, A32, A33
  - added: A26 -- part6 A26 amends entry "C2-5 `red-analysis.md`, C2-3 `check-selection.md`: the rules the carry lines below send there"
- C2-4: amended by A4, A7, A24, A25, A26, A28, A29, A32, A33, A35
  - added: A24 -- part5 A24 (two looks) amends entry "C2-4 `exploration.md`, `stand.md` page rules (`amend:A24`)"
  - added: A26 -- part6 A26 amends entry "C2-4: `exploration.md` = the FIRST-LOOK page; NEW page `f/craft/deep-look.md` ..." and part6 A26 amends entry "NEW `f/data/perturbations.yaml` (under C2-4)"
- C2-5: amended by A16, A25, A26, A28, A31, A33, A35
  - added: A26 -- part6 A26 amends entry "C2-5 `red-analysis.md` ...: the rules the carry lines below send there. Every rule ends `(amend:A26)`"
- C2-7: amended by A30, B4
  - added: B4 -- part4b B4 amends entry "C2-7 ("money keys stripped" -> "price per run"); K4 -> ..."
- C2-8: amended by A30, B4
  - added: B4 -- part4b B4 amends entry "C2-8 ("No money figure.") -> "price per context and in total with tariff date; ...""
  - note: A27 part7 A27 amends entry "C2-8, C4-7: unchanged (F128 (a))" is no amendment of C2-8
- C3-1: amended by A2, A3, A4, A5, A7, A9, A15, A16, A17, A22, A24, A25, A26, A27, A28, A34, A35
  - added: A24 -- part5 A24 (two looks) amends entry "C3-1 `empty-outcomes.yaml` + row `nothing_beyond` (section `findings`, `needs: reason`; ...)"
  - added: A26 -- part6 A26 amends entry "C3-1 `record-schema.yaml` `findings`: `outcome` enum + `open`, `bug` (F113 (a)); ..."
  - added: A27 -- part7 A27 amends entry "C3-1: thin node = `record-schema.yaml` with the sections of the six stage rows ..."
- C3-2: amended by A3, A4, A6, A7, A8, A10, A12, A16, A21, A24, A36, A26, A27, A28, A31, A32, A33, B16
  - added: A26 -- part6 A26 amends entry "C3-2 craft sets: `reds` = red-analysis, bug, exploration, deep-look; ..."
  - added: A27 -- part7 A27 amends entry "C3-2: thin values of `stages.yaml`: every row `critic: none`, ..."
- C3-3: amended by A3, A4, A6, A7, A8, A9, A16, A23, A24, A36, A25, A26, A27, A28, A30, A33, A34
  - added: A23 -- part4-2 A23 amends entry "part3 C3-3 Delivers `lower_seq` leaves the predicate list, `live_ref` joins it; G4.1 wording"
  - added: A26 -- part6 A26 amends entry "C3-3 X4 meaning widened (F113 (a); ...); predicate `no_stale` renamed `no_unresolved`; ... `red-causes.yaml` `flaky` `needs`"
  - added: A27 -- part7 A27 amends entry "C3-3: thin node = `gate-rules.yaml` with TWO rows: X1 ... and W1 ..."
- C3-4: amended by A8, A16
- C3-5: amended by A2, A3, A4, A5, A6, A7, A22, A24, A36, A25, A26, A27, A28, A29, A30, A33, A34, A35
  - added: A26 -- part6 A26 amends entry "C3-5 test_report "Looked at beyond the requirements": per place its answer; ..."
  - added: A27 -- part7 A27 amends entry "C3-5: thin node = `person-docs.yaml` row `test_report` only; ..."
- C3-6: amended by A1, A2, A6, A7, A8, A9, A10, A26, A27, A29, A30
  - added: A26 -- part6 A26 amends entry "C3-6 key `perturbations` (default none; ...)"
  - added: A27 -- part7 A27 amends entry "C3-6, C3-8: whole in the thin pass." (A27's own list, part7 5. Accepted cards whose keys or lines change, names both)
- C3-8: amended by A4, A5, A7, A15, A27
  - added: A27 -- part7 A27 amends entry "C3-6, C3-8: whole in the thin pass." (part7 5. Accepted cards whose keys or lines change lists C3-8)
- C4-1: amended by A1, A2, A3, A4, A5, A12, A13, A14, A19, A24, A36, A27, A28, A29, A30, A34
  - added: A27 -- part7 A27 amends entry "C4-1: thin node = `start`, `next`, `resume`; states ..."
- C4-2: amended by A1, A7, A13, A16, A22, A25, A34
- C4-3: amended by A3, A4, A5, A6, A25, A27, A28
  - added: A27 -- part7 A27 amends entry "C4-3: thin node = `questions.yaml` form `critical`; ..."
- C4-4: amended by A1, A2, A9, A14, A25, A27, A29, A35
  - added: A27 -- part7 A27 amends entry "C4-4: thin node = `run_tests.py run|record`, ..."
- C4-5: amended by A1, A2, A12, A13, A18, A27, A35, B17
  - added: A27 -- part7 A27 amends entry "C4-5: thin node (F126 (a)) = the profile `hosts/claude-code.yaml`, ..."
- C4-6: amended by A1, A17, A27, A29, A30, A35, B4, B16
  - added: A27 -- part7 A27 amends entry "C4-6: thin node = `journal.py` whole; `dashboard.yaml` + view `thin` ..."
  - added: B4 -- part4b B4 amends entry "C4-6 ("no rate value in any repo file") -> ..."
- C4-8: amended by A25
- X1: amended by A24
  - no heading: X1 is a row of the frame's gate table in section 3 "Where judgment lives" (spec.md 3. Where judgment lives), row frame section 3 gate table X1, form `| X1 | <check> | <sections> | <owner> | <class> | <on fail> |`. No card heading can hold the line (fork F1)
  - note: the naive source part4-3 A36 (explore launch) amends entry ("rules X1, X3, X5 at its own exit") is a use. The amendment is A24 r2 part5 A24 (two looks) amends entry "frame 3 X1 reading: a filtered leave is met by a live row of that section, written at the exiting stage ..."
- X2: amended by A36
  - no heading: frame section 3 gate-table row X2, the same form as X1
  - note: part4-3 A36 (explore launch) amends entry "frame 2c + rows `group: explore` are advisory: X2, X4 and X6 are asked of them at no exit" narrows where X2 applies (kept by the tie rule)
- X3: none -- part4-3 A36 (explore launch) amends entry names X3 only as a rule the `explore` launch row asks at its own exit, which is C3-2 launch-row data (a use). X3's text and scope are unchanged
  - not an amendment: A36 -- part4-3 A36 (explore launch) amends entry
  - no heading: frame section 3 gate-table row X3, the same form as X1
- X4: amended by A24, A26, A28, A36
  - added: A26 -- part6 A26 amends entry "C3-3 X4 meaning widened (F113 (a); the link F3+F9, points (1), (4)): "no stale row and no live `open` place among the stage's rows; ...""
  - no heading: frame section 3 gate-table row X4, the same form as X1
  - note: A36 changes X4 at part4-3 A36 (explore launch) amends entry (no X4 for `group: explore` rows) and A24 changes it at part5 A24 (two looks) amends entry ("X1's filter and X4 skip a row whose `about` is `plan:exploration`"). A28 changes it at part8 A28 amends entry "A26 X4 ..., by pointer: the link's points (1) and (4)"
- X5: none -- part4-3 A36 (explore launch) amends entry names X5 only as a rule the `explore` launch row asks at its own exit (a use, as for X3)
  - not an amendment: A36 -- part4-3 A36 (explore launch) amends entry
  - no heading: frame section 3 gate-table row X5, the same form as X1
- X6: amended by A36
  - no heading: frame section 3 gate-table row X6, the same form as X1
  - note: the same frame 2c sentence as X2 (part4-3 A36 (explore launch) amends entry); A26 keeps "X2 and X6 at no exit" (part6 A26 amends entry)

## Extra keys (amended, absent from the naive keys; the DoD does not count these)

Each is amended only through an entry the script did not read, and has no `amended by` line today (checked against
the 47 `- amended by:` lines).

- extra A4: amended by A24 -- part5 A24 (two looks) amends entry "A4 Delivers "the product look is the `explore` launch after stage 2 (A24, F74)" -> "the product look is the stage-2 performer's own work (A24 r2)""; heading part4 A4
- extra C0-5: amended by B4 -- part4b B4 amends entry "C0-5 (...) "money keys stripped" -> "price per run (B4)"; K3 ..."; heading part2 C0-5
- extra C2-6: amended by A27, B4 -- part7 A27 amends entry "C2-6's rule "never a measuring project's source" + "except an A27 story seed ..."" and part4b B4 amends entry "C2-6 (...) -> "price from the arm's run row""; heading part2b C2-6
- extra C4-7: amended by A27, B4 -- part7 A27 amends entry "C4-7 deps + "A27's last portion closed"" and part4b B4 amends entry "C4-7 (...) -> "price per run, per agent ...""; heading part3b C4-7

## Amends entries outside the script's form (the 9)

- part4b B2 `amends C1-4` entry B2 `- amends C1-4 (...)`: target C1-4
- part4b B4 amends entry B4 `- amends (text replaced -> new):` with 13 sub-bullets: targets C0-4, C0-5, C2-6, C2-7, C2-8, C4-6, C4-7, C1-6. Not targets: the frame, the part Common lines, F7/F15/F21, and "C0-1 K3 (...) unchanged"
- part4b-2 B8 amends entry B8 `- amends C1-5 (...)`: target C1-5
- part4b-2 B8 amends entry B8 `- amends C1-6 (...)`: target C1-6
- part4b-2 B8 amends entry B8 `- amends Order:`: no card target. It rewrites the frame section 4 Order, part 2 section 1 Order (part2 1. Scope and pointers) and frame section 6 row 1. The card ids inside it are the order string, and the C1 cards carry no phase line (`phase` occurs in the revision, scope, order, cards and trail; none in the C1 cards)
- part5 A24 (two looks) amends entry A24 r2 `- amends (r1 -> r2; ...)`: targets A36 (formerly A24 r1), C4-1, A1, A12, C3-3, X1, C3-2, C3-1, A26, X4, A21, A4, C2-4, C3-5
- part6 A26 amends entry A26 `- amends (...)`: targets C2-4, C2-5, C2-3, A21, C2-1, C3-2, C3-1, C3-3, X4, A24 and A36 (formerly A24 r1), C3-6, C3-5. Not targets: A28 (d) (cited: "has its home in A28 (d); this card reads it"), and `refs:A20`, `refs:A21`, `slices:A15, A16` (carry ids)
- part7 A27 amends entry A27 `- amends (...)`: targets as A27's own list part7 5. Accepted cards whose keys or lines change: C3-1, C3-2, C3-3, C3-5, C3-6, C3-8, C4-1, C4-3, C4-4, C4-5, C4-6, A1, A21, C0-2, C0-4, C2-6, C4-7. Not targets: C3-4, C3-7, C4-2, C4-8 ("wait"), A2 ("IN through the C4-5 hook"), A14 ("move waits"), A25 (deferred), C2-8 ("unchanged") (fork F3)
- part9 B18 amends entry B18 `- amends C1-4 AS BUILT ...` with "Also amends": targets C1-4, C1-1, B14, B5. Not targets: "Not changed: B5's `role:`/`caps:` lines, B14's id issue and session rules, B2's event list", and "written as B21 rows 9 and 6" (B21's table already holds them)

## Forks (the Lead's decision)

- F1 X1-X6 have no heading. They are rows of the frame's gate table (frame section 3 gate table rows X1–X6), so no `amended by` line can sit under them. Options: (a) one line under the frame's section 3 table, "X1 amended by A24; X2 and X6 by A36; X4 by A24, A26, A28, A36"; (b) rely on C3-3, the gate rows' code home, whose true line already holds A24, A26, A28 and A36; (c) skip. Recommended: (a). It costs one frame line and keeps the gate-row reader one hop from the amenders.
- F2 B14's "the sibling cards by pointer, nothing doubled: B17 (...), B18 (...), B19 (...)" (part5 B14 amends entry) can be read as amending them by pointer, or as pointing at their homes. Listed by the tie rule. Option: drop all three, which leaves B17/B18/B19 with no line (B19 then keeps none). Recommended: keep.
- F3 A27's "wait" cards and A2/A14/A25/C2-8 are dropped on the strength of A27's own list (part7 5. Accepted cards whose keys or lines change). Option: list A27 on C3-4, C4-2, C4-8 by the tie rule (C3-7 and C2-8 too, though C2-8 is named "unchanged"). Recommended: drop, because the card says which of its names change.
- F4 The stale removals on B2 (B1, B5, B9) follow the brief's own example. B2's text names each contribution inline (part4b B2 `amends C1-4` entry, part4b B2 keys K6, part4b B2 edges), so a B2 reader loses nothing. Option: keep them by the tie rule. Recommended: remove.
- F5 Out-of-form entries: the apply script must take the 9 entries and the 4 extra keys, or they stay without back-pointers. Recommended for the next pass: widen `amends_map.py`'s test from `startswith("- amends:")` to the regex `^\s*-\s+amends?\b` (the Lead's scratch script, outside this map).
- F6 Historically A24 had two headings (explore launch r1 and two looks r2), and the script took the first. The reviewed split assigns the explore launch to A36 and retains two looks as A24; A26 amends both, and A24 amends A36.

## Small choices closed

- A1 keeps A12: A12 Delivers adds column `tools` to A1's `launches.yaml` (part4-2 A12 Delivers).
- B10 keeps B11 and C0-4 keeps B12 by the tie rule (both prescribe a change to that card's flow).
- C3-3 keeps A34 although part10 A34 amends entry says "unchanged code": it names C3-3's `probe_per_autotest` reading.
- X2 and X6 keep A36 (a scope narrowing). X3 and X5 drop A36 (a use).
- C1-6 keeps B8, with its true carrier part4b-2 B8 amends entry noted.
- Ids are written in natural order (B1, B2, ..., B10), not in the naive map's string order.

## Trail (read, measured)

- Given: amends_lines.txt (51 lines), amends_naive_map.txt (78 keys), amends_map.py (whole).
- Grep `^- amends:` multiline `[^\n]*\n[^-#\n]` -> 0. Control of the same shape `[^\n]*\n[-]` -> 51 (all), and `\r?\n[ \t]` -> 0. So no `- amends:` entry continues.
- Grep -i `^\s*-\s+(\*\*)?amends?\b` over `*spec*.md` -> 60 (51 + 9). The 9 were read whole: part4b B2, part4b B4; part4b-2 B8; part5 2. Cards; part6 2. Cards; part7 2. Card, part7 5. Accepted cards whose keys or lines change; part9 B18.
- Grep `^- amended by:` -> 47 lines, used as the current lines. Grep `^#{2,4} (C\d+-\d+|[ABX]\d+)\b` -> every heading. Historically A24 had two; the reviewed split now gives A36 its own heading. X1-X6 have none.
- spec.md 3. Where judgment lives (gate table). part2 C1-6 (C1-6 owns `forge/TESTING.md`). part4-2 A12 (A12). part4b B1–B3. part8 B16 amends, PHASE and Delivers (d), and section 5 (Part (d) = amendment to C4-6 and A30). part9 B17 Delivers (B17 (b) order holds B19), part9 B21 Delivers (B21 rows 6, 9, 10, 11). part10 A34 amends and fork F218 (A22 mentions).
- Dangling check: every id named as a target has a heading in the heading list above, except X1-X6, which exist as frame gate rows (frame section 3 gate table rows X1–X6). Dangling: 0.
- DoD: `grep -c -E '^- (C[0-9]+-[0-9]+|[ABX][0-9]+): (amended by|none)' docs/tasks/specs/20261126-forge2-amended-by-map.md`. The Grep tool's count on this file is in the hand-back.
