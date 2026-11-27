# AGENTS.md

- `CLAUDE.md`: worker rules, read by scout, builder, critic and designer.
- `forge/COORDINATOR.md`: rules of the Lead and the Architect.
- `forge/TESTING.md`: test rules for workers.
- `.claude/agents/`: Claude Code roles; the four worker profiles share role instructions and use their host's model bindings.
- `.codex/agents/`: Codex roles; the four worker profiles share role instructions and use their host's model bindings.
- `.claude/settings.json`: registers Forge hooks for Claude Code.
- `.codex/hooks.json`: registers the same checks for Codex after hook review.
- `forge/hooks/git`: Git hooks; Git for Windows runs them with native Python on PATH.
