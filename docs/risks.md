# NSDM — Programme Risk Register

**Updated:** 2 July 2026  
**Review cadence:** Every Sunday sprint review  
**Severity:** 🔴 Critical (halt) | 🟠 High (requires immediate response) | 🟡 Medium (monitor) | 🟢 Low (log only)

---

## Active Risks

### RISK-001 — IAA Gate Failure
**Severity:** 🔴 Critical  
**Probability:** Medium (20–30%)  
**Description:** Inter-annotator agreement on `unsupported`/`under_specified` pair falls below κ = 0.45 after two annotation rounds.  
**Impact:** Sprint halt. Central novelty claim is not operationalised. Paper 1 cannot be submitted in current form.  
**Trigger:** κ < 0.45 on the critical pair after Round 2 IAA.  
**Response:** Revise label definitions and decision tree in `annotation_guide_v1.md`. Run targeted calibration on the minimal pair examples (F5-002 vs F5-004, CAL-003 vs CAL-004). Do not proceed to baselines until gate is passed.  
**Early warning:** κ < 0.50 in Round 1 should trigger immediate guide review before Round 2.  
**Owner:** Rajesh Singh

---

### RISK-002 — Prior Art Discovery
**Severity:** 🟠 High  
**Probability:** Low (5–10%)  
**Description:** A published benchmark is discovered that already captures all six NSDM labels jointly, including the `unsupported`/`under_specified` distinction.  
**Impact:** Central novelty claim collapses. Programme must pivot.  
**Trigger:** ArXiv or ACL Anthology search finds a six-class or greater benchmark that explicitly separates absence-of-chain from partial-chain.  
**Response:** If partial overlap only — reframe NSDM as extending and integrating prior work. If full overlap — halt Paper 1, pivot to Paper 2 (The Free Energy of Choice) as primary contribution, use discovered benchmark as baseline.  
**Mitigation:** Complete literature search was conducted in Session 1. No full-overlap benchmark was found. Monitoring continues.  
**Owner:** Rajesh Singh

---

### RISK-003 — Benchmark Construction Bottleneck
**Severity:** 🟡 Medium  
**Probability:** High (60%+)  
**Description:** Constructing 40+ additional high-quality examples to reach 100 examples (the minimum for a robust methodology claim) takes longer than expected due to single-annotator constraint.  
**Impact:** Paper 1 submitted with 60 examples. This is scientifically defensible (see ADR-002 framing) but may draw reviewer objection.  
**Trigger:** Less than 80 validated examples by 25 July 2026.  
**Response:** Submit Paper 1 at 60 examples, explicitly framed as a methodology paper with documented growth plan. Do not fabricate examples to reach a round number.  
**Mitigation:** Fable 5 case study provides 6 primary-source examples for free. Calibration set provides 10 more. Synthetic generation pipeline planned for August.  
**Owner:** Rajesh Singh

---

### RISK-004 — Reward-Aligned-Unjustified Annotation Reliability
**Severity:** 🟡 Medium  
**Probability:** Medium (30–40%)  
**Description:** Annotators fail to name R and C* explicitly in more than 40% of `reward_aligned_unjustified` annotations, making the label unreliable.  
**Impact:** The label must be restricted to examples with explicitly specified reward functions in the context. This reduces the label's practical applicability but does not eliminate it.  
**Trigger:** >40% of `reward_aligned_unjustified` annotations in IAA round fail to specify R and C* explicitly.  
**Response:** Restrict the label to examples where R is given in the context field. Add a guide rule: "If R is not specified in the context, do not assign `reward_aligned_unjustified` — assign `unsupported` instead."  
**Owner:** Rajesh Singh

---

### RISK-005 — Paper 1 Venue Rejection (Wrong Framing)
**Severity:** 🟡 Medium  
**Probability:** Medium (30–40% for any given venue, low overall across multiple venues)  
**Description:** NLP venues (ACL/EMNLP/NAACL) reject Paper 1 on grounds that the governance and AI safety content is out of scope.  
**Impact:** Delayed publication. Requires venue pivot.  
**Trigger:** Rejection with "out of scope" framing from first venue.  
**Response:** Pivot to *SEM, EMNLP industry track, or FAccT. Reframe introduction to lead more heavily with NLI gap and less with governance case study.  
**Mitigation:** The paper leads with NLI (Section 1.2) and positions governance examples as evaluation domains, not primary content. AbstentionBench (ACL 2025) and ContractNLI (EMNLP 2021) establish precedent for domain-specific reasoning benchmarks at NLP venues.  
**Owner:** Rajesh Singh

---

### RISK-006 — Speculative Theory Contaminating Empirical Paper
**Severity:** 🟠 High  
**Probability:** Medium (ongoing vigilance required)  
**Description:** Connections to free energy, holographic principles, Bekenstein entropy, or quantum models from Papers 2/3 contaminate Paper 1, drawing reviewer objection and damaging the benchmark paper's credibility.  
**Impact:** Rejection. Reputation risk for the programme.  
**Trigger:** Any sentence in Paper 1 that references information-theoretic, thermodynamic, or quantum connections without explicit "speculative / future work" marking.  
**Response:** Immediate edit. Paper 1 must contain zero speculative theoretical claims.  
**Mitigation:** ADR-006 mandates this separation. The reviewer objections document (Objection 5) pre-empts this.  
**Owner:** Rajesh Singh

---

### RISK-007 — South African Internet / Infrastructure Disruption
**Severity:** 🟢 Low  
**Probability:** Low but non-zero (Eskom load shedding, connectivity)  
**Description:** Power or connectivity interruptions affect research workflow.  
**Impact:** Lost work sessions.  
**Response:** All work committed to GitHub at EOD. Critical files backed up to cloud storage. Deep work sessions scheduled for morning (06:00–08:30) when load shedding risk is lowest.  
**Owner:** Rajesh Singh

---

## Closed Risks

| Risk | Closed date | Resolution |
|------|-------------|------------|
| Task-family leakage in baselines | 2 Jul 2026 | Disclosed in paper, leakage-controlled baseline added (ADR-002) |

