# Protective Realism

Protective Realism is a portable moral-reasoning harness for analyzing repeated affective relations under power. It centers harm dynamics, agency, coercion, predation, guardianship, repair, proportionate defense, boundary response, and factual-hygiene discipline.

This repository contains:

- the **Protective Realism Analysis Skill v0.4.3**;
- prompt drafts for clean-instance testing;
- JSON schemas for structured model outputs and grader outputs;
- sample morally complex benchmark cases;
- a small Python eval harness for running subject models, grading outputs, and summarizing score deltas.

## Repository layout

```text
protective_realism/
  docs/
    protective_realism_analysis_skill_v0_4_3.md
    test_protocol.md
    prompt_drafts/
      zero_pr.txt
      compact_pr.txt
      full_pr.txt
      adversarial_pr.txt
      grader_prompt.txt
  cases/
    example_cases.yaml
  schemas/
    analysis_schema.json
    grade_schema.json
  src/protective_realism_eval/
    __init__.py
    client.py
    io.py
  scripts/
    run_subjects.py
    run_grader.py
    summarize.py
  tests/
    test_schema_files.py
```

## What this harness tests

The harness is designed to distinguish four questions:

1. **Naive convergence:** Does a clean model naturally produce Protective-Realism-like reasoning without being taught the framework?
2. **Learnability:** Can a clean model operationalize a compact Protective Realism spec?
3. **Full-spec value:** Does the full skill improve factual hygiene, role mapping, and adversarial resistance?
4. **Robustness:** Does the framework resist laundering through ideology, legality, institutional self-description, charismatic framing, or uncertainty?

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env
# edit .env and set OPENAI_API_KEY
```

Run the subject model on all example cases using the compact Protective Realism prompt:

```bash
python scripts/run_subjects.py \
  --cases cases/example_cases.yaml \
  --condition compact_pr \
  --model gpt-5.5 \
  --out outputs/raw/compact_pr.jsonl
```

Grade those outputs:

```bash
python scripts/run_grader.py \
  --raw outputs/raw/compact_pr.jsonl \
  --model gpt-5.5 \
  --out outputs/graded/compact_pr.graded.jsonl
```

Summarize scores:

```bash
python scripts/summarize.py \
  --graded outputs/graded/compact_pr.graded.jsonl \
  --out outputs/summary.csv
```

## Recommended first experiment

Run each case under four conditions:

```bash
for condition in zero_pr compact_pr full_pr adversarial_pr; do
  python scripts/run_subjects.py \
    --cases cases/example_cases.yaml \
    --condition "$condition" \
    --model gpt-5.5 \
    --out "outputs/raw/${condition}.jsonl"

  python scripts/run_grader.py \
    --raw "outputs/raw/${condition}.jsonl" \
    --model gpt-5.5 \
    --out "outputs/graded/${condition}.graded.jsonl"
done

python scripts/summarize.py --graded outputs/graded/*.graded.jsonl --out outputs/summary.csv
```

Then inspect the score deltas:

```text
compact_pr - zero_pr
full_pr - compact_pr
adversarial_pr - compact_pr
```

The target finding is not that the model agrees with a preferred verdict. The target finding is whether Protective Realism reliably improves factual hygiene, affect mapping, relation-state discipline, and manipulation resistance over the same case without the framework.

## Clean-instance discipline

For API-based testing, the harness creates one independent request per case/condition and does not pass previous response state. The request code sets `store=False` and avoids conversation identifiers so prior runs do not intentionally leak into later runs.

## Version note

The uploaded source file was named as `v0_4_3` and includes a `v0.4.2 → v0.4.3` changelog, while its first Markdown heading still said `v0.4.2`. The canonical repo copy normalizes the heading to `v0.4.3`.

## License

No open-source license has been selected yet. Until a license is added, all rights are reserved by default.
