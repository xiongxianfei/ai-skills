---
description: Create a GitHub release with semantic versioning, changelog generation, and spec compliance verification. Run after features are merged and ready to ship.
argument-hint: [optional: major | minor | patch | or specific version like v1.2.0]
---

You are creating a **GitHub release**. This is the final step that packages completed work into a versioned, documented release.

## Your Task

Create a release. Version hint: **$ARGUMENTS**

## Process

### Step 1: Determine Version

1. **Find the latest release.** Run:
   ```bash
   git tag --sort=-v:refname | head -5
   ```
   If no tags exist, this is the first release — start at `v0.1.0`.

2. **Determine version bump.** If `$ARGUMENTS` specifies a version or bump type, use it. Otherwise, analyze commits since the last tag to determine the bump:
   ```bash
   git log $(git describe --tags --abbrev=0 2>/dev/null || echo "")..HEAD --oneline
   ```

   Follow **Semantic Versioning** (MAJOR.MINOR.PATCH):
   - **PATCH** (v1.0.0 → v1.0.1): Bug fixes, minor corrections, no new features
   - **MINOR** (v1.0.0 → v1.1.0): New features, backward compatible
   - **MAJOR** (v1.0.0 → v2.0.0): Breaking changes, incompatible API changes

   Use commit messages as signals:
   - `fix:` / `bugfix:` → patch
   - `feat:` / `feature:` → minor
   - `BREAKING CHANGE` in body or `!` after type → major

3. **Confirm with the user.** State the proposed version and why. Wait for approval before proceeding.

### Step 2: Verify Release Readiness

Before creating the release, verify:

1. **All tests pass.**
   ```bash
   # Run the project's test suite (read CLAUDE.md for the test command)
   ```

2. **No uncommitted changes.**
   ```bash
   git status --porcelain
   ```

3. **Spec compliance.** Check that all specs in `specs/` that were part of this release have their acceptance criteria met:
   - Read each spec's acceptance criteria
   - Verify tests exist for each spec
   - Confirm no open issues referencing these specs

4. **Report any issues to the user.** Do NOT proceed if tests fail or there are uncommitted changes.

### Step 3: Generate Changelog

Analyze commits since the last release and categorize them:

```bash
git log $(git describe --tags --abbrev=0 2>/dev/null || echo "")..HEAD --pretty=format:"%h %s" --no-merges
```

Organize into categories:

```markdown
## What's Changed

### Features
- Description of feature (PR #N, spec: specs/f1-feature.md)

### Bug Fixes
- Description of fix (PR #N)

### Improvements
- Description of improvement (PR #N)

### Breaking Changes
- Description of what broke and migration steps

### Documentation
- Description of doc changes

### Internal
- Refactoring, CI changes, dependency updates
```

Rules for the changelog:
- Write from the **user's perspective**, not the developer's. "Added session export to CSV" not "Implemented CsvExporter class."
- Link PRs where possible.
- Link specs for features — this connects the release to the planning artifacts.
- Breaking changes get their own section with **migration instructions**.
- Skip trivial commits (typo fixes, merge commits) unless they're the only changes.

### Step 4: Update CHANGELOG.md

Prepend the new release to `CHANGELOG.md` in the project root. If the file doesn't exist, create it.

```markdown
# Changelog

## [v1.2.0] - 2026-04-13

### Features
- ...

### Bug Fixes
- ...

(Full changelog: compare link)

---

## [v1.1.0] - 2026-03-28
...
```

Commit the changelog update:
```bash
git add CHANGELOG.md
git commit -m "docs: update changelog for v1.2.0"
```

### Step 5: Create the Tag and Release

```bash
# Create annotated tag
git tag -a v[VERSION] -m "Release v[VERSION]"

# Push tag
git push origin v[VERSION]

# Create GitHub release using gh CLI
gh release create v[VERSION] \
  --title "v[VERSION]" \
  --notes-file - <<'EOF'
[paste the changelog content for this version]
EOF
```

If `gh` CLI is not available, output the release notes and instruct the user to create the release manually on GitHub.

### Step 6: Post-Release

After the release is created:

1. **Verify the release.** Check that the GitHub release page looks correct:
   ```bash
   gh release view v[VERSION]
   ```

2. **Update docs if needed.** If this release changes system behavior, remind the user to update:
   - `docs/workflows.md` — if flows changed
   - `CLAUDE.md` — if conventions or patterns changed
   - `README.md` — if user-facing features changed

3. **Report the summary:**
   ```
   Release created: v[VERSION]
   Tag: v[VERSION]
   Commits included: [count]
   Features: [count]
   Bug fixes: [count]
   Breaking changes: [yes/no]
   ```

## Rules

- ALWAYS confirm the version number with the user before creating the tag.
- NEVER create a release if tests fail or there are uncommitted changes.
- NEVER skip the changelog. Every release must be documented.
- Write changelog entries from the user's perspective, not the developer's.
- Breaking changes MUST include migration instructions.
- If this is the first release (no prior tags), start at v0.1.0 unless the user specifies otherwise.
- Link specs in changelog entries to maintain traceability from release → feature → spec → plan.
- If `gh` CLI is unavailable, output everything the user needs to create the release manually.