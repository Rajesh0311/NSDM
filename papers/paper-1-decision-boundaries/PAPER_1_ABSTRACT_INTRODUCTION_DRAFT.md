# Paper 1 Abstract and Introduction Draft — NSDM Decision Boundaries

## Working Title

Neuro-Symbolic Decision Boundaries: A Benchmark for Distinguishing Support, Contradiction, Under-Specification, Governance Ambiguity, and Reward-Aligned but Unjustified Action

---

## Abstract Draft

AI systems are increasingly used to support, recommend, and automate decisions. Standard evaluation often asks whether an output is correct, plausible, or aligned with a target answer. However, a decision can appear correct while still being unjustified. It may rely on missing premises, unclear authority, ambiguous governance rules, or reward-seeking behaviour that satisfies a metric while violating a higher constraint.

This paper introduces Neuro-Symbolic Decision Boundaries (NSDM), a framework and seed benchmark for evaluating whether AI decisions are justified by available evidence, rules, and governance context. We present NSDM-Bench-0, a 60-item benchmark covering supported, contradicted, under-specified, ambiguous-governance, and reward-aligned-but-unjustified decisions. We evaluate a ladder of lexical, symbolic, modular, evidence-state, zero-shot LLM, and few-shot LLM baselines.

The results show that aggregate accuracy can hide important boundary failures. A zero-shot gpt-4.1-mini baseline achieved a five-run mean accuracy of 0.703, with strong performance on conventional support and contradiction but zero mean recall on ambiguous_governance and reward_aligned_unjustified. A few-shot version improved repeated-run mean accuracy to 0.753 and improved governance ambiguity recall from 0.000 to 0.200, but reward-aligned unjustified action remained unstable, with mean recall of 0.143.

These findings suggest that decision-boundary awareness is a distinct capability not captured by ordinary correctness evaluation. NSDM reframes AI evaluation around a deeper question: not only whether the model can answer, but whether the answer or action is justified.

---

## One-Sentence Contribution

This paper introduces NSDM-Bench-0, a seed benchmark for testing whether AI systems can distinguish justified decisions from unsupported, contradicted, under-specified, governance-ambiguous, and reward-aligned-but-unjustified decisions.

---

## Introduction Draft

AI systems are moving from text generation into decision support and action. They recommend approvals, classify claims, route workflows, interpret policies, summarise evidence, draft responses, and increasingly act on behalf of users. As these systems become more capable, the central evaluation question changes.

It is no longer enough to ask:

Did the AI produce a plausible answer?

A more important question is:

Was the AI justified in producing that answer or recommending that action?

This distinction matters because many risky AI decisions are not obvious hallucinations. They may be fluent, useful, operationally efficient, or even correct under a narrow interpretation. Yet they may still be unjustified because the evidence is incomplete, a required premise is missing, the governing authority is unclear, or the system has optimised for a reward while violating a higher constraint.

For example, an automated system may close a service ticket because the user stopped replying. This may improve resolution metrics, but it may be unjustified if the governing rule requires explicit fix confirmation. A compliance assistant may recommend an escalation because a policy permits discretionary review, but the authority boundary may be opaque or ambiguous. A claims system may appear to follow evidence while ignoring a missing certification requirement. In each case, the issue is not merely whether the answer is true or false. The issue is whether the decision is justified.

This paper introduces Neuro-Symbolic Decision Boundaries (NSDM), a framework for evaluating this problem.

NSDM begins from the claim that safe and governed AI systems require decision-boundary awareness. A system should be able to distinguish:

- when a decision is supported by the available evidence and rules
- when a decision is contradicted by the available evidence or rules
- when a decision may be possible but is under-specified
- when authority, policy, or governance context is ambiguous
- when an action achieves a reward or metric but remains unjustified

These are evidence-state distinctions. They are related to factual accuracy, but they are not reducible to it.

The central hypothesis of NSDM is that many AI evaluation failures occur because models collapse these boundaries. A model may treat governance ambiguity as support. It may treat missing premises as ordinary unsupported claims. It may recognise that a rule is violated but miss the fact that the proposed action is attractive because it satisfies a reward. These boundary collapses are important because they correspond to real risks in AI deployment.

To study these distinctions, we introduce NSDM-Bench-0, a seed benchmark of decision-boundary examples. The current v0.4 batch contains 60 items across five active labels: supported, contradicted, under_specified, ambiguous_governance, and reward_aligned_unjustified. The benchmark is designed to test whether a classifier can assign the correct evidence-state label using only the allowed input context, facts, rules, and claim or action.

We evaluate a ladder of baselines, including lexical, symbolic, modular, evidence-state, zero-shot LLM, and few-shot LLM approaches. This ladder is important because it separates ordinary performance from shortcut-driven performance. One structured baseline achieved very high accuracy, but this was later identified as leakage-inflated because task-family metadata mapped too directly to target labels. The clean baselines therefore remove such shortcuts and focus on whether the decision boundary itself can be identified.

The empirical results show that overall accuracy alone is misleading. A zero-shot gpt-4.1-mini baseline achieved a five-run mean accuracy of 0.703. At first glance this appears competitive. However, label-level analysis showed perfect mean recall on supported and contradicted examples, but zero mean recall on ambiguous_governance and reward_aligned_unjustified examples. The model performed well on familiar categories while failing on the two labels most specific to NSDM.

A few-shot prompt improved performance. Baseline 009, using the same model with label demonstrations, achieved a five-run mean accuracy of 0.753. Governance ambiguity recall improved from 0.000 to 0.200, and under_specified recall improved from 0.563 to 0.691. However, reward_aligned_unjustified remained unstable, with repeated-run mean recall of 0.143. This suggests that few-shot demonstrations help but do not fully solve deeper decision-boundary recognition.

The contribution of this paper is threefold.

First, it introduces NSDM as a framework for evaluating justified AI decisions rather than only correct AI outputs.

Second, it presents NSDM-Bench-0 as a seed benchmark for testing support, contradiction, under-specification, governance ambiguity, and reward-aligned but unjustified action.

Third, it reports baseline results showing that conventional support and contradiction are easier than NSDM-specific boundary categories, and that few-shot prompting improves but does not solve these categories.

The broader implication is that decision-boundary awareness should be treated as a distinct capability for AI systems. A trustworthy AI system should not only answer. It should know whether it is justified.

---

## Paper Framing Notes

Use this paper as the foundation paper for the NSDM research line.

Keep the claims conservative:

- The benchmark is a seed benchmark, not a final universal evaluation.
- The model result is specific to gpt-4.1-mini and the tested prompt conditions.
- Baseline 009 should use repeated-run mean accuracy of 0.753 as the main result.
- The single-run 0.767 result can be reported as the best observed run.
- The unsupported label gap must be stated clearly.
- Do not claim that all LLMs fail at governance ambiguity.
- Do claim that NSDM-Bench-0 exposes boundary failures that aggregate accuracy hides.

---

## Keywords

- neuro-symbolic AI
- AI evaluation
- AI governance
- decision boundaries
- evidence-state reasoning
- under-specification
- governance ambiguity
- reward alignment
- AI safety
- justified action
