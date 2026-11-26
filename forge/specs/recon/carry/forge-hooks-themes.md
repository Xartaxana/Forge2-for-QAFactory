carrier: forge-hooks
ledgers: forge-hooks.1.md .. forge-hooks.6.md
state: open

Each theme ends with the Architect's verdict of 2026-11-26 at theme level. A row inherits its theme's verdict at the ledger's migration (B15) unless the card that carries the theme says otherwise for that row. Three outcomes: carry (lines built now, in the named card), work-list (the idea is kept as a record of the one work list, B11, with the case that would promote it; nothing is built now), dropped (on purpose, with the reason). carried-differently means the purpose is reached by a thing forge 2 already has, named in the verdict.

Frame of the verdicts: forge 2 is one developer with several sessions; a check looks at an outcome and never prescribes a means; every mechanism has a cost (B16), so code is added where the failure is irreversible or the code is a line in a tool that is being built anyway, and a hook is promoted from a rule line only after a caught case; a lesson with no code is one rule line with its case (C1-1, inside its size budget).

Dropped on purpose, for the owner's list: the Stop gate family -- no stop is blocked for want of a green run, the track of edits and runs, the safety valve, the credit for restored bytes (H14, H25, H28, H33: the outcome is checked at acceptance by the acceptor's own run; the hook itself is a work-list record); the feature registry and its attribution warnings (H2); the architecture and judgment lines of a package commit (H16: no package code); the mechanism gate's axis and tier lines (H12); the wait reaper (H7); generated indexes (H5); main-red tracking (H20: main is protected instead); clone segments and the merge-time journal check (H22, H29: one developer); the judge pins (H19: no judge); the journal echo hook (H24: the one writer refuses at write time); the status lines of machinery that is not carried (H31); the cap of six parallel writers (H36).

Cards to write from these verdicts (a designer; one critic pass per card group): B17 hook runtime and session start (H3, H4, H13, H17, H32, H34; amends C1-5, B2); B18 journal and dispatch tools (H6, H8, H23, H35, H36, H40; amends C1-4); B19 irreversible moves (H9, H38; amends C1-5); B20 ratchets and references (H10, H21, H30, H37; amends C1-2, C1-3, B13); B21 rule lines with their cases (H1, H7, H15, H18, H26, H27; amends C1-1) and the work-list records (H2, H11, H14, H39). The two new refusals of B19 and the hook deadline of B17 are the Architect's own decisions (the owner may cancel them).

## H1 Negative-claim and empty-search control

- statement: Three warn-only hooks catch an absence claim made without a same-form positive control: on subagent reports, on empty search results, and on text about to be written, with a ledger of what was searched.
- what it was for: An empty search from a miscalled tool (Cyrillic word boundary, case folding, wrong body format) was reported as proof of absence and was wrong; command hygiene point 6 is the door each warning names.
- nearest cards: B14, B6, C1-1, C1-4, C1-5, C1-7, C4-5
- rows not-found: FH-1042, FH-1043, FH-1044, FH-1045, FH-1046, FH-1047, FH-1048, FH-1051, FH-3079, FH-3080, FH-3081, FH-3082, FH-3083, FH-3084, FH-3085, FH-3086, FH-3087, FH-5006, FH-5007, FH-5008, FH-5009, FH-5010, FH-5011, FH-5012, FH-5013, FH-5014, FH-5015, FH-5016, FH-5019
- verdict: carried-differently -- the rule is carried as one line of the forge rules (C1-1, with its case: an empty search from a miscalled tool was reported as absence) and as an acceptance duty: a negative claim in a report is spot-checked by the acceptor with a same-form control; the three warn hooks and the search ledger are dropped (no PostToolUse hook in forge 2; promotion after a caught case)
- decider: architect 2026-11-26

## H2 Feature attribution and metrics report

- statement: New backlog rows, package files and journal events must carry a registered feature, checked in WARN mode at commit and merge, and a deterministic per-feature report ranks fragility, process tax and node cost.
- what it was for: Without attribution nothing could be measured per feature; the check never blocks and exit 2 writes nothing, while rework and fix-of-fix counts showed where the process was costly.
- nearest cards: B11, B12, B13, B2, B9, C1-4, C1-5, C1-6, C4-6
- rows not-found: FH-5001, FH-5027, FH-5030, FH-5031, FH-5032, FH-5033, FH-5034, FH-5035, FH-5036, FH-5038, FH-5039, FH-5040, FH-5041, FH-5042, FH-5043, FH-5044, FH-5045, FH-5046, FH-5047, FH-5051, FH-5053, FH-5054, FH-5055, FH-5056, FH-6015
- verdict: split -- dropped: the feature registry, the attribution warnings at commit and merge, the fragility index (forge 2's unit is the card, named in every code file by B13 and in journal lines by task); work-list: rework per card counted from the journal (rejects, fix rounds, defects after acceptance) as one read beside B12's cost band and B9's retro counts
- decider: architect 2026-11-26

## H3 Hook runtime safety: deadlines and fail-open boundary

- statement: Every hook reads stdin and writes stdout on a bounded deadline (10 s and 5 s, env override capped at 600) and runs inside one fail-open boundary, so a broken payload or crash exits 0 with a visible line.
- what it was for: A pipe that never closes, a stuck stdout or a crashing warner once froze or blocked a whole session; a warning must never block, and an unchecked step must say so rather than look checked.
- nearest cards: B2, B5, C1-4, C1-5, C4-5
- rows not-found: FH-1050, FH-2007, FH-2061, FH-2062, FH-3029, FH-3038, FH-3040, FH-3041, FH-3088, FH-3089, FH-4032, FH-4056, FH-4076, FH-4109, FH-4110, FH-5017, FH-5018, FH-5081, FH-6067, FH-6068, FH-6126, FH-6130, FH-6142, FH-6143
- verdict: carry -- B17, amends C1-5 and the factory hooks C4-5: every hook reads stdin under a deadline and never waits forever, a warner that crashes exits open with one visible line, a step that could not check says so and never looks checked; ONE shared helper, never a copy per hook (the old forge copied it into many files)
- decider: architect 2026-11-26

## H4 Wiring audit and enforcement-chain probe

- statement: A read-only audit reports whether hooksPath, the three required git hooks and every settings.json hook command are actually wired, and a pre-commit probe re-runs it when a staged file belongs to the enforcement chain.
- what it was for: A hook that was never added or not executable guards nothing; the chain is built dynamically so a list cannot go stale, and the probe itself fails closed while a git hiccup fails open.
- nearest cards: C1-1, C1-2, C1-5, C4-5
- rows not-found: FH-2008, FH-2009, FH-2010, FH-2011, FH-2012, FH-2013, FH-2014, FH-2029, FH-2030, FH-2031, FH-2032, FH-2033, FH-2034, FH-2035, FH-2036, FH-2037, FH-2038, FH-2039, FH-2040, FH-2041, FH-2042, FH-2043, FH-4138, FH-6007
- verdict: carried-differently -- B17: the session-start hook (B2) prints one line naming how many of the wired hooks and git hooks it found against the list in the repo, and the boot page (B1) says the line is expected, so a missing line is itself the signal; the pre-commit enforcement-chain probe is dropped (a handful of files, their tests run in CI)
- decider: architect 2026-11-26

## H5 Generated indexes and AGENTS.md

- statement: Indexes of architecture invariants, factory rules and owner principles, and AGENTS.md, are generated from their sources with size caps, never hand-edited, and --check refuses a commit where sources changed and the file did not.
- what it was for: These files are read every session, so size matters, and a Codex session must read the same rules (it cuts silently at 32 KiB); a hand edit or stale copy would diverge.
- nearest cards: B1, B10, B3, C1-1, C1-2, C1-5, C1-6, C4-5
- rows not-found: FH-3015, FH-3016, FH-3017, FH-3018, FH-3019, FH-3020, FH-4010, FH-4011, FH-4012, FH-4013, FH-4014, FH-4015, FH-5020, FH-5021, FH-5022, FH-5023, FH-5024, FH-5025, FH-5026, FH-6008, FH-6009
- verdict: dropped -- generated indexes have no sources in forge 2 (no architecture.md, factory-rules.md or principles file to index); the purpose is reached otherwise: the size of what a session reads is C1-2's byte budget, and the same rules for another host are B16's pointer AGENTS.md checked by B13's references
- decider: architect 2026-11-26

## H6 Journal line form: required fields, vocabularies and timestamps

- statement: A journal line must carry the fields its event needs (model, attempt, failure class, builder witness, ref, worker_ref, feature, node) with closed vocabularies, monotonic timestamps within a drift window, and a validator that exits 1 or fail-closed 2.
- what it was for: Later counting (escalation, tier reconciliation, witness checks) needs these fields present and typed; a retelling instead of a witness, or a narrative-future timestamp, made the record unusable.
- nearest cards: B14, C1-4
- rows not-found: FH-2102, FH-2103, FH-2107, FH-2109, FH-2110, FH-2111, FH-2112, FH-2118, FH-2121, FH-2122, FH-2126, FH-2127, FH-2128, FH-2129, FH-2130, FH-2131, FH-3049, FH-3050, FH-4017, FH-4118
- verdict: carry -- B18, amends C1-4's journal tool, checked at write time by the one writer: an accept of builder work carries the verification run's output (a witness, never a retelling), a reject carries a cause word from a closed list of four (spec, capability, recon, tooling); the timestamp is the tool's own clock; dropped: the drift window, the model, node and feature fields
- decider: architect 2026-11-26

## H7 Wait reaper: stop outlived tool-call process trees

- statement: A reaper finds this session's tool-call process trees older than a limit and stops them only with --apply, with pid-reuse protection, a never-reap list, orphan handling, a log and a WAITS line at session start.
- what it was for: Bounded waits were not enforced and stale wait loops piled up; stopping the wrong process (reused pid, ancestor, unrelated tree) would be worse, so every stop is verified.
- nearest cards: A14, B14, B2, B5, C1-5
- rows not-found: FH-1002, FH-4054, FH-4142, FH-5115, FH-5116, FH-5117, FH-5118, FH-5119, FH-5120, FH-5121, FH-5122, FH-5123, FH-5124, FH-5125, FH-5126, FH-5127, FH-5128, FH-5129, FH-5130, FH-5131
- verdict: dropped -- no reaper tool: stopping process trees is the riskiest code of the old forge and the host now refuses an unbounded foreground wait itself; the lesson stays as one rule line (C1-1): a wait has a cap and a named condition
- decider: architect 2026-11-26

## H8 Dispatch gate: manifest, handoff, paths and worktree checks

- statement: Before a dispatch goes out, the gate checks its handoff folder and file, facts header, given and owns paths, label and role file, dry-runs the journal line, logs the verdict, and warns on stale anchors and a worktree cut from an old origin.
- what it was for: Reports were written where nobody reads and worktree workers lacked unpushed commits; each refusal carries an informed-pass line, and an unknown read goes out with a note rather than a block.
- nearest cards: B13, B14, B2, B5, B8, C1-1, C1-4
- rows not-found: FH-6040, FH-6041, FH-6042, FH-6043, FH-6044, FH-6045, FH-6046, FH-6047, FH-6048, FH-6054, FH-6055, FH-6056, FH-6057, FH-6058, FH-6059, FH-6060, FH-6062, FH-6063, FH-6064, FH-6065
- verdict: split -- carry (B18, amends C1-4's dispatch check): every given path exists, every owns path exists or is marked new; a rule line in B14: push before a worktree launch; dropped: the launch-time hook (F117 (a)), the label check, the journal dry run, the verdict log
- decider: architect 2026-11-26

## H9 Shell hygiene gate: directory moves, rollbacks, unbounded waits

- statement: A PreToolUse hook refuses moving the shell's directory, rolling back dirty changes (checkout, restore, reset --hard, clean, stash) and uncapped sleep loops (max 3600 s), names the door, and treats unmeasurable cases as visible passes.
- what it was for: The shell's cwd made cwd-reading gates judge the wrong tree, a rollback destroyed uncommitted work, polling loops hung sessions; pathological input must never widen a refusal, so doubt passes visibly (except the --run road).
- nearest cards: B14, C1-4, C1-5
- rows not-found: FH-6105, FH-6106, FH-6107, FH-6108, FH-6113, FH-6114, FH-6115, FH-6116, FH-6117, FH-6118, FH-6119, FH-6120, FH-6121, FH-6122, FH-6123, FH-6124, FH-6128, FH-6129
- verdict: split -- carry (B19, amends C1-5, the Architect's own decision): a rollback of uncommitted changes (checkout, restore, reset --hard, clean, stash) on a dirty tree is refused with its door (a byte copy, or commit first), because with several sessions in one checkout (B14) it destroys another session's work and cannot be undone; dropped: the directory-move refusal (forge 2 tools take the root as an argument and read nothing by cwd) and the wait-loop refusal (H7)
- decider: architect 2026-11-26

## H10 Baseline ratchets: lint, duplication and night CRAP

- statement: Lint and clone findings are identified without line numbers and compared to a committed baseline that only shrinks, with exit 2 for a different tool version or basis; the night's CRAP verdict is read from an artifact.
- what it was for: An edit above a finding must not read as a new finding, and a version drift must not read as new findings; stale or diverged rows turn visible instead of silently shrinking.
- nearest cards: C1-3
- rows not-found: FH-2017, FH-2019, FH-2023, FH-2024, FH-2026, FH-2027, FH-2028, FH-2097, FH-2098, FH-2099, FH-4130, FH-6072, FH-6076, FH-6079, FH-6081, FH-6082, FH-6083, FH-6085
- verdict: carry -- B20, amends C1-3 (which already holds the CRAP, lint and clone ratchets): a finding's identity carries no line number, so an edit above it is not a new finding; a different tool version or basis is cannot-judge, never new findings; a stale baseline row is shown, never silently shrunk
- decider: architect 2026-11-26

## H11 Automatic journal lines from hooks

- statement: Hooks write delegated, returned and resumed lines from the dispatch itself (model from the role binding, feature, node, attempt, replaces-worker, designer skip), with an index and pending markers, pruned by age.
- what it was for: The Lead's memory lost lines and hand-written ones carried guessed models; the hook writes only what it read, and a stop that precedes its launch is recorded later through a marker.
- nearest cards: B12, B13, B14, B2, B5, B9, C1-4
- rows not-found: FH-4052, FH-4122, FH-4123, FH-5059, FH-5061, FH-5062, FH-5063, FH-5064, FH-5065, FH-5066, FH-5067, FH-5069, FH-5070, FH-5071, FH-5073, FH-5074, FH-5079
- verdict: work-list -- forge 2 writes dispatch and return lines by the Lead's call of the journal tool (B2), and an open dispatch with no return is shown by the journal's open read and by the snapshot; automatic lines from a hook are a work-list record, promoted by the first lost line the open read catches
- decider: architect 2026-11-26

## H12 Mechanism gate: axis lines and tier declaration

- statement: A commit staging a mechanism path must carry an axis line for every axis of the sibling map plus a tier line at the Lead binding, with the one waiver axes: not a mechanism, and a --list and --audit reader for the Architect.
- what it was for: Mechanism edits skipped the sibling check and a bare skip let a builder commit (FG7-72); the net follows the live wiring's import closure, and truth of the declaration is judged by calibration.
- nearest cards: C1-1, C1-5, C1-7
- rows not-found: FH-3063, FH-3064, FH-3065, FH-3066, FH-3067, FH-3068, FH-3069, FH-3070, FH-3071, FH-3072, FH-3073, FH-3074, FH-3075, FH-3076, FH-3077, FH-3078, FH-4002
- verdict: dropped -- no axis lines and no tier line on a commit (one developer; the symmetry map starts empty, C1-7); the purpose is reached by B6's change-loop step (similar places and friction) and B16's cost of any mechanism
- decider: architect 2026-11-26

## H13 Compact snapshot and its session-start announcement

- statement: A hook writes a compaction snapshot (capped lists, git facts under one deadline, unknown never zero) and the next session start announces each once, with a missing-snapshot door, retention of committed old ones and a narrative stamp.
- what it was for: A compaction lost the Lead's working state; the snapshot must be written before slow steps, never overwritten, and an uncollected fact shown as ? so it never looks like zero.
- nearest cards: B14, B2, C1-4
- rows not-found: FH-2049, FH-2050, FH-2051, FH-2054, FH-2055, FH-2056, FH-2057, FH-2058, FH-2059, FH-2060, FH-2063, FH-2064, FH-2066, FH-4155, FH-4156, FH-4157, FH-4159
- verdict: carry -- B17, amends C1-4's snapshot tool and B2: session start names the newest snapshot and its age; a fact that could not be collected is printed as ? and never as zero; a snapshot is never overwritten; dropped: retention rules and the narrative stamp
- decider: architect 2026-11-26

## H14 Stop gate: edits need a green verification run

- statement: A Stop hook blocks a worker, or the main thread, that edited files and has no green verification run after the last edit, judging only its own records, doc-only edits exempt, gate warnings sent to warn.log.
- what it was for: Work was returned unverified; a resubmission must repeat the path and digest whole because only the last message reaches the coordinator, and a stop's stderr reaches nobody so warnings go to a file the Lead reads.
- nearest cards: B2, B5, C1-1, C1-5, C4-5
- rows not-found: FH-4034, FH-4035, FH-4036, FH-4037, FH-4038, FH-4039, FH-4040, FH-4051, FH-4053, FH-4055, FH-4057, FH-6133, FH-6134, FH-6135, FH-6136, FH-6141
- verdict: work-list -- no Stop hook now: forge 2 checks the outcome, not the moment -- the acceptor runs the DoD command itself at acceptance (the witness of H6) and main takes only a green CI (B8); the price is one reject round when a worker returns red; the Stop gate is a work-list record, promoted when the journal shows rejects whose cause is a return without a green run
- decider: architect 2026-11-26

## H15 CI reader CLI

- statement: A CLI reads or starts GitHub Actions runs in a few lines (pipelines, jobs, log, artifact, why, start) with caps on pages, artifact bytes, shown jobs and lines, strict argument checks, and a token sent only in an unredirected header.
- what it was for: Reading CI logs by hand flooded context and a token carried by a redirect would leak; remote text is sanitised and only github.com origins are read.
- nearest cards: B8, C1-6
- rows not-found: FH-2067, FH-2068, FH-2070, FH-2071, FH-2072, FH-2073, FH-2074, FH-2075, FH-2076, FH-2077, FH-2078, FH-2079, FH-2080, FH-2081, FH-2082, FH-2101
- verdict: carried-differently -- reading a red CI run is the host's own command piped through the trim tool (C1-4), one rule line with its case (CI logs flooded the context) in B21; the reader CLI is not rebuilt; its token rule (a token is sent only in an unredirected header) goes into the same rule line
- decider: architect 2026-11-26

## H16 Architecture and judgment lines of a package commit

- statement: A commit staging package paths must carry an architecture line (AR ids from the index or none with a reason) and a judgment line of four closed forms, checked against a census ratchet, refusing once with all problems named.
- what it was for: Package changes broke invariants unnoticed; none is counted at calibration so the reason must be real, and an unreadable census is never a pass (AR-28).
- nearest cards: C1-1, C1-2, C1-3, C1-5, C1-7
- rows not-found: FH-3001, FH-3002, FH-3003, FH-3004, FH-3005, FH-3006, FH-3007, FH-3008, FH-3009, FH-3010, FH-3011, FH-3012, FH-3013, FH-3014, FH-4003, FH-4004
- verdict: dropped -- these are lines of a package commit and forge 2 holds no package code (C1-7); the factory code of forge 2 names its card in every file (B13) and its invariants are the spec's frame
- decider: architect 2026-11-26

## H17 Coordinator rule files: read check and session-start line

- statement: At session start the coordinator gets a line naming its rule files, and at dispatch, verdict and commit a warning names any file not Read in full since the last start, compaction or clear.
- what it was for: A coordinator working on rules it had not read in this context broke them; the check errs toward cannot-judge never unread, and a space or non-ASCII root once printed a door nobody could run (t-1250 F3).
- nearest cards: A18, B2, C1-1
- rows not-found: FH-1006, FH-1007, FH-1010, FH-1011, FH-1013, FH-1014, FH-1015, FH-1016, FH-1017, FH-1018, FH-1019, FH-4151, FH-6066, FH-6127
- verdict: carried-differently -- forge 2 prints the rules a session needs whole into its context at start, clear and compaction (B1 boot page by B2's hook), so a rule file not read cannot happen for them; carry (B17, amends B2): the same print on resume
- decider: architect 2026-11-26

## H18 Report-only workers: handoff gate and owns check at stop

- statement: A critic or designer may write only the one file named on its handoff line, a stopping worker is blocked once if the handoff is missing or changed paths lie outside its owns, with an owns-skip line, and unknowns never refuse.
- what it was for: A reviewer edited product files or its report was lost; the unknown of a gated worker is never a pass, while at stop an unknown is shown as not judged, never as checked.
- nearest cards: B5, C1-1, C1-4, C1-5
- rows not-found: FH-3021, FH-3022, FH-3023, FH-3025, FH-3027, FH-3028, FH-3030, FH-3032, FH-4044, FH-4045, FH-4046, FH-4047, FH-4048, FH-4049
- verdict: carried-differently -- B21: owns is judged at acceptance by the diff (one command named on the boot page), and a critic or designer returns its verdict in the one handoff file, both as rule lines with their cases; a stop-time owns check goes with H14 to the work list; the write-restricting hook for report-only workers is dropped
- decider: architect 2026-11-26

## H19 Escape allowlist and pinned judge prompt/role

- statement: A checker pins each permanent escape or concession clause to its carrier anchor and the sha256 of its decision section, and pins the judge prompt and role-file blocks byte for byte, failing closed at commit.
- what it was for: A concession clause could drift from the owner's recorded decision unnoticed; CRLF hashes the same as LF, and a pinned constant is read by the AST, never by importing repo code from a gate.
- nearest cards: B3, C1-1
- rows not-found: FH-6006, FH-6086, FH-6087, FH-6093, FH-6094, FH-6095, FH-6096, FH-6097, FH-6098, FH-6099, FH-6100, FH-6101, FH-6102, FH-6104
- verdict: split -- carried-differently: a concession clause is tied to the owner's recorded word by B3's append-only registry (a missing id is refused); dropped: the judge prompt and role-file pins (forge 2 has no judge)
- decider: architect 2026-11-26

## H20 Main-red tracking at session start

- statement: main's CI state (red, pending, unknown) is read from a lock-protected state file, refreshed detached and rate-limited, shown as one MAIN RED line at session start, with a single fixer slot and a queue of known-flaky ids.
- what it was for: A red main went unnoticed or two workers fixed it at once; cancelled runs are not red, a corrupt state file starts fresh and never reads as green, and unknown is its own state.
- nearest cards: B2, B8, C1-6
- rows not-found: FH-2083, FH-2084, FH-2085, FH-2087, FH-2088, FH-2089, FH-2090, FH-2091, FH-2092, FH-2093, FH-2094, FH-2095, FH-2096, FH-4129
- verdict: carried-differently -- main cannot go red by a push: B8 protects it and requires the green row, so tracking a red main, the fixer slot and the flaky queue have nothing to track; a test that fails only under load is a defect of the test (one rule line, B21)
- decider: architect 2026-11-26

## H21 Language sites ratchet with owner's word

- statement: A baseline of language sites with mechanism codes only shrinks: a raise needs a quote of the owner's word found in a tracked file, stale rows are refused, a dead scanner is cannot-judge, and the budget is global per token.
- what it was for: A raise written by a command is the cheap way past the ratchet; the owner's words, not a script, open the road.
- nearest cards: B3, C1-2, C1-3
- rows not-found: FH-4082, FH-4084, FH-4086, FH-4087, FH-4089, FH-4090, FH-4093, FH-4094, FH-4095, FH-4096, FH-4098, FH-4099, FH-4100
- verdict: carry -- B20, amends C1-2 and C1-3: a ratchet raise names a record of the owner-words registry (B3), never a bare command; a stale allow row is refused; a scanner that could not run is cannot-judge and never green
- decider: architect 2026-11-26

## H22 Journal files, task ids and per-developer segments

- statement: Journal file names, successor chains, merged read order, task id spelling and the id-jump limit are enforced, a developer file freezes the old history, and a segment declaration separates colliding ids of two clones.
- what it was for: Several clones write one journal; without name, id and order rules a collision read as one task, history was rewritten, or a lookalike id (fullwidth digits, Cyrillic) passed as real.
- nearest cards: B14, B2, C1-4, C1-6
- rows not-found: FH-1024, FH-1027, FH-1029, FH-1030, FH-1032, FH-2114, FH-2137, FH-2138, FH-2140, FH-2141, FH-2143, FH-4125
- verdict: dropped -- clone letters, segments and per-developer files answer several clones of several developers; forge 2 is one developer (F109 (a), the owner's word) with a journal file per session (B14); an ASCII-only id pattern belongs to C1-4's journal tool
- decider: architect 2026-11-26

## H23 Journal task lifecycle and escalation counting

- statement: Duplicate dispatch, reopening a closed task, a return or resume without its worker round are refused, and rejects are counted per task and tier family so the escalated line is owed at the second reject (third when converging).
- what it was for: Rule 6 escalation depends on a true count of rejects per tier; a double dispatch, a collision counting as two tasks or a model alias splitting one tier would hide or fake a retry.
- nearest cards: B14, B2, C1-1, C1-4
- rows not-found: FH-1038, FH-1039, FH-2115, FH-2116, FH-2117, FH-2119, FH-2120, FH-2142, FH-3051, FH-3052
- verdict: carry -- B18, amends C1-4: the journal's open read shows the count of rejects per task; the rule that a second reject of one task moves it one tier up is a rule line (C1-1); dropped: the refusals of a duplicate dispatch and of a reopened task (B14 names a collision and counts two tasks)
- decider: architect 2026-11-26

## H24 Journal echo: immediate feedback on a written line

- statement: After each journal write a PostToolUse hook echoes defects in the new lines, append-only breaks, and the layered notes (limits per layer, fixed order, one JSON context), with a HEAD-diff fallback and silence when clean.
- what it was for: A bad journal line was found only at commit; feedback in the same turn lets the author fix it at once, and the caps stop a whole-file base from flooding the session.
- nearest cards: B14, B2, C1-4, C1-5
- rows not-found: FH-3034, FH-3036, FH-3037, FH-3039, FH-3044, FH-3054, FH-3059, FH-3060, FH-3061, FH-3062
- verdict: dropped -- the one writer validates before it writes (C1-4), so feedback comes in the same call and a PostToolUse echo has nothing to add
- decider: architect 2026-11-26

## H25 Recognising edits and verification runs in the track

- statement: A PostToolUse hook records each edit (four tools) and each verification run (pytest, python test, node, UI witness words) per agent in a track file, stripping zero counters and ignoring scratchpad paths and journal-writer calls.
- what it was for: The stop gates need an exact record of what was edited and what ran green; '0 failed' read as failure, or the journal writer read as a test, gave wrong verdicts.
- nearest cards: C1-4, C1-5, C4-4, C4-5
- rows not-found: FH-4058, FH-4059, FH-4060, FH-4061, FH-4062, FH-4063, FH-4066, FH-4067, FH-4068, FH-4069
- verdict: dropped -- the track exists only for the Stop gate (H14) and goes with it
- decider: architect 2026-11-26

## H26 Critic verdict file shape

- statement: A critic's verdict is a fenced json block with a closed verdict word, fields, a trail of reads and reruns, at most 3 mutants with length limits and an unmutated control rerun for each kill, in ASCII diagnostics that never echo raw input.
- what it was for: A critic verdict that could not show what it read, reran and killed was prose, not evidence; a value holding a fence was once misread.
- nearest cards: A13, C4-2
- rows not-found: FH-4019, FH-4020, FH-4021, FH-4022, FH-4023, FH-4024, FH-4025, FH-4026, FH-4031, FH-4033
- verdict: carried-differently -- B21: a critic's verdict is a file with one closed-word line per reviewed thing, a trail of what was read and rerun, and probes made on copies with an unmutated control run, as rule lines of the critic's dispatch; the fenced JSON shape and its checker are dropped (the grep of the verdict lines is the DoD)
- decider: architect 2026-11-26

## H27 Echo of tier mismatch, witness against track, and critic input

- statement: On a new accepted line the echo compares the declared tier with the models in the worker transcript, the witness text with the DoD track (red, stale after a code edit), and warns R3 MIRROR when no critic input stands under the task.
- what it was for: Self-certification and untrue witnesses: a builder acceptance without a critic, a witness citing a command whose latest run was red, or code edited after the last green run.
- nearest cards: B5, C0-4, C1-1, C1-4, C4-2
- rows not-found: FH-3042, FH-3043, FH-3045, FH-3046, FH-3047, FH-3048, FH-3055, FH-3056, FH-3057
- verdict: split -- carried-differently: the witness is the acceptor's own run (H6), so it cannot cite a stale or red run; one rule line (B21): acceptance comes from above the performer or with a critic's input; dropped: the tier-mismatch measurement from transcripts
- decider: architect 2026-11-26

## H28 Stop-gate safety valve and break-glass record

- statement: The third consecutive violating stop is allowed with a loud line and an appended unsafe_completions record, counters are per worker and separate for the main gate, and session start prints each unacknowledged break-glass once.
- what it was for: A gate that can never be passed deadlocks work; the valve opens but leaves a fact that a later session must see and acknowledge, and one worker's spent valve must not excuse another's first block.
- nearest cards: B2, B5, C1-5
- rows not-found: FH-4041, FH-4042, FH-4043, FH-4139, FH-4140, FH-4141, FH-6138, FH-6139, FH-6140
- verdict: dropped -- with no Stop gate there is nothing to deadlock; the lesson is kept as the frame rule that every refusal names a door the refused party can use
- decider: architect 2026-11-26

## H29 Merge-time journal validation

- statement: A pre-merge-commit hook validates only the journal lines the other clone brought, with the merged parent found from GITHEAD, and a refused merge is cleared by an appended merge-accepts or order-known line.
- what it was for: Journal files merge by union and never conflict, so a bad foreign line arrived unchecked; the merge stays in progress and the person concludes it with git commit after the clearing line.
- nearest cards: B14, C1-4, C1-5
- rows not-found: FH-2132, FH-2133, FH-2134, FH-2135, FH-5002, FH-5003, FH-5004, FH-5005
- verdict: dropped -- spec part 5 says on purpose that the journal's merge validator is not carried (one developer; sessions of one checkout do not merge journals); decider: spec part 5
- decider: architect 2026-11-26

## H30 Document pointer and number lint

- statement: Backticked paths, range claims (FR-1..FR-N), section anchors and numbers written in documents are checked against tracked files, headings and constants read from code, and an exemption that suppressed nothing is itself red.
- what it was for: Rule texts pointed at files and counts that no longer existed; exemptions must not rot into silent holes.
- nearest cards: B13, C1-1, C1-2
- rows not-found: FH-1055, FH-1057, FH-1058, FH-1059, FH-1061, FH-1063, FH-1064, FH-6013
- verdict: split -- carry (B20, amends B13's reference check): a path written in the boot page and the forge rule files names an existing file; an exemption that suppressed nothing is red (the same rule for every allow list, H21); work-list: the number-pair check of documents against constants
- decider: architect 2026-11-26

## H31 Session-start status lines of other machinery

- statement: Session start prints lines for calibration overdue, test quarantine, quota use, boot size (top files and imports), a closed Layer A block with transliteration, and an architect session note.
- what it was for: The Lead must see these states without asking; truncated injection and meaning lost in transliteration are made visible.
- nearest cards: B12, B2, B9, C1-2, C1-6, C1-7, C4-6
- rows not-found: FH-4113, FH-4127, FH-4128, FH-4131, FH-4134, FH-4136, FH-4146, FH-4150
- verdict: dropped -- these lines report machinery forge 2 does not carry (calibration, test quarantine, quota, Layer A); boot size is C1-2's byte budget in CI
- decider: architect 2026-11-26

## H32 Session-start context basics

- statement: Session start prints single-line ASCII facts: the local clock, the harness-declared model, the last journal event, open degradation windows, clock drift and a settings model pin warning, fast and without network.
- what it was for: A session must not trust a narrated timestamp or a model name it only believes, and a slow or networked hook would delay every start.
- nearest cards: A13, B14, B2, C4-5
- rows not-found: FH-1041, FH-4107, FH-4108, FH-4111, FH-4112, FH-4114, FH-4115, FH-4119
- verdict: carry -- B17, amends B2: session start prints the local clock and the last journal event in one line, with no network and under the deadline of H3; dropped: the model pin, degradation windows and clock-drift lines
- decider: architect 2026-11-26

## H33 Credit for edits restored to the last green bytes

- statement: A green run stores per-agent digests of every edited file, and an edit after green earns credit when the file again holds those bytes and git state, within size, path and time budgets, so a restored probe needs no new run.
- what it was for: A probe corrupted and restored by byte copy would otherwise force a pointless second run; the digest time is stamped after capture so a parallel edit never reads as after-green.
- nearest cards: C1-5, C4-2, C4-4
- rows not-found: FH-4050, FH-4071, FH-4072, FH-4073, FH-4074, FH-4075, FH-6137
- verdict: dropped -- the credit for restored bytes exists only for the Stop gate (H14) and goes with it
- decider: architect 2026-11-26

## H34 Git hook gate runner behaviour

- statement: The commit-msg and pre-commit hooks run gates in a fixed order, stop at the first refusal with that gate's own exit code, print one gates: ok line on success and show any WARN whole, naming a check that did not run.
- what it was for: A later passing gate must not mask a refusal, and a crashed warner must not be counted as ok; short output keeps the happy path cheap.
- nearest cards: B11, C1-5
- rows not-found: FH-4001, FH-4008, FH-4009, FH-6001, FH-6002, FH-6003, FH-6016
- verdict: carry -- B17, amends C1-5's git hooks: steps run in a fixed order and stop at the first refusal with that step's exit code; success is one ok line; a step that did not run is named and never counted as ok
- decider: architect 2026-11-26

## H35 Who may accept or reject: acceptance matrix and worker verdict ban

- statement: An accepted line is legal only by a role-versus-tier matrix, basis judge is refused, a second accept by the same agent is refused, and a worker may never run the journal writer with accept or reject.
- what it was for: A worker or a lower tier certified its own or a peer's work; acceptance belongs to the coordinator tier, and the worker's verdict goes in its handoff file.
- nearest cards: B2, C1-1, C1-4
- rows not-found: FH-2123, FH-2124, FH-2125, FH-6005, FH-6111, FH-6112
- verdict: carry -- B18, amends C1-4: the dispatch text printed for a worker says it never writes accept or reject and returns its verdict in its handoff; acceptance belongs to the Lead (one rule line, C1-1); dropped: the role-versus-tier matrix as code
- decider: architect 2026-11-26

## H36 Parallel writer cap and overlapping owns

- statement: A writing dispatch is refused when 6 or more unfinished writer transcripts changed in the last 10 minutes, an unreadable transcript counts as live, budget-skip passes it, and two dispatches owning one path are flagged by code.
- what it was for: Too many concurrent writers collided on files and exhausted the machine; an unknown must never let a seventh through, and overlap was left to the Lead's memory.
- nearest cards: B14, B5, C1-4
- rows not-found: FH-1076, FH-6049, FH-6050, FH-6051, FH-6052, FH-6053
- verdict: split -- carry (B18, amends C1-4's dispatch check): an owns path held by an open dispatch of the journal is flagged; dropped: the cap of six writers (a tempo rule of the old forge; B5 caps each worker)
- decider: architect 2026-11-26

## H37 Test volume warning

- statement: A commit-msg step sums staged added lines per class and warns once when test lines exceed product lines, silenced by a tests-over line with a reason, never blocking and silent on merges and equal counts.
- what it was for: Test mass grew past the code it checks; the door needs a stated reason and, being a warning, the step shows whole at commit time.
- nearest cards: C1-5, C1-6
- rows not-found: FH-2002, FH-2003, FH-2004, FH-2005, FH-2006, FH-4007
- verdict: carried-differently -- B20: the ratio of test lines to product lines is one figure of C1-2's size counters, shown and never blocking
- decider: architect 2026-11-26

## H38 Close, commit-door and push guards

- statement: A push to github.com is refused when an old root commit is an ancestor, door lines in commit messages are read only in prose position (also from a CI range), and a multi-file write is all or nothing.
- what it was for: The old repository's history must never reach the public remote; an SSH alias hides it, a half-applied write left files inconsistent, and a door quoted in a fence is not a door.
- nearest cards: B11, B8, C1-1, C1-2, C1-4, C1-5, C1-7
- rows not-found: FH-1004, FH-1005, FH-1070, FH-1071, FH-1104, FH-1105
- verdict: split -- carry (B19, amends C1-5's push hook, the Architect's own decision): a push of a ref under local/ and of any history holding a root commit of the old forge is refused -- publication cannot be undone; dropped: door lines read only in prose position and the all-or-nothing multi-file write (no forge 2 tool writes several files)
- decider: architect 2026-11-26

## H39 Refusing hand-written journal writes

- statement: A shell or editor write of a journal file is detected (redirect, tee, in-place editors, python payload, Write or Edit in any worktree) and refused or warned, naming the journal writer tool as the door; reading is never refused.
- what it was for: Hand-edited journal lines bypassed validation; the edit tool warns first with a constant that switches to refusal, the shell form is refused outright.
- nearest cards: C1-4, C1-5
- rows not-found: FH-5075, FH-5076, FH-6109, FH-6110
- verdict: work-list -- the journal has one writer and its merged read names an unparsable line (C1-4); a hook refusing a hand edit of a journal file is a work-list record, promoted by the first hand-edited line the read catches
- decider: architect 2026-11-26

## H40 Agent budget warnings

- statement: A budget hook warns at 10 test runs and every 5 more (one witness run per round), tells the Lead to write the compact snapshot, passes a plain git stash as a close-out move, and reuses the last usage when the last line is long.
- what it was for: Workers burned context re-running tests; the context size must never read unknown for want of a short last line.
- nearest cards: B5, C1-4
- rows not-found: FH-6026, FH-6030, FH-6031, FH-6035
- verdict: carry -- B18, amends C1-4: the dispatch text says the verification run is made once, after the last edit; the test-run counter and its warning are dropped (B5 caps the worker)
- decider: architect 2026-11-26
