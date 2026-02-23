from flask import Flask, render_template, abort, request, redirect, url_for
from infrastructure import DataObjectsCreator
from models import BuildingBrowsingModel, BuildingEditingModel

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


# --- CRUD Контролер для будівель (Завдання 2-6) ---

@app.route('/buildings_crud/')
def buildings_index():
    uow = DataObjectsCreator.get_unit_of_work()
    buildings = uow.buildings_repository.get_all()
    architects = uow.architects_repository.get_all()

    # Словник для швидкого пошуку імені архітектора за ID
    arch_dict = {a.id: a.name for a in architects}

    browsing_models = [
        BuildingBrowsingModel.from_entity(b, arch_dict.get(b.architect_id, "Невідомо"))
        for b in buildings
    ]
    return render_template('buildings_crud/index.html', models=browsing_models)


@app.route('/buildings_crud/create', methods=['GET', 'POST'])
def buildings_create():
    uow = DataObjectsCreator.get_unit_of_work()

    if request.method == 'POST':
        model = BuildingEditingModel(
            title=request.form.get('title'),
            address=request.form.get('address'),
            architect_id=int(request.form.get('architect_id')),
            area=float(request.form.get('area', 0.0)),
            description=request.form.get('description', ''),
            note=request.form.get('note', '')
        )
        uow.buildings_repository.add(model.to_entity())
        uow.save()
        return redirect(url_for('buildings_index'))

    model = BuildingEditingModel()
    architects = uow.architects_repository.get_all()
    return render_template('buildings_crud/create.html', model=model, architects=architects)


@app.route('/buildings_crud/edit/<int:id>', methods=['GET', 'POST'])
def buildings_edit(id):
    uow = DataObjectsCreator.get_unit_of_work()
    building = uow.buildings_repository.get_by_id(id)
    if not building:
        abort(404)

    if request.method == 'POST':
        model = BuildingEditingModel(
            id=id,
            title=request.form.get('title'),
            address=request.form.get('address'),
            architect_id=int(request.form.get('architect_id')),
            area=float(request.form.get('area', 0.0)),
            description=request.form.get('description', ''),
            note=request.form.get('note', '')
        )
        uow.buildings_repository.update(model.to_entity())
        uow.save()
        return redirect(url_for('buildings_index'))

    model = BuildingEditingModel.from_entity(building)
    architects = uow.architects_repository.get_all()
    return render_template('buildings_crud/edit.html', model=model, architects=architects)


@app.route('/buildings_crud/delete/<int:id>', methods=['GET', 'POST'])
def buildings_delete(id):
    uow = DataObjectsCreator.get_unit_of_work()
    building = uow.buildings_repository.get_by_id(id)
    if not building:
        abort(404)

    if request.method == 'POST':
        uow.buildings_repository.delete(id)
        uow.save()
        return redirect(url_for('buildings_index'))

    model = BuildingEditingModel.from_entity(building)
    return render_template('buildings_crud/delete.html', model=model)


@app.route('/buildings_crud/details/<int:id>')
def buildings_details(id):
    uow = DataObjectsCreator.get_unit_of_work()
    building = uow.buildings_repository.get_by_id(id)
    if not building:
        abort(404)

    architect = uow.architects_repository.get_by_id(building.architect_id)
    architect_name = architect.name if architect else "Невідомо"

    model = BuildingEditingModel.from_entity(building)
    return render_template('buildings_crud/details.html', model=model, architect_name=architect_name)


if __name__ == '__main__':
    app.run(debug=True)