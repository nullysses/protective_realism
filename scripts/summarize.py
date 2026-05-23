#!/usr/bin/env python
from __future__ import annotations

import argparse
import glob
from pathlib import Path

import pandas as pd

from protective_realism_eval.io import read_jsonl


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Summarize Protective Realism grader outputs.")
    parser.add_argument("--graded", nargs="+", required=True, help="One or more graded JSONL files; globs are accepted by the shell.")
    parser.add_argument("--out", required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    paths: list[str] = []
    for item in args.graded:
        matches = glob.glob(item)
        paths.extend(matches or [item])

    records = []
    for path in paths:
        for row in read_jsonl(path):
            grade = row["grade"]
            scores = grade["scores"]
            records.append({
                "case_id": row["case_id"],
                "title": row.get("title", ""),
                "condition": row["condition"],
                "subject_model": row.get("model", ""),
                "grader_model": row.get("grader_model", ""),
                "run_index": row.get("run_index", 0),
                **scores,
                "total_score": grade["total_score"],
                "normalized_score": grade["normalized_score"],
            })

    df = pd.DataFrame(records)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.out, index=False)
    print(f"wrote {len(df)} rows → {args.out}")
    if not df.empty:
        print(df.groupby("condition")["normalized_score"].agg(["count", "mean", "std"]).to_string())


if __name__ == "__main__":
    main()
