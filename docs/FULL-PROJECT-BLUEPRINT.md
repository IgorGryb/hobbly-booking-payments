# Full project blueprint — Hobbly — Booking and Payment Vertical Slice

> Controlling management update (2026-10-26): [Management dossier](MANAGEMENT-DOSSIER.md) defines business, product, operating, financial and technology-management scope. User practice and production implementation are not documentary gates. Earlier technical content below remains bounded supporting material, not the full portfolio mandate.


Stable project ID: `PRJ-HOBBLY-PROTOTYPE`  
Status: source-grounded target architecture; implementation and validation backlog  
Evidence boundary: this document specifies what should be built and tested. Only linked test artifacts may support implementation claims.

## 1. Project thesis and decision boundary

The credible core is a narrow organizer workflow in which inventory, booking, payment, cancellation, refund, dispute and payout states remain consistent and economically supportable under failures.

**Decision owner:** organizer operations owner / marketplace product owner  
**Decision supported:** Whether a defined organizer segment should adopt the service and whether each booking/payment exception can be resolved safely and profitably.

### Users and reviewers

- activity organizer
- customer
- support operator
- finance/reconciliation operator
- platform administrator

### In scope for the validated portfolio case

- one organizer segment and geography
- listing-to-payout flow
- test or simulated payment provider
- cancellation/refund/dispute/reconciliation
- unit economics and compliance questions

### Explicitly outside the validated claim

- licensed payment institution claims
- custody or wallet operations
- live card data
- pan-market marketplace launch
- assured GDPR/AML/tax compliance

## 2. Layer architecture and operationalization

`Current` is evidence-based maturity now; `target` is the program gate. It is not a claim that the target has been achieved.

### 2.1 problem-user

**Objective:** Validate one organizer segment and customer job rather than a broad hobby marketplace.

**Operationalization:** Document current tools, booking/payment pain, frequency, exception burden, buyer, end user and stop criteria.

**Required artifact:** segment and job-to-be-done brief  
**Acceptance test:** A representative organizer confirms or rejects the workflow map and ranks the pain against alternatives.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling  
**Maturity:** current L2 → target L5  
**Target Evolution:** Continuous operational telemetry and expanded enterprise integration.

### 2.2 market-business

**Objective:** Test a viable beachhead, value chain and adoption model.

**Operationalization:** Compare marketplace, booking SaaS and payment-infrastructure alternatives; model acquisition, switching cost, trust and network dependence.

**Required artifact:** market/strategy decision memo  
**Acceptance test:** Evidence selects one segment and channel; willingness-to-use and switching objections are recorded.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling  
**Maturity:** current L2 → target L5  
**Target Evolution:** Continuous operational telemetry and expanded enterprise integration.

### 2.3 product-service

**Objective:** Provide an end-to-end service slice from discovery to resolved money movement.

**Operationalization:** Specify role journeys, listing/availability, booking, checkout, confirmation, change, cancellation, refund, dispute, payout and support.

**Required artifact:** service blueprint and product specification  
**Acceptance test:** Each role completes happy and failure journeys; system state and communication remain consistent.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling  
**Maturity:** current L3 → target L5  
**Target Evolution:** Continuous operational telemetry and expanded enterprise integration.

### 2.4 operating-model

**Objective:** Make organizer, support, finance and incident work executable.

**Operationalization:** Assign owners, queues, SLA, evidence and escalation for listing review, schedule change, refund, dispute, reconciliation and payout hold.

**Required artifact:** operations and support runbook  
**Acceptance test:** Tabletop day-in-the-life processes all exception types with no unowned state.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling  
**Maturity:** current L2 → target L5  
**Target Evolution:** Continuous operational telemetry and expanded enterprise integration.

### 2.5 data-technology

**Objective:** Guarantee transactional consistency and auditable provider integration.

**Operationalization:** Model aggregates, relational constraints, outbox/webhook handling, idempotency keys, provider adapter, RBAC, audit log and observability.

**Required artifact:** transactional architecture and executable service  
**Acceptance test:** Concurrency and fault injection preserve money/inventory invariants and allow deterministic reconciliation.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling  
**Maturity:** current L4 → target L5  
**Target Evolution:** Continuous operational telemetry and expanded enterprise integration.

### 2.6 analytical-model

**Objective:** Use product/operations analytics to detect failure and adoption patterns.

**Operationalization:** Define funnel, cohorts, cancellation causes, capacity utilization, exception taxonomy and experiment attribution.

**Required artifact:** analytics specification and organizer dashboard  
**Acceptance test:** Synthetic instrumentation is verified, then one observed workflow produces interpretable funnel/exception data.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling  
**Maturity:** current L1 → target L5  
**Target Evolution:** Continuous operational telemetry and expanded enterprise integration.

### 2.7 finance-economics

**Objective:** Demonstrate sustainable unit economics without confusing GMV with revenue.

**Operationalization:** Model price, GMV, take rate, processor fee, refund/chargeback, support, CAC, retention, payout timing, working capital and cash risk.

**Required artifact:** unit-economics and cash-timing model  
**Acceptance test:** Sensitivity reveals break-even transaction value/volume and downside conditions before a go decision.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling  
**Maturity:** current L2 → target L5  
**Target Evolution:** Continuous operational telemetry and expanded enterprise integration.

### 2.8 risk-security-compliance

**Objective:** Identify regulatory perimeter and secure checkout/organizer access.

**Operationalization:** Maintain jurisdictional questions for payment roles, consumer rights, privacy, KYC/AML, tax and safeguarding; threat-model accounts, webhooks and support actions.

**Required artifact:** risk, security and compliance questions pack  
**Acceptance test:** Security tests pass and a qualified reviewer classifies open legal questions; no compliance claim is inferred.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling  
**Maturity:** current L2 → target L5  
**Target Evolution:** Continuous operational telemetry and expanded enterprise integration.

### 2.9 delivery-governance

**Objective:** Control service and money-state changes.

**Operationalization:** Use ADRs, state-transition review, release checklist, incident severity, reconciliation sign-off and post-mortem ownership.

**Required artifact:** delivery/release governance pack  
**Acceptance test:** One simulated release and incident follow change, rollback, reconciliation and learning procedures.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling  
**Maturity:** current L3 → target L5  
**Target Evolution:** Continuous operational telemetry and expanded enterprise integration.

### 2.10 evidence-validation-publication

**Objective:** Present a working slice without overstating market or compliance readiness.

**Operationalization:** Bind claims to tests, synthetic-data disclosure, interview evidence, economics assumptions and expert questions.

**Required artifact:** evidence dossier and validated case study  
**Acceptance test:** All claims distinguish implemented state, model estimate and open regulatory question; user approves publication.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling  
**Maturity:** current L2 → target L6  
**Target Evolution:** Continuous operational telemetry and expanded enterprise integration.

## 3. Operating state model

### Normal states

`organizer onboarded → listing drafted → listing approved → slot published → reservation held → booking pending → payment authorized → captured or failed → service delivered or cancelled → refund/dispute → reconciled → payout released → closed`

Every transition must record actor, timestamp, input state, output state, decision/evidence reference and exception reason when applicable.

### Required exception paths

- double booking
- expired reservation
- duplicate webhook
- late cancellation
- partial refund
- chargeback
- payout hold
- schedule change
- organizer no-show
- provider outage

## 4. Technical and quality envelope

### Non-functional requirements

- idempotent money-changing commands
- money and inventory invariants
- auditable state transitions
- no raw card data
- role separation
- reconciliation completeness
- recoverable provider failures

### Metrics tree

- booking conversion
- payment success
- double-booking rate
- refund and dispute rate
- time to reconcile
- support cases per booking
- organizer retention
- GMV and take rate
- contribution margin per booking

Metrics must be tagged as observed, modeled or estimated. Modeled economic impact cannot be presented as realized impact.

## 5. Falsifiable hypotheses

1. One organizer segment experiences enough scheduling/payment friction to adopt an integrated workflow.
2. An explicit state machine and idempotency controls prevent duplicate capture and inventory inconsistency in fault tests.
3. Contribution margin remains positive across a preregistered range of payment, refund, support and acquisition costs.

A test that cannot refute a hypothesis is practice or demonstration, not validation.

## 6. Experiment sequence

1. Observe or interview at least one representative organizer and map actual exceptions before extending features.
2. Run concurrency, duplicate webhook, timeout, refund and dispute tests against the transactional model.
3. Simulate cohorts and unit economics under pessimistic/base/upside assumptions with break-even thresholds.
4. Have a payment/compliance practitioner review the questions register without treating it as legal advice.

The prediction, threshold and interpretation owner must be recorded before each result. Failed or inconclusive tests remain in the evidence bundle.

## 7. Source-to-practice coverage

| Mapping | Layer | Course | Archive state | Practice/test | Evidence target |
|---|---|---|---|---|---|
| MOD-SPEC | business | FinTech: Foundations, Payments, and Regulations | manifest-complete | map value chain and payment actors | business architecture |
| MOD-SPEC | governance | FinTech Law and Policy | manifest-complete | create jurisdictional questions register | risk/compliance memo |
| MOD-SPEC | technology | Introduction to Relational Databases (RDBMS) | manifest-complete | normalize booking/payment schema and constraints | schema plus tests |
| MOD-SPEC | technology | Introduction to Software Engineering | manifest-complete | write component boundaries and test strategy | technical specification |
| MOD-SPEC | technology | Introduction to Software, Programming, and Databases | manifest-complete | implement transactional service slice | code evidence |
| MOD-SPEC | governance | Application Security for Developers and DevOps Professionals | manifest-complete | threat-model checkout and organizer access | security report |
| MOD-SPEC | governance | Introduction to Cybersecurity Essentials | manifest-complete | define data and credential controls | control checklist |
| MOD-SPEC | operations | Introduction to Project Management | manifest-complete | map organizer/customer/support swimlanes | service blueprint |
| MOD-SPEC | operations | Project Management Capstone | manifest-complete | run release and post-mortem exercise | delivery dossier |
| MOD-SPEC | business | Corporate & Business Strategy | manifest-complete | select beachhead and alternatives | market decision memo |
| MOD-SPEC | business | Developing Data Products | manifest-complete | build organizer operations dashboard | product artifact |
| MOD-SPEC | finance-risk | Financial Acumen for Non-Financial Managers | manifest-complete | construct unit-economics bridge | financial model |
| MOD-SPEC | finance-risk | Introduction to Corporate Finance | manifest-complete | model working-capital and funding implications | finance memo |
| MOD-SPEC | business | Ext-20 — Foundations of Product Strategy | manifest-incomplete | use only as a topic checklist until materials are supplemented | gap record |

All rows above currently mean source routing. They become competence evidence only after the stated practice/test is executed and recorded.

## 8. Artifact backlog and gates

| Artifact ID | Layer | Deliverable | Current → target | Definition of Done |
|---|---|---|---:|---|
| ART-HOBBLY-01 | problem-user | segment and job-to-be-done brief | L2 → L5 | A representative organizer confirms or rejects the workflow map and ranks the pain against alternatives. |
| ART-HOBBLY-02 | market-business | market/strategy decision memo | L2 → L5 | Evidence selects one segment and channel; willingness-to-use and switching objections are recorded. |
| ART-HOBBLY-03 | product-service | service blueprint and product specification | L3 → L5 | Each role completes happy and failure journeys; system state and communication remain consistent. |
| ART-HOBBLY-04 | operating-model | operations and support runbook | L2 → L5 | Tabletop day-in-the-life processes all exception types with no unowned state. |
| ART-HOBBLY-05 | data-technology | transactional architecture and executable service | L4 → L5 | Concurrency and fault injection preserve money/inventory invariants and allow deterministic reconciliation. |
| ART-HOBBLY-06 | analytical-model | analytics specification and organizer dashboard | L1 → L5 | Synthetic instrumentation is verified, then one observed workflow produces interpretable funnel/exception data. |
| ART-HOBBLY-07 | finance-economics | unit-economics and cash-timing model | L2 → L5 | Sensitivity reveals break-even transaction value/volume and downside conditions before a go decision. |
| ART-HOBBLY-08 | risk-security-compliance | risk, security and compliance questions pack | L2 → L5 | Security tests pass and a qualified reviewer classifies open legal questions; no compliance claim is inferred. |
| ART-HOBBLY-09 | delivery-governance | delivery/release governance pack | L3 → L5 | One simulated release and incident follow change, rollback, reconciliation and learning procedures. |
| ART-HOBBLY-10 | evidence-validation-publication | evidence dossier and validated case study | L2 → L6 | All claims distinguish implemented state, model estimate and open regulatory question; user approves publication. |

### External validation required

- representative organizer workflow review
- payments/security practitioner review
- jurisdiction-specific legal and tax questions review

## 9. Integrated delivery sequence

1. Confirm problem, decision owner, user and anti-scope; record the user's own explanation.
2. Freeze approved sources/data and record hashes, permissions and proxy limitations.
3. Pre-register hypotheses, predictions, thresholds, alternatives and falsification conditions.
4. Complete guided practice from the selected courses and save its independent output.
5. Implement the vertical slice with explicit normal and exception states.
6. Compare against baseline; run negative, security, data-quality and sensitivity tests.
7. Review business, operations, finance and governance artifacts with the appropriate role.
8. Correct model, assumptions, dependent documents and evidence manifests.
9. Ask the user to interpret the result and choose continue, pause, pivot, stop or complete.
10. Only after acceptance, regenerate case study, PDF and private web version and run a claim audit.

## 10. Publication claim boundary

Allowed now: the narrow technical baseline exists and its local tests passed.  
Not allowed now: production readiness, market adoption, realized economic impact, legal compliance, client result or broad platform implementation.  
Allowed later: only statements backed by a versioned artifact, test result, reviewer record and evidence-manifest entry.

## 11. User gates

The user participates before irreversible narrowing, before a material test, when interpreting the result and before publication. The minimum prompts are:

- explain the problem and expected mechanism in your own words;
- predict the result and name a falsifying observation;
- interpret differences between baseline, model and judgment;
- choose `continue`, `pause`, `pivot`, `stop` or `complete`;
- state what changed in your understanding.
