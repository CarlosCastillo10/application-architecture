from api.enconde import EmployeeEncoder
from api.database.data_repository import DataRepository
from flask import abort, request
from flask_negotiate import consumes, produces
from api.service import blueprint
import json

data_repository = DataRepository()


@blueprint.route('/')
def index():
    return "Bienvenido"

@blueprint.route('/students', methods=['GET'])

@produces('application/json')
def get_students():
    students = data_repository.get_all_student()
    if students:
        return json.dumps(students, cls=EmployeeEncoder), 200

    abort(404)


@blueprint.route('/students/filter', methods=['GET'])
@produces('application/json')
def get_student_by_filter():
    students = validate_filter(request.args.to_dict())
    if students:
        return json.dumps(students, cls=EmployeeEncoder), 200
    abort(404)


@blueprint.route('/student/<int:pos>', methods=['GET'])
@produces('application/json')
def get_student_by_post(pos):
    student = data_repository.search_student_by_pos(pos)
    if student:
        return json.dumps(student, cls=EmployeeEncoder), 200
    abort(404)


@blueprint.route('/student', methods=['POST'])
@consumes('application/json')
def post_student():
    try:
        pos = data_repository.add_student(request.get_json())
        return "Location: {}/{}".format(request.url, pos), 201
    except:
        abort(400)


@blueprint.route('/student/<int:pos>', methods=['PUT'])
@consumes('application/json')
def put_student_by_pos(pos):
    try:
        data_repository.update_student(pos, request.get_json())
        return "", 204
    except:
        abort(409)


@blueprint.route('/student/<int:pos>', methods=['DELETE'])
@produces('application/json')
def delete_student_by_pos(pos):
    try:
        data_repository.delete_student(pos)
        return "", 204
    except:
        abort(400)


def validate_filter(query_params):
    key = list(query_params.keys())[0]
    value = query_params[key]
    students = []

    if key == 'name':
        students = data_repository.search_student_by_name(value)

    elif key == 'lastname':
        students = data_repository.search_student_by_lastname(value)

    elif key == 'age':
        students = data_repository.search_student_by_age(int(value))

    return students
