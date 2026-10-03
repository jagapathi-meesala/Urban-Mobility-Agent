# Urban Mobility Agent

A framework-independent OpenGAP-compatible agent for analyzing supplied urban mobility information.

## Capabilities
- Analyze mobility status from supplied conditions.
- Analyze traffic conditions using supplied speed, capacity, and incident data.
- Compare mobility options using transparent deterministic scoring.

## Validation

```bash
pytest -q
python3 verification/readiness_audit.py
opengap validate
```

## Limitations
This project does not provide live traffic, public-transit, GPS, routing, or map data. It only analyzes information supplied to its tools.
