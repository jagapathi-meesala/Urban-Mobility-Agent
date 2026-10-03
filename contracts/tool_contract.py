class ToolContract:
    def __init__(self, required=None, properties=None):
        self.required = set(required or [])
        self.properties = properties or {}

    def validate(self, data):
        if not isinstance(data, dict):
            raise TypeError("input must be an object")
        missing = self.required - data.keys()
        if missing:
            raise ValueError(f"missing required fields: {sorted(missing)}")
        unexpected = set(data) - set(self.properties)
        if unexpected:
            raise ValueError(f"unexpected fields: {sorted(unexpected)}")
        for key, expected in self.properties.items():
            if key not in data:
                continue
            value = data[key]
            if expected == "number" and (not isinstance(value, (int, float)) or isinstance(value, bool)):
                raise TypeError(f"{key} must be a number")
            if expected == "string" and not isinstance(value, str):
                raise TypeError(f"{key} must be a string")
            if expected == "list" and not isinstance(value, list):
                raise TypeError(f"{key} must be a list")
            if expected == "object" and not isinstance(value, dict):
                raise TypeError(f"{key} must be an object")
