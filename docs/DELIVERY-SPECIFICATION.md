# Hobbly — transaction service operating specification

Private design study. The product hypothesis is a booking service that connects organizers and customers while making exceptions, payment states and service costs visible. No live payment integration, customer base or regulatory authorization is claimed.

## Business and product model

Organizer: publishes an offering, price and capacity, confirms service delivery and handles organizer-side cancellation. Customer: selects availability, books, pays and requests support or cancellation. Platform operations: reconciles states and exceptions. A payment provider would execute money movement under a separately agreed commercial and compliance model. Platform custody of funds is not assumed.

Potential revenue is a fee or take rate, not gross booking value. The reference economic case uses a synthetic EUR 50 booking and 10% take rate, giving EUR 5 platform revenue. Deduct EUR 1 payment cost, EUR 1.50 support and EUR 0.50 expected loss: EUR 2 contribution before fixed costs and tax. At EUR 4 support cost the contribution becomes EUR -0.50. These are assumptions, not observed transactions or a pricing recommendation.

Alternatives: manual scheduling plus an existing payment link; an existing booking product; a custom integrated service. Begin with the simplest approach that meets capacity, cancellation and reconciliation requirements. A new platform is justified only when differentiation and net economics survive a real operational comparison.

## State and responsibility contract

| Event | Required state/control | Result | Proposed owner |
|---|---|---|---|
| Publish listing | Integer minor-unit price, positive capacity, organizer mandate | Bookable offering | Organizer |
| Reserve | Listing exists; capacity available | Pending payment, slot held | Booking service |
| Capture | Pending payment; unique request key | Confirmed booking and captured amount | Payment orchestration |
| Payment failure | Valid simulated failure outcome | Payment failed; hold remains until cancelled | Support/operations |
| Cancel | Pending, failed or confirmed booking | Cancelled; capacity released | Authorized service operator |
| Full refund | Cancelled booking with captured payment | One refund of captured amount | Payment operations |
| Replay request | Same key, same booking and outcome | Same result; no second capture/refund | Payment orchestration |
| Conflicting key | Different booking/outcome | Reject; investigate | Operations |

The reference has no hold timeout, customer authentication, partial refund, retry-after-failure workflow, authorization/capture split, settlement schedule or chargeback process. Those are specified next-design decisions, not silently implied functions. Production roles must enforce access rights; named owners here are proposed functions.

## Reconciliation and exception handling

Keep booking, payment, refund and settlement records separate. Gross captured less gross refunded is a payment-flow measure, not revenue or profit. Reconcile provider events to internal request IDs, amounts, currency and state; unresolved differences remain an exception queue with owner and timestamp. Never mark a refund paid solely because an internal request was accepted.

The local reference simulates capture and full refund and checks their aggregate identity. It does not reconcile a real provider statement. Concurrent requests require transactional reservation, unique event processing and race-condition tests before operational use. A support agent must not manufacture a successful payment state to resolve a customer complaint.

## Data and technology design

Listing: ID, organizer, product terms, slot/capacity, price in minor units, currency and cancellation version. Booking: ID, customer reference, listing/slot, immutable accepted terms, timestamps and status. Payment event: provider event ID, request key, booking, amount, currency, status and audit time. Refund: original payment reference, authorized reason and amount. Avoid storing card credentials; use a suitable provider boundary after separate review.

The current reference stores a deliberately smaller synthetic subset in SQLite. Currency is a fixed demonstration assumption rather than a multi-currency field. Local documentation is canonical; UI, workflow board and dashboard are controlled views. Build/buy review must include transaction fees, refund treatment, payout schedule, support cost, integration effort and vendor exit—not only developer effort.

## Dashboard and management decisions

Show booked versus fulfilled volume separately; capture/refund/reconciliation amounts separately; contribution per completed booking with support and expected-loss assumptions; unresolved exception age and owner; failed-payment and refund rates with denominators. Missing settlement data means unknown, not zero. Refresh on new events or revised assumptions, and retain prior snapshots.

At the synthetic base assumptions support cost must stay below EUR 3.50 per booking for positive contribution before fixed costs. This is an arithmetic boundary, not proof that it is operationally achievable. The simpler alternative may win after acquisition, organizer onboarding, disputes and fixed costs are included.

## Risks, validation and handoff

Material risks: overselling under concurrency; duplicated or misattributed payment requests; cancellation/refund disagreement; uncosted support; mistaken revenue recognition; access/privacy failures. Controls: atomic inventory reservation, request fingerprinting, provider reconciliation, exception ownership and source-backed metrics. The small reference validates only selected sequential state transitions and arithmetic.

Handoff includes the state table, API/event contracts, refund policy decisions, synthetic tests, economic assumptions and a list of unimplemented controls. Pause deployment until the payment/compliance boundary and operational ownership are approved by suitable specialists. This is not a statement of compliance with any jurisdiction's current law.

Interview narrative: connect product economics to the exceptions a service must actually operate. The review found cross-booking idempotency risk and missing refund/reconciliation coverage. The corrected reference demonstrates those controls locally. It does not demonstrate a production marketplace, revenue or customer adoption.
