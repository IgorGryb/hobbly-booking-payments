# Hobbly — Booking and Payment Vertical Slice

## A bounded prototype with an auditable evidence chain

Can a narrow booking flow maintain valid states, inventory and payment idempotency through happy-path and failure scenarios?

The project turns a broad platform concept into one deterministic vertical slice. SQLite-backed state machine with explicit transitions, inventory reservation, simulated authorization/capture, idempotency ledger and negative-path tests.

**Evidence available:** source map, pre-test prediction, code, unit and negative tests, machine-readable result and SHA-256 evidence manifest.

**Publication boundary:** private draft. The defensible statement is that the disclosed mechanism was implemented and tested on the disclosed fixture. Simulated processor, single-process SQLite and simplified economics. No production security, settlement, refunds, chargebacks, KYC/AML, tax or regulatory compliance claim.
