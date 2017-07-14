# -*- coding:utf-8 -*-
import pymysql
import json


#清洗合并本信息
db = pymysql.connect(host = "localhost", user = "root", password = "123", db = "tyc", port=3306, charset='utf8')
cursor = db.cursor()
select_sql = "SELECT name,jbxx FROM tyc_jbxx_626"
cursor.execute(select_sql)
db.commit()
for i in cursor.fetchall():
    #print type(i[0])
    name = i[0]
    jbxx =  (i[1]).replace(u'详细','').replace(u'收起','').replace(u'〓','').replace(u' ','').replace(u'^；','').replace('\n', '').replace('\r', '').replace('\r\n', '')
    sql1 = 'INSERT INTO tyc_10_jbxx (name,jbxx)VALUES(%s,%s)'
    print(name)
    cursor.execute(sql1,(name,jbxx))
    db.commit()
cursor.close()
db.close()

''''
a = {"change_time": "2015-08-18", "change_after": "<em>60157</em>3<em>.</em>0<em>8</em>7800", "change_project": [], "change_before": "3<em>0</em>078<em>6.5439</em>00"}
print type(a["change_after"])


db = pymysql.connect(host = "localhost", user = "root", password = "123", db = "tyc", port=3306, charset='utf8')
cursor = db.cursor()
select_sql = "SELECT change_record FROM fq_provider_business where company='珠海格力电器股份有限公司'"
cursor.execute(select_sql)
db.commit()
a = cursor.fetchall()
b = a[0]
print type(b)
print b[0]
c= b[0]
c = json.loads(c)
for i in c:
    #i = json.loads(i)
    print type(i['change_after'])

#c = json.loads(c[0])

#d = c[0]

'''

'''
#去重
db = pymysql.connect(host = "localhost", user = "root", password = "123", db = "tyc", port=3306, charset='utf8')
cursor = db.cursor()
select_sql = "SELECT id,name FROM tyc_10_jbxx"
cursor.execute(select_sql)
db.commit()
urls = []
ids = []
for i in cursor.fetchall():
    name = i[1]
    urls.append(name)
select_sql1 = "SELECT id,name FROM tyc_10_c1"
cursor.execute(select_sql)
db.commit()
names = set(urls)
print len(urls)
print len(names)
cursor.close()
db.close()


db = pymysql.connect(host = "localhost", user = "root", password = "123", db = "test15", port=3306, charset='utf8')
cursor = db.cursor()
select_sql = "SELECT name FROM tyc_10_c1"
cursor.execute(select_sql)
db.commit()
#旧剩余
#n2 = []
for i in cursor.fetchall():
    name = i[0]
    urls.append(name)
nams = set(urls)
print len(urls)
print len(nams)

select_sql1 = "SELECT name,number FROM tyc_url"
cursor.execute(select_sql1)
db.commit()
for i in cursor.fetchall():
    name = i[0]
    number =i[1]
    if name not in nams:
        sql2 = "INSERT INTO tyc_sid (name,number)VALUES(%s,%s)"
        cursor.execute(sql2,(name,number))
        db.commit()
cursor.close()
db.close()

'''

'''
global warn,null,error
warn='warn'
null='null'
error='error'
db = pymysql.connect(host = "localhost", user = "root", password = "123", db = "tyc", port=3306, charset='utf8')
cursor = db.cursor()
select_sql = "SELECT id,name,jyfx FROM tyc_10_6"
cursor.execute(select_sql)
db.commit()
n = 0
m=0
#print len(cursor.fetchall())
for i in cursor.fetchall():
    #print i[2]
    try:
        dict1 = json.loads(i[2])
        #print type(dict1)
        dict2 = dict1[u'严重违法']
        if dict2 == 'warn':
            #print dict2
            n+=1
        elif dict2 == 'error':
            n+=1
        else:
            dict3 = json.loads(dict2)
            item = dict3['items']
            if item == []:
                m+=1
            else:
                print item
    except:
        print i[1]

    #print dict2
    #if type(dict2) == dict:
    #    dict3=dict2
    #else:
    #   dict3 = json.loads(dict2)
    #items = dict3['items']
    ##if dict2 ==  []:
    #elif: dict2 == warn
    #elor null or error:
        #pass
    #else:
     #   print i[0]
      #  print i[1]
      #  print dict2
      #  n+=1
print n
print m
'''
'''#coding:utf-8

import pymysql
db = pymysql.connect(host = "localhost", user = "root", password = "123", db = "tyc", port=3306, charset='utf8')
cursor = db.cursor()
select_SQL = 'SELECT company,change_record FROM fq_provider_business;'
cursor.execute(select_SQL)
for i in cursor.fetchall():
    # print(i)
    try:
        a = type(eval(i[1]))
    except:
        print(i[0],i[1])


a=  [{"change_time": "2017-02-17", "change_project": "注册资本","change_before": "88384.3348万元","change_after":"88268.6848万元"},{"change_time": "2016-11-28", "change_project": "注册资本", "change_before":"83069.3439万元","change_after":"88384.3348万元"},{"change_time": "2016-10-08", "change_project": "注册资本", "change_before":"83265.3272万元","change_after":"83069.3439万元"},{"change_time": "2015-10-29", "change_project": "注册资本", "change_before": "41632.6636万元","change_after":"83265.3272万元"}, {"change_time": "2015-05-27", "change_project": "注册资本", "change_before":"41680.3553万元","change_after":"41632.6636万元"}]

print type(a)'''
