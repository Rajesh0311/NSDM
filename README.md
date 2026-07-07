# NSDM — Neuro-Symbolic Decision Boundaries

**AI should not only answer. It should know whether it is justified.**

NSDM is a research programme for evaluating whether AI systems can distinguish justified decisions from decisions that are unsupported, contradicted, under-specified, governance-ambiguous, or reward-aligned but unjustified.

The central question is:

> Was the AI justified in producing this answer or recommending this action?

---

## Current Status

NSDM has advanced from concept into a measurable research programme.

Current public milestone:

- NSDM-Bench-0 seed benchmark direction
- Paper 1 foundation draft
- repeated LLM baseline results
- paper-ready result tables
- release notes and website update copy
- roadmap papers for boundary entropy and mathematical foundations

---

## Foundation Paper

The current anchor paper is:

**Neuro-Symbolic Decision Boundaries: A Benchmark for Distinguishing Support, Contradiction, Under-Specification, Governance Ambiguity, and Reward-Aligned but Unjustified Action**

Draft files:

- `papers/paper-1-decision-boundaries/PAPER_1_FOUNDATION_DECISION_BOUNDARIES_DRAFT.md`
- `papers/paper-1-decision-boundaries/PAPER_1_ABSTRACT_INTRODUCTION_DRAFT.md`
- `papers/paper-1-decision-boundaries/PAPER_1_RESULTS_SECTION_DRAFT.md`
- `papers/paper-1-decision-boundaries/PAPER_1_DISCUSSION_SECTION_DRAFT.md`

---

## Current Results Snapshot

| Evaluation | Mean Accuracy |
|---|---:|
| Clean modular boundary reasoner | 0.733 |
| Evidence-state reasoner v0.2 | 0.733 |
| Zero-shot LLM, gpt-4.1-mini, five-run mean | 0.703 |
| Few-shot LLM, gpt-4.1-mini, five-run mean | 0.753 |

---

## Key Finding

Aggregate accuracy can hide important decision-boundary failures.

A zero-shot LLM baseline performed strongly on conventional support and contradiction but had zero mean recall on:

- `ambiguous_governance`
- `reward_aligned_unjustified`

Few-shot demonstrations improved overall performance and governance ambiguity recall, but the most NSDM-specific categories remain difficult.

---

## Why This Matters

Many risky AI decisions are not obvious hallucinations.

A system may produce an answer or action that is:

- fluent
- useful
- operationally efficient
- aligned with a metric
- commercially attractive
- locally plausible

but still unjustified.

NSDM studies this gap.

It asks whether an output or action is justified by:

- available evidence
- governing rules
- missing premises
- contradiction checks
- authority boundaries
- governance context
- reward-versus-justification separation

---

## Current Labels

NSDM-Bench-0 currently uses the following evidence-state labels:

- `supported`
- `unsupported`
- `contradicted`
- `under_specified`
- `ambiguous_governance`
- `reward_aligned_unjustified`

Important limitation:

The current 60-item benchmark has no true `unsupported` examples. The next benchmark expansion must add true unsupported examples and increase coverage from 60 to 100 examples.

---

## Result Tables

Public result tables are available in:

- `results/paper_tables/baseline_accuracy_table.md`
- `results/paper_tables/per_label_metrics.md`
- `results/paper_tables/confusion_matrix_baseline_009.md`
- `results/paper_tables/failure_frontier_baseline_009.md`

---

## Related NSDM Papers

### Paper 1 — Decision Boundaries and Benchmark

Status: active foundation paper.

This paper defines the NSDM framework, introduces NSDM-Bench-0, reports the baseline ladder, and presents repeated LLM evaluation results.

### Paper 2 — Boundary Entropy and Decision Instability

Status: planned / retained.

This paper will study boundary entropy, label instability, decision volatility, prompt-conditioned uncertainty, and model uncertainty around NSDM justification boundaries.

### Paper 3 — Mathematical Foundations of NSDM

Status: planned / retained.

This paper will formalise evidence states, rule sets, claim/action spaces, governance context, reward pressure, justification functions, boundary classifiers, contradiction operators, governance ambiguity operators, reward-justification divergence, and entropy over decision labels.

---

## Limitations

NSDM-Bench-0 is currently a seed benchmark.

The reported LLM results are specific to:

- the benchmark version
- the model tested
- the prompt conditions
- the repeated-run setup

The results should not be interpreted as a general claim about all LLMs.

---

## Roadmap

Immediate next steps:

1. Expand NSDM-Bench-0 from 60 to 100 examples.
2. Add true unsupported examples.
3. Add more governance ambiguity examples.
4. Add more reward-aligned unjustified examples.
5. Create a dataset card.
6. Prepare the first public Paper 1 preprint draft.
7. Test additional models.
8. Build a structured neuro-symbolic boundary evaluator.
9. Develop the boundary entropy paper.
10. Develop the mathematical foundations paper.

---

## Release Notes

Current research update:

- `docs/releases/RELEASE_NOTES_NSDM_RESEARCH_UPDATE_2026_07_07.md`

Website copy:

- `docs/website/WEBSITE_UPDATE_COPY_NSDM_RESEARCH_2026_07_07.md`

---

## Core Principle

AI evaluation should not stop at whether the answer is plausible or correct.

A trustworthy AI system should be able to say:

- I can answer.
- I cannot answer.
- This action is contradicted.
- This action may be possible, but a premise is missing.
- This action appears useful, but it is not justified.
- This action depends on unclear authority.

That is the foundation of NSDM.
