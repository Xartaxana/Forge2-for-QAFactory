# BOOT: what forge 2 builds, how and why

## What we build and why

We build the light test factory, set out in nine provisions below (plan 1)
Forge 2 is the rules and tools that build and change the light factory; its first requirement: no code that hinders the agent acting correctly, and token-saving tools from day one (plan 3)
Why light: in two comparison runs the free agent with one prompt gave a report in minutes, the old factory none in hours; the new factory does no less than the free agent, and more, with better quality and predictability (plan 7.1)
Growth guard: over half of the old factory's pile nodes (about 1270 of 2063) fixed its own code and rules, not testing, so growth is held by seven mechanisms, each with a number or a run (plan 4)
Why this page: every forge 2 session knows from its first turn what we build, how and why (plan 3.9)

## The yardstick

The yardstick is the free agent with one prompt (plan 3.9)
Goal: not worse than the free agent on any row of the comparison table, and better on requirements, traceability and repeatability (plan 7.2)
A behaviour change of the factory is accepted only by a run on a measured project against the truth table and against the free agent; ordinary tests check tool code only (plan 3.1)
Worse than the free agent on even one row of the comparison table, or over five times its time and cost: the change is not accepted (plan 4.1)
Time and cost of a story: at most twice the free agent's as the goal, at most five times as the ceiling (plan 7.3)

## The nine provisions

1. Work goes in stages: each has a fresh context and its own craft page, one story record passes between them, code (not a model) starts the next stage, and inside a stage the executor acts as a free agent (plan 1.1)
2. Role craft is kept as pages, one home per rule; each page says how the work will be judged, and the critic judges by that same page (plan 1.2)
3. The story record is one data file with known sections; everything passed between stages goes through it; code owns its form, the executor writes its content (plan 1.3)
4. Gates stand between stages: nothing passes until the necessary is finished, and acting is never hindered; a gate checks the record at stage exit, not the moves (plan 1.4)
5. The critic is part of a gate only where judgment is needed: three gates of six to start, and its placement is data changed by measurement (plan 1.5)
6. Project knowledge: onboarding looks at the project itself, asks at most ten main things and the rest once when first needed; an answer is remembered (plan 1.6)
7. The person is about intent: asked once, in plain words, only after the executor tried to find the answer; the answer is kept verbatim and reaches whoever acts on it (plan 1.7)
8. Code is tools the executor calls plus a few hooks; neither knows the harness: the harness form is a host-profile data row (plan 1.8)
9. Routes are data rows with one launch road: story, bug, pre-code, rerun, exploration, onboarding; a route is a list of stages (plan 1.9)

## Six stages and where the person stands

Stages: 1 sources and understanding; 2 product look and smoke; 3 requirements and check plan (checklist and levels); 4 cases, autotests and manual passes, by requirement groups; 5 red analysis; 6 report and delivery (plan 1.1)
The factory stops for the person only at: a critical question; the sources list and understanding; the test plan (checklist and test levels); bug or not; before an MR and any outward write (plan 1.7)

## Decisions and state

decided by the owner: forge/owner-words.yaml
phase 1: the forge 2 skeleton is being built; the session move is pending -- 2026-11-26
