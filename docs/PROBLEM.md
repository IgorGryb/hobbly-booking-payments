# Problem, audience and success criteria

**Problem.** Can a narrow booking flow maintain valid states, inventory and payment idempotency through happy-path and failure scenarios?

**Audience.** Product and engineering stakeholders assessing a marketplace transaction design.

**Success criterion.** The listing-to-capture flow works, duplicate payment requests are idempotent, failed payments preserve a valid booking state and unit economics remain explicit assumptions.

Out of scope: production deployment, client outcomes, regulatory approval and any claim not present in the evidence manifest.
