class Component:
    def __init__(self, id, name, available, missing):
        self.id = int(id)
        self.name = str(name)
        self.available = int(available)
        self.missing = int(missing)

