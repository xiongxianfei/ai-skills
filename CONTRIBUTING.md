# Contributing to ai-skills

Thanks for your interest in contributing! This guide covers everything you need to add a new skill or improve an existing one.

## Adding a new skill

### 1. Create the skill directory

```bash
mkdir skills/<skill-name>
```

Use lowercase, hyphenated names (e.g. `meal-planner`, `code-reviewer`).

### 2. Write `SKILL.md`

Copy the structure below and fill it in:

```markdown
---
name: your-skill-name
description: >
  One or two sentences in English describing what the skill does and when it triggers.
  Be specific about trigger phrases so Claude knows when to auto-invoke it.
argument-hint: <what the user should pass as input>
effort: high
allowed-tools: ""
---

**Input:**
$ARGUMENTS

---

# Role / Profile

[Describe the persona or role Claude should adopt]

## Workflow

[Step-by-step instructions]

## Output Format

[Exact output structure Claude must follow]
```

### 3. Checklist before opening a PR

- [ ] `description` is in English and under 250 characters
- [ ] `argument-hint` is in English
- [ ] `effort: high` is set
- [ ] `allowed-tools: ""` is set (for pure prompt skills)
- [ ] `$ARGUMENTS` appears in the prompt body
- [ ] `## Output Format` section is present
- [ ] No emojis in the Output Format section headers
- [ ] CI passes locally: `python tests/validate_skills.py`
- [ ] Skill added to the README skills table
- [ ] Skill added to the `cp` install commands in README

### 4. Open a pull request

The PR template will pre-fill the checklist for you. Include one or two example inputs and outputs in the PR description so reviewers can quickly understand what the skill does.

---

## Improving an existing skill

- Keep changes focused — one concern per PR
- If you're changing the output format, explain why the new format is better
- CI must pass after your changes

---

## Running the validator locally

```bash
pip install pyyaml
python tests/validate_skills.py
```

Errors block merging. Warnings are non-blocking but should be reviewed.

---

## Skill writing tips

| Do | Don't |
|----|-------|
| Write `description` in English | Write `description` in Chinese or Russian |
| Use `$ARGUMENTS` to capture input | Forget `$ARGUMENTS` (input gets silently dropped) |
| Define a clear `## Output Format` | Leave output structure implicit |
| Keep `description` under 250 chars | Write multi-paragraph descriptions |
| Use `effort: high` for complex tasks | Leave `effort` unset |
| Use plain section headers | Add emojis to Output Format headers |

---

## Questions?

Open an issue using the **Skill Request** or **Bug Report** template.
