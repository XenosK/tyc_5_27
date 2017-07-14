# -*- coding:utf-8 -*-
'''比较已爬取的5000条数据和总数据，得出还有多少数据没有爬取，入库'''

import pymysql
import time



'''
cons = []

def get_cons():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='test15', port=3306, charset='utf8')
    cur = conn.cursor()
    sql = 'SELECT name FROM company_cons'
    cur.execute(sql)
    conn.commit()
    coms = cur.fetchall()
    cur.close()
    conn.close()
    for com in coms:
        com = com[0]
        cons.append(com)

def get_all():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='test15', port=3306, charset='utf8')
    cur = conn.cursor()
    sql = 'SELECT name,number FROM tyc_10_c'
    cur.execute(sql)
    alls = cur.fetchall()
    for a in alls:
        if a[0] not in cons:
            m=a[0]
            n=str(a[1])
            sql = 'INSERT INTO tyc_10_c1 (name,number)VALUES(%s,%s)'
            print sql
            cur.execute(sql,(m,n))
            conn.commit()
        else:
            pass
    cur.close()
    conn.close()

id_cons = []
def get_id_cons():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='test15', port=3306, charset='utf8')
    cur = conn.cursor()
    sql = 'SELECT name FROM id_cons_c'
    cur.execute(sql)
    conn.commit()
    dns = cur.fetchall()
    for name in dns:
        name = name[0]
        id_cons.append(name)
    cur.close()
    conn.close()

tyc_10 = []
def get_tyc_10():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='tyc', port=3306, charset='utf8')
    cur = conn.cursor()
    sql = 'SELECT name FROM tyc_10_6'
    cur.execute(sql)
    conn.commit()
    cons = cur.fetchall()
    for a in cons:
        tyc_10.append(a[0])
    print len(tyc_10)
'''

nums = []
def get_number_name():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='test15', port=3306, charset='utf8')
    cur = conn.cursor()
    sql = 'SELECT name FROM tyc_url'
    cur.execute(sql)
    conn.commit()
    numbers = cur.fetchall()
    for n in numbers:
        name = n[0]
        nums.append(name)
    print len(nums)


def get_all_name():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='test15', port=3306, charset='utf8')
    cur = conn.cursor()
    sql = 'SELECT company_name FROM fq_provider'
    cur.execute(sql)
    alls = cur.fetchall()
    for a in alls:
        if a[0] not in nums:
            m=a[0]
            sql = 'INSERT INTO number_name (name)VALUES(%s)'
            print sql
            cur.execute(sql,(m))
            conn.commit()
        else:
            pass
    cur.close()
    conn.close()

if __name__=='__main__':
    get_number_name()
    time.sleep(5)
    get_all_name()
