- journal.py: fit_with_fixes -- F1, F2, F3 and both docstring residuals are fixed as dispatched; the new OS lock is correct by reading and by probe (M1 killed), one fix: the lock is never explicitly unlocked before the descriptor closes (N3).
- dispatch.py: fit_with_fixes -- F4-F7 are fixed as dispatched; the fence skipper takes the dispatch's letter ("a line starting with") and so misses an indented fence, which gives a false green on a missing DoD (N1, a spec gap more than a builder slip).
- trim.py: fit_with_fixes -- F8 and F9 are fixed; the streamed output is byte-identical to round 1 on 33 probed inputs; a file argument that cannot be opened still ends in a traceback with exit 1 (N2, the sibling of F7 (a)).
- snapshot.py: fit -- F10 and F11 are fixed; three starters in the same second wrote `-2`, `-3` and the bare name, all with exit 0.
- test_token_tools.py: fit_with_fixes -- every row F12-F14 asked for is present and the three probes were killed; the file runs over the 10 s limit of forge/TESTING.md rule 5 (10.02-10.58 s in 4 runs, N5), and the new 200-line cut row pins the builder's `--untracked-files=all` choice, the same class F14 removed (N4).
- ci.py: fit_with_fixes -- R1, R2 and R3 are fixed (probed); `reconfigure` is called on a stream that may not have it (N6).

Verdict: NEEDS WORK (fit_with_fixes), 0 blocking findings, 6 fixes before merge (N1-N6). Accepting the work is the Lead's decision (rule 6).

## F1-F14 (t-1944) and R1-R3 (t-1943)

| id | state | place and evidence |
|---|---|---|
| F1 | fixed | journal.py::write: inside the lock, a non-empty file whose last byte is not `\n` gets `\n` first. Row test_journal_odd_files[files0]. Probe M3 (drop the newline) was killed by that row. A file ending in a bare CR still parses after a write (probe P5c: exit 0, `none`). |
| F2 | fixed | journal.py::take_lock: `msvcrt.locking(LK_NBLCK)` on byte 0 / `fcntl.flock(LOCK_EX\|LOCK_NB)`, the persistent `.lock` is never deleted, no mtime, no takeover; the 10 s wait and the busy text are kept. Row odd_files[files4] (a leftover lock file, write within 5 s). M1 (no lock taken) was killed by test_journal_concurrent_writers. Residual: N3. |
| F3 | fixed | journal.py::load: a non-dict line, or a task/event that is not a string, gives `unparsable line n in f`; an OSError on open gives `unreadable file f`; both make open/read exit 1 with no traceback. Rows odd_files[files1-3]. Probes: a BOM line and `"task": null` are both named `unparsable line 1` (P5, P5b). |
| F4 | fixed | dispatch.py::parse: fence toggle on lines starting with three backticks or three tildes, `>` lines skipped, `repeated: <name>` exit 1. Rows test_dispatch_check 188-192. Residual: N1. |
| F5 | fixed | dispatch.py `KEY` ends a path block. Row 193 (`feature: F19` after owns -> ok). Probes P7: `C:/...`, lowercase `c:/...` and `<root>/a:b.py` stay paths (ok); `https://x.org/a.py` stays a path line and is refused as not absolute (the safe direction). |
| F6 | fixed | dispatch.py::check strips one pair of backticks; ::new wraps a path that holds a space. Rows new "spaced" (161) and check 195. An unbalanced backtick is refused (P7, the safe direction). |
| F7 | fixed | (a) main: OSError -> `cannot read <file>` exit 2 (row 208); (b) new: `if a.test or role == builder` (rows 209-211); (c) one `not v` branch, lines 94-95. |
| F8 | fixed | trim.py: the match runs on the line with one trailing CR removed. Row 228 (CRLF, `FAILED x$` kept, `[trimmed 40 of 71 lines]`). |
| F9 | fixed | trim.py: a `deque(maxlen=N)` plus the kept list; the file argument is iterated too. Round-1 output is byte-identical on 11 inputs x 3 argument sets (P9: no difference). The residual "bounded by N plus the kept lines" is named in the code comment. Not named: a single line with no newline is still held whole. That held in round 1 as well, so it is not a finding. Residual of the same surface: N2. |
| F10 | fixed | snapshot.py: `guard()` on carriers, git status and branch; try/except around journal_text; the file is always written with exit 0. Row test_snapshot "odd" (a folder x.jsonl -> `unreadable file x.jsonl`, `incomplete`, one snapshot). |
| F11 | fixed | open_tasks(root, loaded); journal_text reads once; `found`/`status` are gone; mode `x` with `-N` stepping. Probe P4: three parallel starters -> `...Z.md`, `...Z-2.md`, `...Z-3.md`, exit codes [0, 0, 0]. |
| F12 | fixed | session_end row 49; a NAMES table drops each key (lines 196-197, 11 rows); absolute-outside rows 160 and 194. |
| F13 | fixed | (a) leftover-lock row, with no 10 s busy row (as the Lead decided); (b) session pick, 3 rows; (c) read order, `--last`, `--session`; (d) row 51; (e) row 248. Residual: N4. |
| F14 | fixed | rel row asserts the text (159); `--last 0` asserts the real text (231); o1.jsonl dropped (245 asserts `t-2`, `git status`); GIT_CEILING_DIRECTORIES (264); `s\u00e9` row (56). |
| residuals | fixed | journal.py docstring, lines 10-11, in the dispatch's words. |
| R1 | fixed | ci.py::main reconfigures stdout and stderr with `errors="backslashreplace"`. Probe: the id `caf\u00e9` on a cp1251 console -> `cannot judge: ... id 'caf\xe9' must match`, exit 2, no traceback. Residual: N6. |
| R2 | fixed | ci.py::main: `if a.head and not commit_of(a.head): raise Refuse`. Probes: `matrix --head $'abc\ncount=0' --github-output F` -> exit 2 and F stays 0 bytes; `check --head nosuch` -> exit 2; `--head HEAD` -> runs. |
| R3 | fixed | The module docstring lists `--only not a built id, --head or check's base not a commit`. |

## New findings

N1 (fix before merge) -- dispatch.py::parse. Surface: the R11-f header grammar, fence recognition. `ln.startswith(("```", "~~~"))` does not see an indented fence opener, and it toggles on any marker, so a fence opened with backticks is closed by tildes. Input: a full builder header with no `DoD:` line, followed by `"\n  ```\nDoD: `x`\n  ```\n"` -> `(0, 'ok')` (probe P1). That is a false green on a missing key, the very class F4 was opened for. Input: a header with no DoD, then a backtick fence closed by a tilde line, then `DoD: `x`` -> `(0, 'ok')` (P2c). Neighbouring classes walked: an unclosed fence -> every later line is unread -> `missing: ...` exit 1 (P2, false red, the safe direction); an unclosed fence after a full header -> ok (P2b, correct). The builder implemented the dispatch's own wording ("a line starting with three backticks or three tildes"), so the gap is in the spec. Fix: recognise a marker after leading whitespace (`ln.lstrip()`), and close a fence only with the character that opened it. Which wording goes into the card is the Lead's call.

N2 (fix before merge) -- trim.py::main. Surface: a file argument that cannot be read; the sibling of F7 (a) in the same owns. `trim.py NO-SUCH-FILE` -> FileNotFoundError traceback, exit 1 (probe P3). The docstring lists only exits 0 and 2. Fix: catch OSError -> `cannot read <file>`, exit 2, the same text and exit as dispatch.py.

N3 (fix before merge, low) -- journal.py::write / take_lock. The lock is released only by `os.close(fd)`; there is no `msvcrt.locking(fd, LK_UNLCK, 1)` first (grep -i `LK_UNLCK|LK_NBLCK` on journal.py: one hit, line 117, LK_NBLCK only). Microsoft's LockFileEx documentation says that a lock left at close is freed by the OS after a delay that "depends upon available system resources", and it recommends unlocking explicitly. The scenario: the next writer gets EACCES until the OS frees the lock. The 10 s retry absorbs that, so the cost is latency, and in the worst case a busy exit that loses a hook's line (B9). This is by reading; I did not reproduce the delay. The 8-writer test is green. Fix: in `finally`, on the msvcrt door, `os.lseek(fd, 0, 0); msvcrt.locking(fd, msvcrt.LK_UNLCK, 1)` before `os.close`. The fcntl door frees on close, so it needs nothing.

N4 (fix before merge) -- test_token_tools.py row 248 (`many`), Q5 (b). It creates 205 files under `f/` and expects `[cut: 200 of 205 lines shown]`. Plain `git status --short`, which is what the card names, lists them as one `?? f/` line. The expected value therefore comes from the builder's `--untracked-files=all` choice, the same reason F14 dropped `o1.jsonl`. Proof: probe M2 removed `--untracked-files=all` and this row was the one that failed (`killed`). Fix: create the 205 files at the top of tmp_path (`put(tmp_path, "%d.txt" % i, b"")`). Each top-level file is its own status line in both modes, so the expected value then follows from C1-4's 200-line rule alone.

N5 (fix before merge) -- test_token_tools.py, run time against forge/TESTING.md rule 5 ("A new test file runs in at most 10 seconds"). Measured on a copy of 6f8281811: 10.58 s, 10.02 s, 10.12 s, 10.31 s. The Lead measured 10.02 s. This is over the limit, not at it. The cheapest cut costs no row: test_journal_open_and_read rows 1-4 build their journal through 1-3 `journal.py` subprocesses each (0.24-0.47 s per row, `--durations`). Write those lines with `put()`, as test_journal_read_order already does, and keep one jw-built row for the write-then-open seam. The expected saving is about 1 s (an estimate from the durations, not verified). If rows must go instead, the weakest is test_journal_write `a/b` (the same slash class as `../evil`).

N6 (fix before merge, low) -- ci.py::main. `stream.reconfigure(...)` assumes a TextIOWrapper. In-process, with `sys.stdout = io.StringIO()`, `ci.main([...])` -> `AttributeError: '_io.StringIO' object has no attribute 'reconfigure'` (probe P8). The same happens under pythonw, where stdout is None. No caller in forge 2 does this today (grep `ci\.main|import ci|redirect_stdout|StringIO` over forge/ and .github/: no hit; case-insensitive; its one hit is the text `from ci` in forge/specs/reviews/t-1941-forge2-c1-6-code-review.md:36, which shows the search does find matches). The output of R1's fix is now a precondition of main, though, and the cost is one word. Fix: `r = getattr(stream, "reconfigure", None)` and call it only when present.

## The Lead's key and other edges, judged

- `open` prints the parsed open tasks before `incomplete`: fit. Exit 1 and `incomplete` as the last line are unchanged. The form matches snapshot's open-tasks section from round 1 (tasks plus an incomplete marker). It answers F1's measured complaint ("open gives incomplete with no t-2"). Problems print first, so the named line is not lost. It is not over-building.
- The lock wait loop: `os.open(O_CREAT|O_RDWR)` once, a 20 ms retry, close and None after 10 s, the busy text unchanged: as dispatched. A writer killed while holding the lock: the OS frees the lock at process death (the delay caveat is N3). The fcntl door (by reading): flock on the descriptor, freed on close or exit; correct.
- A file that vanishes between listing and opening: the OSError gives `unreadable file`, so the status is incomplete. That is a transient false incomplete, the safe direction (by reading).
- The key-shape rule: a drive path, a URL and a path with a colon after a slash are never read as keys (P7). An indented key-like line joins the path block and is refused as not absolute (false red, safe).
- Backtick stripping on given paths: given paths are never judged, so it does nothing there. Not a finding.
- The snapshot's guards: a section's error goes into that section; journal failures go into both journal sections; exit 0. The direction is right: the file always exists, and the failure is named in it.
- No over-building found: each change maps to a verdict line or a dispatch decision. The `open` output change is covered above.

## Standing questions

- Q1: every dispatch edge is met, except the fence letter, which is a spec gap (N1). Q2: the builder's own choices (open's output form; `status()` as a function name in snapshot) are safe.
- Q3 seams: `git diff --stat 5163fc992 6f8281811 -- forge/tools forge/tests` shows the four tools, the test file and ci.py. The ci.py lines belong to ddc33b8, which sits inside that range; 6f8281811 changes no ci.py line (`git diff --stat ddc33b8 6f8281811 -- forge/tools/ci.py`: empty).
- Q4 class: N1's surface (fences: indentation, mismatched closer, unclosed) walked; N2 is F7 (a)'s sibling; F3's surface (BOM, null task, non-dict, folder) walked.
- Q5: (a) three probes, all killed; (b) N4; (c) rows present for every F12/F13 door; (d) the rewritten rows rel, `--last 0` and snapshot row 2 are all as F14 asked; (e) no duplicates found within a door; (f) volume 231 test lines against 462 lines in the four tools (non-blank); (g) the run time is N5.
- Q6 duplication: none found. One loader serves read, open and the snapshot (snapshot passes `loaded`). Grepped `take_lock|msvcrt|fcntl` over forge/tools: only journal.py has them. Q7: no new function over 60 lines; no dead branch (F7 (c) folded).
- Q8: ASCII and English in code. Q9: no ratchets in forge 2. Q10: no architecture map in forge 2; VARIETY: every unknown value (BOM, odd line, unreadable path, a missing lock holder) gets a named state. Q11: none. Q12: the msvcrt/fcntl branch is one capability with two stdlib doors, as the verdict prescribed.

## Not judged

- The fcntl door run: no POSIX host here. Judged by reading only.
- The N3 delay itself: the carrier, a reproduction of a delayed OS unlock, is missing. Judged by reading against the LockFileEx documentation.
- The R1 retire-reason probe on a real commit message: I re-ran only the id probe, the same `print` surface.

## Trail

Read: t-1944 (whole), t-1943 (whole), h_c14_fix.txt (whole), forge/TESTING.md (whole), `git diff 5163fc992 6f8281811 -- forge/tools/journal.py forge/tools/dispatch.py forge/tools/trim.py forge/tools/snapshot.py`, `git diff 067f1bba3 ddc33b8 -- forge/tools/ci.py`, `git show 6f8281811:` of trim.py, snapshot.py, the test file (whole) and journal.py 125-215, ci.py 73-85 and 195-235 at ddc33b8. The forge 2 working tree was not touched (`git status --porcelain` shows only the Lead's two untracked recon files). Probes ran on a byte copy (`git archive 6f8281811 forge/tools forge/tests`) in scratchpad/t1947/tree, a fresh git repository, and on tempfile roots.

```json
{
  "verdict": "fit_with_fixes",
  "blockers": [],
  "fixes": [
    "N1: dispatch.py::parse -- an indented fence opener or a tilde closing a backtick fence is not seen: header with no DoD plus an indented fenced DoD gives ok exit 0 (false green); recognise markers after leading whitespace and close only with the opening character (the dispatch's own wording caused it; card wording is the Lead's call)",
    "N2: trim.py::main -- a file argument that cannot be opened gives a FileNotFoundError traceback exit 1; catch OSError, print cannot read <file>, exit 2 (sibling of F7 a)",
    "N3: journal.py::write -- unlock explicitly (lseek 0, msvcrt.locking LK_UNLCK 1) before os.close on the msvcrt door; LockFileEx frees a lock left at close only after a resource-dependent delay",
    "N4: test_token_tools.py row many (line 248) -- the 205 files under f/ make the expected cut depend on --untracked-files=all (probe M2 killed by this row); create them at the top of tmp_path",
    "N5: test_token_tools.py -- runs 10.02-10.58 s, over the 10 s limit of forge/TESTING.md rule 5; build the journal of test_journal_open_and_read rows 1-4 with put() instead of journal.py subprocesses",
    "N6: ci.py::main -- stream.reconfigure on a stream without it (StringIO, pythonw None) raises AttributeError; call it only when getattr finds it"
  ],
  "class_completeness": "F1-F14 and R1-R3 all fixed in place. Surfaces walked: header fences (indented, mismatched closer, unclosed before and after the header) -> N1; unreadable file argument across the tools (dispatch fixed by F7a, trim not) -> N2; journal content shapes (BOM, null task, non-dict, folder, bare CR tail) all named; the OS lock on both doors (fcntl by reading) -> N3; outside text printing in ci.py (R1) and its precondition -> N6; test expected values tied to builder choices (the F14 class) -> N4.",
  "trail": {
    "read": [
      "C:/QAFactory/forge-repo/docs/tasks/specs/reviews/t-1944-forge2-c1-4-code-review.md",
      "C:/QAFactory/forge-repo/docs/tasks/specs/reviews/t-1943-forge2-c1-6-re-review.md",
      "scratchpad/h_c14_fix.txt",
      "C:/QAFactory/forge2-repo/forge/TESTING.md",
      "git diff 5163fc992 6f8281811 -- forge/tools/journal.py forge/tools/dispatch.py forge/tools/trim.py forge/tools/snapshot.py",
      "git diff 067f1bba3 ddc33b8 -- forge/tools/ci.py",
      "git show 6f8281811:forge/tests/test_token_tools.py",
      "git show 6f8281811:forge/tools/trim.py, snapshot.py, journal.py 125-215",
      "git show ddc33b8:forge/tools/ci.py 73-85, 195-235"
    ],
    "reruns": [
      {"command": "( cd C:/QAFactory/forge2-repo && python -B scratchpad/c14_check.py | tail -3; python -B scratchpad/c16_check.py | tail -1 )", "result": "ok owns nothing changed outside the owned paths ([]) / C1-4 check: all keys present / C1-6 check: all keys present"},
      {"command": "( cd scratchpad/t1947/tree && python -m pytest forge/tests/test_token_tools.py -q -p no:cacheprovider ) x3, then once with --durations=12", "result": "83 passed in 10.58s; 83 passed in 10.02s; 83 passed in 10.12s; 83 passed in 10.31s"},
      {"command": "python -B mutate_once.py --root scratchpad/t1947/tree --id M1 --target forge/tools/journal.py --old msvcrt.locking(fd, msvcrt.LK_NBLCK, 1) --new pass --test forge/tests/test_token_tools.py --pytest", "result": "1 failed, 82 passed; FAILED test_journal_concurrent_writers; sha256 equal=True; outcome: killed"},
      {"command": "python -B mutate_once.py --root scratchpad/t1947/tree --id M2 --target forge/tools/snapshot.py --old status --short --untracked-files=all --new status --short --test forge/tests/test_token_tools.py --pytest", "result": "1 failed, 82 passed; FAILED test_snapshot[True-None-False-many-words4]; sha256 equal=True; outcome: killed"},
      {"command": "python -B mutate_once.py --root scratchpad/t1947/tree --id M3 --target forge/tools/journal.py --old lead = newline-if-missing --new lead = empty --test forge/tests/test_token_tools.py --pytest", "result": "1 failed, 82 passed; FAILED test_journal_odd_files[files0-True-1-words0]; sha256 equal=True; outcome: killed"},
      {"command": "python -B - (probe heredoc P1-P10 on the copy and tempfile roots)", "result": "P1 indented fence (0, ok); P2 unclosed fence missing all exit 1; P2c tilde closes backtick fence (0, ok); P3 trim missing file FileNotFoundError exit 1; P4 three snapshots [0,0,0] Z, Z-2, Z-3; P5/P5b BOM and null task unparsable line 1; P8 ci.main with StringIO AttributeError; P9 trim old vs new 33 runs no difference"},
      {"command": "ci.py matrix --head $'abc\\ncount=0' --github-output gh.txt; check --head HEAD; check --head nosuch; --list id.json (id cafe-acute)", "result": "exit 2 not a commit, gh.txt 0 bytes; no base exit 0; exit 2 not a commit; exit 2 id 'caf\\xe9' must match, no traceback"},
      {"command": "git -C C:/QAFactory/forge2-repo status --porcelain", "result": "only the Lead's two untracked forge/specs/recon files"}
    ]
  },
  "mutants": [
    {"place": "forge/tools/journal.py::take_lock (msvcrt door)", "change": "the lock call replaced by pass", "run": "python -B mutate_once.py --root scratchpad/t1947/tree --id M1 --target forge/tools/journal.py --old msvcrt.locking(fd, msvcrt.LK_NBLCK, 1) --new pass --test forge/tests/test_token_tools.py --pytest", "outcome": "killed", "killed_by": "test_journal_concurrent_writers"},
    {"place": "forge/tools/snapshot.py::status", "change": "--untracked-files=all dropped", "run": "python -B mutate_once.py --root scratchpad/t1947/tree --id M2 --target forge/tools/snapshot.py --old status --short --untracked-files=all --new status --short --test forge/tests/test_token_tools.py --pytest", "outcome": "killed", "killed_by": "test_snapshot[True-None-False-many-words4]", "remark": "N4"},
    {"place": "forge/tools/journal.py::write", "change": "the newline before a line after a broken tail dropped", "run": "python -B mutate_once.py --root scratchpad/t1947/tree --id M3 --target forge/tools/journal.py --old lead = newline-if-missing --new lead = empty --test forge/tests/test_token_tools.py --pytest", "outcome": "killed", "killed_by": "test_journal_odd_files[files0-True-1-words0]"}
  ]
}
```
