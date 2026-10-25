#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "metadata/artifact.yaml", "docs/PROBLEM.md", "docs/SOURCE-MAP.md",
    "docs/HYPOTHESES.md", "docs/REQUIREMENTS.md", "docs/adr/ADR-001.md",
    "docs/DATA-CARD.md", "docs/MODEL-CARD.md", "docs/TEST-REPORT.md",
    "docs/LIMITATIONS.md", "docs/DOSSIER.md", "docs/CASE-STUDY.md",
    "docs/PROJECT-OVERVIEW.md", "docs/WEB-COPY.md", "docs/DEMO-GUIDE.md",
    "docs/INTERVIEW-NARRATIVE.md", "docs/ARCHITECTURE.mmd",
    "docs/POST-MORTEM.md", "artifacts/results.json", "artifacts/evidence-manifest.json",
]
missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
if missing:
    raise SystemExit("missing required files: " + ", ".join(missing))
metadata = json.loads((ROOT / "metadata/artifact.yaml").read_text())
results = json.loads((ROOT / "artifacts/results.json").read_text())
manifest = json.loads((ROOT / "artifacts/evidence-manifest.json").read_text())
assert metadata["validation_status"] in {"technical-validation-pending", "technical-validation-passed"}
assert results["project_id"] == metadata["project_id"]
assert manifest["project_id"] == metadata["project_id"]
assert manifest["artifacts"], "empty evidence manifest"
print(f"documentation valid: {metadata['project_id']} ({len(manifest['artifacts'])} evidence files)")
