# -*- coding: utf-8 -*-
"""
Created on Sat Aug 05 07:29:55 2017

@author: u6035034
"""

import tushare as ts
import re
import urllib

def GetAllStockCodes():
    #df = ts.get_stock_basics()
    #print type(df)
    patten = r"http://quote.eastmoney.com/sz[0-9]*.html"
    patten_code = r"[0-9]+"
    url = "http://quote.eastmoney.com/stocklist.html"
    webpage = urllib.urlopen(url).read()
    stockURLlist = re.findall(patten,webpage)
    stocklist=[]
    for url in stockURLlist:
        code = re.findall(patten_code,url)[0]
        stocklist.append(code)
    return stocklist

def GetStockPrice(code,st,ed):
    df = ts.get_hist_data(code,start=st,end=ed)
    return df

if __name__ == '__main__':
    GetStockPrice('600415','2017-08-04','2017-08-04')