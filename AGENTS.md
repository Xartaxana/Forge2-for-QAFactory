# AGENTS.md

- `CLAUDE.md`: worker rules, read by scout, builder, critic and designer.
- `forge/COORDINATOR.md`: rules of the Lead and the Architect.
- `forge/TESTING.md`: test rules for workers.
- `.claude/agents/`: role files, each points to one section of `CLAUDE.md`.
- `.claude/settings.json`: hooks; they do not run under this harness, pre-push and CI still judge.
