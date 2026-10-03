# Explainability

## Inputs

The agent accepts structured input supplied by the caller. It does not retrieve live traffic, transit, GPS, map, or external mobility data.

### Input Requirements

All inputs must match the corresponding tool schema.

The agent uses only values explicitly supplied by the caller. Missing values are not invented or inferred.

### Data Sources

The data source is the caller-provided structured input. No external data source is required for the core implementation.

### Validation

Inputs are validated for required fields, supported types, valid ranges, and unexpected fields before processing.

## Decision

The agent makes deterministic decisions using explicit calculations and rule-based logic.

### analyze-mobility-status

The tool evaluates supplied mobility mode, availability, delay, and occupancy information.

Decision factors:
- availability
- delay in minutes
- occupancy percentage
- supplied mobility mode

The resulting status is derived only from the supplied values.

### analyze-traffic-conditions

The tool evaluates supplied traffic conditions.

Decision factors:
- average speed
- reference speed
- supplied incident information

The tool calculates a speed ratio and incident impact and derives a traffic condition from those values.

### plan-mobility-option

The tool compares caller-provided mobility options.

Decision factors:
- travel time
- cost
- congestion
- caller-supplied weights

The tool normalizes the supplied values and calculates a deterministic weighted score.

### Determinism

Identical valid inputs produce the same result. No random values, hidden external services, or live data are used.

## Limits

- The agent does not provide live traffic information.
- The agent does not access GPS positioning.
- The agent does not query mapping services.
- The agent does not query public-transit APIs.
- The agent does not generate real-world routes from external map data.
- The agent does not infer missing measurements.
- The agent does not fabricate traffic, transit, or mobility conditions.
- Analytical scores depend entirely on the supplied input values.
- Results should not be interpreted as real-time observations unless real-time measurements are explicitly supplied by the caller.
- The agent does not guarantee travel time, traffic conditions, availability, or route feasibility in the real world.

## Failure Handling

Invalid requests are rejected instead of being silently corrected.

Failures include:
- missing required fields
- invalid data types
- values outside supported ranges
- malformed mobility options
- invalid weights
- empty option lists
- unexpected input fields

Errors identify the invalid input condition without fabricating a replacement value.

## Tool Documentation

### analyze-mobility-status

#### Inputs

Required:
- mode
- availability
- delay_minutes
- occupancy_percent

#### Decision

The tool evaluates availability, delay, and occupancy using deterministic rule-based logic and returns a mobility status with supporting information.

#### Outputs

The result contains the derived mobility status and relevant calculated values.

#### Failure Handling

The tool rejects missing, invalid, or unexpected fields.

#### Limits

The result represents only the supplied mobility measurements and does not represent live mobility conditions.

---

### analyze-traffic-conditions

#### Inputs

Required:
- average_speed_kmh
- reference_speed_kmh
- incidents

#### Decision

The tool calculates the relationship between average speed and reference speed and considers the supplied incident information to derive a traffic condition.

#### Outputs

The result contains the calculated traffic indicators and derived traffic condition.

#### Failure Handling

The tool rejects invalid values, non-positive reference speed, malformed incident data, and unexpected fields.

#### Limits

The tool does not obtain traffic conditions from external services and cannot verify whether supplied traffic measurements are current.

---

### plan-mobility-option

#### Inputs

Required:
- options
- weights

Each option contains caller-supplied mobility attributes used for comparison.

#### Decision

The tool normalizes the supplied option values and calculates a deterministic weighted score using the supplied weights.

#### Outputs

The result contains the evaluated mobility options and their calculated comparison scores.

#### Failure Handling

The tool rejects malformed options, invalid weights, missing required values, empty option lists, and unexpected fields.

#### Limits

The comparison is limited to the options and values supplied by the caller. It does not discover additional transportation options or verify real-world availability.

## Traceability

Each decision can be traced to the input values and deterministic rules used by the corresponding tool.

The agent does not use hidden external data for its core decisions.

## Transparency

The agent distinguishes between:
1. caller-provided measurements,
2. calculated values,
3. rule-based classifications, and
4. limitations of the analysis.

It does not present calculated results as independently verified real-world observations.

## Reproducibility

A tool invocation with the same valid inputs produces the same output. This allows results to be reproduced and tested without external services.

## Safety and Scope

The agent is an analytical mobility-support system. It does not autonomously control traffic infrastructure, vehicles, signals, or transportation systems.

Human operators remain responsible for interpreting analytical results and making operational decisions.
