# S11-2 -- the critic set, first exam, 26.11.2026 (UTC)

Question (draft t-2037): does the forge 2 wording of a critic rule still make a critic act as the old forge's wording did? Six tasks, twelve planted items (each on a `carried-differently` row of `forge/specs/recon/carry/forge-roles.1.md`), six intact passages.

## Verdict

- LOSS 0: no item that the old rules caught was missed under the forge 2 rules, in either run.
- GAIN 1 (T3-2, row FO-83: a test that cannot fail): the forge 2 arm caught it 3 of 3, the old arm 0 of 3, the bare arm 0 of 1.
- rank: `does not rank (2 discriminating, 0 unmeasured; LOSS 0, GAIN 1)` -- the set has fewer than three discriminating items, so it says "no loss seen", never "the rewording is proven equal".
- No arm raised a blocker on any of the six intact passages (no false alarm, all three arms alike).
- No ledger change is owed (draft Q5 acts on a LOSS only; the exam writes no ledger verdict, I8).

## What was measured

- arms: `old` = old forge b01363a1 rules, `new` = forge 2 rules at ab6dc5f99317a4e949e2c4a7273f7968a9f64dbe, `bare` = the role body with no rules; rows in `measure/seeded/arms.yaml`.
- model `claude-opus-5-5` in every arm and in the judge; harness `2.1.328 (Claude Code)`; launch tools Read, Glob, Grep.
- command: `python -B measure/tools/seeded.py run --set critic`; score: `python -B measure/tools/seeded.py score --set critic --date 20261126`.
- keys before the first run row: the set d0f1d68 (authored 2026-11-26T22:58:34Z) and the key review's fixes 1c8110f (authored 2026-11-26T23:13:52Z); first run row started 2026-11-26T23:15:47Z. Key review: verdict blocker on the severity sentence of every catch (it would have given a false LOSS), fixed in 1c8110f before any run row.
- rows: 44 run rows (22 arm sessions, 22 judge sessions), all `measured`; 66 score rows; 120,878 output tokens (carrier: `runs.jsonl`, field `tokens`).

## Per item (this folder, the exam of record)

| task | item | ledger row | class | old | new | bare |
|---|---|---|---|---|---|---|
| T1 | T1-1 | FO-4 | does-not-rank | 1/1 | 1/1 | 1/1 |
| T1 | T1-2 | FO-32 | held | 1/1 | 1/1 | 0/1 |
| T2 | T2-1 | FO-29 | does-not-rank | 1/1 | 1/1 | 1/1 |
| T2 | T2-2 | FO-86 | does-not-rank | 1/1 | 1/1 | 1/1 |
| T3 | T3-1 | FO-103 | does-not-rank | 3/3 | 3/3 | 1/1 |
| T3 | T3-2 | FO-83 | GAIN | 0/3 | 3/3 | 0/1 |
| T4 | T4-1 | FO-97 | does-not-rank | 1/1 | 1/1 | 1/1 |
| T4 | T4-2 | FO-33 | does-not-rank | 1/1 | 1/1 | 1/1 |
| T5 | T5-1 | FO-27 | does-not-rank | 1/1 | 1/1 | 1/1 |
| T5 | T5-2 | FO-12 | NOISE | 0/1 | 0/1 | 0/1 |
| T6 | T6-1 | FO-115 | does-not-rank | 1/1 | 1/1 | 1/1 |
| T6 | T6-2 | FO-12 | held | 1/1 | 1/1 | 0/1 |

Classes: LOSS = old caught, new missed; GAIN = the reverse; NOISE = neither rules arm caught; does-not-rank = all three arms caught (the plant is caught with no rules at all); held = both rules arms caught and bare missed (a discriminating item).

## The second folder, `20261126-2`: an accidental second launch

The run command was started twice, 25 seconds apart, by the Architect's mistake (a first command the shell gate reported as refused had started all the same). The second run is kept as a replicate, not as a second exam. It is cut at its very end: the third repetition of T6 in arm `new` was judged once (T6-1 caught, T6-2 unsure) and the process was stopped before the second judge and the score rows, so T6 `new` stands at 2 of 2 there. 51 run rows, 75 score rows, 130,152 output tokens.

- same classes as above, except: T3-2 GAIN again (old 1/3, new 3/3, bare 0/1); T6-2 GAIN instead of held (old 0/3, new 2/2, bare 0/1); T6-1 old 3/3, new 2/2.
- its rank line: `does not rank (1 discriminating, 0 unmeasured; LOSS 0, GAIN 2)`.
- Over both runs: LOSS 0; T3-2 old 1 of 6, new 6 of 6; T6-2 old 1 of 4, new 3 of 3 scored.
- Cost: the two runs together are 95 sessions against the about 52 the owner's word W-199 covered.

## What this exam does not show

- Most plants are too easy: eight of twelve are caught by the bare arm, so they cannot tell a good rule text from none. A next edition needs harder plants to rank.
- T5-2 (FO-12, the class-completeness walk) is caught by nobody, and T6-2 on the same row is unstable in the old arm (1 of 4): the row is weakly exercised, not proven.
- Arms had no Bash: a trap that needs a run or a write is not exercisable in any arm (`residual.txt`); no item is `judged_by: run`.
- Plan-gate rows FO-130, FO-134 and FO-135 are `carried-differently` and qualify, but the authoring dispatch asked for diffs only: they are in no task. A plan-gate task is owed in a later edition.
- Left out with a reason: a review with no spec or DoD (FO-21, FO-141) and the duplicate row (FO-91, FO-151) are `carried` verbatim, so I8 gives no item; the internal-asymmetry kind has no old rule of its own (nearest FO-77).
- T2 holds a third real defect the key does not list (`retro.py sum` prints a missing line without the session a sibling command names); no intact passage sits on it, so it scores nothing either way.
- Verdict vocabularies differ (forge 2 line form, old JSON form); the key's severity sentence counts a blocking finding in either.
- One repetition per arm unless the rules arms disagree (then three): a `held` at 1/1 is one sample.
