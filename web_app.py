from flask import Flask, render_template, abort
from infrastructure import DataObjectsCreator

app = Flask(__name__)


# --- Аналог HomeController ---

@app.route('/')
@app.route('/home/index')
def index():
    # Головна сторінка (Завдання 1)
    return render_template('home/index.html', title="Головна")


@app.route('/home/about')
def about():
    # Сторінка "Про сайт" без макета (Завдання 2)
    return render_template('home/about.html')


# --- Аналог ArchitectsController (Завдання 3) ---

@app.route('/architects/info')
def architects_info():
    architects = DataObjectsCreator.get_architects()
    return render_template('architects/info.html.html', objects=architects)


# --- Часткові представлення (Завдання 4) ---

@app.route('/architects/_descriptive_info/<int:id>')
def _descriptive_info(id):
    uow = DataObjectsCreator.get_unit_of_work()
    architect = uow.architects_repository.get_by_id(id)

    if not architect:
        return ""

    # Імітація багаторядкового тексту (наприклад, ліцензія + ім'я)
    description_lines = [
        "Детальна інформація:",
        f"Ім'я: {architect.name}",
        f"Ліцензія: {architect.license_id}"
    ]

    return render_template('shared/_descriptive_info.html', lines=description_lines)


if __name__ == '__main__':
    app.run(debug=True)