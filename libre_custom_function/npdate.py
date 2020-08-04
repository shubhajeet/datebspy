#!/bin/usr/env python3
import uno
import unohelper
from np.com.maharjansujit.npDate import XnpDate
import logging
import datetime

class npDateImpl(unohelper.Base, XnpDate):
    def __init__(self, ctx):
        self.ctx = ctx
        self.datebs = DateBS();
        self.logger=logging.getLogger('nepalDataScrapper')
        hdlr = logging.FileHandler("/var/tmp/log.log")
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        hdlr.setFormatter(formatter)
        self.logger.addHandler(hdlr)

    def date_to_bs(self,date=None):
        if date is None:
            dateBS = DateBS.from_AD(datetime.datetime.now())
        else:
            dateBS = DateBS.from_AD(datetime.datetime.strptime(date, "%Y-%m-%d"))
        return str(dateBS)

    def date_to_ad(self,date=None):
        if date is None:
            return datetime.datetime.now()
        else:
            dateBS = DateBS.from_string(date)
        return dateBS.toAD()

    def datebs_to_month(self, date):
        return DateBS.from_string(date).month;

    def datebs_to_month_nepali(self, date):
        return DateBS.from_string(date).month_in_string_nepali();

    def datebs_to_month_string(self, date):
        return DateBS.from_string(date).month_in_string();

    def datebs_financial_year(self, date):
        return DateBS.from_string(date).get_finacial_year();


def createInstance( ctx ):
    return npDateImpl(ctx)

g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation(
    createInstance,"np.com.maharjansujit.npDate.python.npDateImpl",
    ("com.sun.star.sheet.AddIn",),)
