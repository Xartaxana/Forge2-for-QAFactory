# AGENTS.md

- `CLAUDE.md`: worker rules, read by scout, builder, critic and designer.
- `forge/COORDINATOR.md`: rules of the Lead and the Architect.
- `forge/TESTING.md`: test rules for workers.
- `.claude/agents/` and `.codex/agents/` define the roles for each host. The four worker profiles share the role instructions and use their host's model bindings.
- `.claude/settings.json` registers Forge hooks for Claude Code. `.codex/hooks.json` registers the same checks for Codex after hook review.
- Git hooks are in `forge/hooks/git`. Git for Windows runs them with native Python on `PATH`.
