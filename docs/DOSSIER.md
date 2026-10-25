# Internal project dossier — Hobbly — Booking and Payment Vertical Slice

Status: technical prototype; publication and user-interpretation gates pending.

## Why this project exists

Can a narrow booking flow maintain valid states, inventory and payment idempotency through happy-path and failure scenarios?

## Mechanism

SQLite-backed state machine with explicit transitions, inventory reservation, simulated authorization/capture, idempotency ledger and negative-path tests.

## Evidence chain

Concept record → source map → pre-test prediction → code → unit and negative tests → deterministic result → evidence hashes → case-study draft.

## Claim boundary

The defensible claim is that a narrow, local prototype was implemented and tested on the disclosed fixture. No production, client or realized-impact claim is made.
