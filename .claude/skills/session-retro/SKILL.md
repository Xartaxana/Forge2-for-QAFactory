---
name: session-retro
description: End-of-session retro of a coordinator session (the Lead or the Architect) -- what got in the agents' way and where the forge or the factory can be optimised. Counts come from forge/tools/retro.py, the reasons from the session's own context; the result is ONE file logs/retro/<session>.md plus a short list of its important points said in chat, never a node. Use before a compaction, from session-handoff step 6, or when the owner says "retro".
---

# session-retro: what got in the way, written while the reasons are in context

Goal (the owner's word 17.11.2026): find what hinders the agents and where the forge or the factory can be optimised.
The reasons live only in this session's context, so the retro runs HERE, before a compaction and before the session
closes; a week later the transcript still shows what happened but not why. A retro entry is raw material, not a task:
nodes are opened only after the weekly reduction has merged the repeats and chosen a SYSTEMIC fix.

## 1. Counts by code

- `python -B forge/tools/retro.py write <session>` creates or refreshes logs/retro/<session>.md with its counts block; never count by reading the transcript; `retro.py check <file>` recounts the block byte for byte.

## 2. Reasons and answers

- A reason per non-zero counter and an answer per question of the file (Q1-Q5); every item carries a NUMBER where one exists (turns, tokens, repeats -- from step 1, or `not measured`), the CARRIER (file and line, hook, tool, dispatch id) and where the fix belongs: code / rule text / spec / tool / nothing. An empty answer is `nothing: <why>`, not left out.

## 3. One file

- One file per session, no money figures (P18).

## 4. Say it in chat

- The file alone does not reach the owner: say ONE short list in plain words, each item one line with its number and where the fix belongs -- at most five IMPORTANT points, and every open question to the owner, none dropped.
- The important points are picked by these marks, in this order: what stopped the work or cost a rejected attempt; the largest counts of step 1; a gate or hook that refused wrongly (Q3); a decision the session took itself and is not sure about (Q4).
- No item under these marks is said as `retro: nothing important -- <why>`; everything else stays in the file.
carry: FS-191, FS-193

## 5. Nothing is fixed from the entry

- Do not open findings or nodes, edit rules, or fix anything from the entry in this session: a patch per entry per session is exactly what this skill must not produce.
- One exception: a defect that blocks the session's own current work is fixed on the usual road, and the entry says so.
carry: FS-194, FS-195

## 6. Commit

- The retro file is committed with the session's last journal commit, after `session_end` (session-handoff step 7).
carry: FS-196

## Weekly reduction

- The Architect reduces the entries at the weekly calibration (forge/calibration.md B9: `retro.py sum --since <last reading>`, `retro.py missing`): items grouped by class of the factory or the forge, not by session or file; per class one line `fix: <node>` / `already fixing: <node>` / `not fixing: <reason>`.
- A `not fixing` class stays on record between readings, so that the next entry of the class raises its count instead of reopening the analysis. (tool: none yet -- B9 names no place where class lines persist between readings)
- A class with one entry gets no node until it repeats, unless the entry names a defect that stopped the work.
carry: FS-204, FS-205

## Detector

- A skipped retro shows as session-handoff step 6's `retro: skipped -- <reason>` line, and as a session on the `retro.py missing` line written in the B9 reading.
