from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module

db = SQLAlchemy()


def register_extensions(app):
    db.init_app(app)


def register_services(app):
    services = ['knowledge_area', 'faculty', 'department', 'degree', 'course_student']
    for service in services:
        module = import_module('src.resource.{}.{}_service'.format(service, service))
        app.register_blueprint(module.blueprint)


def configure_database(app):

    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app(app_config):
    app = Flask(__name__)
    app.config.from_object(app_config)
    register_extensions(app)
    register_services(app)
    configure_database(app)
    return app
