# NSDM-Bench-0 IAA Test Protocol — Week 1

**Date:** 3–9 July 2026  
**Gate requirement:** κ ≥ 0.45 minimum, κ ≥ 0.50 target  
**Blocking test:** If κ < 0.45 on `unsupported` vs `under_specified`, sprint halts and guide is revised.

---

## Step 1: Calibration (Day 1 — 3 July)

1. Open `calibration_set.jsonl`
2. Label all 10 examples without reading the `correct_label` field
3. Score yourself: count matches
4. For every mismatch, read the `explanation` and `nearest_alternative_rejection` fields
5. Reread Section 3 of `annotation_guide_v1.md` for any mismatch involving `unsupported` vs `under_specified`
6. Gate: ≥ 8/10 correct before proceeding to IAA test set

---

## Step 2: IAA Test Set Selection (Day 1)

Select 30 examples from the existing 60 validated examples:
- 5 examples per label
- Stratify across domains (general, legal, governance, AI safety, agent)
- Include at least 3 borderline cases near the `unsupported`/`under_specified` boundary
- Copy selected examples to `iaa_test_set.jsonl` with labels REMOVED

---

## Step 3: Independent Annotation (Days 2–4)

- Annotator 1 and Annotator 2 label independently
- No communication during annotation
- Each annotator records: label, confidence, justification, nearest alternative, rejection reason
- All fields in Section 5.1 of the guide are required

---

## Step 4: IAA Calculation (Day 5)

Run `python scripts/compute_iaa.py --input iaa_results.jsonl`

Required outputs:
- Overall Cohen's κ
- Per-label κ (confusion matrix)
- Specific κ for `unsupported` vs `under_specified` pair
- List of all disagreements with both annotators' labels

---

## Step 5: Disagreement Review (Days 5–6)

For each disagreement:
1. Both annotators state their reasoning (2 sentences each)
2. Apply the decision tree from Section 4 of the guide jointly
3. Record resolution in `adjudication_log.md`
4. Identify guide gaps exposed — add to ambiguity ledger

---

## Step 6: Gate Decision (Day 7)

| κ Result | Action |
|----------|--------|
| κ ≥ 0.65 | Annotation quality excellent. Proceed to full Bench-0 annotation and Paper 1 drafting. |
| κ 0.50–0.64 | Gate passed. Document disagreement sources. Update guide. Continue with caution. |
| κ 0.45–0.49 | Gate minimum reached. Mandatory guide revision before next annotation round. |
| κ < 0.45 | SPRINT HALT. The `unsupported`/`under_specified` distinction is not yet operationalised. Revise definitions and decision tree. Repeat calibration. |

---

## Falsification Criteria

The annotation guide fails if:
- κ on `unsupported`/`under_specified` distinction < 0.45 after two annotation rounds
- More than 40% of `reward_aligned_unjustified` annotations fail to name R and C*
- More than 30% of `under_specified` annotations fail to name the specific missing premise

These failures require definitional revision before any results are reported.

