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
    def __init__(self, id: int = None, title: str = "", address: str = "", architect_id: int = None, area: float = 0.0,
                 description: str = "", note: str = ""):
        self.id = id
        self.title = title
        self.address = address
        self.architect_id = architect_id
        self.area = area
        self.description = description
        self.note = note

    def validate(self):
        """Метод валідації даних (Аналог DataAnnotations у C#)"""
        errors = {}

        if not self.title or len(self.title) < 3 or len(self.title) > 70:
            errors['title'] = "Назва повинна містити від 3 до 70 символів"

        if not self.address or len(self.address) < 4 or len(self.address) > 50:
            errors['address'] = "Адреса повинна містити від 4 до 50 символів"

        if not self.architect_id:
            errors['architect_id'] = "Потрібно вибрати архітектора"

        if self.area is None or self.area < 0.1 or self.area > 130094010:
            errors['area'] = "Значення площі повинно бути в межах від 0.1 до 130094010"

        return errors

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