# Baseline Evidence: Flashcard And Quiz Skills M1

## Scope

M1 adds reviewer-visible eval fixtures before prompt implementation:

- `tests/evals/skills/flashcard-generator/cases.yaml`
- `tests/evals/skills/quiz-generator/cases.yaml`

No skill prompt, README, schema, reference, validator, installer, or CI change is part of M1.

## Baseline State

Before M1 prompt implementation, the new skill directories are intentionally absent:

```text
skills/flashcard-generator/SKILL.md absent
skills/quiz-generator/SKILL.md absent
```

Because the skill directories do not exist yet, full `python tests/validate_skills.py` does not enforce these new fixture directories in M1. Direct fixture validation is the required proof for this milestone.

## Proof Map

| Test ID | Evidence |
| --- | --- |
| T1 | `tests/evals/skills/flashcard-generator/cases.yaml` includes normal Anki, indirect memory prompt, cloze/contrast, source-grounding boundary, non-trigger summary, and both-output cases. |
| T2 | `tests/evals/skills/quiz-generator/cases.yaml` includes normal diagnostic quiz, indirect comprehension check, MCQ distractor quality, unsupported-material boundary, non-trigger rewrite, and both-output cases. |
| T3 | Flashcard source-grounding boundary case requires inference marking or avoidance and no unsupported details. |
| T4 | Quiz unsupported-material boundary case requires no unsupported advanced facts as source-grounded and no ambiguous questions. |
| T5 | Non-trigger cases cover generic summary and rewrite requests. |
| T6 | Both-output cases require separate flashcard and quiz contracts and separate canonical JSON payloads. |

## Same-Slice Completeness

M1 in-scope surfaces:

- Eval fixture for `flashcard-generator`: updated.
- Eval fixture for `quiz-generator`: updated.
- Baseline evidence: updated.
- Active plan and change metadata: updated after validation.

M1 unaffected surfaces:

- `skills/flashcard-generator/`: unaffected with rationale; M2 owns prompt, reference, and schema creation.
- `skills/quiz-generator/`: unaffected with rationale; M2 owns prompt, reference, and schema creation.
- `README.md`: unaffected with rationale; README sync is meaningful after M2 creates skill directories.
- `CONTRIBUTING.md`: unaffected with rationale; contributor guidance changes are only needed if M2 reveals a documentation gap.
- `tests/validate_skills.py`: unaffected with rationale; M1 uses the existing accepted eval fixture validator and does not add executable schema or trigger-case validation.

## Validation Evidence

| Command | Result | Notes |
| --- | --- | --- |
| `python -c 'from pathlib import Path; from tests.validate_skills import validate_cases_file; [(_ := validate_cases_file(name, Path(f"tests/evals/skills/{name}/cases.yaml")), (_).errors and (_ for _ in ()).throw(AssertionError(_.errors))) for name in ("flashcard-generator", "quiz-generator")]; print("direct eval fixture validation passed")'` | passed | Both new eval fixtures validate directly before skill directories exist. |
| `python -m unittest discover tests` | passed | Ran 31 tests. |
| `git diff --check` | passed | No whitespace errors. |
| `test ! -e skills/flashcard-generator/SKILL.md && test ! -e skills/quiz-generator/SKILL.md && echo 'skill prompts absent as expected for M1'` | passed | Confirms prompt implementation remains deferred to M2. |
