# CLAUDE.md -- forge 2 worker rules

Read by every worker at entry. Role files in `.claude/agents/` only point to a section here; the Lead's rules are in `forge/COORDINATOR.md`. A rule stands once; each `rows:` line names the old-forge rules carried in its section (fr: = recon forge-rules, fp: = recon forge-process). `(tool: B<n>, not built)` marks a command whose card is not built yet.

## Worker duties
- One verification run after your last edit; its output goes into your hand-back. Independent calls go out in one message. Trim output before it enters your context; read a red CI run with the host's own command piped through trim: `gh run view <id> --log-failed | python -B forge/tools/trim.py`. A token goes only in an unredirected header, never in a URL or a redirect. (case: owner 24.11.2026, D-0035 (fr:A30); FH-2072, FH-2080; dev1.jsonl:3655, a builder report with no witness, fr:A1, fp:A7)
- A wait has a cap, at most 3600 s, and a named condition; no loop waits on nothing. (case: owner 17.11.2026 (fp:A28); stale wait loops of old workers piled up, plan record 26.11.2026 01:58)
- Everything in forge 2 and every release text is English, with no Cyrillic character. (case: dev1.jsonl:3257, Cyrillic found in a package by critic t-1217)
- Fix the class: a sibling of a defect is fixed in the same round or named with an executor; you report analogs and do not widen your scope. (case: owner 17.11.2026, fr:A6)
- One experiment before machinery: when a decision rests on an unknown property of the environment, measure first. (case: owner 27.10.2026, fp:A25)
- Size caps: designer draft 40,000 bytes; builder report prose about 500 words; critic review about 1800 words; final message 2,000 characters. (case: owner 17.11.2026, fr:D10)
- At a cap warning write what is done; at the cut hand back done and not done; a plain commit of your unfinished work is allowed. (tool: B5 `budget.py`, not built) (case: owner 25.11.2026 20:56, B5)
- Refer to a document by its key -- card id, `W-<n>`/`D-<n>`, `L-<n>`, `plan <h>` -- never by a line number. (tool: B13 `refs.py`, not built) (case: RELATED_WORK section 8 item 4, 113 line references measured in the spec)
- Session start prints now, last, snapshot, hooks, old processes and worktrees; with none of it in your context the start hook did not run: read forge/BOOT.md and forge/COORDINATOR.md by hand. (tool: B2, not built) (case: FH-1007, FH-4151, the old forge printed the rule files at every start)
- An optional hand-back line `snag: <problem> -> <impact> -> <smallest fix>`; the Lead turns it into a work-list record. (tool: B11 `worklist.py`, not built) (case: plan record 25.11.2026 22:20)
rows: fr:A30, fp:A28, fr:A6, fp:A25, fr:D10, fr:A1, fp:A7, fr:A29

## Dispatch form
- A dispatch carries header lines outside fences and quotes, printed and checked by `python -B forge/tools/dispatch.py`: `task:`, `role:`, `caps:`, `given:`, `owns:` (absolute paths), `non-goals:`, `handoff:`, `edges:`, `DoD:` (the verification command in backticks), `siblings:`, `test:`, and for a builder `carry:` and `duties:` (tool: B15, B18, not built). (case: card C1-4, the old forge's rule 11 header form)
- Outside input (a CLI, a ticket, a person's words, a config, a host answer) gets an adversarial mini-battery -- magnitude, nesting, encoding, empty or broken input -- and every limit applied to it a case AT and BEYOND it, each a table row. (case: owner 10.11.2026, 17.11.2026, fr:A3)
- A spec names its edges: every limit, every empty or absent input, every pair of its own requirements that can conflict, every artifact the change brings into existence (both worlds), each with the invariant it protects. A silent edge is the dispatcher's defect, never the performer's guess. (case: dev1.jsonl:1120, a DoD line silent on an edge; t-896, 65 spec rejects of 11-16.11.2026)
- A node is written for a weaker model: file, function or field, expected behavior and a test per item; the direction is chosen, not listed as options; a fork the writer cannot decide is a question with a recommendation, and the node runs on it. (case: owner 30.10.2026)
rows: fr:A3, fr:A2, fr:A27

## Scout
- A negative claim ("absent", "none") counts only with a positive control of the same shape (same tool, syntax, filters; case-insensitive); empty output of a miscalled tool proves nothing. Every role's claim, a scout's above all. (case: an empty search from a miscalled tool was reported as absence: `\b` does not fire on Cyrillic, grep -i does not fold Cyrillic case, a one-language query misses localised data, a marker searched in varying body formats, FH-3083; fr:A4, fp:A10)
rows: fr:A4, fp:A10

## Builder
- Tests are few and strong: the expected value is traced to a spec line, a rule or the owner's word, never to the code under test; a test must be able to fail (a red-before run); test lines never exceed code lines; forge/TESTING.md holds the layers. (case: owner 10.11.2026, 17.11.2026, fr:A20, fp:A9; P20)
- Before hand-back, for each new or changed function search the repo for the same PROBLEM (not the helper's name) and write `similar: <command> -> <hits>; each: reused | changed too | differs: <why>`, with a positive control of the same shape; a text-only change writes `similar: n/a -- no code`. Also `friction: <tool a role calls>: before/after <calls, refusals> | not measured: <why> | n/a -- no tool a role calls`. (case: P12 of the old forge's OWNER_PRINCIPLES; plan catalog "test code: duplicate helpers")
- The first lines of every code file you create name its card: `card: <id>`. (tool: B13 `refs.py`, not built) (case: RELATED_WORK section 8 item 4)
- Add one hand-back line per carry row: `carry: <row id> -> <where it lives now> | not done -- <why>`. (tool: B15 `carry.py`, not built) (case: B15, outside audit point 1: a row proves a decision exists, not that the content survived)
- A commit that adds a tool, hook, CI job, gate row, data file or dashboard view carries `mechanism: <path or id> -- protects ..; origin ..; cost ..; pays ..` (forge/COORDINATOR.md, cost rule); CI reds it without the line. (tool: B16 `size_ratchet.py` mechanisms row, not built) (case: B16, digest K2, old rule 10)
- A file that activates itself (a hook on the live path, a gate) is handed over as content or under a neighbouring name; the Lead places it on the live path at acceptance, after review. (case: dev1.jsonl:4898, a handed-over `.next` hook form that four readers could not read)
- A doc-only witness (a key-presence run) quotes its keys verbatim from the DoD before the run, attaches the script in full, and runs a negative control: one key removed, the script reports failure. (case: docs/tasks/specs/reviews/20261113-stage-critics-removed-plan-critic.md, finding F-15)
rows: fr:A20, fp:A9, fr:C3, fp:A8

## Critic
- A critic or designer writes only its one handoff file and returns its verdict there. (case: FH-3021, a reviewer edited product files)
- The verdict is a file: one line per reviewed thing `<thing>: fit | fit_with_fixes | blocker -- <why>`, a trail of what was read and rerun, and every probe made on a copy with an unmutated control run beside its kill; the DoD greps the verdict lines. (case: FH-4020, FH-4023, FH-4031; fr:B3)
- Test review: killing power (a probe), the source of every expected value, a row per behaviour, no duplicate row, the file budget. (case: owner 10.11.2026, 17.11.2026, fr:Q5)
- Duplication and code quality are judged on every diff: does it re-implement a reader, writer, helper or table the repo has. (case: owner 06.10.2026, fr:A22)
- Does the diff move a role's judgment into code, or add non-craft text a role must read. (case: owner principle P27, D-0060, fr:Q11)
- One road: no language, project or case reaches a shared mechanism outside a data row or the owner's word. (case: owner 06.11.2026, P31, fr:Q12)
- Check the builder's `similar:` and `friction:` lines against the diff. (case: P12, B6)
- Fit to the spec: every requirement, edge and key as written, with the spec's error direction -- no unknown becomes a pass. (case: dev1.jsonl:4669, an unknown passed because the dispatch was silent on that edge)
- The builder's own decisions on points the spec left silent go the safe way and match the consumers the spec names. (case: dev1.jsonl:3791, a fail-open on an unreadable registry)
- Seams: files other nodes own or follow are touched additively, localized, nothing reordered. (case: docs/tasks/specs/reviews/20261113-cl4-1-topic-code-critic.md, a seam note naming the calls the next node must keep)
- Class-wide completeness: the sibling axes of the defect and the neighbours in the same artifact are fixed in the round; a leftover carries an executor. (case: dev1.jsonl:401, a sibling in the same artifact; D-0044)
- A new function over about 60 lines or over 3 nesting levels, copy-paste, a dead branch, a lying name or an unread result is a finding with a severity, never a style pass. (case: dev1.jsonl:2667, a nesting finding)
- A diff that adds or raises a row of a shrink-only ratchet is named in the verdict row by row (key, old to new, reason); an unnamed raise is a finding. (case: critic t-836 of 16.10.2026, in the title of the old SIBLING_MAP axis 18: a raise inside the diff that adds the site was green in-tree)
- Architecture: which invariants of the architecture map the diff touches; for each, producer and reader are walked both ways with a positive control; a second reader, writer, form or seam is a finding; on an unknown value no block, no silent default, no hand-off to a person (VARIETY). (case: D-0055)
- Plan gate: edges in both worlds, the meaning of each changed field restated, premises reproduced, readers of every touched file answered, forks consistent with the evidence. (case: t-896, 65 spec rejects of 11-16.11.2026 -- 42 found by the code critic, 4 by the plan critic)
- The submitter's load-bearing claims are inputs to verify: a negative or codebase-wide claim gets your own search with a positive control, a cheap witness is re-run, a claim you could not reproduce is a finding; a data field's meaning comes from a query on real data, not from a neighbour's code. (case: dev1.jsonl:1848, an unverified claim of two quarantine reds)
rows: fr:B3, fr:Q5, fr:A22, fr:Q11, fr:Q12, fr:A21, fp:A20, fr:A23, fp:A21, fr:Q1, fr:Q2, fr:Q3, fr:Q4, fr:Q6, fr:Q7, fr:D9, fr:Q9, fr:Q10, fr:Q13, fr:A5

## Designer
- Before applying a cited rule, read the cited record's kind and scope (a `decision` is never her word; a record of another scope is listed, not applied). A critic does the same. (case: plan 3.11, B3: a factory rule read as a forge rule; tool `words.py` of B3 not built)
