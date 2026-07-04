# Post-Change Evidence: Flashcard And Quiz Generator Skills

## Scope

This evidence covers M3: prompt inspection, manual smoke proof where feasible, no-integration boundary checks, and final local validation before code-review.

No live model calls were run. The approved test spec allows manual smoke or prompt-inspection proof for M3, and the first slice explicitly avoids live model CI and external services.

## Reviewed Artifacts

- `skills/flashcard-generator/SKILL.md`
- `skills/quiz-generator/SKILL.md`
- `skills/flashcard-generator/references/learning-design.md`
- `skills/quiz-generator/references/learning-design.md`
- `skills/flashcard-generator/references/card-quality.md`
- `skills/quiz-generator/references/question-quality.md`
- `skills/flashcard-generator/schemas/flashcard.schema.json`
- `skills/quiz-generator/schemas/quiz-item.schema.json`
- `tests/evals/skills/flashcard-generator/cases.yaml`
- `tests/evals/skills/quiz-generator/cases.yaml`
- `README.md`

## Prompt Inspection

| Requirement area | Evidence | Result |
| --- | --- | --- |
| Flashcard setup before generation | `flashcard-generator` identifies learner goal, audience, source, count, difficulty, and export format, then extracts objectives and builds a knowledge map before card generation (`SKILL.md` lines 25-36). | Pass |
| Flashcard quality gate | `flashcard-generator` validates cards before returning final output and requires failed cards to be rewritten or dropped (`SKILL.md` lines 44-45). | Pass |
| Flashcard output contract | Output includes deck summary, learning objectives, knowledge map, card table, canonical JSON, requested export, and quality check (`SKILL.md` lines 80-136). | Pass |
| Quiz setup before generation | `quiz-generator` identifies purpose, audience, source, difficulty, count, types, and export format, then extracts objectives, builds a knowledge map, and creates a blueprint before question generation (`SKILL.md` lines 25-40). | Pass |
| Quiz quality gate | `quiz-generator` validates each item and rewrites or drops failed items before returning final output (`SKILL.md` lines 41-42). | Pass |
| Quiz output contract | Output includes quiz blueprint, learning objectives, knowledge map, questions, canonical JSON, requested export, and quality check (`SKILL.md` lines 85-158). | Pass |
| Reference schemas remain documentation-only | Both prompts call schemas reference contracts and say the schema is documentation only; both schema descriptions say they are not enforced by CI in the first slice. | Pass |
| No broad combined skill | The implementation adds only `flashcard-generator` and `quiz-generator`; no `study-artifact-generator` directory or third `learning-design` skill was added. | Pass |

## Manual Smoke Proof

### MP1: Flashcard Anki-Style Generation

Smoke prompt:

```text
Turn this onboarding note into Anki-ready flashcards:

Idempotency prevents duplicate side effects when clients retry requests after
timeouts. Payment APIs commonly require an idempotency key so the server can
recognize a retry and return the original result instead of charging again.
```

Inspection result:

- The prompt requires objectives and knowledge map before cards (`flashcard-generator/SKILL.md` lines 25-36).
- It supports basic, cloze, bidirectional, contrast, example/non-example, procedure, and failure-mode card types (`SKILL.md` lines 36-43).
- It rejects broad, duplicate, trivia, or unsupported cards and requires atomicity and usefulness (`SKILL.md` lines 57-68).
- The output contract includes a card table and canonical JSON (`SKILL.md` lines 100-130).

Result: Pass. The prompt is structured to produce the expected Anki-style output without collapsing into a summary.

### MP2: Diagnostic Quiz And MCQ Quality

Smoke prompt:

```text
Create an 8-question diagnostic quiz from this onboarding note:

Idempotency prevents duplicate side effects when clients retry requests after
timeouts. Payment APIs commonly require an idempotency key so the server can
recognize a retry and return the original result instead of charging again.
```

Inspection result:

- The prompt requires a quiz blueprint before item generation (`quiz-generator/SKILL.md` lines 35-40).
- It supports recall, comprehension, contrast, application, prediction, diagnosis, transfer, and tradeoff judgment when the source supports those levels (`SKILL.md` lines 11-13 and 60).
- It requires objective alignment, source-grounded answer keys, ambiguity control, and useful feedback (`SKILL.md` lines 54-62).
- MCQs require clear stems, one best answer unless multiple-select is requested, plausible but wrong distractors, no grammatical clues, no default all/none-of-the-above, and option explanations (`SKILL.md` lines 64-71).
- The output contract includes blueprint, questions, rationales, feedback, and canonical JSON (`SKILL.md` lines 85-158).

Result: Pass. The prompt is structured to produce diagnostic questions with answer keys and feedback rather than a flat recall list.

### MP3: Unsupported Material Boundary

Smoke prompt:

```text
Create advanced flashcards and quiz questions from this note:

OAuth is used for authorization.
```

Inspection result:

- Flashcard prompt requires external or inferred context to be marked and forbids presenting inferred facts as source-grounded (`flashcard-generator/SKILL.md` lines 15 and 70-78).
- Flashcard prompt requires fewer cards when the source cannot support the requested count or difficulty (`SKILL.md` line 67).
- Quiz prompt requires inferred context marking, forbids unsupported advanced questions from thin source material, and requires only supportable questions when source material is too thin (`quiz-generator/SKILL.md` lines 15, 61, and 75-83).

Result: Pass. Both prompts preserve the source-grounding boundary for thin or under-specified source material.

### MP4: Both-Output Fallback

Smoke prompt:

```text
Create flashcards and a quiz from this codebase overview.
```

Inspection result:

- Flashcard prompt requires shared learning objectives and a compact knowledge map to be extracted once, then keeps the flashcard output separate from quiz output with a separate canonical JSON payload (`flashcard-generator/SKILL.md` line 68).
- Quiz prompt requires shared learning objectives and a compact knowledge map to be extracted once, then keeps the quiz output separate from flashcard output with a separate canonical JSON payload (`quiz-generator/SKILL.md` line 73).
- Both workflows require objective extraction and knowledge mapping before artifact generation (`flashcard-generator/SKILL.md` lines 25-36; `quiz-generator/SKILL.md` lines 25-40), which supports the spec's shared-objectives fallback without creating a third broad skill.

Result: Pass. Combined requests preserve separate contracts and JSON payloads.

## Boundary Checks

| Boundary | Evidence | Result |
| --- | --- | --- |
| No executable schema validation | No validator or CI changes were added in M2 or M3. The schemas are present as reference JSON Schema files only. | Pass |
| No external integration | No AnkiConnect, LMS, Moodle, H5P, QTI, external-service, runtime-dependency, installer, or CI behavior was added. | Pass |
| High-stakes guarantees | Flashcard prompt forbids medical, legal, financial, and high-stakes exam-prep guarantees (`flashcard-generator/SKILL.md` line 78). Quiz prompt does the same (`quiz-generator/SKILL.md` line 62). | Pass |
| Privacy | Fixtures use short fictional/sanitized notes about idempotency, retries, authentication/authorization, and OAuth; no secrets, private paths, or personal data are required by the prompts. | Pass |
| Prompt size | `flashcard-generator/SKILL.md` is 136 lines and `quiz-generator/SKILL.md` is 158 lines, below the approved line limit. | Pass |

## Validation Commands

Recorded after this evidence file was created:

- `python tests/validate_skills.py`
- `python -m unittest discover tests`
- `python tests/check_readme_sync.py`
- `git diff --check`
- `wc -l skills/flashcard-generator/SKILL.md skills/quiz-generator/SKILL.md`
- `python - <<'PY' ... yaml ok`

See `docs/changes/2026-07-04-flashcard-and-quiz-skills/change.yaml` and the active plan validation notes for command results.

## Residual Risks

- Static prompt inspection cannot prove every future model output will satisfy the contract. The first slice intentionally uses prompt contracts and eval fixtures rather than live model CI.
- Reference schemas are not executable validators in this slice. A later proposal/spec is required before CI schema enforcement.
