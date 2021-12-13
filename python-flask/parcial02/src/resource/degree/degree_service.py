from flask import abort, jsonify
from flask_negotiate import produces
from src.repository.degree_repository import DegreeRepository
from src.resource.degree import blueprint


degree_repository = DegreeRepository()


@blueprint.route('/degree/<int:id>', methods=['GET'])
@produces('application/json')
def get_degree_by_id(id):
    try:
        degree = degree_repository.search_degree_by_id(id)
        if degree:
            return jsonify(degree), 200
    except: abort(404)


@blueprint.route('/degree/<int:id>/courses', methods=['GET'])
@produces('application/json')
def get_courses_by_degree(id):
    try:
        courses = degree_repository.get_courses_by_degree(id)
        if courses:
            return jsonify(courses), 200
    except: abort(404)


@blueprint.errorhandler(406)
def handle_406_error(e):
    return ("""
        <h1> Encabezado no aceptable</h1><br>
        El recurso identificado solo es capaz de de soportar clientes que acepten <b>application/json</b>
    """)
