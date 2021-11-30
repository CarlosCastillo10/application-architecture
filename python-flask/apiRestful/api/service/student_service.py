from flask import jsonify
from api.service import blueprint


@blueprint.route('/')
def index():
    return jsonify({"nombre": "Carlos"})
