# Test report

Technical validation status: **passed on 2026-10-25**.  
Source snapshot: `14f1caed72a05745c7da691732fab96451f8dc73`.  
Reproduction command: `make validate`.

## Observed result

Happy path captured once; replay was idempotent; failed payment ended in `payment_failed`; modeled contribution remained an explicit synthetic assumption.

The unit, reproduction and documentation gates passed locally. The result supports a bounded technical-demonstration claim only. User interpretation, external validation and publication approval remain pending.
