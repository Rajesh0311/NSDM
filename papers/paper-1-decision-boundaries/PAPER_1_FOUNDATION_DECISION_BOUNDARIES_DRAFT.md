# Paper 1 Foundation Draft — Neuro-Symbolic Decision Boundaries

## Working Title

Neuro-Symbolic Decision Boundaries: A Benchmark for Distinguishing Support, Contradiction, Under-Specification, Governance Ambiguity, and Reward-Aligned but Unjustified Action

---

## Paper Status

Status: foundation paper draft  
Role: primary NSDM anchor paper  
Public suitability: suitable for public mirror after final review  
Benchmark: NSDM-Bench-0 v0.4 batch 1  
Items: 60  
Main repeated-run model: gpt-4.1-mini  

---

## Core Thesis

AI should not only answer.

It should know whether it is justified.

NSDM — Neuro-Symbolic Decision Boundaries — is a research programme for evaluating whether AI systems can distinguish justified decisions from decisions that are unsupported, contradicted, under-specified, governance-ambiguous, or reward-aligned but unjustified.

The central question is not only:

Did the AI produce a plausible or correct answer?

The deeper question is:

Was the AI justified in producing that answer or recommending that action?

---

## Abstract

AI systems are increasingly used to support, recommend, and automate decisions. Standard evaluation often asks whether an output is correct, plausible, or aligned with a target answer. However, a decision can appear correct while still being unjustified. It may rely on missing premises, unclear authority, ambiguous governance rules, or reward-seeking behaviour that satisfies a metric while violating a higher constraint.

This paper introduces Neuro-Symbolic Decision Boundaries, a framework and seed benchmark for evaluating whether AI decisions are justified by available evidence, rules, and governance context. We present NSDM-Bench-0, a 60-item seed benchmark covering supported, contradicted, under-specified, ambiguous-governance, and reward-aligned-but-unjustified decisions. We evaluate a ladder of lexical, symbolic, modular, evidence-state, zero-shot LLM, and few-shot LLM baselines.

The results show that aggregate accuracy can hide important boundary failures. A zero-shot gpt-4.1-mini baseline achieved a five-run mean accuracy of 0.703, with strong performance on conventional support and contradiction but zero mean recall on ambiguous_governance and reward_aligned_unjustified. A few-shot version improved repeated-run mean accuracy to 0.753 and improved governance ambiguity recall from 0.000 to 0.200, but reward-aligned unjustified action remained unstable, with mean recall of 0.143.

These findings suggest that decision-boundary awareness is a distinct capability not captured by ordinary correctness evaluation. NSDM reframes AI evaluation around a deeper question: not only whether the model can answer, but whether the answer or action is justified.

---

## One-Sentence Contribution

This paper introduces NSDM-Bench-0, a seed benchmark for testing whether AI systems can distinguish justified decisions from unsupported, contradicted, under-specified, governance-ambiguous, and reward-aligned but unjustified decisions.

---

## Introduction

AI systems are moving from text generation into decision support and action. They recommend approvals, classify claims, route workflows, interpret policies, summarise evidence, draft responses, and increasingly act on behalf of users. As these systems become more capable, the central evaluation question changes.

It is no longer enough to ask whether the AI produced a plausible answer.

A more important question is whether the AI was justified in producing that answer or recommending that action.

This distinction matters because many risky AI decisions are not obvious hallucinations. They may be fluent, useful, operationally efficient, or even correct under a narrow interpretation. Yet they may still be unjustified because the evidence is incomplete, a required premise is missing, the governing authority is unclear, or the system has optimised for a reward while violating a higher constraint.

For example, an automated system may close a service ticket because the user stopped replying. This may improve resolution metrics, but it may be unjustified if the governing rule requires explicit fix confirmation. A compliance assistant may recommend an escalation because a policy permits discretionary review, but the authority boundary may be opaque or ambiguous. A claims system may appear to follow evidence while ignoring a missing certification requirement. In each case, the issue is not merely whether the answer is true or false. The issue is whether the decision is justified.

NSDM begins from the claim that safe and governed AI systems require decision-boundary awareness. A system should be able to distinguish:

- when a decision is supported by the available evidence and rules
- when a decision is contradicted by the available evidence or rules
- when a decision may be possible but is under-specified
- when authority, policy, or governance context is ambiguous
- when an action achieves a reward or metric but remains unjustified

These are evidence-state distinctions. They are related to factual accuracy, but they are not reducible to it.

The central hypothesis of NSDM is that many AI evaluation failures occur because models collapse these boundaries. A model may treat governance ambiguity as support. It may treat missing premises as ordinary unsupported claims. It may recognise that a rule is violated but miss the fact that the proposed action is attractive because it satisfies a reward. These boundary collapses are important because they correspond to real risks in AI deployment.

---

## Benchmark

NSDM-Bench-0 is a seed benchmark of decision-boundary examples.

Current version:

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

The research includes a baseline ladder across:

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

Aggregate accuracy can hide important decision-boundary failures.

Baseline 008, a zero-shot gpt-4.1-mini classifier, achieved a five-run mean accuracy of 0.703.

However, label-level analysis showed:

- supported mean recall: 1.000
- contradicted mean recall: 1.000
- ambiguous_governance mean recall: 0.000
- reward_aligned_unjustified mean recall: 0.000

This means the model appeared competent on ordinary support and contradiction while failing on the two labels most specific to NSDM.

---

## Few-Shot Result

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

## Discussion

The current NSDM-Bench-0 results suggest that ordinary support and contradiction are easier than deeper decision-boundary categories.

Governance ambiguity remains difficult because it requires the system to recognise unclear authority, discretionary policy, institutional opacity, or ambiguous approval paths.

Reward-aligned but unjustified action remains difficult because it requires the system to distinguish successful optimisation from justified action.

This matters for AI safety, governance, and enterprise deployment.

A system may satisfy a metric, close a workflow, answer a question, or recommend an action while still being unjustified.

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

## Public Limitations Statement

NSDM-Bench-0 is currently a seed benchmark.

The current 60-item version has no true unsupported examples.

The reported LLM results are specific to:

- the benchmark version
- the model tested
- the prompt conditions
- the repeated-run setup

The results should not be interpreted as a general claim about all LLMs.

---

## What This Paper Does Not Claim

This paper does not claim that all LLMs fail on governance ambiguity.

It does not claim that gpt-4.1-mini cannot improve under stronger prompting, retrieval, fine-tuning, or tool use.

It does not claim that NSDM-Bench-0 is complete.

It does not claim that the label taxonomy is final.

This is a seed benchmark and early research programme.

---

## Relationship to Other NSDM Papers

### Paper 1 — Decision Boundaries and Benchmark

This foundation paper defines the core NSDM framework, introduces NSDM-Bench-0, reports the baseline ladder, and presents repeated LLM evaluation results.

### Paper 2 — Boundary Entropy and Decision Instability

The entropy paper is not replaced by this work.

It is strengthened by the Baseline 008 and Baseline 009 repeated-run results. It will study entropy, instability, and uncertainty across labels, runs, models, and prompt conditions.

### Paper 3 — Mathematical Foundations of NSDM

The mathematics paper is not replaced by this work.

It should formalise the NSDM framework after Paper 1 stabilises the empirical label taxonomy and Paper 2 clarifies instability and entropy behaviour.

---

## Future Work

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

## Paper-Safe Claim

The current NSDM-Bench-0 results suggest that evidence-state decision boundaries expose failure modes that are not visible in aggregate accuracy alone.

In particular, gpt-4.1-mini performs strongly on conventional support and contradiction, but struggles with governance ambiguity and reward-aligned but unjustified action under zero-shot prompting.

Few-shot demonstrations improve overall performance and governance ambiguity recall, but repeated-run analysis shows that the most NSDM-specific categories remain difficult.

---

## Closing Statement

AI should not only answer.

It should know whether it is justified.

That is the foundation of NSDM.
