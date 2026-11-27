# t-2103 critic verdict: B11 worklist (cc09fa7)

verdict: fit_with_fixes -- 2 fix-before-merge findings (1, 2), 1 more fix (3); review is PARTIAL, cut by the wall cap (see Not done)
worklist.py: fit_with_fixes -- the reseal and base reads let an unknown through (findings 1, 2)
session_start.py.next: fit -- additive block (10), cut order shifted by one step, nothing reordered
foreign_write.py.next: fit -- additive pane_road check before the existing body; the residual (script file, variable) is named in its docstring
tests: not judged -- 45 green in the tree; no probe, no row audit (wall cap)
DUPLICATION AND CONSISTENCY: none found: reads only -- lock reuses journal.take_lock/release_lock, session form reuses journal.SESSION_RE, ids reuse words.resolve_id/linked_worktree; no second lock, reader or regex seen in the parts read
CODE QUALITY: not judged in full -- functions listed by `grep -n "def "`; none read was over 60 lines, but not all were read
one road: not judged (wall cap)
VARIETY: finding 1 is the variety class (an unknown git result becomes a pass)
class completeness: surface = git reads of the list (git_list callers: cmd_check --base, cmd_reseal); both callers walked; other git callers (newest_tag, the commit check in cmd_check) not walked
probe: none -- wall cap reached at entry (2880/3600 s); no time for a control plus mutant runs

## Findings
1. forge/tools/worklist.py::cmd_reseal (and ::git_list) -- blocks merge. `head, why = git_list(root, "HEAD")`; when `why` is set (HEAD unreadable: a git timeout, an OSError, a repo with no commit) the code drops `why` and prints `no committed list: priority and release not judged`, then reseals. Scenario: a hand edit of `priority` in a checkout whose git call times out is resealed and the hand value gets a valid seal. Fix: `if why: raise Refuse("cannot judge: " + why)`; only `head is None and why is None` takes the "not judged" road. failure_class: capability.
2. forge/tools/worklist.py::git_list -- blocks merge. After the ref check, ANY `git show ref:LIST` error returns `(None, None)` = "absent". A git timeout or an OSError (git() returns `(None, str(e))`) is then read as "no list at the base": cmd_check prints `born: ... judged for form only` and runs no base_problems, so an owner-value change passes CI green. Fix: tell absence apart (`git cat-file -e ref:LIST` exit 128 with "does not exist"/"exists on disk, but not in", or `git ls-tree ref -- LIST` empty) and return the error otherwise; check prints `cannot judge` and exits 2.
3. forge/tools/worklist.py::field_problems -- fix before merge. An owner_source of form `pane <ts>` is accepted on `own.startswith("pane ")` only; the ts is not parsed. Scenario: a hand-written record with `"owner_source": {"priority": "pane x"}` passes record_problems and, as a new record, base_problems (which only compares records present at the base). Fix: parse the ts with the same parser now_ts() writes (fullmatch), and in base_problems flag a new or changed `pane` owner_source with no matching history entry of `by: pane`. Surface: owner-source form; neighbour walked: the W-<n> branch resolves to a live word (OK).

## Seam and class notes
- .next files vs main at 30f326a: diffed both (`diff <(git show 30f326a:...) ....next`); changes are additive; session_start shifts the cut thresholds 2->3, 3->4 and range(4)->range(5) consistently, and render(..., 4) follows. work_text never raises (OSError, SubprocessError caught; a non-`work list:` first line becomes `work list: unknown -- ...`).
- Builder's declared deviations: not judged one by one (wall cap). Read only: "reseal refusing an uncommitted set" -- confirmed in cmd_reseal (keys compared against HEAD); it forces a commit between `set` and a hand-fix reseal; a safe-way choice, the Lead's call.

## Spot-checks
- Narrow test file green in the tree (output in Trail).
- Data file is JSON syntax read with json.loads (load_rows), as the dispatch rule says.

## Not done (wall cap)
spec B11/B12/B14/B15/B21 text not read against the code; test review (Q5) and probe; one-road line; deviations list; register.tsx / marketplace / plugin.json not read.

## Trail
- `git status --porcelain` in C:/QAFactory/forge2-wt/t-2103: empty; HEAD cc09fa7.
- `git diff main...cc09fa7 --stat`: 10 files, 2329 insertions.
- `python -B -m pytest forge/tests/test_worklist.py -q -p no:cacheprovider`: `45 passed in 17.67s`.
- Read worklist.py lines 100-232, 594-725; grep of `def ` over worklist.py; forge/worklist-rows.yaml; the amended-by map rows for B11.
- `diff` of both .next files against `git show 30f326a:<path>`.
