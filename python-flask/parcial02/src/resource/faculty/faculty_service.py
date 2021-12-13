from flask import abort, jsonify
from flask_negotiate import produces
from src.repository.faculty_repository import FacultyRepository
from src.resource.faculty import blueprint


faculty_repository = FacultyRepository()


@blueprint.route('/faculty/<int:id>', methods=['GET'])
@produces('application/json')
def get_faculty_by_id(id):
    try:
        faculty = faculty_repository.search_faculty_by_id(id)
        if faculty:
            return jsonify(faculty), 200
    except: abort(404)


@blueprint.route('/faculty/<int:id>/departments', methods=['GET'])
@produces('application/json')
def get_departments_by_faculty(id):
    try:
        departments = faculty_repository.get_departments_by_faculty(id)
        if departments:
            return jsonify(departments), 200
    except: abort(404)


@blueprint.errorhandler(406)
def handle_406_error(e):
    return ("""
        <h1> Encabezado no aceptable</h1><br>
        El recurso identificado solo es capaz de de soportar clientes que acepten <b>application/json</b>
    """)