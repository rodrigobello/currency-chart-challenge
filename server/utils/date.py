import datetime


def subtract_days_from_date(date, days):
    """
    :param date: datetime
    :return: date as datetime
    """
    return date - datetime.timedelta(days)


def days_diff(first_date, second_date):
    """
    :param from_date: datetime
    :param to_date: datetime
    :return: days as int
    """
    if first_date > second_date:
        return (first_date - second_date).days
    return (second_date - first_date).days


def date_to_str(date):
    """
    :param date: datetime
    :return: date as String
    """
    return date.strftime('%Y-%m-%d')


def str_to_date(date):
    """
    :param date: String
    :return: date as datetime
    """
    return datetime.datetime.strptime(date, '%Y-%m-%d')


def get_last_dates(number_of_days):
    """
    Create an array with the "n" dates, where "n" is the last number
    of days passed.

    :param number_of_days: int
    :return: dates as [ String ]
    """
    now = datetime.date.today()
    return [date_to_str(subtract_days_from_date(now, i + 1)) for i in range(number_of_days)]
