# ADR 0002: SHA-256 Idempotency Keys for Duplicate Payment Elimination

- **Status:** Accepted
- **Date:** 2026-10-28
- **Context:** Payment Gateway Orchestration & PCI-DSS Tokenization
- **Deciders:** Igor Grybek (Systems Architect, Arxa Group)

## Context & Problem Statement
During peak booking periods or mobile network latency, customers frequently double-click checkout buttons or refresh checkout screens. Without cryptographic deduplication, multiple capture requests hit payment processors (Stripe/Adyen), triggering double debiting, customer rage, and chargeback fines.

## Decision Drivers
1. **Zero Double-Charging:** Repeated API calls with identical intent must return the cached success response.
2. **Cross-Booking Replay Rejection:** Attempting to reuse an idempotency key across differing booking IDs must be treated as a security violation.
3. **PCI-DSS Tokenization Boundaries:** Raw card numbers must never enter the platform's state machine.

## Decision Outcome
Chosen Option: **Cryptographic SHA-256 Idempotency Key Gate**.
Every client payment request carries an `Idempotency-Key` header:
- First Request: Recorded in the SQLite/Redis store as `IN_FLIGHT`.
- Matching Replay: Returns the cached receipt without calling the payment gateway again.
- Conflicting Payload: If the key matches an existing record but the booking ID or amount differs, the request is rejected with `409 CONFLICT` and logged in the security exception queue.
