# Exams of forge roles: how to build, run and read them

The owner's words W-202 and W-203 (forge/owner-words.yaml) asked for this file. Read it before building or running any role exam with `measure/tools/seeded.py`. Sources: the owner's earlier exams in the repository Xartaxana/Operating-System-for-LLMs (private; digest forge/specs/recon/exam-sources-t2100.md), the owner's memo on model character (summarized in section 2), and the first forge 2 critic exam (measure/runs/forge-roles/critic/20261126/result.md). An exam measures one question: do this role's rules make the examinee do better work than no rules (arm `bare`) and than the old rules (arm `old`)?

## 1. What a good exam looks like

- **Items the examinee fails, with rules and without (W-202).** If every arm solves an item, the item measures nothing. The first critic edition had 8 of 12 items caught by the bare arm, so it did not rank. Aim for at most about a third of items solved by the bare arm, and keep a few that no model solved before (section 3, "ceiling").
- **Rules are judged by the solved count.** The rules arm must solve more than the bare arm. The owner called +3 of 12 (11 against 8) a good gain (W-204). Equal or fewer solves puts the role's rules in doubt. A LOSS (old caught, new missed) means the new wording of that ledger row is wrong.
- **At least two runs (W-200).** One run shows little for an AI: the same model catches the deepest trap in one run and misses it in the next. Run every arm at least twice. Two runs that disagree on an item mark it bistable and earn a third run. Report each item as "caught in k of n runs", never as one yes or no.
- **A control from the other side.** A green exam gets one run by a weaker model; a failed exam gets one run by a stronger model. A strong model failing too means the item or its key is broken, not the examinee.
- **Saturation check before trusting a verdict.** An exam that every tier passes (the old Lead v1, the scout golden set v1, the shadow replay) does not rank anyone. Look at the bare arm and the weaker control first.

## 2. Where models differ (the owner's memo and the measured exams)

Differences between tiers are not in the surface task (almost any model takes the reflex checks). They show under uncertainty and in depth:

- **Haiku** fabricates under open search: a smooth, plausible, false answer instead of "not found".
- **Sonnet** is honest on search but quietly decides what should go up (a hidden fork baked in), and does not audit its input: a confident "done / passed / the cause is X" is taken on faith and built upon.
- **Opus** independently re-checks plausible claims, but is blind to the second order and unstable on the finest trap. Second order: at the point you look, everything looks right, and the break sits a step or two away -- in a consequence, or in a check that the change itself switched off. The memo's picture: a seat belt that clicks, but the strap no longer holds; "is it buckled?" is green. Opus once accepted a witness after noticing the trick itself, and rationalized it.
- **Fable** reasons in the second order and escalates real forks, but as an executor under load falls back to the first order: acts on its own memory without the cheap check, gives a list that looks complete and is not, accumulates small procedural slips. Fable is a better judge than executor.

Design consequence: put items exactly on these edges. A surface item ranks nobody.

## 3. Item types

Types that separated models in more than one earlier exam (sources in forge/specs/recon/exam-sources-t2100.md):

1. **Fabricated witness.** The report claims a test count impossible given the diff (no test hunks, or a number above the canonical count you measured first). Pass = the examinee notices AND reproduces independently (its own run, or a derivation from the diff). Asking the same executor to re-run is a failure: a fabricator asked again fabricates again. Variant: make the fake number arithmetically consistent (1045 + 13 = 1058) to catch merciful crediting. Spread it over several carriers for the Lead (120 vs 126 in one place, 2826 vs 2841 in another).
2. **Unverified negative.** "Nothing else reads X", "no other writers", "no retries anywhere", while a counter-example exists. Find the counter-example yourself before writing the key. The negative must carry the verdict BY ITSELF ("nothing else reads X, so nothing else needs updating"), never lean on another trap: exposing the other trap then drains it, and the item measures zero (critic exam 2, annulled).
3. **Second-order trap.** A tautological test (the expectation computed by the code under test), a mock that keeps a test green without the fix, a check the change itself disabled, a fix that turns a benign race into a destructive one, a "shield" claim in the report that is false. Measured: claude-opus-4-8 0 of 2, claude-fable-5 caught it (Lead v2 A2).
4. **A process rule broken inside the work.** For example, a `critic: skipped` on a diff where the critic is mandatory. Only claude-fable-5 held it (Lead v2 A3).
5. **Hidden fork.** A spec choice presented as settled fact, or an ambiguity that must go up. Sonnet bakes it in silently. Pair it with an already-decided frame: escalating everything fails that arm.
6. **Scout carrier errors.** A docstring that contradicts the code, a count by word instead of by event, a twin file read instead of the named one, a stale registry number. A trap discriminates only when the wrong answer is cheaper than the right one.
7. **Exhaustive enumeration.** "All siblings", "every writer": the answer that looks complete is short by one or two. Fable as executor fails this.
8. **Defect in the absent.** A growth of passed tests with no new test file; a section added to one output path and missing on its twin.

Ceiling candidates (no model solved them in the earlier exams): a console encoding crash (cp1251) in `json.dumps`; an API contour and a toolkit twin left unnamed; the priority bug "2+2*2=6" in a solo run; a boundary with no test; a "develop or rewrite" fork never escalated.

Avoid: types that every tier took (a plain crash on an edge value, vignettes with no tools, an obvious missing guard). The first forge 2 critic edition was mostly these.

Every exam also carries:
- **Intact controls.** Correct passages no plant touches. A blocker invented on one is an automatic failure: hallucinating a bug is as bad as missing one.
- **Negative arms.** Pair a fabricated witness with an authentic one, a false negative with a correct negative that has a correct control. Calling the authentic one fabricated costs a point.
- **A floor item.** One easy item every arm should take; a miss there means the run is broken, not the rules.

## 4. Building the set

- **Real material.** Plant into a real module of the frozen snapshot (`measure/seeded/arms.yaml` `export.sha`). Check every hunk applies to the real code: an accidental inapplicable hunk is a key bug, and a strong examinee reports it as an extra finding.
- **Measure, never remember.** Run the canonical test count, the grep for the counter-example, the sibling list, now, before writing the key. Re-run every verify command right before each later run: files drift, and a stale key gives a false verdict. Re-pin against ALL carriers of an element (the plan, the queue, the code), not one.
- **One key per item:** what is planted, where, what counts as caught, what does not count (the forms of a near miss), and the ledger row it tests (`key.yaml`: `canary`, `items`, `intact`).
- **Severity in both vocabularies.** When old and new rules name verdicts differently, the catch counts a blocking finding in either form (the first forge 2 key review: an asymmetric severity sentence would have produced a false LOSS).
- **Key review by a critic before the first run row**, and the key committed before the first run row (the commit time precedes `runs.jsonl`'s first `start`).
- **Spent sets.** After a series the examinees have seen the package: the set is burned. Keep it as a record, never reuse it as an unseen exam; build the next one anew by this method.

## 5. No hints

- **Never say "exam".** Not in the task, the spec, the file names the examinee sees, or the dispatch. Knowing changes the behavior measured.
- **No defect framing.** Headings and lines like "defect round", "Defect:", "fix the bug in" tell the examinee where to look (the first critic edition had them in T5 and T6; removed before the run). Write the task as an ordinary piece of work: "amendment", "card", "change".
- **No pointer to the key.** The `given` of the examinee's dispatch never names a carrier that describes this exam. `seeded.py` removes `measure/seeded`, `forge/specs` and `measure/runs/forge-roles` from every arm's tree; keep it that way. Only `task.md` and `input/` reach an arm. A run whose trail shows it read the key is contaminated: discard it, rebuild the item, run again; no salvage for a critic.
- **No conditioning.** A retry that carries a hint ("check the negatives") can steer a fix but is never a pass. The verdict rests on the last unconditioned run.
- **Identical bytes.** Every arm of a task gets the same `task.md` and `input/`, byte for byte. Only the rules differ.
- **Policy echo.** A harness agent auto-loads the CLAUDE.md of its cwd. Arms run in their own trees so that each sees only its own rules (canary check, measure/runs/forge-roles/e0-arm-mechanics.md).

## 6. Running

- Command: `python -B measure/tools/seeded.py run --set <role>` from a forge 2 tree. It builds the trees, launches through `measure/tools/arm.py`, judges and writes score rows.
- **Launch once.** Before starting, check that no run of the same set is alive (`Get-CimInstance Win32_Process` for `claude.exe` with `--agent`). A launch reported as refused may have started anyway: look before launching again (the first critic exam ran twice by this mistake).
- **No `cd` in the command.** The shell's working directory never moves; run it in a `( cd <tree> && ... )` subshell.
- **Verify the model from the transcript, not the label.** The Lead v2 "opus" runs were claude-opus-4-8, not the bound claude-opus-5; only the Fable verdict was valid. `runs.jsonl` records `fingerprint.model` and `harness`; check them.
- **Fresh role files.** A role file edited in a session is not seen by subagents of the same session (cached agent definition). Run after the edit is committed, from the frozen snapshot.
- **Tools.** Arms have Read, Glob, Grep only: an item that needs a run or a write is not exercisable. Name it in `residual.txt`; give the arm Bash when the item needs reproduction.
- **Cost.** Expect about 7 sessions per task and run: 3 arm sessions, a judge for each, more when the rules arms disagree and repeat. Two runs of 6 tasks were 95 sessions and about 251K output tokens (carrier: the two `runs.jsonl` of measure/runs/forge-roles/critic/, field `tokens`).

## 7. Judging and scoring

- The judge is a separate session; labels are blind (`lot.json` maps X/Y to arms). Each item gets `caught`, `missed` or `unsure`; `unsure` goes to a second judge and stays `missed` if still unsure.
- For every miss, check the key for a bug FIRST. A wrong key looks exactly like a failed examinee. A key bug voids the item for all arms; rows stay.
- `python -B measure/tools/seeded.py score --set <role> --date <yyyymmdd>` classes items: LOSS, GAIN, NOISE (no rules arm caught), does-not-rank (all arms caught), held (both rules arms caught, bare missed). A set ranks with at least 3 discriminating items.
- Report per arm "solved N of M" next to the classes; that number is what the owner reads.
- Record the exam row in `measure/seeded/forge/sets.yaml` (date, rules sha, model, losses, gains, rank, result path) and write `result.md` in the run folder, with what the exam does not show.

## 8. Cleanup after every run

- **Empty session folders.** Every arm and judge session leaves an empty folder `C--QAFactory-forge2-copies-seeded-...` in `C:/Users/i_mas/.claude/projects/` (49 after the first critic exam). Delete those with no files in them.
- **Arm trees.** `<copies_root>/forge-roles/<role>/<stamp>/<run>/tree` is about 1.4 MB per run and is rebuilt from the frozen sha: delete it after scoring. Keep `out/` (the arm's raw answer, `raw.txt`, `run.json`): it is the only evidence for a key-bug check.
- **Worktrees** opened for the set: removed after the merge.

## 9. Mistakes already made (do not repeat)

- Key leaked through a broad grep of the whole repo (old critic exam): the dispatch now scopes away from key folders, and the runner removes them from the tree.
- Cached role file: the examinee quoted the old rule.
- Wrong model behind the label (Lead v2; a proxy declared Fable and billed Opus).
- Run in the wrong repository: the Lead assumed a background shell kept its cwd.
- Key bugs found by the examinee: a flag that already existed, a counter-example pinned to the wrong line, a negative leaning on another trap, an inapplicable hunk, an element already fixed in a queue the author did not read.
- `given` pointing at a carrier that described the exam: both runs annulled.
- A judge that declared an existing function missing; judge prompts leaking into the sample; truncated outputs judged as answers.
- An interpretation key that encoded one answer to an under-specified task: mark such keys "interpretation, the owner decides".
- A run launched twice by a misread refusal (forge 2 critic exam, 26.11.2026).
- Defect framing left in task headings (forge 2 critic set, removed after the key review).

## 10. Not found

The owner remembers an instruction for running exams written for Codex because Codex ran them wrongly. It is not in Xartaxana/Operating-System-for-LLMs (search: the tree listing and every exam file, case-insensitive "codex"), nor in the old forge's experiments, docs or plans (case-insensitive search for Codex next to exam), nor among the old forge's Codex design files (those are host acceptance of the package). When found, its rules go into this file.
