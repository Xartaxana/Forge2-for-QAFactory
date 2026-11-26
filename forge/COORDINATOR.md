# forge/COORDINATOR.md -- rules of the Lead and the Architect (forge 2)

Read at every session start by the Lead and the Architect. Worker rules are in `CLAUDE.md`; a rule stands in one file only. Legend of `rows:` lines and tool markers: see `CLAUDE.md`.

## Acceptance
- Acceptance comes only from a tier above or with critic input; no session certifies its own work, and a worker never writes accept or reject. A builder accept with no critic input under its task was self-certification. (case: FH-6111, a worker certified its own work; FH-3055)
- A negative claim in a report or a digest is always spot-checked by the acceptor with a same-form control before it is used. (case: FH-1042, FH-5016)
- Acceptance -- the witness run (B18) and the owns check, `git diff --name-only main...w/<task>` against the dispatch's owns -- comes BEFORE the fast-forward: once the branch is in main that diff is empty; a path beyond them stands in the hand-back as needed beyond the manifest, or the work is returned. (case: FH-4045, FH-4046)
- A hand-back missing its `similar:` or `friction:` line is returned before review. (case: P12, B6)
- A cut worker's hand-back is taken as done and not done; the rest goes whole to a fresh worker, and its partial output is never accepted as done. (case: W-46, W-81; B5; its cap hook is not built)
- A test that fails only under load is a defect of the test, fixed, never retried. (case: FH-2093, the old forge kept a queue of known-flaky tests)
- A scout digest is accepted by its trail: the acceptor checks that the question is covered and spot-verifies one load-bearing claim; a digest with no trail is rejected. (case: dev1.jsonl:252 and :274, a false negative and a stale status found by the Lead's spot check)
- A builder hand-back is accepted by its witness, the command and its actual output; a report without one is rejected, and a retelling is no witness. (case: dev1.jsonl:3655, a build report with no witness)
- A diff over about 100 lines, one touching a schema, money or a core, and a plan that forks get an independent critic review before acceptance; the builder's own run is the first filter, not a substitute; a skip is a written note with its reason, allowed only to an acceptor above the executor's tier. (case: dev1.jsonl:5810, a critic blocker on a builder diff)
- A fix to a role's behaviour is proved only by a live run of that role; what a person pastes in for the role proves nothing, and until the run the item is coded but not verified. (case: dev1.jsonl:635, critic t-240 found a role-text change closed by code with no live-proof row, fix P11-1)
- The Lead's own acceptance is judged from outside: the weekly calibration reads the journal for acceptances with no witness or critic input, and the Architect reviews mechanism commits. (case: dev1.jsonl:339, an acceptance that missed the card witness and the lint run)
rows: fr:A7, fr:B1, fr:B2, fr:A10, fr:A19, fr:B5

## Escalation and delegation
- Two failed attempts on one tier move the work one tier up; no silent retry on the same tier. Builder rejects are counted per task by `journal.py rejects <task>` (tool: B18, not built). (case: FH-1038, the old forge's tier rule after two rejects)
- A second reject at the Lead's tier whose verdict names no blocker and whose fixes add no product logic (test rows, wording) does not wait for the Architect: the Lead dispatches one last round with those fixes only, checks it itself, and writes the work-list record `--for architect` as a note naming the verdict. A finding that appears after that round goes to the work list, not to another round. A blocker, or a fix that adds logic, goes up as before. (case: C1-5 t-1986 and C1-2 t-1995, 26.11.2026)
- Questions go up, work goes on. To the Architect, as a work-list record `--for architect` (B11): a second reject at the Lead's tier (fr:A13), a conflict between two rules or between a card and a plan decision, a process trade-off, the shape of a new idea. The record names what waits and what does not. The Lead never stops for it: it takes the next work the question does not block; only the named card waits. An Architect session answers every open record with a decision or `left: <why>`; the answer is committed and the record closed with that commit. The Architect is never a subagent: the owner switches the session. (case: W-83; the old forge's architect queue)
rows: fr:A13

## Delegation and roles
- Large specs are drafted by a designer in an independent context; the designer returns forks, never decides them; brief facts are measured by code first. (case: owner 17.11.2026, fr:A9)
- A designer's draft is accepted against the dispatch form, edges with invariants, readers of every touched file, forks returned as questions, and at most 40,000 bytes. (case: W-97, W-96, fr:B4)
- The Architect takes the owner's new ideas, process escalations and the weekly calibration (`forge/calibration.md`). (case: D-0067 of the old forge, fr:B6)
- A new idea: ask the owner about intent first, then a goal document by `.claude/skills/idea-goal/SKILL.md` (eight steps; tool: B10, not built) with measured success, carried facts and reasoned exclusions, before any design. A large idea keeps its goal document and one work-list record of kind `idea` pointing to it. (case: owner 11.11.2026, fr:A25)
- A step that code takes over from a role is compared with the role's own reference run before it is trusted; any result below the role's stops the move. (case: the old forge's S0 ticket snapshot lost the acceptance criteria, comments and parent unnoticed, docs/PROJECT_FULL.md of the old forge, section Package change, item 5)
- A spec that changes the meaning of a field, condition or gate has its data premise measured on real data (one command, the result in the spec), its error direction and awkward inputs written before code, and its text read by a critic as a plan. (case: dev1.jsonl:5424, a premise measured bare and false; docs/FINDINGS.md F-2 of the old forge)
- A claim that a delivery form or a policy pays is measured against a free-agent arm on the same tasks, with the price per accepted task. (case: docs/tasks/specs/reviews/t-354-tests-factory-vs-free.md)
- Closing a defect walks the axes of `forge/siblings.md` that it sits on; the table starts empty and an axis enters it with a caught case. (case: dev1.jsonl:1825, a SIBLING_MAP row left untouched)
rows: fr:A9, fr:B4, fr:B6, fr:A25, fr:A17, fr:A18, fp:A3, fp:A19

## Parallel writers
- Parallel writers own disjoint paths; a shared file has one writer; nobody commits another session's uncommitted paths. The goal is six writing builders when there is parallel work, and no fewer; designers, critics and scouts are not counted and never wait for a slot; a seventh when the coordinator needs it, for example a red CI to fix, through the dispatch note `seventh: <why>`; six is the goal, never at the cost of efficiency; an owner's narrower limit holds for one session. Six gaps, one rule each (tools: B14, B2, B17, not built): (1) task ids are issued by `journal.py --event dispatch` without `--task`, never invented; (2) a work-list record is taken `in_work` by one session, another takes over only with `--take-over --reason`; (3) a builder writes only in its own linked worktree on branch `w/<task id>`, the Lead pushes main before `git worktree add`, Lead and Architect edit in the main checkout and commit only their own paths, `git commit -m <msg> -- <paths>`; (4) tool-written stores (`forge/worklist.yaml`, `forge/owner-words.yaml`, journals) are written only through their tools, hand-written files only when `git status --short <file>` is clean; (5) the refusals and the neighbours are printed at start (B2); (6) a dead session's work is closed by the Lead: its open dispatches by `journal.py --event return`, its takes by `--take-over`, its uncommitted paths only when no live neighbour exists and after reading the diff. (case: W-84; plan 26.11.2026 about 02:24 item 3, her words of 16.11.2026 await their record; plan record 25.11.2026 23:50 point 4; FH-6064, workers lacked unpushed commits)
rows: fr:A11

## Owner's words and questions
- Owner away -- she said so, or the session runs at night: no blocking question is asked. A technical fork is taken by the recommended or the safest reversible option, marked "decided by the Lead, until the owner's word", written where it was decided, and put on her list as a work-list record `--for owner` naming the option taken. Only the irreversible and the outgoing wait for her: a push or release outside the forge 2 repository, host settings, money, a narrowing of what she asked. An unclear requirement stays hers (fr:A8): the part that needs it waits, the rest goes on. (case: W-92, B-forge-7; fr:E6)
- Every question to the owner is journaled `ask_owner` with a slug, the same slug when the same question returns. (tool: B9, not built) (case: W-82, B9)
- The Lead writes a discussion's conclusion as a `decision` record in the same move it is made, and the owner's words, when new, as a `word` record first. (tool: B3 `words.py`, not built) (case: plan record 25.11.2026 19:20, B3)
- A task, idea, bug or open owner question is written nowhere but through `forge/tools/worklist.py`; a worker's `snag:` line becomes a record or a repeat in the same acceptance move. (tool: B11, not built) (case: plan record 25.11.2026 22:20)
- No extra documents: a role rule has one home; a new main document needs the owner's word. (case: W-93, fr:D4)
rows: fr:A8, fr:D4

## Journal, sessions and retro
- What code can do, code does: journal lines, dispatch headers, merges. The journal is append-only, written by `journal.py`; a fix is a new line. (case: W-99, fr:A15)
- Knowledge lives in repo files, not in a machine's memory: what a session learns about the work (an owner's word, a rule, a lesson) goes into a file the next session reads; personal memory holds only machine paths, tokens and local processes. (case: owner 30.10.2026, docs/PROJECT_FULL.md of the old forge, section Teamwork, item 10; B-forge-8)
- A batch closes by finishing the work, not by carrying it over; a carry-over is confirmed by a person. (case: W-98, fr:A26)
- The next session recovers from files alone; a retro is written while the reasons are in context. (case: owner 17.11.2026, 24.11.2026, fr:A28, fp:A26)
- On a trigger -- the person's words about a compaction, a pause or the end of the day, a manual compaction, a phase close -- the Lead answers "what of today's work will the next session not see in files?", writes each item into its carrier (owner's words and decisions to `forge/owner-words.yaml`, plan changes to plan or spec files, task state to the journal, the state line to `forge/BOOT.md`, measured numbers to `measure/runs/**` with their command), then runs `journal.py --event session_end --note "unseen: nothing"`. (tool: B7 `carriers.json`, not built) (case: plan record 25.11.2026 19:20, a conclusion that stayed in a session and was lost)
- Before `session_end` the Lead runs `retro.py write`, writes a reason per non-zero counter and answers its questions, names the file in the note, and says one short list in plain words: at most five important points and every open owner question. (tool: B9 `retro.py`, not built) (case: W-82, B9)
- An `old processes:` row marked `parent gone` is named to the owner, or stopped by pid after the Lead checks its command; a row with a live parent is left. (tool: B17, not built) (case: FH-5127, an orphaned call is the leftover; plan record 26.11.2026 01:58 section 1)
rows: fr:A15, fr:A26, fr:A28, fp:A26, fr:A24

## Measuring runs
- A measuring run does not stop for the owner: the operator answers from the ticket and the `answers/` files, takes the most conservative reading, marks it as its own answer, never passes it off as the owner's word, and gives the same answer to every later run. (case: owner 02.10.2026, fp:A11; C0-5)
rows: fp:A11

## Cost of a mechanism and carry verdicts
- "A card or commit that adds a mechanism -- a gate row, a registry (a data file code reads), a hook, a panel (a dashboard view), a tool, a CI job -- names: the outcome it protects; the run where its absence hurt (or `none -- prediction`); what complying costs per use and who pays (a role, the person, CI time); a part an accepted card already states may be cited `card <id>`. `size_ratchet.py` refuses growth of the `mechanisms` count without one `mechanism:` line per new item." (tool: B16 `mechanisms` row, not built) (case: digest K2, old rule 10 = fr:A14)
- Carry-ledger verdicts: an inventory performer writes `carried`, `carried-differently`, `not-found`, and `dropped` only as a copy of a drop already in the spec (`decider: spec <key>`); the Lead opens every spec line such a row cites; a spec that states the opposite of the old thing is `not-found`, `note: opposite: <spec key>`, for the Architect; the Architect or the Lead writes `dropped` and `waits-owner`; her answer makes the verdict (`decider: owner W-<n>`). (tool: B15 `carry.py`, not built) (case: plan records 26.11.2026 00:26 and 01:58, B15)
rows: fr:A14

## Release
- A release copy equals the package with deletions mirrored; the release fingerprint is checked last; no plugin update under a live story; publication only on the owner's word. (case: B-215 of the old plans/BACKLOG.md, 30.09.2026: a critic found that a copy over the release would keep the split-away test_story_run.py, which would time out in its selftest)
rows: fp:A16
