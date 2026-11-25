# Forge 2 and the light QA factory

Status: the plan is approved; phase 0 is in work. The light factory itself is not built yet.

## What this repository is for

- **The light factory** (not built yet) -- the QA factory rebuilt: work goes in stages, each stage in a fresh
  context with its own craft page; one story record is the only handoff form between stages; a gate at the exit of
  each stage does not hinder the performer inside the stage and does not let unfinished work pass.
- **Forge 2** -- the tooling and rules that build the light factory.

## Yardstick

The factory does everything a free agent with one prompt would do, and more: better and more predictably. A factory
that does less than a free agent is working wrong.

## Where the plan and the spec live

Byte copies, made in phase 0 card C0-1, are in `forge/specs/`:

- the plan: `forge/specs/20261125-forge2-light-factory-plan.md`
- the frame: `forge/specs/20261125-forge2-light-factory-spec.md`
- the other spec parts are in the same folder; each copy, its source path, source commit and sha256 are in
  `forge/specs/SOURCES.md`.

The layout of this repository and the rules in force are in section 1 of the frame (`Frame and invariants`); they
are not repeated here.

## The previous factory

FROZEN since 25.11.2026. Its state at the freeze is recorded in `C:/QAFactory/forge-repo/CURRENT_CONTEXT.md`.
Nothing is copied from it by default: what moves here is decided by the plan, item by item.

## Phases

| Phase | What | State |
|---|---|---|
| 0 | place, measuring projects, arm launcher, free-agent baseline (cards C0-*) | in work |
| 1 | rules, ratchets, token tools, hooks, CI (cards C1-*) | not started |
| 2 | cards C2-* of the spec | not started |
| 3 | cards C3-* of the spec | not started |
| 4 | cards C4-* of the spec | not started |
