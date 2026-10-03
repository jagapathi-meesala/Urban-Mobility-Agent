class ToolRegistry:
    def __init__(self):
        self._tools = {}

    def register(self, name, fn):
        self._tools[name] = fn

    def get(self, name):
        return self._tools[name]

    def names(self):
        return sorted(self._tools)
