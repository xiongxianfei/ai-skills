# Explain Change: Flashcard And Quiz Generator Skills

## Summary

This change adds two focused learning-artifact skills:

- `flashcard-generator` for source-grounded, spaced-repetition-ready flashcards.
- `quiz-generator` for source-grounded diagnostic quizzes and assessment items.

The change keeps the skills separate, gives each one its own prompt, references, schema contract, output format, quality bar, and eval fixture, and records lifecycle evidence from proposal through implementation review. It intentionally stays prompt-first: no direct AnkiConnect, LMS, QTI, Moodle, H5P, external service, runtime dependency, live model CI, executable schema validation, installer behavior, or CI behavior was added.

## Problem

The accepted proposal records that Skillsmith should support high-quality learning artifact generation without collapsing flashcards and quizzes into one broad study-artifact skill. Flashcards optimize for durable recall and long-term retention; quizzes optimize for diagnostic assessment, feedback, and transfer. The main design risk was a shallow generator that turns source text directly into broad cards or flat quiz questions without learning objectives, knowledge mapping, source grounding, validation, or exportable structure.

## Decision Trail

| Decision | Where recorded | Effect on diff |
| --- | --- | --- |
| Use two production skills, not one combined skill | `docs/proposals/2026-07-04-flashcard-and-quiz-skills.md` | Added `skills/flashcard-generator/` and `skills/quiz-generator/`; did not add `study-artifact-generator`. |
| Use compact local shared learning-design references, not a third runtime skill | Proposal and `specs/flashcard-and-quiz-skills.md` R21-R23 | Added duplicated `references/learning-design.md` files and skill-specific quality references. |
| Require objectives and knowledge map before generation | Spec R9-R10, R16 | Both `SKILL.md` workflows require objective extraction and compact knowledge maps before artifacts. |
| Use canonical JSON plus Markdown | Spec R15, R20, R24-R25 | Both prompts include canonical JSON blocks and reference JSON Schema files. |
| Keep schemas reference-only | Spec R25, R33 | Added schema files as documentation contracts only; no validator or CI enforcement changed. |
| Add eval fixtures before prompt implementation | Spec R27-R30 and test spec M1 | Added eval fixtures first in M1 and recorded baseline evidence. |
| Record post-change prompt and smoke evidence | Test spec M3 | Added `post-change-evidence.md` before final implementation review. |

Architecture was recorded as not required in `docs/changes/2026-07-04-flashcard-and-quiz-skills/reviews/spec-review-r1.md` because the slice is additive prompt, reference, schema-reference, eval, README, and lifecycle documentation work.

## Diff Rationale By Area

| File or area | Change | Reason | Source artifact | Test/evidence |
| --- | --- | --- | --- | --- |
| `docs/proposals/2026-07-04-flashcard-and-quiz-skills.md` | Added and accepted the proposal. | Establishes the product direction, alternatives, non-goals, and rollout path. | Proposal workflow; accepted status. | Proposal review R1. |
| `specs/flashcard-and-quiz-skills.md` | Added approved behavioral spec. | Converts the proposal into trigger, workflow, output, safety, compatibility, and acceptance requirements. | Spec R1-R35, AC1-AC12. | Spec review R1. |
| `specs/flashcard-and-quiz-skills.test.md` | Added proof map. | Maps requirements and edge cases to eval fixtures, prompt inspection, manual smoke evidence, and validation commands. | Test spec T1-T15, MP1-MP4, CMD1-CMD6. | Test-spec-review R1. |
| `docs/plans/2026-07-04-flashcard-and-quiz-skills.md` | Added and updated execution plan across M1-M3. | Sequenced evals, prompt packages, and evidence into reviewable milestones. | Plan review R1. | M1-M3 implementation and code-review records. |
| `docs/changes/2026-07-04-flashcard-and-quiz-skills/change.yaml` | Added change metadata and validation ledger. | Keeps the active lifecycle state, artifact paths, reviews, and command evidence in one change-local record. | Workflow metadata requirement. | YAML parse checks; review records. |
| `tests/evals/skills/flashcard-generator/cases.yaml` | Added flashcard eval scenarios. | Provides normal, indirect trigger, source-boundary, non-trigger, and both-output evidence for the new skill. | Spec R27-R30; test spec T1, T3, T5, T6. | Direct fixture validation; full skill validation after M2. |
| `tests/evals/skills/quiz-generator/cases.yaml` | Added quiz eval scenarios. | Provides diagnostic quiz, MCQ quality, unsupported material, non-trigger, and both-output evidence. | Spec R27-R30; test spec T2, T4, T5, T6. | Direct fixture validation; full skill validation after M2. |
| `docs/changes/2026-07-04-flashcard-and-quiz-skills/baseline-evidence.md` | Recorded that skill prompts were intentionally absent during M1. | Shows eval fixtures were added before prompt implementation. | M1 plan and test spec. | M1 code review. |
| `skills/flashcard-generator/SKILL.md` | Added flashcard prompt with required frontmatter, `$ARGUMENTS`, workflow, quality rules, source boundaries, output format, canonical JSON, and fallback for combined requests. | Implements flashcard requirements and trigger behavior. | Spec R1, R3-R5, R8-R15, R26, R34-R35. | `validate_skills.py`; prompt inspection; M2 and M3 reviews. |
| `skills/flashcard-generator/references/learning-design.md` | Added compact shared principles. | Keeps the skill portable while sharing learning-design rules. | Spec R21. | M2 review. |
| `skills/flashcard-generator/references/card-quality.md` | Added flashcard-specific card quality checks. | Keeps flashcard atomicity, usefulness, card types, and reject/rewrite rules out of the main prompt body. | Spec R12-R14, R22. | M2 review. |
| `skills/flashcard-generator/schemas/flashcard.schema.json` | Added reference JSON Schema. | Documents canonical JSON fields and shape without adding executable validation. | Spec R24-R25. | JSON parse checks; M2 review. |
| `skills/quiz-generator/SKILL.md` | Added quiz prompt with required frontmatter, `$ARGUMENTS`, workflow, blueprinting, MCQ rules, source boundaries, output format, canonical JSON, and fallback for combined requests. | Implements quiz requirements and trigger behavior. | Spec R2-R4, R6, R8-R11, R16-R20, R26, R34-R35. | `validate_skills.py`; prompt inspection; M2 and M3 reviews. |
| `skills/quiz-generator/references/learning-design.md` | Added compact shared principles. | Keeps the skill portable while sharing learning-design rules. | Spec R21. | M2 review. |
| `skills/quiz-generator/references/question-quality.md` | Added quiz-specific item quality checks. | Captures objective alignment, answerability, ambiguity, feedback, MCQ, and reject/rewrite rules. | Spec R17-R19, R23. | M2 review. |
| `skills/quiz-generator/schemas/quiz-item.schema.json` | Added reference JSON Schema. | Documents canonical JSON fields and shape without adding executable validation. | Spec R24-R25. | JSON parse checks; M2 review. |
| `README.md` | Added both skills to the skills table, install command lists, usage examples, and skill details. | Keeps public catalog and slash-command docs synchronized. | Spec R31. | `python tests/check_readme_sync.py`. |
| `docs/changes/.../post-change-evidence.md` | Added prompt-inspection and manual smoke evidence. | Provides reviewer-visible proof for objectives, knowledge maps, output contracts, unsupported-material handling, both-output fallback, no integration, and high-stakes boundaries. | Test spec T9-T11, T13, T15; MP1-MP4. | M3 code review. |
| `docs/changes/.../reviews/*.md` and `review-log.md` | Added proposal, spec, plan, test-spec, code-review, and metadata-cleanup review records. | Records lifecycle review decisions, no-material-finding outcomes, validation evidence, and stage handoffs. | Workflow review requirements. | Review artifacts and review log. |
| `docs/plan.md` | Added and updated the active plan index entry. | Keeps the repository-level plan index pointed at the current lifecycle stage. | Plan lifecycle bookkeeping. | Review and metadata cleanup checks. |

## Tests Added Or Changed

No executable validator code was added. The test surfaces are static eval fixtures and workflow evidence:

| Test or proof ID | Artifact | What it proves |
| --- | --- | --- |
| T1, T3, T5, T6 | `tests/evals/skills/flashcard-generator/cases.yaml` | Flashcard normal use, indirect triggers, unsupported facts, non-trigger boundaries, and both-output behavior are reviewer-visible. |
| T2, T4, T5, T6 | `tests/evals/skills/quiz-generator/cases.yaml` | Quiz normal use, MCQ quality, unsupported facts, non-trigger boundaries, and both-output behavior are reviewer-visible. |
| T7, T8, T12, T13, T14, T15 | Prompt, reference, schema, README, and no-integration inspection | The two skill packages match structure, references, schema-reference-only policy, README sync, privacy, and safety requirements. |
| T9, T10, T11; MP1-MP4 | `post-change-evidence.md` | Prompt inspection and manual smoke proof cover Anki-style flashcards, diagnostic quiz behavior, unsupported material, and both-output fallback. |

The chosen level is appropriate because the first slice is pure prompt content and reference files. Live model calls, executable schema validators, direct export integrations, and CI enforcement were explicitly out of scope.

## Validation Evidence Before Final Verify

Validation was run during implementation and review stages. The latest recorded evidence includes:

- `python tests/validate_skills.py`
  - Passed for 13 skills.
  - Known non-blocking warning remains for unrelated grandfathered skills without eval fixtures.
- `python -m unittest discover tests`
  - Passed; 31 tests.
- `python tests/check_readme_sync.py`
  - Passed.
- `git diff --check`
  - Passed during implementation.
- `git diff --check HEAD^..HEAD`
  - Passed during review checks.
- `wc -l skills/flashcard-generator/SKILL.md skills/quiz-generator/SKILL.md`
- `flashcard-generator`: 149 lines after PR review resolution.
- `quiz-generator`: 170 lines after PR review resolution.
- YAML parse checks for `docs/changes/2026-07-04-flashcard-and-quiz-skills/change.yaml`
  - Passed.
- Direct fixture validation for both new eval files in M1
  - Passed before the skill prompt directories existed.
- Scoped no-integration checks
  - No CI, validator, installer, or unrelated skill changes were found in the reviewed implementation slices.

Hosted CI status is not claimed here. Final verification has not yet run.

## Review Resolution Summary

PR review recorded two material findings. Both were accepted and resolved in `docs/changes/2026-07-04-flashcard-and-quiz-skills/review-resolution.md`.

Review-resolution summary:

- Accepted: 2
- Rejected: 0
- Deferred: 0
- Partially accepted: 0
- Needs decision: 0
- Closeout status: closed

Clean or closed review records exist for:

- Proposal review R1.
- Spec review R1.
- Plan review R1.
- Test spec review R1.
- Code review M1 R1.
- Code review M2 R1.
- Code review M3 R1.
- Metadata cleanup review R1.
- PR review resolution for `F-PR32-SKILL-001` and `F-PR32-SKILL-002`.

## Alternatives Rejected

| Alternative | Why rejected |
| --- | --- |
| One `study-artifact-generator` skill | It would blur flashcard and quiz triggers, output contracts, and quality bars. |
| Third `learning-design` skill | Shared learning theory is a reference, not a user-facing workflow in this first slice. |
| Full duplicated theory in both `SKILL.md` files | It would bloat prompts and make review harder. Compact local references preserve portability. |
| Executable JSON Schema validation now | It would add CI and failure-mode design beyond the first prompt-centered slice. |
| Direct AnkiConnect, LMS, Moodle, H5P, QTI, or external export integrations | These would add tool/API complexity and validation scope outside the approved first slice. |
| Live model CI | The accepted proof strategy uses static eval fixtures, prompt inspection, and manual smoke evidence. |

## Scope Control

The change preserves the approved non-goals:

- No `study-artifact-generator`.
- No third `learning-design` runtime skill.
- No spaced-repetition scheduler.
- No direct export integrations or external services.
- No validator, CI, installer, or runtime dependency changes.
- No live model calls in CI.
- No unrelated existing skill behavior changes.
- No high-stakes exam-prep, medical, legal, or financial guarantees.

## Risks And Follow-Ups

Remaining risks:

- Static prompt inspection cannot guarantee every future model output will satisfy the prompt contract.
- Reference schemas are documentation contracts only until a later accepted proposal/spec adds executable validation.
- Shared learning-design references are intentionally duplicated locally and may need sync tooling later if drift becomes painful.

Potential follow-ups:

- Executable JSON Schema validation after output shapes stabilize.
- Anki TSV export hardening.
- QTI/Moodle/H5P export profiles.
- AnkiConnect integration.
- Adaptive remediation or repair-loop workflows.
- High-stakes exam-prep review policy if the project later supports regulated or exam-sensitive contexts.

## Current Handoff

Implementation milestones are closed and PR review-resolution is closed. This explanation is ready for refreshed final verification.

This artifact does not claim final verification, branch readiness, PR readiness, hosted CI success, or merge readiness.
