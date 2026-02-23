from entities import Building

class BuildingBrowsingModel:
    def __init__(self, id: int, title: str, architect_name: str, area: float):
        self.id = id
        self.title = title
        self.architect_name = architect_name
        self.area = area

    @staticmethod
    def from_entity(building: Building, architect_name: str):
        return BuildingBrowsingModel(
            id=building.id,
            title=building.title,
            architect_name=architect_name,
            area=building.area
        )

class BuildingEditingModel:
    def __init__(self, id: int = None, title: str = "", address: str = "", architect_id: int = None, area: float = 0.0, description: str = "", note: str = ""):
        self.id = id
        self.title = title
        self.address = address
        self.architect_id = architect_id
        self.area = area
        self.description = description
        self.note = note

    @staticmethod
    def from_entity(building: Building):
        if not building:
            return None
        return BuildingEditingModel(
            id=building.id,
            title=building.title,
            address=building.address,
            architect_id=building.architect_id,
            area=building.area,
            description=building.description,
            note=building.note
        )

    def to_entity(self) -> Building:
        return Building(
            id=self.id,
            title=self.title,
            address=self.address,
            architect_id=self.architect_id,
            area=self.area,
            description=self.description,
            note=self.note
        )