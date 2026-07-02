# NSDM — Architectural Decisions Log

**Purpose:** Record significant decisions about the research programme, benchmark design, and paper strategy.  
**Rule:** Every decision that would be hard to reverse or that affects reproducibility must be logged here.  
**Format:** Each entry includes context, decision, rationale, alternatives rejected, and consequences.

---

## ADR-001: Six-Class Taxonomy (Not Three, Not Eight)

**Date:** July 2026  
**Status:** Accepted  
**Context:** Multiple possible granularities for the label set were considered. NLI has 3 classes. An expanded version could add 8+ classes (including temporal, causal, probabilistic).  
**Decision:** Six classes: `supported`, `unsupported`, `contradicted`, `under_specified`, `ambiguous_governance`, `reward_aligned_unjustified`.  
**Rationale:** The six classes cover the most practically important failure modes in AI governance and decision-making while remaining operationalisable by human annotators. Fewer than six collapses the central distinction (`unsupported` ≠ `under_specified`). More than six may reduce IAA below usable thresholds for a 60-example benchmark.  
**Alternatives rejected:** (a) 3-class (NLI-style) — collapses the central novelty. (b) 8-class (adding temporal, causal subclasses) — annotation complexity too high at 60 examples.  
**Consequences:** Any model that achieves near-chance performance on the 6-class task is still scientifically informative — it demonstrates the difficulty of the taxonomy.

---

## ADR-002: Leakage Control — Remove Task-Family Metadata

**Date:** July 2026  
**Status:** Accepted  
**Context:** An early baseline achieved inflated performance because task-family metadata (governance examples → `ambiguous_governance`, safety examples → `reward_aligned_unjustified`) was predictive of the label without genuine reasoning.  
**Decision:** Remove all domain and task-family metadata from the input format. Report both stratified and unstratified baselines. Disclose the leakage episode in the paper.  
**Rationale:** Transparent disclosure of a methodological failure is a stronger position than concealment. Leakage-inflated results would not survive peer review. The leakage episode is a valuable contribution to benchmark design methodology.  
**Alternatives rejected:** (a) Keep metadata — inflates baselines and undermines novelty claims. (b) Conceal the inflated baseline — integrity risk.  
**Consequences:** All baseline results must be run on the leakage-controlled version. The inflated baseline is included in the results table as a negative example, clearly labelled.

---

## ADR-003: Primary-Source Grounding for Governance Examples

**Date:** July 2026  
**Status:** Accepted  
**Context:** Governance and AI safety examples could be constructed synthetically or drawn from primary sources. Synthetic construction is faster but harder to defend against reviewer challenge.  
**Decision:** All governance and AI safety examples cite verifiable primary sources. The Fable 5 incident examples cite Anthropic official posts, peer-reviewed research, and named journalist reporting.  
**Rationale:** Primary-source grounding makes the label assignments verifiable and falsifiable. A reviewer who disputes a label can examine the source and apply the annotation guide's decision tree. Synthetic examples cannot be independently verified.  
**Alternatives rejected:** (a) Fully synthetic benchmark — faster but defensibility is lower. (b) Anonymised synthetic based on real events — harder to cite and harder to verify.  
**Consequences:** The benchmark's governance examples are time-stamped to specific events. This is a strength (verifiability) and a mild weakness (temporal binding). Future versions should include examples from multiple time periods.

---

## ADR-004: IAA Gate Before Any Results Are Reported

**Date:** July 2026  
**Status:** Accepted  
**Context:** IAA could be run after the full benchmark is constructed and only reported at submission. This is common practice.  
**Decision:** IAA is a gate condition, not a retrospective measurement. If κ < 0.45 on `unsupported`/`under_specified` after two annotation rounds, the sprint halts and the label definitions are revised.  
**Rationale:** The central novelty claim (the `unsupported`/`under_specified` distinction) is falsifiable. If human annotators cannot reliably apply the distinction, the claim is not yet operationalised. Reporting results on a benchmark with κ < 0.45 on the central distinction would be scientifically dishonest.  
**Alternatives rejected:** (a) Report IAA retrospectively at submission — delays discovery of definition problems. (b) Skip IAA entirely — reviewer will require it.  
**Consequences:** The programme has a defined halt condition. This is a strength, not a weakness.

---

## ADR-005: arXiv First, Venue Second

**Date:** July 2026  
**Status:** Accepted  
**Context:** Papers can be submitted directly to venues without prior arXiv posting, or posted to arXiv first.  
**Decision:** Post Paper 1 to arXiv by 31 July 2026, then submit to ACL/EMNLP/NAACL rolling review.  
**Rationale:** arXiv posting establishes priority and enables community feedback before formal review. The benchmark community uses arXiv extensively. Early posting also allows identification of any prior work missed in the literature review.  
**Alternatives rejected:** (a) Venue-first without arXiv — delays community visibility. (b) Wait for perfect paper before posting — premature.  
**Consequences:** Once on arXiv, the benchmark definitions are effectively frozen for the posted version. Updates require a new version number.

---

## ADR-006: Paper 2 and Paper 3 Are Not Dependencies for Paper 1

**Date:** July 2026  
**Status:** Accepted  
**Context:** Papers 2 and 3 (The Free Energy of Choice, The Entropy of Choice) are theoretically richer but empirically thinner. There was a question of whether to wait for Papers 2/3 before submitting Paper 1.  
**Decision:** Paper 1 is independent and self-contained. Papers 2/3 are referenced as companion work and future directions, not prerequisites.  
**Rationale:** Paper 1's contribution (benchmark + annotation methodology + baseline results) is independently publishable. Papers 2/3 depend on empirical results from Paper 1 to be credible. The sequence is correct: benchmark first, theory second.  
**Alternatives rejected:** (a) Merge Papers 1+2 — overloads the paper and dilutes both contributions. (b) Submit Paper 2 first — no empirical anchor.  
**Consequences:** Paper 1 must not make theoretical claims that require Papers 2/3 to justify. All speculative connections (information theory, variational inference, active inference) must be marked as future work in Paper 1.

