#!/bin/usr/env python3
import uno
import unohelper
from np.com.maharjansujit.npDate import XnpDate
from datebs import DateBS
import logging
import datetime

class npDateImpl(unohelper.Base, XNepalDataScrapper):
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

    def date_to_ad(date=None):
        if date is None:
            return datetime.datetime.now()
        else:
            dateBS = DateBS.from_string(date)
        return dateBS.toAD()


def createInstance( ctx ):
    return npDateImpl(ctx)

g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation(
    createInstance,"np.com.maharjansujit.npDate.python.npDateImpl",
    ("com.sun.star.sheet.AddIn",),)
