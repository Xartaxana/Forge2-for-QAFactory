<!-- scout hand-back, journal task t-1885, recon for docs/tasks/specs/20261125-forge2-light-factory-plan.md; saved verbatim from the worker's final message -->

digest: v1 t-1885
Read me first. AGENTS.md is a GENERATED host copy: lines 5-884 inline CLAUDE.md, COORDINATOR.md and PROJECT.md (a spot check, `converging` count 4 in both, shows no drift; not diffed byte for byte). It differs only in: the 3-line header (111147 bytes; Codex cuts at 32 KiB, raise `project_doc_max_bytes` to 114688), the generated indexes FR (59 rules), AR (29) and P1-P31 at lines 885-1041, and the Codex section at lines 1043-1088 (16 hooks, roles table, journal note). Row format: kind `A:` + outcome/means/knowledge = DoD section A. Owner cell = owner's word + date, as the document quotes it. B = role knowledge, C = machinery-only (`M` = restricts an agent's MEANS), D = growth guards, X = contradictions/duplicates (D2), E = open. Every `ev` tid is a Trail row below.

## Objects
| id | kind | gist | paths | status | owner | links | ev |
|---|---|---|---|---|---|---|---|
| A1 | A:outcome | Work is done only when the actual output of a named verification run proves it; a paraphrase never counts | COORDINATOR.md:86-93; CLAUDE.md:20-38 | — | — | C2 | t1,t30 |
| A2 | A:outcome | Every spec names its edges (limits, empty input, conflicting requirements) and the invariant each protects; silence is the dispatcher's defect | CLAUDE.md:20-38; .claude/agents/designer.md:16-37 | — | — | C2 | t30,t4 |
| A3 | A:outcome | Outside input gets adversarial cases (magnitude, nesting, encoding, empty) plus a case at and beyond every limit | CLAUDE.md rule 11 tests; .claude/agents/critic.md:241-268 | — | owner words 10.11 and 17.11.2026 | D8 | t30,t2 |
| A4 | A:outcome | A negative claim ("absent") counts only with a same-shape positive control, case-insensitive; empty output of a miscalled tool proves nothing | CLAUDE.md hygiene pt 6; .claude/agents/scout.md:35-53; critic.md:68-87 | — | — | — | t8,t9,t2 |
| A5 | A:outcome | A reviewer reproduces the submitter's load-bearing and negative claims itself; field semantics come from real data, not a neighbour's code | .claude/agents/critic.md:74-95 | — | — | B3 | t2 |
| A6 | A:outcome | Fix the class: siblings are fixed in the same round or named with an executor; workers report analogs without widening scope | COORDINATOR.md:225-242; scout.md:73-78; builder.md:60-65 | — | owner word 17.11.2026 | — | t1,t8,t3 |
| A7 | A:outcome | Acceptance comes only from a tier above (or with critic input); no session certifies its own work | COORDINATOR.md:420-457 | — | — | C13 | t1 |
| A8 | A:outcome | An underspecified requirement is asked of the operator, never decided by any tier; technical choices are decided and flagged «решила сама» | COORDINATOR.md:283-295; PROJECT.md:207-219 | — | — | — | t1,t5 |
| A9 | A:outcome | Large specs are drafted in an independent context; forks are returned, never decided; brief facts are measured by code first | COORDINATOR.md:95-114; designer.md:39-57 | — | owner word 17.11.2026 | B4 | t1,t4 |
| A10 | A:outcome | Big or risky diffs (over ~100 lines, schema, money) and forking plans get an independent review before acceptance | COORDINATOR.md:116-131 | — | — | B3 | t1 |
| A11 | A:outcome | Parallel writers own disjoint paths; a shared file has one writer; nobody commits another session's uncommitted paths | COORDINATOR.md:133-139; PROJECT.md:165-168 | — | — | — | t1,t5 |
| A12 | A:outcome | Workers never spawn workers; a decomposable task returns to the Lead | COORDINATOR.md:162-165; builder.md:29-34 | — | — | — | t1,t3 |
| A13 | A:outcome | Two failed attempts move the work one tier up; no silent retry on the same tier | COORDINATOR.md:167-192 | — | — | C5 | t1 |
| A14 | A:outcome | A mechanism ships with its compliance cost, a registered detector, and what stops it being skipped | COORDINATOR.md:244-267 | — | — | C8 | t1 |
| A15 | A:outcome | What code can do, code does (journal lines, dispatch headers, merges); the journal is append-only, accomplished facts, fixed by new lines | COORDINATOR.md:297-304,344-418 | — | «Номер 123 и 123А» 14.11.2026 (id letters) | C4 | t1 |
| A16 | A:outcome | A reading worker's LAST message is the whole self-contained report with its trail; "see above" loses it | scout.md:79-89; builder.md:71-98; critic.md:115-143; designer.md:66-91 | — | — | C16 | t9,t3,t2,t4 |
| A17 | A:outcome | Code that takes over a role's step is compared with the role's reference run; "less than the LLM" means stop | PROJECT.md:91-96 | — | — | — | t5 |
| A18 | A:outcome | A spec that changes a meaning has its data premise measured and its error direction written before code | PROJECT.md:97-106 | — | — | — | t5 |
| A19 | A:outcome | A role-behaviour fix is proved only by a live run of the role (FR-33) | PROJECT.md:88-90; AGENTS.md:954 | — | — | — | t5,t21 |
| A20 | A:outcome | Tests are few and strong: expected value traced to spec/rule/owner, able to fail, test lines not above code lines | critic.md:179-188,241-268; builder.md:99-118 | — | owner words 10.11, 17.11.2026 | D8 | t2,t3 |
| A21 | A:outcome | One action, one road: no language, project or case reaches a shared mechanism another way without a data row or the owner's word | critic.md:305-317; designer.md:92-106 | — | owner word 06.11.2026 (P31) | — | t2,t4 |
| A22 | A:outcome | Duplication and code quality are judged on every diff | critic.md:165-169,269-278 | — | «поддерживать порядок» 06.10.2026 | D6,D9 | t2 |
| A23 | A:outcome | Code judges data (shape, joins, presence); a role's judgment is judged by a tier above (P27, AR-29) | critic.md:296-304; AGENTS.md:983,1036 | — | P27 | C8 | t2,t21 |
| A24 | A:outcome | Knowledge lives in repo files, not in a machine's memory | PROJECT.md:179-182 | — | — | — | t5 |
| A25 | A:outcome | A new idea: ask the owner about intent first; goal doc with measured success, carried facts, reasoned exclusions, before design | PROJECT.md:112-133; .claude/skills/idea-goal/SKILL.md:52-88 | — | owner word 11.11.2026 | — | t5,t7 |
| A26 | A:outcome | A batch closes by finishing the work, not by carrying it over; a carry-over is confirmed by a person | docs/TEAMWORK.md:58-70 | — | «пачка закрывается доделкой, не переносом» 08.10.2026 | — | t10 |
| A27 | A:outcome | A work node is executable by a weaker model: direction chosen, files and tests named, no "invent an approach" | docs/TEAMWORK.md:87-92 | — | — | — | t10 |
| A28 | A:outcome | The next session recovers from files alone; a retro is written while the reasons are in context | .claude/skills/session-handoff/SKILL.md:12-85; session-retro/SKILL.md:6-51 | — | owner words 17.11.2026, 24.11.2026 | C24 | t15,t16 |
| A29 | A:outcome | The package release text is English with no Cyrillic | CLAUDE.md:148-158 (Язык); AGENTS.md:148 | — | — | — | t30,t22 |
| A30 | A:means | One witness run after all edits; independent calls go out in one message; trim output before it enters context | CLAUDE.md:7-18 | — | owner word 24.11.2026; D-0035 | D11 | t30 |
| A31 | A:means | A probe is rolled back from a byte copy, proved by hash, never by git checkout | CLAUDE.md hygiene pt 7 | — | — | C1 | t30,t20 |
| A32 | A:knowledge | Builder: package work reads factory-rules.md whole; stdlib only; new config key has a default; old projects keep working | builder.md:134-145 | — | — | B2 | t3 |
| B1 | B:scout | Knows: digest form v1, trail rules, judgment refusal ends with the fixed line, no Bash. Checked by: trail spot-check, golden set | scout.md:12-155; COORDINATOR.md:81-84 | — | — | A4 | t8,t9,t1 |
| B2 | B:builder | Knows: spec-only work, forks go back as questions, witness, tests by TESTING.md, git and staging rules. Checked by: witness at acceptance, critic | builder.md:12-150 | — | — | A32 | t3 |
| B3 | B:critic | Knows: 24 rules, probe via runner, verdict JSON, Q1-Q13. Checked by: critic_verdict_check exit 0, Lead walks fix diffs by Q1-Q12 | critic.md:12-361; COORDINATOR.md:321-328 | — | — | Q1 | t2,t1 |
| B4 | B:designer | Knows: rule 11 form, edges with invariants, readers of every touched file, forks, 40,000-byte cap. Checked by: Lead acceptance, plan critic (Q13) | designer.md:14-125 | — | owner words 16.11.2026, 17.11.2026 | Q13 | t4 |
| B5 | B:Lead | Knows: routing, acceptance matrix, journal, cost gates, PROJECT.md steps. Checked by: weekly calibration, journal detectors, architect | COORDINATOR.md:49-66,420-489; PROJECT.md:63-133 | — | — | — | t1,t5 |
| B6 | B:architect | Owner's new ideas steps 1-4, process escalations, weekly calibration; never a subagent (D-0067); start list in PROCESS/ARCHITECT_START.md (exists, not read) | COORDINATOR.md:59-62,186-192; PROJECT.md:117-118 | — | D-0067 | — | t1,t27 |
| B7 | B:judge | Role file exists with two verbatim prompts but rule 13 says no judge is bound; unused | judge.md:1-72; COORDINATOR.md:336-338 | — | — | X3 | t14,t1 |
| Q1 | B:critic-Q | Fit to the spec: every requirement and edge as written, spec's error direction (no unknown becomes a pass) | critic.md:233-234 | — | — | B3 | t2 |
| Q2 | B:critic-Q | Builder's own decisions on silent points go the safe way and match the named consumers | critic.md:235-236 | — | — | B3 | t2 |
| Q3 | B:critic-Q | Seams: other nodes' files are touched additively, localised, nothing reordered | critic.md:237 | — | — | B3 | t2 |
| Q4 | B:critic-Q | Class-wide completeness: SIBLING_MAP axes and same-artifact neighbours fixed in the round; leftovers carry an executor | critic.md:238-240 | — | — | A6 | t2 |
| Q5 | B:critic-Q | Tests: killing power (probe), expected-value source, row per door behaviour, rewrite trace, no duplicate row, file budget | critic.md:241-268 | — | owner words 10.11, 17.11.2026 | A20 | t2 |
| Q6 | B:critic-Q | Duplication: does the diff re-implement a reader, writer, helper or table the repo already has | critic.md:269-274 | — | — | A22 | t2 |
| Q7 | B:critic-Q | Code quality: functions over ~60 lines or 3 nesting levels, copy-paste, dead branches, lying names, unread results | critic.md:275-278 | — | — | A22 | t2 |
| Q8 | B:critic-Q | Hygiene in the package: FR-29/FR-30, size caps, CRLF kept | critic.md:279 | — | — | D13 | t2 |
| Q9 | B:critic-Q | In-tree shrink-only ratchets: every added or raised row named row by row; an unnamed raise is a finding | critic.md:280-294 | — | — | D6 | t2 |
| Q10 | B:critic-Q | Architecture: AR-n touched and named, one-way rule, VARIETY (no block, silent default or hand-off to a person on an unknown) | critic.md:295 | — | — | A23 | t2 |
| Q11 | B:critic-Q | Judgment: does the diff move a role's judgment into code or add non-craft text a role must read | critic.md:296-304 | — | P27 | A23 | t2 |
| Q12 | B:critic-Q | One road: no language, project or case outside a shared mechanism without a data row or the owner's word | critic.md:305-317 | — | P31 | A21 | t2 |
| Q13 | B:critic-Q | Plan gate: edges both worlds, meaning restated, premises reproduced, readers block answered, forks consistent with evidence | critic.md:327-361 | — | — | B4 | t2 |
| C1 | C:M | hygiene_gate refuses cd, journal writes by shell, discarding dirty changes; doors are fixed forms | CLAUDE.md:93-147; AGENTS.md:1054 | — | owner words 14.11.2026, 16.11.2026 | A31 | t30,t20 |
| C2 | C:M | Dispatch header lines, dispatch_new/manifest/gate; DoD names at most 3 test files, never --witness-for | CLAUDE.md:51-92; designer.md:20-23 | — | — | A1 | t30,t4 |
| C3 | C:M | Enforcement files: builder hands over, Lead places on the live path (review rule) | CLAUDE.md:9-12 | — | — | — | t30 |
| C4 | C:machinery | Journal base fields, ts format, SHAPES table, clone letters, validator at pre-commit and write time | COORDINATOR.md:344-418 | — | — | A15 | t1 |
| C5 | C:machinery | Rule 6 "converging" mark, rule6_due, fix_round_count border, reviewed:<sha> token in dispatch description | COORDINATOR.md:173-185,306-332 | — | owner word 17.11.2026 | A13 | t1 |
| C6 | C:M | Background by default, label starts with the role, tier mismatch warn by transcript | COORDINATOR.md:194-205 | — | D-0016 | — | t1 |
| C7 | C:M | dispatch_skipped events, small-work batching, "first move only" counter for Lead self-execution | COORDINATOR.md:207-223 | — | — | — | t1 |
| C8 | C:machinery | mechanism_gate/architecture_gate commit lines, axis blocks, judgment census, tier line | COORDINATOR.md:257-279 | — | — | A14 | t1 |
| C9 | C:M | Batch canon: builder runs only the `--witness-for` block, never CI, never canon files | COORDINATOR.md:141-153; builder.md:45-52; PROJECT.md:194-196 | — | owner word 14.11.2026 | — | t1,t3,t5 |
| C10 | C:machinery | Task DAG at 5+ events, piles.py take/close/check, wave.py merge, statuses, B-ids | COORDINATOR.md:155-160; docs/TEAMWORK.md:13-108 | — | — | — | t1,t10 |
| C11 | C:M | Builder git rules: no stash/add/commit in a shared tree, mechanism paths stay staged, regenerate AGENTS.md | builder.md:125-133 | — | — | — | t3 |
| C12 | C:M | Report shape caps (final message 2,000 chars, 4+N lines), critic JSON block, handoff_gate one-file write | builder.md:71-98; critic.md:115-164; designer.md:59-91 | — | — | A16 | t3,t2,t4 |
| C13 | C:machinery | Lead degradation: lead_degraded/restored events, entry and exit tier checks, lead-queue | COORDINATOR.md:459-488 | — | — | A7 | t1 |
| C14 | C:M | Critic probe only via mutate_once.py by Bash, 3 mutants cap, no hand edits | critic.md:204-231 | — | owner word 17.11.2026 | — | t2 |
| C15 | C:M | Digest form v1 and its flag grammar (trail_unbacked, zero_case...) restrict a scout's report shape | scout.md:90-155 | — | — | A16 | t9 |
| C16 | C:machinery | Exam-before-editing-a-role-file gates; PROCESS/SCOUT_GOLDEN_SET.md and CRITIC_EXAM.md are absent | scout.md:59-63; critic.md:58-67 | absent | — | X4 | t26,t27 |
| C17 | C:machinery | session-handoff steps 2, 2a, 2b, 5a (journal closed, r3_integration_check, wait_reaper), session_retro counts | .claude/skills/session-handoff/SKILL.md:20-70 | — | — | A28 | t15,t16 |
| C18 | C:machinery | Rule 13 leaf routing, judge prompts, DELEGATION_TABLE four-state statuses; AGENTS hooks table (16 hooks) | COORDINATOR.md:334-342; DELEGATION_TABLE.md:7-53; AGENTS.md:1049-1066 | — | — | B7 | t1,t11,t21 |
| D1 | D:budget | Boot budget: breach at over 120KB total or over 10% growth in one session; measured by the BOOT BUDGET block | .claude/skills/boot-diet/SKILL.md:3,21-29; session-handoff/SKILL.md:56-63 | — | — | — | t6,t15 |
| D2 | D:cap | CURRENT_CONTEXT.md at most 10 KB, only main's state | PROJECT.md:165-167 | — | — | — | t5 |
| D3 | D:cap | Rule section about 40 lines at most; boot title needs a contents line; numbers never reused | boot-diet/SKILL.md:113-125 | — | — | X1 | t6 |
| D4 | D:rule | No extra documents; a role rule has one home; new main document needs owner's word and an axis-31 row | PROJECT.md:56; test_role_carriers_one_owner.py | — | «избавится от всех брифов и закрепить что мы не создаём лишние документы» 17.11.2026 | X6 | t5 |
| D5 | D:rule | PROJECT.md holds only active rules; stories go to PROJECT_FULL.md; closed items archived verbatim with a pointer | PROJECT.md:13-14; boot-diet/SKILL.md:30-64 | — | owner word 11.11.2026 | — | t5,t6 |
| D6 | D:ratchet | Shrink-only ratchets: clone baseline, lint baseline, judgment census, process_ratchet_tokens, told_ratchet, norms.json, known-red ledgers, driver-exits | critic.md:280-294; COORDINATOR.md:276-279; AGENTS.md:993 | — | AR-20 | A22 | t2,t1,t21 |
| D7 | D:rule | A ratchet raise is named row by row in the verdict (key, old to new, reason); unnamed raise is a blocker | critic.md:280-289 | — | — | D6 | t2 |
| D8 | D:budget | Test lines not above code lines; new test file runs at most 10 s (split part 60 s CI), one table per file | critic.md:259-268; builder.md:99-118 | — | owner words 10.11, 17.11.2026 | A20 | t2,t3 |
| D9 | D:cap | New functions over ~60 lines or over 3 nesting levels are findings | critic.md:275-278 | — | — | Q7 | t2 |
| D10 | D:cap | Size caps: designer draft 40,000 bytes, builder report prose ~500 words, critic review ~1800 words, final message 2,000 chars | designer.md:118-125; builder.md:57-59; critic.md:322 | — | owner word 17.11.2026 | — | t4,t3,t2 |
| D11 | D:cap | Worker context WARN 250K and STOP 400K; main compaction hint at ~300K; about 15 main turns per task (goal) | COORDINATOR.md:304,309; PROJECT.md:149-153 | — | — | — | t1,t5 |
| D12 | D:cap | One critic pass per topic, topic at most 4 nodes; batch S up to 4, M 5-9, L 10-15 nodes; target 6 writers | COORDINATOR.md:342; docs/TEAMWORK.md:102-103; PROJECT.md:185-192 | — | owner words 17.11.2026, 13.11/16.11.2026 | — | t1,t10,t5 |
| D13 | D:cap | Package size caps `selftest.py --limits`, audit A22; text added to a role is paid for by removing text (numbers not in given files) | builder.md:137-139 | — | — | Q8 | t3 |
| D14 | D:cap | Journal notes at most 300 chars; BACKLOG.md frozen; no node without a pile; no leftovers by design | COORDINATOR.md:330; docs/TEAMWORK.md:50-52,93-96 | — | owner word 18.11.2026 | — | t1,t10 |
| D15 | D:detector | Growth between calibrations watched by weekly calibration (check 10); no code-gate for boot rules | boot-diet/SKILL.md:134-137 | — | — | — | t6 |
| X1 | analog | Section length: "about 40 lines" (rule 2) vs "longer than 50 lines" flagged by check 33 (rule 7), same file | boot-diet/SKILL.md:114,124-125 | — | — | D3 | t6 |
| X2 | analog | Rule 6 states the "two rejected on one tier force escalation" clause twice in one rule | COORDINATOR.md:175-176,182-183 | — | — | A13 | t1 |
| X3 | analog | Rule 13 says no judge is bound, yet judge.md and the AGENTS roles table carry a judge role | COORDINATOR.md:336-338; judge.md:1-72; AGENTS.md:1083 | — | — | B7 | t1,t14,t21 |
| X4 | analog | scout.md requires a golden set before editing the role; COORDINATOR R1 row a says none is registered; file absent; critic.md alone has a deviation clause | scout.md:59-63; COORDINATOR.md:83; critic.md:63-67 | absent | — | C16 | t26,t27 |
| X5 | analog | Duplicates against one-home rule: one-critic-per-topic in COORDINATOR.md:309,342 and PROJECT.md:191; witness scope in COORDINATOR.md:143-153, builder.md:45-52, PROJECT.md:77-81; negative-claim rule in 4 files | boot-diet/SKILL.md:113-115 | — | — | A4 | t1,t3,t5,t6 |
| X6 | analog | "No extra documents" (PROJECT.md:56) vs frozen full copies PROJECT_FULL.md, CLAUDE_HOST_ADAPTATIONS_FULL.md and generated AGENTS.md | PROJECT.md:13-14,56; AGENTS.md:1-3 | — | — | D4 | t5,t20 |
| E1 | E:open | Docs never say where a second factory lives or what of the package/forge it reuses; only one factory and one forge appear | PROJECT.md:3-14 | — | — | — | t5 |
| E2 | E:open | Which of the 16 hooks and the hygiene refusals may stay under "constraints on outcomes, not means"; no rule separates them | AGENTS.md:1049-1066; CLAUDE.md:93-100 | — | — | C1 | t21,t30 |
| E3 | E:open | What replaces the journal-driven calibration (counters, events) if outcomes are checked instead; calibration is tied to journal fields | COORDINATOR.md:416-418 | — | — | C4 | t1 |
| E4 | E:open | The numeric caps of selftest --limits and A22, lint/clone baselines and crap thresholds are not in the given files; "crap" has no hit in AGENTS/CLAUDE/COORDINATOR/PROJECT/BOOT/DELEGATION_TABLE, hits only in plans/piles/forge/README.md | builder.md:137-139 | — | — | D6 | t31,t32 |
| E5 | E:open | Model bindings for forge2 roles (judge unbound, Haiku banned D-0002, architect on Fable) and whether an architect tier exists | COORDINATOR.md:49-66 | — | — | B6 | t1 |
| E6 | E:open | Whether the owner-away rule, the 6-writer target and the owner-word registry survive in forge2 | PROJECT.md:185-192,215-219 | — | — | — | t5 |
| E7 | E:open | Whether "no extra documents" and the one-home rule apply to the factory too; the rule text is forge-only | PROJECT.md:56 | — | — | D4 | t5 |
| E8 | E:open | Whether FR/AR/P (59, 29, 31 items) are the factory's inherited spec or forge-only; their full texts were not read | AGENTS.md:885-1041 | — | — | A23 | t21 |

## Trail
| tid | op | target | pattern / range | flags | result | control |
|---|---|---|---|---|---|---|
| t1 | read | C:\QAFactory\forge-repo\COORDINATOR.md | 1-489 | — | read C:\QAFactory\forge-repo\COORDINATOR.md:1-489 | — |
| t2 | read | C:\QAFactory\forge-repo\.claude\agents\critic.md | 1-361 | — | read C:\QAFactory\forge-repo\.claude\agents\critic.md:1-361 | — |
| t3 | read | C:\QAFactory\forge-repo\.claude\agents\builder.md | 1-150 | — | read C:\QAFactory\forge-repo\.claude\agents\builder.md:1-150 | — |
| t4 | read | C:\QAFactory\forge-repo\.claude\agents\designer.md | 1-125 | — | read C:\QAFactory\forge-repo\.claude\agents\designer.md:1-125 | — |
| t5 | read | C:\QAFactory\forge-repo\PROJECT.md | 1-234 | — | read C:\QAFactory\forge-repo\PROJECT.md:1-234 | — |
| t6 | read | C:\QAFactory\forge-repo\.claude\skills\boot-diet\SKILL.md | 1-137 | — | read C:\QAFactory\forge-repo\.claude\skills\boot-diet\SKILL.md:1-137 | — |
| t7 | read | C:\QAFactory\forge-repo\.claude\skills\idea-goal\SKILL.md | 1-174 | — | read C:\QAFactory\forge-repo\.claude\skills\idea-goal\SKILL.md:1-174 | — |
| t8 | read | C:\QAFactory\forge-repo\.claude\agents\scout.md | 1-40 | — | read C:\QAFactory\forge-repo\.claude\agents\scout.md:1-40 | — |
| t9 | read | C:\QAFactory\forge-repo\.claude\agents\scout.md | 40-155 | — | read C:\QAFactory\forge-repo\.claude\agents\scout.md:40-155 | — |
| t10 | read | C:\QAFactory\forge-repo\docs\TEAMWORK.md | 1-108 | — | read C:\QAFactory\forge-repo\docs\TEAMWORK.md:1-108 | — |
| t11 | read | C:\QAFactory\forge-repo\BOOT.md and DELEGATION_TABLE.md | 1-53 each | — | read C:\QAFactory\forge-repo\BOOT.md:1-53 | — |
| t12 | read | C:\QAFactory\forge-repo\README.md | 1-72 | — | read C:\QAFactory\forge-repo\README.md:1-72 | — |
| t14 | read | C:\QAFactory\forge-repo\.claude\agents\judge.md | 1-72 | — | read C:\QAFactory\forge-repo\.claude\agents\judge.md:1-72 | — |
| t15 | read | C:\QAFactory\forge-repo\.claude\skills\session-handoff\SKILL.md | 1-85 | — | read C:\QAFactory\forge-repo\.claude\skills\session-handoff\SKILL.md:1-85 | — |
| t16 | read | C:\QAFactory\forge-repo\.claude\skills\session-retro\SKILL.md | 1-82 | — | read C:\QAFactory\forge-repo\.claude\skills\session-retro\SKILL.md:1-82 | — |
| t17 | read | C:\QAFactory\forge-repo\.claude\skills\permission-audit\SKILL.md | 1-124 | — | read C:\QAFactory\forge-repo\.claude\skills\permission-audit\SKILL.md:1-124 | — |
| t18 | read | C:\QAFactory\forge-repo\.claude\skills\critic-exam-gen\SKILL.md | 1-60 (skim) | — | read C:\QAFactory\forge-repo\.claude\skills\critic-exam-gen\SKILL.md:1-60 | — |
| t19 | read | C:\QAFactory\forge-repo\.claude\skills\scout-exam-gen\SKILL.md | 1-60 (skim) | — | read C:\QAFactory\forge-repo\.claude\skills\scout-exam-gen\SKILL.md:1-60 | — |
| t20 | read | C:\QAFactory\forge-repo\AGENTS.md | 1-60 | — | read C:\QAFactory\forge-repo\AGENTS.md:1-60 | — |
| t21 | read | C:\QAFactory\forge-repo\AGENTS.md | 885-1088 | — | read C:\QAFactory\forge-repo\AGENTS.md:885-1088 | — |
| t22 | grep | C:\QAFactory\forge-repo\AGENTS.md | `^(# \|## \|--- \|<!-- )` | content | found 51; AGENTS.md:5, AGENTS.md:159, AGENTS.md:649, AGENTS.md:885 | — |
| t23 | grep | C:\QAFactory\forge-repo\COORDINATOR.md | `^#{1,3} ` | content | found 27; COORDINATOR.md:1, COORDINATOR.md:70, COORDINATOR.md:459 | — |
| t24 | glob | C:\QAFactory\forge-repo | `.claude/{agents,skills}/**/*` | — | found 12; .claude\agents\scout.md | — |
| t25 | glob | C:\QAFactory\forge-repo | `{SYSTEM_PROMPT.md,DECISIONS.md,CURRENT_CONTEXT.md,delegation.config.yaml,PROCESS/ARCHITECT_START.md,docs/TESTING.md,docs/SIBLING_MAP.md,docs/OWNER_PRINCIPLES.md}` | — | found 8; SYSTEM_PROMPT.md, DECISIONS.md, CURRENT_CONTEXT.md | — |
| t26 | glob | C:\QAFactory\forge-repo | `PROCESS/{CRITIC_EXAM,SCOUT_GOLDEN_SET}.md` | — | absent | t27 |
| t27 | glob | C:\QAFactory\forge-repo | `PROCESS/{ARCHITECT_START,WEEKLY_CALIBRATION_PROTOCOL}.md` | — | found 2; PROCESS\ARCHITECT_START.md, PROCESS\WEEKLY_CALIBRATION_PROTOCOL.md | — |
| t28 | grep | C:\QAFactory\forge-repo\COORDINATOR.md | `converging` | count | count 4 | — |
| t29 | grep | C:\QAFactory\forge-repo\AGENTS.md | `converging` | count | count 4 | — |
| t30 | read | C:\QAFactory\forge-repo\CLAUDE.md | 1-30 (rest from the injected context) | — | read C:\QAFactory\forge-repo\CLAUDE.md:1-30 | — |
| t31 | grep | C:\QAFactory\forge-repo | `crap\|крэп\|крап` | -i count glob={AGENTS,CLAUDE,COORDINATOR,PROJECT,README,BOOT,DELEGATION_TABLE}.md | found 7; plans\piles\forge\README.md:7 | — |
| t32 | grep | C:\QAFactory\forge-repo | `ratchet` | -i count glob={AGENTS,CLAUDE,COORDINATOR,PROJECT,README,BOOT,DELEGATION_TABLE}.md | found 46; AGENTS.md:4, COORDINATOR.md:3 | — |

## Forks
Forks the documents leave open (facts only, no pick): (1) forge2 outcome-only rules vs the many code gates that restrict means (C-rows marked `M`); the documents state P1 and FR-47 "code is an instrument, not a substitute" but also run 16 hooks. (2) Size control exists as caps and ratchets (D rows), but caps' numbers for the package live outside the given files. (3) The crap/linter work exists as piles (plans/piles/forge, findings 20261124-crap*, specs fg7-132/133 seen only as grep hits in a worktree copy), not in the given files.
this needs a decision from a tier above.

## Not done
- F, per file: read fully: COORDINATOR.md, critic.md, builder.md, designer.md, PROJECT.md, boot-diet, idea-goal, scout.md, TEAMWORK.md, BOOT.md, DELEGATION_TABLE.md, README.md, judge.md, session-handoff, session-retro, permission-audit (t1-t12, t14-t17). Skimmed (first 60 lines, procedure not needed): critic-exam-gen, scout-exam-gen (t18, t19). AGENTS.md: lines 1-60 and 885-1088 read, 61-884 not read (generated copy of CLAUDE/COORDINATOR/PROJECT; only headings and the `converging` count compared, t22, t29, t28). CLAUDE.md: read tool 1-30; the full text came in the injected context, not a Read, so its rows rest on t30 plus that context.
- Trail gaps: t13 was skipped in numbering (BOOT.md and DELEGATION_TABLE.md are one row, t11, which names only BOOT.md in its result; DELEGATION_TABLE.md:1-53 was read in the same turn). No Read of PROCESS/ARCHITECT_START.md, docs/TESTING.md, docs/SIBLING_MAP.md, factory-rules.md, OWNER_PRINCIPLES.md (outside `given`; bodies behind rules cited here were not opened).
- Scope boundary: .claude/worktrees/* holds copies of the repo; my greps t31-t32 matched them too (only root-file hits were used). A search of .claude/**/*.md for "crap" hit its time limit and is incomplete, so no claim rests on it.
- Counts of critic rule line spans for Q1-Q3 are approximate (+-2 lines).
- The environment (hooks alive, CI) was not checked: outside this role's tools, a tier with Bash is needed.
