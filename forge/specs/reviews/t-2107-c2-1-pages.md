Critic verdict t-2107: C2-1 craft page index, page check (`git -C C:/QAFactory/forge2-wt/t-2107 diff main...9401abf`, base 30f326a; spec part2b::C2-1 with A21, A26, A32, A33, A34)

verdict: blocker
failure_class: capability (the work; the dispatch is sound)
factory/tools/pages_check.py: blocker -- a CI red from the universality scanner (F1); with stages.yaml missing it writes and passes pages that lack their due rows (F2); a data file of any other shape crashes with a traceback (F3); writes `None` into a page (F4)
factory/data/craft-pages.yaml: blocker -- test-code criteria lack A34 L7 and half of L8 (F6); a stray key no code reads (F7)
factory/tests/test_pages_check.py: fit_with_fixes -- three load-bearing branches have no row (F8)
tests (Q5): fit_with_fixes -- all 8 rows the spec's table asks for are there, with their sources; the after_critic, stages-differ and absent-gate-row branches have no row (F8); a subprocess for every row (F8)
DUPLICATION AND CONSISTENCY: fit_with_fixes -- only 4 of 11 finding lines give a door (F9); the other analog is `measure/tools/arm.py:52 load_json`, outside factory/ and not importable (the factory imports nothing outside factory/), so not a finding; rows.py twin: seam note S1
CODE QUALITY: fit_with_fixes -- every function is under 60 lines and 3 nesting levels; the dead key (F7) and the `None` text (F4) are findings; none found beyond them: grepped `def load_json|def sections|refs\|slices|def digest_ids` over the repo's *.py files
one road: fit -- `--write-how-checked` is the only writer of How checked; id sources are data rows (`sources`, `amend`); no branch on a language or project. The scanner flags the `python` door text (F1).
VARIETY: blocker -- an unknown data shape gives a traceback rather than exit 2 (F3); a missing stages.yaml becomes a silent empty default (F2)
architecture: fit_with_fixes -- the diff touches AR-1, AR-9, AR-10, AR-19, AR-27/28 and AR-29, and neither commit names any of them (F10)
class completeness: walked the loader (load_json, the shape of the index, stages.yaml, gate-rules.yaml and gate-row fields) and every check (statements, rows, data, sections, craft, how); the input surface "data file given to the check" was walked by magnitude (an empty list), by shape (a dict, a missing key, a missing field) and by a missing peer file -- F2, F3 and F4 are its instances; the "id cited in a page" surface gives F5
probe: none -- no mutation runner that takes `--root` exists in forge 2 (`ls forge/tools`: no such tool); the control run was green (19 passed) and `git status --porcelain` was empty; F2-F5 were shown with a scratch root built for each input instead (trail)

## Findings

F1 (blocks merge) `factory/tools/pages_check.py:18` DOOR_HC. `python -B forge/tools/universality.py --root .` in the worktree exits 1: `new: factory/tools/pages_check.py::python factory/tools/pages_check.py:18`. The ci.yml universality job will be red. There is no CI run on `w/t-2107` yet (`gh run list --branch w/t-2107` is empty). Fix: name the door as `factory/tools/pages_check.py --write-how-checked`, without the runtime word, or add an allow row to `forge/universality-names.json` with a reason (the F10 runtime is not a project's language). The allow row is the Lead's choice.

F2 (blocks) `pages_check.py:148-151` run, `:124` check_rows. stages.yaml is optional even when gate-rules.yaml is there. Input: gate-rules `[G1, X1]` present, stages.yaml absent, a page indexed with `stages: ["s"]`. Wrong output: `--write-how-checked` writes `Gate rows:\n- X1: x` with no G1, and the check then exits 0 (trail run `rules_only`). It also skips the page/stages comparison (`if stages else []`). A `[]` stages.yaml does the same. This is an unknown turned into a pass (AR-27/28; frame 2b: "never an empty list"; A21: no due rule may go untold). The spec allows only gate-rules.yaml to be absent. Fix: when gate-rules is present and stages.yaml is absent or an empty list, raise Cannot (exit 2) naming stages.yaml and its card C3-2. Add a row for it.

F3 (blocks) `pages_check.py:25-33` load_json, `:146-151`. Nothing checks the shape. Input: `stages.yaml` = `{"schema":"stages/1","rows":[...]}`, the form of the only data file already in the repo (`factory/data/secret-patterns.yaml`, `{"schema", "rows"}`). Output: `TypeError: string indices must be integers` and a Python traceback, exit 1 (trail `stages_rows_dict`). An index with no `amend` gives `KeyError: 'amend'` (trail `no_amend`). The same happens with no `sources`, or a stage or gate row with no `id`. Exit 1 reads as "red with findings", yet it prints none, and a traceback is friction by RULES (Measurement and money, P11). The builder's top-level-list choice clashes with the repo's one data form: frame 2b and 2c fix no form, and C3-2 and C3-3 are not written. Fix: check each loaded file against the expected form, and on any other shape or a missing key raise Cannot naming the file, the key and the expected form. Add one row per shape. Fixing the stages.yaml and gate-rules.yaml form for C3-2 and C3-3 is the Lead's call (S1).

F4 (blocks) `pages_check.py:82` render. A gate row with neither `debt` nor `checks` renders as `- G1: None` in a page every run reads, and the check exits 0 (trail `rule_no_text`, after `--write-how-checked`). Fix: report it as a finding (`gate row G1 has no debt text; door: ...`) or raise Cannot; never print `None`. This is a sibling of F3 (an absent field).

F5 (Lead's decision; recommended this round) `pages_check.py:96-99` check_craft. Amend ids in `## Craft` are checked against their range, but `refs:` and `slices:` ids in the same text are not checked against their digests. Input: Craft text `rule (refs:A99, slices:A40)`. Output: `pages: 0 finding(s)`, exit 0 (trail `craft_invented`). The edge says "an id not in its digest -> red (an invented home never counts)". The Lead's review of cedc0ee dropped only the own-page citation rule. Digest membership is the edge itself, and the TOKEN regex already parses these ids. Fix: flag a refs or slices token whose id is not in `ids[kind]`, and add a row.

F6 (blocks; or the Lead opens a node with an id) `factory/data/craft-pages.yaml:14` test-code `critic_criteria`. A34 amends "`test-code`'s own criteria + L7, L8". L7 is missing; the builder declared this. That is 11 + 18 bullets of `qa-code-critic.md` § Where bugs hide (30-40) and § Techniques (45-62) whole, plus the Tools line 78, minus the excepted PA rows, plus the PA-205/222 single-run words. The source exists at `C:/QAFactory/forge-repo/ai-packages/qa-factory/agents/qa-code-critic.md`. L8 is cut short without being declared: "read every test first, then probe; never rerun a green the record holds; a finding is worded, never fixed by the critic" were dropped. Failure: the G4 critic's How checked misses criteria that A34 K1 checks for test-code. Fix: add L7 and the rest of L8 this round. Otherwise the Lead opens a node with an id and an owner for them; that choice is the Lead's.

F7 (fix before merge) `craft-pages.yaml:16` exploration row `"first look": null`. The C2-1 or A26 index schema has no such field, and no code reads it (Continuity: every field produced has a reader). Its name holds a space. Fix: delete it. The first-look role belongs on the page (A26).

F8 (fix before merge) `factory/tests/test_pages_check.py:48-66` ROWS. Three branches have no row, and a mutant that removes any of them would survive (reasoned; no runner): (a) the `after_critic` column in due_ids (G4.5, G6.1 and D1 sit there); (b) `:124-127` "stages ... differ from stages.yaml"; (c) `:90` "stage names gate row ... absent". Fix: add three table rows. Also, every row starts a subprocess where `pages_check.main(["--root", ...])` in-process would do (non-blocking; 3.51 s, under budget).

F9 (fix before merge) Finding lines with no door: `:53` not in digest, `:55` two places, `:107` section missing, `:121` page with no row, `:123` stage names page, `:126` stages differ, `:90` absent gate row. Lines 18, 104 and 100 give doors. AR-9 / RULES Refusals and doors: never leave the reader without a move. Fix: give each line its door (drop or add the index row, add the section, move the id, and so on).

F10 (non-blocking) Neither cedc0ee nor 9401abf names the AR-n invariants or the RULES lines it touches (RULES Changing the factory). Fix: the hand-back or the next commit names AR-1 (code-held X1-X6 and SECTIONS; second loader, S1), AR-9, AR-10, AR-19, AR-27/28 and AR-29, and how each is kept.

## Seam and class notes
S1. Twin rows.py (C3-2) is not built. Its `load()` of every factory/data/*.yaml is the one loader (AR-1), and its W1 "each craft id in craft-pages.yaml with its file" doubles check_rows and the file-absent check. `X_IDS` (`:16`) is a closed set held in code that W1 will also need. Proposed node, for the Lead to open (owner C3-2's builder): pages_check reads stages.yaml and gate-rules.yaml through `rows.load()`, and the implied X set comes from data, once C3-2 lands. The same node fixes the stages and gate-rules form named in F3.
S2. The spec does not say what text stands for a gate row. The builder chose `debt` with `checks` as the fallback, plus the headings `Gate rows:` and `Critic criteria:`. This is a finding against the spec (A21 or F12). The Lead names the text, and the C3-3 rows must fill it.
S3. Only new files were added; no file another node owns was touched.

## Spot-checks
- 65 ids: refs has 38 A ids and 8 D ids, slices 27 A and 7 D (python regex over both digests). A loose `^\W*([AD]\d+)\b` control found nothing extra. Every A id has exactly one home: the real run shows no "has no home", "in two places" or "not in its digest".
- Builder's claim "15 findings, all pages not yet written": reproduced. There are 14 `file absent` lines, plus `deep-look: data perturbations names no factory/data/perturbations.yaml`, a file C2-4 will write.
- `amend: {first:1,last:35}`: matches part10's readers line "A21 (`amend:` ids A1-A35)". No card `### A36` or later exists in forge/specs (grep with an empty result; control: the same grep finds `### A35`).
- "Due from that stage on" read literally: this is fit. A21's parenthesis defines "due at" as the exit or after_critic column, and C3-2 makes the `exit / after_critic` column the one source of where a rule falls due. A rule first named at an earlier stage is not repeated on later pages; that is the spec's choice.
- The A26 `data` column and its check, A34's common entry with the K4 row, and A32 L16/L21 and A33 L14/L16/L18 in the criteria were all checked against their cards. A33 L18 drops "(cause `expectation_stricter_than_requirement`)", which is acceptable because the vocabulary is cited from its data and never copied.
- Amend ids in the index: the builder refuses them (they read as "not in its digest") and accepts them only in page text. This is fit, because a single amend card spreads rules over several pages, so the one-home rule cannot apply to it.

## factory/RULES.md, heading by heading
- Refusals and doors: F9.
- Text shown to a person: none; no page text reaches a person here.
- Contracts between code and roles: only the count and the finding lines go to stdout (fit); "every state the other side can return" fails on shape (F3).
- Identity and evidence: none.
- Delivery and reporting: paths are relative to root (fit).
- Measurement and money: a traceback is friction (F3).
- Writing factory code: no PyYAML, json is stdlib (fit); the regexes are proven by rows (fit); the script stands on a `mechanism:` line (fit).
- Universality: F1 and F3; no Cyrillic (scanner).
- One action, one way: F9 and S1.
- Continuity between stages: F7, F2 and F4.
- Changing the factory: F10.
- Hygiene: the index stores LF for all factory files (`git ls-files --eol`); the new files match.

## Trail
- Read: diff whole; part2b::C2-1 and C2-2 keys; part4-2 A21; part6 A26 (amends, Delivers); part10 A32 L16/L21, A33 amends L8-L18, A34 whole with L1-L13, A35 L12, readers line; frame 2b/2c and section 1 AR list; part3 C3-2 table; factory/RULES.md whole; amended-by map C2-1; commit messages of cedc0ee and 9401abf with the 9401abf code diff.
- `python -B -m pytest factory/tests/test_pages_check.py -q -p no:cacheprovider` -> `19 passed in 3.51s`.
- `python -B factory/tools/pages_check.py` -> `pages: 15 finding(s)`, exit 1.
- `python -B forge/tools/universality.py --root .` -> exit 1, `new: factory/tools/pages_check.py::python factory/tools/pages_check.py:18`.
- Scratch roots (scratchpad/w/mk.py, one per case): `craft_invented` -> 0 findings, exit 0; `no_amend` -> `KeyError: 'amend'`; `stages_rows_dict` -> `TypeError: string indices must be integers, not 'str'`; `rules_only --write-how-checked` -> `Gate rows:\n- X1: x`, 0 findings; `rule_no_text --write-how-checked` -> `- G1: None`, 0 findings.
- Builder report not in the dispatch: its `similar:` and `friction:` lines were not checked.
