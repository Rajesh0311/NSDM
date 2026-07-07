# Baseline Accuracy Table

| baseline_dir | baseline | description | n_rows | accuracy | clean_60_item_comparison | leakage_note | paper_use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_001 | Baseline 001 | Lexical / majority-supported baseline | 120 | 0.308 | False |  | Historical weak baseline; not directly comparable because row count differs. |
| baseline_002 | Baseline 002 | Early symbolic checker | 24 | 1.0 | False |  | Historical early symbolic baseline; not directly comparable because row count differs. |
| baseline_003 | Baseline 003 | Raw symbolic checker | 60 | 0.517 | True |  | Current 60-item comparison set. |
| baseline_004 | Baseline 004 | Structured symbolic reasoner | 60 | 0.967 | True | Leakage-inflated; task-family metadata mapped too directly to target labels. | Use only as leakage audit, not as best valid performance. |
| baseline_005 | Baseline 005 | No-task-family structured reasoner | 60 | 0.667 | True |  | Cleaner control after removing task-family shortcut. |
| baseline_006 | Baseline 006 | Clean modular boundary reasoner | 60 | 0.733 | True |  | Current strongest clean baseline. |
| baseline_007 | Baseline 007 | Evidence-state reasoner v0.1 | 60 | 0.6 | True |  | Evidence-state baseline v0.1; internal/provisional. |
| baseline_007_v0_2 | Baseline 007 v0.2 | Evidence-state reasoner v0.2 | 60 | 0.733 | True |  | Evidence-state baseline v0.2; paper-useful because it produces evidence-state JSONL. |
| baseline_008 | Baseline 008 | Zero-shot LLM - gpt-4.1-mini | 60 | 0.683 | True |  | Zero-shot LLM baseline using gpt-4.1-mini; paper-useful comparison against clean symbolic/modular baselines. |
| baseline_009 | Baseline 009 | Few-shot LLM - gpt-4.1-mini | 60 | 0.767 | True |  | Few-shot LLM baseline using gpt-4.1-mini; tests whether label demonstrations improve NSDM-specific categories. |
