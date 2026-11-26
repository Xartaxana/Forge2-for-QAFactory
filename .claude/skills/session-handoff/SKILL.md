---
name: session-handoff
description: Close-out check before a session ends -- every repo the session touched is committed and pushed, the journal is closed, accepted work stands in the committed HEAD, what only this chat knows is in its carrier, background processes are named, the retro is written, and the journal and retro are committed and pushed after `session_end` as the very last act. Use on a session-end trigger (forge/COORDINATOR.md, Journal, sessions and retro) or when the owner asks to check the handoff.
---

# session-handoff: checking a session's close-out

Goal: the next session recovers from the files alone, without this chat. The check is symmetric to boot: what the next
start reads, the close-out verifies. The outcome is a short report against points 1-6 (step 7).

## 1. Git, every repo the session touched

- In every repo this session touched (forge 2, its worktrees, and any other repo under the same deployment edited this session, not only this one) `git status --short` shows no path of this session left uncommitted: commit it now; another session's dirty paths are named in the report, not committed (forge/COORDINATOR.md, Parallel writers); in the measured project "A comparison run leaves no traces in the project" (forge/COORDINATOR.md, Measuring runs), so it gets no commit.
- `git log origin/main..main --oneline` is empty, otherwise push.
- Unfamiliar untracked files are never swept into a commit silently: find out what they are first.
carry: FS-138, FS-141

## 2. Journal closed

- `python -B forge/tools/journal.py open` lists no task of this session left without its accept or reject; a `return` alone is RESULT PENDING: the worker stopped and the acceptance is still owed. (tool: none yet -- journal.py open counts a return as closing)
- A session that ends below Lead rank (degradation or mid-tier mode, .claude/agents/critic.md) says so in its `session_end` note, the journal's last event: what was done below Lead rank and what waits for a Lead. (tool: none yet -- journal.py has no degradation event)
carry: FS-143

## 2a. Accepted work is in the committed HEAD

- For every builder `accept` of this session, the entity the witness names (a test, a function, a file, read from the accept note or the hand-back) exists in the COMMITTED HEAD of main (`git show HEAD:<path>` or a grep against HEAD), not merely in a working tree; checked BEFORE pushing.
- A divergence found is fixed the same evening: re-commit from the working tree if the diff still exists, or an honest journal line naming the original accept if it does not; never a silent re-run passed off as if nothing happened. (tool: none yet -- journal.py has no defect event)
carry: FS-145, FS-146

## 2b. Critic-trail candidates

- The handoff report lists the session's commits over 100 lines (by numstat) with no critic trail in the journal as CANDIDATES, not a verdict, and the window's count of small commits, the input to the cumulative critic-integration judgment (old R13-g); the listing only reads git and the journal. The candidates are read by the weekly reading of acceptances with no critic input (forge/COORDINATOR.md, Acceptance); the count has no reader in forge 2 yet. (tool: none yet -- the old informant tools/r3_integration_check.py has no forge 2 twin)
carry: FS-149

## 3. What only this chat knows

- The trigger question is answered: "is everything only I know now written down in a file?"; each item is in its carrier (forge/carriers.json), the state line of forge/BOOT.md is current. (partner: forge/COORDINATOR.md, Journal, sessions and retro, the "On a trigger" line)

## 4. Size and the boot chain

- `python -B forge/tools/size_ratchet.py` is green; a red row runs the boot-diet skill the same evening (it owns the reaction order; a rule line is never cut to fit without the owner's word).
- Every file forge/BOOT.md and the session-start print name still exists: a rename that does not update them breaks the next session's start. (tool: none yet -- the `refs` job, B13, not built)

## 5. Background processes

- A process tree of this session still running is stopped by pid after its command is checked, or named in the report with the reason it stays; a deliberate long run is started detached (old forge docs/RUNBOOK.md 9.8).
carry: FS-158

## 6. Retro

- A coordinator session runs the session-retro skill now, before step 7's commit and before any compaction if one is near. (partner: forge/COORDINATOR.md, Journal, sessions and retro, the "Before `session_end`" line)
- The report line is `retro: written <path>` or `retro: skipped -- <reason>` (a worker session, or a session of a few turns). (tool: none yet -- `retro.py missing` keeps a skipped session listed as missing)
- Under a `written` line the report prints in chat the session-retro step-4 list (the important points and the owner questions); a report with the path alone is a FAIL of this point.
carry: FS-161

## 7. Outcome and the last act

- Outcome: a short report against points 1-6 (OK or FAIL for each, and what was done).
- A FAIL is fixed BEFORE the session closes, never written down as "later".
- Then `journal.py --event session_end`, and after it the commit (`git commit -m <msg> -- <paths>`) and push of the session's journal file and retro file (logs/journal/*.jsonl and logs/retro/*.md are not git-ignored): that commit and push is the session's very last act.
carry: FS-163, FS-164, FS-165

## Detector

- A dirty tree or a divergence from origin at the next start means the previous session closed without this check; it is recorded as a finding, not silently absorbed. (forge/hooks/session_start.py prints `main: ahead/behind` and `previous session: no session_end after ...`; tool: none yet for the dirty tree)
