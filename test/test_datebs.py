import datebs
import pytest
import datetime

def test_from_string():
    date = datebs.DateBS.from_string("2077-03-01")
    assert date.year == 2077
    assert date.month == 3
    assert date.day == 1

def test_from_AD():
    date = datebs.DateBS.from_AD(datetime.datetime(2020,8,1))
    assert date.year == 2077
    assert date.month == 4
    assert date.day == 17 

def test_day_of_year():
    date = datebs.DateBS.from_string("2077-01-05")
    assert date.day_of_year() == 5

def test_days_in_year():
    assert datebs.DateBS.days_in_year(2077) == 366

def test_day_since():
    date = datebs.DateBS(2000,9,18)
    assert date.day_since() == 1

def test_add():
    date =  datebs.DateBS(2077,1,1)
    assert date.add(10).day == 11

def test_to_AD():
    date = datebs.DateBS(2077,4,23)
    assert date.to_AD().year == 2020
    assert date.to_AD().month == 8
    assert date.to_AD().day == 7

def test_months_in_year():
    assert datebs.DateBS.months_in_year(2001) == [ 31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30 ]  #2001

def test_days_in_month():
    assert datebs.DateBS.days_in_month(2077,4) == 32

def test_month_in_string():
    date = datebs.DateBS(2077,1,1)
    assert date.month_in_string() == "Baishakh"

def test_month_in_string_nepali():
    date = datebs.DateBS(2077,1,1)
    assert date.month_in_string_nepali() == "वैशाख"

def test_get_financial_year():
    date = datebs.DateBS(2077,1,1)
    assert date.get_financial_year() == "2076/77"



