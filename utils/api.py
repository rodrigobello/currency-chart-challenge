from werkzeug.security import safe_str_cmp
import requests
import json


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
        "access_key": "4727a0941e98946607483bb5b86958f5",
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


def get_dates_quotations(dates, currency):
    """
    :param dates: [ String ]
    :param currency: String
    :return: quotations as [ { date: String, currency: String, brl: Float } ]
    """
    return list(map(lambda x: create_quotation_dictionary(x, currency), dates))


def create_quotation_dictionary(date, currency):
    """
    :param quote: Float
    :param date: String
    :param currency: String
    :return: quotation as { date: String, currency: String, brl: Float }
    """
    return {
        'date': date,
        'quote': request_quotation(currency, date),
        'currency': currency,
    }
