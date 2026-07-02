# NSDM — Neuro-Symbolic Decision Boundaries

**Research Programme:** NSDM — Neuro-Symbolic Decision Boundaries  
**Lead:** Rajesh Singh, MetaForgeX AI  
**Location:** Johannesburg, South Africa  
**Programme start:** 2 July 2026  
**Current phase:** Phase 1 — Benchmark Hardening & Paper 1 Sprint  
**Sprint end:** 31 July 2026  

---

## What This Is

NSDM is a research programme developing a rigorous science of justified AI decision-making.

**Central research question:**  
How can AI systems formally distinguish between decisions that are supported, unsupported, contradicted, under-specified, governance-ambiguous, or reward-aligned but unjustified — before they answer or act?

**Core claim:**  
Modern AI systems fail not only because they answer incorrectly, but because they collapse distinct epistemic and decision states into one output. NSDM proposes a benchmark and formal evidence-state framework for separating these states.

---

## Repository Structure

```
nsdm/
├── benchmark/                  # NSDM-Bench-0 and future versions
│   ├── annotation_guide_v1.md  # Authoritative annotation protocol
│   ├── calibration_set.jsonl   # 10 calibration examples with rationales
│   ├── compute_iaa.py          # IAA calculator (Cohen's kappa)
│   ├── iaa_test_protocol.md    # Week 1 IAA test procedure
│   ├── adjudication_log.md     # Disagreement ledger
│   ├── examples/               # Validated benchmark examples
│   │   ├── fable5_incident_examples.jsonl   # 6 primary-source examples
│   │   └── fable5_incident_README.md
│   ├── scripts/                # Annotation pipeline scripts
│   └── splits/                 # Train/dev/test splits (after IAA gate)
├── papers/
│   ├── paper1/                 # NSDM Decision Boundaries benchmark paper
│   │   ├── paper1_draft_v1.md
│   │   └── paper1_reviewers_objections.md
│   ├── paper2/                 # The Free Energy of Choice
│   └── paper3/                 # The Entropy of Choice
├── tools/                      # Evidence-state classifier, RAG checker, etc.
├── website/                    # nsdm.co.za / nsdm-research.html
├── data/
│   ├── raw/                    # Original collected examples pre-annotation
│   ├── processed/              # Validated, labelled JSONL
│   └── synthetic/              # Synthetically generated + human reviewed
└── docs/                       # Programme documentation
    ├── status.md               # Daily status (update every EOD)
    ├── tasks.md                # Active task board
    ├── decisions.md            # Architectural decisions log
    └── risks.md                # Programme risk register
```

---

## The Six Labels

| Label | Definition |
|-------|------------|
| `supported` | Justification chain from evidence + rules to claim is complete and undefeated |
| `unsupported` | No justification chain can be initiated — the claim is groundless |
| `contradicted` | Available evidence actively falsifies the claim under the operative criteria |
| `under_specified` | Partial chain exists but a specific, nameable missing premise breaks it |
| `ambiguous_governance` | Two applicable rules structurally conflict — no fact resolves it, only a rule change |
| `reward_aligned_unjustified` | Action achieves reward R but violates implicit constraint C* not represented in R |

**The critical distinction:** `unsupported` ≠ `under_specified`. This is the programme's central novelty claim.

---

## Current Sprint: Paper 1

**Target:** Submit Paper 1 to arXiv by 31 July 2026  
**Gate (Week 1):** IAA κ ≥ 0.50 on `unsupported`/`under_specified` pair  

| Week | Milestone |
|------|-----------|
| Week 1 (3–9 Jul) | IAA test — κ gate |
| Week 2 (10–16 Jul) | Baseline implementation |
| Week 3 (17–23 Jul) | Results tables + Section 4 |
| Week 4 (24–31 Jul) | Final draft + arXiv submission |

---

## Quick Start (Windows / VS Code)

```bash
# Clone
git clone https://github.com/[your-handle]/nsdm.git
cd nsdm

# Python environment
python -m venv .venv
.venv\Scripts\activate       # Windows
pip install -r requirements.txt

# Run calibration self-test
python benchmark/scripts/self_calibrate.py --input benchmark/calibration_set.jsonl

# Run IAA calculator (after annotation round)
python benchmark/compute_iaa.py --input benchmark/iaa_results.jsonl
```

---

## Falsification Criteria

The programme halts or pivots if:
- IAA κ on `unsupported`/`under_specified` < 0.45 after two annotation rounds
- No venue accepts Paper 1 after two revision cycles AND the central distinction cannot be defended at κ ≥ 0.50
- A published benchmark is found that already captures all six labels jointly

---

## Licence

- Benchmark data: CC BY 4.0 (open, attribution required)
- Code: MIT
- Papers: author copyright, arXiv preprint open access

