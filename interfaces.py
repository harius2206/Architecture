from abc import ABC, abstractmethod
from typing import List, Optional

class IArchitectsRepository(ABC):
    @abstractmethod
    def get_all(self) -> List: pass
    @abstractmethod
    def get_by_id(self, id: int): pass
    @abstractmethod
    def add(self, item): pass
    @abstractmethod
    def delete(self, id: int): pass

class IBuildingsRepository(ABC):
    @abstractmethod
    def get_all(self) -> List: pass
    @abstractmethod
    def add(self, item): pass

class IUnitOfWork(ABC):
    @property
    @abstractmethod
    def architects_repository(self) -> IArchitectsRepository: pass
    @property
    @abstractmethod
    def buildings_repository(self) -> IBuildingsRepository: pass
    @abstractmethod
    def save(self): pass