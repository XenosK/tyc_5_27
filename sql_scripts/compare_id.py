# -*- coding:utf-8 -*-
import pymysql
import time

urls = []
def get_idr():
    try:
        conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='test15', port=3306, charset='utf8')
        cur = conn.cursor()
        sql = 'SELECT name FROM tyc_10_c1'
        cur.execute(sql)
        conn.commit()
        coms = cur.fetchall()
        for com in coms:
            name = com[0]
            #number = comp[1]
            #a=[name,number]
            urls.append(name)
    except Exception as e:
        print(u'提取url异常%s'%e)
    finally:
        cur.close()
        conn.close()

def get_ids():
    try:
        conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='test15', port=3306, charset='utf8')
        cur = conn.cursor()
        sql = 'SELECT name,number FROM tyc_10_c'
        cur.execute(sql)
        conn.commit()
        comps = cur.fetchall()
        for comp in comps:
            name = comp[0]
            number = comp[1]
            if name in urls:
                pass
            else:
                sql = 'INSERT INTO tyc_10_c2 (name,number)VALUES(%s,%s)'
                cur.execute(sql,(name,number))
                conn.commit()
                print(u'%s导入成功'%name)
    except Exception as e:
        print(u'导入剩余公司异常%s'%e)
    finally:
        cur.close()
        conn.close()

if __name__=='__main__':
    get_idr()
    time.sleep(5)
    get_ids()