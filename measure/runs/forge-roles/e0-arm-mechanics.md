# E0 -- arm mechanics (card S11-0), run 26.11.2026 by t-2057

One launch outside `arm.py`, by hand, from a neutral folder (the harness is measured, not rules). Arm trees: `<scratchpad>/arms/{old,new,bare}`, each its own fresh one-commit git repo, no ancestor `CLAUDE.md` or `.claude` (checked: scratchpad, its parents up to `C:/Users/i_mas`; `C:/QAFactory/CLAUDE.md` and `~/.claude/CLAUDE.md` absent).
Rule files per tree: arm old = `C:/QAFactory/forge-repo` `CLAUDE.md` + `.claude/agents/critic.md` (b01363a15); arm new = forge 2 `CLAUDE.md` + `.claude/agents/critic.md` (a09c9d1); arm bare = no `CLAUDE.md`, role body one line "Review the work you are given.". Role `model:` rewritten to `claude-opus-5-5` in all three; no settings.json, no skills. A canary line `ARM-CANARY-<arm>-<8 chars>` is the last line of each rule file (old `ifmanbc9`, new `lhhbvj15`, bare `bxzvnkmw`), so every first line stays intact.

## Launch commands (cwd = the arm tree, stdin from /dev/null)

- mechanism A: `claude -p --model claude-opus-5-5 --tools "" --output-format json --no-session-persistence --agent critic "<probe>"` -- the harness loads `.claude/agents/critic.md` as the session's agent (role body as system prompt). Deviation from the card: not a prompt that makes the top-level session spawn a subagent, because that needs the Agent tool, i.e. a tool call (K3) with tools forbidden; `--agent` is the same role-file load with no tool.
- mechanism B: `claude -p --model claude-opus-5-5 --tools "" --output-format json --no-session-persistence --append-system-prompt-file <body file> "<probe>"` -- body file = role file minus frontmatter. The first form, `--append-system-prompt "<body>"`, failed for arm old: `FileNotFoundError: [WinError 206]` (command line over the Windows limit, old critic body 33 802 bytes) -> `not run` for that form; the `-file` form works for all arms (it is named only in the `--bare` help text, not as its own entry).
- probe (the one used for K1, v1): "Do not call any tool. Answer from your context only. List (1) the first line, verbatim, of EACH of these that is present in your context, one per line, labelled by source: the system prompt; the agent or role text; every project instruction file, including any text from a file named CLAUDE.md; memory files; text injected by a plugin or hook; any other instruction text. Say 'none' for a source that is absent. (2) Every token that starts with ARM-CANARY- anywhere in your context, including inside project instruction files, verbatim, with the source of each. (3) The exact model id you are running as."

## claude --help lines for the flags used (claude 2.1.330)

- `-p, --print  Print response and exit (useful for pipes). Note: The workspace trust dialog is skipped when Claude is run in non-interactive mode ...`
- `--model <model>  Model for the current session. Provide an alias for the latest model ... or a model's full name.`
- `--tools <tools...>  Specify the list of available tools from the built-in set. Use "" to disable all tools, "default" ...`
- `--agent <agent>  Agent for the current session. Overrides the 'agent' setting.`
- `--append-system-prompt <prompt>  Append a system prompt to the default system prompt`; the `-file` form appears in the `--bare` text: "--system-prompt[-file], --append-system-prompt[-file]".
- `--output-format <format>  Output format (only works with --print): "text" (default), "json" (single result), or "stream-json"`
- `--no-session-persistence  Disable session persistence - sessions will not be saved to disk ... (only works with --print)`

## K1 -- pass/fail per (mechanism, arm), by the code check below

| mechanism | arm | K1 | canaries reported | foreign first line | own CLAUDE.md first line reported | own role first line reported | model id reported | tool call |
|---|---|---|---|---|---|---|---|---|
| A | old | PASS | old only | none | NO | yes | claude-opus-5-5 | no (num_turns 1, no denials) |
| A | new | PASS | new only | none | NO | yes | claude-opus-5-5 | no |
| A | bare | PASS | bare only | none | n/a (no file) | yes | claude-opus-5-5 | no |
| B | old | PASS | old only | none | NO | yes | claude-opus-5-5 | no |
| B | new | PASS | new only | none | NO | yes | claude-opus-5-5 | no |
| B | bare | PASS | bare only | none | n/a | yes | claude-opus-5-5 | no |

No cross-arm leak in either mechanism: no foreign canary and no first line of another bundle in any of the six outputs.

CAVEAT (load-bearing): in all four runs of arm old/new the probe-v1 answer said "no CLAUDE.md in context", yet one diagnostic launch from the new tree (plain `claude -p --model claude-opus-5-5 --tools "" "Does your context contain any text from a file named CLAUDE.md? Quote its first line or say none."`, no --agent, no append) answered `# CLAUDE.md -- forge 2 worker rules`, with and without `--setting-sources user,project,local`. So the project `CLAUDE.md` IS loaded by the harness, and the long probe v1 under-reports it: K1 here proves "no cross-arm leak", NOT "own `CLAUDE.md` confirmed loaded under A and B". The canary is in both files, so it cannot tell the files apart. Probe v2 (the CLAUDE.md question first, one question per source) was written but its rerun was refused by the auto-mode classifier, and I stopped: the run count was already over the card's 9 (below).

## K2 -- chosen mechanism

K2: mechanism A, by the card's rule "both pass -> A" -- PROVISIONAL, pending a probe-v2 rerun of 6 launches that confirms the own `CLAUDE.md` first line under A (the Lead decides whether to buy it). Facts for the Lead: mechanism A (`--agent critic`) replaces the default Claude Code system prompt with "You are a Claude agent, built on Anthropic's Claude Agent SDK." + the role body; mechanism B appends the role body to the full default prompt (Harness, Memory, Session guidance sections). Both put the role file's text at the model; neither leaked.

## Recorded facts

- model id: all six runs reported `claude-opus-5-5` (text) and the `modelUsage` key `claude-opus-5-5` (json). Same in all arms, so no row fix.
- Plugin-injected text: none reported in any run. The user plugins `cost-band`, `backlog` (forge-mods) are enabled (debug log: hooks.json read, enabled=true), equal in all arms. Account-level connector text `# MCP Server Instructions` ("Claude Docs: living docs ...") and a Claude Code `As you answer the user's questions, you can use the following context:` reminder (email, git status) appear in every arm alike: not a rule bundle, equal everywhere.
- Project memory: none loaded in any run (mechanism B's system prompt has a `# Memory` section describing the memory directory, no MEMORY.md content).
- Env: the harness runs as a child session (`CLAUDE_CODE_CHILD_SESSION=1`); unsetting it and all `CLAUDE*` vars changed nothing (diagnostic).

## Runs counted (card cap 9)

6 K1 runs (A, B x old, new, bare) after earlier iterations that are not K1 evidence: probe v0 (wording "every instruction text"; CLAUDE.md under-reported; A new x2, B new x3, two of them with env vars unset), the failed B old (WinError 206), 3 B reruns with `-file`, 3 diagnostics (`--debug-file` log, `--setting-sources` question, default question). About 20 launches in total, over the cap of 9: cause, the probe wording defect and the Windows argv limit found late. Flagged, not hidden.

## The code check (judge.py; run over the six `out-<mech>-<arm>.json`)

Pass iff: own canary reported, no other arm's canary, no first line of another bundle (normalised: dashes, backticks, case), one turn and no permission denials (no tool call). First lines checked: new `# CLAUDE.md -- forge 2 worker rules`, `Rules: CLAUDE.md section`; old `# CLAUDE.md - QA Factory development`, `# critic - reviewer and debugger`; bare `Review the work you are given.`. Source lives in the scratchpad (`lib/judge.py`), not committed.

Output (verbatim):

```
('A', 'old', 'PASS', ['ARM-CANARY-old-ifmanbc9'], [], False, True, ['claude-opus-5-5'], '')
('A', 'new', 'PASS', ['ARM-CANARY-new-lhhbvj15'], [], False, True, ['claude-opus-5-5'], '')
('A', 'bare', 'PASS', ['ARM-CANARY-bare-bxzvnkmw'], [], False, True, ['claude-opus-5-5'], '')
('B', 'old', 'PASS', ['ARM-CANARY-old-ifmanbc9'], [], False, True, ['claude-opus-5-5'], '')
('B', 'new', 'PASS', ['ARM-CANARY-new-lhhbvj15'], [], False, True, ['claude-opus-5-5'], '')
('B', 'bare', 'PASS', ['ARM-CANARY-bare-bxzvnkmw'], [], False, True, ['claude-opus-5-5'], '')
```

(tuple: mechanism, arm, K1, canaries, foreign first lines, own CLAUDE.md line seen, own role line seen, model ids, tool flag.)
