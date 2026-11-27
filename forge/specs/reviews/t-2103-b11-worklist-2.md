# t-2103 critic verdict, part 2: B11 worklist (cc09fa7), the rest of the cut review

verdict: blocker -- 1 blocking finding (4), 1 fix before merge (5); PARTIAL again: this entry started at the session wall cap (hook line `wall 2880/3600 s -- at the cap: hand back done and not done`), so only list/add/line/ordering were read against the card
worklist.py (list, add, line, ordering): blocker -- `list --grep` hides done and dropped records against the card and K6 (finding 4); add's candidate order is not "newest activity first" (finding 5)
tests (Q5): blocker -- the K6 row passes `--all` beside `--grep` and so leaves open the very door finding 4 names; the rest of the table not audited
builder's deviations: `list --state X` implies --all -- fit (the state filter names the state wanted; the safe reading); `WORKLIST_TODAY` -- fit (the docstring names it as a test hook; check reads no clock, confirmed at worklist.py::today callers view/line/set only by the docstring, estimate, not verified); the others (per-field source dicts, stem sources form-checked only, lock via journal.take_lock, duplicate-id re-add order, fixture patching words.linked_worktree, takeover best-effort, K8 pane never driven) -- not judged (wall cap)
DUPLICATION AND CONSISTENCY: none found in the parts read: ordered() is the one sorter used by view, list and add candidates (that reuse is the cause of finding 5)
CODE QUALITY: none found in the parts read (activity, ordered, topic_candidates, cmd_add 307-343, line_of, cmd_view, cmd_line, cmd_list); none over 60 lines or 3 levels
one road: not judged (wall cap)
VARIETY: not judged beyond the first verdict's finding 1
class completeness: surface = which states a reader shows (filters of list/view/add candidates); walked: cmd_list (finding 4), topic_candidates (excludes done only: open/in_work/held/dropped as the card says -- fit), cmd_view (done/dropped absent: fit by build_view's reading not traced, estimate, not verified); neighbour axis "order of a shown set" walked in add candidates (finding 5) and line top (fit)
probe: none -- the wall cap was reached at entry; control run done (45 passed), no mutant time

## Findings
4. forge/tools/worklist.py::cmd_list -- blocks merge. The card's Delivers (2) says `list ... [--grep <text>]` is "search over every state, done and dropped included", and K6 says done and dropped records are "present in `list --all` and `list --grep`". The filter is `(a.all or a.state or r["state"] not in ("done", "dropped"))`: `--grep` does not widen it. Scenario: a dropped record `L-3` "closed thing"; `worklist.py list --grep closed` prints nothing, so the Lead searching for an earlier drop before `add --new` misses it (the very use the card gives search). The test row forge/tests/test_worklist.py::test_default_view_hides_closed_list_all_finds (line with `box("list", "--grep", "CLOSED", "--all")`) adds `--all` and so cannot see the defect. Fix: `a.all or a.state or a.grep or ...`, and drop `--all` from the grep half of that row so the row guards the door. failure_class: capability.
5. forge/tools/worklist.py::topic_candidates -- fix before merge. The card: `add` prints the same-topic records "newest activity first, at most 20, then `and N more`". The code returns `ordered(...)`, which sorts by her priority, then re-decide, then repeats, with activity only as the last key. Scenario: a topic with 25 candidates, 21 of them P1/P2 old ones; the record touched today, unset priority, falls past the 20 cut and is only in `and N more`, so the Lead's same-or-new judgment is made without the most recent record. Fix: `sorted(..., key=lambda r: (activity(r), idnum(r)), reverse=True)` in topic_candidates; a row in test_add_shows_candidates_then_writes with two candidates of different priority checks the order. failure_class: capability.

## Seam and class notes
- ordered() is shared by view, line, list and add; finding 5's fix must stay local to topic_candidates (view/line keep the K15 order).
- Not done (wall cap): Delivers (1) data shape, (2) set/owner-set/repeat/reseal/check text, (3) CI row, (4) pane and marketplace, (5); edges beyond the empty list; B12/B14/B15/B21 amendments; the rest of the Q5 table and row budget; the remaining deviations; one-road line; a probe. The Lead re-dispatches these or takes the merge risk; the decision is the Lead's.

## Spot-checks
- `--state` implies --all: confirmed in cmd_list (`a.state` in the widening term).
- add candidates exclude only `done`: confirmed in topic_candidates; card lists open, in_work, held, dropped -- matches.
- line top marker `<priority|x repeats|re-decide>` and the 200-char cut: read in line_of, matches the card form.

## Trail
- Card read: forge/specs/20261125-forge2-light-factory-spec-part4b-3.md B11 amends, Delivers (1)-(5), owns, deps, keys K1-K15 (head), edges (head).
- Read worklist.py 238-262, 303-345, 525-580; `grep -n "def \|WORKLIST_TODAY"` over it; `grep -n "grep\|def test"` over test_worklist.py.
- `git status --porcelain` in C:/QAFactory/forge2-wt/t-2103: empty; HEAD cc09fa7.
- `python -B -m pytest forge/tests/test_worklist.py -q -p no:cacheprovider`: `45 passed in 10.69s`.
