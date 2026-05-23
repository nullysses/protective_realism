from __future__ import annotations

import json
from pathlib import Path

from jsonschema.validators import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]


def test_analysis_schema_is_valid_json_schema() -> None:
    schema = json.loads((ROOT / "schemas" / "analysis_schema.json").read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)


def test_grade_schema_is_valid_json_schema() -> None:
    schema = json.loads((ROOT / "schemas" / "grade_schema.json").read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)


def test_prompt_drafts_exist() -> None:
    for name in ["zero_pr", "compact_pr", "full_pr", "adversarial_pr", "grader_prompt"]:
        path = ROOT / "docs" / "prompt_drafts" / f"{name}.txt"
        assert path.exists(), f"missing {path}"
        assert path.read_text(encoding="utf-8").strip()


def test_skill_version_is_normalized() -> None:
    text = (ROOT / "docs" / "protective_realism_analysis_skill_v0_4_3.md").read_text(encoding="utf-8")
    assert text.startswith("# Protective Realism Analysis Skill v0.4.3")
