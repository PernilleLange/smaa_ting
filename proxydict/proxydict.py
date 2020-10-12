from types import MappingProxyType

class ProxyDict:
    def __init__(self, intake):
        self.intake = MappingProxyType(intake)

    def keys(self):
        return self.intake.keys()

    def __str__(self):
        return f'ProxyDict({self.intake})'

    def __getitem__(self, item):
       return self.intake[item]

    def __len__(self):
        return len(self.intake)

    def items(self):
        return self.intake.items()

    def values(self):
        return self.intake.values()

    def get(self, key, default = None):
        return self.intake.get(key, default)

    def __iter__(self):
        return iter(self.intake)

    def __eq__(self, other):
        return self.intake == other

