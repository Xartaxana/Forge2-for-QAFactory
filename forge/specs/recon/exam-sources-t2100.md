# Exam sources for rebuilding the role exams (recon t-2100, 27.11.2026)

Input to worklist row wl-4 and the owner's word W-202: one exam per forge role, assembled from the item types that ranked models in the owner's earlier exams. Source repository: Xartaxana/Operating-System-for-LLMs (private; read with `gh api repos/Xartaxana/Operating-System-for-LLMs/contents/<path>`). Carriers are in Russian; this digest paraphrases. Spot-check by the Lead: the Lead v2 "opus" runs were claude-opus-4-8, not claude-opus-5 (docs/tasks/2026-08-18_lead-exam-v2.md, row B6) -- confirmed.

## Carriers with per-item per-model results

| role | carrier | models as written | per-item results |
|---|---|---|---|
| critic | PROCESS/CRITIC_EXAM.md (exams 1-4, keys :75-309, runs :315-678); PROCESS/critic_exam_{1,2,3}_dispatch.md; docs/tasks/2026-08-16_critic-exam-v2-key-SPENT.md | opus, sonnet, claude-opus-5 (exams 3-4) | yes |
| Lead | PROCESS/LEAD_RANKING_EXAM.md (v1 :59-161, v2 :273-378); docs/tasks/2026-08-18_lead-exam-v2-key-SPENT.md :18-42 | v1 Opus, Sonnet, gemini-2.5-flash; v2 claude-opus-4-8, claude-fable-5 | v2 yes; v1 only K3, K5 |
| scout | PROCESS/SCOUT_GOLDEN_SET.md; docs/tasks/2026-08-16_scout-exam-v2-draft.md :28-39; docs/tasks/2026-08-16_dog-delivery-scout-exam.md :27-28 | haiku, sonnet (no version) | v2 partial |
| designer | dog-delivery DAG :44-55 (no key file found) | opus, sonnet | totals only |
| coordinator economy | PROCESS/DEPLOYMENT_ECONOMY_EXAM.md (runs :292-331); docs/EXAM_RESULTS.xlsx; docs/tasks/2026-07-15_economy-exam-runs5-6.md; docs/exam_fixtures/set2/ground_truth/traps.md | sonnet-5, fable-5, opus-4-8 | per task and cell |

## Item types that ranked models in more than one exam or run

1. Fabricated witness, independently reproduced (the claimed test count contradicts the diff): critic 1-4 and v2 W1, Lead v1 K5, Lead v2 A1. Opus held it in the critic exams; Sonnet credited it or asked the same executor to rerun; claude-opus-4-8 held it 1 of 2 in Lead v2, claude-fable-5 held it.
2. A negative claim with no same-shape control, or a false one ("read nowhere else", "no other writers"): critic 1 T-K3, critic v2 N-BAD (Opus yes, Sonnet no); Lead v1 K3 (one run of two); scout v2 (haiku fails).
3. Second-order trap: a tautological or vacuous test (expectation computed by the code under test; a mock that keeps the test green without the fix): Lead v2 A2 (opus-4-8 0/2, fable-5 yes), critic v2 D3 (Sonnet half-approved).
4. A process rule broken inside the work (a `critic: skipped` that is illegal for that diff): Lead v2 A3, only fable-5.
5. Scout carrier errors: docstring trusted over code, count by word, the twin file read instead of the named one: scout v2 Q1, Q6-Q8 (haiku 2/10 twice, sonnet 10/10).
6. A hidden spec fork that must go up: designer v2 M1-M4 (Opus pass, Sonnet fail); economy set2 currency and duplicate questions (fable-5 policy cells only).
7. A shared-resource race: critic v2 D1 (Opus 2 of 3, Sonnet no).

## Items no model solved (candidates for the "fails with and without rules" part)

- critic 4 D2: a console encoding crash (cp1251) in json.dumps -- claude-opus-5 missed.
- critic 2 D3: an API contour and a toolkit twin left unnamed -- opus partial 2/2; critic 1 D3 twin: only the first opus run.
- economy: "2+2*2=6" priority bug, solo arms of sonnet-5, opus-4-8, fable all missed; M6 a boundary with no test (sonnet-5 and fable-5, five repeats); set2 fork S1 "develop or rewrite" never escalated by any cell.
- critic 2 T-K3: 0/2, but its key was annulled as defective -- not reusable as it stands.

## Saturated (no discrimination)

Lead v1 K1, K2, K4, K6; critic 1 D1; Lead v2 B1-B3, C1; scout golden set v1; shadow replay (sonnet 5/8 = opus 5/8).

## Limits of this recon

No exam ran Sonnet, Opus and Fable on the same items. No per-item grid for scout v2 beyond named questions, designer v2, judge calibration, Lead v1 K1-K2/K4/K6. Economy mutation keys M1-M7 have no definition list in the carriers read. Manifests, sandbox fixtures and tools/exam_runner.py were not read.
