import datetime
from utils.api import get_historical_rates, get_live_rate
from utils.date import (
    get_last_dates,
    date_to_str,
    str_to_date,
    days_diff
)


class Rates:
    """
    The idea behind this data is to store the latest quotations for each
    currency. By doing so, we can avoid a lot of requests each time a new
    chart is plotted.

    For example, if a currency chart was plotted yesterday and today we
    want to plot it again, this API already have the quotes for the previous
    six days and only one request is needed: the live request.

    The live request should aways be done, cause its quote is regularly
    updated.

    Ideally, this data should be stored in a database for its persistance.
    """
    def __init__(self, currencies):
        self.currencies = {}
        for currency in currencies:
            self.currencies.update({
                currency: {
                    'updated': None,
                    'quotes': []
                }
            })

    def get_currencies(self):
        return self.currencies

    def get_currency(self, currency):
        self.update_quotes(currency)
        return self.currencies[currency]

    def update_quotes(self, currency):
        last_update = self.currencies[currency]['updated']
        current_quotes = self.currencies[currency]['quotes']

        today = datetime.datetime.today()
        days = None

        if last_update:
            date_of_update = str_to_date(last_update)
            days = days_diff(today, date_of_update)

        # Either currency is empty or the update was a long time ago
        if days is None or days > 2:
            days = 2

        live_rate = get_live_rate(currency)

        last_dates = get_last_dates(days - 1)

        last_rates = (
                    get_historical_rates(currency, last_dates) if last_dates
                    else []
        )

        new_quotes = (
            [live_rate] + current_quotes[1:] if days == 0
            else [live_rate] + last_rates + current_quotes[:-days]
        )

        self.currencies[currency]['updated'] = date_to_str(today)
        self.currencies[currency]['quotes'] = new_quotes
