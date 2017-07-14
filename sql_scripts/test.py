# -*- coding:utf-8 -*-
'''
一共17975条数据
抓取到的重复性数据  c
未抓取的小范围数据  b
天眼查上不存在的数据  a
已经爬去的数据  m
m-c+a+a = 17975
'''

import pymysql
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''
#不可爬取
def get_no_comp():
    try:
        conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='tyc', port=3306, charset='utf8')
        cur = conn.cursor()
        sql = 'SELECT name FROM tyc_10_6'
        cur.execute(sql)
        conn.commit()
        comps = cur.fetchall()
        cur.close()
        conn.close()
    except Exception as e:
        print(u'异常%s'%e)
    else:
        #name =[]
        for comp in comps:

            if len(str(comp[0]))<12:
                print comp[0]
            else:pass

                name = comp[0]
                conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='tyc', port=3306,
                                       charset='utf8')
                cur = conn.cursor()
                sql = 'INSERT INTO tyc_no_company (name)VALUES(%s)'
                cur.execute(sql,(name))
                conn.commit()
                cur.close()
                conn.close()

            #else:
            #    pass

'''
'''
#已爬取
names = []
def get_company_info():

    try:
        conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='tyc', port=3306, charset='utf8')
        cur = conn.cursor()
        sql = 'SELECT name FROM tyc_10_6'
        cur.execute(sql)
        conn.commit()
        coms = cur.fetchall()
        print len(coms)
    except Exception as e:
        print(u'异常%s'%e)
    else:
        cur.close()
        conn.close()
        for com in coms:
            name = com[0]
            names.append(name)
        print(u'已爬取数据库中有')
        print len(names)
        a = set(names)
        print(u'去重以后还有')
        print len(a)
        return a

a = get_company_info()
conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='test15', port=3306, charset='utf8')
cur = conn.cursor()
sql = 'SELECT name FROM tyc_url'
cur.execute(sql)
conn.commit()
comps = cur.fetchall()
cur.close()
conn.close()
coms = []
comqcs = []
for i in comps:
    name = i[0]
    comqcs.append(name)
    if name not in a:
        coms.append(name)
print(u'number总数')
print len(comqcs)
b=set(comqcs)
print(u'去重后的number总数')
print len(b)
print(u'未爬取得number')
print len(coms)
canurl = []
nourl = []
for i in coms:
    if len(i)<4:
        #print i
        nourl.append(i)
    else:
        print i
        canurl.append(i)
print len(nourl)
print len(canurl)
for i in a:
    if i in names:
        n = names.index(i)
        names.pop(n)
print(u'已爬取的重复个数')
print len(names)
'''




#获取完整信息
'''
def get_all():
    names=[]
    try:
        conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='tyc', port=3306, charset='utf8')
        cur = conn.cursor()
        sql = 'SELECT name,jbxx FROM tyc_10_jbxx LIMIT 13348,5000'
        cur.execute(sql)
        conn.commit()
        coms = cur.fetchall()
        print len(coms)
    except Exception as e:
        print(u'异常%s' % e)
    else:
        cur.close()
        conn.close()
        urls = []
        for com in coms:
            urls.append(com[0])
        names = set(urls)
        for com in coms:
            name = com[0]
            jbxx = com[1]
            get_all_json(name,jbxx)
            #names.append(name)


def get_all_json(name,jbxx):
    print name
    try:
        conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='tyc', port=3306, charset='utf8')
        cur = conn.cursor()
        sql1 = "SELECT * FROM tyc_10_6 WHERE name=(%s)"
        cur.execute(sql1,(name))
        conn.commit()
        comp1 = cur.fetchall()
        #conn1 = pymysql.connect(host='127.0.0.1', user='root', password='123', db='test15', port=3306, charset='utf8')
        #cur1 = conn.cursor()
        #sql2 = "SELECT * FROM tyc_jbxx WHERE name=(%s)"
        #cur1.execute(sql2,(name))
        #conn1.commit()
        #comp2 = cur.fetchall()
        print comp1
        #print comp2
        c1 = comp1[0]
        #c2 = comp2[0]
        name = c1[1]
        ssxx = c1[2]
        qybj = c1[3]
        qyfz = c1[4]
        sffx = c1[5]
        jyfx = c1[6]
        jyzk = c1[7]
        zscq = c1[8]
        #name1 = c2[1]
        #jbxx = c2[2]
        #if name == name1:
        put_db(name, ssxx, qybj, qyfz, sffx, jyfx, jyzk, zscq, jbxx)
    except Exception as e:
        print(u'异常%s'%e)
    finally:
        cur.close()
        conn.close()


def put_db(name, data1, data2, data3, data4, data5, data6, data7,data8):
    name = str(name)
    try:
        conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='test15', port=3306, charset='utf8')
        cur = conn.cursor()
        sql = 'INSERT INTO test123 (name,ssxx,qybj,qyfz,sffx,jyfx,jyzk,zscq,jbxx)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cur.execute(sql, (name, data1, data2, data3, data4, data5, data6, data7,data8))
        conn.commit()
        print(u'%s导入成功' % name)
    except Exception as e:
        print(u'导入异常%s' % e)
        print(u'失败%s' % name)
    finally:
        cur.close()
        conn.close()
'''
'''
#获取剩余183条
conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='test15', port=3306, charset='utf8')
cur = conn.cursor()

for i in canurl:
    print type(i)
    i=str(i)
    print type(i)
    sql = 'SELECT name,number FROM tyc_url WHERE name=(%s)'
    print sql
    cur.execute(sql,(i))
    conn.commit()
    comp = cur.fetchall()
    print comp
    com = comp[0]
    name = com[0]
    number = com[1]
    sql1 = 'INSERT INTO tyc_10_sid (name,number)VALUES(%s,%s)'
    cur.execute(sql1,(name,number))
    conn.commit()
cur.close()
conn.close()
'''
'''
#剩余id
names = []
conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='tyc', port=3306, charset='utf8')
cur = conn.cursor()
sql = 'SELECT name FROM tyc_10_6 limit 14761,200'
cur.execute(sql)
conn.commit()
comps = cur.fetchall()
for i in comps:
    name = i[0]
    names.append(name)
cur.close()
conn.close()
conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='test15', port=3306, charset='utf8')
cur = conn.cursor()
sql = 'SELECT name FROM tyc_10_sid'
cur.execute(sql)
conn.commit()
coms = cur.fetchall()
for i in coms:
    name1 = i[0]
    if name1 in names:
        sql1='DELETE FROM tyc_10_sid WHERE name=(%s)'
        cur.execute(sql1,(name1))
        conn.commit()
    else:
        print name1

cur.close()
conn.close()
'''
#获取总的待清洗数据
'''
names = []
def get_clean_info():
    try:
        conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='test15', port=3306, charset='utf8')
        cur = conn.cursor()
        sql='SELECT name FROM test'
        cur.execute(sql)
        conn.commit()
        comps = cur.fetchall()
    except:
        print(u'错误')
    else:
        for comp in comps:
            name = comp[0]
            names.append(name)
        print len(names)
        b = set(names)
        print len(b)
        for name in b:
            if name in names:
                a = names.index(name)
                names.pop(a)
        for c in names:
            c = str(c)
            sql = 'DELETE FROM test WHERE name=(%s)'
            print sql
            cur.execute(sql,(c))
            conn.commit()
'''
'''

#获取余下一千条待爬取的数据
def get_1000_jbxx():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='test15', port=3306, charset='utf8')
    cur = conn.cursor()
    sql1 = 'SELECT name FROM test'
    sql2 = 'SELECT name,number FROM tyc_url'
    names=[]
    cur.execute(sql1)
    conn.commit()
    comp1 = cur.fetchall()
    cur.execute(sql2)
    conn.commit()
    comp2 = cur.fetchall()
    for com1 in comp1:
        name = com1[0]
        names.append(name)
    for com2 in comp2:
        name = com2[0]
        number = com2[1]
        print name
        print number
        if name not in names:
            sql3 = 'INSERT INTO tyc_sid (name,number)VALUES(%s,%s)'
            print sql3
            cur.execute(sql3,(name,number))
            conn.commit()
    cur.close()
    conn.close()
'''
if __name__=='__main__':
	get_all()
    #get_1000_jbxx()