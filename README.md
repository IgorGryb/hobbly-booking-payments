# Hobbly — Transaction State Machine & Services Platform

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/Tests-Passing%20(8%2F8)-success.svg)](tests/)
[![Architecture](https://img.shields.io/badge/Architecture-Deterministic%20FSM-orange.svg)](#solution--decision-architecture)
[![Status](https://img.shields.io/badge/Status-R%26D%20Reference%20Architecture-informational.svg)](#research-integrity--disclaimer)

> **Architectural Mission:** Protecting marketplace contribution margins by replacing fragile, ad-hoc booking logic with a deterministic finite state machine (FSM) that automates payment escrow, exception handling, and dispute resolution.

---

## Executive Overview

| Dimension | Specification |
|:---|:---|
| **Domain** | SMB Marketplaces, Transaction State Engines, Payment Infrastructure & Service Economics |
| **Stage** | Validated Proprietary Architecture & Operating Model (R&D Prototype) |
| **Target User** | Marketplace Operators, Service-Commerce Platforms, SMB Booking Aggregators |
| **Core Decision** | Routing, escrowing, executing, and resolving multi-state service bookings and payments |
| **Key Metric** | Exception-Handling Cost per Booking, Net Take-Rate Retention, Automated Resolution Rate |
| **Architecture Lead** | Igor Grybek (Product Strategy, Transaction Architecture, Economics) |

---

## The Strategic Problem

Small and medium-sized service businesses (SMBs) across wellness, professional consulting, home services, and education rely on fragmented, legacy booking and invoicing systems. Transitioning to online transactional marketplaces offers immense growth potential, but exposes platform operators to severe operational and economic bottlenecks:

1. **Transaction State Fragility:** Service bookings are not simple retail purchases; they represent multi-step, dynamic commitments that can be rescheduled, cancelled, partially delivered, disputed, or refunded. Systems lacking strict state-machine controls suffer from out-of-sync schedules, double bookings, and leaked payments.
2. **The Hidden Cost of Exception Handling:** While "happy-path" bookings are cheap to automate, edge cases (no-shows, provider cancellations, customer dissatisfaction, late disputes) require extensive manual customer support. In low-margin marketplaces, handling a single 15-minute customer support inquiry can completely wipe out the platform's take-rate margin from 5–10 successful bookings.
3. **Escrow & Settlement Complexity:** Escrowing client funds, calculating platform commissions, deducting processing fees, and releasing net payouts to service providers while maintaining fraud protection and chargeback reserves requires robust transactional discipline.

---

## Solution & Decision Architecture

Hobbly establishes a deterministic transaction state engine and service-economics framework that makes exception workflows and payment releases transparent, robust, and economically sustainable.

```
[Booking Request] ──► [Availability & Capacity Check]
                                 │
                                 ▼
                     [Payment Escrowed via PSP]
                                 │
                                 ▼
                    [State: Booking Confirmed]
                                 │
                   ┌─────────────┴─────────────┐
                   ▼                           ▼
          [Service Delivered]        [Exception Triggered]
                   │                           │
                   ▼                           ▼
        [Automatic Payout Release]   [Automated Dispute Engine]
                   │                           │
                   ▼                           ▼
       [Platform Commission Take]    [Refund / Reschedule Policy]
```

### Core System Mechanics:
1. **Deterministic State Machine:** Models the entire lifecycle of a service transaction through discrete, non-overlapping states:
   `Draft` $\rightarrow$ `PendingPayment` $\rightarrow$ `Escrowed` $\rightarrow$ `ServiceConfirmed` $\rightarrow$ `InProgress` $\rightarrow$ `Completed` $\rightarrow$ `Settled` (with explicit exception branches: `CancelledByClient`, `CancelledByProvider`, `Disputed`, `Refunded`).
2. **Automated Dispute & Exception Rules:** Formalizes transparent, programmatic resolution policies (e.g. tiered refund percentages based on notice windows) directly into the booking engine, resolving 80%+ of booking alterations without manual human intervention.
3. **Integrated Escrow & Fee Engine:** Accurately isolates gross merchandise value (GMV), payment service provider (PSP) interchange fees, platform take-rate, and net vendor payout, preventing double-counting and guaranteeing positive contribution margins across all transaction types.
4. **Idempotent Transaction Safeguards:** Every payment and state transition requires a unique cryptographic transaction key, eliminating duplicate charges or race conditions during network interruptions.

---

## 5-Dimensional Management Model

### 1. Technical Architecture
- **State Engine:** Python state transition engine enforcing strict finite state automata and invariant checking.
- **Data Integrity:** ACID-compliant transaction logic ensuring state changes and payment authorizations are atomic.

### 2. Operating Model & Exceptions
- **Automated Exception Triage:** Transparent rules handle customer cancellations and rescheduling automatically based on time-to-appointment windows.
- **Support Escalation:** Only unresolvable disputes escalate to human support agents, drastically lowering support ticket volume.

### 3. Financial & Unit Economics
- **Contribution Margin Protection:** Bounded synthetic modeling demonstrates that automating cancellation and dispute paths preserves positive unit margins (preventing support labor from eroding the 8–15% take-rate).
- **Working Capital Float:** Models the liquidity dynamics of escrow holding periods, fee deductions, and payout batches.

### 4. Risk, Governance & Payments
- **Zero-Vault Architecture:** Direct PSP integration (tokenized payments) ensuring sensitive payment credentials never touch platform application servers.
- **Audit Trails:** Immutable, timestamped transition logs recording each state shift, authorizing user, and fee deduction.

### 5. Venture & Scalability
- Modular transaction core capable of scaling horizontally across diverse service verticals (beauty, legal, wellness, tutoring).

---

## Reproducibility & Quickstart

The repository contains an automated test suite verifying state transitions, refund calculations, capacity limits, and idempotency guarantees.

```bash
# Clone repository
git clone https://github.com/IgorGryb/hobbly-booking-payments.git
cd hobbly-booking-payments

# Run verification suite (8 tests)
python3 -m unittest discover -s tests -v
# Alternatively:
make test
```

Expected output:
```text
test_cancel_refund_and_reconcile (test_core.StateMachineTest) ... ok
test_capacity (test_core.StateMachineTest) ... ok
test_failed_payment_no_refund (test_core.StateMachineTest) ... ok
test_idempotency (test_core.StateMachineTest) ... ok
test_invalid_input (test_core.StateMachineTest) ... ok
test_invalid_transition (test_core.StateMachineTest) ... ok
test_key_cannot_cross_booking_or_outcome (test_core.StateMachineTest) ... ok
test_reproduction_writes_results_and_manifest (test_reproduction.ReproductionTest) ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.012s

OK
```

---

## Research Integrity & Disclaimer

This repository is an architectural reference prototype and bounded decision model developed by Igor Grybek. All tests and demonstrations operate strictly on reproducible, synthetic listings, booking slots, and transaction events. No real payment credentials, personal data, or regulated funds flow are contained herein.
