- ci.py: blocker -- `matrix` hands a built row whose `{base}`/`{head}` token has no value to Actions as the raw command, so the edge "token with no value -> a failure on Actions" is not enforced and a tolerant tool goes green on an unknown (F1); a non-UTF-8 list exits 1 with a traceback instead of 2 (F2).
- ci-jobs.json: fit_with_fixes -- 13 rows, shape and states right, card ids verified; the `w1` command is empty although C3-2 names the invocation `rows.py walk` (F3).
- ci.yml: fit_with_fixes -- the job-level `if`, the heredoc and the all-green rule hold by reading; the matrix step carries the F1 road, the not-built line is formatted a second time (F4), and there is no `permissions:` block (F8).
- TESTING.md: fit_with_fixes -- every Delivers rule and B8's sentence present; the owner's word is legal only as a `W-` record before B3's registry exists, and rule 6 has no carrier in C1-6/B8 (F7).

Verdict: REJECT (failure_class: code) -- one blocking finding (F1), small fix; the rest fix before merge. The decision is the Lead's (rule 6).

## Findings

F1 (blocks) -- ci.py::matrix line 101 + ci.yml job `matrix`, step `bash -c "$JOB_COMMAND"`. `fill()` returns None when any token has no value, and `matrix` then falls back with `or r["command"]` to the UNFILLED command. On Actions nothing ever runs `run_all`, so the exit-3 / GITHUB_ACTIONS rule never applies. Probe (copy list, row `tok` = `echo range {base}..{head}`, built): `ci.py matrix --head abc` emits `"command": "echo range {base}..{head}"` (even `{head}`, which had a value, stays unfilled), and `bash -c "$JOB_COMMAND"` prints `range {base}..{head}`, exit 0 -> green. The same row under `GITHUB_ACTIONS=true ci.py --head abc` prints `FAIL tok (exit 3)`. So you get two roads for one action (Q12), and the Actions road lets an unknown through as a pass (FR-41). It triggers on every push whose `before` is all zeros (first push, every new branch) as soon as `secrets`, `worklist` or `rates` is built. C1-5 `secrets` comes next in order. Fix: the matrix job runs `python -B forge/tools/ci.py --only <id> --base "$BASE" --head "$HEAD"` and `matrix` stops filling tokens, so filling and the exit-3 rule live only in `run_all`. The frame already says "ci.yml runs `ci.py <job>` per entry" (spec.md:362). Minimal alternative: `matrix` drops the `or` fallback and gives such a row a command that exits 3 with `not judged: token {base} has no value`.

F2 (fix before merge) -- ci.py::load line 52-56 and ci.py::check line 113. `load` catches only OSError. A list with byte 0xff raises UnicodeDecodeError (a ValueError) outside `parse_rows`'s try. Probe: `ci.py --list bad.json` -> traceback, exit 1. The edge says malformed -> exit 2 naming the file, and exit 1 means "a job failed". `check`'s `git show ... text=True, encoding="utf-8"` fails the same way on a non-UTF-8 list at the base. The error direction is still red, which is why this does not block. Fix: catch UnicodeDecodeError in `load` and decode `shown.stdout` from bytes inside a `Refuse`.

F3 (fix before merge; answers deviation 3) -- ci-jobs.json row `w1`. C3-2 Delivers (part3.md:48) says "`rows.py`: ... `walk` = W1". C3-2 owns `factory/tools/rows.py` (part3.md:50), and the C3-3 table (part3.md:74) names `ci (rows.py walk)`. The dispatch's edge asks for the invocation verbatim where a card names one. Fix: `"command": "python -B factory/tools/rows.py walk"`, the same convention as the other rows. Yes to the builder's question.

F4 (fix before merge, Q6) -- ci.yml job `list`, heredoc line 41-42 duplicates ci.py::not_built_line line 70-72 (the `not built: %d (%s)` format). Two writers of one printed line will drift. Fix: `ci.py matrix` emits the formatted line (for example key `not_built_line`) and the heredoc only copies it. Better: `ci.py matrix --github-output` writes the three `key=value` lines and the heredoc goes away.

F5 (fix before merge) -- ci.py::parse_rows line 36-47:
- (a) `card` is never type-checked. Probe: `"card": 5` is accepted, exit 0.
- (b) a non-string `command` on a `not_built` row is refused with the message "is built but holds no command". The name lies. Probe: `command: 5`, not_built -> that text.
- (c) `id` has no character set. An id holding a newline reaches `$GITHUB_OUTPUT` through `nb_line` and can append a key (for example `count=0`) on a push with no base, where `check` is not judged. That GitHub takes the last value of a duplicate key is an estimate, not verified.

Fix: `card` a non-empty str, a message per cause, `id` restricted to `[a-z0-9_-]+`.

F6 (fix before merge, Q7) -- ci.py::check takes `list_path` and never reads it (dead parameter). Drop it.

F7 (fix before merge) -- TESTING.md:
- rule 4: "the owner's word (a `W-` record)". No `W-` registry exists until B3 lands, so today no owner's word is a legal source. The dispatch's edge says "no rule about a tool that does not exist stated as if it existed". Fix: "the owner's word, quoted with its carrier (a `W-` record once B3's registry exists)".
- rule 6 (red before the fix, the red run shown) has no carrier in the C1-6 Delivers line or in B8. Name its carrier or drop it.
- rule 9's first sentence restates rule 7's "not run" ("each rule once"). Merge them.

F8 (fix before merge) -- ci.yml, top level: no `permissions:` block, and `actions/checkout` persists the GITHUB_TOKEN into `.git/config`, where every job command can read it. Same-repo runs get the repository default, which was not measured here. Fix: `permissions: contents: read` at the top level, and `persist-credentials: false` on the checkout of job `matrix`.

F9 (spec residuals for the Lead, not the builder; propose a fork / node, the decision is the Lead's):
- (a) B8 says on Actions "the first push all history", but the builder's dispatch edge says "a token with no value -> a failure on Actions". With F1 fixed, every new-branch push turns red on `{base}` rows. The spec has to choose (for example a token `{range}` that fills to `<head>` alone when there is no base).
- (b) Deleting a BUILT row from ci-jobs.json passes `check` (only `not_built` growth is checked) and `all-green`. B8's invariant "no unjudged BUILT job is green on main" escapes by deletion. Proposed node: `check` also refuses a built id at the base that is absent at head.
- (c) Deviation 6 sends a force-push into a red `all-green`: the `before` commit is unreferenced, not fetched, so `rev-parse` fails and the list step exits 2. The next push clears it. This is the safe direction and I accept it as fit, but it is noise.
- (d) On `pull_request` the workflow file comes from the PR's merge commit, so a PR that edits ci.yml or ci.py decides its own `all-green`. The required check certifies nothing about CI-file diffs, so those diffs need the Lead's reading on the merge road (F86).

## Deviations
- (1) fit: full paths and `python -B`. These are the owning cards' Delivers paths; B11/B13 name exactly this form; a bare name would not run from the root.
- (2) fit.
- (3) F3.
- (4) fit as data; the yml's reformatting of it is F4.
- (5) F1.
- (6) fit, see F9c.
- (7) fit to the edge's words ("pinned to a version"). SHA pins are stronger but were not asked for.
- (8) fit: "data joint" = a data file read against its consumer, which matches the term.

## ci.yml on GitHub (by reading; estimate, not verified, no run possible here)
- Job-level `if: needs.list.outputs.count != '0'` on an empty matrix: holds. The output is the string `0`. The implicit `success()` also skips the job when `list` failed, so `fromJSON` of an empty include is never evaluated.
- Heredoc: holds. The YAML literal block strips the 10-space indent, so `EOF` and the Python lines land at column 0. `<<'EOF'` is quoted, so nothing expands. The default `bash -e -o pipefail` stops the step on `matrix` exit 2 and on `check` exit 1/2.
- all-green: holds for each case. `LIST_RESULT != success` -> red, and that also covers an empty COUNT. COUNT != 0 with `needs.matrix.result` failure, cancelled or skipped -> red. COUNT 0 with matrix skipped -> green with `nb_line`.
- First push, `before` all zeros: `case 0000000*` clears BASE, and `check` prints `no base`, exit 0. Today count is 0, so green. Token rows: F1 / F9a.
- Injection: `matrix.command` reaches bash through `env`, not through `${{ }}` in the script, so there is no expression injection; `name: ${{ matrix.id }}` is display only. The list is code by design. A fork's `pull_request` can run any command (as it can by editing ci.py or ci.yml). Its GITHUB_TOKEN is read-only and repository secrets are not passed. Same-repo runs: F8.

## ci.py edges
- Exit other than 0, 1, 3: FAIL (probe: exit 2 -> `FAIL e2 (exit 2)`).
- Exit 3: `not judged here` locally, FAIL with GITHUB_ACTIONS=true (probe).
- Cannot start: FAIL (probe on Windows cmd: exit 1; bash gives 127).
- Valid JSON of another shape: refused, exit 2 (object, non-dict row, wrong fields); `card` type: F5a.
- Duplicate id: refused.
- Base not a commit: exit 2 (probe `--base nosuchref`).
- Token with no value: locally right (probe `not judged here: tok`); Actions: F1.
- Job output not UTF-8: it is not captured, so it is not decoded. Holds.
- List not UTF-8: F2.
- List path with spaces: holds (probe ran `--list ".../dir with space/a.json"`).
- Empty array: `not built: 0`, exit 0 (spec silent; see F9b).
- No job id or command in ci.py or ci.yml: holds (key script K4; my reading).
- Over-building: only token filling in `matrix` (deviation 5, the source of F1).

## Standing questions
- Q1 fit to spec: F1 (error direction), F2, F3.
- Q2 own decisions: deviations above.
- Q3 seams: none (new files in an empty repository).
- Q4 class: F1's class is "a token rule on one road only". The other road, `check`, takes no tokens; no sibling.
- Q5 tests: card `test: none`, so nothing to cut. Behaviour probes on copies, below.
- Q6 duplication: F4. Grepped `not built` over the 4 files: ci.py:72 and ci.yml:42 (the positive control is the hit itself).
- Q7 code quality: F5b, F6; no function over 60 lines.
- Q8 hygiene: English, no Cyrillic (key script).
- Q9 ratchets: none in forge 2.
- Q10 architecture: not judged (forge 2 has no architecture map). VARIETY: n/a, forge tooling.
- Q11 judgment: none.
- Q12 one road: F1. Second road: `shell=True` is cmd.exe locally on Windows but bash on Actions. Today's commands are portable `python -B` calls, so it is a note, not a finding.

## not judged:
- GitHub behaviour beyond reading -- missing carrier: an Actions run URL (B8 K2/K5).
- First-time-contributor approval and the default GITHUB_TOKEN rights of the forge 2 repository -- missing carrier: `gh api repos/<owner>/<repo>/actions/permissions/workflow` (no GitHub call allowed).
- The duplicate-output-key semantics in F5c -- missing carrier: an Actions run.
- Commands of rows `pages`, `size`, `universality`, `lint`, `clone`, `crap` -- their cards name tools but no CI invocation that I found; the empty command is accepted as the edge's "else the empty string", with no carrier contradicting it.

## Trail
- Read: ci.py (1-146), ci-jobs.json, ci.yml (1-77), TESTING.md (1-25), part2.md:97-140 (C1-2, C1-3, C1-6), part4b-2.md:12-22 (B8), part3.md:34-74 (grep), part4b/4b-3/4b-4 row lines (grep), h_c16.txt.
- `git -C forge2-repo log --oneline -2` -> `143462c Phase 0, card C1-6...`. `show --stat` -> `4 files changed, 263 insertions(+)`. `status --porcelain` -> empty before and after the probes.
- Control: `python -B c16_check.py` -> `C1-6 check: all keys present`.
- Live: `python -B forge/tools/ci.py` -> `not built: 13 (tests, ..., rates)`, exit 0.
- Probes on copies in scratchpad/t1941 via `--list` (outputs quoted in F1, F2, F5 and the edges).

```json
{
  "verdict": "blocker",
  "blockers": ["F1: ci.py::matrix falls back to the unfilled command for a built row whose {base}/{head} has no value; on Actions bash runs it raw (probe: echo range {base}..{head} exits 0, green), so the edge 'token with no value -> failure on Actions' is not enforced; fix: matrix job runs ci.py --only <id> (one road through run_all) or matrix emits an exit-3 command for such a row"],
  "fixes": [
    "F2: ci.py::load and ci.py::check -- a non-UTF-8 list exits 1 with a traceback; catch UnicodeDecodeError and refuse with exit 2 naming the file",
    "F3: ci-jobs.json row w1 -- command python -B factory/tools/rows.py walk (C3-2 Delivers part3:48, C3-3 table part3:74)",
    "F4: ci.yml job list heredoc duplicates ci.py::not_built_line; matrix emits the formatted line (or writes GITHUB_OUTPUT itself)",
    "F5: ci.py::parse_rows -- check card type, one message per cause, restrict id to [a-z0-9_-]+",
    "F6: ci.py::check -- drop the unused list_path parameter",
    "F7: TESTING.md -- owner's word legal before B3 (W- record once the registry exists); carrier for rule 6 or drop it; merge rule 9's first sentence into rule 7",
    "F8: ci.yml -- permissions: contents: read at top level; persist-credentials: false on the matrix job checkout",
    "F9: spec residuals for the Lead -- (a) B8 first push all history vs the dispatch edge; (b) deleting a built row passes check and all-green; (c) force-push red until next push; (d) a PR editing CI files decides its own all-green"
  ],
  "class_completeness": "F1 class (token rule enforced on one road only): the only other consumer of tokens is run_all, which is right; check takes no tokens. SIBLING_MAP of the old forge has no forge 2 axis; no sibling outside the four files.",
  "trail": {
    "read": [
      "C:/QAFactory/forge2-repo/forge/tools/ci.py",
      "C:/QAFactory/forge2-repo/forge/ci-jobs.json",
      "C:/QAFactory/forge2-repo/.github/workflows/ci.yml",
      "C:/QAFactory/forge2-repo/forge/TESTING.md",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part2.md:97-140",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4b-2.md:12-22",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part3.md:34-74 (grep)",
      "scratchpad/h_c16.txt"
    ],
    "reruns": [
      {"command": "python -B scratchpad/c16_check.py", "result": "C1-6 check: all keys present"},
      {"command": "python -B forge/tools/ci.py", "result": "not built: 13 (tests, lint, clone, crap, size, universality, pages, w1, secrets, words, worklist, refs, rates); exit 0"},
      {"command": "python -B forge/tools/ci.py matrix --list <copy with built row tok = echo range {base}..{head}> --head abc", "result": "include carries command 'echo range {base}..{head}' unfilled; exit 0"},
      {"command": "bash -c 'echo range {base}..{head}'", "result": "range {base}..{head}; bash exit 0"},
      {"command": "GITHUB_ACTIONS=true python -B forge/tools/ci.py --list <copy> --head abc", "result": "FAIL e2 (exit 2), FAIL e3 (exit 3), FAIL nostart (exit 1), FAIL tok (exit 3); exit 1"},
      {"command": "python -B forge/tools/ci.py --list <copy with byte 0xff>", "result": "UnicodeDecodeError traceback; exit 1"},
      {"command": "python -B forge/tools/ci.py check --base nosuchref ; --base HEAD ; --base 83a36d2", "result": "cannot judge ... not a commit here exit 2; ok not_built did not grow exit 0; born ... exit 0"}
    ]
  },
  "mutants": [],
  "mutants_none": "no node worktree named for the runner and the card's test line is none (no narrow test file); behaviour probes ran on list copies via --list instead"
}
```
