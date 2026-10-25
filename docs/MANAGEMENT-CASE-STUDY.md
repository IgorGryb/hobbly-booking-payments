# Hobbly — management case study

Private review draft. Design study, not a client deployment.

## Problem

A reservation is not operationally complete until capacity, payment, cancellation and settlement states agree.

## Approach

A booking-service operating model with explicit transaction economics and exception ownership.

The design connects source evidence, explicit assumptions, operating ownership and model checks. Its primary output is a decision package that can be handed to an execution team.

## Key decision

Describe the end-to-end service, use simulated payments, and validate state transitions before evaluating commercial integrations.

## Operating design

1. Validate listing and available slot
2. Reserve capacity with expiry
3. Request and reconcile payment state
4. Confirm booking or release capacity
5. Handle cancellation/refund and reconcile settlement

## Economics and validation

Contribution per completed booking = fee revenue - payment cost - support cost - expected refund/dispute loss. Gross merchandise value is not revenue. Capacity, cancellations and failed payments constrain volume.

Testable hypothesis: Exception handling and transaction economics determine viability more than feature breadth.

Negative check: Duplicate callback and payment timeout; no double allocation or recognition of uncollected revenue.

## Outcome and limits

The current result is a documented management model with explicit handoffs, metrics and validation cases. Historical technical prototypes are supporting evidence only. Market adoption, customer impact and production operation are not established.

Synthetic payment state tests do not establish provider integration, fraud prevention or legal compliance.

## Next decision

Validate support/refund workload assumptions and compare buy versus partner delivery.

[Full management dossier](MANAGEMENT-DOSSIER.md)
