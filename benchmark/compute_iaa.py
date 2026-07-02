"""
NSDM-Bench-0 IAA Calculator
Usage: python compute_iaa.py --input iaa_results.jsonl
Output: Cohen's kappa overall, per-label, and per confusion pair
"""

import json
import argparse
from collections import defaultdict
import math

LABELS = [
    "supported",
    "unsupported", 
    "contradicted",
    "under_specified",
    "ambiguous_governance",
    "reward_aligned_unjustified"
]

def load_annotations(filepath):
    annotations = {}
    with open(filepath, 'r') as f:
        for line in f:
            item = json.loads(line.strip())
            example_id = item['id']
            if example_id not in annotations:
                annotations[example_id] = {}
            annotations[example_id][item['annotator_id']] = item['label']
    return annotations

def compute_cohens_kappa(labels_a, labels_b):
    n = len(labels_a)
    if n == 0:
        return 0.0
    
    label_set = sorted(set(labels_a + labels_b))
    k = len(label_set)
    label_idx = {l: i for i, l in enumerate(label_set)}
    
    # Observed agreement
    observed_agree = sum(1 for a, b in zip(labels_a, labels_b) if a == b) / n
    
    # Expected agreement
    count_a = defaultdict(int)
    count_b = defaultdict(int)
    for a, b in zip(labels_a, labels_b):
        count_a[a] += 1
        count_b[b] += 1
    
    expected_agree = sum(
        (count_a[l] / n) * (count_b[l] / n) 
        for l in label_set
    )
    
    if expected_agree == 1.0:
        return 1.0
    
    kappa = (observed_agree - expected_agree) / (1 - expected_agree)
    return round(kappa, 4)

def build_confusion_matrix(labels_a, labels_b, label_list):
    n_labels = len(label_list)
    label_idx = {l: i for i, l in enumerate(label_list)}
    matrix = [[0] * n_labels for _ in range(n_labels)]
    for a, b in zip(labels_a, labels_b):
        if a in label_idx and b in label_idx:
            matrix[label_idx[a]][label_idx[b]] += 1
    return matrix

def compute_pairwise_kappa(labels_a, labels_b, label1, label2):
    filtered_a = []
    filtered_b = []
    for a, b in zip(labels_a, labels_b):
        if a in [label1, label2] or b in [label1, label2]:
            filtered_a.append(a)
            filtered_b.append(b)
    if not filtered_a:
        return None
    return compute_cohens_kappa(filtered_a, filtered_b)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--annotator1', default=None)
    parser.add_argument('--annotator2', default=None)
    args = parser.parse_args()
    
    annotations = load_annotations(args.input)
    
    # Get annotator IDs
    all_annotators = set()
    for ex_annotations in annotations.values():
        all_annotators.update(ex_annotations.keys())
    
    annotator_list = sorted(all_annotators)
    if len(annotator_list) < 2:
        print("ERROR: Need at least 2 annotators")
        return
    
    ann1 = args.annotator1 or annotator_list[0]
    ann2 = args.annotator2 or annotator_list[1]
    
    print(f"\nAnnotators: {ann1} vs {ann2}")
    print("=" * 60)
    
    # Extract paired labels
    labels_a, labels_b = [], []
    disagreements = []
    
    for ex_id, ex_annotations in sorted(annotations.items()):
        if ann1 in ex_annotations and ann2 in ex_annotations:
            la = ex_annotations[ann1]
            lb = ex_annotations[ann2]
            labels_a.append(la)
            labels_b.append(lb)
            if la != lb:
                disagreements.append((ex_id, la, lb))
    
    n_total = len(labels_a)
    n_agree = sum(1 for a, b in zip(labels_a, labels_b) if a == b)
    
    print(f"\nTotal paired examples: {n_total}")
    print(f"Agreements: {n_agree} ({100*n_agree/n_total:.1f}%)")
    print(f"Disagreements: {len(disagreements)}")
    
    # Overall kappa
    kappa_overall = compute_cohens_kappa(labels_a, labels_b)
    print(f"\nOverall Cohen's κ: {kappa_overall}")
    
    # Interpret
    if kappa_overall >= 0.80:
        interpretation = "EXCELLENT"
    elif kappa_overall >= 0.65:
        interpretation = "SUBSTANTIAL — Paper submission ready"
    elif kappa_overall >= 0.50:
        interpretation = "MODERATE — Gate passed, continue"
    elif kappa_overall >= 0.45:
        interpretation = "MARGINAL — Guide revision required"
    else:
        interpretation = "POOR — SPRINT HALT. Revise definitions."
    
    print(f"Interpretation: {interpretation}")
    
    # Confusion matrix
    print("\nConfusion Matrix (rows=Annotator1, cols=Annotator2):")
    matrix = build_confusion_matrix(labels_a, labels_b, LABELS)
    header = f"{'':32s} " + " ".join(f"{l[:8]:>8s}" for l in LABELS)
    print(header)
    for i, row_label in enumerate(LABELS):
        row_str = " ".join(f"{matrix[i][j]:>8d}" for j in range(len(LABELS)))
        print(f"{row_label:32s} {row_str}")
    
    # Critical pairwise: unsupported vs under_specified
    print("\nCritical pairwise κ values:")
    critical_pairs = [
        ("unsupported", "under_specified"),
        ("supported", "under_specified"),
        ("contradicted", "unsupported"),
        ("ambiguous_governance", "under_specified"),
    ]
    
    for l1, l2 in critical_pairs:
        pk = compute_pairwise_kappa(labels_a, labels_b, l1, l2)
        if pk is not None:
            flag = " *** CRITICAL FAILURE" if (l1 == "unsupported" and l2 == "under_specified" and pk < 0.45) else ""
            print(f"  {l1} vs {l2}: κ = {pk}{flag}")
    
    # Disagreement list
    if disagreements:
        print(f"\nDisagreements ({len(disagreements)}):")
        for ex_id, la, lb in disagreements:
            print(f"  {ex_id}: {ann1}={la} | {ann2}={lb}")
    
    # Gate decision
    print("\n" + "=" * 60)
    print("GATE DECISION:")
    if kappa_overall >= 0.65:
        print("PASS — Proceed to full Bench-0 and Paper 1 drafting")
    elif kappa_overall >= 0.50:
        print("PASS (MINIMUM) — Document sources of disagreement, update guide")
    elif kappa_overall >= 0.45:
        print("MARGINAL PASS — MANDATORY guide revision before next round")
    else:
        print("FAIL — Sprint halted. Revise annotation_guide_v1.md Section 3.")
        
    # Check the critical pair
    unspec_kappa = compute_pairwise_kappa(labels_a, labels_b, "unsupported", "under_specified")
    if unspec_kappa is not None and unspec_kappa < 0.45:
        print("\n*** CRITICAL FAILURE: unsupported/under_specified κ below threshold ***")
        print("The central novelty distinction is not yet operationalised.")
        print("Revise Section 3 of annotation_guide_v1.md before ANY annotation proceeds.")

if __name__ == '__main__':
    main()
