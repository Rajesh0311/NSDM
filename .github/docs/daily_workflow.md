# NSDM — Daily Workflow Protocol

**This is the operating system for the programme.**  
**Follow it every research day. Non-negotiable blocks are marked 🔒.**

---

## Morning Protocol (06:00–08:30 SAST)

### 06:00 — Boot (5 minutes)
```
1. Open status.md — read yesterday's status and today's first task
2. Open tasks.md — confirm what is IN PROGRESS this week
3. Open terminal in VS Code: cd nsdm-repo && git pull
```

### 06:05 — Self-Calibration 🔒
```bash
python benchmark/scripts/self_calibrate.py --input benchmark/calibration_set.jsonl
```
- Score ≥ 8/10 → proceed
- Score 6–7 → reread annotation_guide_v1.md Section 3 first
- Score < 6 → annotation is prohibited today. Do paper writing or code only.

**Why this is non-negotiable:** The programme's central claim is that the `unsupported`/`under_specified` distinction is reliably operationalisable. If the lead annotator cannot apply it consistently, the claim fails. This check takes 10 minutes and costs nothing.

### 06:15 — Deep Work Block 🔒 (06:15–08:30)
- **One task only.** Pick the highest-priority item from tasks.md.
- No email, no Slack, no social media, no news.
- Sprint phase (current): Annotation or paper writing only during this block.
- Code implementation: baseline classifiers, IAA scripts.
- Do not switch tasks during this block.

**Typical outputs per session:**
- Annotation: 5–8 validated examples per 2-hour session
- Paper writing: 500–800 new words per 2-hour session
- Baseline implementation: one complete classifier per session

---

## Midday Check (13:00 — optional, 15 minutes max)

```
1. Commit morning work: git add -A && git commit -m "[date] [brief description]"
2. Update tasks.md: move any completed items to DONE
3. Check: any new papers on arXiv relevant to NSDM? (search: epistemic uncertainty NLI, reward hacking benchmark)
4. Note any blockers for tomorrow
```

---

## Evening — CrossFit 🔒 (17:00–18:30)

Non-negotiable. Hard stop on all research at 17:00. The physical session is part of the programme — sustained research requires sustained physical capacity.

---

## EOD Protocol 🔒 (20:20–20:30)

### 20:20 — Daily Commit (5 minutes)
```bash
cd nsdm-repo
git add -A
git commit -m "EOD [date]: [what was done today]"
git push origin main
```

### 20:25 — Status Update (5 minutes)
Open `docs/status.md`. Update the CURRENT STATUS block:
```
- What was completed today (checkboxes)
- What is in progress
- Next action for tomorrow morning
- Any new risks or blockers
- Paper 1 word count if writing happened
```

### 20:30 — Done. Close everything.

---

## Weekly Retrospective (Sunday, 20:00–20:30)

```
1. Review tasks.md — what was completed, what slipped, why
2. Review risks.md — any new risks, any risk severity changes
3. Update IAA tracking table in status.md
4. Check paper 1 word count against target
5. One decision: what is the single most important thing for next week?
6. Update tasks.md with next week's THIS WEEK section
7. Commit: git commit -m "Weekly retrospective [date]"
```

---

## Commit Message Convention

```
[type] [date]: [description]

Types:
  annotation: New or revised benchmark examples
  paper:      Paper draft changes
  script:     Code changes
  docs:       Documentation changes
  iaa:        IAA results or guide updates
  fix:        Bug fixes
  data:       Dataset changes

Examples:
  annotation 2026-07-03: Add 3 supported examples, medical domain
  paper 2026-07-10: Section 4 baseline results added, 6700 words total
  iaa 2026-07-09: IAA round 1 results - kappa 0.61, gate passed
  docs 2026-07-02: EOD status update
```

---

## Annotation Session Protocol (when running annotation)

```
1. Self-calibrate first (see above)
2. Open: annotation_guide_v1.md (split screen, always visible)
3. For each example:
   a. Read context, rules, history, proposed action/claim
   b. Apply the decision tree (Section 4 of guide)
   c. Apply the naming test (Section 3)
   d. Record: label, confidence, justification (2–3 sentences), missing premise (if under_specified), R+C* (if reward_aligned_unjustified)
   e. Record nearest alternative and rejection reason
4. After each 10 examples: brief break (5 minutes), no more
5. After 20 examples: stop annotation for the day — quality degrades
6. Commit annotation work immediately after session
```

---

## Paper Writing Session Protocol

```
1. Open: paper1_draft_v1.md
2. Read the last 2 paragraphs written (continuity)
3. Check today's target: which section, which gap
4. Write — no editing during the session, only drafting
5. After session: run word count, update status.md
6. Commit immediately
```

---

## Emergency Protocol (if IAA gate fails)

If `compute_iaa.py` returns κ < 0.45 on `unsupported`/`under_specified`:
```
1. Stop all annotation immediately
2. Do NOT update the benchmark with any examples from this round
3. Open annotation_guide_v1.md Section 3
4. Write 3 new minimal pair examples by hand (one `unsupported`, one `under_specified`, one borderline)
5. Run disagreement review with second annotator on ALL failed cases
6. Revise the naming test definition based on disagreement patterns
7. Update annotation_guide_v1.md — increment version to v1.1
8. Re-run calibration on new version
9. Restart IAA round with revised guide
10. Add the failure and revision to decisions.md (ADR-007)
```

---

## Programme Health Metrics (check weekly)

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Benchmark size (validated) | 60 | 60 | ✓ |
| IAA κ (unsup/unspec) | ≥ 0.50 | Pending | ⏳ |
| Paper 1 word count | 8,000 | ~4,800 | 🔄 |
| Consecutive deep work days | — | 0 (start tomorrow) | ⏳ |
| Days since last EOD commit | 0 | — | — |

