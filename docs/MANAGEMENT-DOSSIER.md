# Hobbly — management and operating dossier

Project: `PRJ-HOBBLY-PROTOTYPE`. Authored 2026-10-26. Status: internally specified design; not a deployed service. Source concept: `SRC-PRJ-HOBBLY-DOC`. Methods: M-SIPOC, M-RACI, M-MOSCOW, M-FURPS, M-FEASIBILITY, M-SCENARIO, M-MEASURE.

## Decision and business model

A booking-service operating model with explicit transaction economics and exception ownership.

**Problem:** A reservation is not operationally complete until capacity, payment, cancellation and settlement states agree.
**Customer / decision user:** Activity organizer and customer
**Payer:** Organizer or transaction commission payer; pricing remains a hypothesis
**Value proposition (hypothesis):** A consistent booking journey and understandable control of capacity, money and service exceptions.

**Alternatives:**

- Manual calendar and bank transfer: suitable baseline at small scale
- Buy booking/payment services: default integration option after due diligence
- Custom payments stack: excluded

**Selected design decision:** Describe the end-to-end service, use simulated payments, and validate state transitions before evaluating commercial integrations.

Market size, paid demand, channel conversion and real service delivery are not established. First access channel is a controlled review with the target decision user. Scale only after the problem and acceptance criteria survive that review.

## Product scope and acceptance

| ID | Must requirement | Acceptance evidence |
|---|---|---|
| HOBBLY-REQ-01 | Capacity and payment state cannot contradict confirmed booking | Reviewer checks the corresponding model/process step; records source, exception and outcome. |
| HOBBLY-REQ-02 | Duplicate event has one financial effect | Reviewer checks the corresponding model/process step; records source, exception and outcome. |
| HOBBLY-REQ-03 | Cancellation/refund has an explicit service owner | Reviewer checks the corresponding model/process step; records source, exception and outcome. |

Should: export a decision memo and traceability view. Could: automate repetitive updates after correctness is established.
**Will not do:** Real money, production regulatory compliance, assumed licensed payment capability.

## Operating model — SIPOC

- Supplier: Organizer, customer and simulated payment provider
- Inputs: Listing, capacity, selected slot, customer instruction and payment event
- Process: Validate listing and available slot → Reserve capacity with expiry → Request and reconcile payment state → Confirm booking or release capacity → Handle cancellation/refund and reconcile settlement
- Outputs: Confirmed or declined reservation, settlement record and exception ticket
- Customer: Activity organizer and customer

### Control and exception handoffs

| Step | Responsible | Accountable | Control / handoff |
|---|---|---|
| 1. Validate listing and available slot | Analyst / process owner | Decision owner | Record input version, output ID and reviewer; exceptions escalate before the next release. |
| 2. Reserve capacity with expiry | Analyst / process owner | Decision owner | Record input version, output ID and reviewer; exceptions escalate before the next release. |
| 3. Request and reconcile payment state | Analyst / process owner | Decision owner | Record input version, output ID and reviewer; exceptions escalate before the next release. |
| 4. Confirm booking or release capacity | Analyst / process owner | Decision owner | Record input version, output ID and reviewer; exceptions escalate before the next release. |
| 5. Handle cancellation/refund and reconcile settlement | Analyst / process owner | Decision owner | Record input version, output ID and reviewer; exceptions escalate before the next release. |

Roles are proposed functions, not claims of an existing staffed organization. Reviewer is consulted; downstream owner is informed. A single person may hold several roles, but cannot claim independent review of their own work.

**Exception policy:** Payment timeout stays pending; repeated callback must not double-charge or double-book. Refund exception has a named finance owner.

## End-to-end operationalization

| Stage | Input | Owner | Method | Tool | Artifact | Gate | Next owner |
|---|---|---|---|---|---|---|---|
| Initiation | Mandate and source record | Decision owner | M-RACI | Obsidian | Problem/mandate brief | Alternative of no action stated | Analyst |
| Analysis | Brief and approved sources | Analyst | M-SIPOC | Obsidian | Source and assumption map | Facts separated from hypotheses | Model owner |
| Modeling | Assumptions and baseline | Model owner | M-SCENARIO | Excel | Economic and operational model | Units, population and perspective explicit | Product owner |
| Design | Model and user needs | Product owner | M-FEASIBILITY | FigJam / local flow | Requirements and data flow | Every Must links to acceptance test | Delivery owner |
| Planning | Requirements and dependencies | Delivery owner | M-MOSCOW | Linear / local backlog | Prioritized handoff plan | Single accountable owner and next action | Implementer or analyst |
| Execution | Approved scope | Analyst / implementer | M-FEASIBILITY | Local documents/model | Controlled artifact version | No undocumented scope expansion | Reviewer |
| Testing | Artifact, baseline and forecast | Reviewer | M-SCENARIO | Excel / targeted tests | Test report | Normal and negative cases documented | Decision owner |
| Evaluation | Results and limitations | Decision owner | M-MEASURE | Dashboard + PowerPoint storyboard | Decision memo | Recommendation conditional on evidence | Change owner |
| Change management | New source, exception or decision | Change owner | M-RACI | Git + local change log | Impact and revised baseline | Dependent outputs marked stale/rechecked | Next stage owner |

Tool configuration is proposed, not connected. Local Markdown/YAML is authoritative. Cloud tools require a separate data-sharing decision. See [toolchain](../../../00.%20ARCHIVE%20SYSTEM/portfolio/TOOLCHAIN-AND-HANDOFF.md).

## Financial and operating economics

Contribution per completed booking = fee revenue - payment cost - support cost - expected refund/dispute loss. Gross merchandise value is not revenue. Capacity, cancellations and failed payments constrain volume.

Estimates must disclose cost population, currency, horizon and baseline. Sensitivity changes one driver or a declared scenario while other external assumptions remain equal. Missing required input makes the result unavailable. No forecast is reported as a realized business result.

## Technology management and build/buy/partner

Keep a source/assumption register, a model layer, a review layer and derived communication outputs. Stable IDs connect them. Access labels travel with the data. Maintain exportable local records and a documented exit path before selecting a hosted service.

Buy or reuse commodity task management, presentation and modeling tools. Build only a narrow calculation or validator when it resolves a decision-critical uncertainty. Partner for specialist legal, domain or security validation when the scope requires it. Proposed interfaces exchange artifact ID, version, owner, status and source IDs; no integration is claimed as implemented.

NFR design: outputs must be traceable and reproducible; invalid inputs must be visible; sensitive data must not leave the approved boundary. Response-time, uptime and capacity targets remain uncalibrated until a real user/process requires them.

## Metrics and dashboard specification

| Metric | Unit | Calculation | Source | Decision |
|---|---|---|---|---|
| Contribution per booking | EUR/booking | fee - payment cost - support - expected losses | unit-economics assumptions | Reprice or change process |
| Booking completion | fraction | confirmed / valid initiated bookings | event log | Inspect abandonment and payment failures |
| Unreconciled settlements | count | settlements lacking matching booking/payment | reconciliation register | Hold settlement and investigate |

Metric owner: process/model owner. Review event: new result, changed assumption or operating incident, not an imposed calendar. For fractions, zero/missing denominator means unavailable. Actual metrics need a defined reporting period and event population; none are invented here.

Dashboard layout: decision/status at top, scenario comparison in the center, assumptions and exceptions below. Use a line chart for time, bars for comparable alternatives, and a table for exact constraints. Do not combine projected and realized values without explicit labeling.

## Validation and risk

**Hypothesis:** Exception handling and transaction economics determine viability more than feature breadth.

**Negative scenario:** Duplicate callback and payment timeout; no double allocation or recognition of uncollected revenue.

**Material limitation:** Synthetic payment state tests do not establish provider integration, fraud prevention or legal compliance.

Validation layers: structural document review; arithmetic/model tests; scenario/exception walkthrough; external validation only when an appropriate recipient participates. Existing technical-baseline tests remain bounded evidence. User practice is optional and not a release gate for documentation.

## Delivery and stop conditions

Sequence: source and mandate → explicit model and handoffs → targeted validation → decision memo → review-ready case study. Continue if the model answers the decision with traceable assumptions. Pivot if the decision or economics changes. Pause if a necessary source is unavailable. Stop if the best supported option is no action or a simpler existing solution.

**Next event-triggered action:** Validate support/refund workload assumptions and compare buy versus partner delivery.

## Presentation storyboard

1. Decision and user problem. 2. Alternatives and source basis. 3. Product and operating model. 4. Economics and scenarios. 5. Architecture and ownership. 6. Validation result and limitations. 7. Recommendation and next decision.

Each slide and dashboard number must point back to this dossier and its model/run. Storyboard is not a delivered slide deck. No public publishing or external application is performed.

## Provenance and authoring boundary

This management model was authored with an AI agent from existing project sources, course materials and the approved user direction. It demonstrates the documented design and review process, not independent proof that the user performed every implementation step. All economic sample cases are synthetic.

## Multidimensional reinforcement and technical depth

Management connects technical/domain depth to product, operating and capital decisions; it does not replace that depth. The following application mappings are candidate design hypotheses, not proven benefits or claims of independent competence.

[Canonical mechanisms and evidence boundaries](../../../00.%20ARCHIVE%20SYSTEM/portfolio/REINFORCEMENT-MAP.yaml). [Full qualification records and source links](../../../00.%20ARCHIVE%20SYSTEM/portfolio/QUALIFICATION-INVENTORY.yaml). Program metadata has been reviewed; module-level support is not asserted for these candidate links.

### RF-03 — Product strategy connected to transaction reliability

**Career anchors:** EXP-PORTFOLIO-2023, EXP-SANTANDER-2022.
**Learning sources (official titles):** From Product Strategy to Product Leadership; Product Marketing & Go-to-Market Strategy; IBM Systems Analyst; IBM Back-End Development; Fintech: Foundations & Applications of Financial Technology.

| Dimension | Proposed application |
|---|---|
| Technical | Booking/payment states, idempotency, failure recovery, role boundaries and event reconciliation. |
| Product | Define the organizer/customer job and a narrow service proposition before adding transaction volume. |
| Operating | Make support, refunds, reconciliation, disputed states and escalation part of the service design. |
| Finance | Contribution per booking includes payment, support and loss assumptions; no gross-volume-as-revenue claim. |

**Reinforcement mechanism (hypothesis):** A product promise becomes operationally credible when state integrity and exception costs are included in pricing and service design.

**Failure/cost of integration:** Growth can increase exception load and destroy contribution; payment-provider dependency remains.

**Comparison to run:** Compare happy-path pricing with a full exception-cost model; test duplicate callbacks, cancellation and payment/booking mismatch.

**Next option and activation condition:** Test a new booking segment only after its support burden and payment-state assumptions are explicit.

### RF-06 — Management metrics backed by financial and data controls

**Career anchors:** EXP-BNP-2025, EXP-SANTANDER-2022.
**Learning sources (official titles):** Microsoft Power BI Data Analyst; Microsoft Power BI Developer and Architect; BI Essentials for Finance Analysts (Power BI Edition); IBM Data Architecture; Business Analytics with Excel.

| Dimension | Proposed application |
|---|---|
| Technical | Metric lineage, schema/grain, denominator, reconciliation, access and stale-data controls. |
| Product | A decision dashboard and memo derived from canonical models, not an independent narrative. |
| Operating | Metric owner handles exceptions and version changes; decision owner accepts the reporting scope. |
| Finance | Separate cash, value, revenue, volume and estimates; define perspective and period before aggregation. |

**Reinforcement mechanism (hypothesis):** Shared definitions connect technical data quality with management interpretation and financial control.

**Failure/cost of integration:** A polished dashboard can conceal incompatible populations or denominators; centralization creates common-mode errors.

**Comparison to run:** Compare dashboard output to underlying records; inject missing/duplicate/stale data and test invalidation.

**Next option and activation condition:** Reuse a metric across projects only when its unit, grain and decision meaning match.

### RF-07 — Advanced technical options with explicit activation conditions

**Career anchors:** EXP-PORTFOLIO-2023.
**Learning sources (official titles):** Algorithms; Probabilistic Graphical Models; Statistical Methods for Computer Science; IBM AI Engineering; IBM DevOps and Software Engineering; Decentralized Finance (DeFi): The Future of Finance; Building AI Cloud Apps with Microsoft Azure.

| Dimension | Proposed application |
|---|---|
| Technical | Algorithmic complexity, probabilistic inference, ML evaluation, reproducible delivery and optional programmable-contract design. |
| Product | A menu of technical options attached to explicit unmet requirements; no automatic blockchain/ML requirement. |
| Operating | Assess skill/resource needs, maintenance, failure recovery, security review and vendor exit before activation. |
| Finance | Compare incremental decision benefit with integration, operating and switching cost; preserve a simpler baseline. |

**Reinforcement mechanism (hypothesis):** Technical breadth supplies alternative solution paths; governance makes selection conditional on a demonstrated bottleneck.

**Failure/cost of integration:** Complexity can exceed the value of the problem; a course does not establish production security or deployability.

**Comparison to run:** Specify a bottleneck first, then benchmark the candidate against the simplest adequate approach with negative and resource-limit cases.

**Next option and activation condition:** Activate one technical extension only when it resolves a material assumption and its cost/risk is justified; otherwise retain as observing.
