# Protective Realism Clean-Instance Test Protocol

## Purpose

This protocol tests whether Protective Realism transfers to clean model instances as an operational reasoning harness rather than merely as conversation-specific shared context.

## Conditions

| Condition | Prompt file | Measures |
|---|---|---|
| `zero_pr` | `docs/prompt_drafts/zero_pr.txt` | Naive convergence without naming the framework |
| `compact_pr` | `docs/prompt_drafts/compact_pr.txt` | Learnability from a compact operational definition |
| `full_pr` | `docs/prompt_drafts/full_pr.txt` | Full-skill operational value |
| `adversarial_pr` | `docs/prompt_drafts/adversarial_pr.txt` | Robustness against laundering, framing contamination, and bad-faith exploitation |

## Experimental unit

```text
case × condition × model × run_index → structured analysis → grader score
```

## Clean-instance controls

- Use one API request per case/condition/run.
- Do not pass previous responses into later requests.
- Do not use a persistent conversation object.
- Set `store=False`.
- Randomize case order when running larger experiments.
- Keep case text fixed across conditions.
- Keep grader prompt fixed across all conditions.

## Interpreting results

The main signal is not whether the output agrees with an expected verdict. The main signal is whether the framework improves:

- factual hygiene;
- source-frame risk detection;
- temporal-origin discipline;
- affect-vector mapping;
- relation-state mapping;
- role-transition handling;
- scoundrel vs predator distinction;
- force discipline;
- anti-contamination robustness;
- refusal to collapse into law, ideology, popularity, or pure utility.

## Recommended first run

```text
10 cases × 4 conditions × 3 repeated runs = 120 subject outputs
120 grader calls
1 summary CSV
```

This is enough to detect whether the framework produces a stable discipline gain over naive moral analysis.

## Human audit

Use model grading for scale, but human-audit at least 10–20% of outputs. Focus especially on:

- high scores given to obviously contaminated answers;
- low scores given to morally dissenting but structurally disciplined answers;
- cases where the grader rewards ideological agreement rather than Protective Realism discipline.
