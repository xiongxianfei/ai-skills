---
description: Post-implementation learning. Updates CLAUDE.md, workflows, and specs based on what went wrong or was discovered.
argument-hint: [feature name or "general"]
model: sonnet
---

You are capturing LESSONS LEARNED after implementation.

## Your Task

Review what happened during the implementation of: $ARGUMENTS

## Process

1. Read the current state of:
   - `CLAUDE.md`
   - `docs/workflows.md`
   - `specs/$ARGUMENTS.md` (if feature-specific)
   - Recent git log: `git log --oneline -20`

2. Ask me:
   - What went wrong during implementation?
   - What did Claude get wrong repeatedly?
   - Were there any spec gaps discovered?
   - Did the system flow change from what was documented?

3. Based on answers, update the appropriate documents:

### If it's a pattern across features → Update CLAUDE.md
Add to `## Known Pitfalls` or `## Conventions`:
```markdown
## Known Pitfalls
- Claude tends to [specific mistake] — always [specific fix]
```

### If it's specific to one feature → Update that spec
Add to the spec's `## Gotchas` section:
```markdown
## Gotchas
- [Date]: Claude [what happened] — fix: [what to do instead]
```

### If the system flow changed → Update docs/workflows.md
Revise the affected workflow to match reality.

### If a new pattern was established → Update CLAUDE.md Conventions
```markdown
## Conventions
- [New convention discovered during implementation]
```

## Output

After making updates, summarize what changed:

```markdown
# Lessons Learned: [Feature/Context]

## Documents Updated
- CLAUDE.md: Added [what] to [section]
- specs/[name].md: Added gotcha about [what]
- docs/workflows.md: Updated [flow name]

## Key Takeaways
1. [Most important lesson]
2. [Second lesson]
```

## Rules
- Do NOT delete existing content — only ADD to it.
- Keep additions concise — one line per pitfall/convention.
- Date-stamp gotchas in specs so you can see when they were discovered.
- If nothing went wrong, it's fine to say so. Don't fabricate lessons.
