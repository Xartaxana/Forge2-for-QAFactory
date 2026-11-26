# Work list, interim carrier

This file holds the work list until B11 (`forge/tools/worklist.py`) is built: one row per task, idea, bug or open owner question, and nothing else. The Lead writes it (an Architect session writes only its answers); the Lead reads it at every session start. It retires into `worklist.py` when B11 lands: its open rows are moved there and the file is deleted in the same commit.

| id | kind (task, idea, bug, owner-question) | for (lead, architect, owner) | what waits | status |
|---|---|---|---|---|
| wl-1 | task | lead | 382 carry-ledger rows are `carried` but their note is still the pre-restore text (`candidate drop: ...; restored wave 1/2`, no quote): refresh each note to a `path:N "quote"` of the rule file (builder t-2078 round 5 sweep; FR-1062, FO-5, FR-1135, FO-25 spot-checked, the rule files hold them); statuses stand | open |
| wl-2 | owner-question | owner | the drop list: every old rule not carried into forge 2 needs her confirmation with its reason (W-188); the list is read from the carry ledgers after restore waves 2-3 merge | open |
| wl-3 | owner-question | owner | S1 the forge code ceiling and S2 the plan and spec ceiling: her numbers | open |
| wl-4 | task | lead | S11 seeded sets: the runner is built, the sets are not planned (owner: every S task before the move) | open |
