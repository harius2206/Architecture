from data_context import SimpleDataContext
from repositories import FileUnitOfWork
from entities import Architect, Building
from extensions import EnumerableMethods


def study_uow():
    print("--- StudyUOW Architecture Project ---")

    context = SimpleDataContext()
    # Саме тут виникала помилка через відсутність методу в data_context.py
    if context.is_empty():
        print("Контекст порожній, створюємо тестові дані...")
        context.create_testing_data()

    uow = FileUnitOfWork(context)

    print(EnumerableMethods.to_line_list(uow.architects_repository.get_all(), "Список архітекторів"))
    print(EnumerableMethods.to_line_list(uow.buildings_repository.get_all(), "Список будівель"))

    new_arch = Architect("Norman Foster", "UK-777")
    uow.architects_repository.add(new_arch)

    new_build = Building("Gherkin", "London", new_arch.id, 47000.0)
    uow.buildings_repository.add(new_build)

    print("\nПісля додавання нових об'єктів:")
    print(EnumerableMethods.to_line_list(uow.architects_repository.get_all(), "Архітектори"))

    uow.save()


def load_and_check():
    print("\n--- Перевірка завантаження зі збереженого файлу ---")
    new_context = SimpleDataContext()
    new_uow = FileUnitOfWork(new_context)
    print(EnumerableMethods.to_line_list(new_uow.architects_repository.get_all(), "Завантажені архітектори"))


if __name__ == "__main__":
    study_uow()
    load_and_check()