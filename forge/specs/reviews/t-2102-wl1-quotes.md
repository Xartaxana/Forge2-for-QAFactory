# t-2102 critic verdict: wl-1 carry-ledger quotes (diff 30f326a..9800b88)

verdict: fit_with_fixes -- 374/374 quotes byte-exact on their line, 0 status cells changed; 8 quotes carry a different clause of a long line than the row's rule (fixes F1-F8), FR-1118 carries the inverted rule (node N1)
blocking findings: 0

## Verdict lines
- mechanical (quote on line N at 30f326a, status cells): fit -- quotes 374, on their line 374, not 0; status cells changed 0; no column but `note` changed; every changed row `carried`; every quote <= 200 chars; each note keeps its `restored wave N` tail (374/374)
- not-found rows (FO-47, FO-48, FO-51, FO-74, FO-1089, FO-1105, FO-1121, FR-63): fit -- unchanged, and exactly these 8 still hold `candidate drop` in the six ledgers (scan below)
- builder-flagged weak quotes: fit_with_fixes -- FO-8, FO-1078, FO-2046, FR-1034, FR-1065, FR-2026 carry the rule; FO-1111 carries half (F10); FO-2017/FO-2060 share a line that holds both halves (fit); FR-1118 carries the opposite rule (N1)
- unflagged quotes (meaning sweep over all 374): fit_with_fixes -- 8 rows quote a different clause of the same line (F1-F8); 5 are cut before the rule's object (F9)
- tests: none -- data-only diff, no behaviour, no test file touched
- DUPLICATION AND CONSISTENCY: none found -- data-only diff; no reader/writer/helper added (diff --stat: 6 ledger .md files only)
- CODE QUALITY: none found -- no code in the diff
- one road: none -- no shared mechanism touched (ledger cells only)
- VARIETY / architecture: none -- no AR-n touched; no producer or reader changed
- class completeness: the mis-windowed-quote class walked over all 374 rows by a word-overlap scan (rule text vs quote vs whole line), 47 candidates read by hand; shared-quote class walked over all 21 groups; partial-carry axis noted (seam notes)
- probe: none -- data-only gate, no new behaviour to mutate

## Findings
Severity: none blocks the merge (the base note of each row was `candidate drop: none found`, worse than any new quote; the diff regresses no row). F1-F10 are fixes of THIS round (one data-only fix pass, same owns).

F1. forge/specs/recon/carry/forge-rules.*.md row FR-1073 -- quote `forge/COORDINATOR.md:80 "Fix the class: FIRST apply the class to every neighbour..."` is the neighbour-sweep clause; the rule is the sweep UNIT. Line 80 holds it: re-window to `"The sweep unit is the enclosing structural block, widening to the whole file only when the move already read it; opening a file specially for the sweep is forbidden"`. blocks: no.
F2. row FR-1074 -- same quote as FR-1073 (a shared quote the builder did not flag); the rule is the ENUMERATION. Re-window to `"The sweep is an ENUMERATION with a verdict per neighbour (applied / not applicable and why / moved, with its id)"`. blocks: no.
F3. row FR-120 -- quote `factory/RULES.md:12 "When the factory cannot cope ... through one seam ... (P22)"` is the seam rule (that is FR-191/FR-225's); FR-120 is "called for a problem, never to run a command, settles it before asking". Re-window to `"called for a problem and never to run a command (P3)"` (+ optional `"it settles the problem itself before it asks a person"`). blocks: no.
F4. forge-roles row FO-147 -- quote `.claude/agents/critic.md:66 "The probe breaks 1 to 3 load-bearing places ... hard cap of 3 mutant runs per verdict"` is FO-69/FR-1034's clause; FO-147 is the tree timing. Re-window to `"only after the builder handed back; no fix round, merge or worktree removal starts in it until the verdict returns"`. blocks: no.
F5. row FR-33 -- quote `forge/COORDINATOR.md:170 "Before sending, the dispatcher runs the five-point checklist: (1) ... (2) ..."` is points 1-2; FR-33 is the miss-is-a-spec-defect rule. Re-window to `"A checklist miss exposed by a reject or a finding is a spec defect of the dispatcher (a calibration case); promotion to a machine layer follows the next recurrence."`. blocks: no.
F6. row FR-32 -- same quote as FR-33; FR-32 is point (5). Re-window to `"(5) freshness: the spec's load-bearing facts are checked against their carrier, not memory."`. blocks: no.
F7. row FR-1139 -- quote `forge/COORDINATOR.md:129 "A calibration overdue ... in the boot report"` is FR-1133's rule (identical quote); FR-1139 is "told to the owner once per session with one item" (+ Lead-class work queued). Re-window to `"the Lead tells the owner once per session and opens one `--for architect` record if none is open"`; the queue half is `forge/COORDINATOR.md:37 "Lead-class work is queued for the Lead as a work-list record"`. blocks: no.
F8. row FR-2079 -- quote `forge/COORDINATOR.md:106 "... the session root is the"` stops before the rule (the next token is an inner `"`). Re-window to `"of the environment block and only it (one look before the first link; in doubt, a path with no repo prefix"`. blocks: no.
F9. weak, cut before the rule's object, line holds it (optional in the same pass): FR-190 and FR-256 (`factory/RULES.md:16 ... goes through the` -> `"goes through the factory's one question form (P9)"`); FO-2034 (`designer.md:37`, the "always four lines" half is past the window -> `"It is always four lines: `report: <path>`"`); FO-2066 (`designer.md:45` cut at "or the owner's" -> `"or the owner's word, quoted with its carrier beside the line."`); FR-1140 (`COORDINATOR.md:37` first 200 chars; the mid-tier half -> `"a session below lead (mid-tier mode) runs the same acceptance rules"`). blocks: no.
F10. forge-roles row FO-1111 (builder-flagged) -- `scout.md:15 "The digest ends with `Not done`..."` carries the `## Not done` half only; the Forks half has a carrier at `.claude/agents/scout.md:9 "a fork is reported as a fork, never closed by a recommendation"`: add it as a second quote. blocks: no.

N1 (proposed node, id to be assigned by the Lead; owner: the Lead, the ledger status is a Lead change and this DoD forbids status edits). Row FR-1118 (forge-rules) -- old rule "`ts` is local time with NO zone suffix; a trailing `Z` fails the gate"; the quote `forge/COORDINATOR.md:128 "`ts` is ISO 8601 UTC with a trailing `Z`..."` is the inverted rule, and the same line calls the old form a defect ("the old forge's local time with no zone included"). The rule is replaced, not carried: verdict `carried` -> `carried-differently` (or `dropped` with the replacing line as carrier). The builder's flag is correct; the quote itself stays (it is the right evidence for the new verdict).

## Judgment of the builder's flags
- FO-8 `critic.md:27 "I don't like it"`: the line reads `"I don't like it" is not a finding`; the quote form cannot hold the inner `"`, line 27 holds the predicate right after it. Carries; fit.
- FO-1078 `builder.md:41`: "when your change alters a file's interface, find its readers yourself" -- the duty survives with a hand search in place of `owns_readers.py`. Carries; fit.
- FO-2046 `COORDINATOR.md:65`: readers of every touched file and changed name, by a hand search; the line goes on "with its command and hit count" (the counts). The function of the tool is carried; fit.
- FR-1034 `critic.md:66`: holds all three (runner, cap of 3, Bash only). Not weak; fit.
- FR-1065 `COORDINATOR.md:78`: "justifies self-execution only on the FIRST such move in a session" is the rule's core; the subject sits behind an inner `"`. Carries; fit.
- FR-2026 `COORDINATOR.md:71`: the detector clause exactly; the cost clause is on the same line. Carries; fit (`rejected` -> forge 2's `reject` is the journal kind rename).
- FO-2017 / FO-2060 `designer.md:18`: one line holds both "the owner it serves" (FO-2060) and "and its class: shape, xref, presence (data)," (FO-2017); sharing is legitimate. Fit.
- FO-1111: F10. FR-1118: N1.

## Seam and class notes
- Class of F1-F8: the builder took the first <= 200 chars of a long line (or stopped at an inner `"`), so the quote proves the line, not the rule. All 374 rows were scanned for it (window.py below); 34 scan hits plus 13 low-overlap rows were read by hand; F1-F9 are every hit judged wrong or weak. Scan limit: a word-overlap scan misses a mis-window whose wrong clause shares the rule's words; residual risk, not a known instance.
- Shared quotes (21 groups): all hold both rules on the quoted window except FR-1073/FR-1074 (F1/F2), FR-32/FR-33 (F5/F6); FR-1133/FR-1139 (F7) is a non-flagged duplicate of the same kind.
- Partial carry (not a quote defect, a status question for the Lead's next ledger pass): FO-168 lists 8 answer forms, `critic.md:91` holds 4 (absent, exists, names, unsearched; quarantined, slow, hot, more are gone) -- same class as N1 (a `carried` verdict wider than its carrier); FR-1128 (`by` as family word through FAMILIES) is carried only as "read as a rank".
- The 8 not-found rows remain `carried` with a `candidate drop` note: a `carried` verdict with no carrier quote. Out of this DoD (status cells unchanged); the Lead's open wl item holds them.

## Spot-checks
- Mechanical script, positive control: same script with every line number shifted by +1 prints `on their line: 0 not: 374` (the check can fail).
- Not-found scan: positive control is the same scan finding the 8 named ids (it printed exactly them).
- Status cell: column 6 (`verdict`) per the header `| id | source | section | kind | what | verdict | where | proof | note | ...`.
- Tree: `git -C C:/QAFactory/forge2-wt/t-2102 status --porcelain` empty; HEAD 9800b88.

## Trail
- Read: forge-roles.1.md header (lines 1-19); diff 30f326a..9800b88 (stat + head); rule lines at 30f326a: critic.md 13, 27, 34, 56, 66, 91; scout.md 9, 12, 15; builder.md 41; designer.md 18, 37, 45, 46, 51-58; COORDINATOR.md 19, 21, 34, 37, 47, 65, 71, 78, 80, 99, 106, 115, 128, 129, 170, 174, 175; factory/RULES.md 3, 11, 12, 16, 41, 44, 96.
- Scripts (scratchpad C:/Users/i_mas/AppData/Local/Temp/claude/57a17d91168f4ad2/90d4afc4-2c4f-4694-a38b-df8f4ac34380/scratchpad/): check_quotes.py (parses every added `path:N "quote"` in the note cell of each `+|` row, checks it is a substring of line N of `git -C C:/QAFactory/forge2-repo show 30f326a:<path>`, compares every other cell with the `-|` row); ctl.py (line+1 control); tails2.py (note tail kept); window.py (rule/quote/line overlap); show.py.
- `python -B check_quotes.py` output, verbatim:
  `rows old/new: 374 374 keys equal: True`
  `changed rows: 374`
  `quotes: 374 on their line: 374 not: 0`
  `status cells changed: 0 []`
  `rows with a column other than note changed: []`
  `changed rows not 'carried': []`
  `changed rows with no new quote: []`
  `quotes over 200 chars: []`
  then 21 shared-quote groups (listed in the class notes).
- `python -B ctl.py`: `quotes: 374 on their line: 0 not: 374`.
- `python -B tails2.py`: `374 (True, True, True, 1)` (old tail kept, `restored wave` kept, one quote per note).
- `python -B window.py`: `34` hits, first rows `(0.0, 0.95, 'FR-1073', 1733)`, `(0.05, 0.95, 'FR-1074', 1733)`, `(0.09, 1.0, 'FR-120', 2241)`, `(0.1, 0.85, 'FO-147', 827)`, `(0.12, 1.0, 'FR-33', 799)`.
- Not-found scan (python over carry/*.md, `candidate drop` in note or id in the 8): printed FO-47, FO-48, FO-51, FO-74, FO-1089, FO-1105, FO-1121, FR-63, nothing else.
