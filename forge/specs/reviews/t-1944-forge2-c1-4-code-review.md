- journal.py: fit_with_fixes -- the closed list, note cap, task rule and ASCII session pattern hold, but a killed writer's partial line swallows the next whole line (F1) and the stale-lock takeover lets two writers in at once (F2).
- dispatch.py: fit_with_fixes -- the header is printed and checked as dispatched, but check reads header lines inside fences, lets a later repeat win, takes any non-NAMES key under owns: as a path, and refuses the R11-f backticked path with spaces (F4, F5, F6).
- trim.py: fit_with_fixes -- the at/over-N rule, the marker, the never-twice rule and the replaced-bytes marker hold; a `--keep` pattern ending in `$` misses on CRLF input (F8), and the whole input is held in memory several times over (F9).
- snapshot.py: fit_with_fixes -- sections, -2/-3 names, carriers print and git failure hold; any error while reading the journal crashes it and no snapshot is written, which breaks "it never refuses" (F10); the journal is read twice (F11).
- test_token_tools.py: fit_with_fixes -- 42 rows green in 5.25 s, within budget (134 of 395 non-blank lines), writes only under tmp_path; rows the cards name are missing (B7's `session_end`, "dispatch per missing key"), and three load-bearing branches have no row that kills them (F12-F14).

Verdict: NEEDS WORK (fit_with_fixes), 0 blocking findings, 14 fixes before merge. The decision to accept is the Lead's.

## Findings

F1. journal.py::write -- a writer killed mid-line breaks the next whole line. Input: `logs/journal/s.jsonl` ends in `{"ts": "2026-11-25T10:00:00Z", "task": "t-1", "ev` with no newline; then `journal.py --event dispatch --task t-2 --note n --session s` exits 0. Result: `read` gives `unparsable line 1 in s.jsonl` and exit 1, and `open` gives `incomplete` with no `t-2`. The whole `dispatch t-2` line is gone from every reader because it was appended onto the broken line. Fix: inside the lock, if the file is not empty and its last byte is not `\n`, write `\n` before the line, so the broken tail stays its own named unparsable line and the new line still parses.

F2. journal.py::take_lock -- taking over a stale lock is not atomic. Trace: writers A and B both fail `os.open(O_EXCL)` on a lock older than 60 s. Both run `getmtime` and see it as old. A runs `unlink` and `continue`, creates a new lock and starts appending. B's `os.unlink(path)` then deletes A's NEW lock. B creates its own lock and appends while A is still writing. Then A's `finally: os.unlink(lock)` deletes B's lock, so a third writer can come in too. The card says "a lock serialises writers", and this serialisation breaks on the stale path, which is exactly the edge the dispatch lists ("two writers both taking over a stale lock"). I traced this; I did not reproduce it, because it depends on timing. A related cost, measured: for up to 60 s after a writer is killed, every writer waits 10.1 s and then exits 1 `journal busy ... nothing written`. B9 says "a failed journal write never changes a verdict", so a hook's `cut`/`refuse` line from that window is lost without a trace. Fix: hold an OS lock on a persistent `logs/journal/.lock` (`msvcrt.locking` on Windows, `fcntl.flock` elsewhere, both stdlib). The OS releases it when the process dies, so there is no staleness to guess and no takeover race. Keep the 10 s wait and the busy exit.

F3. journal.py::open_tasks and journal.py::load -- a parsable but odd journal makes them crash instead of naming the line. Input: the line `{"ts": "x", "task": ["t"], "event": "dispatch"}` -> `open` gives a traceback, `TypeError: unhashable type: 'list'`, exit 1. Input: a folder named `logs/journal/x.jsonl` -> `open` gives a traceback, `PermissionError`, exit 1. Both are measured. Fix: a line whose `task` or `event` is not a string counts as unparsable (named with its number). A `.jsonl` path that cannot be opened is named the same way (`unreadable file <f>`) and makes the status `incomplete`, never a crash.

F4. dispatch.py::parse -- header lines inside a fenced block are read, and a repeated header overrides the earlier one. R11-f says header lines are "outside fences and quotes". Measured: a header with no `DoD:` line, followed by a fence holding ``DoD: `example` ``, gives `ok` exit 0. That is a false green on a missing key. A complete header followed by a fenced example `owns:` / `forge/x.py` gives exit 1 naming `forge/x.py` and the fence line itself. That is a false red. Fix: skip lines between fence markers (and `>`-quoted lines). On a repeated header name, either take the first one and report `repeated: <name>`, or refuse with exit 1.

F5. dispatch.py::parse -- every non-header line after `owns:` (or `given:`) is taken as a path until the next NAMES key. Keys outside NAMES (`feature:`, `designer:`, `facts:`, `manifest-skip:`, all of them real R11-f lines) are absorbed too. Measured: `owns:` / `<root>/a.py` / `feature: F19` gives `owns path not absolute or not inside the root: feature: F19`, exit 1. Fix: a line matching `^[A-Za-z][\w-]*:(\s|$)` that is not a drive path ends the path block.

F6. dispatch.py::check / inside -- an owns path with spaces written in the R11-f form (in backticks) is refused. Measured: ``owns:`` / `` `<root>/a b/c.py` `` gives `owns path not absolute or not inside the root`, exit 1, while the same path bare gives `ok`. `new` prints such a path bare, so `new` writes the non-R11-f form and `check` refuses the R11-f form. Fix: strip one pair of surrounding backticks before `inside()`, and have `new` wrap a path that holds a space in backticks.

F7. dispatch.py::main and dispatch.py::check -- error direction and dead code. (a) `check <missing file>` gives a FileNotFoundError traceback with exit 1. Exit 1 means "something missing", so a typo in the file name reads as a header defect. It should be exit 2 with `cannot read <file>`. (b) `new --role critic ... --test ""` prints `test: ` and exits 1 `missing: test`, although test is optional for a non-builder. Either do not print an empty test line for a non-builder, or do not flag it. (c) Lines 79-82: `elif not v and n != "caps" or (...)` followed by `elif n == "caps" and not v` gives the same `missing:` outcome through two branches. Fold them into one `not v` test (Q7, quality).

F8. trim.py::main -- input is split on `\n` only, so on CRLF output every line keeps a trailing `\r`, and a `--keep` pattern anchored with `$` never matches. Measured: 71 CRLF lines with `FAILED x` at line 41 and `--keep 'FAILED x$'` give `[trimmed 41 of 71 lines]` and the FAILED line is dropped. Without `$` it is kept (`[trimmed 40 of 71 lines]`). Windows tool output is CRLF. Fix: match the pattern against the line with one trailing `\r` removed (print the line as it was).

F9. trim.py::main -- `raw` (bytes), `text` (str) and `lines` (a list of str) all hold the whole input at once. For a log of G bytes that is about 3G or more of memory, plus about 50 bytes per line of object overhead. This is an estimate by reading; I did not measure it. The dispatch lists "memory on a very large input". Fix: read line by line (`sys.stdin.buffer` iteration), keep a `collections.deque(maxlen=n)` for the tail plus the kept lines, decode each line with `errors="replace"` and note whether any byte was replaced. Memory is then bounded by n plus the kept lines.

F10. snapshot.py::main -- the journal read is not guarded. Any exception in `journal.load` / `journal.open_tasks` ends the run before the file is written. Measured: a folder `logs/journal/x.jsonl` -> traceback `PermissionError`, exit 1, and `snapshots/` is never created. The task-list line of F3 -> traceback `TypeError`, exit 1, no snapshot. The dispatch says "it never refuses: it is called before a compaction". C1-5's hook fails open, so work goes on, but the snapshot the next session reads is lost. Fix: wrap each section's computation like `git()` does (`journal read failed: <error>` in that section) so the file is always written. F3's fix removes these two causes. The guard covers the rest of the class (permissions, an encoding crash).

F11. snapshot.py::main -- `journal.load(a.root)` is called, and then `journal.open_tasks(a.root)` reads every file again. `found` and `status` are assigned and never read (Q7: work whose result nobody reads). The open-files race also gets two windows instead of one. Fix: `open_tasks(root, loaded=None)` takes the result of `load`, and the snapshot passes it. Also: `os.path.exists` followed by `open(path, "w")` lets two snapshots started in the same second overwrite each other. Open with mode `"x"` and step to `-N` on `FileExistsError`.

F12. test_token_tools.py -- rows the cards name are missing. Q1 for the test file, Q5 (c). (a) B7's test line says "`session_end` accepted", and the journal table has no `session_end` row. (b) C1-4's test line says "dispatch per missing key", but only `owns` (via `new`), `DoD` and the role are exercised. There is no table that drops each of the 11 names from a full header and expects `missing: <name>`, and the builder-only rule for `test` has no check row. (c) An absolute owns path outside the root has no row; the only outside case is relative, which `isabs` already refuses. Fix: add `session_end` to the write table; add one table over NAMES that drops each line from a full builder header and expects `missing: <name>`; add a row with `<tmp_path>/../x.py`. Expected values come from C1-4's keys and R11-f, and the budget has room (134 of 395 lines).

F13. test_token_tools.py -- new behaviours reachable at a door have no row. Q5 (c). (a) The stale-lock takeover line and the busy exit 1 are a CLI output and an exit, and are the dispatch's lock edge. (b) The session pick: `FORGE_SESSION`, the newest file other than `git-hooks`, `s-<stamp>`. Hooks of later cards reach this through the environment. (c) `read` in ts order across two files, and `--last`. (d) A newline in a note stored escaped on one line. (e) The git status cut at 200 lines with its marker. For (a), an mtime set back 120 s through `os.utime` is cheap. A young lock costs 10 s and should not be written into this file. Fix: one row each, in the existing tables where the door is the same.

F14. test_token_tools.py -- killing power and expected values. Q5 (a), (b). These are by reading; I ran no probe (see the json block). The following mutants would survive the current file: `inside()` returning `True` after the `isabs` test (no absolute-outside row, F12 (c)); `SESSION_RE` widened to `[\w-]{1,128}`, which the dispatch names as a finding class (no non-ASCII row such as `sé`); the stale takeover branch removed (F13 (a)). Vacuous assertions: test_dispatch_new row `(None, "rel", 1, ["x.py"])` checks for `x.py`, which is in every printed header (the DoD is `python -B x.py`), so only the exit code tests it. Assert the `owns path not absolute` text instead. test_trim row `(1, ["--last", "0"], ..., "--last 0 must be")`: the last-line value is never checked when code is 2, and it does not match the real text (`--last must be at least 1, got 0`). Drop it or make it true. test_snapshot row 2 expects `o1.jsonl`, which appears only because of the builder's own `--untracked-files=all` choice. No card says the snapshot lists untracked files one by one, so the value comes from the code's own output (TESTING.md rule 4). Assert `t-2` and a `git status` section instead, or put the choice into the card first. test_snapshot row 1 expects `git failed` because tmp_path is not inside any git repository. That depends on the environment: it holds here (a non-repo temp), but it would fail under a temp directory inside a checkout. Pass `GIT_CEILING_DIRECTORIES=<tmp_path parent>` to the run.

Lower (no number, included in the fixes): journal.py::pick_session -- with no `--session` and no `FORGE_SESSION`, a writer joins the newest file, even one belonging to another live session. Measured: the line landed in `other-live.jsonl`. The dispatch prescribed this pick, but the residual is not named anywhere. Name it in the docstring: "without --session/FORGE_SESSION a line may land in another live session's file; hooks pass the session." A note starting with `-` (`-x`, `-v`) is refused by argparse (`expected one argument`, exit 2). The door `--note=-x` works (measured). Name that door in the docstring, because hooks journal free text.

## The builder's six decisions

1. The test: line printed only for a builder or when given: fit, except the `--test ""` case of F7 (b).
2. An empty given: accepted: fit. R11-f requires the line; whether the list is sufficient is the dispatcher's duty (rule 11), not code's.
3. caps: required by check, and an unknown role in a checked header exits 2: fit. B5 K5 says "every dispatch printed by dispatch.py carries role: and caps:", and exit 2 matches `new`'s unknown-role exit.
4. An unparsable line takes the previous good ts in the merged read: fit. It stays next to its neighbours, and an unparsable first line sorts to the start, where it is still named.
5. git status with --untracked-files=all: fit as code. In short format tracked changes print before the `??` lines, so the 200-line cap eats only untracked lines, and the 60 s timeout bounds the walk. The heading still says `git status --short`, and the test pins the choice from code output: F14.
6. open counts git-hooks.jsonl: fit. B9's git hooks journal `refuse` lines with an empty task, which `open_tasks` skips (`if not t: continue`), so they cannot open or close anything.

## Seam, class and standing questions

- Q1 fit to the spec: the closed list of 10 events is held once, in journal.py:19-20. A case-sensitive grep for `ask_owner|hook_failed` over the repo (specs excluded) finds only journal.py and the test, which uses the word as an expected value. Positive control: the same grep finds journal.py. K1-K5 are met (key script green). The card edge "two writers -> both lines land" is broken on the stale path (F2) and the killed-writer path (F1).
- Q2 builder's own decisions: above. Points the dispatch left silent, each judged: owns equal to the root is accepted (`inside` gives commonpath == root). That is in the repo, and R11-f does not forbid it: fit. Equal ts across files sorts by file name. Measured: `dispatch` in z.jsonl and `accept` in a.jsonl at the same second leave `t-1` open. The error is in the safe direction (a false open, never a hidden one): fit, noted. The same task dispatched again in a second file after an accept is open (measured): correct. A --root that does not exist is created on the first write (measured). That matches "journal absent -> created on first write": fit. Reserved names `NUL`, `CON`, `com1` as session ids write `NUL.jsonl` etc. on this Windows 11 machine, and those files read back (measured): fit here. Control characters and U+2028 in a note are stored on one line and read back as one line, because the read splits on `\n` only (measured): fit.
- Q3 seams: no file of another card changed. The key script prints `owns nothing changed outside the owned paths ([])`.
- Q4 class-wide completeness: the defect surface of F3/F10 is "journal content that parses but is not the expected shape, or a path that cannot be read". It covers both readers (`open_tasks`, `snapshot`). I walked the third reader: `read` prints raw lines and survives both inputs (traced: it does not index the object). The defect surface of F4-F6 is "the R11-f header grammar". I walked fences, repeats, foreign keys, the backtick form, drive case (ok, measured), `..` (refused, measured) and absolute outside (refused, measured). No sibling outside the owns: forge 2 has no other header reader (ci.py reads ci-jobs.json).
- Q5 tests: F12-F14. Volume: 134 test lines against 395 code lines (non-blank, `grep -c .`). Speed: 5.25 s. Writes: every run goes through `--root <tmp_path>`. One table per behaviour: yes (journal write, open/read, concurrent, dispatch new, dispatch check, trim, snapshot). No rewritten or deleted test (a new file).
- Q6 DUPLICATION AND CONSISTENCY: the root expression `dirname x3 of __file__` appears three times (journal.py:18, dispatch.py:18, ci.py:19; snapshot.py reuses `journal.ROOT`; trim reads no root). The dispatch prescribes "finds the repository root from its own location" per tool. It is one expression with no logic, and a shared module would make each tool edit `sys.path` as snapshot.py does. Not a finding. `--root` is one argparse line per tool, prescribed by the dispatch: not a finding. The event list is held once (Q1). `load` is reused by snapshot (no second reader): consistent. Searched: `grep -rn 'dirname(os.path.dirname(os.path.dirname' forge` gives 3.
- Q7 CODE QUALITY: no function over 60 lines or over 3 nesting levels (the longest is snapshot.main, lines 44-73). Findings: F7 (c) dead double branch, F11 unused `found`/`status` and the double read.
- Q8 hygiene: English and ASCII in the code, apart from the replacement character in a test row (`"b\ufffd"` written literally), which is a test fixture of the replaced-bytes edge.
- Q9 ratchets: none touched (forge 2 has no ratchet files yet).
- Q10 architecture / VARIETY: the forge tools are not factory code, and no AR-n of the package map applies. VARIETY: on an unknown value (no caps.json, no carriers.json, no journal) every tool prints a named state, never a silent default. That is measured by the key script's rows and the probes above.
- Q11 judgment: none moved into code. dispatch.py checks the presence and form of lines, not their content.
- Q12 ONE ROAD: none found. Searched the four tools for branches on a language, project or OS name (`grep -n -i -E 'win|nt|posix|platform' forge/tools/{journal,dispatch,trim,snapshot}.py`: none besides `os.path` calls). F2's fix adds an OS branch for the lock, one capability with two stdlib doors.
- Over-building: none. `read --session/--last`, trim's `--root` and the `-N` names are all in the dispatch.

## not judged

- The F2 race itself, reproduced: it needs timing control between two processes. Carrier missing: a deterministic hook into take_lock. Traced only.
- F9 memory, measured: no peak-memory tool on this machine (`resource` is POSIX; psutil not checked). It is an estimate by reading.
- Reserved device names on Windows 10, and the lock on POSIX: only this Windows 11 host was measured.
- The CI files and forge/TESTING.md as a rule text: another review, by the dispatch.

## Spot-checks

- Mechanical layer re-run as the control: `python -B .../c14_check.py` ends with `ok   owns nothing changed outside the owned paths ([])` and `C1-4 check: all keys present`. This matches the fact line of the dispatch.
- Tests re-run: `( cd C:/QAFactory/forge2-repo && python -m pytest forge/tests/test_token_tools.py -q -p no:cacheprovider )` gives `42 passed in 5.25s`.
- Commit and size: `git log --oneline -3` shows `5163fc9 Phase 0, card C1-4 ...` at HEAD. `show --stat` gives `6 files changed, 608 insertions(+)`, which matches the dispatch's fact. `git status --porcelain` is empty (clean tree).

## Trail

Read: spec-part2.md:114-121 (C1-4), spec-part4b.md:62-71 (B2), 107-115 (B5), spec-part4b-2.md:3-10 (B7), 24-33 (B9), h_c14.txt (whole), forge/TESTING.md (whole), journal.py, dispatch.py, trim.py, snapshot.py, test_token_tools.py (whole), logs/journal/.gitignore (`.lock`), ci.py (ROOT lines via grep), the schema tools/critic_verdict.schema.json.

The probes ran through `--root` on fresh folders `%TEMP%/c14probe-zvg2cvta` and `%TEMP%/c14probe2-*`, made by `tempfile.mkdtemp`; nothing was written in forge 2. Verbatim results, quoted in the findings: midline write 0, then read `(1, ['unparsable line 1 in s.jsonl'])`, open `(1, [..., 'incomplete'])`. Stale lock `journal lock older than 60 s taken over`, then exit 0. Young lock exit 1 `journal busy ... nothing written`, waited 10.1 s. Folder x.jsonl open/snapshot `PermissionError` traceback, snapshots dir False. Task list `TypeError: unhashable type: 'list'` in open and snapshot. Default pick wrote `other-live.jsonl`. dispatch: backticked spaces exit 1, bare spaces ok, lower drive ok, `..` exit 1, `C:/Windows/x.py` exit 1, owns = root ok, owns then `feature: F19` exit 1 naming it, no DoD plus fenced example `(0, ['ok'])`, fenced owns example exit 1, check of a missing file FileNotFoundError, critic `--test ''` `missing: test`. trim: CRLF `FAILED x$` gives `[trimmed 41 of 71 lines]` with the line absent; `FAILED x` gives `[trimmed 40 of 71 lines]` with the line kept; empty input `(0, [])`; keep also in tail gives `[trimmed 1 of 4 lines]`, b, c, b (never twice). snapshot: carriers row lacking a field gives `forge/carriers.json malformed: 'what goes there'` and the file is written; second and third gave `-2.md` and `-3.md`. Notes `-x` and `-v` give exit 2 `expected one argument`; `--note=-x` gives exit 0.

```json
{
  "verdict": "fit_with_fixes",
  "blockers": [],
  "class_completeness": "Surfaces walked: journal readers on parsable-but-odd content and unreadable paths (open_tasks, snapshot crash; read survives) -> F3+F10 together; the R11-f header grammar (fences, repeats, foreign keys, backticked paths, drive case, dot-dot, absolute outside) -> F4-F6; the lock (stale takeover, killed writer, young lock) -> F1, F2. No sibling outside the owns: forge 2 has no other header or journal reader.",
  "trail": {
    "read": [
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part2.md:114-121",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4b.md:62-71,107-115",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4b-2.md:3-33",
      "scratchpad/h_c14.txt",
      "C:/QAFactory/forge2-repo/forge/TESTING.md",
      "C:/QAFactory/forge2-repo/forge/tools/journal.py",
      "C:/QAFactory/forge2-repo/forge/tools/dispatch.py",
      "C:/QAFactory/forge2-repo/forge/tools/trim.py",
      "C:/QAFactory/forge2-repo/forge/tools/snapshot.py",
      "C:/QAFactory/forge2-repo/forge/tests/test_token_tools.py",
      "C:/QAFactory/forge2-repo/logs/journal/.gitignore"
    ],
    "reruns": [
      {"command": "python -B scratchpad/c14_check.py | tail -3", "result": "ok   owns nothing changed outside the owned paths ([]) / C1-4 check: all keys present"},
      {"command": "( cd C:/QAFactory/forge2-repo && python -m pytest forge/tests/test_token_tools.py -q -p no:cacheprovider )", "result": "42 passed in 5.25s"},
      {"command": "python -B - (edge probes through --root on tempfile.mkdtemp folders)", "result": "midline: read exit 1 unparsable line 1, open incomplete without t-2; folder x.jsonl: open and snapshot PermissionError, no snapshot; task list: TypeError in open and snapshot; fenced DoD example with no DoD: ok exit 0; owns then feature: F19 named as a path; backticked path with spaces refused; CRLF keep FAILED x$ dropped the line"},
      {"command": "git -C C:/QAFactory/forge2-repo show --stat --format= 5163fc992", "result": "6 files changed, 608 insertions(+)"}
    ]
  },
  "fixes": [
    "F1: journal.py::write -- newline before the line when the file does not end in one (a killed writer's tail must not swallow the next line).",
    "F2: journal.py::take_lock -- replace unlink-takeover with an OS lock (msvcrt.locking / fcntl.flock) on a persistent .lock; no stale guess, no double entry.",
    "F3: journal.py::open_tasks/load -- non-string task/event and an unopenable .jsonl named as unparsable/unreadable, status incomplete, never a traceback.",
    "F4: dispatch.py::parse -- skip fenced and quoted lines; a repeated header named, not silently overriding.",
    "F5: dispatch.py::parse -- any key-shaped line ends a given:/owns: path block.",
    "F6: dispatch.py::check/new -- accept backticked owns paths; new wraps a path with spaces in backticks.",
    "F7: dispatch.py -- unreadable check file exit 2; no empty test: line flagged for a non-builder; fold the double missing branch (lines 79-82).",
    "F8: trim.py::main -- match --keep against the line without its trailing CR.",
    "F9: trim.py::main -- stream with a bounded deque instead of holding the input three times.",
    "F10: snapshot.py::main -- guard each journal section so the snapshot is always written.",
    "F11: snapshot.py::main -- read the journal once (open_tasks takes load's result), drop unused found/status, open the snapshot with mode x.",
    "F12: test_token_tools.py -- rows for session_end (B7), each missing header key (C1-4 test line), absolute owns outside the root.",
    "F13: test_token_tools.py -- rows for stale-lock takeover, session pick, read order and --last, escaped newline, the 200-line status cut.",
    "F14: test_token_tools.py -- assert real texts in the rel and --last 0 rows, drop the o1.jsonl pin (code output), set GIT_CEILING_DIRECTORIES for the git-failed row; add a non-ASCII session row. Plus docstring residuals: session pick may join another live session; --note=-x door."
  ],
  "mutants": [],
  "mutants_none": "no probe: the dispatch forbids changing any file of forge 2 and a second critic runs its key script in the same working tree now, so a runner mutation there would be seen by it; forge 2 also holds no mutate_once.py; survivors are argued by reading in F14"
}
```
