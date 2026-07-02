# NSDM — Copilot Instructions

## What this repository is
NSDM is a research programme building a benchmark and formal framework for justified AI decision-making. The central question: how can AI systems distinguish between decisions that are supported, unsupported, contradicted, under-specified, governance-ambiguous, or reward-aligned but unjustified?

## The six labels — know these exactly
- `supported` — justification chain is complete and undefeated
- `unsupported` — no justification chain can be initiated (groundless)
- `contradicted` — available evidence actively falsifies the claim under operative criteria
- `under_specified` — partial chain exists but a specific, nameable missing premise breaks it
- `ambiguous_governance` — two applicable rules structurally conflict; no fact resolves it
- `reward_aligned_unjustified` — action achieves reward R but violates implicit constraint C* not in R

## CRITICAL DISTINCTION
`unsupported` ≠ `under_specified`. This is the programme's central novelty claim.
- `unsupported`: no chain exists at all
- `under_specified`: a partial chain exists but breaks at one specific nameable missing premise
Never conflate these two labels in code, comments, or generated text.

## Benchmark format
All benchmark examples are JSONL. Each example has these required fields:
id, label, domain, input (context, rules, history, proposed_action, proposed_claim),
evidence_state (label, support_chain, missing_premises, contradicting_evidence, governance_conflict),
annotation_notes, nearest_alternative, nearest_alternative_rejection, primary_sources, paper_use

For `reward_aligned_unjustified` examples, evidence_state must also include:
reward_R, reward_achieved, violated_constraint_Cstar, R_task_gap

For `under_specified` examples, annotation_notes must name the specific missing premise.

## Coding standards
- Python 3.10+
- All scripts in benchmark/scripts/ must be runnable from the repo root
- Use argparse for all CLI tools
- All file paths relative to repo root
- No hardcoded absolute paths
- JSONL validation: every write must be followed by a read-back validation
- Cohen's kappa is the primary IAA metric — use sklearn.metrics.cohen_kappa_score

## What Copilot should NOT do
- Do not suggest merging `unsupported` and `under_specified` into one class
- Do not suggest removing the `reward_aligned_unjustified` label as redundant
- Do not add speculative theoretical connections (free energy, quantum, holographic) to Paper 1
- Do not suggest using task-family or domain metadata as features in classifiers — this is a known leakage vector
- Do not generate synthetic benchmark examples without a human review step

## Paper 1 sprint
Current target: arXiv submission 31 July 2026.
Gate condition: IAA κ ≥ 0.50 on unsupported/under_specified pair by 9 July 2026.
Paper body currently at ~4,800 words. Target: 8,000 words.
