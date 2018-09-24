from flask import Flask
from flask_restful import Api


def create_app():
    """
    Create flask application instance using the factory pattern.
    http://flask.pocoo.org/docs/1.0/patterns/appfactories/
    """
    app = Flask(__name__)
    # app.config.from_pyfile(config_filename)

    register_api(app)

    return app


def register_api(app):
    api = Api(app)

    from api.resources.currency import Currency
    api.add_resource(Currency, '/api/quotes/<string:currency>')

    from api.resources.quotes import Quotes
    api.add_resource(Quotes, '/api/quotes')
