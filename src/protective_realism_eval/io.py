from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

import yaml

ROOT = Path(__file__).resolve().parents[2]


def read_text(path: str | Path) -> str:
    return Path(path).read_text(encoding="utf-8")


def read_json(path: str | Path) -> dict[str, Any]:
    return json.loads(read_text(path))


def read_yaml(path: str | Path) -> Any:
    return yaml.safe_load(read_text(path))


def write_jsonl(path: str | Path, rows: Iterable[dict[str, Any]]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def append_jsonl(path: str | Path, row: dict[str, Any]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def read_jsonl(path: str | Path) -> list[dict[str, Any]]:
    rows = []
    with Path(path).open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def load_prompt(condition: str, prompts_dir: str | Path = "docs/prompt_drafts") -> str:
    prompt_path = Path(prompts_dir) / f"{condition}.txt"
    prompt = read_text(prompt_path)
    if "{{PROTECTIVE_REALISM_SKILL}}" in prompt:
        skill = read_text("docs/protective_realism_analysis_skill_v0_4_3.md")
        prompt = prompt.replace("{{PROTECTIVE_REALISM_SKILL}}", skill)
    return prompt
