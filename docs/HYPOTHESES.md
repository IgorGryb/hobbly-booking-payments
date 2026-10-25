# Hypotheses, prediction and falsification

## Primary hypothesis

The listing-to-capture flow works, duplicate payment requests are idempotent, failed payments preserve a valid booking state and unit economics remain explicit assumptions.

## Prediction recorded before test

The state machine will reject invalid transitions, capture the happy path once and return the same result for a repeated idempotency key.

## Falsification criterion

The prediction is falsified if an invalid transition succeeds, inventory becomes negative, or a repeated key creates a second charge.

## Alternative explanation

A passing result may follow from the deliberately narrow fixture or chosen assumptions rather than general capability. External validity therefore remains unconfirmed.
