import datetime


def days_diff(date, days):
    """
    :param date: datetime
    :return: date as datetime
    """
    return date - datetime.timedelta(days)


def date_to_str(date):
    """
    :param date: datetime
    :return: date as String
    """
    return date.strftime('%Y-%m-%d')


def get_last_dates(number_of_days):
    """
    Create an array with the "n" dates, where "n" is the last number
    of days passed.

    :param number_of_days: int
    :return: dates as [ String ]
    """
    now = datetime.date.today()
    return [date_to_str(days_diff(now, i + 1)) for i in range(number_of_days)]
