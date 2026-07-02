# NSDM — Task Board

**Updated:** 2 July 2026  
**Rule:** Tasks move left to right: Backlog → This Week → In Progress → Done → Blocked  
**Sprint:** Paper 1 Sprint — 3–31 July 2026  

---

## 🔴 BLOCKED

*(Empty — no blocked tasks at programme start)*

---

## 🔵 IN PROGRESS

- [ ] **Paper 1 draft v0.1** — `papers/paper1/paper1_draft_v1.md` — body at 4,800/8,000 words. Awaiting: IAA results (Section 4.3), baseline results (Appendix C), Table 1, Table 2.

---

## 🟡 THIS WEEK (3–9 July 2026)

### Day 1 — Thursday 3 July
- [ ] Self-calibration: complete `calibration_set.jsonl` test, score ≥ 8/10
- [ ] Select 30-example IAA test set from existing 60 (5 per label, 3 borderline `unsup`/`unspec`)
- [ ] Strip labels from IAA test set → `iaa_test_set_stripped.jsonl`
- [ ] Begin independent annotation of IAA test set

### Days 2–4 — Friday–Sunday 4–6 July
- [ ] Complete IAA annotation (both annotators)
- [ ] Draft non-governance `ambiguous_governance` example (medical dual-obligation)
- [ ] Add 3 new `supported` examples from public domain (legal, medical, general)

### Days 5–6 — Monday–Tuesday 7–8 July
- [ ] Run `compute_iaa.py` on IAA results
- [ ] Disagreement review session — complete `adjudication_log.md` entries
- [ ] Draft Table 1 (NSDM vs. existing benchmarks label comparison)

### Day 7 — Wednesday 9 July
- [ ] Gate decision: κ ≥ 0.50? → proceed OR revise guide
- [ ] Update `status.md` with IAA results
- [ ] Week 1 retrospective — 30 minutes max

---

## 🟢 BACKLOG (Week 2 onwards)

### Week 2 (10–16 July)
- [ ] Implement lexical baseline classifier
- [ ] Implement raw symbolic checker
- [ ] Implement structured symbolic reasoner
- [ ] Draft Table 2 (label coverage map across existing benchmarks)
- [ ] Add 5 reward_aligned_unjustified examples from public sources
- [ ] Begin Section 4 (Baselines) expansion in paper

### Week 3 (17–23 July)
- [ ] Run all 5 baselines on NSDM-Bench-0
- [ ] Produce results table for Appendix C
- [ ] Expand paper body to 7,000 words
- [ ] Add full reference list (draft)
- [ ] Add 10 examples to reach Bench-0 → 70 total

### Week 4 (24–31 July)
- [ ] Final paper draft to 8,000 words
- [ ] Abstract final version
- [ ] arXiv submission (target: 31 July 2026)
- [ ] Push repo to GitHub (public)
- [ ] Announce on NSDM website

### Future (August+)
- [ ] NSDM-Bench-0.1 — add multi-hop, temporal, OCR-noisy examples
- [ ] Reach 300 validated examples
- [ ] Begin NSDM-B (benevolence/regret/intent) label design
- [ ] Paper 2 draft: The Free Energy of Choice

---

## ✅ DONE

| Task | Completed | Output |
|------|-----------|--------|
| 12-stage research programme architecture | 2 Jul 2026 | Session 1 report |
| NSDM website | 2 Jul 2026 | `nsdm-research.html` |
| Annotation guide v1 | 2 Jul 2026 | `annotation_guide_v1.md` |
| Calibration set | 2 Jul 2026 | `calibration_set.jsonl` (10 examples) |
| IAA test protocol | 2 Jul 2026 | `iaa_test_protocol.md` |
| IAA calculator script | 2 Jul 2026 | `compute_iaa.py` |
| Fable 5 incident examples | 2 Jul 2026 | `fable5_incident_examples.jsonl` (6 examples) |
| Paper 1 draft v0.1 | 2 Jul 2026 | `paper1_draft_v1.md` |
| Reviewer objections document | 2 Jul 2026 | `paper1_reviewers_objections.md` |
| GitHub repo structure | 2 Jul 2026 | This repo |

