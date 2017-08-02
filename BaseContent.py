# -*- coding: utf-8 -*-
"""
Created on Wed Aug 02 19:38:21 2017

@author: u6035034

base class used for getting content from web page

"""
import collections
import urllib
import com
import requests
"""
url        : get web page
outputType : store type (excel,csv)
name       : content name
"""
Config=collections.namedtuple('contentConfig',['url','outputType','name'])

logger = com.logger

class BaseContent:
    
    def __init__(self,config):
        self.url=config.url
        self.type=config.outputType
        self.name=config.name
    
    #get web page source code
    #code: stock code
    def GetSourceCode(self,code,isStore=False):
        logger.info('try to get '+self.url % code)
        f=urllib.urlopen(self.url % code)
        if(isStore):
            ft=open(code+'_sourcecode.html','w+')
            ft.write(f.read())
            ft.close
        return f.read()
    def GetSourceCode_request(self,code,isStore=False):
        logger.info('try to get '+self.url % code)
        response=requests.get(self.url %code)
        if(isStore):
            ft=open(code+'_sourcecode.html','w+')
            ft.write((response.text).encode('gbk'))
            ft.close
        return response.text

if __name__=='__main__':
    com.init_logger()
    testConfig=Config('http://data.eastmoney.com/gdhs/detail/%s.html','excel','test')
    mycontent=BaseContent(testConfig)
    mycontent.GetSourceCode_request('000065',True)