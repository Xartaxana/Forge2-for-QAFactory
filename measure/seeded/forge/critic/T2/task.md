# Review: journal.load returns Loaded with files (card C1-4 amendment)

given: input/spec.md (the dispatch the builder worked to, its DoD included), input/report.md (the builder's hand-back), input/change.diff (the change as a git diff against this tree), the tree itself (read-only)
non-goals: no edit of any file, no fix written, no change applied
handoff: none -- this session has no write tool: the whole verdict is your final message, nothing is read from a file
edges: the change is not applied: the tree holds the code before it, input/change.diff the change itself
DoD: the final message holds the verdict line `journal-loaded: fit | fit_with_fixes | blocker -- <why>`, then each finding numbered with file:line, whether it blocks, and a concrete failure scenario, then the trail of what was read; it is checked by reading
siblings: none -- one change under review

Review the change in input/change.diff against input/spec.md before it is accepted. The builder's hand-back is input/report.md.
