"""
NSDM IAA Set Preparation Script
Strips labels from a JSONL file for blind annotation.
Usage: python benchmark/scripts/prepare_iaa_set.py --input benchmark/examples/fable5_incident_examples.jsonl --output benchmark/splits/iaa_test_set_stripped.jsonl
"""

import json
import argparse
import random

FIELDS_TO_STRIP = ['label', 'confidence', 'annotation_notes', 'nearest_alternative',
                   'nearest_alternative_rejection', 'paper_use', 'R_and_Cstar_annotation_required']

def strip_labels(example):
    stripped = {k: v for k, v in example.items() if k not in FIELDS_TO_STRIP}
    # Also strip from evidence_state
    if 'evidence_state' in stripped:
        es = stripped['evidence_state']
        if isinstance(es, dict):
            stripped['evidence_state'] = {k: v for k, v in es.items() if k != 'label'}
    # Add annotation fields for the annotator to fill
    stripped['annotator_id'] = ""
    stripped['annotator_label'] = ""
    stripped['annotator_confidence'] = ""
    stripped['annotator_justification'] = ""
    stripped['annotator_missing_premise'] = ""
    stripped['annotator_nearest_alternative'] = ""
    stripped['annotator_nearest_alternative_rejection'] = ""
    return stripped

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--shuffle', action='store_true')
    args = parser.parse_args()

    with open(args.input) as f:
        examples = [json.loads(l) for l in f if l.strip()]

    if args.shuffle:
        random.seed(args.seed)
        random.shuffle(examples)

    stripped = [strip_labels(ex) for ex in examples]

    with open(args.output, 'w') as f:
        for ex in stripped:
            f.write(json.dumps(ex, ensure_ascii=False) + '\n')

    print(f"Prepared {len(stripped)} examples → {args.output}")
    print("Labels stripped. Give to annotators for independent labelling.")
    print("Annotators must fill: annotator_id, annotator_label, annotator_confidence,")
    print("                      annotator_justification, annotator_missing_premise")

if __name__ == '__main__':
    main()
