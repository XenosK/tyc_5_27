# -*- coding:utf-8 -*-
import requests
import pymysql
import json

#高管信息
url = 'http://www.tianyancha.com/stock/seniorExecutive.json?graphId=665989&ps=100&pn=1'
response = requests.get(url)
ggxx = json.loads(response.text)
a = ggxx["data"]
b = json.dumps(a, ensure_ascii=False)
'''
#股票行情
url = 'http://www.tianyancha.com/stock/stockVolatility.json?graphId=437099469'
response = requests.get(url)
gphq = json.loads(response.text)
a = gphq["data"]
b = json.dumps(a, ensure_ascii=False)
print b



#企业简介
url = 'http://www.tianyancha.com/stock/companyInfo.json?graphId=665989'
response = requests.get(url)
qyjj = json.loads(response.text)
a = qyjj[data]
b = json.dumps(a,ensure_ascii=False)
'''

conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='tyc', port=3306, charset='utf8')
cur = conn.cursor()
sql = 'INSERT INTO test123 (name)VALUES(%s)'
cur.execute(sql,(b))
conn.commit()
cur.close()
conn.close()












'''
d = str(c.encode('utf-8').strip())
print d
print (u"\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a"+u"\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a")
def dict_str(dict):
    for (k,v) in dict.items():
        if type(v)==dict:
            dict_str(v)
        else:
            print "dict[%s]=" %k,v

dict_str(a)
print type(a)=="<type 'dict'>"


print a
print type(a)
b = str(a)
print type(b)

d = c.encode('utf-8').strip()
print type(c)
print b
print c
print d
'''