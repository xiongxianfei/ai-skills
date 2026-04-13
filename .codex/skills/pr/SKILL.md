---
name: pr
description: Prepare a feature for pull request creation in repositories that use specs/[feature].md and GitHub CLI workflows. Use when Codex should verify acceptance criteria, summarize changes against the base branch, ensure tests pass, and draft a concise PR body before opening or proposing a PR.
---

# Pull Request Preparation

## Task

Prepare a completed feature for review with a clear PR summary grounded in the spec and actual diff.

## Instructions

1. Read the feature spec and acceptance criteria.
2. Verify tests pass before preparing the PR.
3. Check git status for uncommitted changes.
4. Confirm the branch is based on the correct base branch.
5. Summarize the change from the actual diff, not memory.
6. Draft a PR body that covers:
   - what changed
   - spec reference
   - test results
   - compliance with requirements and non-goals
   - reviewer notes
   - post-merge follow-ups
7. Create or propose the PR only if the repo is ready.

## Gotchas

- Do not open a PR if tests are failing.
- Do not open a PR with uncommitted changes unless the user explicitly wants that workflow.
- Do not omit the spec reference when the repo uses spec-driven development.
- Do not claim CI passed unless it actually did.

## Expected Output

- readiness check results
- concise change summary from diff
- draft PR title and body or a created PR when appropriate
- explicit blockers if the branch is not ready
