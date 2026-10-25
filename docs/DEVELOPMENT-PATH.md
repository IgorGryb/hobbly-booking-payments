# Source-grounded development path — Hobbly

> Status: enrichment specification. The current executable prototype is a technical baseline, not the finished portfolio case.

## Verified inputs

- canonical concept record: `1. Portfolio/Hobbly Payments/PROJECT-RECORD.md`
- representative internal project documents:
  - `1. Portfolio/Hobbly Payments/Hobbly_Full_Documentation.md`
  - `1. Portfolio/Hobbly Payments/Hobbly Payments 19a9e7860f814fd8827d34ddc6bf03cd.md`
  - `1. Portfolio/Hobbly Payments/HOBBLY Payments Systems (1) 39be5c6f32dc8029872ef2182e97f86a.md`
  - `1. Portfolio/Hobbly Payments/Hobbly_LIBRARY 77a77fbb0e924e818b49b42b26101bf9.md`
- archived courses below were checked for an existing directory and reviewed at syllabus level; selected module materials exist where `materials_state` is complete.
- a certificate record confirms completion provenance only. It does not independently prove the project capability.

## Layers to develop

### Business

Narrow the market to one organizer segment and one customer job. Test organizer willingness to adopt, booking conversion, cancellation behavior, take rate, payment cost, support burden and contribution margin before broad marketplace expansion.

### Technology

Develop explicit listing, availability, reservation, booking, payment, refund and payout aggregates; transactional persistence; idempotent APIs; provider adapters; role-based access; audit log and observability.

### Operations

Map listing review, schedule changes, capacity, reminders, no-shows, cancellations, refunds, disputes, reconciliation, organizer payout, customer support and incident escalation.

### Finance Risk

Model GMV, take rate, processor fees, refunds, chargebacks, CAC, organizer retention, support cost and cash timing. Separate platform economics from safeguarded or regulated funds flows.

### Governance

Create a jurisdiction-specific questions register for payments, consumer rights, data protection, KYC/AML and tax. The prototype may document risks but cannot claim compliance.

## Course-to-practice map

| Layer | Course | Archive state | How it changes the project | Required evidence |
|---|---|---|---|---|
| business | C419-194 — FinTech: Foundations, Payments, and Regulations | manifest-complete; platform-listed | map value chain and payment actors | business architecture |
| governance | C419-050 — FinTech Law and Policy | manifest-complete; platform-listed | create jurisdictional questions register | risk/compliance memo |
| technology | C419-102 — Introduction to Relational Databases (RDBMS) | manifest-complete; platform-listed | normalize booking/payment schema and constraints | schema plus tests |
| technology | C419-103 — Introduction to Software Engineering | manifest-complete; platform-listed | write component boundaries and test strategy | technical specification |
| technology | C419-104 — Introduction to Software, Programming, and Databases | manifest-complete; platform-listed | implement transactional service slice | code evidence |
| governance | C419-063 — Application Security for Developers and DevOps Professionals | manifest-complete; platform-listed | threat-model checkout and organizer access | security report |
| governance | C419-097 — Introduction to Cybersecurity Essentials | manifest-complete; platform-listed | define data and credential controls | control checklist |
| operations | C419-101 — Introduction to Project Management | manifest-complete; platform-listed | map organizer/customer/support swimlanes | service blueprint |
| operations | C419-110 — Project Management Capstone | manifest-complete; platform-listed | run release and post-mortem exercise | delivery dossier |
| business | C419-005 — Corporate & Business Strategy | manifest-complete; platform-listed | select beachhead and alternatives | market decision memo |
| business | C419-131 — Developing Data Products | manifest-complete; platform-listed | build organizer operations dashboard | product artifact |
| finance-risk | C419-195 — Financial Acumen for Non-Financial Managers | manifest-complete; local certificate linked | construct unit-economics bridge | financial model |
| finance-risk | C419-197 — Introduction to Corporate Finance | manifest-complete; local certificate linked | model working-capital and funding implications | finance memo |
| business | Ext-20 — Foundations of Product Strategy | manifest-incomplete; platform-listed | use only as a topic checklist until materials are supplemented | gap record |

## Execution sequence

1. Extend the state machine through cancellation, refund, dispute and payout reconciliation.
2. Create invariant and property tests for inventory, money conservation and idempotency.
3. Interview or simulate one organizer workflow and measure operational exceptions.
4. Build a cohort/unit-economics model with explicit uncertainty and break-even conditions.
5. Produce a compliance-questions memo for expert review, without converting it into legal assurance.

## Readiness rule

The project may return to `productize` only when the selected learning sources have been converted into executed practice, the new test evidence is in the manifest, the limitations are updated and the user has interpreted the result. Unused course material remains provenance, not a portfolio claim.
