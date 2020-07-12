import sys
import datetime
from datebs import DateBS


def date_to_bs(date=None):
    if date is None:
        dateBS = DateBS.from_AD(datetime.datetime.now())
    else:
        dateBS = DateBS.from_AD(datetime.datetime.strptime(date, "%Y-%m-%d"))
    return str(dateBS)


def date_to_ad(date=None):
    if date is None:
        return datetime.datetime.now()
    else:
        dateBS = DateBS.from_string(date)
    return dateBS.toAD()
