# NSDM Research Update — 2026-07-07

## Title

NSDM Research Update: Evidence-State Decision Boundaries, LLM Baselines, and Sovereign AI Stack Justification

---

## One-Line Summary

We advanced NSDM from a concept into a measurable research programme with a seed benchmark, baseline ladder, repeated LLM evaluations, Paper 1 draft sections, and an applied sovereignty branch for enterprise AI stack justification.

---

## What Changed

This release consolidates the latest NSDM research work around Neuro-Symbolic Decision Boundaries.

The central research question is:

Can an AI system distinguish whether a decision is justified by available evidence, rules, and governance context?

NSDM does not only ask whether an AI output is plausible or correct. It asks whether the output or action is justified.

---

## New Research Artifacts

### Paper 1 Draft Spine

The first Paper 1 draft components are now in place:

- Abstract and Introduction draft
- Results section draft
- Discussion section draft
- Paper-ready baseline tables
- Confusion matrices
- Failure frontier tables

Working title:

Neuro-Symbolic Decision Boundaries: A Benchmark for Distinguishing Support, Contradiction, Under-Specification, Governance Ambiguity, and Reward-Aligned but Unjustified Action

---

## Benchmark Status

Current benchmark:

- Name: NSDM-Bench-0
- Version: v0.4 batch 1
- Items: 60
- Format: JSONL
- Status: internal seed benchmark

Current labels:

- supported
- unsupported
- contradicted
- under_specified
- ambiguous_governance
- reward_aligned_unjustified

Important limitation:

The current 60-item benchmark has no true unsupported examples. The next benchmark expansion must add true unsupported examples and increase the benchmark from 60 to 100 examples.

---

## Baseline Ladder

The research now includes a baseline ladder across:

- lexical / majority baseline
- early symbolic checker
- raw symbolic checker
- structured symbolic reasoner
- clean modular boundary reasoner
- evidence-state reasoner
- zero-shot LLM baseline
- few-shot LLM baseline

Current clean comparison results:

| Baseline | Description | Accuracy |
|---|---|---:|
| Baseline 006 | Clean modular boundary reasoner | 0.733 |
| Baseline 007 v0.2 | Evidence-state reasoner v0.2 | 0.733 |
| Baseline 008 | Zero-shot LLM, gpt-4.1-mini, five-run mean | 0.703 |
| Baseline 009 | Few-shot LLM, gpt-4.1-mini, five-run mean | 0.753 |

---

## Key Empirical Finding

Aggregate accuracy hides important decision-boundary failures.

Baseline 008, a zero-shot gpt-4.1-mini classifier, achieved a five-run mean accuracy of 0.703.

However, label-level analysis showed:

- supported mean recall: 1.000
- contradicted mean recall: 1.000
- ambiguous_governance mean recall: 0.000
- reward_aligned_unjustified mean recall: 0.000

This means the model appeared competent on ordinary support and contradiction while failing on the two labels most specific to NSDM.

---

## Few-Shot LLM Result

Baseline 009 tested whether few-shot demonstrations improve NSDM-specific boundary recognition.

Repeated-run result:

- Model: gpt-4.1-mini
- Condition: few-shot
- Runs: 5
- Items per run: 60
- Mean accuracy: 0.753
- Standard deviation: 0.007
- Minimum accuracy: 0.750
- Maximum accuracy: 0.767

Comparison to Baseline 008:

| Metric | Baseline 008 Zero-Shot Mean | Baseline 009 Few-Shot Mean | Change |
|---|---:|---:|---:|
| Accuracy | 0.703 | 0.753 | +0.050 |
| ambiguous_governance recall | 0.000 | 0.200 | +0.200 |
| reward_aligned_unjustified recall | 0.000 | 0.143 | +0.143 |
| under_specified recall | 0.563 | 0.691 | +0.128 |

Interpretation:

Few-shot prompting improves overall NSDM-Bench-0 performance relative to zero-shot prompting. It also improves governance ambiguity recognition from zero to a measurable non-zero recall.

However, reward_aligned_unjustified remains difficult and unstable across runs. This suggests that reward-versus-justification separation may require stronger architecture, not only prompt examples.

---

## Leakage Audit

One structured baseline achieved 0.967 accuracy, but this was identified as leakage-inflated because task-family metadata mapped too directly to target labels.

This result is not treated as the best valid baseline.

Instead, it is reported as a leakage audit showing why benchmark metadata and shortcut controls matter.

---

## Main Research Interpretation

NSDM-Bench-0 exposes evidence-state distinctions that ordinary correctness evaluation can hide.

The current evidence suggests:

- support and contradiction are comparatively easier
- governance ambiguity is a distinct and difficult boundary
- reward-aligned but unjustified action is not reliably captured by ordinary contradiction detection
- few-shot prompting helps but does not solve the deepest NSDM-specific categories
- per-label recall is more informative than aggregate accuracy alone

---

## NSDM-S: Sovereign Decision Boundaries

This release also adds the NSDM-S roadmap branch.

NSDM-S extends decision-boundary reasoning from model outputs to enterprise AI stacks.

The applied question becomes:

Is the organisation justified in using this AI stack, exposing this data, paying this token cost, depending on this vendor, and allowing this system to influence decisions?

NSDM-S connects the research programme to applied enterprise products such as:

- AI Stack Justification Layer
- Alpha Boundary Audit
- Token Justification Audit
- Sovereign AI Readiness Score
- Model Routing Justification
- Data Exposure Risk Classifier
- Vendor Dependency Score
- Enterprise AI Control Boundary

---

## Paper-Safe Claim

The current NSDM-Bench-0 results suggest that evidence-state decision boundaries expose failure modes that are not visible in aggregate accuracy alone.

In particular, gpt-4.1-mini performs strongly on conventional support and contradiction, but struggles with governance ambiguity and reward-aligned but unjustified action under zero-shot prompting.

Few-shot demonstrations improve overall performance and governance ambiguity recall, but repeated-run analysis shows that the most NSDM-specific categories remain difficult.

---

## What This Does Not Claim

This release does not claim that all LLMs fail on governance ambiguity.

It does not claim that gpt-4.1-mini cannot improve under stronger prompting, retrieval, fine-tuning, or tool use.

It does not claim that NSDM-Bench-0 is complete.

It does not claim that the label taxonomy is final.

This is a seed benchmark and early research programme.

---

## Next Research Work

Immediate next steps:

1. Expand NSDM-Bench-0 from 60 to 100 examples.
2. Add true unsupported examples.
3. Add more governance ambiguity examples.
4. Add more reward-aligned unjustified examples.
5. Create a dataset card.
6. Create a methods section draft.
7. Create a limitations section draft.
8. Prepare the first public Paper 1 preprint draft.
9. Decide which artifacts to mirror to the public NSDM repository.
10. Update the public website with a research milestone release.

---

## Public Website Message

Short public message:

AI should not only answer. It should know whether it is justified.

NSDM is building a benchmark and research framework for testing whether AI systems can distinguish supported decisions from contradicted, under-specified, governance-ambiguous, and reward-aligned but unjustified decisions.

The latest internal results show that a capable low-cost LLM performs strongly on ordinary support and contradiction, but struggles with governance ambiguity and reward-aligned unjustified action. Few-shot prompting improves performance, but does not fully solve the hardest boundary categories.

This is why decision-boundary awareness should be treated as a distinct capability for trustworthy AI.

---

## Release Status

Status: internal release notes ready  
Website update: pending  
Public repo mirror: pending  
Paper 1 preprint: in progress  
