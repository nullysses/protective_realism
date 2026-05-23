.PHONY: setup test run-compact grade-compact summarize clean

setup:
	python -m pip install -e .

test:
	python -m pytest

run-compact:
	python scripts/run_subjects.py --cases cases/example_cases.yaml --condition compact_pr --model $${SUBJECT_MODEL:-gpt-5.5} --out outputs/raw/compact_pr.jsonl

grade-compact:
	python scripts/run_grader.py --raw outputs/raw/compact_pr.jsonl --model $${GRADER_MODEL:-gpt-5.5} --out outputs/graded/compact_pr.graded.jsonl

summarize:
	python scripts/summarize.py --graded outputs/graded/*.graded.jsonl --out outputs/summary.csv

clean:
	rm -f outputs/raw/*.jsonl outputs/graded/*.jsonl outputs/*.csv
