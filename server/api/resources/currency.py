from flask_restful import Resource
from api.data import rates


class Currency(Resource):
    def get(self, currency):
        # currency should be case insensitive ?
        try:
            return {'rate': rates.get_currency(currency)}
        except KeyError:
            return {'message': 'Currency not available.'}, 404


class Currencies(Resource):
    """ This resource is for test only """
    def get(self):
        return {'rates': rates.get_currencies()}
