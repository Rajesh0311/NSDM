"""Check current tracked public files; never print matching credential values."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
policy = json.loads((ROOT / ".public-release.json").read_text(encoding="utf-8"))
tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
approved = set(policy["approved_paths"])
errors = []
patterns = [
    ("private key", re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
    ("GitHub credential", re.compile(rb"(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{50,})")),
    ("AWS access-key identifier", re.compile(rb"(?:AKIA|ASIA)[A-Z0-9]{16}")),
    ("OpenAI-style credential", re.compile(rb"sk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{40,}")),
]
for name in filter(None, tracked):
    if name not in approved:
        errors.append(f"{name}: absent from public-release inventory")
    path = ROOT / name
    if not path.is_file():
        continue
    lower = name.lower()
    if any(part in {"private", "confidential", "customer-data", "client-data", "credentials", "secrets"} for part in Path(lower).parts):
        errors.append(f"{name}: private-content path")
    if Path(lower).name.startswith(".env") and not lower.endswith((".example", ".sample")):
        errors.append(f"{name}: environment secrets file")
    if lower.endswith((".pem", ".key", ".p12", ".pfx", ".kdbx")):
        errors.append(f"{name}: credential-container extension")
    data = path.read_bytes()
    for label, pattern in patterns:
        if pattern.search(data):
            errors.append(f"{name}: possible {label}; inspect privately")
    expected = policy.get("frozen_private_record_stubs", {}).get(name)
    # Git may check Markdown out as CRLF on Windows. Freeze the notice
    # content while accepting that checkout-only newline conversion.
    stub_data = data.replace(b"\r\n", b"\n")
    if expected and hashlib.sha256(stub_data).hexdigest() != expected:
        errors.append(f"{name}: private operational record must not be republished")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print("PASS: tracked paths inventoried; private-record stubs frozen; selected credential patterns absent.")
print("Scope: current tracked bytes only. No full history, archive decompression or semantic confidentiality guarantee.")
