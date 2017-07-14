# -*- coding:utf-8 -*-
import pymysql
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

companys = []
conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='tyc', port=3306, charset='utf8')
cur = conn.cursor()
sql = 'SELECT id,qybj FROM com_infs'
cur.execute(sql)
coms = cur.fetchall()
#cur.close()
#conn.close()
print len(coms)


for con in coms:
    id = con[0]
    q = con[1]
    a = json.dumps(q,ensure_ascii=False)
    b = json.loads(a)
    c = json.loads(b)
    if c[u'主要人员'] == 'null':
        #conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='tyc', port=3306, charset='utf8')
        #cur = conn.cursor()
        #name = str(id)
        sql1 = 'DELETE FROM com_infs WHERE id="%s"'%id
        print sql1
        cur.execute(sql1)
        conn.commit()
    else:
        companys.append(id)

cur.close()
conn.close()
print len(companys)


