# Preserving UNKNOWN in Decision Scores

## A development case study of numeric coercion, proxy validity and correction evidence

**Author:** Rajesh Singh · MetaForgeX AI  
**Version:** 0.1 · 26 November 2026  
**Status:** Author-approved public technical working draft; not peer-reviewed.  
**Evidence:** Supplied Claude-built Rentier Monitor export and local synthetic function probes. A reported repair remains unverified against revised code and a live browser.

### Abstract

A decision score can become misleading through valid language behaviour applied to an invalid measurement contract. We inspect a supplied monitoring export containing 25 calculation definitions and 31 concentration records. All 27 scored concentration rows reproduce, yet their measurement units and aggregation assumptions limit economic interpretation. Synthetic calls to exported functions additionally show missing required inputs converted into numeric outputs: an unknown time-to-cash receives the fastest rating, and a second missing field produces a score of 103 on a nominal 100-point scale. We distinguish function-level defects from observed production impact, describe a guarded scoring contract, and preserve the difference between a reported correction and a reproduced repair. The case does not establish prevalence, financial harm or a new missing-data method.

### 1. Scope and provenance

The Rentier Monitor is Rajesh Singh's Claude-assisted project. This is a cross-workflow review of supplied source, not a third-party security investigation. The supplement export is identified as OWHO-2026-11-26-supplement; its method version is c070. All seven content-file hashes matched the supplied manifest.

The original calculation export has SHA-256 `3dd30f60a20d99366c133f64f4c1678eabfa00f2487c7e7c9be9824f4f253324`. It contains 25 safeCalc definitions and additional browser-rendering code. Only the calculation-definition prefix was evaluated in the local probe context; rendering code was excluded. Dependencies needed by the selected calls were supplied explicitly. This does not reproduce the full dashboard or unexported validation paths.

### 2. A correct formula can measure the wrong construct

For fractional supplier shares s_i and an others tail o evenly distributed over k suppliers, the exported formula uses:

HHI = Σ s_i² + o²/k; N_eff = 1/HHI.

Its displayed score is max(0, round(100×(1−log10(N_eff)/3))). The direction is correct: concentration raises the score. All 27 scored rows reproduced at the displayed precision; four rows had insufficient shares and remained unscored.

The underlying units vary: firm revenue, country output, web referrals, survey responses, cloud-region counts and registered persons. These should not be treated as interchangeable measurements of market power. In particular, cp27 assigns 100% evenly across 8,512 registered persons, obtaining 8,512 effective suppliers and a score of zero. The registry count is not evidence of independent firms, equal revenue shares or zero economic rents.

Grouped records also change apparent concentration. Dividing the supplied 66% turbine bloc equally among its three firms changes its score from 89 to 74 with other assumptions fixed. Equal division of the 48.86% colocation bloc among five firms changes 81 to 63. These are sensitivity examples, not corrected estimates or complete uncertainty bounds. The code already excludes marked bloc rows from the Global capital-pillar mean; that safeguard should be preserved.

### 3. Numeric validity differs from evidence validity

ECMAScript specifies numeric conversion of null to positive zero [1]. That is defined language behaviour. An application requiring an observed cost, cash balance or threshold must decide whether such conversion is admissible before using it.

The exported opportunity function calculates speed from Number(months_to_cash), then combines rent, fit, capital and speed. With rent=5, fit=5, capital=1 and months_to_cash=null, the function assigns speed=5 and score=100. Replacing capital with null yields score=103. The conversion has supplied both favourable timing and a capital value that the input did not establish.

| Synthetic probe on original export | Observed result |
|---|---|
| Opportunity months_to_cash=null | Fastest speed rating |
| Opportunity months_to_cash=null and capital=null | Score 103 |
| Labour index=null | Numeric share 0 |
| Neocloud cash=null | Numeric cash 0 |
| Household trigger=null, clock=16.6 | Trigger 0 and action status Later |

These calls demonstrate executable behaviours for the supplied functions. They do not show those inputs occurred in every live table, or that an operator acted on the outputs. The source came from a development monitoring system; no customer data or real financial transaction was exercised.

### 4. Proposed guarded scoring contract

Preserve distinct states for confirmed zero, UNKNOWN, NOT APPLICABLE, malformed and stale values. A missing required field should prevent a definitive score or ranked recommendation. Optional-field defaults must be declared individually and remain distinguishable from observed values.

Before conversion, validate type and presence. After permitted conversion, require finite values and task-specific ranges. Return a reason and input provenance with any withheld score. Bounds checks detect impossible outputs; clamping 103 to 100 would hide this example's cause and is not an adequate repair.

A timestamp contract is also necessary. A valid historical reading may be stale for a current decision. Validity rules should use the source's expected cadence and the decision's consequence rather than a universal age threshold.

### 5. Correction record and verification boundary

Claude's subsequent return note, supplied as return_2026-11-26b.md, reports two distinct changes. c072 revises measurement-kind labels and makes cp27 unscored while retaining its registration count as context. c073 reportedly updates the four affected calculations and panels after the owner's approval.

The note reports no affected current rows in opportunities, labour-share inputs or household actions, and one missing NBIS finance-lease value in the financial table. It describes regression checks, unchanged valid outputs apart from new flags, and UNKNOWN results for synthetic invalid inputs. It explicitly says browser visuals were not checked.

This paper treats those statements as a maintainer/Claude report. The revised core.js, relevant current inputs and rendered panels were not supplied here. Therefore the repair and its regression claims are not independently reproduced. Publication should retain that distinction or update this section with an actual verification record.

### 6. Reproduction contract

The preparation pack contains a synthetic probe script, results, environment and hashes tied to the original source. It captures definitions, invokes only selected calculation functions and records outputs as JSON. Reproduction requires Node.js and the exact original calculation export. It does not use the live Claude artifact or execute its browser interface.

The paper's acceptance checks are separate: original failure demonstrated; proposed repair contract specified; revised-code behaviour pending; rendered-panel behaviour pending. Do not collapse these into a single PASS.

### 7. Implications for ACE and NSDM

Numeric correctness, construct validity and action admissibility require separate checks. An implementation can reproduce an arithmetic formula while giving a proxy a stronger meaning than its data supports. It can also obey its programming language while inventing application-level evidence through coercion.

Before optimizing a workload, establish the required states and their transitions. A fast path should preserve UNKNOWN and confirmed zero distinctly. Later backend comparisons can then assess speed only after the relevant semantic contract holds. This case has not run a GPU comparison or validated a general admission framework.

### 8. Limits and next test

This is one supplied project and a small set of targeted probes, not a representative sample of AI-built software. There is no estimate of prevalence, downstream loss or customer demand. Source labels and hashes do not independently validate every financial, political or licensing claim in the monitor.

Next, obtain the corrected definitions and selected inputs. Replay the original probes, test valid controls, compare missing versus zero, and inspect rendered UNKNOWN states. Preserve failures and correction history. Broader cases such as stale and conflicting data are proposed extensions, not tested results.

### References and disclosure

[1] Ecma TC39. ECMAScript Language Specification, ToNumber. https://tc39.es/ecma262/multipage/abstract-operations.html#sec-tonumber. Accessed 26 November 2026; mutable specification, no release pin claimed.

[2] Rentier Monitor, OWHO-2026-11-26-supplement, supplied source and manifest; owner-supplied development record; selected reproducibility inputs released in monitor/.

[3] MetaForgeX, Rentier/Overwrite supplement review, 26 November 2026; original probe findings and measurement-sensitivity analysis.

[4] Supplied Claude return note, return_2026-11-26b.md, c072/c073 reports; revised source and browser QA pending.

AI-assisted review and drafting under human direction. The author owns the reviewed project. Author publication sign-off recorded 26 November 2026; this is not independent validation of the owner's system or a claim of a novel missing-data method.

Suggested citation: Singh, R. (2026). Preserving UNKNOWN in Decision Scores. MetaForgeX AI technical case-study draft, v0.1, 26 November.


Public release note: author authorized proceeding with this reviewed package on 26 November 2026. Working-paper status and scientific limitations are unchanged. Source and reproduction record: https://github.com/Rajesh0311/accelerated-computing-engineering/tree/ace-nsdm-2026-11-26/publications/weekly/2026-11-26
