from flask import Blueprint, render_template, request
from models.model_dropdown import model_dropdown

main = Blueprint('dropdown_bp', __name__)


@main.route('/')
def Index():
    departamentos = model_dropdown.get_data()
    datadepart = []
    for departamento in departamentos:
        deparDic = {
            'co_ubigeo': departamento.co_ubigeo,
            'de_ubigeo': departamento.de_ubigeo,
        }
        datadepart.append(deparDic)
    return render_template('index.html', departamentos=datadepart)

@main.route('/cities', methods=["POST", "GET"])
def cities():
    if request.method == 'POST':
        depart_id = request.form['co_ubigeo']

        cities = model_dropdown.get_datacity(depart_id)
        datacity = []
        for city in cities:
            citydic = {
                'co_city': city.id_city,
                'de_city': city.city
            }
            datacity.append(citydic)
    return datacity