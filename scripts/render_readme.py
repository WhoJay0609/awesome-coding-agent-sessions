#!/usr/bin/env python3
"""Render the catalog section in README.md from catalog.json."""

from __future__ import annotations

import argparse
import difflib
from pathlib import Path

from validate_catalog import CatalogError, load_and_validate

ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
BEGIN_MARKER = "<!-- catalog:start -->"
END_MARKER = "<!-- catalog:end -->"


class ReadmeError(ValueError):
    """Raised when README generation markers are malformed."""


def _escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def _join(values: list[str]) -> str:
    return "<br>".join(_escape(value) for value in values)


def _stars_badge(repository: str) -> str:
    badge = f"https://img.shields.io/github/stars/{repository}?style=flat&label=stars"
    return f"[![GitHub stars]({badge})](https://github.com/{repository}/stargazers)"


def _stars_metric(project: dict) -> str:
    return (
        f"{_stars_badge(project['repository'])}<br>"
        f"<sub>{project['stars_snapshot']:,} on {project['verified_at']}</sub>"
    )


def render_catalog(data: dict) -> str:
    projects = data["projects"]
    categories = data["categories"]
    lines = [
        "## Comparison matrix",
        "",
        f"**Catalog:** {len(projects)} projects across {len(categories)} categories. "
        f"Repository metadata was last checked on **{data['metadata_checked']}**.",
        "",
        "> Stars are live badges loaded from GitHub via Shields.io. They show adoption, not quality, "
        "and are never an inclusion threshold. Supported-agent and scope claims come from each project's documentation.",
        "",
        "| Project | Category | Stars | Supported agents | Interface | Best for | License |",
        "|---|---|---:|---|---|---|---|",
    ]
    category_titles = {category["id"]: category["title"] for category in categories}
    for project in sorted(projects, key=lambda item: item["name"].casefold()):
        lines.append(
            "| "
            f"[{_escape(project['name'])}]({project['source']}) | "
            f"{_escape(category_titles[project['category']])} | "
            f"{_stars_metric(project)} | "
            f"{_join(project['agents'])} | "
            f"{_join(project['interfaces'])} | "
            f"{_escape(project['best_for'])} | "
            f"`{_escape(project['license'])}` |"
        )

    lines.extend(["", "## Projects", ""])
    for category in categories:
        lines.extend([f"### {category['title']}", "", category["description"], ""])
        category_projects = [project for project in projects if project["category"] == category["id"]]
        for project in category_projects:
            metrics = (
                f"**Agents:** {', '.join(project['agents'])}. "
                f"**Interface:** {', '.join(project['interfaces'])}. "
                f"**Best for:** {project['best_for']} "
                f"**License:** `{project['license']}`."
            )
            lines.append(
                f"- [{project['name']}]({project['source']}) — {project['summary']} "
                f"{metrics} {_stars_badge(project['repository'])}"
            )
        lines.append("")
    return "\n".join(lines).rstrip()


def update_readme(current: str, generated: str) -> str:
    if current.count(BEGIN_MARKER) != 1 or current.count(END_MARKER) != 1:
        raise ReadmeError("README.md must contain exactly one catalog marker pair")
    if current.index(BEGIN_MARKER) > current.index(END_MARKER):
        raise ReadmeError("README.md catalog start marker must appear before the end marker")
    prefix, rest = current.split(BEGIN_MARKER, 1)
    _, suffix = rest.split(END_MARKER, 1)
    return f"{prefix}{BEGIN_MARKER}\n\n{generated}\n\n{END_MARKER}{suffix}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if README.md is stale")
    args = parser.parse_args()
    try:
        data = load_and_validate()
    except CatalogError as exc:
        parser.error(str(exc))
    try:
        current = README_PATH.read_text(encoding="utf-8")
        expected = update_readme(current, render_catalog(data))
    except (OSError, ReadmeError) as exc:
        parser.error(str(exc))
    if args.check:
        if current == expected:
            print("README catalog is up to date.")
            return 0
        print(
            "".join(
                difflib.unified_diff(
                    current.splitlines(keepends=True),
                    expected.splitlines(keepends=True),
                    fromfile="README.md",
                    tofile="README.md (rendered)",
                )
            )
        )
        return 1
    README_PATH.write_text(expected, encoding="utf-8")
    print(f"Rendered {len(data['projects'])} projects into README.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
