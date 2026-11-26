# t-1973 -- plan critic, forge 2 spec part 9, topic 1: cards B17 and B19

Reviewed state: forge 2 `980a437` (clean tree, `wc -c` part 9 = 68020). Frame: part 9 section 1, the owner's yardstick of the dispatch, plan records 26.11.2026 01:58 and 02:24 (fork decisions F190-F196 (a)). Plan gate: Q13 (a)-(e), Q4, Q6, Q12, VARIETY answered at the end.

- B17: blocker
- B19: blocker

Verdict: REJECT both as written (NEEDS WORK would do once F1, F2, F13, F15 are fixed; the rest are fixes). The decision to accept is the Lead's.

## Findings

**F1 (B17 + B19, blocker) -- one guard input contract that three of its users contradict.** B17 (a): `guard(body, policy)` treats "an unparsable or non-object payload, a payload with no session id, or stdin not closed by the deadline" as `not checked` -> exit 0 (warn) or refusal (refuse); edges: "empty stdin -> unknown, policy decides". Cases: (i) session start with empty or broken stdin -> guard prints one line and skips the body, so BOOT and COORDINATOR are not printed; accepted B2 edge says "`source` unknown or missing -> as `startup` (prints more, never less)"; (ii) git gives `pre-commit` no stdin (empty) -> policy `refuse` -> every commit refused; (iii) pre-push stdin is ref lines, not a JSON object -> every push refused; B19 reads it "through `_io.read_input`'s text form" -- B17 (a) defines only `read_input(deadline_s=10) -> (payload dict or None, note)`, no text form; and B19 edge "pre-push stdin empty -> passes" is the opposite of B17's empty -> refuse; (iv) `foreign_write.py` needs no session id, yet a payload lacking one is passed unchecked. Fix: `read_input(form=json|lines|none)`; the session-id cause only skips the `hook_failed` line; `session_start` with payload None runs its body as `startup` plus the not-checked line; pre-commit reads no stdin; pre-push `lines`: empty = nothing to push (pass), malformed lines per B19's edges; K1/K2 and the `deadline x policy` table follow the forms.

**F2 (B17, blocker) -- the session-start hook has no total time bound.** The sweep (`git worktree list`, per worktree a journal read, `merge-base`, `worktree remove`, `branch -d`) and the hooks-line git calls carry no timeout; only stdin (10 s), stdout (5 s) and the process list (5 s) do. The output is one final `write_output`, so a harness kill at its hook timeout (`estimate`) loses everything, the facts line, BOOT and COORDINATOR included -- against the card's "never cut" and B2's invariant "this hook never blocks or delays work". Case: six builders merged (the owner's tempo target), each worktree holding an ignored venv; at the next startup six removals of thousands of files run on Windows inside the hook. Fix: key `start_budget_s` in `limits.json` (AT/BEYOND rows); a timeout on every git call; the sweep runs last and starts no removal past the budget, printing `worktrees: <n> not swept -- start budget`.

**F3 (B17, fix) -- "folder gone" cannot be reached by the stated order.** Measured (git 2.56.0.windows.2, scratch repo): `git worktree remove <path>` on a worktree whose folder was deleted exits 0 and drops the registration. With steps (1)(2)(3) as written, a closed+merged worktree with its folder gone is `removed:`, so K7 "folder gone -> kept with the prune door" fails and small choice "a folder-gone worktree is never pruned by code" is broken by step (3). Fix: add step (0) "porcelain `prunable` -> kept `folder gone`" before (3), or accept git's removal (only a registration, task closed and merged) and drop the row and the small choice.

**F4 (B17, fix) -- ignored paths are deleted silently.** Measured: a worktree holding only an ignored file is removed, exit 0, and the folder is deleted with it (the trail's `estimate` is a fact). No edge, no K7 row. Case: the old plugin's `qa-factory/state/cost/` folder, which plan record 00:36 says C1-5 will add to the ignore list, written inside a worktree, is gone at the next start. Fix: edge + K7 row "closed+merged+ignored file -> removed, `(<n> ignored paths deleted)` on the row"; the residual is named.

**F5 (B17, fix) -- task state read once, removal later (FH-3109's lesson).** Session B's sweep reads t-5 as closed (rejected, clean, merged, no commits); session A writes `dispatch --task t-5` (next attempt, B14 rule 1) and its builder starts in that worktree; B's `git worktree remove` then succeeds (nothing uncommitted yet) and the folder vanishes under the builder. The card's edge assumes "the next attempt adds a new worktree", but B14 says no such thing. Fix: re-read the task's state right before step (3) for each worktree (FH-3109 carried); or hold the journal's OS lock across the re-read and step (3).

**F6 (B17, fix) -- "every other row of `tools/worktree_sweep.py` stays as its ledger says" does not hold.** FH-3091..3111 are dropped with the reason "B14 point 6 ... (no sweep tool)" (forge-hooks.3.md:102-122). That reason is now void, and B17 itself carries FH-3101 (two sweeps never at once -> the lock), FH-3105 (main checkout only), FH-3103 (local main chosen), FH-3099 (main never swept: only `w/<id>`), FH-3111 (named: full refname). Fix: the rows line re-judges FH-3090..3113, each with a reason. The salvage classes, reflog and 24 h rows stay dropped ("git speaks instead", 01:58). FH-3109 is carried per F5.

**F7 (B17, fix) -- the old-process line does not yet name what the owner would act on.** (a) The parent pid and creation times are read, but the line has no orphan mark (FH-5127: a call whose parent is gone is the leftover; one with a live parent may be a running 3-hour factory run of a live session); (b) no duty line says who reads `old processes:` and does what (B21 line 2 is about waits; B1's pointer is state-free), so the line can be printed at every start with nobody acting on it, and the processes pile up as before, only visibly; (c) `<command head 80>` conflicts with (c)'s FH-4107 rule "command heads ... cut to 64", and on Windows the head is the interpreter path (`C:\Users\<user>\Python312\python.exe` is about 60 characters), so the script name is cut off; (d) "holds the repository root" misses worker processes of linked worktrees outside the root (B14 rule 3 names no location: `git worktree add <dir>`), and it matches a sibling folder sharing the prefix (`...forge2-repo-old`). Fix: per row `parent gone | parent <pid>`; head = executable basename + arguments, one cut number; match the main root and every path of `git worktree list` followed by a separator or the end of the line; one COORDINATOR/B1 duty clause: the Lead names `parent gone` rows to the owner, or stops them by pid after checking.

**F8 (B17, fix) -- amends quote text already replaced.** B17 amends B14 rule 6 "its worktrees -> kept until the Lead checks ... (no sweep tool)" and B14 section 1 "Not here: ... the worktree sweep -> struck". t-1967 already replaced both: part5:161 "B14 rule 6's 'by hand (no sweep tool)' replaced by B17's session-start sweep", and part5:11 now reads "a light sweep returns in the sibling card B17". "Struck" would delete a correct pointer. Fix: drop both amends ("B14 r1 carries it").

**F9 (B17, fix) -- two fallback texts for one crash.** B2 edge: `reminder failed: <error>; read forge/BOOT.md by hand`. B17 guard: `<hook> not checked: <why>`, with no door, and B17 does not amend B2's edge. Fix: for `session_start` the guard line carries "read forge/BOOT.md and forge/COORDINATOR.md by hand"; amend B2's edge.

**F10 (B17, fix) -- the step runner's interface and the written order.** `run_steps(steps)` with `(name, argv, kind)` gives the steps neither the pre-push stdin lines nor the hook's argv (remote name, URL), which B8's remote step, B8's range scan and B19 all need. "A refuse step that ... times out" names no timeout. The written pre-push order leaves out C1-5's release step (`v*` tag or `release` branch needs `owner-word:`). Fix: steps receive the stdin text and the hook's argv; a per-step timeout (or "none" for `ci.py`); the order gets `release owner-word (C1-5)` before `ci.py`.

**F11 (B17, fix) -- the 64 MiB edge has no cap, so its test row depends on timing.** "Read until the deadline, then unknown" holds only when the writer is slow; a 64 MiB pipe can close inside the 0.2 s test deadline, so the expected value depends on throughput, and a fast 64 MiB payload is parsed whole. The old forge's "never from a TTY" (FH-4109, counted carried) is missing. Fix: key `stdin_max_bytes`, sized above a large Write payload, with AT -> read and BEYOND -> unknown, the policy deciding; a TTY stdin -> no read, payload None at once.

**F12 (B17, fix) -- `worktrees:` on `resume|clear|compact`.** The sweep runs on `startup` only. B14 block (6) prints `worktrees:` with "the sweep's reason" on every source, and what it prints when no sweep ran is unstated. Fix: on other sources, the same three conditions are evaluated read-only and printed `kept: ... (not swept: <source>)`.

**F13 (B19, blocker) -- the `local/` refusal reads names, not the content it protects.** Measured in forge 2: `refs/heads/local/pre-email-rewrite` (root `cb9d29e`, 16 commits), `refs/heads/local/pre-name-rewrite` (17), `refs/original/refs/heads/main` (17, filter-branch's backup of the same pre-rewrite history), `main` = `origin/main` (30, root `c19d2ff`). Measured pre-push stdin (scratch hook): a sha push arrives as `<sha> <sha> refs/heads/a 0000...`, and `refs/original/refs/heads/main` arrives under its own name. Neither falls under `refs/heads/local/`. So `git push origin refs/original/refs/heads/main:refs/heads/x` and `git push origin cb9d29e:refs/heads/main` pass both B19 rules and publish the history the 00:36 record cleaned of the outsider's name. That record says these branches "не отправляются". B8's Delivers still says "push `cb9d29e`", and B19's deps quotes it as the one allowed push. Fix: rule (1) also refuses when the commits a pushed sha would publish (`git rev-list <sha> --not --remotes=<remote>`) include one reachable from `refs/heads/local/*`, `refs/tags/local/*` or `refs/original/*` but not from `refs/heads/main`. Keep the name rule. B19 amends B8: the first-push step is done, and `cb9d29e` is now the root of `local/pre-email-rewrite`, so "no push but `cb9d29e`" is struck. The invariant holds: `main`'s commits are excluded.

**F14 (B19, fix) -- K3 expects exit 1; the real repository gives 128.** Measured: `git -C C:/QAFactory/forge2-repo merge-base --is-ancestor <root> main` for the three old roots -> `fatal: Not a valid commit name`, exit 128 each (the objects are absent). Controls: `c19d2ff` -> 0, `cb9d29e` -> 1. K3 only says what to do on 0. Fix: K3 = "`rev-parse --verify -q <id>^{commit}` empty, or is-ancestor exit 1; anything else -> stop and return". The count is measured: 3 roots (`9ac00f0`, `b1787e0`, `ad9901f`), not FH-1004's two.

**F15 (B19, blocker) -- "carried by pointer" to B14 for nine H9 rows that B14 does not carry.** B14 r1 (part5:72) names none of FH-6105, 6113-6117, 6122-6124. FH-6115 (an unmeasurable rollback passes visibly) is decided the other way in B14: status unreadable -> refused, so it is carried differently. FH-6116 and 6117 (look through `env, nohup, exec, nice, timeout, stdbuf, xargs, builtin, command, time`, up to 8 nested) are neither in B14's matcher nor in its named residual (script, alias, `sh -c`, `--git-dir/--work-tree`). Case: `timeout 60 git clean -fd` in a dirty main checkout; whether it is refused is unspecified, and a pass loses another session's untracked paths irreversibly. Fix: B19 amends B14 rule 3 with one clause: the ten heads are looked through up to 8; deeper -> judged as B14's error direction (refuse). The rows line: 6105/6113/6114 carried by B14 rule 3 (a)/(b); 6115 carried differently (refuses); 6122-6124 dropped (B14 parses no payload).

**F16 (B19, fix) -- push refusals are not told at entry.** B14 rule 5's fixed `refused here:` line, printed at every start, lists the main-checkout refusals but not B19's. Fix: B19 amends that line: "a push of a `local/` ref or local-only history, or of a history holding an old forge root".

**F17 (B19, fix) -- the door of rule (1) does not open.** "Push it under another name after review": `git push origin local/x:refs/heads/y` is still refused (the local ref is `refs/heads/local/x`), and with F13 any name carrying that history is refused. Fix: the door is "rebuild the reviewed commits on main without the local-only history (cherry-pick), then push that branch".

**F18 (B19, fix) -- FH-1070/1071 dropped with no reason, while forge 2 reads doors from commit messages for outward acts.** C1-5's release door (`owner-word: «<words>» <date>` in the tagged commit) and B8's other-remote door are such doors. B20 names its residual for raise lines (part9:90); B19 and C1-5 name none for the release door. Case: a tagged commit message quoting the rule in an indented block `    owner-word: «yes» 2026-11-26` opens a release. Fix: a reason plus the residual named in the rows line, or carry FH-1070 for `owner-word:` (line start, outside fence and quote).

**F19 (B19, fix) -- the shallow-clone edge's reason is false.** "A shallow clone missing the root object -> the default (not pushed)": later old-forge commits can sit above the shallow boundary with the root absent. The hook passes them, and only the server's own shallow refusal stands between them and the remote (`estimate`). Fix: `git rev-parse --is-shallow-repository` true -> refused `cannot judge: shallow clone`, or the residual named.

## Seam and class notes

- Joints that hold, read in their carriers: B14 rule 3 is the one home of the rollback refusal ("merged with B19's rollback half"); B14 rule 6 r1 and B17 (e) state the same three conditions; B14 rule 1 issues the id at `dispatch`, before the branch `w/<id>` can exist, so condition (1) protects a fresh worktree; `take_lock` is an OS lock freed when the process dies (journal.py:108-125); `open_tasks` returns `ok|unknown|incomplete` (journal.py:77-93); `snapshot.py` uses mode `x` and `timeout=60` (snapshot.py:27, 90); B2 + 20480 (F82 (a)) + 6144 = the 26624 cap.
- Rows arithmetic, checked: B17 114 = 64 + 50, per theme 24/24/20/17/14/8/7, every id listed once. B19 24 = 2 + 9 + 13.
- Class (Q4): F1 is one defect class, a shared helper's contract made for one user and applied to all; every user was walked (session_start, pre_compact/budget under warn, foreign_write, pre-push, pre-commit). F13's class: name-based outward guards. `refs/original/*` and sha pushes are its siblings, both inside B19.

## Plan-gate questions

- Q13 (a) EDGES: findings F2, F3, F4, F11, F12, F19.
- Q13 (b) MEANING: "closed" = dispatched and the last event closing, status `ok`; "from this tree" (F7 d); "not checked" (F1).
- Q13 (c) PREMISES: re-run K3 (F14) and `git worktree remove` semantics (F3, F4); the first did not reproduce.
- Q13 (d) READERS: no `owns_readers.py` block (part 9 section 6 says so, files unbuilt); not re-run, the Lead's step.
- Q13 (e) FORKS: F191, F192, F195, F196 (a) are consistent with their evidence. F195 (a)'s residual is widened, not reversed (F7 d).
- Q6 DUPLICATION: none found beyond F9 (two fallback texts) and F7 c (two cut numbers); one stdin reader is enforced by K10.
- Q12 ONE ROAD: none found. The Windows/`ps` split in (d) is per OS capability, one output; grepped the cards for "only", "not for", "except".
- VARIETY: n/a, forge-side cards (section 1).
- Owner's questions: worktrees no longer pile up for `w/<id>` branches once F2, F3 and F5 are fixed; harness `worktree-agent-*` and temporary pre-push worktrees stay listed as `state unknown` with the hand door (B14 rule 6). Old processes are visible but not yet actionable (F7).

## Spot-checks and trail

- The B17 and B19 cards and part 9 sections 1, 3 and 4 were read whole. Plan 3380-3528 (records 01:58, 02:07, 02:13, 02:24) and 3025-3061 (00:36). Themes H3, H4, H7, H9, H13, H17, H32, H34, H38. Ledger rows by id: FH-3090..3113, FH-5115..5131 with 1002/4054/4142, the H3 rows, the H9 and H38 rows, and the dropped H4/H13/H17/H32 rows. Part 5 B14 (67-81, 11, 161); part 4b B2 (62-71); part 4b-2 B8 (12-22); part 2 C1-4 and C1-5 (114-131); journal.py 40-130; snapshot.py (grep).
- `git -C C:/QAFactory/forge2-repo log --oneline -1` -> `980a437 specs: parts 5-9 after the fix rounds; ...`; `wc -c` part 9 -> 68020.
- `rev-list --max-parents=0`: forge-repo -> 3 roots; forge2 -> `cb9d29e`, `c19d2ff`; old roots in forge2 -> absent x3.
- Per-ref roots and counts: main 30/`c19d2ff`, origin/main 30, `local/pre-email-rewrite` 16/`cb9d29e`, `local/pre-name-rewrite` 17, `refs/original/refs/heads/main` 17; `forge/remote.json` absent; one worktree.
- Scratch `git worktree remove` (git 2.56.0.windows.2): gone -> exit 0; locked -> 128 "cannot remove a locked working tree"; untracked -> 128 "contains modified or untracked files"; ignored -> exit 0; clean -> exit 0.
- Scratch pre-push stdin dump: sha push, `refs/original` push, `local/x` push, `HEAD~1` push -- four lines, as quoted in F13.
- Searches with positive controls: Grep "prose position|in a fence" -i over the specs -> part9:90 (B20 residual) and theme H38. Grep `pytest|python -B` in forge/TESTING.md -> 0; control `python|test` -i -> 11 (not used as a finding).

```json
{
  "verdict": "blocker",
  "blockers": [
    "F1: B17 (a) guard input contract (JSON object + session id + empty=unknown) contradicts B2 edge (print as startup), pre-commit (no stdin), pre-push (text lines; B19 relies on an undefined read_input text form and on empty -> pass), foreign_write (no session id needed); fix: read_input forms json|lines|none, session_start prints on payload None",
    "F2: B17 session-start hook has no total time bound (sweep and hooks-line git calls untimed, one final write); a harness kill loses facts, BOOT and COORDINATOR; fix: start_budget_s key, git timeouts, sweep last and bounded",
    "F13: B19 local/ refusal is name-only; measured forge 2 refs/original/refs/heads/main and sha pushes (cb9d29e, B8's still-written first push) pass both rules and publish the pre-rewrite history; fix: refuse pushed commits reachable from local/* or refs/original/* but not main; strike B8's cb9d29e step",
    "F15: B19 rows carried by pointer to B14 rule 3 that B14 does not carry: FH-6115 decided the other way, FH-6116/6117 wrapper heads absent (timeout 60 git clean -fd unspecified); fix: one clause in B14 rule 3 via B19 amends, rows re-judged"
  ],
  "fixes": [
    "F3: B17 folder-gone row unreachable: git worktree remove on a missing folder exits 0 (measured); add a prunable check before step 3 or accept removal",
    "F4: B17 ignored paths deleted silently by worktree remove (measured); edge, K7 row, count on the removed row",
    "F5: B17 task state must be re-read right before step 3 (FH-3109)",
    "F6: B17 sweep ledger rows FH-3090..3113 keep a void reason and several are carried by B17; re-judge them",
    "F7: B17 old-process line: orphan mark, a duty line, one cut number with exe basename, match linked worktree roots with a separator",
    "F8: B17 amends of B14 rule 6 and section 1 quote text t-1967 already replaced; drop them",
    "F9: B17 guard line vs B2 reminder-failed line; keep the door to read BOOT and COORDINATOR by hand",
    "F10: B17 run_steps passes no stdin or hook argv, names no step timeout, omits C1-5 release step from the order",
    "F11: B17 64 MiB edge timing-dependent; stdin_max_bytes AT/BEYOND; TTY stdin not read",
    "F12: B17 worktrees rows on resume, clear, compact unstated",
    "F14: B19 K3 expects exit 1, measured 128 x3; restate K3; 3 roots measured",
    "F16: B19 push refusals absent from the start refusals line",
    "F17: B19 door of rule 1 does not open; name the rebuild door",
    "F18: B19 FH-1070/1071 dropped with no reason while owner-word doors exist; reason and residual or carry for owner-word",
    "F19: B19 shallow-clone edge reason false; refuse on shallow or name the residual"
  ],
  "class_completeness": "F1 walked every guard user (session_start, pre_compact, budget, foreign_write, pre-push, pre-commit); F13 walked name-based bypasses (sha push, refs/original, tag) inside B19; sweep ledger rows FH-3090..3113 walked for void reasons (F6); no sibling outside the two cards claimed",
  "trail": {
    "read": [
      "C:/QAFactory/forge2-repo/forge/specs/20261126-forge2-light-factory-spec-part9.md:1-47,65-76,125-183",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-plan.md:3025-3061,3380-3528",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part5.md:11,67-104,161",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4b.md:62-81",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part4b-2.md:12-22,54",
      "C:/QAFactory/forge2-repo/forge/specs/20261125-forge2-light-factory-spec-part2.md:114-131",
      "C:/QAFactory/forge2-repo/forge/specs/recon/carry/forge-hooks-themes.md H3,H4,H7,H9,H13,H17,H32,H34,H38",
      "C:/QAFactory/forge2-repo/forge/specs/recon/carry/forge-hooks.1..6.md rows by id",
      "C:/QAFactory/forge2-repo/forge/tools/journal.py:40-130",
      "C:/QAFactory/forge2-repo/forge/tools/snapshot.py grep"
    ],
    "reruns": [
      {"command": "git -C C:/QAFactory/forge2-repo log --oneline -1; wc -c part9", "result": "980a437 specs: parts 5-9 after the fix rounds; 68020"},
      {"command": "git -C C:/QAFactory/forge2-repo merge-base --is-ancestor <each of 3 old roots> main; controls c19d2ff, cb9d29e", "result": "fatal: Not a valid commit name, exit 128 x3; controls exit 0 and exit 1"},
      {"command": "rev-list --max-parents=0 and --count per ref in forge2", "result": "main 30 root c19d2ff = origin/main; local/pre-email-rewrite 16 root cb9d29e; local/pre-name-rewrite 17; refs/original/refs/heads/main 17"},
      {"command": "scratch repo: git worktree remove on gone, locked, untracked, ignored, clean worktrees (git 2.56.0.windows.2)", "result": "gone exit 0; locked exit 128; untracked exit 128; ignored exit 0; clean exit 0"},
      {"command": "scratch pre-push hook dumping stdin for sha, refs/original, local/x, HEAD~1 pushes", "result": "<sha> <sha> refs/heads/a 000; refs/original/refs/heads/main <sha> refs/heads/b 000; refs/heads/local/x <sha> refs/heads/c 000; HEAD~1 <sha> refs/heads/d 000"}
    ]
  },
  "mutants": [],
  "mutants_none": "plan gate: no diff and no worktree named, nothing to probe"
}
```
