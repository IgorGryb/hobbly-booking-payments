# Internal project dossier — Hobbly — Booking and Payment Vertical Slice

Status: technical prototype; publication and user-interpretation gates pending.

## Why this project exists

Can a narrow booking flow maintain valid states, inventory and payment idempotency through happy-path and failure scenarios?

## Mechanism

SQLite-backed sequential booking/capture reference with key-conflict checks, cancellation, full refund and reconciliation; no separate authorization stage, live PSP or production concurrency guarantee.

## Evidence chain

Concept record → source map → pre-test prediction → code → unit and negative tests → deterministic result → evidence hashes → case-study draft.

## Claim boundary

The defensible claim is that a narrow, local prototype was implemented and tested on the disclosed fixture. No production, client or realized-impact claim is made.
