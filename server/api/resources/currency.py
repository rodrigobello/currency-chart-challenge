from flask_restful import Resource
from api.data import rates

from utils.exceptions import ApiException


class Currency(Resource):
    def get(self, currency):
        # currency should be case insensitive ?
        try:
            return {'rate': rates.get_currency(currency)}
        except KeyError as e:
            return {'message': 'Currency not available.'}, 404
        except ApiException as e:
            return {'message': str(e.message)}, 500


class Currencies(Resource):
    """ This resource is for test only """
    def get(self):
        return {'rates': rates.get_currencies()}
