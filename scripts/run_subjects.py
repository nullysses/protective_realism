#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone

from dotenv import load_dotenv
from openai import OpenAI

from protective_realism_eval.client import create_structured_response
from protective_realism_eval.io import append_jsonl, load_prompt, read_json, read_yaml


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run subject model analyses for Protective Realism eval cases.")
    parser.add_argument("--cases", default="cases/example_cases.yaml")
    parser.add_argument("--condition", required=True, choices=["zero_pr", "compact_pr", "full_pr", "adversarial_pr"])
    parser.add_argument("--model", default=os.environ.get("SUBJECT_MODEL", "gpt-5.5"))
    parser.add_argument("--schema", default="schemas/analysis_schema.json")
    parser.add_argument("--out", required=True)
    parser.add_argument("--run-index", type=int, default=0)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> None:
    load_dotenv()
    args = parse_args()
    cases = read_yaml(args.cases)
    if args.limit is not None:
        cases = cases[: args.limit]

    prompt = load_prompt(args.condition)
    schema = read_json(args.schema)

    if args.dry_run:
        for case in cases:
            print(json.dumps({"case_id": case["id"], "condition": args.condition, "prompt_preview": prompt[:300]}, ensure_ascii=False))
        return

    client = OpenAI()
    for case in cases:
        user_payload = json.dumps({"case_id": case["id"], "title": case["title"], "case_text": case["text"]}, ensure_ascii=False)
        analysis = create_structured_response(
            client=client,
            model=args.model,
            system_prompt=prompt,
            user_payload=user_payload,
            schema_name="protective_realism_analysis",
            schema=schema,
        )
        row = {
            "case_id": case["id"],
            "title": case["title"],
            "condition": args.condition,
            "model": args.model,
            "run_index": args.run_index,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "analysis": analysis,
        }
        append_jsonl(args.out, row)
        print(f"wrote {case['id']} → {args.out}")


if __name__ == "__main__":
    main()
