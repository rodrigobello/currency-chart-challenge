import os

from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS

from instance.config import app_config


def create_app(config):
    """
    Create flask application instance using the factory pattern.
    http://flask.pocoo.org/docs/1.0/patterns/appfactories/

    :param config: Configuration Object
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(app_config[config])
    app.config.from_pyfile('config.py')

    register_api(app)
    error_handler(app)

    if config is 'production':
        production_handler(app)

    from api.model import db
    db.init_app(app)

    return app


def register_api(app):
    """
    Turn the app in an api instance and add the CORS header to it.

    :param app: Flask app
    :return: None
    """
    api = Api(app)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    from api.resource import Quotes
    api.add_resource(Quotes, '/api')


def error_handler(app):
    """
    Give the user a feedback when an invalid API endpoint is requested.

    :param app: Flask app
    :return: None
    """

    @app.errorhandler(404)
    def endpoint_not_found(e):
        message = {"message": "This route is not supported."}
        return jsonify(message), 404


def production_handler(app):
    """
    Set heroku env variables when app is in production.

    :param app: Flask app
    :return: None
    """
    production = os.environ.get('PRODUCTION', None)

    if production:
        app.config['CURRENCY_LAYER_KEY'] = os.environ.get('CURRENCY_LAYER_KEY')
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
