#coding:utf-8

import json
import requests

url = '127.0.0.1:8888'
headers = {'content-type':'application/json'}

data = {
    'jsonrpc':'2.0',
    'id':'1',
    'method':'login',
    'params':{
	'name':'test',
	'password':'123123'
    }
}

data = requests.post(url,headers=headers,json=data)
print data.status_code
print data.text
