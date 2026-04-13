---
description: Create a pull request for a completed feature. Links spec, lists changes, runs final checks.
argument-hint: [feature name]
allowed-tools: Read, Bash(git *), Bash(gh *)
model: sonnet
---

You are creating a PULL REQUEST for a completed feature.

## Your Task

Create a PR for: $ARGUMENTS

## Pre-PR Checks

1. Read `specs/$ARGUMENTS.md` for the acceptance criteria
2. Run ALL tests — confirm they pass
3. Check git status — are there uncommitted changes?
4. Check that the branch is up to date with main

## Process

1. Verify acceptance criteria from the spec:
   - [ ] All MUST requirements implemented
   - [ ] All edge cases handled
   - [ ] Tests pass
   - [ ] Code review completed (check for review notes)

2. Generate a change summary by diffing against main:
   ```bash
   git diff main --stat
   git diff main --name-only
   ```

3. Create the PR using `gh`:
   ```bash
   gh pr create \
     --title "feat([feature-name]): [concise description]" \
     --body "[generated from template below]"
   ```

## PR Body Template

```markdown
## What
[One sentence: what this PR does]

## Spec
[Link: specs/[feature-name].md]

## Changes
- [file/module]: [what changed and why]
- ...

## Test Results
- [x] Unit tests pass ([N] tests)
- [x] Integration tests pass ([N] tests)
- [x] CI workflow passes

## Spec Compliance
- [x] All MUST requirements met
- [x] All edge cases handled
- [x] Non-goals respected

## Review Notes
[Any context the reviewer should know — tricky decisions, known limitations, follow-up items]

## Post-Merge TODO
- [ ] Update docs/workflows.md if system flow changed
- [ ] Update CLAUDE.md if new patterns were established
- [ ] Add gotchas to spec if Claude got something wrong during implementation
```

## Rules
- Do NOT create the PR if tests fail. Fix first.
- Do NOT create the PR if there are uncommitted changes. Commit first.
- Link the spec in the PR body — reviewers need the contract.
- Keep the PR title under 72 characters.
- If this is the first PR, ask me to confirm the base branch.
