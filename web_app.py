from flask import Flask, render_template, abort
from infrastructure import DataObjectsCreator

app = Flask(__name__)

@app.route('/')
@app.route('/home/index')
def index():
    return render_template('home/index.html', title="Головна")

@app.route('/home/about')
def about():
    return render_template('home/about.html')

@app.route('/architects/info')
def architects_info():
    architects = DataObjectsCreator.get_architects()
    return render_template('architects/info.html', objects=architects)

@app.route('/architects/_descriptive_info/<int:id>')
def _descriptive_info(id):
    uow = DataObjectsCreator.get_unit_of_work()
    architect = uow.architects_repository.get_by_id(id)

    if not architect:
        return ""

    description_lines = [
        "Детальна інформація:",
        f"Ім'я: {architect.name}",
        f"Ліцензія: {architect.license_id}"
    ]

    return render_template('shared/_descriptive_info.html', lines=description_lines)

if __name__ == '__main__':
    app.run(debug=True)