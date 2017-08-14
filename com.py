# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 17:20:20 2016

@author: u6035034
"""

import datetime
import logging

logger = logging.getLogger("com")


def GetLastTwentyDay(num=20):
    now = datetime.datetime.now()
    dayofweek = datetime.datetime.isoweekday(now)
    datelist=[]
    while(num!=0):
        if(dayofweek <6):
            datelist.append(now.date())
            num-=1
        now=now+datetime.timedelta(days=-1)
        dayofweek = datetime.datetime.isoweekday(now)
    return datelist

def init_logger():
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    logger.addHandler(ch)

if __name__ == "__main__":
    datelist=GetLastTwentyDay()
    for d in datelist:
        print str(d)
