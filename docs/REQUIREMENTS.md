# Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-01 | Deterministic local execution with Python standard library | `make reproduce` |
| REQ-02 | Baseline or control comparison | `artifacts/results.json` |
| REQ-03 | Negative or falsification test | `make test` and result flag |
| REQ-04 | Explicit source and data provenance | `docs/SOURCE-MAP.md`, data card |
| REQ-05 | Reproducible evidence hashes | evidence manifest |
| REQ-06 | Limitations and claim boundaries | limitations and model card |
