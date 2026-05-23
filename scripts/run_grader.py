#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone

from dotenv import load_dotenv
from openai import OpenAI

from protective_realism_eval.client import create_structured_response
from protective_realism_eval.io import append_jsonl, read_json, read_jsonl, read_text


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Grade Protective Realism subject outputs.")
    parser.add_argument("--raw", required=True)
    parser.add_argument("--model", default=os.environ.get("GRADER_MODEL", "gpt-5.5"))
    parser.add_argument("--schema", default="schemas/grade_schema.json")
    parser.add_argument("--prompt", default="docs/prompt_drafts/grader_prompt.txt")
    parser.add_argument("--out", required=True)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> None:
    load_dotenv()
    args = parse_args()
    rows = read_jsonl(args.raw)
    schema = read_json(args.schema)
    prompt = read_text(args.prompt)

    if args.dry_run:
        print(json.dumps({"to_grade": len(rows), "first_case": rows[0]["case_id"] if rows else None}, ensure_ascii=False))
        return

    client = OpenAI()
    for row in rows:
        payload = {
            "case_id": row["case_id"],
            "condition": row["condition"],
            "title": row.get("title", ""),
            "analysis": row["analysis"],
        }
        grade = create_structured_response(
            client=client,
            model=args.model,
            system_prompt=prompt,
            user_payload=json.dumps(payload, ensure_ascii=False),
            schema_name="protective_realism_grade",
            schema=schema,
        )
        out_row = {
            **{k: row[k] for k in ["case_id", "title", "condition", "model", "run_index"] if k in row},
            "grader_model": args.model,
            "graded_at": datetime.now(timezone.utc).isoformat(),
            "grade": grade,
        }
        append_jsonl(args.out, out_row)
        print(f"graded {row['case_id']} → {args.out}")


if __name__ == "__main__":
    main()
