from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from config import app_config


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

    return app


def register_api(app):
    """
    Turn the app in an api instance and add the CORS header to it.
    :param app: Flask app
    :return: None
    """
    api = Api(app)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    from api.resources.currency import Currency, Currencies
    api.add_resource(Currency, '/api/currencies/<string:currency>')
    api.add_resource(Currencies, '/api/currencies')
