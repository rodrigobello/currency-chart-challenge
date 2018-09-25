from werkzeug.security import safe_str_cmp
from flask import current_app
import requests
import json

from utils.date import datetime, date_to_str


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

    if date is None:
        response = requests.get(
            'http://apilayer.net/api/live?',
            params=params)
    else:
        response = requests.get(
            f'http://apilayer.net/api/historical?date={date}',
            params=params)

    data = json.loads(response.text)

    if data['success'] is False:
        return data['error']

    quotes = data['quotes']

    if safe_str_cmp(currency, 'USD'):
        return quotes['USDBRL']

    return quotes[f'USD{currency}'] / quotes['USDBRL']


def create_quotation_dictionary(currency, date=None):
    """
    :param quote: Float
    :param date: String
    :param currency: String
    :return: quotation as { date: String, currency: String, brl: Float }
    """
    return {
        'date': date if date else date_to_str(datetime.date.today()),
        'quote': request_quotation(currency, date=date),
        'currency': currency,
    }


def get_historical_rates(currency, dates):
    """
    :param dates: [ String ]
    :param currency: String
    :return: quotations as [{ date: String, currency: String, brl: Float }]
    """
    return list(map(lambda x: create_quotation_dictionary(currency, x), dates))


def get_live_rate(currency):
    """
    :param date: String
    :param currency: String
    :return: quotation as { date: String, currency: String, brl: Float }
    """
    return create_quotation_dictionary(currency)
