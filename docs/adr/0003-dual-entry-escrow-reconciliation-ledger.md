# ADR 0003: Dual-Entry Escrow Reconciliation & Net Contribution Economics

- **Status:** Accepted
- **Date:** 2026-10-28
- **Context:** Marketplace Unit Economics & Financial Accounting
- **Deciders:** Igor Grybek (Systems Architect, Arxa Group)

## Context & Problem Statement
Marketplaces often mistake Gross Booking Value (GBV) or gross captured funds for net revenue. When refunds, chargebacks, and gateway fees are processed asynchronously, platforms suffer unallocated financial drift. Moreover, excessive customer support overhead for edge-case cancellations can easily flip positive take-rate revenue into operating losses.

## Decision Drivers
1. **Zero Financial Leakage:** Total captured funds minus refunds and payouts must continuously reconcile to zero across internal accounts.
2. **Support Cost Guardrails:** Establishing the mathematical ceiling where customer support friction renders transactions unprofitable.
3. **Transparent Escrow Lifecycle:** Funds remain held in protected escrow until service completion is verified.

## Decision Outcome
Chosen Option: **Dual-Entry Transaction Ledger with Breakeven Friction Bounds**.
- Financial ledger records separate entries for: `GROSS_CAPTURED`, `GATEWAY_FEE`, `ORGANIZER_ESCROW`, `PLATFORM_COMMISSION`, and `REFUND_DISBURSEMENT`.
- On a €50 booking at a 10% take-rate (€5.00 revenue), fixed processing and loss reserves equal €1.50.
- Customer support costs must remain strictly below **€3.50 per transaction** to maintain a positive contribution margin.
- Automated self-service cancellation workflows keep average support friction at €1.50, securing a **40% net contribution margin (+€2.00/booking)**.
