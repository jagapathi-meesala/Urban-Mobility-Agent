import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from contracts.tool_contract import ToolContract
CONTRACT = ToolContract(required=["options", "weights"], properties={"options":"list", "weights":"object"})
def plan(payload):
    CONTRACT.validate(payload)
    options, weights = payload["options"], payload["weights"]
    if not options or not all(isinstance(o, dict) for o in options): raise ValueError("options must be a non-empty list of objects")
    if set(weights) != {"time", "cost", "congestion"}: raise ValueError("weights must contain time, cost, congestion")
    if any(not isinstance(v, (int,float)) or isinstance(v,bool) or v < 0 for v in weights.values()): raise ValueError("weights must be non-negative numbers")
    total = sum(weights.values())
    if total <= 0: raise ValueError("weights must have a positive total")
    required = {"name", "time_minutes", "cost", "congestion"}
    for o in options:
        if set(o) != required: raise ValueError("each option must contain exactly name, time_minutes, cost, congestion")
        if o["time_minutes"] < 0 or o["cost"] < 0 or not 0 <= o["congestion"] <= 100: raise ValueError("invalid option values")
    def norm(key):
        vals = [o[key] for o in options]; lo, hi = min(vals), max(vals)
        return {id(o): 0.0 if hi == lo else (o[key]-lo)/(hi-lo) for o in options}
    ns = {k:norm(k) for k in ("time_minutes","cost","congestion")}
    results=[]
    for o in options:
        score = (weights["time"]*ns["time_minutes"][id(o)] + weights["cost"]*ns["cost"][id(o)] + weights["congestion"]*ns["congestion"][id(o)]) / total
        results.append({"name":o["name"], "score":round(score,4)})
    results.sort(key=lambda x:(x["score"], x["name"]))
    return {"options": results, "selected": results[0]["name"]}
if __name__ == "__main__":
    import json, sys
    print(json.dumps(plan(json.loads(sys.stdin.read()))))
