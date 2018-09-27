import requests
import json
import sys

from werkzeug.security import safe_str_cmp
from flask import current_app

from utils.date import datetime, date_to_str
from utils.exceptions import ApiException


def request_quotation(currency, date=None):
    """
    Consume the currencylayer API (https://currencylayer.com) to get a
    specific currency quotation.

    It can get the most recent exchange rate or the historical rate for a
    specific day.

    :param currency: ['USD', 'EUR', 'ARS'] as String
    :param date: 'YYYY-MM-DD' as String
    :return: quotation as Float
    """
    params = {
        "access_key": current_app.config['CURRENCY_LAYER_KEY'],
        "currencies": f'BRL,{currency}'
    }

    try:
        if date is None:
            response = requests.get(
                'http://apilayer.net/api/live?',
                params=params)
        else:
            response = requests.get(
                f'http://apilayer.net/api/historical?date={date}',
                params=params)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        """ Error ocurring while connecting to the API """
        sys.exit(str(e))

    data = json.loads(response.text)

    if data['success'] is False:
        raise ApiException(
            f"{data['error']['info']} (Error code: {data['error']['code']})"
        )

    quotes = data['quotes']

    if safe_str_cmp(currency, 'USD'):
        return quotes['USDBRL']

    return quotes['USDBRL'] / quotes[f'USD{currency}']


def create_quotation_dictionary(currency, date=None):
    """
    :param quote: Float
    :param date: String
    :param currency: String
    :return: quotation as { date: String, currency: String, brl: Float }
    """
    try:
        return {
            'date': date if date else date_to_str(datetime.date.today()),
            'quote': request_quotation(currency, date=date),
        }
    except ApiException as e:
        raise ApiException(e)


def get_historical_rates(currency, dates):
    """
    :param dates: [ String ]
    :param currency: String
    :return: quotations as [{ date: String, currency: String, brl: Float }]
    """
    try:
        return list(
            map(lambda x: create_quotation_dictionary(currency, x), dates)
        )
    except ApiException as e:
        raise ApiException(e)


def get_live_rate(currency):
    """
    :param date: String
    :param currency: String
    :return: quotation as { date: String, currency: String, brl: Float }
    """
    try:
        return create_quotation_dictionary(currency)
    except ApiException as e:
        raise ApiException(e)
