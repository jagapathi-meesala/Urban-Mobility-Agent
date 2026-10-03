# Explainability

## Inputs and Data Sources

The Urban Mobility Agent accepts only structured information explicitly supplied by the caller.

### Input Requirements

The agent validates required fields, data types, numeric constraints, and unexpected fields before executing a tool.

### Data Sources

The core implementation uses caller-provided mobility, traffic, and trip-option data. It does not silently retrieve external traffic, GPS, mapping, transit, or location data.

### Failure Handling

Invalid or incomplete input is rejected with a structured validation error. Missing information is not fabricated or inferred.

## Decision and Reasoning

All core decisions are deterministic and based only on validated input values.

### Rules Applied

`analyze-mobility-status` evaluates:
- mobility mode
- availability
- delay
- occupancy

`analyze-traffic-conditions` evaluates:
- average speed
- reference speed
- incident count

`plan-mobility-option` evaluates:
- supplied mobility options
- supplied weights
- normalized time
- normalized cost
- normalized congestion

### Expected Outputs

The tools return structured classifications, calculations, or comparisons derived from the supplied input.

### Explainability

Each result can be traced to the input values and deterministic rules used by the corresponding tool.

### Determinism

The same valid input produces the same output. No random values or hidden external services are used.

## Limits and Constraints

The agent does not provide live traffic information, live public-transit availability, GPS positioning, external map routes, or independently verified transportation data.

### Constraints

Results depend on the quality and completeness of caller-provided data.

### Known Issues

Rule-based classifications may not represent rapidly changing real-world transportation conditions.

### Unsupported Behavior

The agent does not:
- fabricate traffic measurements
- fabricate transit availability
- invent routes
- invent travel times
- invent costs
- invent congestion values
- control vehicles
- control traffic signals
- control transportation infrastructure

## Tool Documentation

## analyze-mobility-status

### Inputs

Required:
- `mode`
- `availability`
- `delay_minutes`
- `occupancy_percent`

### Data Sources

All values are supplied by the caller.

### Decision

The tool evaluates availability, delay, occupancy, and mobility mode using deterministic rules.

### Outputs

Returns a structured mobility-status assessment and supporting values.

### Failure Handling

Rejects missing fields, invalid types, invalid numeric values, and unexpected fields.

### Limits

The result describes only the supplied mobility measurements and is not a live observation.

## analyze-traffic-conditions

### Inputs

Required:
- `average_speed_kmh`
- `reference_speed_kmh`
- `incidents`

### Data Sources

All traffic indicators are supplied by the caller.

### Decision

The tool compares average speed with reference speed and considers the supplied incident count.

### Outputs

Returns calculated traffic indicators and the resulting traffic assessment.

### Failure Handling

Rejects missing fields, invalid types, invalid speed values, and unexpected fields.

### Limits

The tool cannot independently verify the freshness or accuracy of supplied traffic data.

## plan-mobility-option

### Inputs

Required:
- `options`
- `weights`

Each option contains caller-supplied mobility attributes.

### Data Sources

Only caller-provided options and weights are used.

### Decision

The tool normalizes supplied time, cost, and congestion values and calculates a deterministic weighted comparison.

### Outputs

Returns evaluated mobility options and their calculated comparison values.

### Failure Handling

Rejects missing fields, malformed option arrays, invalid weights, invalid option values, and unexpected fields.

### Limits

The tool compares only the options supplied by the caller. It does not discover or verify real-world transportation availability.

## Traceability

Every result is derived from explicit input values and deterministic processing rules.

## Transparency

The agent distinguishes between:
1. caller-provided inputs
2. calculated values
3. rule-based classifications
4. documented limitations

The agent does not claim to have collected external evidence when no external source was used.

## Reproducibility

Core tool execution is deterministic and reproducible with identical valid inputs.

## Safety and Scope

The agent provides analytical mobility support only. It does not autonomously operate vehicles, traffic signals, or transportation infrastructure.

Human operators remain responsible for interpreting the results and making operational decisions.
