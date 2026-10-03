class PortableAdapter:
    def __init__(self, registry):
        self.registry = registry

    def invoke(self, tool_name, payload):
        return self.registry.get(tool_name)(payload)
