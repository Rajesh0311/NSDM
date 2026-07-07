# Paper 1 Results Section Draft — NSDM Decision Boundaries

## Purpose

This document drafts the Results section for Paper 1.

Paper 1 working title:

Neuro-Symbolic Decision Boundaries: A Benchmark for Distinguishing Support, Contradiction, Under-Specification, Governance Ambiguity, and Reward-Aligned but Unjustified Action

This section is based on the current NSDM-Bench-0 v0.4 batch 1 results.

---

## Benchmark Version

Benchmark: NSDM-Bench-0  
Version: v0.4 batch 1  
Items: 60  
Format: JSONL  
Status: internal seed benchmark  
Public status: not yet public

Current labels:

- supported
- unsupported
- contradicted
- under_specified
- ambiguous_governance
- reward_aligned_unjustified

Important limitation:

The current 60-item benchmark has no true unsupported examples in the generated confusion matrix. The 100-example expansion must add true unsupported examples.

---

## Result Overview

We evaluated a sequence of baselines on NSDM-Bench-0 to test whether systems can classify evidence-state decision boundaries.

The baseline ladder includes lexical, symbolic, structured, modular, evidence-state, zero-shot LLM, and few-shot LLM approaches.

The central empirical pattern is that conventional support and contradiction are easier than NSDM-specific categories such as governance ambiguity and reward-aligned but unjustified action.

---

## Baseline Accuracy Table

Current generated results:

| Baseline | Description | Items | Accuracy | Status |
|---|---:|---:|---:|---|
| Baseline 001 | Lexical / majority-supported baseline | 120 | 0.308 | Historical weak baseline; not directly comparable |
| Baseline 002 | Early symbolic checker | 24 | 1.000 | Historical early baseline; not directly comparable |
| Baseline 003 | Raw symbolic checker | 60 | 0.517 | Current 60-item comparison set |
| Baseline 004 | Structured symbolic reasoner | 60 | 0.967 | Leakage-inflated; audit only |
| Baseline 005 | No-task-family structured reasoner | 60 | 0.667 | Cleaner control |
| Baseline 006 | Clean modular boundary reasoner | 60 | 0.733 | Strongest clean symbolic/modular baseline |
| Baseline 007 | Evidence-state reasoner v0.1 | 60 | 0.600 | Internal/provisional |
| Baseline 007 v0.2 | Evidence-state reasoner v0.2 | 60 | 0.733 | Evidence-state JSONL output |
| Baseline 008 | Zero-shot LLM — gpt-4.1-mini | 60 | 0.683 single official run; 0.703 five-run mean | Repeated-run result available |
| Baseline 009 | Few-shot LLM — gpt-4.1-mini | 60 | 0.767 | Best current clean single-run result |

---

## Leakage Audit Result

Baseline 004 achieved 0.967 accuracy, but this result is leakage-inflated.

The leakage occurred because task-family metadata mapped too directly to target labels.

Known leakage mapping:

- rule_support -> supported
- missing_premise -> under_specified
- ambiguous_governance -> ambiguous_governance
- reward_vs_justification -> reward_aligned_unjustified
- contradiction -> contradicted

This result is not treated as the strongest valid baseline.

Instead, it is reported as a leakage audit showing why benchmark metadata and task-family shortcuts must be controlled.

Paper interpretation:

The leakage-inflated result strengthens rather than weakens the benchmark methodology because it identifies a concrete shortcut risk and motivates the clean comparison baselines.

---

## Clean Symbolic and Modular Baselines

Baseline 005 removed the direct task-family shortcut and achieved 0.667 accuracy.

Baseline 006, the clean modular boundary reasoner, achieved 0.733 accuracy.

Baseline 007 v0.2, the evidence-state reasoner, also achieved 0.733 accuracy while producing evidence-state JSONL outputs.

Interpretation:

The best clean non-LLM baselines currently reach approximately 0.733 accuracy on the 60-item benchmark.

The evidence-state baseline is particularly useful because it produces interpretable intermediate outputs rather than only final labels.

---

## Baseline 008 — Zero-Shot LLM Result

Baseline 008 evaluated gpt-4.1-mini in zero-shot mode.

The single official full run achieved:

Accuracy: 0.683

Because an earlier run produced a different value, Baseline 008 was repeated five times.

Repeated-run aggregate:

- Runs: 5
- Items per run: 60
- Total classifications: 300
- Mean accuracy: 0.703
- Standard deviation: 0.014
- Minimum accuracy: 0.683
- Maximum accuracy: 0.717

Mean recall by label:

| Label | Mean Recall |
|---|---:|
| ambiguous_governance | 0.000 |
| contradicted | 1.000 |
| reward_aligned_unjustified | 0.000 |
| supported | 1.000 |
| under_specified | 0.563 |

Interpretation:

The zero-shot LLM baseline is competitive with clean symbolic and modular baselines but does not outperform the strongest clean baseline.

More importantly, it shows a sharp label-level split.

The model performs reliably on conventional support and contradiction, but repeatedly fails on ambiguous_governance and reward_aligned_unjustified.

This suggests that ordinary zero-shot LLM judgement may collapse NSDM-specific labels into more familiar categories such as supported, contradicted, or under_specified.

---

## Baseline 009 — Few-Shot LLM Result

Baseline 009 evaluated the same model, gpt-4.1-mini, using few-shot label demonstrations.

The purpose was to test whether explicit demonstrations improve the two labels that failed in Baseline 008:

- ambiguous_governance
- reward_aligned_unjustified

Result:

Accuracy: 0.767

Per-label recall:

| Label | Support | Recall |
|---|---:|---:|
| ambiguous_governance | 6 | 0.167 |
| contradicted | 19 | 1.000 |
| reward_aligned_unjustified | 7 | 0.429 |
| supported | 17 | 0.941 |
| under_specified | 11 | 0.636 |
| unsupported | 0 | 0.000 |

Comparison to Baseline 008 repeated-run mean:

| Metric | Baseline 008 zero-shot mean | Baseline 009 few-shot | Change |
|---|---:|---:|---:|
| Accuracy | 0.703 | 0.767 | +0.064 |
| ambiguous_governance recall | 0.000 | 0.167 | +0.167 |
| reward_aligned_unjustified recall | 0.000 | 0.429 | +0.429 |
| supported recall | 1.000 | 0.941 | -0.059 |
| contradicted recall | 1.000 | 1.000 | 0.000 |
| under_specified recall | 0.563 | 0.636 | +0.073 |

Interpretation:

Few-shot prompting improves overall performance and improves the two NSDM-specific labels that failed in zero-shot mode.

The largest improvement is reward_aligned_unjustified, which moves from 0.000 mean recall in zero-shot mode to 0.429 recall in the few-shot run.

Governance ambiguity improves from 0.000 to 0.167 recall, but remains difficult.

This suggests that explicit label demonstrations help the model recognise some NSDM-specific boundaries, but governance ambiguity may require stronger architecture, more targeted demonstrations, or a dedicated governance module.

---

## Failure Pattern Analysis

### Zero-Shot LLM Failure Pattern

Baseline 008 repeatedly failed on:

- ambiguous_governance
- reward_aligned_unjustified

This matters because these are not ordinary factual accuracy labels.

They require the system to recognise that:

- an authority chain may be unclear
- an approval path may be discretionary
- a system may achieve a reward while violating a higher justification constraint
- success on a metric is not equivalent to justified action

### Few-Shot LLM Failure Pattern

Baseline 009 improved reward_aligned_unjustified recognition, but several failures remained.

Remaining failure types include:

- governance ambiguity still being classified as supported or under_specified
- reward-aligned unjustified examples still being classified as contradicted
- under_specified examples being classified as unsupported
- OCR/noisy examples creating uncertainty

The distinction between contradicted and reward_aligned_unjustified remains especially important.

A reward-aligned unjustified action can violate a rule, but the NSDM label captures the specific pattern that the action is attractive because it satisfies a metric or reward while lacking justification.

---

## Main Empirical Finding

The strongest current empirical finding is:

NSDM-Bench-0 exposes evidence-state distinctions that are not captured by ordinary support or contradiction detection.

A low-cost capable LLM performs strongly on conventional support and contradiction, but struggles with governance ambiguity and reward-aligned but unjustified action.

Few-shot demonstrations improve these NSDM-specific categories, but do not fully solve them.

---

## Paper-Ready Claim

Safe paper claim:

On NSDM-Bench-0 v0.4 batch 1, gpt-4.1-mini achieved a five-run zero-shot mean accuracy of 0.703, with perfect mean recall on supported and contradicted labels but zero mean recall on ambiguous_governance and reward_aligned_unjustified. A few-shot prompt improved overall accuracy to 0.767 and improved recall on reward_aligned_unjustified to 0.429 and ambiguous_governance to 0.167.

Unsafe paper claim:

LLMs cannot detect governance ambiguity or reward-aligned unjustified action in general.

The result is model-specific, benchmark-specific, and prompt-condition-specific.

---

## Methodological Lessons

1. Task-family metadata can create leakage.
2. Repeated LLM runs are necessary because single-run values vary.
3. Per-label analysis is more informative than overall accuracy.
4. Governance ambiguity is a distinct and difficult evidence-state boundary.
5. Reward-aligned unjustified action is learnable to some degree with explicit demonstrations.
6. Current benchmark expansion must add true unsupported examples.
7. Few-shot prompting improves results, but may introduce demonstration imitation risk.

---

## Required Figures and Tables

The Paper 1 results section should include:

1. Baseline accuracy table.
2. Leakage audit table.
3. Baseline 008 repeat-run accuracy table.
4. Baseline 008 mean recall by label.
5. Baseline 009 per-label recall.
6. Baseline 008 vs Baseline 009 comparison table.
7. Confusion matrix for Baseline 006.
8. Confusion matrix for Baseline 009.
9. Failure frontier table.
10. Unsupported-label gap note.

---

## Next Results Work

1. Generate confusion matrix for Baseline 009.
2. Generate comparison table: Baseline 008 repeated mean vs Baseline 009.
3. Decide whether Baseline 009 needs repeated-run evaluation.
4. Add true unsupported examples to benchmark expansion.
5. Create dataset card draft.
6. Begin Paper 1 introduction and methods draft.

---

## Baseline 009 Repeated-Run Update

After the initial Baseline 009 single run, Baseline 009 was repeated five times to test stability.

Repeated-run aggregate:

- Runs: 5
- Items per run: 60
- Mean accuracy: 0.753
- Standard deviation: 0.007
- Minimum accuracy: 0.750
- Maximum accuracy: 0.767

Run accuracies:

| Run | Accuracy |
|---|---:|
| run_01 | 0.767 |
| run_02 | 0.750 |
| run_03 | 0.750 |
| run_04 | 0.750 |
| run_05 | 0.750 |

Mean recall by label:

| Label | Mean Recall |
|---|---:|
| ambiguous_governance | 0.200 |
| contradicted | 0.989 |
| reward_aligned_unjustified | 0.143 |
| supported | 0.976 |
| under_specified | 0.691 |
| unsupported | 0.000 |

Comparison to Baseline 008 repeated-run aggregate:

| Metric | Baseline 008 zero-shot mean | Baseline 009 few-shot mean | Change |
|---|---:|---:|---:|
| Accuracy | 0.703 | 0.753 | +0.050 |
| ambiguous_governance recall | 0.000 | 0.200 | +0.200 |
| reward_aligned_unjustified recall | 0.000 | 0.143 | +0.143 |
| supported recall | 1.000 | 0.976 | -0.024 |
| contradicted recall | 1.000 | 0.989 | -0.011 |
| under_specified recall | 0.563 | 0.691 | +0.128 |

Updated interpretation:

The repeated-run result confirms that few-shot prompting improves overall accuracy relative to zero-shot prompting. It also confirms a measurable improvement on ambiguous_governance and under_specified. However, reward_aligned_unjustified remains unstable: the initial single run reached 0.429 recall, but the five-run mean recall is 0.143. Paper 1 should therefore use the repeated-run mean as the primary result and treat the initial single run as the best observed run.

