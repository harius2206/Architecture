class Architect:
    def __init__(self, name: str, license_id: str, id: int = None):
        self.id = id
        self.name = name
        self.license_id = license_id

    def __str__(self):
        return f"ID: {self.id} | Architect: {self.name} (License: {self.license_id})"

class Building:
    def __init__(self, title: str, address: str, architect_id: int, area: float, description: str = "", note: str = "", id: int = None):
        self.id = id
        self.title = title
        self.address = address
        self.architect_id = architect_id
        self.area = area
        self.description = description
        self.note = note

    def __str__(self):
        return f"ID: {self.id} | Building: {self.title} at {self.address}"