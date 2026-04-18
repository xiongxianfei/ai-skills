# Execution plan template

Use this template for every concrete plan file under `docs/plans/`. Plans are living documents: keep `Progress`, `Surprises & Discoveries`, `Decision Log`, `Validation Notes`, and `Outcomes & Retrospective` up to date as work proceeds.

A good plan is self-contained enough that a new contributor can continue the work without prior chat context.

## Required sections

### Title
Use a short, action-oriented title.

### Metadata
- Status: proposed | active | blocked | completed | superseded
- Created:
- Updated:
- Owner:
- Related spec(s):
- Supersedes / Superseded by:
- Branch / PR:
- Last verified commands:

### Purpose / Big picture
Explain what changes for the user and how someone can tell the work succeeded.

### Context and orientation
Describe the current repo state relevant to this task as if the reader knows nothing. Name the key files, modules, workflows, and constraints by path.

### Constraints
State the hard limits: performance, platform, compatibility, privacy, release policy, rollout safety, and explicit non-goals.

### Done when
State the observable finish line, not just “code compiles”.

### Milestones
Describe milestone-by-milestone work in prose. Each milestone should be independently reviewable and verifiable. For each milestone, include:
- scope
- files or components touched
- dependencies
- risk
- validation commands
- expected observable result

### Progress
Use checkboxes with timestamps. This section must always reflect the real current state.
- [x] Example completed step.
- [ ] Example remaining step.
- [ ] Example partially complete step (done: …; remaining: …).

### Surprises & Discoveries
Record unexpected behaviors, bugs, tradeoffs, or insights with brief evidence.

### Decision Log
For each important decision:
- Decision:
- Rationale:
- Date/Author:

### Validation and Acceptance
Record the concrete commands to run, where to run them, and what success looks like.

### Validation Notes
Keep short notes or outputs proving milestone validation.

### Idempotence and Recovery
Describe safe re-runs, rollback paths, cleanup steps, and how to recover from failure.

### Outcomes & Retrospective
Summarize what shipped, what remains, and what future contributors should remember.

## Working rules

- New initiatives create a new file under `docs/plans/YYYY-MM-DD-slug.md`.
- Do not overwrite an older plan file to start a new initiative.
- If validation fails after a milestone, stop and fix the failure before continuing.
- Keep the plan specific: name files, commands, and acceptance behavior.
- Prefer additive changes and small milestones over large speculative rewrites.
