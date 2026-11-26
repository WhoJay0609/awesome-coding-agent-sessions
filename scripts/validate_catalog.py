#!/usr/bin/env python3
"""Validate the curated catalog without network access."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "catalog.json"
REPOSITORY_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TOP_LEVEL_FIELDS = {"schema_version", "metadata_checked", "categories", "projects"}
REQUIRED_PROJECT_FIELDS = {
    "name",
    "repository",
    "category",
    "summary",
    "agents",
    "interfaces",
    "capabilities",
    "best_for",
    "license",
    "stars_snapshot",
    "verified_at",
    "source",
}
PROMOTIONAL_WORDS = {"best", "leading", "ultimate", "revolutionary", "unmatched"}


class CatalogError(ValueError):
    """Raised when catalog data violates a curation invariant."""


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _nonempty_string_list(value: Any) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(_nonempty_string(item) for item in value)
        and len(value) == len(set(value))
    )


def _parse_date(value: Any, label: str, errors: list[str]) -> date | None:
    if not _nonempty_string(value) or not DATE_RE.fullmatch(value):
        errors.append(f"{label} must use YYYY-MM-DD: {value!r}")
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        errors.append(f"{label} must use YYYY-MM-DD: {value!r}")
        return None


def load_and_validate(path: Path = CATALOG_PATH) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CatalogError(f"cannot read {path}: {exc}") from exc

    if not isinstance(data, dict):
        raise CatalogError("catalog root must be a JSON object")

    errors: list[str] = []
    missing_top_level = TOP_LEVEL_FIELDS - set(data)
    extra_top_level = set(data) - TOP_LEVEL_FIELDS
    if missing_top_level:
        errors.append(f"catalog missing fields: {', '.join(sorted(missing_top_level))}")
    if extra_top_level:
        errors.append(f"catalog has unknown fields: {', '.join(sorted(extra_top_level))}")
    schema_version = data.get("schema_version")
    if isinstance(schema_version, bool) or not isinstance(schema_version, int) or schema_version != 1:
        errors.append("schema_version must equal 1")

    checked_date = _parse_date(data.get("metadata_checked"), "metadata_checked", errors)
    categories = data.get("categories")
    projects = data.get("projects")
    if not isinstance(categories, list) or len(categories) < 5:
        errors.append("catalog must define at least 5 categories")
        categories = []
    if not isinstance(projects, list) or len(projects) < 10:
        errors.append("catalog must contain at least 10 projects")
        projects = []

    category_ids: list[str] = []
    for index, category in enumerate(categories):
        label = f"categories[{index}]"
        if not isinstance(category, dict):
            errors.append(f"{label} must be an object")
            continue
        if set(category) != {"id", "title", "description"}:
            errors.append(f"{label} must contain exactly id, title, and description")
        for field in ("id", "title", "description"):
            if not _nonempty_string(category.get(field)):
                errors.append(f"{label}.{field} must be a non-empty string")
        if _nonempty_string(category.get("id")):
            category_ids.append(category["id"])

    for category_id, count in Counter(category_ids).items():
        if count > 1:
            errors.append(f"duplicate category id: {category_id}")

    names: list[str] = []
    repositories: list[str] = []
    project_counts: Counter[str] = Counter()
    for index, project in enumerate(projects):
        label = f"projects[{index}]"
        if not isinstance(project, dict):
            errors.append(f"{label} must be an object")
            continue
        missing = REQUIRED_PROJECT_FIELDS - set(project)
        extra = set(project) - REQUIRED_PROJECT_FIELDS
        if missing:
            errors.append(f"{label} missing fields: {', '.join(sorted(missing))}")
        if extra:
            errors.append(f"{label} has unknown fields: {', '.join(sorted(extra))}")

        for field in ("name", "repository", "category", "summary", "best_for", "license", "source"):
            if not _nonempty_string(project.get(field)):
                errors.append(f"{label}.{field} must be a non-empty string")
        for field in ("agents", "interfaces", "capabilities"):
            if not _nonempty_string_list(project.get(field)):
                errors.append(f"{label}.{field} must be a non-empty list of unique strings")

        name = project.get("name")
        repository = project.get("repository")
        category_id = project.get("category")
        if _nonempty_string(name):
            names.append(name.casefold())
        if _nonempty_string(repository):
            repositories.append(repository.casefold())
            if not REPOSITORY_RE.fullmatch(repository):
                errors.append(f"{label}.repository is not owner/name: {repository!r}")
            expected_source = f"https://github.com/{repository}"
            if project.get("source") != expected_source:
                errors.append(f"{label}.source must equal {expected_source}")
        if category_id not in category_ids:
            errors.append(f"{label}.category references an unknown category: {category_id!r}")
        else:
            project_counts[category_id] += 1

        for field in ("summary", "best_for"):
            value = project.get(field)
            if _nonempty_string(value) and not value.endswith("."):
                errors.append(f"{label}.{field} must end with a period")
        summary_words = set(re.findall(r"[a-z]+", str(project.get("summary", "")).lower()))
        if summary_words & PROMOTIONAL_WORDS:
            errors.append(f"{label}.summary contains promotional wording")

        stars = project.get("stars_snapshot")
        if isinstance(stars, bool) or not isinstance(stars, int) or stars < 0:
            errors.append(f"{label}.stars_snapshot must be a non-negative integer")
        verified_date = _parse_date(project.get("verified_at"), f"{label}.verified_at", errors)
        if checked_date and verified_date and verified_date > checked_date:
            errors.append(f"{label}.verified_at cannot be after metadata_checked")

    for value, count in Counter(names).items():
        if count > 1:
            errors.append(f"duplicate project name: {value}")
    for value, count in Counter(repositories).items():
        if count > 1:
            errors.append(f"duplicate repository: {value}")
    for category_id in category_ids:
        if project_counts[category_id] == 0:
            errors.append(f"category has no projects: {category_id}")
        category_names = [
            project["name"]
            for project in projects
            if isinstance(project, dict) and project.get("category") == category_id and _nonempty_string(project.get("name"))
        ]
        if category_names != sorted(category_names, key=str.casefold):
            errors.append(f"projects in {category_id} must be sorted alphabetically")

    if errors:
        raise CatalogError("catalog validation failed:\n- " + "\n- ".join(errors))
    return data


def main() -> int:
    try:
        data = load_and_validate()
    except CatalogError as exc:
        print(exc, file=sys.stderr)
        return 1
    print(
        f"Catalog valid: {len(data['projects'])} projects across "
        f"{len(data['categories'])} categories."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
