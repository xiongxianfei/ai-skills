"""
Validate all skills in the skills/ directory against best-practice rules.

Rules checked per SKILL.md:
  [REQUIRED]  Frontmatter is valid YAML
  [REQUIRED]  name field present
  [REQUIRED]  description field present
  [REQUIRED]  argument-hint field present
  [REQUIRED]  $ARGUMENTS appears in the prompt body
  [REQUIRED]  ## Output Format section present in the prompt body
  [BEST PRACTICE]  effort field present
  [BEST PRACTICE]  allowed-tools field present

Rules checked for plugin.json:
  [REQUIRED]  Valid JSON
  [REQUIRED]  name, description, version, license fields present
"""

import json
import sys
from pathlib import Path

import yaml

SKILLS_DIR = Path(__file__).parent.parent / "skills"
PLUGIN_JSON = Path(__file__).parent.parent / ".claude-plugin" / "plugin.json"

REQUIRED_FRONTMATTER = ["name", "description", "argument-hint"]
BEST_PRACTICE_FRONTMATTER = ["effort", "allowed-tools"]
REQUIRED_PLUGIN_FIELDS = ["name", "description", "version", "license"]

errors = []
warnings = []


def error(path: str, msg: str):
    errors.append(f"  ERROR  {path}: {msg}")


def warn(path: str, msg: str):
    warnings.append(f"  WARN   {path}: {msg}")


def parse_skill(path: Path) -> tuple[dict, str]:
    """Split SKILL.md into frontmatter dict and body string."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm = yaml.safe_load(parts[1]) or {}
    body = parts[2]
    return fm, body


def validate_skill(skill_dir: Path):
    skill_file = skill_dir / "SKILL.md"
    label = f"skills/{skill_dir.name}/SKILL.md"

    if not skill_file.exists():
        error(label, "SKILL.md not found")
        return

    try:
        fm, body = parse_skill(skill_file)
    except yaml.YAMLError as e:
        error(label, f"invalid YAML frontmatter: {e}")
        return

    for field in REQUIRED_FRONTMATTER:
        if field not in fm:
            error(label, f"missing required frontmatter field: '{field}'")

    for field in BEST_PRACTICE_FRONTMATTER:
        if field not in fm:
            warn(label, f"missing best-practice frontmatter field: '{field}'")

    if "$ARGUMENTS" not in body:
        error(label, "$ARGUMENTS not found in prompt body — slash command input will be dropped")

    if "## Output Format" not in body:
        error(label, "## Output Format section missing — output structure is undefined")


def validate_plugin_json():
    label = ".claude-plugin/plugin.json"
    if not PLUGIN_JSON.exists():
        warn(label, "plugin.json not found — required for Claude Code plugin distribution")
        return

    try:
        data = json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        error(label, f"invalid JSON: {e}")
        return

    for field in REQUIRED_PLUGIN_FIELDS:
        if field not in data:
            error(label, f"missing required field: '{field}'")


def main():
    skill_dirs = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir())

    if not skill_dirs:
        print("No skills found — add skill directories under skills/")
        sys.exit(1)

    print(f"Validating {len(skill_dirs)} skill(s)...\n")
    for skill_dir in skill_dirs:
        validate_skill(skill_dir)

    validate_plugin_json()

    if warnings:
        print("Warnings:")
        for w in warnings:
            print(w)
        print()

    if errors:
        print("Errors:")
        for e in errors:
            print(e)
        print(f"\n{len(errors)} error(s) found. Fix them before merging.")
        sys.exit(1)

    print(f"All {len(skill_dirs)} skill(s) passed validation.")
    if warnings:
        print(f"{len(warnings)} warning(s) — review recommended but not blocking.")


if __name__ == "__main__":
    main()
