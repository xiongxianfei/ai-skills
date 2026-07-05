# PR Handoff: Flashcard And Quiz Generator Skills

## Result

- Skill: pr
- Status: opened
- Branch: `docs/flashcard-and-quiz-skills`
- Base: `main`
- PR title: `feat: add flashcard and quiz generator skills`
- PR URL: https://github.com/xiongxianfei/skillsmith/pull/32
- Open blockers: none
- Readiness: PR opened; hosted CI in progress at handoff

## Readiness Checks

| Check | Result | Evidence |
| --- | --- | --- |
| Working tree | pass | `git status --short --branch` was clean before PR creation. |
| Branch and base | pass | Current branch is `docs/flashcard-and-quiz-skills`; base is `main`; verify confirmed branch base equals local `main` at `4ae3baaa555c792a81fb7c558616bfe5e09ad4bf`. |
| Commits scoped | pass | Branch contains the workflow-managed proposal, spec, plan, implementation, review, explain-change, verify, and PR handoff commits for this change. |
| Validation | pass | Verify report records local validation passing: skill validation, unit tests, README sync, whitespace check, schema/fixture parsing, direct fixture validation, and no-integration diff check. |
| CI status | pending | GitHub reports `Validate skill files` is `IN_PROGRESS` at handoff. |
| Lifecycle state | pass | `docs/plan.md`, plan body, and `change.yaml` showed final closeout, branch-ready, next stage `pr` before PR open. |
| Required change pack | pass | `change.yaml`, `explain-change.md`, `verify-report.md`, reviews, review log, and post-change evidence exist under `docs/changes/2026-07-04-flashcard-and-quiz-skills/`. |
| Review resolution | pass | PR review material findings were accepted and closed in `review-resolution.md`; needs-decision count is 0. |
| Secrets/debug artifacts | pass | Verify found no scripts, secrets, API credentials, dependency changes, installer changes, validator changes, CI changes, or unrelated skill changes. |

## PR Body

## Summary
- Add two focused prompt skills: `flashcard-generator` and `quiz-generator`.
- Add local learning-design references, skill-specific quality references, reference JSON Schemas, eval fixtures, README discovery updates, and lifecycle evidence.
- Keep the first slice prompt-centered with no runtime integration, validator changes, CI changes, installer changes, or external services.

## Why
- Flashcards and quizzes solve different learning jobs and need different triggers, workflows, output contracts, and quality bars.
- The accepted direction requires objectives and a compact knowledge map before artifact generation so the skills do not become shallow summary/list generators.
- Canonical JSON plus Markdown gives reviewers and downstream export workflows a stable structure without adding executable schema validation in this first slice.

## Spec / plan / architecture
- Proposal: `docs/proposals/2026-07-04-flashcard-and-quiz-skills.md`
- Spec: `specs/flashcard-and-quiz-skills.md`
- Test spec: `specs/flashcard-and-quiz-skills.test.md`
- Architecture / ADRs: not required; spec-review R1 records the accepted pure-prompt boundary.
- Plan: `docs/plans/2026-07-04-flashcard-and-quiz-skills.md`
- Explain-change: `docs/changes/2026-07-04-flashcard-and-quiz-skills/explain-change.md`
- Verify report: `docs/changes/2026-07-04-flashcard-and-quiz-skills/verify-report.md`

## What changed
- Added `skills/flashcard-generator/SKILL.md` with trigger-forward frontmatter, `$ARGUMENTS`, objective extraction, knowledge mapping, card-quality validation, source boundaries, output format, canonical JSON, export section, and both-output fallback.
- Added `skills/quiz-generator/SKILL.md` with trigger-forward frontmatter, `$ARGUMENTS`, objective extraction, knowledge mapping, quiz blueprinting, MCQ rules, item validation, source boundaries, output format, canonical JSON, export section, and both-output fallback.
- Added compact local learning-design references and skill-specific quality references for both skills.
- Added reference JSON Schemas for canonical flashcard and quiz JSON, explicitly not enforced by CI in this slice.
- Added eval fixtures for both skills covering normal use, indirect triggers, source-grounding boundaries, non-trigger cases, and both-output requests.
- Updated `README.md` so both skills appear in the skill table, command lists, usage examples, and skill details.
- Added proposal/spec/test-spec/plan/review/evidence/explain/verify artifacts for the workflow-managed change.

## Tests and verification
- [x] `python tests/validate_skills.py` - passed for 13 skills with the known non-blocking grandfathered-evals warning for unrelated older skills.
- [x] `python -m unittest discover tests` - passed, 31 tests.
- [x] `python tests/check_readme_sync.py` - passed.
- [x] `git diff --check main...HEAD` - passed.
- [x] JSON/YAML parse check for change metadata, fixtures, and schemas - passed.
- [x] Direct `validate_cases_file` invocation for both new eval fixture files - passed.
- [x] `wc -l skills/flashcard-generator/SKILL.md skills/quiz-generator/SKILL.md` - 149 and 170 lines after PR review resolution.
- [x] Scoped no-integration diff-name check - no CI, validator, installer, or unrelated skill changes.
- [ ] CI - `Validate skill files` in progress at handoff.

## Requirement coverage
- R1-R4, AC5 -> T7, T8, CMD2 -> required skill frontmatter, `$ARGUMENTS`, `## Output Format`, no optional frontmatter.
- R5-R7, R30, AC7 -> T1, T2, T5, T6 -> flashcard-only, quiz-only, neither-skill, and both-skill trigger evidence.
- R8-R15, AC8-AC9 -> T7, T9, MP1 -> flashcard workflow and output contract.
- R16-R20, AC8-AC9 -> T8, T10, MP2 -> quiz workflow, blueprinting, MCQ rules, feedback, and output contract.
- R21-R25, AC10 -> T12, T13 -> local references and reference-only JSON Schemas.
- R26, E4, EC4 -> T6, T11, MP4 -> both-output fallback with shared objectives/map and separate JSON payloads.
- R27-R30, AC6-AC7 -> T1-T6, CMD1, CMD2 -> eval fixtures and source-grounding boundaries.
- R31-R32, AC3, AC11 -> T14, CMD4 -> README synchronization and contributor-doc no-change rationale.
- R33-R35, AC12 -> T13, T15, CMD2, CMD6 -> no forbidden integrations, no high-stakes guarantees, prompt line limits.

## Review resolution summary
- Accepted: 2
- Rejected: 0
- Deferred: 0
- Partially accepted: 0
- Needs decision: 0
- Review-resolution: `docs/changes/2026-07-04-flashcard-and-quiz-skills/review-resolution.md`

## Risks and rollback
- Static prompt inspection and eval fixtures cannot guarantee every future model output will satisfy the prompt contract.
- Reference schemas are documentation contracts only; executable schema validation remains a follow-up.
- Duplicated learning-design references may need sync tooling later if drift becomes painful.
- Rollback is additive: remove the two skill directories, their eval fixtures, README entries, and change-local lifecycle artifacts.

## Reviewer notes
- Focus review on whether the two skills stay distinct while still handling combined flashcard-and-quiz requests predictably.
- Confirm source-grounding, unsupported inference, high-stakes boundaries, and reference-schema-only wording are clear enough.
- Hosted CI is expected to run after PR open; it was in progress at handoff.

## Follow-ups
- Executable JSON Schema validation after output shapes stabilize.
- Anki TSV export hardening and optional AnkiConnect integration.
- QTI/Moodle/H5P export profiles.
- Adaptive remediation or repair-loop workflows.
- High-stakes exam-prep review policy if the project later supports regulated or exam-sensitive contexts.

## Opened PR

- URL: https://github.com/xiongxianfei/skillsmith/pull/32
- State: open
- Draft: no
- Initial hosted CI status: `Validate skill files` in progress at handoff.
