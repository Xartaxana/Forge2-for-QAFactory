- ci.py: fit_with_fixes -- every first-pass finding on this file is fixed and the Lead's new logic (base resolution, {range}, --only, the retire door, --github-output) behaves as the dispatch says on every probed edge; two fix-before-merge findings remain: outside text printed to a non-UTF-8 console crashes with a traceback (R1), and --head is never validated (R2).
- ci-jobs.json: fit -- w1 carries `python -B factory/tools/rows.py walk` (F3) and secrets takes `{range}` (F9a); nothing else changed.
- ci.yml: fit -- by reading (it cannot run here): one road through `ci.py --only`, the base, head and fallback reach the list job only, the matrix job reuses the list job's outputs, read-only token and no persisted credentials; GitHub behaviour beyond reading is not judged.
- TESTING.md: fit -- rule 4 makes the owner's word legal now, the old rule 6 is dropped, the old rule 9 is merged into the new rule 6; no other file cites the rule numbers.

Verdict: NEEDS WORK -- nothing blocks the merge; R1, R2 and R3 are fixes before merge. The decision is the Lead's (rule 6).

F1: fixed -- ci.py::matrix gives out ids only (`{"id": ...}`), ci.py::run_all takes `--only`, and ci.yml job `matrix` runs `python -B forge/tools/ci.py --only "$JOB_ID" --base "$BASE" --head "$HEAD"`; no `bash -c`. Probe: a `{base}` row with no base under GITHUB_ACTIONS=true -> `FAIL b (exit 3)`, exit 1.
F2: fixed -- ci.py::load catches UnicodeDecodeError (exit 2, file named, key F2), and ci.py::check decodes `git show` bytes inside a Refuse.
F3: fixed -- ci-jobs.json row w1.
F4: fixed -- ci.py::matrix `--github-output` appends include, count, nb_line, base and head; the heredoc is gone, and ci.yml formats no not-built line.
F5: fixed -- ci.py::parse_rows: ID_RE `[a-z0-9_-]+` (fullmatch), card a non-empty str, a separate message for a non-string command.
F6: fixed -- `check(rows, base, head)`; list_path dropped.
F7: fixed -- TESTING.md rule 4 wording as dispatched; rule 6 dropped; rule 9's first sentence merged into the new rule 6 ("its tool does not exist, so it is not run").
F8: fixed -- ci.yml top-level `permissions: contents: read`; `persist-credentials: false` on both checkouts; fetch-depth 0 stays.
F9a: fixed -- ci.py::fill `{range}` = base..head / head alone / no value; ci.py::resolve_base is the one resolution used by the run path, matrix and check; ci.yml passes before/PR base, the head sha and `origin/$DEFAULT_BRANCH` in the list job only.
F9b: fixed -- ci.py::check refuses a built row that is absent at head and names it; RETIRE_RE door prints `retired: <id> -- <reason>`; the refusal names the door. (The residual R4 belongs to the spec, not the builder.)
F9c: answered by the fallback (an unfetched `before` is not a commit -> merge-base with origin/<default>).
F9d: the Lead's, recorded in the plan (e397a6f); nothing to build.

## New findings

R1 (fix before merge) -- ci.py::main/check/parse_rows: outside text is printed to a console whose encoding cannot hold it. Surface: printing outside input (a commit message, a list's id, a path) to stdout. Windows here has stdout cp1251 (measured: `sys.stdout.encoding` -> cp1251).
- (a) The retire door. A commit message line `retire-job: b -- caf\u00e9` (valid UTF-8) makes `ci.py check --base <c1> --head HEAD` crash at `print("retired: ...")` with UnicodeEncodeError: exit 1 and a traceback. The expected result is `retired: b -- café`, exit 0. The same happens with an emoji. With PYTHONIOENCODING=utf-8 the same run gives exit 0, which proves the cause. Raw non-UTF-8 bytes (`caf\xe9`) crash the same way, because git re-encodes them.
- (b) Neighbour class, the same surface, in F5's new code: a list row with id `café` -> traceback, exit 1, where the edge says malformed -> exit 2 naming it (`%r` keeps printable non-ASCII).
On Actions (UTF-8 stdout) neither crashes. Locally the error direction is red, so nothing becomes a pass and this does not block. But a legitimate retire fails locally, before the push.
Fix, one place for the class: at the top of ci.py::main, `sys.stdout.reconfigure(errors="backslashreplace")` and the same for stderr.

R2 (fix before merge) -- ci.py::main / resolve_base: `--head` is never checked to be a commit, although the dispatch's edge asks about it (the builder's own noted analog).
- Probe: `matrix --github-output F --base <c1> --head $'abc\ncount=0'` writes `head=abc` followed by a second `count=0` line into F, a duplicate key.
- Probe: `--only r --base <c1> --head nosuch` runs the tool with the range `<c1>..nosuch`.
- `check --head nosuch` hides the git log failure, so a real retire line goes unseen. That direction is safe: it refuses.
On Actions the head is `github.sha` or the PR head sha, both GitHub-controlled hex, so the output injection is not reachable there (estimate by reading, not verified). The base cannot carry a newline, because it must pass `rev-parse --verify`. The note line `base: ...` goes to stderr under `matrix`, so the JSON on stdout stays whole (probe: stdout parses, the note is on stderr).
Fix: in main, a given `--head` that is not a commit is refused with exit 2 (`commit_of(head)` already exists).

R3 (fix before merge, Q7) -- ci.py module docstring. "2 cannot judge (list absent or malformed)" no longer covers every exit 2: `--only` with an id that is not a built row exits 2, and so does `check` with an invalid base and no fallback. Fix: "2 cannot judge (the list absent or malformed, --only not a built id, check's base not a commit)".

R4 (spec residual for the Lead, not the builder; a proposed node, the decision is the Lead's) -- F9b's invariant still escapes on direct pushes to main. Push 1 deletes a built row with no retire line, and check is red. Push 2 is any commit: its base is push 1's head, which already lacks the row, so `gone` is empty and the run is green. The `not_built`-growth rule has the same shape, which the first pass accepted. On the PR road the PR base keeps the comparison across the whole PR, so the hole needs a direct push to the default branch. Proposed: either branch protection forbids direct pushes to main (a rule of card C1-1, next to F9d), or check compares against the last green base. Related noise, the safe direction and per the Lead's invariant: a branch pushed with no new commits has merge-base == head, so it has no base, and every built `{base}` row is red on Actions.

## Edges walked (probes on copies in a temp git repository; outputs in the trail)
- Base resolution:
  - all zeros + fallback tag `v1` -> merge-base, note printed;
  - fallback remote branch `origin/main` -> merge-base;
  - empty base and no fallback -> `{range}` is the head alone;
  - a tree sha as base: run path -> `{base}` not judged here; check -> exit 2 `not a commit here`; check + unresolved fallback -> exit 2 (the safe reading of "no fallback"); check + fallback equal to head -> `no base`, exit 0;
  - fallback equal to the head -> no base: locally not judged here, on Actions FAIL exit 3;
  - unrelated history (orphan) -> no merge-base -> head alone;
  - a merge commit as head -> merge-base = the merged main tip, a non-empty range.
  All as dispatched.
- {range}: no head -> not judged here (on Actions red: key F9a no head).
- --only: a not_built id, an absent id, or an empty string -> exit 2 naming it. No not-built line under --only: fit, because all-green prints nb_line, so the line is not lost.
- check --head: fit, not over-building. The dispatch's retire range is base..head and the fallback's merge-base needs the head; ci.yml passes it in the list job.
- Retire door:
  - an indented line, a `> ` quoted line, an empty reason, two ids (`b r`) or an id `B` -> refused;
  - the line as the subject -> retired (fits "a line");
  - a merge in the range -> its commits are in `base..head` (literal fit);
  - a non-UTF-8 or non-cp1251 reason -> R1.
- --github-output: R2.
- First-round behaviour: still held. The Lead's key script covers the first-round keys and passes; the run path without --only still prints `not built: N`.

## ci.yml on GitHub (by reading; estimate, not verified)
- The list job's base/head outputs reach the matrix job: holds. Step `m` writes them through `--github-output "$GITHUB_OUTPUT"`, the job maps `steps.m.outputs.base/head`, and the matrix job `needs: list` and reads `needs.list.outputs.*`.
- origin/<default branch> after fetch-depth 0 with persist-credentials false: holds. With fetch-depth 0 the checkout fetches `refs/heads/*` into `refs/remotes/origin/*` during its own step; persist-credentials only governs the config left afterwards. `github.event.repository.default_branch` is in both the push and the pull_request payloads. If it is absent, the fallback does not resolve: a zeros base -> no base, and an unfetched base under check -> exit 2. Both are red or not judged, never a pass.
- `permissions: contents: read` is enough for actions/checkout: holds.
- pull_request head sha vs the checked-out merge commit: holds for ranges. head.sha and base.sha are parents of `refs/pull/N/merge`, so both are present, and `base..head` is the PR's commits. Tools that read the working tree see the merge commit, not head.sha; no row today compares `{head}`'s tree with the working tree.
- The first branch push after cb9d29e: holds. Either `before` = cb9d29e, an ancestor fetched with depth 0, or zeros with fallback merge-base cb9d29e; in both cases check prints `born` (cb9d29e holds no list) and exits 0, count is 0, and all-green is green.

## Standing questions
- Q1: F1-F9 fixed as dispatched; R2 is the one edge the dispatch named that is not handled.
- Q2: the builder's choices (no not-built line under --only, check --head, the note on stderr under matrix, check exit 2 with an unresolved fallback) are each in the safe direction.
- Q3: seams: only the four owned files in 067f1bb. e397a6f (the plan file) is the Lead's own commit, not the builder's.
- Q4: R1's class is printing outside text: walked over the retire line, the id refusal and the path refusal (the path one predates this round). The one-line fix covers the whole class.
- Q5 tests: `test: none` (the table lands with C1-5); the mechanical layer is the Lead's key script, re-run green.
- Q6 duplication: none found. `git(`/`commit_of` replace the two inline subprocess calls of the first round; grepped `rev-parse` and `subprocess.run` in ci.py: one site each, in `git()` and run_all.
- Q7: R3. No function over 60 lines (check is the longest at about 40); no dead branch found.
- Q8: English, LF/CRLF unchanged per file, no non-ASCII (measured).
- Q9: no ratchets in forge 2. Q10: not judged (no architecture map in forge 2). Q11: none.
- Q12 one road: holds. One road to run a job, and one base resolution called from three entry points.

## not judged:
- The actual run on GitHub (outputs, fetch, permissions, the merge-commit checkout) -- missing carrier: an Actions run URL after the first push.
- GitHub's squash-merge default message, and whether it keeps a `retire-job:` line at column 0 -- missing carrier: a squash merge on the forge 2 repository.
- The semantics of a duplicate `$GITHUB_OUTPUT` key (R2) -- missing carrier: an Actions run.

## Trail
- Read: t-1941 verdict (whole), h_c16_fix.txt (whole), ci.yml (whole), ci.py 104-148 and the whole fix diff (`git diff 143462c 067f1bba3 -- forge .github`), c16_check.py 50-184, critic_verdict.schema.json.
- `git log --oneline 143462c..067f1bba3 --stat` -> 067f1bb 4 files (ci.yml, TESTING.md, ci-jobs.json, ci.py); e397a6f plan file only.
- `git diff --stat 067f1bba3 HEAD -- the four files` -> empty (5163fc9 does not touch them). `git status --porcelain` -> empty before and after.
- Control: `( cd forge2-repo && python -B c16_check.py )` -> `C1-6 check: all keys present`.
- Probes: scratchpad/t1943/probe.py and probe2.py (temp git repositories, copies of ci.py; outputs quoted above); the id probe `ci.py --list scratchpad/t1943/id.json` -> UnicodeEncodeError, exit 1.

```json
{
  "verdict": "fit_with_fixes",
  "blockers": [],
  "fixes": [
    "R1: ci.py::main -- outside text printed to a non-UTF-8 console crashes (retire reason 'café' -> UnicodeEncodeError exit 1 instead of retired exit 0; id 'café' -> traceback exit 1 instead of exit 2); fix: sys.stdout/sys.stderr.reconfigure(errors='backslashreplace') at the top of main",
    "R2: ci.py::main -- --head never validated: --head with a newline adds a duplicate count key to GITHUB_OUTPUT, --head nosuch fills a bogus range; fix: refuse a given --head that is not a commit with exit 2 (commit_of exists)",
    "R3: ci.py module docstring -- exit 2 list omits --only with a non-built id and check with a base that is not a commit",
    "R4: spec residual for the Lead -- a deleted built row (and not_built growth) goes green on the next direct push to main; propose branch protection rule in C1-1 or a last-green base"
  ],
  "class_completeness": "R1 class (printing outside text to stdout): the retire line, the id refusal and the path refusal walked; one reconfigure in main covers all. F1 class (token rule on one road): matrix now gives ids only, so run_all is the single filler on both roads. Base resolution: one function, three callers (run path, matrix, check).",
  "trail": {
    "read": [
      "C:/QAFactory/forge-repo/docs/tasks/specs/reviews/t-1941-forge2-c1-6-code-review.md",
      "scratchpad/h_c16_fix.txt",
      "C:/QAFactory/forge2-repo/.github/workflows/ci.yml",
      "C:/QAFactory/forge2-repo/forge/tools/ci.py (104-148 and the fix diff)",
      "git diff 143462c 067f1bba3 -- forge .github",
      "scratchpad/c16_check.py:50-184",
      "C:/QAFactory/forge-repo/tools/critic_verdict.schema.json"
    ],
    "reruns": [
      {"command": "( cd C:/QAFactory/forge2-repo && python -B scratchpad/c16_check.py )", "result": "C1-6 check: all keys present"},
      {"command": "python -B scratchpad/t1943/probe.py", "result": "base resolution, range, --only, retire edges as dispatched; head 'abc\\ncount=0' -> GITHUB_OUTPUT gets head=abc and a duplicate count=0; retire reason with byte e9 -> UnicodeEncodeError traceback exit 1"},
      {"command": "python -B scratchpad/t1943/probe2.py (PYTHONIOENCODING unset vs utf-8)", "result": "reason café / emoji: exit 1 UnicodeEncodeError unset; exit 0 ok with utf-8"},
      {"command": "python -B forge/tools/ci.py --list scratchpad/t1943/id.json (id café)", "result": "UnicodeEncodeError traceback; exit 1"},
      {"command": "git -C forge2-repo status --porcelain", "result": "empty"}
    ]
  },
  "mutants": [],
  "mutants_none": "no node worktree named for the runner (the forge 2 working tree is shared with another critic and its files may not change), and the card's test line is none, so there is no narrow test file; behaviour probes ran on copies in temp git repositories instead"
}
```
