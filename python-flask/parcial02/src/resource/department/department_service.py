from flask import abort, jsonify
from flask_negotiate import produces
from src.repository.department_repository import DepartmentRepository
from src.resource.department import blueprint


department_repository = DepartmentRepository()


@blueprint.route('/department/<int:id>', methods=['GET'])
@produces('application/json')
def get_department_by_id(id):
    try:
        department = department_repository.search_department_by_id(id)
        if department:
            return jsonify(department), 200
    except: abort(404)


@blueprint.route('/department/<int:id>/degrees', methods=['GET'])
@produces('application/json')
def get_degrees_by_department(id):
    try:
        degrees = department_repository.get_degrees_by_department(id)
        if degrees:
            return jsonify(degrees), 200
    except: abort(404)


@blueprint.errorhandler(406)
def handle_406_error(e):
    return ("""
        <h1> Encabezado no aceptable</h1><br>
        El recurso identificado solo es capaz de de soportar clientes que acepten <b>application/json</b>
    """)