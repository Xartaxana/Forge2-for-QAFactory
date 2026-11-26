# Work list, interim carrier

This file holds the work list until B11 (`forge/tools/worklist.py`) is built: one row per task, idea, bug or open owner question, and nothing else. The Lead writes it (an Architect session writes only its answers); the Lead reads it at every session start. It retires into `worklist.py` when B11 lands: its open rows are moved there and the file is deleted in the same commit.

| id | kind (task, idea, bug, owner-question) | for (lead, architect, owner) | what waits | status |
|---|---|---|---|---|
| wl-1 | task | lead | 382 carry-ledger rows are `carried` but their note is still the pre-restore text (`candidate drop: ...; restored wave 1/2`, no quote): refresh each note to a `path:N "quote"` of the rule file (builder t-2078 round 5 sweep; FR-1062, FO-5, FR-1135, FO-25 spot-checked, the rule files hold them); statuses stand | open |
| wl-2 | owner-question | owner | the drop list: every old rule not carried into forge 2 needs her confirmation with its reason (W-188); the list is read from the carry ledgers after restore waves 2-3 merge; the list is written (Architect, 26.11.2026) and waits for her word | done: W-198, 26.11.2026 (117 rows dropped, FO-1035 and FO-1057 restored) |
| wl-3 | owner-question | owner | S1 the forge code ceiling and S2 the plan and spec ceiling: her numbers | done: W-199, 26.11.2026 (forge_code 6000, plan_spec 1,700,000 bytes) |
| wl-4 | task | lead | S11 seeded sets: the scout, builder and Lead sets are the first tasks after the move (W-199); done before it: the critic set (S11-2, first exam 26.11.2026: LOSS 0, does not rank, measure/runs/forge-roles/critic/20261126/result.md) and the re-run rule S11-7 (`seeded.py due`); a later critic edition owes harder plants and a plan-gate task (rows FO-130, FO-134, FO-135) | open |
| wl-5 | task | lead | forge/tools/journal.py CLOSING counts `return` as closing a dispatch, while .claude/skills/session-handoff/SKILL.md says a `return` alone is RESULT PENDING (old rule FR-1127): the open list keeps a returned dispatch open until `accept` or `reject` (scout t-2089) | open |
