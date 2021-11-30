from flask import Flask
from importlib import import_module


def register_services(app):
    services = ['student']
    for service in services:
        module = import_module('api.service.{}_service'.format(service))
        app.register_blueprint(module.blueprint)


def create_app():
    app = Flask(__name__)
    register_services(app)
    return app
