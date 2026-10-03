# Explainability

## Inputs and Data Sources
The agent accepts only structured values supplied by the caller. No external live data source is required.

## Decision and Reasoning
### Mobility Status
The status tool classifies supplied mobility indicators using explicit thresholds documented in its implementation.

### Traffic Analysis
Traffic analysis calculates utilization from supplied average speed and reference speed, plus incident impact when supplied.

### Trip Planning
Trip planning compares supplied options using travel time, cost, and congestion score. The resulting score is a calculation, not a claim about real-world conditions.

## Limits and Constraints
- No live traffic or transit lookup.
- No GPS positioning.
- No route generation from maps.
- No fabricated missing values.
- Scores are analytical aids and depend on the supplied inputs.

## Tool Documentation

### analyze-mobility-status
Inputs: mode, availability, delay_minutes, occupancy_percent.

Decision: derives a deterministic status from availability, delay, and occupancy.

Failure handling: rejects missing, invalid, or unexpected fields.

### analyze-traffic-conditions
Inputs: average_speed_kmh, reference_speed_kmh, incidents.

Decision: computes speed ratio and incident count, then assigns a traffic condition.

Failure handling: rejects non-positive reference speed and invalid incident counts.

### plan-mobility-option
Inputs: options, weights.

Decision: normalizes supplied time, cost, and congestion values and calculates a weighted score for each option.

Failure handling: rejects malformed options, invalid weights, and empty option lists.
