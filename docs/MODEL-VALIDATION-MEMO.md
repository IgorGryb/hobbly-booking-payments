# Hobbly — validation and decision memo

Private synthetic study. Eight repository tests cover capacity, key replay/conflict, valid states, cancellation, refund, amount reconciliation and invalid inputs.

## Result

One capture of 5000 cents and one full refund of 5000 cents reconcile to zero net payment flow. Replay produces no second financial event. Cross-booking key reuse is rejected. Cancellation releases the local slot. This is a sequential local reference, not provider settlement.

At the separately declared economic scenario, platform contribution is EUR 2.00 per completed booking and EUR -0.50 when support cost rises. The break-even support cost is EUR 3.50, before fixed costs and tax. Gross booking value is not platform revenue. The pre-recorded cost forecast matches the arithmetic.

## Decision

Continue documenting the service and compare a manual/existing-product baseline. Do not deploy a payment service from this reference. Confirm cancellation terms, support workload, refund fees, settlement rules and access responsibilities before implementation. A favorable unit contribution does not establish total profitability.

## Post-mortem

The earlier implementation replayed a key without checking the booking identity and treated any unknown outcome as failure. Both now reject ambiguous input. Full-refund reconciliation was absent and is now demonstrated. Authorization/capture, concurrency, partial refunds and chargebacks remain explicit gaps; no claim of production safety is made.

Source and handoff: DELIVERY-SPECIFICATION.md, MODEL-CARD.md, the local reference tests and artifacts/management-review.json. The historical technical demo uses a different synthetic pricing scenario; do not combine its numbers with this management scenario.
