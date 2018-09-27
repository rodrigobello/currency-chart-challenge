from flask_restful import Resource, reqparse
from api.data import rates

from utils.exceptions import ApiException


class Currency(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'orderby',
        choices=("asc", "desc"),
        help="You have entered an invalid value. "
        + "[Should be 'asc' or 'desc']",
    )
    # TO DO: parser.add_argument('days', type=int)

    def get(self, currency):
        data = self.parser.parse_args()

        try:
            if data.orderby == 'asc':
                return list(reversed(rates.get_currency(currency)))
            else:
                return rates.get_currency(currency)
        except KeyError as e:
            return {'message': 'Currency not available.'}, 404
        except ApiException as e:
            return {'message': str(e.message)}, 500


class Currencies(Resource):
    """ This resource is for test only """
    def get(self):
        return {'rates': rates.get_currencies()}
