from data_context import SimpleDataContext
from repositories import FileUnitOfWork

class DataObjectsCreator:
    _data_context = None
    _unit_of_work = None

    @classmethod
    def get_unit_of_work(cls):
        if cls._unit_of_work is None:
            # Ініціалізація контексту, як у main.py
            cls._data_context = SimpleDataContext()
            if cls._data_context.is_empty():
                cls._data_context.create_testing_data()
            cls._unit_of_work = FileUnitOfWork(cls._data_context)
        return cls._unit_of_work

    @classmethod
    def get_architects(cls):
        uow = cls.get_unit_of_work()
        return uow.architects_repository.get_all()

    @classmethod
    def get_buildings(cls):
        uow = cls.get_unit_of_work()
        return uow.buildings_repository.get_all()