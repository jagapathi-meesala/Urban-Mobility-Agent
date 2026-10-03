import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from contracts.tool_contract import ToolContract

CONTRACT = ToolContract(
    required=["mode", "availability", "delay_minutes", "occupancy_percent"],
    properties={"mode":"string", "availability":"string", "delay_minutes":"number", "occupancy_percent":"number"},
)

def analyze(payload):
    CONTRACT.validate(payload)
    delay = payload["delay_minutes"]
    occupancy = payload["occupancy_percent"]
    if delay < 0 or not 0 <= occupancy <= 100:
        raise ValueError("delay_minutes must be >= 0 and occupancy_percent must be between 0 and 100")
    availability = payload["availability"].strip().lower()
    if availability not in {"available", "limited", "unavailable"}:
        raise ValueError("availability must be available, limited, or unavailable")
    if availability == "unavailable": status = "unavailable"
    elif delay > 30 or occupancy >= 90: status = "high_constraint"
    elif delay > 10 or occupancy >= 70 or availability == "limited": status = "moderate_constraint"
    else: status = "normal"
    return {"mode": payload["mode"], "status": status, "delay_minutes": delay, "occupancy_percent": occupancy}

if __name__ == "__main__":
    import json, sys
    print(json.dumps(analyze(json.loads(sys.stdin.read()))))
