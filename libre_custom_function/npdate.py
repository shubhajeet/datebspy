#!/bin/usr/env python3
import uno
import unohelper
from np.com.maharjansujit.npDate import XnpDate
import datetime
from datebs import DateBS

class npDateImpl(unohelper.Base, XnpDate):
    def __init__(self, ctx):
        self.ctx = ctx

    def dateToBS(self,date):
        try:
            if (date == None):
                dateBS = DateBS.from_AD(datetime.datetime.now())
                return str(dateBS)
            else:
                dateBS = DateBS.from_AD(datetime.datetime.strptime(date, "%Y-%m-%d"))
                return str(dateBS)
        except Exception as e:
            return str(e)

    def dateToAD(self,date):
        try:
            if (date == None):
                return str(datetime.datetime.now().strftime("%Y-%m-%d"))
            else:
                dateBS = DateBS.from_string(date)
                return str(dateBS.to_AD().strftime("%Y-%m-%d"))
        except Exception as e:
            return str(e) 

    def echo(self,text):
        print("text")
        return text

    def greet(self):
        print("greet")
        return "hi"

    def BSMonth(self, date):
        try:
            if (date == None):
                return DateBS.from_AD(datetime.datetime.now()).month
            else:
                return DateBS.from_string(date).month
        except Exception as e:
            return str(e)

    def BSMonthNepali(self, date):
        try:
            if (date == None):
                return DateBS.from_AD(datetime.datetime.now()).month_in_string_nepali()
            else:
                return DateBS.from_string(date).month_in_string_nepali()
        except Exception as e:
            return str(e)

    def BSMonthString(self, date):
        try:
            if (date == None):
                return DateBS.from_AD(datetime.datetime.now()).month_in_string()
            else:
                return DateBS.from_string(date).month_in_string()
        except Exception as e:
            return str(e)

    def BSFinancialYear(self, date):
        try:
            if (date == None):
                return DateBS.from_AD(datetime.datetime.now()).get_financial_year()
            else:
                return DateBS.from_string(date).get_financial_year();
        except Exception as e:
            return str(e)


def createInstance( ctx ):
    return npDateImpl(ctx)

g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation(
    createInstance,"np.com.maharjansujit.npDate.python.npDateImpl",
    ("com.sun.star.sheet.AddIn",),)
