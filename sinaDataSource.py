# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a python script file for get sina stock data.
"""

import requests
import pandas as pd
from pandas import DataFrame,Series
import numpy as np
import datetime
import time



def get_Big_Deal(code,num):
    url="http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/MoneyFlow.ssl_qsfx_lscjfb?page=1&num={num}&sort=opendate&asc=0&daima={code}"
    result=requests.get(url.format(code=code,num=num))
    data=result.content
    print data
    data=data.replace('[{','').replace('}]','')
    r_d={}
    
    for item in data.split('},{'):
        r_dict={}
        for line in item.split(','):        
            key,value=line.split(':')
            r_dict[key]=value
        date=r_dict['opendate']
        y,m,d=date.strip("\"").split('-')
        date=datetime.datetime(int(y),int(m),int(d),0,0)
        r_d[date]=r_dict['r0']
    return r_d
        
def read_Big_Deal(file_name,num=1):
    df=pd.read_excel(file_name,index_col='opendate')
    code = df.index.values
    new_index=get_new_columns(code[0],num)
    print df.columns.values
    for i in new_index:
        if i not in df.columns:
            print "insert "+str(i)
            df.insert(9,i,Series())
    for c in code:
        if c != None:
            r_d=get_Big_Deal(c,num)
            time.sleep(1)
            print c
            for item in r_d.keys():
                if item in df.columns:
                    df[item][c] = r_d[item].strip('"')
    writer=pd.ExcelWriter('tmp.xlsx')
    df.to_excel(writer,'sheet1')
    writer.save()
        
        
def get_new_columns(code,num):
    r_d=get_Big_Deal(code,num)
    key=r_d.keys()
    key.sort()
    print key
    return key
        
        

if __name__=="__main__":
    #get_new_columns("sh600004",10)
    read_Big_Deal("../test.xlsx",10)
    #get_Big_Deal("sh600375",10)