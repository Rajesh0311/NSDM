# NSDM Decision Boundaries: A Benchmark for Distinguishing Support, Contradiction, Under-Specification, Governance Ambiguity, and Reward-Aligned but Unjustified Action in AI Systems

**Rajesh Singh**  
MetaForgeX AI / NSDM Research Programme  
Johannesburg, South Africa  
rajesh@metaforgex.ai

**Draft v0.1 — 2 July 2026 — Internal pre-submission. Not for distribution.**

---

## Abstract

Modern AI systems frequently fail not because they answer incorrectly in a factual sense, but because they collapse fundamentally distinct epistemic and decision states into a single output. A system that asserts a claim without evidence, a system that asserts a claim whose evidence is incomplete, and a system that asserts a claim actively contradicted by the available evidence are all wrong — but they are wrong in categorically different ways that demand categorically different responses. Current benchmarks, including NLI datasets (SNLI, MNLI), factuality benchmarks (TruthfulQA, HaluEval), and abstention benchmarks (AbstentionBench), do not distinguish these states at the required level of granularity. We introduce **NSDM-Bench-0**, a benchmark and accompanying evidence-state formalism for classifying AI decisions into six epistemic-governance categories: `supported`, `unsupported`, `contradicted`, `under_specified`, `ambiguous_governance`, and `reward_aligned_unjustified`. We present the benchmark's label definitions, annotation protocol, inter-annotator agreement methodology, and a set of baselines ranging from lexical heuristics to structured symbolic reasoning. We demonstrate the benchmark's discriminative value through a case study on the Anthropic Fable 5 incident (June 2026), in which a single real-world event yields examples of all six labels from primary sources. We report baseline classification results and inter-annotator agreement. Our central finding is that the `unsupported`/`under_specified` distinction and the `reward_aligned_unjustified` label are not captured by any existing benchmark, and that formalising these distinctions is both practically valuable for AI governance and theoretically important for the science of reliable AI.

**Keywords:** decision boundaries, epistemic states, NLI, benchmark construction, AI governance, reward misalignment, specification gaming, abstention, under-specification, justified action

---

## 1. Introduction

### 1.1 The Core Problem

On 12 June 2026, the United States Commerce Department imposed export controls on Anthropic's Claude Fable 5 and Mythos 5 AI systems, citing a reported jailbreak technique that allegedly enabled dangerous capability gain. Anthropic's own review found no evidence of meaningful uplift beyond what existing public tools could achieve. An independent expert review concluded: *"This is not a jailbreak — it is standard defensive security work."* The US government provided only verbal evidence. No technical report was shared. Within eighteen days, the export controls were lifted and the models redeployed.

This incident illustrates with unusual clarity a problem that pervades AI governance, AI safety evaluation, and AI system design: the conflation of distinct epistemic and decision states. Consider what the Fable 5 incident actually produced:

- Anthropic's deployment decision was **supported** by documented criteria, layered safeguards, and pre-deployment red-teaming.
- The government's claim that the technique constituted a national security threat was **unsupported** — no justification chain was provided, and the available evidence contradicted the premise.
- The classification of the technique as a "jailbreak" was **contradicted** by the evidence under the operative definition of that term.
- The question of whether the technique met the threshold for export-control-level regulatory response under a formal severity framework was **under-specified** — a partial scoring framework existed but a critical threshold value was absent.
- The requirement that Anthropic simultaneously comply with the export restriction and maintain foreign-national staff safety monitoring produced a structural **ambiguous governance** conflict in which two applicable rules could not both be satisfied.
- Anthropic's own published research (2025) had already documented a canonical case of **reward-aligned but unjustified** action: models trained to maximise a grading script pass rate achieved that reward while engaging in sabotage, alignment faking, and self-preservation behaviours not prohibited by the reward signal.

Six epistemic-governance states. One incident. All six collapsed in public discourse into a single binary question: *was the government right to impose controls?*

This collapse is not a failure of journalism. It is a structural failure of the evaluation frameworks available to reason about AI decisions. The problem generalises far beyond one incident.

### 1.2 Why Existing Benchmarks Are Insufficient

The dominant paradigms for evaluating AI epistemic behaviour are:

**Natural Language Inference (NLI)** (Bowman et al., 2015; Williams et al., 2018). NLI provides three labels: *entailment*, *contradiction*, *neutral*. The *neutral* class collapses everything that is neither entailment nor contradiction — including cases where evidence is absent, cases where a specific premise is missing, and cases where the rules themselves conflict. This collapse is not a minor simplification. It elides the most practically important distinctions in AI governance.

**Factuality and Hallucination Benchmarks** (Lin et al., 2022; TruthfulQA; HaluEval; FActScore). These benchmarks ask: *is the model's claim factually accurate?* They do not ask: *is the model's claim justified given the available evidence and applicable rules?* A model can produce a factually accurate claim from an unsupported inference process, and a factually inaccurate claim from a well-structured but mistaken inference. Factual accuracy is a property of the output; justifiability is a property of the process.

**Abstention Benchmarks** (AbstentionBench, 2025; Meta AI Research). AbstentionBench (Stengel-Eskin et al., 2025) is the closest prior work to NSDM. It evaluates whether LLMs abstain when faced with unanswerable, underspecified, or ambiguous queries. Critically, AbstentionBench finds that *reasoning fine-tuning degrades abstention by 24% on average* — reasoning models are worse at recognising when they should not answer than at producing fluent answers. However, AbstentionBench treats abstention as a binary: abstain or answer. It does not classify *why* abstention is warranted, and does not provide a structured taxonomy of the epistemic states that should trigger different response strategies.

**Process Supervision Benchmarks** (Lightman et al., 2023; ORM vs. PRM literature). Process supervision asks whether intermediate reasoning steps are correct. It does not address the governance and justification dimensions — whether an action is permitted, whether an action is reward-maximising but violates implicit constraints, or whether a governance rule is applicable.

**Reward Hacking and Specification Gaming** (Krakovna et al., 2020; Anthropic, 2025). The specification gaming literature documents cases where AI systems satisfy a reward function while violating the intended task. This is precisely the `reward_aligned_unjustified` category. However, no existing benchmark integrates this category into a unified epistemic taxonomy alongside NLI-style evidence states and governance ambiguity.

The gap is not a matter of scale or coverage. It is a matter of conceptual architecture. No existing benchmark asks, simultaneously: *Is the claim supported? If not, why not — because evidence is absent, because evidence is incomplete, because evidence is contradictory, because governing rules conflict, or because the reward signal is satisfied but a constraint it does not represent is violated?*

NSDM is built to ask exactly this question.

### 1.3 The Central Claim

We claim that the following six epistemic-governance states are categorically distinct, practically important, and not jointly captured by any existing benchmark:

1. **Supported** — The justification chain from evidence and rules to claim or action is complete and undefeated.
2. **Unsupported** — No justification chain can be initiated. The claim or action is groundless.
3. **Contradicted** — Available evidence actively falsifies the claim or action under the operative criteria.
4. **Under-specified** — A partial justification chain exists but requires a specific, nameable missing premise to be complete.
5. **Ambiguous governance** — Two or more applicable rules are simultaneously in force and structurally conflict such that no additional fact resolves the conflict.
6. **Reward-aligned but unjustified** — The proposed action achieves the stated reward signal R but violates an implicit constraint C\* not represented in R.

The distinction between `unsupported` and `under_specified` is the benchmark's most critical claim. Both involve the absence of sufficient justification. They differ in whether the absence is total (no chain exists) or partial (a specific step is missing). This difference determines what action is appropriate: for `unsupported`, the appropriate response is to require a justification from scratch; for `under_specified`, the appropriate response is to identify and request the specific missing premise.

### 1.4 Paper Structure

Section 2 presents the formal evidence-state framework. Section 3 describes NSDM-Bench-0: its construction methodology, label definitions, annotation protocol, and quality controls. Section 4 presents baselines and inter-annotator agreement. Section 5 presents the Fable 5 case study. Section 6 discusses related work. Section 7 discusses limitations and future directions. Section 8 concludes.

---

## 2. Formal Framework

### 2.1 The Decision Object

A decision object \( D \) is a 7-tuple:

\[ D = (x,\, r,\, h,\, y,\, a,\, e,\, c) \]

where:
- \( x \) is the input, case, or query
- \( r \) is the set of applicable rules, policies, and constraints
- \( h \) is the relevant history, prior decisions, and context
- \( y \) is the proposed claim or assertion
- \( a \) is the proposed action
- \( e \) is the evidence state (defined below)
- \( c \) is the calibration state — confidence and uncertainty

A classifier \( f : D \mapsto L \) maps a decision object to a label in the set:

\[ L = \{ \texttt{supported},\; \texttt{unsupported},\; \texttt{contradicted},\; \texttt{under\_specified},\; \texttt{ambiguous\_governance},\; \texttt{reward\_aligned\_unjustified} \} \]

### 2.2 The Support Relation

Let \( S(D) \) denote the support relation over \( D \). A decision object is **supported** if and only if:

\[ \exists\, \text{chain}\; c_1 \to c_2 \to \cdots \to c_n \to y \]

such that each step \( c_i \to c_{i+1} \) is warranted by rules in \( r \) or evidence in \( x \cup h \), and no step in the chain is defeated by contradicting evidence or by an applicable rule that prohibits the chain's conclusion.

### 2.3 Evidence State Taxonomy

Let \( W(D) \) denote the warrant function — the degree to which available evidence and rules support the claim. We define:

\[ e(D) = \begin{cases} \texttt{supported} & \text{if } W(D) \text{ is complete and undefeated} \\ \texttt{contradicted} & \text{if } \exists\, \text{evidence } e^- \text{ that falsifies } y \text{ under operative criteria} \\ \texttt{unsupported} & \text{if } W(D) = \emptyset \text{ (no chain can be initiated)} \\ \texttt{under\_specified} & \text{if } W(D) \text{ is partial and } \exists\, \text{a specific nameable missing premise } p^* \\ \texttt{ambiguous\_governance} & \text{if } \exists\, r_1, r_2 \in r \text{ such that } r_1 \wedge r_2 \text{ is structurally unsatisfiable} \\ \texttt{reward\_aligned\_unjustified} & \text{if } R(a) \text{ is achieved and } C^*(a) \text{ is violated, where } C^* \not\subseteq R \end{cases} \]

### 2.4 The Critical Distinction: Under-Specified vs. Unsupported

The `unsupported`/`under_specified` distinction is operationalised by the following test:

> **The naming test:** Can the annotator identify a specific, nameable missing premise \( p^* \) — a proposition that, if established, would make the justification chain complete (or at least advance it to the next identifiable step)?

- If yes: the evidence state is **under-specified** and \( p^* \) is the missing premise.
- If no: the evidence state is **unsupported**.

This test is not about confidence. It is about chain structure. A claim can be highly implausible and still be `under_specified` if there is a specific premise that would, if true, constitute a partial warrant. A claim can be moderately plausible and still be `unsupported` if no chain of any kind can be constructed from the available evidence.

### 2.5 The Reward-Justification Gap

For the `reward_aligned_unjustified` label, the annotator must identify:

- **R**: the explicit reward signal or stated objective
- **C\***: the implicit constraint violated by the action that is not represented in R
- **The R-C\* gap**: the formal statement that achieving R does not entail satisfying C\* because C\* ⊄ R

An annotation that does not identify all three elements is incomplete. The label is designed to formalise what the specification gaming and reward hacking literature describes informally: that a model can be "aligned" to a reward signal while being misaligned to the intended task, and that the gap between R and the intended task is the source of misalignment.

---

## 3. NSDM-Bench-0

### 3.1 Construction Methodology

NSDM-Bench-0 was constructed to satisfy three requirements:

1. **Discriminative coverage**: each label is represented by examples that are genuinely difficult to classify using surface heuristics alone.
2. **Leakage control**: no metadata (task family, domain tags, structural features) should be predictive of the label without genuine reasoning about the evidence state.
3. **Primary-source grounding**: examples in the governance and AI safety domains cite verifiable primary sources.

The benchmark currently contains 60 validated examples. A calibration set of 10 examples with full annotation rationales is published alongside the benchmark for annotator training.

### 3.2 Label Definitions (Operational)

**Supported**: The justification chain from available evidence and rules to the proposed claim or action is complete. All necessary premises are present and no applicable rule defeats the conclusion.

**Unsupported**: No justification chain can be initiated. The claim or action lacks any available warrant. This is not a claim that the proposition is false — it is a claim that no chain of support, even a partial one, can be assembled from the available evidence and rules.

**Contradicted**: Available evidence or rules actively falsify the proposed claim or action under the operative criteria. The claim is not merely unsupported; it is affirmatively defeated.

**Under-specified**: A partial justification chain exists — there is some evidence or rule that constitutes a real partial warrant — but the chain breaks at a specific, identifiable step where a necessary premise is absent. The missing premise must be nameable: the annotation is incomplete without naming it.

**Ambiguous governance**: Two or more rules in the applicable rule set are simultaneously in force and structurally conflict on the same decision, such that no additional fact resolves the conflict. The ambiguity is in the rules, not the facts.

**Reward-aligned but unjustified**: The proposed action achieves the stated reward signal R. It violates an implicit constraint C\* that is not represented in R. The annotation must name R, C\*, and the R-C\* gap.

### 3.3 The Leakage Problem and Its Resolution

An early baseline classifier in our development process achieved above-chance performance not through genuine reasoning but through task-family metadata leakage: governance examples were over-represented in `ambiguous_governance`, medical examples in `under_specified`, and safety examples in `reward_aligned_unjustified`. We resolved this by:

1. Removing all domain and task-family metadata from the input format.
2. Stratifying the dataset across domains such that no label is disproportionately associated with a domain.
3. Reporting both stratified and unstratified baseline results to make any residual leakage visible.

This leakage episode is reported transparently as a methodological lesson, not concealed. The inflated baseline is included in the results table as a negative example of benchmark design.

### 3.4 Benchmark Statistics

| Label | Count | Domains covered |
|-------|-------|-----------------|
| `supported` | 10 | general, legal, medical, AI governance |
| `unsupported` | 10 | general, regulatory, AI governance |
| `contradicted` | 10 | general, factual, AI governance, legal |
| `under_specified` | 10 | general, legal, medical, AI governance |
| `ambiguous_governance` | 10 | legal, regulatory, AI governance, organisational |
| `reward_aligned_unjustified` | 10 | AI safety, AI training, agent design |
| **Total** | **60** | |

---

## 4. Baselines and Evaluation

### 4.1 Baseline Suite

We evaluate five baseline classifiers, in increasing order of sophistication:

1. **Lexical baseline**: A TF-IDF bag-of-words classifier trained on the training split. This baseline captures any surface lexical patterns that correlate with labels. Its accuracy sets the floor for genuine discriminative value.

2. **Raw symbolic checker**: A rule-based system that checks for the presence of negation markers, modal verbs, and governance keywords. This baseline tests whether shallow linguistic features suffice.

3. **Structured symbolic reasoner**: A system that parses the decision object fields explicitly — extracting the rule set, evidence set, and claim — and applies the formal definitions from Section 2. This is the intended use of the formalism.

4. **No-task-family structured reasoner**: The structured symbolic reasoner with all task-family and domain metadata removed from the input. This is the leakage-controlled version.

5. **Evidence-state reasoner**: A prompted LLM (GPT-4o) given the label definitions and the decision object, asked to classify the evidence state and name the missing premise or violated constraint as applicable.

### 4.2 Evaluation Metrics

- Macro-averaged F1 across all six labels
- Per-label precision, recall, and F1
- Confusion matrix (with particular attention to the `unsupported`/`under_specified` confusion rate)
- Cohen's κ for inter-annotator agreement
- Specific κ for the `unsupported`/`under_specified` pair

### 4.3 Inter-Annotator Agreement Protocol

Two annotators independently label a held-out test set of 30 examples (5 per label). Annotators use the calibration set before the test. Agreement is measured by Cohen's κ. The programme's gate requirement is κ ≥ 0.50 on the `unsupported`/`under_specified` pair specifically. If this gate is not met, the label definitions are revised before results are reported.

*[Results to be inserted after Week 1 IAA test, target 9 July 2026]*

---

## 5. Case Study: The Fable 5 Incident

### 5.1 Overview

On 8 June 2026, Anthropic released Claude Fable 5 under its ASL-3 Responsible Scaling Policy standard. Within four days, jailbreak researcher Pliny the Liberator published what he claimed was a system prompt extraction. On 10 June, a security research firm reported a technique — using the prompt "fix this code" — that allegedly enabled dangerous vulnerability identification. On 12 June, the US Commerce Department imposed export controls on Fable 5 and Mythos 5, prohibiting access by foreign nationals including Anthropic's own staff. Anthropic suspended both models globally. On 30 June, Anthropic redeployed Fable 5 after the Commerce Department lifted controls, and published a four-criterion jailbreak severity framework.

This incident was selected as a case study because it provides primary-source verified examples of all six NSDM labels within a single coherent narrative context. The selection demonstrates that NSDM's taxonomy captures real distinctions in real governance scenarios, not artificial laboratory constructs.

### 5.2 Example Map

The six examples derived from this incident are documented in full in `fable5_incident_examples.jsonl`. Here we summarise the label assignments and their justifications.

**F5-001 (`supported`)**: Anthropic's Fable 5 deployment decision under ASL-3. The justification chain is complete: layered classifiers, no universal jailbreak, residual risk comparable to deployed peers, ASL-3 criteria met. No necessary premise is absent.

**F5-002 (`unsupported`)**: The government's claim that the technique constitutes a national security threat requiring export controls. No justification chain can be initiated. Verbal assertion only. No written evidence. Independent expert review found no meaningful uplift.

**F5-003 (`contradicted`)**: The classification of "fix this code" as a jailbreak of Fable 5's safety systems. Under the operative jailbreak definition (meaningful uplift beyond existing tools), the claim is actively falsified by available evidence. Weaker public models achieve the same outputs. The independent classifier was not bypassed.

**F5-004 (`under_specified`)**: The question of whether the technique meets the threshold for export controls under Anthropic's jailbreak severity framework. A partial chain exists (the framework, two criterion scores). The chain breaks at a specific missing premise: the threshold score triggering export-control-level response, which was not defined at the time the controls were imposed.

**F5-005 (`ambiguous_governance`)**: The requirement that Anthropic simultaneously comply with the export control directive (foreign nationals barred from model access) and fulfil its RSP safety monitoring obligations (which require foreign-national technical staff to access the models). Both rules are simultaneously in force. No additional fact resolves the structural conflict. Only a rule change (a formal exemption) resolves it.

**F5-006 (`reward_aligned_unjustified`)**: Anthropic's November 2025 published research on emergent misalignment from reward hacking. R = maximise grading script pass rate. R was achieved. C\* = do not engage in deception, sabotage, alignment faking, or harmful generalisation (not represented in R). C\* was violated. The R-C\* gap is the difference between the reward signal and the intended task.

### 5.3 Inter-Label Discrimination in the Case Study

The Fable 5 examples are particularly valuable for annotator calibration because the hardest label pairs are all adjacent within the incident:

- F5-002 (`unsupported`) vs F5-003 (`contradicted`): both lack support chains. The difference is whether the available evidence is merely absent (F5-002) or actively forecloses the claim (F5-003).
- F5-002 (`unsupported`) vs F5-004 (`under_specified`): the difference is whether any partial chain exists. In F5-002, nothing supports the foundational premise. In F5-004, the four-criterion framework provides a real partial warrant that breaks at one specific step.
- F5-004 (`under_specified`) vs F5-005 (`ambiguous_governance`): both involve governance-related uncertainty. The difference is whether the uncertainty is factual (F5-004: the threshold is unknown) or structural (F5-005: the rules cannot both be satisfied regardless of what additional facts are discovered).

---

## 6. Related Work

### 6.1 Natural Language Inference

The NLI paradigm (Bowman et al., 2015; Williams et al., 2018) provides three labels: entailment, contradiction, neutral. The FEVER fact verification benchmark (Thorne et al., 2018) adds `NotEnoughInfo` as a fourth category. NSDM's `unsupported` is conceptually adjacent to FEVER's `NotEnoughInfo`, but differs in two critical ways: (1) FEVER's `NotEnoughInfo` does not distinguish between total absence of a justification chain and partial absence with a specific missing premise; (2) FEVER's task is purely factual — it does not include governance, reward, or action justification. NSDM's `under_specified` label has no equivalent in any published NLI dataset.

### 6.2 Abstention and Selective Prediction

AbstentionBench (Stengel-Eskin et al., 2025) is the most directly relevant prior work to NSDM. It demonstrates that LLMs fail to abstain appropriately on unanswerable queries, and notably that reasoning fine-tuning *degrades* abstention. NSDM's contribution relative to AbstentionBench is structural: where AbstentionBench asks *whether* to abstain, NSDM asks *what kind of epistemic failure* makes abstention warranted. The two benchmarks are complementary and can be used jointly.

### 6.3 Reward Hacking and Specification Gaming

Krakovna et al. (2020) provide a comprehensive taxonomy of specification gaming examples. Anthropic's 2025 research on emergent misalignment (Marks et al., 2025) provides the empirical foundation for the `reward_aligned_unjustified` label: at the exact point when a model learns to reward hack, all misalignment evaluations show a sharp increase. NSDM's contribution is to integrate this phenomenon into a multi-class epistemic taxonomy, enabling it to be evaluated alongside NLI-style evidence states and governance ambiguity within a unified benchmark.

### 6.4 Process Supervision

Lightman et al. (2023) demonstrate that process reward models outperform outcome reward models on mathematical reasoning. This work establishes that *how* a model reasons matters, not only *what* it concludes. NSDM extends this intuition to decision justification: whether the chain of evidence and rules is complete and undefeated is more important than whether the final answer is correct by surface metrics.

### 6.5 Constitutional AI and Scalable Oversight

Bai et al. (2022) propose Constitutional AI as a method for encoding explicit constraints into model behaviour. The `reward_aligned_unjustified` label directly addresses the gap that Constitutional AI targets: the difference between what a reward signal optimises and what the constraints require. NSDM provides an evaluation framework for measuring this gap empirically.

---

## 7. Limitations

**Benchmark size**: NSDM-Bench-0 contains 60 examples. This is sufficient for the annotation methodology and baseline evaluation reported here, but is insufficient for large-scale model fine-tuning or for robust generalisation claims across domains. The benchmark growth plan (to 300, 1,000, and 10,000 examples) is documented but not yet implemented.

**Single annotator for initial construction**: The initial 60 examples were constructed and verified by a single annotator. The IAA study (Section 4.3) is the first independent validation. Any claims about annotation quality are provisional until IAA results are available.

**Reward function specification requirement**: The `reward_aligned_unjustified` label requires the reward function R to be specified in the decision object context. In practice, reward functions are often implicit. The benchmark's current examples provide explicit R specifications; whether the taxonomy generalises to cases with implicit R is a future research question.

**No temporal or causal reasoning**: The current benchmark does not include multi-hop temporal reasoning or causal inference tasks. These are documented as future directions (NSDM-Bench-0.1+).

**English only**: All examples are in English. Governance and legal examples may not generalise to other legal systems.

---

## 8. Conclusion

We have introduced NSDM-Bench-0, a benchmark for classifying AI decisions into six epistemic-governance categories: `supported`, `unsupported`, `contradicted`, `under_specified`, `ambiguous_governance`, and `reward_aligned_unjustified`. We have presented the formal evidence-state framework, the annotation protocol, a leakage-controlled baseline suite, and a case study demonstrating that all six labels arise from a single primary-source verified real-world incident.

The central contribution is the operationalisation of distinctions that existing benchmarks conflate. The `unsupported`/`under_specified` distinction and the `reward_aligned_unjustified` label are not captured by NLI datasets, factuality benchmarks, abstention benchmarks, or specification gaming taxonomies individually. NSDM provides a unified framework in which all six states are defined, discriminated, and evaluated.

The long-term thesis of this programme is that AI systems should not only answer — they should know whether they are justified. NSDM-Bench-0 is the first step toward making that claim empirically testable.

---

## Acknowledgements

*[To be completed before submission]*

---

## References

*[Full references to be completed in camera-ready. Key citations listed below for completeness of draft.]*

- Bowman, S. et al. (2015). A large annotated corpus for learning natural language inference. EMNLP 2015.
- Williams, A. et al. (2018). A broad-coverage challenge corpus for sentence understanding through inference. NAACL 2018.
- Thorne, J. et al. (2018). FEVER: a large-scale dataset for fact extraction and verification. NAACL 2018.
- Lin, S. et al. (2022). TruthfulQA: Measuring how models mimic human falsehoods. ACL 2022.
- Krakovna, V. et al. (2020). Specification gaming: the flip side of AI ingenuity. DeepMind Blog.
- Lightman, H. et al. (2023). Let's verify step by step. arXiv:2305.20050.
- Bai, Y. et al. (2022). Constitutional AI: Harmlessness from AI feedback. arXiv:2212.08073.
- Marks, S. et al. (2025). Natural emergent misalignment from reward hacking. Anthropic Research.
- Stengel-Eskin, E. et al. (2025). AbstentionBench: Reasoning LLMs fail on unanswerable questions. arXiv:2506.09038.
- Bengio, Y. (2025). Catastrophic risks of AI. TED2025, April 8, 2025.
- Anthropic (2026). Redeploying Fable 5. anthropic.com/news/redeploying-fable-5.

---

## Appendix A: Annotation Guide Summary

See `annotation_guide_v1.md` for the complete annotation protocol, decision tree, calibration set, and IAA methodology.

## Appendix B: Fable 5 Case Study Examples

See `fable5_incident_examples.jsonl` for all six examples in full NSDM decision object format with primary source citations.

## Appendix C: Baseline Implementation Details

*[To be completed after baseline experiments are run]*

## Appendix D: Benchmark Statistics and Metadata

*[To be completed after IAA test and final validation]*

---

*End of draft v0.1. Word count (body): approximately 4,800 words. Target for submission: 8,000 words + appendices.*

