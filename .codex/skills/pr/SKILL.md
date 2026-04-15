---
name: pr
description: >
  Prepare a completed feature for pull request creation in repositories that
  use concrete execution plans, specs, test specs, and GitHub workflows.
  Use when Codex should verify readiness, summarize the real diff, and draft
  a concise PR title and body grounded in what was actually verified.
---

# Pull request preparation

## Task

Prepare a completed feature for review with a clear PR summary grounded in
the spec, the plan, and the actual diff.

## Instructions

1. Read the concrete plan file, feature spec, and acceptance criteria.
2. Verify the relevant tests and validation commands passed before preparing the PR.
3. Check git status for uncommitted changes.
4. Confirm the branch is based on the correct base branch.
5. Summarize the change from the actual diff, not memory.
6. Draft a PR body that covers:
   - what changed
   - plan and spec references
   - test and validation results
   - compliance with requirements and non-goals
   - reviewer notes
   - post-merge follow-ups
7. Create or propose the PR only if the branch is ready.

## Gotchas

- Do not open a PR if tests are failing.
- Do not open a PR with uncommitted changes unless the user explicitly wants that workflow.
- Do not omit the concrete plan and spec references.
- Do not claim CI passed unless it actually did.

## Expected output

- readiness check results
- concise change summary from diff
- draft PR title and body or a created PR when appropriate
- explicit blockers if the branch is not ready
