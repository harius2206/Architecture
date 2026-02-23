from flask import Flask, render_template, abort
from infrastructure import DataObjectsCreator

app = Flask(__name__)

# --- Аналог HomeController (Завдання 1) ---
@app.route('/')
@app.route('/home/index')
def index():
    return render_template('home/index.html', title="Головна")

# --- Сторінка "Про сайт" без макета (Завдання 2) ---
@app.route('/home/about')
def about():
    return render_template('home/about.html')

# --- Аналог ArchitectsController (Завдання 3) ---
# Файл web_app.py
@app.route('/architects/info')
def architects_info():
    architects = DataObjectsCreator.get_architects()
    # Змініть 'architects/info.html.html' на 'architects/info.html'
    return render_template('architects/info.html', objects=architects)

# --- Часткові представлення (Завдання 4) ---
@app.route('/architects/_descriptive_info/<int:id>')
def _descriptive_info(id):
    uow = DataObjectsCreator.get_unit_of_work()
    architect = uow.architects_repository.get_by_id(id)

    if not architect:
        return ""

    # Формування даних для часткового представлення
    description_lines = [
        "Детальна інформація:",
        f"Ім'я: {architect.name}",
        f"Ліцензія: {architect.license_id}"
    ]

    return render_template('shared/_descriptive_info.html', lines=description_lines)

if __name__ == '__main__':
    app.run(debug=True)