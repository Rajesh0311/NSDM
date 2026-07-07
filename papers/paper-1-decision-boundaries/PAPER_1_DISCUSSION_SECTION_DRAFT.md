# Paper 1 Discussion Section Draft — NSDM Decision Boundaries

## Purpose

This document drafts the Discussion section for Paper 1.

Paper 1 working title:

Neuro-Symbolic Decision Boundaries: A Benchmark for Distinguishing Support, Contradiction, Under-Specification, Governance Ambiguity, and Reward-Aligned but Unjustified Action

The Discussion interprets the current NSDM-Bench-0 v0.4 batch 1 results and explains why the findings matter for AI safety, governance, decision automation, and enterprise AI deployment.

---

## Core Discussion Claim

NSDM-Bench-0 shows that AI decision evaluation cannot stop at whether a model output appears correct.

A decision may be factually plausible while still being unjustified because:

- required premises are missing
- authority is unclear
- governance rules are ambiguous
- a reward or metric is satisfied while a higher constraint is violated
- the system has collapsed justification into outcome success

The benchmark therefore evaluates a deeper question:

Is this decision justified by the available evidence, rules, and governance context?

---

## Why Overall Accuracy Is Not Enough

The Baseline 008 and Baseline 009 results show why aggregate accuracy can hide important boundary failures.

Baseline 008 achieved a five-run zero-shot mean accuracy of 0.703 using gpt-4.1-mini. At the aggregate level, this appears competitive with clean symbolic and modular baselines.

However, the per-label results reveal a sharper problem:

- supported mean recall: 1.000
- contradicted mean recall: 1.000
- ambiguous_governance mean recall: 0.000
- reward_aligned_unjustified mean recall: 0.000

This means the model can appear competent on ordinary support and contradiction while failing completely on the two most NSDM-specific categories.

The result supports the central NSDM argument:

A system can perform well on conventional correctness tests while remaining weak at recognising unjustified decisions.

---

## Boundary Failure Is Not Random Error

The errors are not simply random misclassifications.

They form meaningful boundary collapses.

Baseline 009 improves overall performance to 0.767, but the confusion matrix shows persistent patterns:

- ambiguous_governance is misclassified as supported or under_specified
- reward_aligned_unjustified is misclassified as contradicted
- under_specified is misclassified as unsupported

These are not trivial mistakes. Each collapse reflects a different failure to preserve a decision boundary.

---

## Governance Ambiguity Is a Distinct Failure Mode

Governance ambiguity remains the hardest category.

In Baseline 009:

- ambiguous_governance support: 6
- correct: 1
- recall: 0.167

The remaining ambiguous_governance examples were classified as:

- supported: 2
- under_specified: 3

This shows two common failure modes.

First, the model may treat discretionary or unclear authority as sufficient support. If a rule says an official may decide, request, assess, or escalate, the model may infer that the action is supported without recognising the governance ambiguity.

Second, the model may treat opaque authority as ordinary missing information. This collapses ambiguous_governance into under_specified.

The distinction matters.

Under-specification asks:

What factual premise is missing?

Governance ambiguity asks:

Who has the authority, under what rule, with what constraint, and how is that authority interpreted?

A model that collapses governance ambiguity into under-specification may request more facts when the real problem is institutional authority or policy opacity.

---

## Reward-Aligned but Unjustified Action Is Partly Learnable

Baseline 008 failed completely on reward_aligned_unjustified.

Baseline 009 improved reward_aligned_unjustified recall to 0.429.

This is the largest NSDM-specific improvement from few-shot prompting.

The result suggests that reward-aligned but unjustified action is partly teachable through explicit label demonstrations.

However, four of seven reward_aligned_unjustified examples were still classified as contradicted.

This is an important boundary collapse.

Contradiction means that the available evidence directly conflicts with the claim or action.

Reward-aligned unjustified action means the action may be attractive because it satisfies a reward, target, user preference, workflow metric, or optimisation goal, but it is still not justified by the governing evidence or higher constraint.

The model recognises the rule violation, but often misses the reward-alignment structure.

That structure is central to AI safety and agentic systems.

Many harmful automated decisions will not look like arbitrary errors. They will look like successful optimisation against the wrong justification boundary.

---

## The Unsupported Versus Under-Specified Gap

The current benchmark has an important limitation: the 60-item version has no true unsupported examples.

Even so, Baseline 009 predicted unsupported for four under_specified examples.

This reveals a useful boundary issue but also a dataset gap.

Unsupported means:

There is no sufficient evidence or justification.

Under_specified means:

The claim or action may be justified, but a required premise is missing.

This distinction matters because the correct system behaviour differs.

For unsupported decisions, the system should reject or refuse.

For under-specified decisions, the system should ask for the missing premise.

The benchmark expansion to 100 examples must add true unsupported cases so that this boundary can be tested properly.

---

## Few-Shot Prompting Helps but Does Not Solve the Problem

Baseline 009 improves over Baseline 008:

- accuracy improves from 0.703 zero-shot mean to 0.767
- ambiguous_governance recall improves from 0.000 to 0.167
- reward_aligned_unjustified recall improves from 0.000 to 0.429
- under_specified recall improves from 0.563 to 0.636

This is encouraging.

It means that NSDM-specific boundaries are not invisible to language models. Explicit label definitions and demonstrations help.

But the remaining failure pattern shows that prompting alone is not sufficient.

Governance ambiguity remains weak. Reward-aligned unjustified action is still often collapsed into contradiction. Under-specification is still confused with unsupported.

The likely implication is that robust NSDM performance may require more than prompt wording.

Future systems may need:

- explicit evidence-state representations
- governance-rule modelling
- authority-chain checks
- missing-premise detection
- reward-versus-justification separation
- contradiction detection as one component, not the whole evaluator
- structured intermediate reasoning
- audit logs showing why a decision was considered justified or unjustified

---

## Why Neuro-Symbolic Framing Matters

The results support the neuro-symbolic framing of NSDM.

Pure symbolic systems can preserve explicit rules and boundary logic, but may be brittle when evidence is noisy, contextual, or semantically varied.

Pure language-model approaches can interpret context flexibly, but may collapse institutional, evidential, and optimisation boundaries into familiar natural-language categories.

NSDM sits between these approaches.

The goal is not merely to classify text.

The goal is to produce systems that can reason over:

- evidence
- rules
- missing premises
- contradictions
- authority
- incentives
- reward pressure
- governance opacity
- justified action

This requires both semantic interpretation and symbolic boundary discipline.

---

## Implications for AI Safety

NSDM is relevant to AI safety because many unsafe AI actions are not simple hallucinations.

A system may produce an action that is:

- locally useful
- reward-maximising
- user-satisfying
- procedurally convenient
- commercially attractive
- operationally efficient

but still unjustified.

The reward_aligned_unjustified label is designed to capture this class of failure.

This is especially relevant for agentic AI systems that optimise goals, route workflows, close tickets, approve claims, escalate decisions, recommend interventions, or act on behalf of users.

The question is not only:

Did the AI get the answer right?

The question is:

Was the AI justified in taking or recommending that action?

---

## Implications for AI Governance

The ambiguous_governance label is relevant to AI governance because many real-world decisions depend on unclear authority.

In organisations, rules are often discretionary, incomplete, conflicting, or embedded in tacit practice.

AI systems deployed into these environments may treat authority as clear when it is not.

This creates risk in:

- compliance workflows
- procurement decisions
- insurance and claims processing
- HR decisions
- public-sector eligibility decisions
- enterprise approvals
- legal and policy interpretation
- financial controls
- healthcare operations
- customer service escalation

A governance-aware AI system must be able to say:

The facts may be present, but the authority boundary is unclear.

This is different from saying:

More facts are needed.

---

## Implications for Enterprise AI and NSDM-S

The results also motivate the NSDM-S branch: Sovereign Decision Boundaries.

The same logic that applies to model outputs also applies to enterprise AI stacks.

A company should not only ask whether an AI output is correct.

It should also ask whether the AI stack is justified.

This includes:

- data exposure
- vendor dependence
- token economics
- infrastructure control
- model routing
- memory and logging
- auditability
- governance authority
- reproducibility
- strategic alpha preservation

The NSDM-S extension reframes enterprise AI deployment as a justification problem.

The applied question becomes:

Is the organisation justified in using this AI stack, exposing this data, paying this token cost, depending on this vendor, and allowing this system to influence decisions?

This creates a bridge between NSDM research and applied products such as:

- AI Cost Optimizer
- Token Justification Audit
- Alpha Boundary Audit
- Sovereign AI Readiness Score
- Model Routing Justification
- Data Exposure Risk Classifier
- Vendor Dependency Score
- AI Stack Justification Layer

---

## What the Current Results Do Not Prove

The current results should be interpreted carefully.

They do not prove that all LLMs fail on governance ambiguity or reward-aligned unjustified action.

They do not prove that gpt-4.1-mini cannot solve these labels under stronger prompting, more examples, fine-tuning, retrieval, or tool use.

They do not prove that the current benchmark is complete.

They do not prove that the label taxonomy is final.

The current benchmark is a seed benchmark.

The results are best understood as evidence that these decision-boundary labels expose meaningful failure modes under controlled prompt conditions.

---

## Main Limitations

### 1. Small Benchmark Size

NSDM-Bench-0 v0.4 batch 1 contains 60 examples.

This is sufficient for seed testing and baseline development, but not enough for broad generalisation.

### 2. Unsupported Label Gap

The current 60-item benchmark has no true unsupported examples.

This must be corrected in the 100-example expansion.

### 3. Single Few-Shot Run

Baseline 009 is currently a single full run.

Baseline 008 showed that repeated LLM runs can vary, so Baseline 009 should ideally be repeated before final publication.

### 4. Single LLM Family

The current LLM tests use gpt-4.1-mini.

Future work should compare multiple model families and sizes.

### 5. Demonstration Selection Risk

Few-shot prompting may improve results through surface imitation rather than true boundary reasoning.

Future work should use held-out demonstrations, multiple prompt variants, and repeated-run evaluation.

### 6. Synthetic or Semi-Synthetic Benchmark Risk

If benchmark examples are synthetic or semi-synthetic, they may not fully represent the messiness of real institutional decision-making.

Future work should include real-world anonymised decision traces where possible.

---

## Future Work

Immediate future work:

1. Repeat Baseline 009 across five runs.
2. Expand NSDM-Bench-0 from 60 to 100 examples.
3. Add true unsupported examples.
4. Add more governance ambiguity examples.
5. Add more reward-aligned unjustified examples.
6. Create the dataset card.
7. Add inter-annotator agreement workflow.
8. Test additional LLMs.
9. Test retrieval-augmented and structured-reasoning variants.
10. Add NSDM-S applied stack-justification examples.

Longer-term future work:

1. Build a neuro-symbolic boundary evaluator.
2. Build a governance ambiguity detector.
3. Build a reward-versus-justification classifier.
4. Connect NSDM to AI audit workflows.
5. Connect NSDM to enterprise AI cost and stack governance.
6. Develop NSDM-B for benevolent and regret-sensitive decision boundaries.
7. Develop NSDM-S for sovereign and alpha-preserving AI stack decisions.

---

## Discussion Conclusion

The current results support the core NSDM thesis.

AI systems should not only be evaluated on whether they produce plausible or correct outputs.

They should be evaluated on whether their outputs and actions are justified by the available evidence, rules, and governance context.

NSDM-Bench-0 shows that conventional support and contradiction can be easier than deeper decision-boundary categories.

Zero-shot LLM evaluation performs well on familiar categories but fails on governance ambiguity and reward-aligned but unjustified action.

Few-shot prompting improves these categories, but does not fully solve them.

This suggests that future reliable AI systems will need explicit decision-boundary awareness.

The practical aim is an AI system that can say:

I can answer.

I cannot answer.

This action is contradicted.

This action may be possible, but a premise is missing.

This action appears useful, but it is not justified.

This action depends on unclear authority.

That ability is central to trustworthy AI decision-making.

---

## Paper-Ready Discussion Claim

Safe version:

The current NSDM-Bench-0 results suggest that evidence-state decision boundaries expose failure modes that are not visible in aggregate accuracy alone. In particular, gpt-4.1-mini performs strongly on conventional support and contradiction, but struggles with governance ambiguity and reward-aligned but unjustified action under zero-shot prompting. Few-shot demonstrations improve these labels, but do not fully solve them.

Stronger version for later, only after more evidence:

Decision-boundary awareness should be treated as a distinct capability for safe and governed AI systems.

---

## Baseline 009 Repeated-Run Discussion Update

The repeated Baseline 009 result moderates the initial interpretation.

The initial single Baseline 009 run suggested a strong improvement on reward_aligned_unjustified, with recall moving from 0.000 in Baseline 008 zero-shot runs to 0.429 in the few-shot condition.

The five-run repeat evaluation shows a more conservative pattern:

- Baseline 009 mean accuracy: 0.753
- Baseline 009 mean ambiguous_governance recall: 0.200
- Baseline 009 mean reward_aligned_unjustified recall: 0.143
- Baseline 009 mean under_specified recall: 0.691

This confirms that few-shot prompting helps, but it does not reliably solve the NSDM-specific labels.

The strongest stable finding is that few-shot prompting improves overall evidence-state classification and improves governance ambiguity recognition from zero to a non-zero mean recall. The reward_aligned_unjustified label remains difficult and unstable.

This is scientifically useful. It suggests that reward-aligned unjustified action may require more than label definitions and a small number of examples. Future systems may need explicit reward-versus-justification decomposition, rather than relying only on prompt demonstrations.

The revised Paper 1 claim should therefore be:

Few-shot demonstrations improve NSDM-Bench-0 performance over zero-shot prompting, but repeated-run analysis shows that the most NSDM-specific categories remain difficult. Governance ambiguity improves but remains low, while reward-aligned unjustified action remains unstable across runs.

