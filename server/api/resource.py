from flask_restful import Resource, reqparse

from api.model import Quote, QuoteSchema
from utils.exceptions import ApiException

quotes_schema = QuoteSchema(many=True)
quote_schema = QuoteSchema()


class Quotes(Resource):
    """
    API resource that return the quotes of the currency passed in the request.

    :param currency: Must be one of ['USD, 'ARS', 'EUR]
    :return: The last seven days currency quotes (BRL currency)
    """
    parser = reqparse.RequestParser()
    parser.add_argument(
        'orderby',
        choices=("asc", "desc"),
        help="You have entered an invalid sorting type. "
        + "[Should be 'asc' or 'desc']",
    )
    parser.add_argument(
        'currency',
        choices=("USD", "ARS", "EUR"),
        required=True,
        help="You have entered an invalid currency. "
        + "[Keep in mind that we only work with ARS, EUR and USD]"
    )

    def get(self):
        data = self.parser.parse_args()

        try:
            Quote.request_quotes(data.currency)

            quotes = Quote.get_currency_last_quotes(
                        data.currency,
                        2,
                        data.orderby,
                    )

            quotes = quotes_schema.dump(quotes).data

            return {'success': True, 'quotes': quotes}, 200

        except ApiException as e:
            return {'success': False, 'message': str(e.message)}, 500
