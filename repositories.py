from interfaces import IArchitectsRepository, IBuildingsRepository, IUnitOfWork
from entities import Architect, Building

class ArchitectsRepository(IArchitectsRepository):
    def __init__(self, collection: list):
        self._collection = collection

    def get_all(self):
        return [Architect(**a) for a in self._collection]

    def get_by_id(self, id: int):
        data = next((a for a in self._collection if a['id'] == id), None)
        return Architect(**data) if data else None

    def add(self, item: Architect):
        new_id = max([a['id'] for a in self._collection], default=0) + 1
        item.id = new_id
        self._collection.append(item.__dict__)

    def delete(self, id: int):
        self._collection[:] = [a for a in self._collection if a['id'] != id]


class BuildingsRepository(IBuildingsRepository):
    def __init__(self, collection: list):
        self._collection = collection

    def get_all(self):
        return [Building(**b) for b in self._collection]

    def get_by_id(self, id: int):
        data = next((b for b in self._collection if b['id'] == id), None)
        return Building(**data) if data else None

    def add(self, item: Building):
        new_id = max([b['id'] for b in self._collection], default=0) + 1
        item.id = new_id
        self._collection.append(item.__dict__)

    def update(self, item: Building):
        for i, b in enumerate(self._collection):
            if b['id'] == item.id:
                self._collection[i] = item.__dict__
                break

    def delete(self, id: int):
        self._collection[:] = [b for b in self._collection if b['id'] != id]


class FileUnitOfWork(IUnitOfWork):
    def __init__(self, data_context):
        self._data_context = data_context
        # Ініціалізуємо репозиторії
        self._architects_repo = ArchitectsRepository(data_context.architects)
        self._buildings_repo = BuildingsRepository(data_context.buildings)

    @property
    def architects_repository(self):
        return self._architects_repo

    @property
    def buildings_repository(self):
        return self._buildings_repo

    def save(self):
        self._data_context.save()