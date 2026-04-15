---
name: ci
description: >
  Create or update a focused GitHub Actions workflow for a feature in
  repositories that use `AGENTS.md`, `docs/workflows.md`, a concrete plan
  file, `specs/[feature].md`, and `specs/[feature].test.md`. Use when
  Codex should create scoped, fast workflows with the right triggers,
  concurrency, and Android verification steps.
---

# CI workflow authoring

## Task

Create a concise, feature-scoped GitHub Actions workflow for automated
verification.

## Instructions

1. Read `AGENTS.md` for CI conventions, toolchain expectations, and do-not rules.
2. Read `docs/workflows.md` for Android verification and stability notes.
3. Read the concrete plan file, feature spec, and test spec to understand
   the paths, commands, and runtime boundaries involved.
4. Check existing workflows for naming, cache setup, and style consistency.
5. Scope triggers using `paths` so the workflow runs only when relevant files change.
6. Prefer `pull_request` plus `push` on `main` only unless the repo
   explicitly needs more triggers.
7. Add `concurrency` for expensive jobs.
8. Keep PR workflows fast; push heavy emulator checks into scheduled or
   manual smoke workflows unless the feature explicitly requires them on the
   PR path.
9. For generated-code Android features, include verification that proves the
   wiring exists, not just local JVM tests.

## Gotchas

- Do not guess toolchain setup if repo conventions are missing; inspect
  existing workflows or flag the gap.
- Do not trigger the workflow on unrelated files.
- Do not bloat the workflow with unnecessary jobs.
- Do not claim caching or CI optimization unless the repo actually supports it.

## Expected output

- a workflow file path
- a compact GitHub Actions workflow
- scoped triggers
- concurrency for expensive jobs when needed
- setup and cache steps that match repo conventions
- test and build commands aligned to the feature
