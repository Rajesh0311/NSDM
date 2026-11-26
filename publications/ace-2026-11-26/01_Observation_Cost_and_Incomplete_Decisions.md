# Observation Cost and Incomplete Decisions

## A controlled development study of early exit, evidence acquisition and declared availability

**Author:** Rajesh Singh · MetaForgeX AI  
**Version:** 0.1 · 26 November 2026  
**Status:** Author-approved public working draft; not peer-reviewed or submitted.  
**Evidence:** Synthetic CPU development fixtures recorded on 25–26 November 2026. No new scientific run was performed to write this paper.

### Abstract

Reducing observation expenditure can preserve a decision, change its completion status, or conceal insufficient evidence. We distinguish these cases using an existing synthetic thermal screen. An equal-information comparison on 128 development cases produced identical fixed-pair and early-exit decisions, while early exit used 203 rather than 256 readings. A subsequent two-action utility model allowed acquisition or HOLD after a non-flagging first reading. Acquisition was preferred when its attempt price plus waiting penalty was below the expected avoided incomplete-outcome penalty. Across 7,680 enumerated branch traces, weighted losses matched analytic expectations. At one high-price setting, lower declared loss coincided with 75 incomplete outcomes. The study supplies accounting and validity controls, rather than a new acquisition algorithm, quality-matched economic savings or protected evaluation of an autonomous agent.

### 1. Research question and contribution

When does acquiring less evidence preserve the required decision, and when does it instead change the service being delivered?

The contribution is a bounded comparison with explicit incomplete outcomes, shared information, declared charging and a reproducible analytic reference. The acquisition problem is established territory. Li and Oliva's active-acquisition POMDP formulation incorporates information-acquisition cost into subsequent decision rewards [1]. We have not reproduced their algorithm or benchmarked against it. Our reference is deliberately smaller and does not establish algorithmic novelty.

### 2. Task and information boundary

The fixture evaluates a two-reading residual screen. A reading strictly outside ±0.25 K flags the case. The declared reading times are 220 and 320 simulated seconds; the cap is two attempts and the deadline is 320 simulated seconds. A successful first reading is already acquired and charged. If it flags, the OR screen is resolved without reading the second value. Otherwise CLEAR requires a delivered second reading within tolerance. Missing follow-up evidence remains INCOMPLETE.

FLAG and CLEAR describe this screen. They do not establish physical model adequacy, industrial safety or scientific truth.

On 25 November, both policies received the same six-field context, provider access and caps. Hidden family labels, seeds, future residuals and complete-data scores were excluded from that interface. This establishes a trusted development interface, not protection against hostile policy code: same-identity code can still access evaluator memory or files.

The 128 cases come from eight authored thermal families with repeated noise and paired controls/challenges. They are not 128 independently sampled physical systems. Previously generated residuals were replayed; no new physical simulation or fitting was performed on 25–26 November.

### 3. Matched-decision early-exit control

The fixed-pair policy acquired both readings. The early-exit policy stopped after a first flag and otherwise acquired the second reading. Equal tools and limits did not require equal expenditure.

| Recorded development result, 25 November | Fixed pair | Early exit |
|---|---:|---:|
| Cases | 128 | 128 |
| FLAG | 63 | 63 |
| CLEAR | 65 | 65 |
| Readings | 256 | 203 |
| Summed simulated seconds | 40,960 | 35,660 |

All 128 screen decisions matched. For 53 first-flag cases, replacing the unacquired future residual with +1000 or −1000 K did not change decision or resources and caused no provider calls: 106 functional checks. Thirteen boundary controls also passed. These results validate logical short-circuiting for the declared screen. They do not quantify wall-clock speedup, energy or financial savings.

### 4. Declared acquisition utility

Let p be the follow-up attempt price, d the waiting penalty, q the authored probability of successful delivery, and H the incomplete-screen penalty. The common first-reading charge is sunk and omitted from the remaining-action comparison.

L(HOLD) = H.

L(ACQUIRE) = p + d + (1 − q)H.

Therefore acquisition is preferred exactly when p + d < qH. Ties select HOLD. Failed acquisition pays attempt and waiting costs and retains the incomplete penalty. Successful acquisition resolves the limited screen; it does not validate the physical model.

The frozen study used H=2, d=0.5, q∈{0,0.5,1} and p∈{0,0.5,1,1.5,2}. Each first observation incurred a common charge of 1. These are hypothetical utility units. q is not measured provider reliability. The choice rule is optimal by construction for this two-action objective; that property is not learned superiority.

### 5. Enumeration and results

The study enumerated 128 cases × 3 beliefs × 5 prices × 2 policies × 2 delivery branches: 7,680 traces. Branch weights q and 1−q produce analytic expectations. Zero-weight branches were retained as labelled counterfactual controls. They are neither observed failures nor additional independent samples.

All 3,840 case/policy/cell expected-loss checks matched closed form. Query traces matched the prior replay, resource charges reconciled, caps held, and unsupported CLEAR outcomes were prohibited. Exact ties and no-provider-call paths were checked.

| q | p | Policy | Complete | Incomplete | Readings/attempts | Total declared loss |
|---:|---:|---|---:|---:|---:|---:|
| 1 | 0 | Both | 128 | 0 | 203 | 165.5 |
| 1 | 2 | Always acquire after first non-flag | 128 | 0 | 203 | 315.5 |
| 1 | 2 | Cost-aware acquire/HOLD | 53 | 75 | 128 | 278 |

The high-price result changes completion. The lower declared loss cannot be presented as delivering the same completed service more cheaply. The authored objective explicitly permits paying an incomplete-outcome penalty instead of purchasing evidence.

A separate adverse control declared q=1 and p=1 while making the source unavailable. Acquisition remained INCOMPLETE and incurred 4.5 total units, compared with 3 for holding, including the common first charge. The 1.5-unit difference exposes the consequence of a mistaken availability belief. It does not estimate real outage risk.

### 6. Reproducibility and evidence identity

The 26 November package SHA-256 is `af2d15b9cd7687bfeed84bd39d606fe4c5fb369949bb0027b4c4e74d12de29ff`. Its source is `NSDM_Observation_Price_Availability_2026-11-26.zip`. The contained 25 November archive is pinned at `b33c2754fa62089902d6aad99b51714c8a1f462fd441f373db34a9f91a5ed186`.

Recorded environment: Python 3.12.14, Linux 6.18.57 x86-64, standard-library CPU replay. The 26 November environment manifest reports glibc 2.41. It must not be replaced by a different day's host metadata.

Recorded commands from the extracted dated package:

```bash
timeout 20s python3 -B price_control.py run1 > run1.log
timeout 20s python3 -B price_control.py run2 > run2.log
```

The original validation reports byte-identical JSON, CSV and stdout across those executions, and an unchanged baseline rerun. During publication preparation, the saved archive's SHA-256 and CRC were checked. The scientific experiment was not rerun to draft this manuscript. The complete historical archive remains private. A curated reproduction subset is released alongside this paper under thermal/.

### 7. Threats to validity

The fixture is synthetic, the utility is authored, successful observation is simplified, and the same-identity evaluator is exposed. Scenario enumeration does not establish frequencies or confidence intervals for real systems. Cost excludes preparation, policy development, verification, plotting and human review; simulated time is not measured runtime. There is no protected holdout, external replication, general-agent comparison, calibrated reliability, real invoice, metered energy or customer outcome.

### 8. Next falsifiable comparison

Freeze assumed availability q_hat separately from actual scenario availability q_actual. Compare the current rule, fixed acquisition and an interval-robust reference with the same information and accounting. Under this unchanged utility, the worst-case interval rule uses q_low in p+d<q_low H. Test its loss and completion tradeoffs; do not assume conservatism always improves useful service. Confirmatory agent comparisons remain dependent on legitimate evaluator separation.

### References and disclosure

[1] Li, Y. and Oliva, J. (2025). Towards Cost Sensitive Decision Making. AISTATS, PMLR 258:3601–3609. https://proceedings.mlr.press/v258/li25h.html. Primary abstract and method overview inspected; algorithm/software not reproduced.

[2] MetaForgeX, NSDM thermal policy-interface audit, 25 November 2026. Source archive identified above; curated reproduction subset in thermal/.

[3] MetaForgeX, NSDM observation price and availability control, 26 November 2026. Frozen protocol, source, traces and validation in the identified archive.

Prepared with AI assistance under human direction. Author publication sign-off recorded 26 November 2026. No peer-review, novelty or independent-validation claim is made.

Suggested citation: Singh, R. (2026). Observation Cost and Incomplete Decisions. MetaForgeX AI working-paper draft, v0.1, 26 November.


Public release note: author authorized proceeding with this reviewed package on 26 November 2026. Working-paper status and scientific limitations are unchanged. Source and reproduction record: https://github.com/Rajesh0311/accelerated-computing-engineering/tree/ace-nsdm-2026-11-26/publications/weekly/2026-11-26
