# Website Update Copy — NSDM Research Update 2026-07-07

## Page / Section Title

AI should not only answer.  
It should know whether it is justified.

---

## Short Hero Copy

NSDM is a research programme for evaluating whether AI systems can distinguish justified decisions from unsupported, contradicted, under-specified, governance-ambiguous, and reward-aligned but unjustified actions.

The goal is not only factual correctness.  
The goal is decision-boundary awareness.

---

## Main Update Headline

NSDM Research Update: Evidence-State Decision Boundaries and Repeated LLM Baselines

---

## Website Announcement Copy

We have advanced NSDM from a concept into a measurable research programme.

The latest research work includes:

- NSDM-Bench-0, a 60-item seed benchmark
- a baseline ladder across symbolic, modular, evidence-state, zero-shot LLM, and few-shot LLM approaches
- repeated LLM evaluations across five runs
- Paper 1 draft sections
- paper-ready baseline tables
- confusion matrices and failure-frontier tables
- a new NSDM-S branch for sovereign enterprise AI stack justification

The central question is:

Can an AI system tell whether a decision is justified by the available evidence, rules, and governance context?

---

## Key Finding

Aggregate accuracy can hide important decision-boundary failures.

In our current NSDM-Bench-0 results, a zero-shot gpt-4.1-mini baseline achieved a five-run mean accuracy of 0.703.

At the label level, however, it showed a sharp split:

- strong recall on ordinary support and contradiction
- zero mean recall on governance ambiguity
- zero mean recall on reward-aligned but unjustified action

A few-shot version improved five-run mean accuracy to 0.753 and improved governance ambiguity recall, but the hardest NSDM-specific labels remain difficult.

This suggests that decision-boundary awareness is a distinct capability that should be tested directly.

---

## Research Result Snapshot

| Evaluation | Mean Accuracy |
|---|---:|
| Clean modular boundary reasoner | 0.733 |
| Evidence-state reasoner v0.2 | 0.733 |
| Zero-shot LLM, gpt-4.1-mini, five-run mean | 0.703 |
| Few-shot LLM, gpt-4.1-mini, five-run mean | 0.753 |

---

## Interpretation

The results suggest that conventional support and contradiction are easier than deeper decision-boundary categories.

Governance ambiguity remains difficult because it requires the system to recognise unclear authority, discretionary policy, institutional opacity, or ambiguous approval paths.

Reward-aligned but unjustified action remains difficult because it requires the system to distinguish successful optimisation from justified action.

This matters for AI safety, governance, and enterprise deployment.

A system may satisfy a metric, close a workflow, answer a question, or recommend an action while still being unjustified.

---

## NSDM-S: Sovereign Decision Boundaries

This update also introduces the NSDM-S roadmap branch.

NSDM-S extends decision-boundary reasoning from AI outputs to enterprise AI stacks.

The applied question becomes:

Is the organisation justified in using this AI stack, exposing this data, paying this token cost, depending on this vendor, and allowing this system to influence decisions?

This connects NSDM research to applied enterprise tools such as:

- AI Stack Justification Layer
- Alpha Boundary Audit
- Token Justification Audit
- Sovereign AI Readiness Score
- Model Routing Justification
- Data Exposure Risk Classifier
- Vendor Dependency Score

---

## Short Public Claim

NSDM tests whether AI systems can distinguish justified decisions from decisions that are merely plausible, useful, or reward-aligned.

---

## Conservative Research Claim

The current NSDM-Bench-0 results suggest that evidence-state decision boundaries expose failure modes that aggregate accuracy can hide.

A capable low-cost LLM performs strongly on conventional support and contradiction, but struggles with governance ambiguity and reward-aligned unjustified action under zero-shot prompting.

Few-shot demonstrations improve overall performance, but repeated-run analysis shows that the most NSDM-specific categories remain difficult.

---

## Do Not Overclaim

Do not say:

- all LLMs fail at governance ambiguity
- NSDM-Bench-0 is complete
- the label taxonomy is final
- the current benchmark proves general model weakness
- reward-aligned unjustified action is solved by few-shot prompting

Say instead:

- this is a seed benchmark
- the result is specific to the model, benchmark, and prompt conditions tested
- the early evidence shows meaningful boundary failures
- repeated-run analysis matters
- the benchmark will expand from 60 to 100 examples

---

## Website CTA Options

### Option 1

Read the NSDM research update.

### Option 2

Explore the decision-boundary framework.

### Option 3

Follow the Paper 1 development.

### Option 4

See why AI correctness is not enough.

---

## LinkedIn / Social Short Post

AI should not only answer.

It should know whether it is justified.

We have advanced NSDM — Neuro-Symbolic Decision Boundaries — from concept into a measurable research programme.

The current internal benchmark tests whether AI systems can distinguish:

- supported decisions
- contradicted decisions
- under-specified decisions
- governance-ambiguous decisions
- reward-aligned but unjustified actions

Early repeated-run results show something important:

A capable low-cost LLM performs strongly on ordinary support and contradiction, but struggles with governance ambiguity and reward-aligned unjustified action.

Few-shot prompting improves performance, but does not fully solve the hardest boundary categories.

This is the core NSDM argument:

AI evaluation should not stop at whether the answer is plausible or correct.

We need to know whether the answer or action is justified.

---

## Homepage Small Card

### NSDM Research Update

We are building a benchmark for decision-boundary awareness: whether AI systems can tell when a decision is supported, contradicted, under-specified, governance-ambiguous, or reward-aligned but unjustified.

Latest internal results show that aggregate accuracy can hide important boundary failures.

---

## Research Page Section

### Evidence-State Decision Boundaries

NSDM-Bench-0 evaluates whether AI systems can classify the evidence state of a decision.

The benchmark asks whether a proposed claim or action is:

- supported by evidence and rules
- contradicted by evidence or rules
- missing required premises
- affected by ambiguous governance authority
- reward-aligned but unjustified

This reframes AI evaluation from answer correctness to decision justification.

---

## Release Status

Website copy: ready  
Public repo mirror: pending  
Paper 1 preprint: in progress  
Benchmark expansion: pending  
