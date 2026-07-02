# Paper 1 — Anticipated Reviewer Objections and Responses

**Document purpose:** Pre-emptive rebuttal preparation for Paper 1.  
**Use:** Strengthen the paper before submission. Insert responses directly into the relevant sections.  
**Last updated:** 2 July 2026  

---

## Objection 1: "The `unsupported`/`under_specified` distinction is not novel — FEVER already has `NotEnoughInfo`."

**Source:** Most likely from an NLI/NLP reviewer familiar with FEVER.

**Response:**  
FEVER's `NotEnoughInfo` (NEI) collapses two structurally different states into one: (a) total absence of a justification chain and (b) partial justification chain with a specific missing premise. NSDM separates these. The difference is not terminological. It is operationally critical: the appropriate response to `unsupported` is to require a justification from scratch; the appropriate response to `under_specified` is to identify and request the specific missing premise. These are different governance actions. An AI agent that conflates them will either over-challenge fully evidenced decisions or under-challenge groundless ones. The distinction is empirically testable (Section 4.3) and falsifiable: if inter-annotator agreement on this pair fails to exceed κ = 0.45, the distinction is not operationalised and we will say so explicitly.

**Strengthen in paper:** Add Table 1 comparing NSDM labels to FEVER/NLI/AbstentionBench labels explicitly, showing what is collapsed vs. separated in each system.

---

## Objection 2: "60 examples is too small for reliable benchmark evaluation."

**Source:** Any reviewer familiar with large-scale NLI or factuality benchmarks (SNLI: 570K, MNLI: 433K, FEVER: 185K).

**Response:**  
NSDM-Bench-0 is not designed to train neural classifiers. It is designed to: (a) test whether the six-class taxonomy is coherently operationalised (IAA study); (b) evaluate whether existing systems distinguish the categories at all (baseline study); (c) serve as an anchor for the benchmark growth programme. Many seminal benchmarks began small and grew: the original BIG-Bench (Srivastava et al., 2022) was designed as a quality-first benchmark specifically in contrast to quantity-first approaches. We document the growth plan explicitly (to 300, 1,000, 10,000) and make the construction methodology replicable. The benchmark's value at 60 examples is as a rigorous conceptual validation and methodology proof, not as a statistical machine learning training resource.

**Strengthen in paper:** Add a short paragraph in Section 3 explicitly framing NSDM-Bench-0 as a methodology paper and benchmark design paper, with the growth programme as future work.

---

## Objection 3: "`reward_aligned_unjustified` is just specification gaming — Krakovna et al. (2020) already cover this."

**Source:** AI safety reviewer familiar with the specification gaming literature.

**Response:**  
Krakovna et al. (2020) provide a catalogue of specification gaming examples but do not integrate this category into a multi-class epistemic taxonomy alongside NLI-style evidence states. The novelty of NSDM's `reward_aligned_unjustified` label is not the phenomenon — it is the structural integration: by placing this label alongside `supported`, `unsupported`, `contradicted`, `under_specified`, and `ambiguous_governance`, NSDM enables a unified evaluation framework in which a single AI decision can be analysed for all six failure modes simultaneously. The Fable 5 case study (Section 5) demonstrates this value: without NSDM's taxonomy, the incident was publicly discussed as a binary governance question. With it, six distinct epistemic states are identifiable from primary sources.

**Strengthen in paper:** Add Table 2 showing which existing benchmarks cover which of the six NSDM labels, making the integration claim visible.

---

## Objection 4: "The `ambiguous_governance` label is too domain-specific to be a general epistemic category."

**Source:** NLI or ML reviewer unfamiliar with legal/governance reasoning benchmarks.

**Response:**  
Governance ambiguity — the structural conflict of simultaneously applicable rules — appears in legal reasoning (contract law, regulatory compliance), medical decision-making (conflicting clinical guidelines), organisational policy (data protection vs. audit retention), and AI safety (Constitutional AI constraints vs. reward signals). The legal NLP literature (ContractNLI, SARA, etc.) and deontic logic formalise this phenomenon as a core reasoning challenge. NSDM does not claim to solve governance reasoning — it claims that governance ambiguity is a distinct epistemic state that AI systems must recognise and flag, rather than silently resolve in favour of one rule.

**Strengthen in paper:** Add one non-governance domain example of `ambiguous_governance` (e.g., medical dual-obligation) in Section 3 or Appendix B to demonstrate generality.

---

## Objection 5: "The formal framework in Section 2 is too informal / not rigorous enough."

**Source:** Formal methods, logic, or theoretical ML reviewer.

**Response (honest):**  
The formal framework in Section 2 is intentionally kept at a level of rigour appropriate for a benchmark paper. The full mathematical formalisation — including connections to deontic logic, defeasible reasoning, and Bayesian decision theory — is developed in companion papers (Singh, 2026a: The Free Energy of Choice; Singh, 2026b: The Entropy of Choice). Section 2 provides the formalism required to make the label definitions precise and the annotation protocol reproducible. We do not claim to have solved the mathematics of justification; we claim to have made the distinctions formally precise enough to operationalise in a benchmark.

**Note:** Do not over-promise in Section 2. Mark all connections to Bayesian decision theory and information-theoretic frameworks as *speculative* or *future work* unless independently supported. The core formalism (the decision object and the evidence state taxonomy) is defensible; the theoretical connections are not yet fully established.

---

## Objection 6: "The Fable 5 case study is based on a transient news event. The labels may not be stable."

**Source:** Any reviewer concerned about case study validity.

**Response:**  
All six Fable 5 examples are grounded in primary sources: Anthropic official posts, Anthropic published research (Marks et al., 2025 on emergent misalignment), The Register, SecurityWeek, Fortune, and CNET. Each source citation is verifiable and archived. The label assignments are derived from publicly documented facts — the decision object fields (rules, evidence, proposed action) are quotes or paraphrases from these primary sources, not editorial reconstructions. The incident's transience as news does not affect the validity of the labels; the epistemic states are properties of the decision objects, not of the incident's newsworthiness. If a reviewer disputes a specific label assignment, we welcome the challenge — the annotation guide provides the decision tree required to adjudicate the dispute rigorously.

---

## Objection 7: "This is an AI safety paper, not an NLP paper. Wrong venue."

**Source:** An NLP venue reviewer who sees safety/governance content as out of scope.

**Response (venue strategy):**  
The primary venue strategy is ACL/EMNLP/NAACL for the benchmark paper, positioning it as an NLP evaluation contribution. The abstract and introduction lead with the NLI gap (Section 1.2) before introducing governance examples. The formal framework is presented in NLP-compatible notation. The Fable 5 case study is presented as a multi-domain evaluation case, not as a policy position. If a reviewer objects to the governance content as out of scope for NLP, the response is: AbstentionBench (ACL 2025), ContractNLI (EMNLP 2021), SARA (legal NLP), and FinNLI (NAACL 2025) all demonstrate that domain-specific reasoning benchmarks are within scope for NLP venues. NSDM's contribution is to the benchmark and evaluation methodology literature, not to any specific domain.

---

## What Must Be Completed Before Submission

1. IAA study with κ ≥ 0.50 on `unsupported`/`under_specified` pair (gate: 9 July 2026)
2. Baseline suite implementation and results table (target: 25 July 2026)
3. Table 1: NSDM vs. existing benchmarks label comparison
4. Table 2: which existing benchmarks cover which NSDM labels
5. One non-governance `ambiguous_governance` example added to the benchmark
6. Section 7 (Limitations) must explicitly acknowledge the 60-example size and single-annotator construction
7. All speculative theoretical connections marked clearly as future work
8. References section completed with full citations
9. Appendix C (baseline implementation details) completed after experiments

