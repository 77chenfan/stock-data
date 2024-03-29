# -*- coding: utf-8 -*-
"""
Created on Thu Aug 03 19:16:01 2017

@author: u6035034
"""
import BaseContent
import com
import json
import re
import JsonUtil
import os
import sys
import tushareUtil
import time



class ShareHolder(BaseContent.BaseContent):
    
    #suppose get raw data from url
    def preProcess(self,content):
        # replace two strings in content
        #logger.debug(content)
        patten1=r'data'
        patten2=r'page' 
        assert(len(re.findall(patten1,str(content)))==1,"get content has multi replace string")
        assert(len(re.findall(patten2,str(content)))==1,"get content has multi replace string")
        tempString = str(content).replace('data','\"data\"')
        preContent = tempString.replace('pages','\"pages\"')
        contentJson = json.loads(preContent)
        return contentJson
    # format data
    def saveContent(self,contentJson,code):
        com.init_logger()
        schema = JsonUtil.getSchema(contentJson['data'][0])
        if(self.type == 'csv'):
            if(os.path.exists(self.name+'_store.csv') == False):
                storeFile = open(self.name+'_store.csv','w')
                headline=",".join(schema)
                print ('schema is '+headline+',code')
                storeFile.write(headline+',code')
                storeFile.write('\n')
                storeFile.close()
            
            storeFile = open(self.name+'_store.csv','a')
            for ele in contentJson['data']:
                line=[]
                for key in schema:
                    line.append(str(ele[key]))
                storeFile.write((','.join(line)))
                storeFile.write(','+code)
                storeFile.write('\n')
            
            storeFile.close()
        



if __name__ == "__main__":
    testConfig=BaseContent.Config("http://dcfm.eastmoney.com//em_mutisvcexpandinterface/api/js/get?type=HOLDERNUM&token=70f12f2f4f091e459a279469fe49eca5&sty=detail&filter=(securitycode='%s')&st=EndDate&sr=1&js={data:(x),pages:(tp)}",'csv','shareHolder')
    mycontent=ShareHolder(testConfig)
    stocklist = tushareUtil.GetAllStockCodes()
    offset = sys.argv[1]
    count=0
    print offset
    for code in stocklist:
        count +=1
        if(count < int(offset)):
            print 'skipped'
        else:
            print("try to get %s share holder numbers"%code)
            try :
                rawdata=mycontent.GetSourceCode(code)
            #f1=open('000065_sourcecode.html')
            #rawdata=f1.readlines()[0]
                contentJson = mycontent.preProcess(rawdata)
                if(len(contentJson['data'])!=0):
                    mycontent.saveContent(contentJson,code)
            except Exception as err:
                print err
            finally:
                print "now the offset is %d"%count
        
        
        