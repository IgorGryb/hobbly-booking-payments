# Hobbly — Booking and Payment Vertical Slice

> Private case-study draft. Technical validation does not equal production validation.

## Context

Can a narrow booking flow maintain valid states, inventory and payment idempotency through happy-path and failure scenarios?

## Decision

I reduced a broad platform concept to one falsifiable vertical slice and selected a transparent implementation that can be reproduced without external services.

## Implementation

SQLite-backed state machine with explicit transitions, inventory reservation, simulated authorization/capture, idempotency ledger and negative-path tests.

## Validation

The repository records a prediction before the test, compares against a baseline or control, executes a negative test and hashes the resulting evidence. Exact metrics come from `artifacts/results.json` and must not be copied into public material without claim review.

## What this demonstrates

Problem framing, explicit assumptions, executable modeling, test design, evidence discipline and the ability to communicate limitations.

## Limitations

Simulated processor, single-process SQLite and simplified economics. No production security, settlement, refunds, chargebacks, KYC/AML, tax or regulatory compliance claim.
