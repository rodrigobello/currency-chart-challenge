from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields

from utils.api import get_historical_rates, get_live_rate
from utils.date import (
    get_last_dates,
    days_diff,
    get_today_date
)

from utils.exceptions import ApiException

marsh = Marshmallow()
db = SQLAlchemy()


class Quote(db.Model):
    """
    The idea behind this is to store the latest quotes for each
    currency. By doing so, we can avoid a lot of requests each time a new
    chart is plotted.

    For example, if a currency chart was plotted yesterday and today we
    want to plot it again, this API already have the quotes for the previous
    six days and only one request is needed: the live request.

    The live request should aways be done, cause its quote is regularly
    updated.
    """

    __tablename__ = 'quotes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    currency = db.Column(db.String, nullable=False)
    value = db.Column(db.Float, primary_key=True)
    date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(),
                     nullable=False)

    def __init__(self, currency, value, date):
        self.currency = currency
        self.value = value
        self.date = date

    @classmethod
    def request_quotes(cls, currency, days):
        days_without_request = None

        last_quote = cls.get_currency_last_quote(currency)

        if last_quote:
            days_without_request = days_diff(get_today_date(), last_quote.date)

        # Either currency is empty or the update ocurred a long time ago
        if days_without_request is None or days_without_request > 2:
            days_without_request = days

        previous_dates = get_last_dates(days_without_request - 1)

        try:
            if previous_dates:
                previous_quotes = get_historical_rates(
                    currency,
                    previous_dates
                )

                for quote in previous_quotes:
                    cls.save_quote(quote)

            cls.update_quote_value(get_live_rate(currency))

        except ApiException as e:
            raise ApiException(e)

    @classmethod
    def save_quote(cls, quote):
        quote = Quote(
            currency=quote['currency'],
            value=quote['value'],
            date=quote['date']
        )

        db.session.add(quote)
        db.session.commit()

    @classmethod
    def update_quote_value(cls, quote):
        last_quote = Quote.query.filter_by(
            currency=quote['currency'],
        ).filter_by(date=get_today_date()).first()

        if not last_quote:
            cls.save_quote(quote)
        else:
            last_quote.value = quote['value']

        db.session.commit()

    @classmethod
    def get_currency_last_quotes(cls, currency, days, orderby=None):
        quotes = Quote.\
                query.\
                filter_by(currency=currency).\
                order_by(Quote.date.desc()).limit(days)

        if orderby == 'asc':
            return quotes[::-1]

        return quotes

    @classmethod
    def get_currency_last_quote(cls, currency):
        return cls.query.order_by(
            Quote.date.desc()
        ).filter_by(currency=currency).first()


class QuoteSchema(marsh.Schema):
    id = fields.Integer(required=True)
    currency = fields.String(required=True)
    value = fields.Float(required=True)
    date = fields.String(required=True)
