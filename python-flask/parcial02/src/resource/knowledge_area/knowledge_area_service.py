from flask import abort, jsonify, request
from flask_negotiate import produces
from src.resource.knowledge_area import blueprint
from src.repository.knowledge_area_repository import KnowledgeAreaRepository


knowledge_area_repository = KnowledgeAreaRepository()


@blueprint.route('/')
def index():
    return """
        <h4>Bienvenido a la resolución del segundo parcial del primer bimestre!</h4> <br>
        No olvides configurar en el encabezado de <b>'Accept=application/json'</b><br>
        La ruta inicial es: <a href={}knowledge-areas>{}knowledge-areas</a>
    """.format(request.url, request.url)


@blueprint.route('/knowledge-areas', methods=['GET'])
@produces('application/json')
def get_knowledge_areas():
    knowledge_areas = knowledge_area_repository.get_knowledge_areas()
    if knowledge_areas:
        return jsonify(knowledge_areas), 200
    abort(404)


@blueprint.route('/knowledge-area/<int:id>', methods=['GET'])
@produces('application/json')
def get_knowledge_area_by_id(id):
    try:
        knowledge_area = knowledge_area_repository.search_knowledge_area_by_id(id)
        if knowledge_area:
            return jsonify(knowledge_area), 200
    except: abort(404)


@blueprint.route('/knowledge-area/<int:id>/faculties', methods=['GET'])
@produces('application/json')
def get_faculties_by_knowledge_area(id):
    try:
        faculties = knowledge_area_repository.get_faculties_by_knowledge_area(id)
        if faculties:
            return jsonify(faculties), 200
    except: abort(404)


@blueprint.errorhandler(406)
def handle_406_error(e):
    return ("""
        <h1>Encabezado no aceptable</h1><br>
        El recurso identificado solo es capaz de de soportar clientes que acepten <b>application/json</b>
    """)
