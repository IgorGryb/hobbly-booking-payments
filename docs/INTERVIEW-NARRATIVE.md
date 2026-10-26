# Interview narrative

**Problem:** Can a narrow booking flow maintain valid states, inventory and payment idempotency through happy-path and failure scenarios?

**Choice:** I selected a narrow vertical slice with an explicit baseline and falsification criterion instead of treating existing documentation as implementation evidence.

**Execution:** SQLite-backed sequential booking/capture reference with key-conflict checks, cancellation, full refund and reconciliation; no separate authorization stage, live PSP or production concurrency guarantee.

**Mistake risk:** the fixture can overstate generality. I address that by labeling provenance, keeping alternative explanations and separating technical from external validation.

**Result:** the repository produces a reproducible, hashed technical result. Exact metrics are discussed only with the machine-readable evidence open.

**Next step:** seek user interpretation, then test on an approved external or public dataset where appropriate.
