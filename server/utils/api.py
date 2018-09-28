import requests
import json
import sys

from werkzeug.security import safe_str_cmp
from flask import current_app

from utils.date import get_today_date, date_to_str
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
            date = date_to_str(date)
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
        return 1 / quotes['USDBRL']

    return quotes[f'USD{currency}'] / quotes['USDBRL']


def create_quotation_dictionary(currency, date=None):
    """
    :param quote: Float
    :param date: Datetime
    :param currency: String
    :return: quotation as { date: Datetime, currency: String, value: Float }
    """
    try:
        return {
            'currency': currency,
            'date': date if date else get_today_date(),
            'value': round(request_quotation(currency, date=date), 4),
        }
    except ApiException as e:
        raise ApiException(e)


def get_historical_rates(currency, dates):
    """
    :param dates: [ Datetime ]
    :param currency: String
    :return: quotations as [{ date: Datetime, currency: String, value: Float }]
    """
    try:
        return list(
            map(lambda x: create_quotation_dictionary(currency, x), dates)
        )
    except ApiException as e:
        raise ApiException(e)


def get_live_rate(currency):
    """
    :param date: Datetime
    :param currency: String
    :return: quotation as { date: Datetime, currency: String, value: Float }
    """
    try:
        return create_quotation_dictionary(currency)
    except ApiException as e:
        raise ApiException(e)
