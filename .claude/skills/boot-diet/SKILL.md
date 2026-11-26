---
name: boot-diet
description: Reaction to a red `size` job or a byte-ceiling breach of the rule and boot files (forge/budgets.json rows, measured by forge/tools/size_ratchet.py) -- measure which file grew and why, move or deduplicate what does not belong there, check trimmed and full pairs, re-measure, report. Cutting a rule line to fit is never the reaction without the owner's word; a ceiling goes up only by a `ratchet-raise:` line. Use when size_ratchet.py exits 1, when a ceiling is near, or when asked how to shrink the rule files.
---

# boot-diet: reacting to a ceiling breach of the rule and boot files

The rule and boot files (CLAUDE.md, .claude/agents/*.md, forge/COORDINATOR.md, forge/BOOT.md) are read by every
session, so their bytes are a paid resource. Their ceilings are the rows of `forge/budgets.json` (rules_worker,
rules_coordinator, boot_page); `python -B forge/tools/size_ratchet.py` (CI job `size`) measures them and exits 1 on a
value above its ceiling or an unrecorded raise. This skill owns the order of the reaction; session-handoff step 4
triggers it and does not repeat its steps.

## The order of moves

- The order is strict: cheap reversible moves (moving content to its own carrier, deduplication) come BEFORE expensive irreversible ones (cutting into the operational homes: CLAUDE.md, forge/COORDINATOR.md, forge/BOOT.md, .claude/agents/*.md and any other file every session loads).
- A breach never authorizes a cut: cutting or over-compressing a rule line to fit a ceiling is never the reaction without the owner's word; still breached after the reversible moves, the deep cuts go to the owner as an explicit decision (a work-list record `--for owner`, tool: B11 not built) and are never done unilaterally, because policy that is not loaded every session is silently skipped. (tool: none yet -- size_ratchet.py gates a raise of a ceiling, nothing gates a cut of a rule line)
- The other road is a raise: a ceiling in forge/budgets.json goes up only with a commit line `ratchet-raise: budgets.json <row> -- <W-n | D-n>` in the checked range whose id resolves to a record (forge/tools/ratchets.py judge_raises).
carry: FS-7, FS-31

## 1. Measure and diagnose

- Run `python -B forge/tools/size_ratchet.py` (bytes per budget row), then name WHICH file of the red row grew and by how much (`wc -c` per file, `git log` on it): treat the cause of the growth, not the symptom.

## 2. Relevance walk

- Walk every file of the red row entry by entry and ask of each: does every future session need this? Anything that belongs to one task, one card or one day moves to its own carrier (forge/carriers.json: spec, journal, owner-words record, measured run), with a one-line pointer only where a reader could still look for it.
- The report writes a verdict per entry walked: `moved to <carrier> -- <why>` or `stays -- <why>`. A line nobody needs that has no other carrier is reported to the Lead and the owner, never cut without the owner's word (a deep cut: "The order of moves").
carry: FS-28

## 3. Deduplicate

- Content living in two of these files at once gets a single owner plus a pointer from the other (a rule stands once).

## 4. Trimmed and full pairs

- When a trimmed core and its full side exist, confirm their entry counts and ordering still match; if the full side was edited more recently than the core (`git log -1` on both), review the full side's diff since the core's last edit and answer "does the core need this too".
- Confirm every path a trimmed and full pair names still exists: the point check, at a breach, of the path liveness the `refs` job (B13, not built) will run. (tool: none yet)
carry: FS-22, FS-23

## 5. Re-measure

- Re-run size_ratchet.py: green goes to step 6; still red follows "The order of moves" (the owner's word for a cut, or a raise line), never a unilateral cut.

## 6. Report and commit

- The report gives bytes before and after per file, what was moved and where, the verdicts per entry (step 2) and on the pairs (step 4), and the remaining queue (the deep cuts put to the owner); then the commit.
carry: FS-32

## How rules for agents are written

- One heading, one topic: a rule hidden inside another topic gets its own heading.
- A section is at most about 40 lines; one table is not a defect. (tool: none yet -- the byte ceilings bound files, not sections)
- A subheading goes only at a paragraph boundary, never between a condition and its consequence.
- CLAUDE.md imports nothing (no `@` import): an import loads into every worker, and its target lies outside the rules_worker row, so the `size` job would not see it. (tool: none yet)
- A retelling of a rule outside its home, a section over 50 lines and a boot heading with no contents line are defects found by the weekly calibration until code checks pointers and contents (the `refs` job, B13, not built). (tool: none yet -- forge/calibration.md row 33(h) is the weekly reading)
carry: FS-37, FS-38, FS-39, FS-45, FS-48
