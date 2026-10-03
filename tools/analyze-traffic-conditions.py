import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from contracts.tool_contract import ToolContract
CONTRACT = ToolContract(required=["average_speed_kmh", "reference_speed_kmh", "incidents"], properties={"average_speed_kmh":"number", "reference_speed_kmh":"number", "incidents":"number"})
def analyze(payload):
    CONTRACT.validate(payload)
    speed, ref, incidents = payload["average_speed_kmh"], payload["reference_speed_kmh"], payload["incidents"]
    if speed < 0 or ref <= 0 or incidents < 0 or int(incidents) != incidents:
        raise ValueError("invalid traffic inputs")
    ratio = speed / ref
    if ratio < 0.4 or incidents >= 3: condition = "severe"
    elif ratio < 0.7 or incidents >= 1: condition = "congested"
    elif ratio < 0.9: condition = "moderate"
    else: condition = "free"
    return {"speed_ratio": round(ratio, 4), "incident_count": int(incidents), "condition": condition}
if __name__ == "__main__":
    import json, sys
    print(json.dumps(analyze(json.loads(sys.stdin.read()))))
