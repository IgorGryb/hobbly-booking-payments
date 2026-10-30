# ADR 0001: Deterministic Finite State Automaton (FSM) for Booking Workflows

- **Status:** Accepted
- **Date:** 2026-10-28
- **Context:** Marketplace Transaction Governance & Exception Ownership
- **Deciders:** Igor Grybek (Systems Architect, Arxa Group)

## Context & Problem Statement
In activity booking platforms, transactions involve multiple asynchronous events: slot reservation, customer payment pre-authorization, organizer confirmation, cancellations within policy windows, and post-service payouts. Ad-hoc boolean flags in database rows (`is_paid`, `is_cancelled`) frequently drift into contradictory states (e.g. `is_paid = true` AND `is_cancelled = true` while capacity remains locked), resulting in double-booking or failed payouts.

## Decision Drivers
1. **Mathematical State Integrity:** The booking state must reside in exactly one valid state at any timestamp.
2. **Strict Transition Guards:** Only authorized operational events may trigger transitions.
3. **Atomic Inventory Control:** Slot capacity decrements and releases must be transactionally bound to state transitions.

## Decision Outcome
Chosen Option: **Deterministic Finite State Automaton (FSM)**.
The lifecycle is defined by states $\mathcal{S}$ and transition function $\delta(s, e) \to s'$:
$$\mathcal{S} = \{ \text{PUBLISHED}, \text{RESERVED}, \text{PENDING\_PAYMENT}, \text{CONFIRMED}, \text{PAYMENT\_FAILED}, \text{CANCELLED}, \text{REFUNDED}, \text{COMPLETED} \}$$
Invalid transitions (e.g. attempting to cancel an already refunded booking or capturing funds on an expired reservation) are deterministically rejected with strict exception codes.
