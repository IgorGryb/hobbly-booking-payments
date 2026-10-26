# Model / mechanism card

## Method

SQLite-backed single-process state reference: reservation, simulated capture/failure, cancellation, full refund, key-conflict checks and capture/refund reconciliation. No separate authorization stage, live payment provider, settlement, partial refund or chargeback is implemented. Concurrent reservation/payment safety is not established; production use requires atomic transactions, provider webhook reconciliation and independent security review.

## Intended use

Transparent technical demonstration and discussion aid.

## Non-intended use

Production decisions, regulated decisions, investment advice, autonomous operation or claims about client impact.

## Validation

Unit tests, deterministic reproduction, baseline comparison and a negative or falsification test. User interpretation and external validation remain separate gates.
