# NSDM — GitHub Setup Instructions (Windows / VS Code)

Follow these steps once, on Day 1 (3 July 2026, before 06:30).

---

## Step 1: Create the GitHub Repository (5 minutes)

1. Go to https://github.com/new
2. Repository name: `nsdm`
3. Description: `NSDM — Neuro-Symbolic Decision Boundaries: A benchmark and framework for justified AI decision-making`
4. Visibility: **Private** initially (switch to Public when Paper 1 is submitted)
5. ✅ Add a README file: **No** (we have our own)
6. ✅ Add .gitignore: **No** (we have our own)
7. Licence: **None** (we have our own structure)
8. Click **Create repository**

---

## Step 2: Clone and Initialise (Windows Terminal / VS Code terminal)

```bash
# Navigate to your dev folder (adjust path as needed)
cd C:\Users\[YourName]\dev

# Clone the empty repo
git clone https://github.com/[your-handle]/nsdm.git
cd nsdm

# Copy all the files from the NSDM package into this folder
# (Copy everything from the downloaded NSDM package)

# Initial commit
git add -A
git commit -m "docs 2026-07-03: Programme initialisation — all threads completed 2 July 2026"
git push origin main
```

---

## Step 3: Python Environment

```bash
# In the nsdm/ folder
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Verify
python --version   # Should be 3.10+
python -c "import transformers, sklearn; print('Dependencies OK')"
```

---

## Step 4: Run First Self-Calibration

```bash
# With .venv active, from the nsdm/ root:
python benchmark/scripts/self_calibrate.py --input benchmark/calibration_set.jsonl
```

Expected: 10 examples, interactive CLI. Score ≥ 8/10 to proceed.

---

## Step 5: VS Code Setup

Install extensions:
- **Python** (Microsoft)
- **Pylance**
- **Markdown All in One** (Yu Zhang)
- **GitLens** (GitKraken)
- **Better Comments** (Aaron Bond) — for TODO/FIXME tracking

Recommended settings (`settings.json`):
```json
{
  "editor.rulers": [100],
  "editor.wordWrap": "wordWrapColumn",
  "editor.wordWrapColumn": 100,
  "files.autoSave": "onFocusChange",
  "python.defaultInterpreterPath": ".venv/Scripts/python.exe",
  "markdown.preview.scrollEditorWithPreview": true
}
```

---

## Step 6: Branch Strategy

```
main          — stable, always working
dev           — active development
paper1        — Paper 1 draft (branch off main when writing seriously)
baselines     — baseline classifier implementation
```

Daily workflow uses `main` until the paper enters submission review, then branching.

---

## Step 7: GitHub Actions (Optional — Week 3+)

Add a simple CI check to validate JSONL format on push:

```yaml
# .github/workflows/validate_benchmark.yml
name: Validate Benchmark
on: [push]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: python -c "import json; [json.loads(l) for f in __import__('glob').glob('benchmark/**/*.jsonl', recursive=True) for l in open(f) if l.strip()]; print('All JSONL valid')"
```

