from flask_restful import Resource
from api.quotes import quotes


class Currency(Resource):
    def get(self, currency):
        try:
            return quotes[currency]
        except KeyError:
            return {'message': 'Currency not available.'}, 404
