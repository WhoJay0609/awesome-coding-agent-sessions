from __future__ import annotations

import copy
import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import render_readme
from render_readme import BEGIN_MARKER, END_MARKER, render_catalog, update_readme
from validate_catalog import CATALOG_PATH, CatalogError, load_and_validate


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog = load_and_validate()

    def test_catalog_meets_public_contract(self) -> None:
        self.assertGreaterEqual(len(self.catalog["projects"]), 10)
        self.assertGreaterEqual(len(self.catalog["categories"]), 5)
        for project in self.catalog["projects"]:
            self.assertTrue(project["agents"])
            self.assertTrue(project["interfaces"])
            self.assertTrue(project["best_for"])
            self.assertTrue(project["license"])

    def test_render_exposes_live_stars_for_every_project(self) -> None:
        rendered = render_catalog(self.catalog)
        for project in self.catalog["projects"]:
            badge = f"img.shields.io/github/stars/{project['repository']}"
            self.assertIn(badge, rendered)
            self.assertIn(
                f"{project['stars_snapshot']:,} on {project['verified_at']}",
                rendered,
            )
            self.assertIn(project["best_for"], rendered)
            self.assertIn(project["license"], rendered)

    def test_render_uses_each_projects_verification_date(self) -> None:
        mixed_dates = copy.deepcopy(self.catalog)
        mixed_dates["projects"][0]["verified_at"] = "2026-08-01"
        rendered = render_catalog(mixed_dates)
        project = mixed_dates["projects"][0]
        self.assertIn(
            f"{project['stars_snapshot']:,} on 2026-08-01",
            rendered,
        )

    def test_duplicate_repository_is_rejected(self) -> None:
        invalid = copy.deepcopy(self.catalog)
        invalid["projects"][1]["repository"] = invalid["projects"][0]["repository"]
        invalid["projects"][1]["source"] = invalid["projects"][0]["source"]
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "catalog.json"
            path.write_text(json.dumps(invalid), encoding="utf-8")
            with self.assertRaisesRegex(CatalogError, "duplicate repository"):
                load_and_validate(path)

    def test_non_object_catalog_root_is_rejected_cleanly(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "catalog.json"
            path.write_text("[]", encoding="utf-8")
            with self.assertRaisesRegex(CatalogError, "root must be a JSON object"):
                load_and_validate(path)

    def test_boolean_schema_version_is_rejected(self) -> None:
        invalid = copy.deepcopy(self.catalog)
        invalid["schema_version"] = True
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "catalog.json"
            path.write_text(json.dumps(invalid), encoding="utf-8")
            with self.assertRaisesRegex(CatalogError, "schema_version must equal 1"):
                load_and_validate(path)

    def test_dates_require_calendar_valid_yyyy_mm_dd(self) -> None:
        for invalid_date in ("20260811", "2026-W33-2", "2026-02-30"):
            with self.subTest(invalid_date=invalid_date):
                invalid = copy.deepcopy(self.catalog)
                invalid["metadata_checked"] = invalid_date
                with tempfile.TemporaryDirectory() as temp_dir:
                    path = Path(temp_dir) / "catalog.json"
                    path.write_text(json.dumps(invalid), encoding="utf-8")
                    with self.assertRaisesRegex(CatalogError, "must use YYYY-MM-DD"):
                        load_and_validate(path)

    def test_unknown_top_level_field_is_rejected(self) -> None:
        invalid = copy.deepcopy(self.catalog)
        invalid["unexpected"] = "value"
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "catalog.json"
            path.write_text(json.dumps(invalid), encoding="utf-8")
            with self.assertRaisesRegex(CatalogError, "unknown fields: unexpected"):
                load_and_validate(path)

    def test_readme_replacement_preserves_surrounding_content(self) -> None:
        current = f"before\n{BEGIN_MARKER}\nstale\n{END_MARKER}\nafter\n"
        updated = update_readme(current, "fresh")
        self.assertEqual(
            updated,
            f"before\n{BEGIN_MARKER}\n\nfresh\n\n{END_MARKER}\nafter\n",
        )

    def test_malformed_readme_markers_fail_without_traceback(self) -> None:
        malformed_readmes = {
            "missing": "no markers here\n",
            "duplicate": f"{BEGIN_MARKER}\n{BEGIN_MARKER}\n{END_MARKER}\n",
            "reversed": f"{END_MARKER}\n{BEGIN_MARKER}\n",
        }
        for case, content in malformed_readmes.items():
            with self.subTest(case=case), tempfile.TemporaryDirectory() as temp_dir:
                path = Path(temp_dir) / "README.md"
                path.write_text(content, encoding="utf-8")
                stderr = io.StringIO()
                with (
                    mock.patch.object(render_readme, "README_PATH", path),
                    mock.patch.object(sys, "argv", ["render_readme.py", "--check"]),
                    contextlib.redirect_stderr(stderr),
                    self.assertRaises(SystemExit) as raised,
                ):
                    render_readme.main()
                self.assertEqual(raised.exception.code, 2)
                self.assertIn("error:", stderr.getvalue())
                self.assertNotIn("Traceback", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
