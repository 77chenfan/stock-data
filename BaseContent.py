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
    def GetSourceCode(self,code,isStore=False,isPureData=False):
        logger.info('try to get '+self.url % code)
        f=urllib.urlopen(self.url % code)
        if(isStore):
            ft=open(code+'_sourcecode.html','w+')
            ft.write(f.read())
            ft.close
        return f.read()
    def GetSourceCode_request(self,code,isStore=False,isPureData=False):
        logger.info('try to get '+self.url % code)
        response=requests.get(self.url %code)
        if(isStore):
            ft=open(code+'_sourcecode.html','w+')
            ft.write((response.text).encode('gbk'))
            ft.close
        return response.text
    def preProcess(self,content):
        pass
        
    def analyze(self,content):
        pass
    
    def saveContent(self,content):
        if(self.type =='excel'):
            pass
        elif(self.type =='csv'):
            pass
if __name__=='__main__':
    com.init_logger()
    testConfig=Config('http://data.eastmoney.com/gdhs/detail/%s.html','excel','test')
    testConfig2=Config("http://dcfm.eastmoney.com//em_mutisvcexpandinterface/api/js/get?type=HOLDERNUM&token=70f12f2f4f091e459a279469fe49eca5&sty=detail&filter=(securitycode='%s')&st=EndDate&sr=1&js={data:(x),pages:(tp)}",'excel','test')
    mycontent=BaseContent(testConfig)
    mycontent.GetSourceCode('000065',True)