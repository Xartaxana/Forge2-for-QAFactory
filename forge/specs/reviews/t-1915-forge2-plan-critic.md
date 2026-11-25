# t-1915 -- plan gate: forge 2 and the light factory (plan v1.1 + frame spec r0, commit 8cc6b5192)

Critic, rule 24, one pass. Under review: `docs/tasks/specs/20261125-forge2-light-factory-plan.md` (the plan) and
`docs/tasks/specs/20261125-forge2-light-factory-spec.md` (the spec). Part 2 (card bodies C0-1..C2-7) not judged, only
its index rows. Every finding names its carrier; "ARCH" = it changes a contract, an owner of judgment, a stage or a
gate; "WORDING" = text only. "Blocks cards" = must be fixed in spec r1 before part 2 or any phase-3/4 builder dispatch.
The decision to accept and every owner fork stay with the Architect / the owner (rule 6).

V1 verdict: fit_with_fixes (NEEDS WORK). The frame holds: one record, one writer, gates as data rows, judgment kept
out of code, worlds before/after, forks returned. But eight contract defects would build dead ends or silent passes
into exactly the gates the owner asked for ("не мешали правильным действиям ... не давали пройти дальше не закончив").
None needs a new frame; all are bounded edits of spec sections 2-4 and three plan sentences.

Fixes (numbered; section; what changes; kind; blocks cards?):

1. Spec §3 X6, §4 C3-3 edge "reason outside the list -> debt stays, door lists valid reasons (rule 6: no third way)";
   plan 1а rule 6 "третьего нет". A closed list with no exit is the LOCAL-1 trap AR-29 names verbatim ("closes a
   role's obligation by a closed-list reason ... is a breach"; architecture.md:176, breakage :191-193) and an AR-2
   passage breach (a value the list lacks blocks). Concrete: G4.2 debt for REQ-7 whose code is not merged yet
   (axis 4, В3) -- no reason in plan's four ("стенд недоступен", "источника ожидания нет", "источник недоступен",
   "человек решил не проверять") fits; the debt stays forever unless a person passes it, and stage 4 has no person
   stop. Change: `reasons.yaml` gets an open row (`other`: the performer's words + what was tried) that the gate does
   NOT refuse but routes to the tier above (next critic gate, else the person at the next stop, else the conductor
   seam) and that reaches the report by name; add the rows the variety walk itself promises (readiness "not
   implemented yet", axis 4; "no tool for this surface", axis 2). Plan rule 6 reads "третьего нет" as "молчания нет".
   The owner's words support the open row (gates must not hinder right actions). ARCH. Blocks cards.
2. Spec §3 G4.2 ("autotest with run + can-fail record", owner data, at stage-4 exit) vs G4.C ("critic red probe");
   plan положение 5 and нестыковка 6: "пробу делает критик". If the critic writes the can-fail record, G4.2 at the
   performer's exit can never be met (the critic runs after); if the performer must write it, the probe is done
   twice and plan 5 is contradicted. Silent POSITIONAL fork. Change: state who writes the can-fail row and the order
   (code check without can-fail -> G4.C probe writes can-fail rows -> post-critic check of their presence), and the
   same order statement for G3 and G6 (code check -> critic -> fix rounds -> docs_build -> person stop), with the
   invariant: the person never sees an un-critiqued plan or report. ARCH. Blocks cards.
3. Plan 1в "Понимание ... **Что проверяем** -- перечень требований" (owner 25.11 ~03:12: "в текущем таком файле ещё и
   перечень требований"), shown at the FIRST stop; but requirements are a stage-3 leave (plan положение 1, gate table
   rows 1 and 3; spec G3.1-G3.4, D2, section 1 "AR-26: the requirement is the unit from stage 3"). D2 ("every
   requirement in checking/not checking of understanding") is vacuous at G1. In the frozen factory understanding.md
   is written at S2 after the requirements register (premise re-run, V6). Change: either stage 1 leaves the
   requirement list (stage 3 adds expectation sources, checks, levels) or the understanding stop moves after
   requirements. The owner's words support the list in the understanding at the first stop. ARCH (stage contract).
   Blocks cards.
4. Spec §2a header `stages` (`open|exited|stale`) and C4-1 key "every record state in the fixture set has a move":
   the state set is not enumerated and lacks: exit refused with open debts (who is launched, with what context --
   relaunch in fresh context with the debt list?), waiting at a person stop, held by a question (rule 8), in a fix
   round after the critic, stopped by the person (В4 outcome "просит остановиться"), a shortfall returned to an
   already exited producer (1б needed 5). Change: §2a enumerates stage states and the move of each; C4-1 tests that
   list. ARCH. Blocks cards.
5. Spec §2c `stages` field scoping + plan положение 1 / rule 7 (a later stage writes "не по своей части"): a
   requirement added at stage 4 is never checked by G3.1-G3.4 (their `stages` is 3) and never seen by G3.C. Concrete:
   REQ-15 added at stage 4 with no `expectation_source` passes every later exit (G6.2 needs only a result) -- a
   silent P20 hole. Change: rules scope by SECTION (run over every live row of their section at every exit), and a
   row added after its critic gate goes to the next critic gate by name. ARCH. Blocks cards.
6. Spec §2a Row: `state` (`live|stale|added_after_approval`) mixes liveness with provenance, and record.py has no
   revise operation (init, add, stale, empty, check). Concrete: REQ-9 added after approval, later staled by a stage-4
   correction -> one of the two marks is lost (X4 or the report section "added after approval"). Second: revising
   REQ-4 as REQ-12 with `from: [REQ-4]`, then `stale REQ-4` -- transitive over `from` -- stales REQ-12 too. Change:
   `state` = `live|stale`; after-approval derived (`seq > approved_plan_seq`, AR-10: a derivable value is written by
   code); a `supersedes` link excluded from stale propagation. Also define "obligation" (plan 1.3, spec `links`,
   `results`): a check, or one Then of a check (В19 mixed results); and split critic findings from performer
   `findings` (F1) and say whether open critic findings count in G6.3 (plan 1.5: the rest goes to the report by
   name -> not debt). ARCH (contract). Blocks cards (C3-1 is the first phase-3 card).
7. Spec §3 X3 / C3-4 ("files created/changed since stage start") with stage-4 groups in parallel (C4-1 "a closed
   group goes on while others work"): group A's exit sees group B's not-yet-referenced files -> false debt, a gate
   defect built in (rule 10). VCS-ignored files (Gradle `build/` on ao3-wrapper) unstated. Change: attribute by agent
   (the `observe` event carries `agent`) or run X3 per group over the files its agent touched; ignored files
   excluded. ARCH. Before C3-4.
8. Plan 1а rule 8 ("открытый вопрос держит только зависящее"), spec C4-1 edge: no field links a row to the question
   holding it. Change: `questions` row `holds: [ids]` (performer's judgment) or row `held_by`, read by run_stage.
   ARCH. Before C4-1.
9. Spec C3-2 edge "context over the host window -> refused with its size": a state with no move (rule 9, AR-25,
   axis 11). Change: goes through the no-move seam to the conductor with options (group split, sections by pointer);
   "never cut silently" stays. ARCH. Blocks cards.
10. Spec §1 "P13, FR-4: a person's word passes any gate, recorded": no contract carries it -- §2a has no pass row,
    §2c no person's-word door, FR-4's "pass over a factory-owned block is filed as a factory finding" has no road.
    And plan 1а "ночью и в сравнительном прогоне столбец «человек» исполняет запускающая модель": unbounded, the
    launching model could pass any gate or grant X5 permission -- dishonest measurement and a trace (P8, FR-53).
    Change: §2a pass rows (block, words, speaker); §2c door "person's word"; launching model answers questions at
    stops only, never passes a gate or grants outward permission; passes counted by score.py. ARCH. Blocks cards.
11. Spec §2d closed list + C4-3 ("a stop message cites only these ids") + F2: the G5.P "bug or not" stop for an
    autotest red has no document -- the bug draft is not one of the five, the test report does not exist yet, and
    run output is a log ("никаких леджеров и логов"). Change: a bug-or-not question body built by docs_build from
    the bug-draft rows (template + budget) in §2d; state that the conductor's questions go through ask.py too. ARCH.
    Before C3-5/C4-3.
12. Spec §3 D3 owner "per F13" is no owner (the dispatch DoD: data / judgment / intent). Plan 1в issue rule 3 has
    code return a working-file request to the performer (a refusal), F13(a) says "never a refusal" -- they are about
    different things. Change: D3 = data (document ids in the stop message's field); author wording = critic G6.C
    with code advice. WORDING (+ owner column).
13. Spec §1 line "AR-7 ... another road is accepted with `obtained_by`" vs line "P26, P30 ... -> agent-written
    evidence rows" (broken): a screenshot taken by the host's own tool and recorded with `obtained_by` is both
    accepted and a breach. Change: `obtained_by` accepted for runs; manual-pass evidence for "прошло" is
    tool-recorded (P26), another road reads "выполнено агентом, доказательств нет: почему". P26 (owner 02.11) supports
    this; the 25.11 word on tools was about the test launcher. WORDING (+ C4-4 key).
14. Spec §1 walk "AR-6: one reader each for record and knowledge; sources by every route": that is AR-13; AR-6's
    clause "an LLM agent is never a read route" (architecture.md:122) is dropped, while plan положение 2 adds helpers
    on large stages -- a helper's retelling of an attachment is the TP1-15045 breakage. Change: restate AR-6; craft
    rule: sources are read by the performer or a helper and land in the record whole, never as a retelling. WORDING.
15. Missing owners and carriers (spec §1 layout "each path named once"; §4 owns): delivery-target rows (AR-1 list,
    axis 6) -- no card; expectation-source kinds -- no named file; C3-6 keys lack surface kind (axis 2 walk says "a
    knowledge row"), repositories (axes 1, 11), who answers (axis 9), how the project accepts results (axis 6, plan
    "Что затронуто" 6); case and bug export to `.md` (plan положение 8 "выгрузка кейсов", owner answer 4 "по
    умолчанию всё в .md", P8 "баги только в md") -- no card; §5 row "everything to .md -> C3-5" is false (C3-5
    builds only person documents). ARCH (cards/owns). Before phase 3.
16. Measurement statements with no carrier field: plan 1б «Чем это мерится» (shortfalls, unpaired rows, findings
    re-found by the next stage -- the last is judgment, FR-12: an acceptor's label, not code) and 1в issue rule 4
    (documents and sizes given to the person; each time the person had to open a working file): no field in §2f, no
    row in §5. Change: add the fields/labels and trace rows. ARCH (contract).
17. Absent / unreadable data files: only `gate-rules.yaml` has a stated behaviour (§2c). Silent for stages, routes,
    reasons, red-causes, empty-outcomes, person-docs, questions, knowledge-keys, hook-points, runner-forms. Change:
    one statement on `rows.py`: absent or unreadable -> launch refused naming file and door, never read as an empty
    list (AR-28). WORDING (one contract line).
18. Cost (plan «Цена», «Фазы»; spec §2a): every row goes through a record.py CLI call -- dozens to hundreds of tool
    calls per story the free agent does not pay. Change: `record.py add` takes a batch fragment in one call; and the
    riskiest premise (six fresh-context stages fit "вдвое") is first measured at C4-7, after everything is built --
    add a hand-run spike of the stage chain on a stub record in phase 0 or 2 (cheap, before phase 3). ARCH (plan
    phases) -- not blocking.
19. Duplication (rule 22 Q6): forge C1-5 "secrets" hook and factory C4-5 `secrets` point = two secret-pattern tables,
    the exact AR-15 open item (architecture.md:217); `measure/tools/seeded.py` and `measure/tools/arm.py` both launch
    an agent arm; F14 `forge/tools/ci.py` and `ci.yml` run "the same jobs" by two lists. Change: one pattern table in
    `factory/data` read by the forge hook; seeded.py calls arm.py; one job list read by both. WORDING (card owns).
20. VARIETY: a project whose tests live in a separate repository or across several (axis 1, axis 3 "tests apart"):
    §2e `outward_write` is not defined -- writing tests into the test repository may be refused mid-stage (an AR-2
    block) or slip through. Change: define outward as writes outside the project roots in knowledge (key
    `repositories`) plus publication; unknown root -> ask once at first need. And F10: a host without Python 3 has no
    record writer -> write the `axis 8: narrows` line (launch refused with a door) for the owner. ARCH (2e).
21. AR-22 claimed kept by W1, but W1 walks sections; AR-22 is field level. Typed fields with no named reader:
    `readiness`, `executable_where`. Change: name readers (run_stage grouping, docs_build "Оставлено вам") or extend
    W1 to typed fields. WORDING.
22. Spec §1 does not name invariants the design touches: AR-8, AR-9 (2c doors), AR-11 (start-load budget, F9),
    AR-15, AR-16 (ask.py one form), AR-18 (exit_check output shape), AR-20 (forge ratchets), P5, P15, P18 (F7).
    WORDING.

V2 rule 24 in full.
- Q13 (a) EDGES: NEEDS WORK. Stated well: budgets AT/BEYOND (C3-5), fix rounds exhausted (C4-2), absent record /
  gate-rules / knowledge / journal / craft page / host profile (§2, §6), unreadable record, empty outcomes, unknown
  route, VCS absent, both worlds of every artifact the change creates (§6). Silent or wrong: absent data files other
  than gate-rules (fix 17); context over window has no move (fix 9); reason outside the list (fix 1); critic/probe
  order (fix 2, POSITIONAL, invariant not stated); parallel groups vs X3 (fix 7, a pair of the spec's own
  requirements: F11 parallel + X3); re-approval after "изменился замысел" (В4) -- what happens to
  `approved_plan_seq` and after-approval marks is unstated (fold into fix 4).
- Q13 (b) MEANING: NEEDS WORK. Restated: `state` = liveness AND provenance (contradiction, fix 6); `findings` = both
  performer observations (F1) and critic findings (C4-2) -- G6.3 meaning undefined (fix 6); "obligation" undefined
  though `links` and `results` key on it (fix 6); D3 owner "per F13" (fix 12); X6 passes a gate before the person
  accepts the reason -- a provisional pass the text never calls provisional (fix 1); §1 AR-7 line vs P26 line (fix
  13); AR-6 restated as AR-13 (fix 14).
- Q13 (c) PREMISES: ACCEPT. Plan and spec premises carry carriers; two re-run (V6), both reproduce; a third (85 KB in
  5 coordinator files) reproduces too.
- Q13 (d) READERS: none -- the new repository `C:/QAFactory/forge2-repo` holds `README.md` and `.git` only (one
  commit cb9d29e, V6); no existing reader can starve. Not re-run beyond that, per the dispatch edge. KNOWN MISSES:
  n/a for the same reason; miss 6: the plan's base is this repo's main at 8cc6b5192, read as committed.
- Q13 (e) FORKS decided by the Lead (F5, F6, F7, F13 per «Решила сама»): F5, F6, F7 consistent with the owner's
  words quoted (success definition needs a truth table; "перед релизом: 2"; P18 no money in files). F13 consistent
  with FR-12/AR-29 but leaves plan 1в issue rule 3 unreconciled (fix 12).
- Q4 CLASS-WIDE: NEEDS WORK. Each defect's siblings: absent-file behaviour -> all eleven `factory/data` files (fix
  17); gate scope by stage -> every G-rule over a section another stage may write (fix 5); dead-end refusals -> X6,
  C3-2 window, C3-6 "unknown key read -> refused" (that one is a factory defect, door named: fine), outward_write on
  multi-repo (fix 20); measurement statements -> 1б and 1в both (fix 16).
- Q6 DUPLICATION: NEEDS WORK -- fix 19. Two `journal.py` (forge C1-4, factory C4-6) are separate products, one
  ships: not a finding. Searched: spec §1 layout and §4 owns for repeated nouns (journal, hooks, secrets, launcher,
  ci).
- Q12 ONE ROAD: NEEDS WORK on residuals only (fix 19: two launchers in measure/, two CI job lists). Exclusions that
  STAY, named: functional checks only (owner 17.11.2026, architecture.md:64; spec axis 12); `md` the only delivery
  target in phases 0-4 (owner answer 4, plan line 1449; phase 7); Claude Code the first harness (spec §8; phase 9
  Codex); English person documents by default (axis 10, architecture.md:63). Python 3 host precondition: unnamed
  narrowing (fix 20). Searched: spec §1, §6, §8 and plan «Чего план сознательно не делает» for "only", "not",
  "phase".
- Q10 VARIETY: NEEDS WORK. Breaks on: a project with tests in a separate repository (fix 20); a large story whose
  stage-3 reads exceed the window (fix 9, axis 11); a story where a requirement's code is not written yet (fix 1,
  axis 4: blocks G4.2); Android/Gradle (fix 7: ignored build outputs). Elsewhere the factory degrades to a free
  agent by design (commands from knowledge, raw output kept, "no environment" with attempt).

V3 invariants (kept / broken: where).
- AR-1 kept in form; delivery-target rows and expectation-source kinds have no owning card (fix 15).
- AR-2 broken: spec C3-3 edge "no third way" (fix 1); C3-2 window refusal (fix 9); outward_write undefined (fix 20).
- AR-7 kept, but the §1 paraphrase "never mandatory" over-claims (record.py is mandatory by AR-14) and collides with
  P26 (fix 13).
- AR-10 kept (F12 generated "how checked"), on condition fix 5: a later stage's page must carry the G3 rules it can
  trigger.
- AR-14 kept (record.py, journal.py, knowledge.py, docs_build.py one writer each).
- AR-21 kept; C3-2 window refusal must not become a cut (fix 9 keeps "never cut").
- AR-22 kept at section level only (fix 21).
- AR-23 kept (`empty-outcomes.yaml`, X1, D-section words).
- AR-25 broken: states not enumerated (fix 4); window refusal (fix 9); rule 8 has no field (fix 8).
- AR-28 kept for record and gate-rules; other data files silent (fix 17).
- AR-29 broken: X6 closure by closed-list reason with a content refusal of other reasons (fix 1). Otherwise kept --
  §3 assigns cause/reason/critical mark to the performer and code checks presence and membership.
- P1 kept (rule 2 / `obtained_by`). P2 kept (walk; universality counter C1-2).
- P3 with P22: kept in placement (C4-1 seam, conductor.md); no contract for what the conductor receives and records
  (fold into fix 4: the seam's input = state + evidence + options, output = record rows `by: conductor`).
- P13: broken -- no carrier (fix 10).
- P16 with P19: kept (check `level`, `mode`; C2-3; G3.C).
- P20 kept (`expectation_source` kind or `none`; G3.1), conditional on fix 5.
- P27 broken where AR-29 is (fix 1); data/judgment/intent split otherwise kept.
- P31 kept (one launcher, one writer); residual duplicates fix 19.
- FR-4 broken (fix 10). FR-12 kept (F13, no phrase list). FR-38 kept (F12). FR-58 kept. FR-59 kept (`on_unknown`
  printed), conditional on fix 17.
- Touched and not named in §1: AR-6 mis-stated (fix 14); AR-8, AR-9, AR-11, AR-15, AR-16, AR-18, AR-20, P5, P15, P18
  (fix 22).

V4 feasibility.
- (i) data rows: code can decide X1, X2, X4, X5, G1.2, G1.3, G2.1, G2.2, G3.1-G3.4, G4.1, G4.3, G5.1-G5.3, G6.1-G6.3,
  D1, D2, W1 from ids, links, `seq` and presence. Judgment in disguise: X3 -- which created files are "the stage's"
  is decidable only with attribution (fix 7); X6 -- closure by list membership (fix 1); G4.2 -- unsatisfiable by its
  owner as ordered (fix 2); D3 -- unowned (fix 12); 1б "re-found findings" (fix 16) needs judgment. G4.1 is data
  only if revision never re-numbers (fix 6). Reverse: G3.C's "autotests not one-to-one with cases" can get code
  ADVICE (link ratio per check) for the critic -- advice, not ownership; no judgment row should move to code.
- (ii) ten rules: rule 1 holds (refusal mid-stage only X5 and person_address); rule 2 holds (`obtained_by`), except
  evidence (fix 13); rule 3 holds; rule 4 holds (record written by tool); rule 5 holds (exit_check any time); rule 6
  breaks (fix 1); rule 7 breaks for gate scope (fix 5) and revision (fix 6); rule 8 has no field (fix 8); rule 9 --
  states with no move: exit refused with debts (fix 4), window exceeded (fix 9), reason outside the list (fix 1);
  rule 10 holds (label by acceptor, unlabelled `unknown`); who the acceptor is in a C4-7 run is unstated (fold into
  fix 16). "A recorded word passes any gate": no carrier (fix 10). "Every refusal names a door": §2c `door` --
  holds, except C3-3's door that lists the very reasons that do not fit (fix 1).
- (iii) 1б ten checks vs §2a: needed 1 (W1) supported; needed 2 supported; needed 3 supported (context.py byte-equal
  sections); needed 4 supported except revision and after-approval mark (fix 6) and later-written requirements (fix
  5); needed 5 NOT supported -- returning a debt to an exited producer has no state (fix 4). Found 1 supported, but
  `findings` overloaded (fix 6); found 2 supported; found 3 NOT supported under parallel groups (fix 7); found 4
  supported (X2); found 5 supported in placement, blind to rows added after a critic gate (fix 5). "Чем это мерится":
  no fields (fix 16).
- (iv) roads to the person outside the five documents: the G5.P bug-or-not stop for an autotest red (fix 11); the
  conductor's own questions (not stated to go through ask.py, fix 11); `person_address` is an OPEN point with floor
  D3 at stage exit -- on a harness without it, a working file reaches the person mid-stage and is caught only after
  (acceptable as floor, but must be counted per plan 1в issue rule 4, fix 16); test-plan "details on request" from
  the record is the person's own choice (plan 1в issue rule 1: allowed).
- (v) cost: reachable in principle -- no form gates, conductor rare, critic once per gate, two rounds (F8), context
  assembled by code, stages mergeable as rows. Against it: six cold starts plus three critic contexts plus up to six
  fix-round relaunches, against free-agent stories of 7 and 12 minutes; per-row record.py calls (fix 18); fix rounds
  that relaunch a fresh performer (unstated, fix 4). The first measuring run must show, per stage and per agent:
  wall time, tokens with cache split, share of turns spent in factory tools (record.py separately), refusals by
  label, critic rounds, person-stop wait (answered by the launching model), and the same figures for the free agent
  -- so that a miss names which stage to merge. Measure this before phase 3, not at C4-7 (fix 18).

V5 owner's standing requirements.
- Not less than a free agent with one prompt: measured by C0-4, C0-5, C4-7; design gaps that make it do less: fixes
  1, 9, 20 (dead ends on unknown shapes).
- Gates do not hinder right actions and do not pass unfinished work: §3 + §2c; gaps fixes 1, 2, 7 (hinder) and 5, 10
  (pass unfinished / unbounded launching-model pass).
- Story record is not free text; checkable that everything found and needed is handed over: §2a + 1б mapping; gaps
  fixes 4 (needed 5), 6, 7 (found 3), 8, 16.
- A check with no earlier requirement is a defect: G4.1 + C3-1 edge; holds only if revision keeps order (fix 6).
- Person gets only the agreed documents: §2d, D3, ask.py; gaps fixes 11, 12.
- Universal across projects: §1 walk, C1-2 counter; gaps fixes 15 (axis 2/6/9 keys), 20 (multi-repo, Python host).
- Tests created by levels of the pyramid: check `level`, G3.3, G3.C, C2-3 -- realised.
- Test case and autotest not one-to-one: `links` many-to-many, G3.C -- realised; "obligation" must be defined (fix
  6).
- Code quality not worsened (CRAP, linters): C1-3 ratchets at zero, C1-6 CI; G4.4 for the project's test code --
  realised.

V6 premises re-run.
- The new repository is empty: `git -C C:/QAFactory/forge2-repo log --oneline -3` -> `cb9d29e Start the
  repository: forge 2 and the light QA factory`; `ls -a` -> `. .. .git README.md`. Reproduces (spec §1, §9; plan
  «Решила сама»).
- ao3-wrapper has no truth table (F5): `RUN-INSTRUCTIONS.md:37` reads "**Правды о продукте заранее нет** (на MyBooks
  был список 24 спорных мест)"; positive control `ls experiments/mybooks/truth/` -> `add-to-cart.yaml`. Reproduces.
- Extra: "правила координатора -- 5 файлов, 85 КБ": `tools/coordinator_rules.py` COORDINATOR_FILES summed with
  `os.path.getsize` -> `5 85826`. Reproduces.
- Extra, for fix 3: frozen `references/stages.json` `/stages[2]/required_outputs[2] understanding.md`, and the
  template's line 3 "Written by qa-requirements-tester at S2", line 6 "Checked ... against
  work/requirements-register.md" -- the understanding with its requirement list came after requirements.

V7 forks F1-F14 and silent decisions.
- F1 (a) one document, one stop: sound; the owner named "список источкинов и андестендинг" in one clause. Depends on
  fix 3.
- F2 (a): sound for manual failures; leaves autotest reds without a form (fix 11).
- F3 (a) no retro in phase 4: sound; the owner called it optional.
- F4 (a) language key, default English: sound, matches architecture.md:63.
- F5 (a) ao3 truth table in phase 0: sound, on one condition the spec omits: the table is frozen before any craft
  page or seeded set (C2-6) is written and its bugs are not used as seeds -- else the measurement trains on its test.
- F6 (a) 2 factory + 1 free per project, baseline 2 free: sound against "перед релизом: 2".
- F7 (a) tokens in files, money at display: sound against P18; P18's two-source price equality stays unaddressed
  (phase 8 at the latest).
- F8 (a) one call per gate, two rounds: sound; state that a fix round relaunches the performer and with what context
  (fix 4).
- F9 budgets: sound as a start; §3 already holds 38 rule rows against a ceiling of 45.
- F10 (a) Python + PyYAML pure: sound for this machine; the host precondition is an unnamed narrowing (fix 20).
- F11 (a) one file + lock: sound for the record; does not cover X3 attribution (fix 7).
- F12 (a) generated check section: sound (AR-10, one home).
- F13 (a): sound (FR-12, AR-29); D3 still needs an owner (fix 12).
- F14 (a): sound; one job list (fix 19); the push waits for the owner's word, as stated.
- Decided silently in the body (not in §7, not in «Решила сама»): who writes the can-fail record and the critic order
  (fix 2); understanding before requirements (fix 3); rows are never edited, only added and staled (fix 6); X6
  passes the gate before the reason is accepted (fix 1); the launching model holds every power of "the person" in
  comparison runs (fix 10); a context over the window is refused rather than routed (fix 9); `state` carries the
  after-approval mark (fix 6).

## Trail

Read whole: spec (399 lines); plan lines 1-45, 474-1061, 1062-1531; architecture.md 1-335; OWNER_PRINCIPLES.md
1-152. Read by line: factory-rules.md FR-4, FR-7, FR-8, FR-9, FR-12, FR-13, FR-33, FR-38, FR-47, FR-52, FR-58, FR-59
(sed ranges 53-60, 146-165, 181-195, 209-216, 272-300, 443-450, 483-500). Not read: plan catalogue «Что установлено»
(lines 131-473) and section 2 table (888-926) -- no finding rests on them. Commands and outputs are in V6. No probe:
plan gate, no code.

```json
{
  "verdict": "fit_with_fixes",
  "blockers": [],
  "fixes": [
    "1: spec 3 X6 and C3-3 edge, plan 1a rule 6 -- closed reason list with no exit breaks AR-29/AR-2; add an open reason row routed to the tier above, plus readiness and no-tool reasons. ARCH, blocks cards",
    "2: spec 3 G4.2 vs G4.C, plan positions 4-5 -- who writes the can-fail record and the order code-check / critic / docs / stop. ARCH, blocks cards",
    "3: plan 1v understanding lists requirements at the first stop while requirements are a stage-3 leave (D2 vacuous). ARCH, blocks cards",
    "4: spec 2a stage states not enumerated: exit refused, waiting at stop, held, fix round, stopped, shortfall to exited producer; conductor seam input/output. ARCH, blocks cards",
    "5: spec 2c gate rules scoped by stage: a requirement added at stage 4 escapes G3.1-G3.4 and G3.C; scope by section. ARCH, blocks cards",
    "6: spec 2a state mixes liveness and provenance; no revise op; supersedes link; derive after-approval; define obligation; split critic findings. ARCH, blocks cards",
    "7: spec X3/C3-4 world diff false debt with parallel groups; ignored files. ARCH",
    "8: plan 1a rule 8 has no holds/held_by field. ARCH",
    "9: spec C3-2 context over window refused with no move; route to conductor seam. ARCH, blocks cards",
    "10: P13/FR-4 no carrier; bound the launching model's powers in comparison runs. ARCH, blocks cards",
    "11: spec 2d no form for the bug-or-not stop on autotest reds; conductor questions via ask.py. ARCH",
    "12: spec 3 D3 owner per F13 is no owner; reconcile plan 1v issue rule 3. WORDING",
    "13: spec 1 AR-7 line vs P26 line on evidence by another road. WORDING",
    "14: spec 1 AR-6 restated as AR-13; restore the agent-is-never-a-read-route clause. WORDING",
    "15: no card for delivery-target rows, expectation-source kinds, md export of cases/bugs; C3-6 lacks axis 2/1/6/9 keys. ARCH",
    "16: plan 1b and 1v measurement statements have no field in 2f nor trace row. ARCH",
    "17: absent/unreadable data files other than gate-rules: one rows.py statement. WORDING",
    "18: batch record.py add; spike the six-stage chain cost before phase 3. ARCH (plan phases), not blocking",
    "19: two secret tables, two agent launchers in measure/, two CI job lists. WORDING",
    "20: outward_write undefined for multi-repo projects; Python host narrowing line. ARCH",
    "21: AR-22 field-level readers for readiness and executable_where. WORDING",
    "22: section 1 does not name AR-8, AR-9, AR-11, AR-15, AR-16, AR-18, AR-20, P5, P15, P18. WORDING"
  ],
  "class_completeness": "Plan gate on an empty repo: SIBLING_MAP not applicable (forge2 map starts empty, C1-7). Classes walked inside the artifact: absent-file behaviour over all factory/data files (fix 17); gate scope over every rule on a section another stage writes (fix 5); dead-end refusals X6, C3-2, outward_write (fixes 1, 9, 20); measurement statements 1b and 1v (fix 16).",
  "trail": {
    "read": [
      "docs/tasks/specs/20261125-forge2-light-factory-spec.md (whole)",
      "docs/tasks/specs/20261125-forge2-light-factory-plan.md (1-45, 474-1531)",
      "ai-packages/qa-factory/design/architecture.md (whole)",
      "docs/OWNER_PRINCIPLES.md (whole)",
      "ai-packages/qa-factory/design/factory-rules.md (FR-4, 7, 8, 9, 12, 13, 33, 38, 47, 52, 58, 59)",
      "experiments/ao3-wrapper/factory-vs-free-agent/RUN-INSTRUCTIONS.md (35-39)",
      "ai-packages/qa-factory/references/stages.json (understanding entries)",
      "ai-packages/qa-factory/references/templates/understanding.md (grep)"
    ],
    "reruns": [
      {"command": "git -C C:/QAFactory/forge2-repo log --oneline -3; ls -a C:/QAFactory/forge2-repo", "result": "cb9d29e Start the repository: forge 2 and the light QA factory; . .. .git README.md"},
      {"command": "sed -n 35,39p experiments/ao3-wrapper/factory-vs-free-agent/RUN-INSTRUCTIONS.md; ls experiments/mybooks/truth/", "result": "line 37: Pravdy o produkte zaranee net (Russian); control: add-to-cart.yaml"},
      {"command": "python -B -c sum getsize over tools/coordinator_rules.COORDINATOR_FILES", "result": "5 85826"},
      {"command": "grep -ciE per pattern over the spec: revis|update|edit|supersed; batch; held_by|holds; delivery target; expectation-source; repositor; export; person.s word|override|waiver (control: stale)", "result": "0; 0; 3 (none a field: lines 192, 233 prose); 2 (section 1 only, no card); 2 (section 1 only); 0; 0; 1 (section 1 claim only); control stale 7"},
      {"command": "python -B walk of references/stages.json for 'understanding'; grep -n -i requirement references/templates/understanding.md", "result": "/stages[2]/required_outputs[2] understanding.md; line 3 Written by qa-requirements-tester at S2; line 6 checked against work/requirements-register.md"}
    ]
  },
  "mutants": [],
  "mutants_none": "plan gate: no code and no tree under review, so no probe"
}
```
