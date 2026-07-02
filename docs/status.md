# NSDM — Daily Status

**Updated:** 2 July 2026  
**Rule:** Update this file every day at 20:20 SAST before committing.  
**Format:** Replace the CURRENT STATUS block. Archive yesterday to the log below.

---

## CURRENT STATUS — 2 July 2026

**Phase:** 1 — Benchmark Hardening & Paper 1 Sprint  
**Sprint day:** 0 (sprint starts 3 July)  
**Blocking issue:** None  
**Next action (tomorrow 06:00):** Run calibration_set.jsonl self-test. Achieve ≥ 8/10 before touching any other file.

### Completed today
- [x] Full 12-stage research programme architecture (Stages 1–12)
- [x] NSDM website built (`nsdm-research.html`) — LangChain aesthetic
- [x] Thread A: `annotation_guide_v1.md` (597 lines), `calibration_set.jsonl` (10 examples), `iaa_test_protocol.md`, `compute_iaa.py`, `adjudication_log.md`
- [x] Thread B: `fable5_incident_examples.jsonl` — 6 primary-source verified examples, one per label, all from Fable 5 incident
- [x] Thread C: `paper1_draft_v1.md` (~4,800 words, 8 sections structured), `paper1_reviewers_objections.md` (7 objections + responses)
- [x] Thread D: Full GitHub repo structure, README, status.md, tasks.md, decisions.md, risks.md, workflow scripts

### Active risks today
- IAA gate not yet run — programme novelty claim is provisional until κ ≥ 0.50 confirmed
- Benchmark size at 60 examples — insufficient for statistical claims but sufficient for methodology paper

### Paper 1 word count
- Body: ~4,800 / 8,000 target
- Sections needing expansion: Section 4 (baseline results), Appendix C, Table 1, Table 2

---

## Status Log

| Date | Phase | Key event | Sprint day |
|------|-------|-----------|------------|
| 2 Jul 2026 | 1 | Programme launch. All 4 threads completed. | 0 |

---

## IAA Tracking

| Round | Date | Annotator 1 | Annotator 2 | Overall κ | unsup/unspec κ | Gate |
|-------|------|-------------|-------------|-----------|----------------|------|
| 1 | TBD | — | — | — | — | Pending |

