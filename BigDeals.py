# -*- coding: utf-8 -*-
"""
Created on Sun Aug 06 14:49:09 2017

@author: u6035034
"""

import BaseContent
import json
import JsonUtil
import os
import urllib
import sys
import traceback
import com
import logging
import tushareUtil

reload(sys)
sys.setdefaultencoding('utf-8')

class BigDeals(BaseContent.BaseContent):
    
    #get web page source code
    #code: stock code
    def GetSourceCode(self,code,date,isStore=False,isPureData=False):
        page=1
        if(int(code)>30000):
            code = "sh"+code
        else:
            code = "sz"+code
        self.logger.info('try to get '+self.url.format(code=code,date=date,page=page))
        content=[]
        while(page):
            f=urllib.urlopen(self.url.format(code=code,date=date,page=page))
            pagecontent=f.read()
            if(pagecontent!='null'):
                if(isStore):
                    ft=open(code+'_sourcecode.html','w+')
                    ft.write(pagecontent)
                    ft.close
                content.append(pagecontent)
                page +=1
            else:
                page=0
        return content    
    
    def preProcess(self,contentlist):
        #need to replace all fields
        contentJson=[]
        for content in contentlist:
            pattern = ['symbol','name','ticktime','price','volume','kind']
            tempContent = str(content)
            for ptn in pattern:
                tempContent= tempContent.replace(ptn,'\"'+ptn+'\"')
            tempContent = tempContent.replace('prev_\"price\"','\"prev_price\"')
#            f1=open("tempdata.txt",'w+')
#            f1.write(unicode(tempContent).encode('utf-8'))
#            f1.close()
#            f1=open("tempdata.txt")
            contentJson.append(json.loads(tempContent.decode('GBK')))
        
        return contentJson
    # save data
    def saveContent(self,contentJson,date):
        schema = JsonUtil.getSchema(contentJson[0])
        if(self.type == 'csv'):
            if(os.path.exists(self.name+'_store.csv') == False):
                storeFile = open(self.name+'_store.csv','w')
                headline=",".join(schema)
                print ('schema is '+headline+',date')
                storeFile.write(headline+',date')
                storeFile.write('\n')
                storeFile.close()
            
            storeFile = open(self.name+'_store.csv','a')
            for ele in contentJson:
                line=[]
                for key in schema:
                    line.append(str(ele[key]))
                storeFile.write((','.join(line)))
                storeFile.write(','+date)
                storeFile.write('\n')
            
            storeFile.close()


if __name__ == '__main__':
    bigdealsConfig = BaseContent.Config('http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_Bill.GetBillList?symbol={code}&num=100&page={page}&sort=ticktime&asc=0&volume=20000&amount=100000&type=0&day={date}','csv','BigDeals')
    mycontent=BigDeals(bigdealsConfig)
    mycontent.logger=logging.getLogger(mycontent.name)
    #stocklist = tushareUtil.GetAllStockCodes()
    #stocklist=['600415']
    stocklist = tushareUtil.GetAllStockCodes()
    offset_c = sys.argv[1]
    offset_d = sys.argv[2]
    
    if(sys.argv[3]!=0):    
        days=sys.argv[3]
    else:
        days=20
    datelist = com.GetLastTwentyDay(int(days))
    count_c=0
    count_d=0
    print datelist
    for code in stocklist:
        count_c +=1
        if(count_c < int(offset_c)):
            print 'skipped'
        else:
            print("try to get %s big deals"%code)
            for dt in datelist:
                count_d +=1
                if(count_d <int(offset_d)):
                    print 'skipped'
                else:
                    mycontent.logger.info("try to get %s" %str(dt))
                    try :
                        rawdata=mycontent.GetSourceCode(code,str(dt))
                        #f1=open('000065_sourcecode.html')
                        #rawdata=f1.readlines()[0]
                        contentJson = mycontent.preProcess(rawdata)
                        if(len(contentJson)!=0):
                            for content in contentJson:
                                mycontent.saveContent(content,str(dt))
                    except Exception as err:
                        print err
                        traceback.print_exc()
                    finally:
                        print "now the offset_c is %d , the offset_d is %d"%(count_c,count_d)
                        print dt
            count_d=0
        
        
        