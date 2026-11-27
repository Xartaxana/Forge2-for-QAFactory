# t-2109 critic verdict: wl-8 dispatch-line hook (W-210)

reviewed: `git -C C:/QAFactory/forge2-wt/t-2109 diff origin/main...8fb6883` (forge/hooks/dispatch_line.py, forge/tests/test_dispatch_line.py)

verdict: blocker
failure_class: spec (F1: the dispatch's edges put every "no line" outcome on stderr, a channel the Lead does not see) and capability (F2)
blocking findings: 2 (F1, F2)

forge/hooks/dispatch_line.py: blocker -- F1 (a missed line is invisible to the Lead), F2 (second role table)
forge/tests/test_dispatch_line.py: fit_with_fixes -- F5 (not blocking)
tests (Q5): fit_with_fixes -- one table of 5 edge rows plus a 2-case loop (F5); expected values come from the dispatch's edges and a real async launch result; no duplicate row; 6 passed in 1.44 s, inside the 10 s budget for a new file; no row for the `tool_name` filter, but that mutant is near-equivalent (a SendMessage payload has no description, so `plan` gives no line anyway), so no finding
one road (Q12): fit -- the hook reaches the journal only through `HIO.journal` -> `journal.py` (dispatch_line.py::body); no language, project or case branch
DUPLICATION AND CONSISTENCY: F2 (ROLES is a copy of forge/tools/dispatch.py:21); checked: the TASK, REVIEWED and AGENT_ID regexes, by grep `t-\\d|reviewed:|agentId|agent_id` over forge/tools and forge/hooks (positive control: the grep hits dispatch_line.py's own lines), with no second copy found; budget.py reads `agent_id`, the caller's id, which is a different field from the launch's `agentId`; the stdin reader, the guard and run_root are reused from _io.py, and the journal writer is reused
CODE QUALITY: F1 includes an unread result (`HIO.journal(...)` returns a bool that body discards); no function is over 60 lines or over 3 nesting levels; no dead branch (`payload is None` is guard's unreadable-input path)
VARIETY: blocker -- F1: on an unknown value (no role label, no t-id, a tool_response shape without agentId, a journal refusal) the line silently goes unwritten, as far as the Lead can see
architecture: AR-14 (one writer per store) is touched and respected: the journal is written only via journal.py; the commit does not name it (F4)
class completeness: walked the description parser axes (role label case, t-id position, `node:`, `reviewed:`) against all 35 real Agent descriptions, the agentId carrier axes (dict key, text, content blocks, a synchronous result), the tool-name axis (Agent, Task, SendMessage), and the output channel (stderr vs additionalContext) next to budget.py
probe: none -- forge 2 has no mutation runner with `--root` (tool: none yet); the control run was green

## Findings

F1 -- blocking, fix before merge -- forge/hooks/dispatch_line.py::body (and ::plan notes). Every "no line" outcome is one stderr line with exit 0, and a journal refusal is one stderr line from `HIO.journal`, whose `False` body never reads. Claude Code shows the stderr of a PostToolUse hook that exits 0 only in transcript mode, never to the model (from the harness docs: estimate, not verified in this harness). budget.py:449 emits its warnings as `hookSpecificOutput.additionalContext` on stdout for that reason, and this session proves that channel reaches the model ("PreToolUse:Bash hook additional context: caps ..."). Failure scenario: once the Lead switches to the hook (the COORDINATOR edit W-210 asks for), a launch described `critic re-review t-2105` (no colon), or a PostToolUse `tool_response` whose shape differs from the transcript's `toolUseResult` (unmeasured, see open point a), gives no line and no visible note. `journal.py open` then does not list the task, so the missed B17 dispatch line that the commit's `mechanism:` line cites happens again silently. COORDINATOR Journal's "a tool line saying a journal line was NOT written is repaired the same turn" cannot be followed, because the Lead never sees that line. Fix: in body, for each no-line note and when `HIO.journal(...)` returns False, print `{"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": "dispatch line NOT written: <why>; write it with journal.py"}}` on stdout (stderr may stay as well); add one table row asserting it (e.g. the `lead:` row and the no-agentId row check stdout).

F2 -- blocking (code quality / duplication, fix before merge) -- forge/hooks/dispatch_line.py::ROLES (line 23) re-implements forge/tools/dispatch.py:21 `ROLES = ("scout", "builder", "critic", "designer")`, the table dispatch.py checks headers against. Failure scenario: a role added to dispatch.py (for example a fifth worker role) gets checked headers and a budget row, but the hook drops each of its launches with `role ... is not one of builder|critic|designer|scout` (and per F1 nobody sees that). Fix: read ROLES from forge/tools/dispatch.py, loaded by path the way dispatch.py:37 loads budget.py. No extension of dispatch.py is needed.

F3 -- not blocking for this diff's code; a fix of this round in the Lead's lead-applies (executor: lead, failure_class spec) -- forge/hooks/dispatch_line.py::plan NODE/REVIEWED vs COORDINATOR Journal ("a `dispatch` note carries `node: <card or node id>` when it belongs to one") and Delegation (`reviewed:<sha>` the first token after the label). Of the 35 Agent descriptions in the Lead transcript 90d4afc4, 0 carry `node:`; the node is a bare token ("t-2101 wl-5 ..."). Of 16 critic descriptions, 8 carry `reviewed:`; for example "critic: re-review fix t-2105 B4 price 39538a8" has the sha bare. Every Lead-written dispatch line carries `node:`. My run on the real shape wrote `role:critic handle:a8f0...` for t-2105 with neither token. Fix: the COORDINATOR Delegation edit that goes with the settings entry must require `node: <id>` (and keep `reviewed:<sha>`) in the description. It must also say that a replacement of a dead worker still needs a Lead line naming the dead handle (the Journal repeat rule), because the hook cannot know that handle.

F4 -- not blocking -- commit 8fb6883 message: AR-14 (one writer per store) is touched and not named. Fix: the fix-round commit names `AR-14: journal written only through journal.py (HIO.journal)`.

F5 -- not blocking -- forge/tests/test_dispatch_line.py::test_no_session_and_bad_input (lines 44-47) loops two behaviours inside one test, so a failure of the first hides the second. Fix: make them two rows (fold them into the edge table with a session column, or parametrize).

F6 -- not blocking -- forge/hooks/dispatch_line.py::agent_id / AGENT_ID: the text fallback takes the first `agentId: <hex>` anywhere in the content. Input `{"status":"completed","agentId":"","content":[{"type":"text","text":"report quoting agentId: deadbeef of another"}]}` (a synchronous result whose report quotes an id) wrote `handle:deadbeef`, a wrong handle (this shape is constructed, not measured). Fix: anchor the pattern at a line start, `(?m)^agentId:\s*([0-9a-f]+)`, which is where the real launch text puts it ("...\nagentId: a8f0...").

## Seam and class notes

- The settings.json entry (PostToolUse, matcher `Agent|Task`) and the COORDINATOR "No hook writes a journal line" edit must land in one commit. Between them each launch gets two dispatch lines, the hook's and the Lead's. journal.states still holds (a repeat dispatch stays open), but retro.py counts `dispatch:critic` plus `dispatch:?` for one launch, and the second line reads as a repeat dispatch.
- Positive: the note form `role:<role> handle:<id>` is the one retro.py reads (retro.py:35 `ROLE`, :60 `ROLE.match(note)`), so hook lines are counted by role. The Lead's manual form "node: B4; builder; ..." counts as `dispatch:?`.
- session_start's harness line will show `dispatch_line.py@PostToolUse` not wired until the Lead registers it. That is visible and correct.
- Proposal, the Lead's call: the prompt header (`task:`, `role:` lines, checked by dispatch.py and read by budget.py) is a checked carrier of role and task. W-210 as approved names the description, so the hook follows the owner's word and this is no finding.

## Open points (as the dispatch asked)

a) Handle: the transcript has 31 of 31 `async_launched` toolUseResults with a non-empty `agentId` (transcript 90d4afc4, my script). Whether PostToolUse's `tool_response` equals `toolUseResult` is not measured: estimate, not verified. The key path is right if it does; if it does not, every line is missed, which is why F1 blocks. The first live launch after registration must be checked against the journal.
b) The first `t-\d+` rule: 34 of 34 role-labelled descriptions carry a t-id, and the first is the task in each, including "critic: reviewed:ef0bdec t-2101 ..." and "critic: re-review fix t-2105 ..." (my run wrote t-2101 and t-2105). The one unlabelled call ("Claude Code autocompact settings") correctly gets no line.
c) SendMessage: filtered by `tool_name`, no line, no note (my run). Synchronous Agent: see F6. Its line is also written only after the worker finished.
d) A repeat dispatch (critic entry, fix round) is legal under COORDINATOR Journal and is written every time. The note cannot tell an entry from a retry, and no rule asks it to.
e) `# card: wl-8`: no checker reads card ids (the only reader of the first lines is session_start's `hook:` mark). It is the first `wl-` value in a card line; whether work-list ids are legal card values is the Lead's call.

## Spot-checks

- Real-shape run (scratch root with journal.py copied, the hook unmodified): toolUseResult {isAsync, status, agentId, ...} gave one line `role:critic handle:a8f05955ffdf6c1da reviewed:ef0bdec` task t-2101. `Critic: t-9` (capitalised label) was accepted as critic. SendMessage gave no line and an empty stderr. A string response `agentId: abc` gave handle abc.
- Negative "no second role table": the grep `"designer"` over forge/hooks and forge/tools hit dispatch_line.py:23 (positive control) and dispatch.py:21.
- CRLF: the new files are LF, like budget.py and test_hooks.py (0 CR in each).

## Trail

- Read: the full diff; forge/hooks/_io.py; hio.py; forge/tools/journal.py; dispatch.py 1-37; retro.py 1-85; budget.py 3-22 and grep :449; COORDINATOR.md lines with dispatch, handle, `node:` and `reviewed:`; owner-words.yaml W-210; test_hooks.py 580-625; the builder's dispatch prompt and all Agent calls/results in transcript 90d4afc4.
- `git status --porcelain` (t-2109): empty. `python -B -m pytest forge/tests/test_dispatch_line.py -q -p no:cacheprovider`: `6 passed in 1.44s`.
- Count script over the transcript: `agent calls 35 labelled 34 with t-id 34 node: token 0 critic 16 critic with reviewed: 8 async results [31, 31]`.
- Scratch run journal tail (excerpt): `{"task": "t-2105", "event": "dispatch", "by": "lead", "note": "role:critic handle:a8f05955ffdf6c1da"}`, `{"task": "t-2109", ..., "note": "role:builder handle:deadbeef"}`.
