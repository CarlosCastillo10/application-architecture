from flask import abort, jsonify
from flask_negotiate import produces
from src.repository.course_student_repository import CourseStudentRepository
from src.resource.course_student import blueprint


course_student_repository = CourseStudentRepository()


@blueprint.route('/course/<int:id>', methods=['GET'])
@produces('application/json')
def get_course_by_id(id):
    try:
        course = course_student_repository.search_course_by_id(id)
        if course:
            return jsonify(course), 200
    except: abort(404)


@blueprint.route('/course/<int:id>/students', methods=['GET'])
@produces('application/json')
def get_students_by_course(id):
    students = course_student_repository.get_students_by_course(id)
    if students:
        return jsonify(students), 200
    abort(404)


@blueprint.route('/student/<int:id>', methods=['GET'])
@produces('application/json')
def get_student_by_id(id):
    try:
        student = course_student_repository.search_student_by_id(id)
        if student:
            return jsonify(student), 200
    except: abort(404)


@blueprint.errorhandler(406)
def handle_406_error(e):
    return ("""
        <h1> Encabezado no aceptable</h1><br>
        El recurso identificado solo es capaz de de soportar clientes que acepten <b>application/json</b>
    """)
