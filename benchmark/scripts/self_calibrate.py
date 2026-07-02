"""
NSDM Self-Calibration Script
Run this EVERY MORNING before touching any benchmark files.
Usage: python benchmark/scripts/self_calibrate.py --input benchmark/calibration_set.jsonl
"""

import json
import argparse

LABELS = ["supported","unsupported","contradicted","under_specified","ambiguous_governance","reward_aligned_unjustified"]

LABEL_ABBREV = {
    "su": "supported", "sup": "supported", "supported": "supported",
    "un": "unsupported", "uns": "unsupported", "unsupported": "unsupported",
    "co": "contradicted", "con": "contradicted", "contradicted": "contradicted",
    "us": "under_specified", "under": "under_specified", "under_specified": "under_specified",
    "ag": "ambiguous_governance", "amb": "ambiguous_governance", "ambiguous_governance": "ambiguous_governance",
    "rr": "reward_aligned_unjustified", "rew": "reward_aligned_unjustified", "reward_aligned_unjustified": "reward_aligned_unjustified",
}

def parse_label(s):
    s = s.strip().lower()
    return LABEL_ABBREV.get(s, s)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--blind', action='store_true', help='Hide correct labels until end')
    args = parser.parse_args()

    with open(args.input) as f:
        examples = [json.loads(l) for l in f if l.strip()]

    print("\n" + "="*60)
    print("NSDM SELF-CALIBRATION")
    print("="*60)
    print(f"Total examples: {len(examples)}")
    print("Label abbreviations: su=supported | un=unsupported | co=contradicted")
    print("                     us=under_specified | ag=ambiguous_governance | rr=reward_aligned_unjustified")
    print("Type the full label or abbreviation. Enter to confirm.")
    print("="*60 + "\n")
    print("GATE: Score ≥ 8/10 before proceeding to any annotation today.\n")

    results = []
    for i, ex in enumerate(examples):
        print(f"--- Example {i+1}/{len(examples)} | ID: {ex['id']} ---")
        ctx = ex['input']['context']
        action = ex['input']['proposed_action']
        claim = ex['input'].get('proposed_claim', '(see action)')
        rules = ex['input'].get('rules', [])

        print(f"CONTEXT: {ctx[:400]}{'...' if len(ctx) > 400 else ''}")
        print(f"RULES:   {' | '.join(rules[:2])}")
        print(f"ACTION:  {action}")
        print(f"CLAIM:   {claim}")

        while True:
            user_label = input("\nYour label: ").strip()
            parsed = parse_label(user_label)
            if parsed in LABELS:
                break
            print(f"  Not recognised. Use: {' | '.join(LABELS)}")

        correct = ex.get('correct_label', ex.get('label', '?'))
        match = (parsed == correct)
        results.append({'id': ex['id'], 'your_label': parsed, 'correct': correct, 'match': match})

        if not args.blind:
            if match:
                print(f"  ✓ CORRECT: {correct}")
            else:
                print(f"  ✗ WRONG. Correct: {correct}")
                print(f"    Explanation: {ex['annotation_notes'][:300]}")
                print(f"    Nearest alternative rejected: {ex['nearest_alternative_rejection'][:200]}")
        print()

    score = sum(1 for r in results if r['match'])
    print("\n" + "="*60)
    print(f"SCORE: {score}/10")

    if score >= 9:
        print("EXCELLENT — Proceed to annotation.")
    elif score >= 8:
        print("PASS — Proceed to annotation. Review any misses before starting.")
    elif score >= 6:
        print("MARGINAL — Reread annotation_guide_v1.md Section 3 before annotating.")
    else:
        print("FAIL — DO NOT annotate today. Reread Sections 2–4 of the guide. Rerun tomorrow.")

    # Show misses
    misses = [r for r in results if not r['match']]
    if misses:
        print(f"\nMissed examples ({len(misses)}):")
        for r in misses:
            print(f"  {r['id']}: You said {r['your_label']}, correct is {r['correct']}")
        if any(r['your_label'] in ['unsupported','under_specified'] and r['correct'] in ['unsupported','under_specified'] for r in misses):
            print("\n  *** unsupported/under_specified confusion detected ***")
            print("  Mandatory: reread Section 3 — The Naming Test — before annotating.")
    print("="*60)

if __name__ == '__main__':
    main()
