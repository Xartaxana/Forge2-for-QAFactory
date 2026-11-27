# t-2106 critic: B17 (c) (d) start facts, commit ffd8562 (post-hoc)

verdict: blocker -- 5 blocking findings (F1-F5); failure_class: capability (the card was right, the work missed it)
forge/hooks/session_start.py: blocker -- outside values reach the facts and previous lines unclipped and the writer encodes strictly (F1); a failed git call is printed as a known zero (F2, AR-27/AR-28); the budget starts after the stdin read (F3); a duplicated git reader (F4); nesting (F5)
forge/tests/test_hooks.py: fit_with_fixes -- K4-K6 rows are real and cheap (13 new rows, 3.79 s), but process_list itself has no row (F7)
forge/hooks/budget.py, foreign_write.py, pre_compact.py (`# hook:` lines): fit -- one additive line in the first 3 lines beside `# card:`, as the card's hooks line asks; live line reads `harness 4 of 4 wired`
W-205 (stable first): fit -- live order BOOT, re-read, hooks, [checklist], now, main, old processes, worktrees, previous; the clock has minutes
class completeness: surface = an outside value -> a printed start line; walked: `last` (clipped), `open` (not, F1), `previous` ts (not, F1), snapshot name (not, F1), worktree path/branch (clipped), command head (clipped), git value of hooksPath (clipped), magnitude (64 cut), control chars (newline), encoding (lone surrogate), empty (open `none`, ok); second surface = a git call that fails: main_sync (says why, ok), tree_roots (marked, ok), worktrees_text (says why, ok), git_hooks_text (F2); pre_compact.py: only the mark line was touched, nothing printed from outside values there
DUPLICATION AND CONSISTENCY: F4 (`git worktree list --porcelain` run and parsed twice in one hook run); none other found: grepped `forge/**/*.py` case-insensitive for `worktree list`, `isprintable`, `\\u%04x`, `%dh|%dm|divmod`, `def (age|clip|cut|closed_tasks|open_tasks)` -- only session_start.py and journal.open_tasks hit (positive control: the same grep finds clip/age in session_start.py)
CODE QUALITY: F5 (harness_text 4 levels); every new function under 60 lines; unread result: `staged, _` in git_hooks_text drops the why (F2)
tests: fit_with_fixes -- expected values sourced from card B17 (c) (d) and W-205 (comment above the new rows); no duplicate row; budget fine (3.79 s for the new rows); gap F7; the cap row at test_hooks.py::test_session_start_crash_and_cap pins the unclipped open list (comment "the open list grows") and must be re-padded with F1
one road: fit -- the only new branch on a name is `os.name == "nt"` (process_list), the card's own "read per OS capability" door (B17 (d)); universality ratchet read from CI run 45989372922 (success), not re-run; no exclusion stays
VARIETY: blocker -- AR-27/AR-28 (part 9 "Frame invariants touched": every session-start fact prints `?` when not collected) broken by F2: an unknown tracked state is printed as `0 of 2 tracked executable (2 untracked)`; the commit names no AR-n (F8)
ratchets: no ratchet row added or raised (the diff touches no ratchet table)
probe: none -- no runner with `--root` exists in forge 2 (tool: none yet), and the tree is dirty (`git status --porcelain`: ` M forge/owner-words.yaml`, `?? logs/journal/90d4afc4-...jsonl`); defects shown instead by fixture runs and in-process calls of pure functions, no file of the repo edited

## Findings

F1 (blocks) session_start.py::open_text (open list), ::previous (ts), ::newest_snapshot (file name), ::emit and ::emitted (strict UTF-8). Card B17 (c) FH-4107: every printed line single-line, outside values cut to 64 with control characters escaped, written as UTF-8 with replacement. The diff clipped only `last:`. Concrete: a journal line `{"event":"dispatch","task":"a\nb: injected line",...}` -> the facts line ends `| open: a` and the next context line is `b: injected line` (a forged line in the Lead's start text). A task `"x\ud800"` -> `emitted()` raises inside `fit()`, the whole start text (BOOT, hooks, facts) is replaced by `reminder failed: 'utf-8' codec can't encode character '\ud800' ...`. The ts in `previous session: ... after <ts>` is journal.load's raw `ts` (journal.py::load, `last_ts = str(obj.get("ts", ""))`) -- same class. Fix: clip each id in open_text and the ts in previous and the snapshot name; one encoder `text.encode("utf-8", "replace")` used by both emitted() and emit() so the cap counts the bytes sent; one row with a newline id and a lone-surrogate id; re-pad the cap row with more ids instead of one long id.

F2 (blocks) session_start.py::git_hooks_text. `staged, _ = git_out(... "ls-files" ...)`: a failed or timed-out call, or one past the start budget, gives `modes = {}` and the line says every hook is untracked. Measured (git_out patched to fail only ls-files, this repo): `hooksPath ok, 0 of 2 tracked executable (2 untracked)`; control: `2 of 2 tracked executable`. AR-27/AR-28: unknown read as zero; the Lead is told to fix hooks that are fine. Also the rev-parse branch returns bare `?`, so past the budget the line reads `git: ?`, not the card's `? (not collected: start budget)` (measured: `hooks: harness 4 of 4 wired; git: ?`). Fix: ls-files None -> `<m> files, tracked ? (<why>)`; rev-parse None -> `? (<why>)`. Card edge "git missing or failing -> `hooks: ?`": the code keeps the harness half, which needs no git -- better, but a deviation; the card amendment is the Lead's call.

F3 (blocks) session_start.py::body sets `T0` after `_io.py::guard` has run `read_input(form)` (deadline 10 s). Card B17 (c): the budget is "measured from the hook's start" and the hook ends within budget + git_timeout + stdout deadline (40 s). Scenario: a harness that closes stdin at 9.9 s (FH-3029's class) -> the budget runs to about 40 s after that, and the last call can end near 45 s, past the card's bound and closer to the harness kill (60 s, `estimate`). Fix: take T0 in `run()` before `HIO.guard`.

F4 (blocks) session_start.py::tree_roots and ::worktrees_text each run `git worktree list --porcelain` and parse it their own way (startswith `worktree ` vs a block dict). One hook run spends two calls of the shared budget on one fact, and the two readers can disagree (one may fail past the budget while the other has read). Fix: one reader returning (blocks, why), called once in compose and passed to both.

F5 (blocks) session_start.py::harness_text, the try/for/for/if body: 4 nesting levels (over 3). Fix: flatten the commands into a list of (event, command) first, or put the per-command check in a helper.

F6 (does not block) session_start.py::git_hooks_text resolves a relative `core.hooksPath` against the main root. Git resolves it against the worktree's top level (githooks: hooks run in the root of the working tree). This repo's value is relative (`git config --get core.hooksPath` -> `forge/hooks/git`), so in a linked worktree the line says `ok` while git runs `<wt>/forge/hooks/git`; the card (FH-2030) wants the main checkout's. The file count also reads `root`, not main. It does not block because SessionStart runs in the main checkout (plan S6, the `rules` comment in compose). Fix: resolve against `rev-parse --show-toplevel`, compare to main's `forge/hooks/git`.

F7 (fix in this round, does not block alone) test_hooks.py: every K6 row patches `process_list`, so the Windows decode road (Console UTF8, strict decode, JSON) and its `?` exits have no row. The card's battery rows timeout, empty, not JSON, not UTF-8, exit not 0, all rows unreadable and 65536-char command are not written, and the commit has no `tests not written` line. Fix: one table over process_list with subprocess.run patched {b"", b"nope", b"\xff", returncode 1, TimeoutExpired, all rows unreadable}.

F8 (does not block) commit ffd8562 names no AR-n; the diff touches AR-27/AR-28 (part 9). Fix: the fix-round commit names them (a pushed commit is not amended).

## Seam and class notes
- Not in this diff (non-goals; noted only): (a) the fallback text (docstring and body still print `reminder failed: ...; read forge/BOOT.md by hand`, guard policy `"pass"`); (b) git steps; COORDINATOR printed whole and its 26624 cap; BOOT on resume; limits.json (the constants are hard-coded at the module head); the (e) sweep. The read-only `worktrees:` rows use `- <path> (<branch>) -- <state>`, not (e)'s `kept: ... -- removable (not swept: <source>)` form: to be reconciled when (e) lands. worktrees_text's `sent` set re-derives "dispatched at least once" beside journal.open_tasks; (e) says "CLOSED by journal.open_tasks": the (e) builder should take one road there.
- Card owns: session_start.py was to land as `session_start.py.next` placed by the Lead; it was committed directly (the recorded miss).
- head(): an unquoted Windows exe path with a space (`C:\Program Files\x.exe a`) keeps `Program Files\x.exe a` -- still readable, not a finding.

## Spot-checks
- Windows encoding of the process list: the real call (PS_NT, CREATE_NO_WINDOW) took 0.64 s, rc 0, 191297 bytes, first bytes `[{"ProcessId` (no BOM), json ok 363 rows; process_list -> 358 rows, 0 unreadable; this process's age 0.6 s (the `/Date(ms)/` reading is right); 11 ancestors excluded.
- from_tree positive control: 4 live processes from the tree are found (age 0); the live line `old processes: 0 started from this tree, older than 7200 s` agrees (none older).
- Live hook: startup 1.22 s, 4550 bytes; compact 1.18 s, 4802 bytes; under 6144, no cut today.
- 7200 strict (`>`), rows cap 5 then `and N more`, ancestors with the creation-time link, `parent gone` for absent and newer parent, the sibling-prefix lookahead, the linked-worktree root and the 60-char interpreter head: each traced in old_text/from_tree/head/ancestors and asserted by test_session_start_old_processes.
- K5: wired, not wired, broken, unparsed, no settings, not JSON, non-object hooks -> `?`; hooksPath unset/ok/wrong with 1 untracked: rows present and green.
- CI for ffd8562: main run 45989372922 success, branch run 45988668564 success.

## Trail
- Read: `git show ffd8562` (stat, three mark hunks, session_start.py removed lines, test diff); forge/hooks/session_start.py whole (497 lines); part 9 B17 (amends, Delivers (a)-(e), keys, edges, test); part 9 "Frame invariants touched"; forge/owner-words.yaml::W-205; forge/hooks/_io.py::guard; forge/tools/journal.py::files, ::load, ::open_tasks.
- `python -B -m pytest forge/tests/test_hooks.py -q -p no:cacheprovider -k session_start` -> `36 passed, 176 deselected in 56.01s` (control, green).
- Same file `-k <the 7 new tests> --durations=12` -> `13 passed, 199 deselected in 3.79s`, slowest `1.73s call test_session_start_worktrees`.
- `git config --get core.hooksPath` -> `forge/hooks/git`; `wc -c forge/BOOT.md forge/COORDINATOR.md` -> 3691, 49544.
- Live PowerShell process list (inline python) -> `secs 0.64 rc 0 bytes 191297 first b'[{"ProcessId'`, `json ok 363`.
- process_list/tree_roots/from_tree/ancestors in-process -> `rows 358 unreadable 0`, `roots 8`, `from tree: 4`, `me in list True ancestors 11`, `own age s 0.6`.
- Hook on startup/compact (stdin source JSON) -> 1.22 s/4550 B, 1.18 s/4802 B; output lines 41-53 as quoted above.
- Fixture roots in the scratchpad: r1 (task `a\nb: injected line`) -> `... | open: a` then `b: injected line`; r2 (task `x\ud800`) -> `reminder failed: 'utf-8' codec can't encode character '\ud800' in position 253: surrogates not allowed; read forge/BOOT.md by hand`.
- git_hooks_text with ls-files failing -> `hooksPath ok, 0 of 2 tracked executable (2 untracked)`; control -> `hooksPath ok, 2 of 2 tracked executable`; all git past budget -> `hooks: harness 4 of 4 wired; git: ?`.
- `gh run list --commit ffd8562...` -> both runs `completed success`.
- Greps: listed under DUPLICATION; `AR-\d+` over forge (part 9: AR-14, AR-27/AR-28, AR-20, AR-10).
