# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a python script file for get sina stock data.
"""

import requests




def get_Big_Deal(code,num):
    url="http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/MoneyFlow.ssl_qsfx_lscjfb?page=1&num={num}&sort=opendate&asc=0&daima={code}"
    result=requests.get(url.format(code=code,num=num))
    data=result.content
    print type(data)
    print result.content


if __name__=="__main__":
    get_Big_Deal("sz002473",1)