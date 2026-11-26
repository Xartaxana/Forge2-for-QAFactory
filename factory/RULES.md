# RULES.md -- rules for building the factory

Rules of the factory's craft, for whoever changes the factory (not for the factory's own roles). Restored from the old forge at sha b01363a15: the rules behind `docs/FACTORY_RULES_INDEX.md` (full text `ai-packages/qa-factory/design/factory-rules.md`, ids FR-n) and `docs/ARCHITECTURE_INDEX.md` (full text `ai-packages/qa-factory/design/architecture.md`, ids AR-n), grouped by the old headings; reasons and examples dropped. `P<n>` is a line of `forge/PRINCIPLES.md`. Old package tools do not exist here: a duty a tool would enforce ends `(tool: none yet)`. Each `carry:` line names the carry-ledger ids restored under its heading.

## Refusals and doors
- The door a refusal names is one the refused party can use: a role's refusal names a command in that role's own permitted set, the orchestrator's names an orchestrator operation; a refusal never names a path or tool the refused party cannot reach and never leaves it without a move; a test opens every door a refusal names (P15).
- A reason owned by the factory is reported to a person, in a section that says it is the factory's, and never put to them as a choice: nothing is asked of a person for the factory's own defects; every reason reaching a person carries an owner, and only `product`, `person` and `environment` reasons are phrased as decisions.
- A stage may not require, to close, an artifact nothing in the factory can produce: for each completion requirement some command builds it, and the refusal names that command and the words that pass it; an item that may be empty is declared in the factory's null-outcome table and walked by a test. (tool: none yet)
- The class of a refusal says whose fault it is: a malformed request (the call's fault) and a story that is not ready (the story's fault) are different answers on different routes; a block about recorded state raises the state class, a block about the request raises the request class.
- A ban is never bypassed and never a dead end: it holds regardless of state (no exemption because a file already exists or a step already ran) and is never passed by a workaround (a heredoc, a helper script, another tool); every ban names its door -- the command that does the legitimate version of the refused act, and the person's word, which the ban accepts and records (P13); where the role can judge, the door is the role's, not a question: an interrupted artifact is continued by default (keep the rows that parse, validate and were built on the same inputs, repair the stale ones, set the rest aside as `.superseded` only when nothing is usable); a role that cannot judge and has no door files a finding and asks, and neither stops silently nor works around; a person's "delete it and start again" still reaches a command that executes it.
- Whatever the work needs from outside is tried by every route before a person is asked -- for a read: the tracker's API in a light form, SSH or git for a repository, a browser where an API is closed; an LLM agent is never a read route (P5) -- and then the person gets three answers: not needed, here is how to get it, here it is as text; the refusal lists each route tried and why it failed; text a person pastes is a legitimate input for the story but never proves a fix to the route.
carry: FR-115, FR-116, FR-118, FR-119, FR-122, FR-255

## Text shown to a person
- Every text a person reads -- gate questions, boundary questions, a role's halt, a refusal the conductor relays, the report's factory-defects section, the closing question -- obeys the factory's one question form (P9): what the factory decided by itself, why the answer cannot be derived, exactly what is needed (one question), a closed set of answers, how to answer (at the bottom, the only place for a script name), and the price and consequences of each option; no filler stands where a question belongs, and code checks outgoing text for form-field names, plugin paths, dispatch ids and internal row ids in its body (a presence check). (tool: none yet)
- Everything a person decides at a gate has an executor, and the decision is kept whole: a gate is a decision before the last stage, not the last stage; list everything the decision can order and point at the step that performs each item.
- One packet shown to a person does not contradict itself: sections that could disagree are computed from one source and read the same field.
carry: FR-256, FR-257, FR-127

## Contracts between code and roles
- If a contract requires a field from a role, a command in that role's own permitted set must emit it; otherwise the field is not required.
- A detector never reads a person's or a role's wording by a phrase list: code triggers on a field, a state or the presence of words; what words mean is judged by the role that owns the subject, or by the conductor.
- A path a role needs is given to it -- in its known paths or in the dispatch's own lines -- never searched for.
- What the rules say a party may do, the guard permits: for each permission stated in a reference, a test exercises the guard on that exact path.
- For every state the other side can return, this side has a move or a refusal that names who acts: enumerate the other side's states from its own source and match each to a branch; a state the code has no move for goes through the one seam to the conductor (P22), and a site outside the seam is found by an audit. (tool: none yet)
carry: FR-128, FR-129, FR-258, FR-134, FR-135

## Identity and evidence
- Evidence of execution is not evidence of coverage: a green run says what was built, not what was promised; "covered" is never written where "ran and passed" is meant, and a field's name says which of the two it carries.
- Every state the factory can record has a sanctioned way out: a change that introduces a state names the command that reverses it.
carry: FR-140, FR-141

## Delivery and reporting
- Every blocking reason names its owner, and an unrecognised reason is a defect of the classifier: the default owner may not be `product`; a new reason family joins the owner vocabulary, not a list of exceptions, in the same change.
- The reason a delivery is not ready is stated in the task's own terms, first: the first blocking reason names a requirement, a behaviour or a user, not a receipt; the factory's bookkeeping goes in its own section below, marked as the factory's.
- A skip because the product lacks what a requirement demands blocks delivery; a skip by the factory's own decision does not; the two never share one word, and the blocking set holds the first; the third verdict `after_checks` (ready once the person finishes the checks left with them, P21) is never reached while a failure or a product gap stands, and a verdict kind the delivery-verdict table does not hold reads `no`.
- A discrepancy with a requirement has a road to a bug file under the story's `bugs/` even when no test can fail.
- Every step has a recordable completed state for the null outcome ("nothing goes out", "nothing to file", "no failures to triage" are results): the empty state is recorded, not escalated, and declared in the null-outcome table. (tool: none yet)
- A report never changes the meaning of a role's own verdict: each distinct source verdict maps to its own reported state (rejected, unverified and approved stay three words).
- A capability the run's standing decision forbids is neither probed nor advertised: the probe reads the standing decision first, and the packet says the channel is closed by the person's word instead of confirming it.
- Every path named in text a person or a role reads is the path the code writes, resolved through the factory's one path resolver, never written by hand. (tool: none yet)
- A comparison run leaves no trace in the project (P8): no merge request, no tracker comment or subtask; bugs go to a Markdown file or the chat; the run works on a copy; the experiment's external writes are closed and its record of outward writes is empty.
carry: FR-144, FR-145, FR-146, FR-147, FR-148, FR-149, FR-150, FR-151, FR-152

## Measurement and money
- A story's spend is the sessions its own journal names -- a record of what the factory launched -- not every session that mentions the ticket; a roll-up that cannot name its sessions says so instead of publishing a number (P18).
- When two records of the same quantity disagree, the report names the authoritative one, prints the gap and states the method behind each figure.
- A measurement is not a finding until the raw evidence is read: a count of refusals is not a count of defects, and the claim quotes an example from the raw record.
- A cache belongs to the run it measured and is keyed by that run; a report says out loud when it used one and names it.
- A measurer is code and gets a test like any other code: a measurement change ships with a case that fails without it.
- An unknown is never reported as a fact: a measure with no evidence says `unknown`, the reporting path has a distinct state for "no evidence", and the report prints that word.
- Work moved to a deterministic tool is judged by the LLM spend it removes; the tool's own cost is reported, not optimised; the change reports the LLM spend of the affected stage before and after (P6).
- Friction with the factory's own code is measured on every run, and code that makes a role's stage dearer than without it is a defect (P11): a turn is friction when our code returns a traceback, a hook refusal, an argument-shape error or a validator refusal of our own artifact, or when the role writes itself a helper script; the turn carries its full context cost; a change reports the affected role's code friction on a live run, before and after.
carry: FR-153, FR-154, FR-155, FR-156, FR-157, FR-158, FR-159, FR-259

## Writing factory code
- Code bearing escape sequences is never written through a heredoc -- use an editor tool, or build the escape from `chr(92)` -- and no factory file carries a control byte 0x07, 0x08, 0x0b or 0x0c; a regex is proved to match in a test. (tool: none yet)
- Every fix goes to the root cause, with a case that fails without it and a green selftest; never a bigger model, a retry or a wider timeout; extra critic iterations are a missing self-check.
- A red test against a requirement is a bug, not a blocker: a discrepancy is the goal of the work; never re-read the requirement until the test agrees with the product, and no change by itself turns a requirement discrepancy into a blocked or waived row.
- A process someone reads while it runs writes line-buffered: it is started with `-u` or flushes at every progress line.
- A validator writes nothing -- not into the request, and not onto a copy the projection rebuilds; what it must record goes to a durable record of its own; replaying the same request with the same idempotency key after the validator ran still succeeds and reads that record back.
- The factory's roles run on Sonnet or Terra, never on Haiku (P7); a fix that holds only on a stronger model is not a fix: role files bind no other model, and a quality regression is fixed in the role's instructions or the code, never in its model line.
carry: FR-161, FR-164, FR-166, FR-167, FR-169, FR-260

## Universality across projects
- Open variety is a role's judgment; code reports and leaves a move: code triggers on a field, a state or the presence of words and never decides meaning; on a project shape the factory does not know (a value of a variety axis that no table row, key or role step names) code never blocks and never takes a default branch silently -- it says what it could not establish and leaves the move to the owning role, or to the conductor's seam when no role owns the state (P22), and the gate never passes on such a shape; a refusal naming a door the receiving role can take is not a block; the role proceeds as a free agent on the same model would, asks the person only for what it cannot find, and the person gets only what the role cannot do (a physical device, a credential); a stage may cost more when that buys quality but never blocks; a default is silent unless it is declared in data and the run says it was taken; a safety refusal stays a refusal, and a person's word still passes any gate (P13); a changed script is run on one fixture shaped unlike the default and must report, not halt.
- Every config key has a default: what varies per project is a config key or a strategy-file section, and onboarding asks for it; a fact only a person's answer can give lives in the answer registry, read config first, registry second; every template key has `since` and `absent_means`; migration fills missing keys and never touches a person's value, so a project onboarded on an older version runs without re-onboarding; one commit carries the template row, the key row, the read with its default and the interview topic that asks it.
- Nothing the factory writes is tied to one machine or one layout: a stored or printed path is relative to the project root and resolved through the one path resolver; a stored path is a hint, never a fact; a project may sit in a subfolder of a git repository, and one project-marker walk finds it. (tool: none yet)
- Data is read by every route; an LLM agent is never a read route (P5): the ticket, links, comments, attachments and repositories are read by API, git, SSH or browser in a light form; an agent only writes, and only where the project writes that way; what the factory's own probe proves unreachable is a reported gap, not a question; a person is asked only for access they can give, with three answers; a new ticket field or source read by the API route is compared with an LLM run, and anything less than the LLM output stops the change.
carry: FR-261, FR-262, FR-177, FR-179

## One action, one way, everywhere
- A fact with a reader function is read only through it: every consumer calls the one reader, and a second parser of the same bytes is a defect even when it agrees today; before writing a reader, search for the same parsing shape with a positive control, and a new reader joins its axis row in the sibling map.
- Every text a person reads goes through one question form: it uses the story's words and asks one closed question, each option priced for the factory, the person and the story; code reads back only the offered tokens, and a free answer goes to the conductor (P22); a question asked again changes its text.
carry: FR-187, FR-190

## Continuity between stages
- Every field read has a producer; every field produced has a reader: whatever a script, role or phase reads (a field, config key, strategy paragraph, interview answer) has a producer the factory can run (an interview question, a permitted tool, a deriver); what is produced is read downstream or declared terminal; removing, renaming or rewording a producer removes or re-homes its readers in the same commit, found by a case-insensitive search of its name with a positive control.
- Every required list or field declares its empty outcome: exactly one home for "empty" -- a contract null outcome, a never-empty row with its guard, or a pending row that only shrinks; a null result is a recorded completed state, not an escalation; a new required field or list is declared in the commit that adds it, never born pending.
- Every recorded state has a way out, and every returned state a move: each recorded state has a command that reverses it and a row in the state-exits table, every state the other side can return has a move here or a refusal naming who acts, and stage run marks survive a second close.
- Requirements, not code and not AC, are the unit from S2 to delivery (P23): completeness is counted by the S2 register's requirements through the plan, the cases, the binding and the verdict; an expectation comes from a requirement, never from the implementation (P20), and an unconfirmed one stays `unresolved: expectation_unconfirmed` and is reported as a gap; text that counts completeness says "requirement", and a new expectation names its oracle.
- A finding, bug or gap reaches the report under its own owner: a discrepancy has a road to `bugs/` even when no test fails; every blocking reason names an owner; the factory's own reasons are reported, never asked; the verdict has three words and one reader, and an unknown kind reads `no`; "Left with you" lists every handed-over item and the regression scope (P21).
carry: FR-196, FR-197, FR-199, FR-200, FR-201
