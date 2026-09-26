#!/usr/bin/env python3
"""Check skill packaging invariants without external dependencies.

- SKILL.md starts with YAML frontmatter carrying non-empty `name` and `description`.
- Every `references/*.md` path mentioned in SKILL.md exists.
- Every file under references/ is mentioned in SKILL.md (no orphaned guidance).
- Every relative Markdown link in checked-in Markdown files resolves.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFERENCE_PATH = re.compile(r"references/[A-Za-z0-9_.-]+\.md")
MARKDOWN_LINK = re.compile(r"\]\(([^)\s]+)\)")


def frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        key, sep, value = line.partition(":")
        if sep and not line.startswith((" ", "\t")):
            fields[key.strip()] = value.strip()
    return {}


def main() -> int:
    errors: list[str] = []
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")

    fields = frontmatter(skill)
    for key in ("name", "description"):
        if not fields.get(key):
            errors.append(f"SKILL.md frontmatter missing non-empty `{key}`")

    mentioned = set(REFERENCE_PATH.findall(skill))
    for path in sorted(mentioned):
        if not (ROOT / path).is_file():
            errors.append(f"SKILL.md mentions missing file {path}")
    for path in sorted((ROOT / "references").glob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        if rel not in mentioned:
            errors.append(f"{rel} is not referenced from SKILL.md")

    markdown_files = sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)
    for md in markdown_files:
        for target in MARKDOWN_LINK.findall(md.read_text(encoding="utf-8")):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
                continue
            resolved = (md.parent / target.split("#", 1)[0]).resolve()
            if not resolved.exists():
                errors.append(f"{md.relative_to(ROOT)}: broken relative link {target}")

    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    if errors:
        return 1
    print(
        f"checked SKILL.md ({len(mentioned)} references) and "
        f"{len(markdown_files)} Markdown files for relative links"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
