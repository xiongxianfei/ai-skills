---
name: ci
description: Generate a focused GitHub Actions workflow for a feature in repositories that use AGENTS.md, specs/[feature].md, and specs/[feature].test.md. Use when Codex should create or update a scoped CI workflow that runs only for relevant paths and follows repo conventions for setup, caching, and test execution.
---

# CI Workflow Authoring

## Task

Create a concise, feature-scoped GitHub Actions workflow for automated testing.

## Instructions

1. Read `AGENTS.md` for CI conventions such as toolchain, JDK or runtime, package manager, and caching.
2. Read the feature spec and test spec to understand the source paths and test commands involved.
3. Check existing workflows for naming and style consistency.
4. Scope triggers using `paths` so the workflow only runs when relevant files change.
5. Separate unit and integration tests when the repo benefits from staged execution.
6. Keep the workflow compact and aligned with the repo's patterns.

## Gotchas

- Do not guess toolchain setup if the repo conventions are missing; ask or flag the gap.
- Do not trigger the workflow on unrelated files.
- Do not bloat the workflow with unnecessary jobs.
- Do not claim caching or CI optimization unless the repo actually supports it.

## Expected Output

- a workflow file path
- a compact GitHub Actions workflow
- scoped triggers
- setup and cache steps that match repo conventions
- test commands aligned to the feature
