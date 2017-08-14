# -*- coding: utf-8 -*-
"""
Created on Wed Aug 02 19:38:21 2017

@author: u6035034

base class used for getting content from web page

"""
import collections
import urllib
import logging
import requests
"""
url        : get web page
outputType : store type (excel,csv)
name       : content name
"""
Config=collections.namedtuple('contentConfig',['url','outputType','name'])

class BaseContent:
    
    def __init__(self,config):
        self.url=config.url
        self.type=config.outputType
        self.name=config.name
        self.logger=logging.getLogger(self.name)
    
    #get web page source code
    #code: stock code
    def GetSourceCode(self,code,isStore=False,isPureData=False):
        self.logger.info('try to get '+self.url % code)
        f=urllib.urlopen(self.url % code)
        content=f.read()
        if(isStore):
            ft=open(code+'_sourcecode.html','w+')
            ft.write(content)
            ft.close
        return content
    def GetSourceCode_request(self,code,isStore=False,isPureData=False):
        self.logger.info('try to get '+self.url % code)
        response=requests.get(self.url %code)
        content = response.text
        if(isStore):
            ft=open(code+'_sourcecode.html','w+')
            ft.write((content).encode('gbk'))
            ft.close
        return content
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
    testConfig=Config('http://data.eastmoney.com/gdhs/detail/%s.html','excel','test')
    testConfig2=Config("http://dcfm.eastmoney.com//em_mutisvcexpandinterface/api/js/get?type=HOLDERNUM&token=70f12f2f4f091e459a279469fe49eca5&sty=detail&filter=(securitycode='%s')&st=EndDate&sr=1&js={data:(x),pages:(tp)}",'excel','test')
    mycontent=BaseContent(testConfig)
    mycontent.GetSourceCode('000065',True)