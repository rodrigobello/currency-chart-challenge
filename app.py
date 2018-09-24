from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

quotes = {
    'USD': {
        "updated": "",
        "quotes": [],
    },
    'ARS': {
        "updated": "",
        "quotes": [],
    },
    'EUR': {
        "updated": "",
        "quotes": [],
    },
}


class Currency(Resource):
    def get(self, currency):
        try:
            return quotes[currency]
        except KeyError:
            return {'message': 'Currency not available.'}, 404


class Quotes(Resource):
    def get(self, currency):
        return quotes


api.add_resource(Currency, '/api/quotes/<string:currency>')
api.add_resource(Quotes, '/api/quotes')


if __name__ == '__main__':
    app.run(debug=True)
