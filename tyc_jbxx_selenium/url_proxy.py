# -*- coding:utf-8 -*-

import pymysql

def get_url():
	try:
		conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='tyc', port=3306, charset='utf8')
		cur = conn.cursor()
		sql = 'SELECT name,url FROM tyc_url_new'
		cur.execute(sql)
		conn.commit()
		coms = cur.fetchall()
	except Exception as e:
		print(u'获取url异常%s' %e)
	finally:
		cur.close()
		conn.close()
		urls = []
		for com in coms:
			name = com[0].strip()
			number = com[1].strip()
			#url = u'http://www.tianyancha.com/company/%s'%number
			url = number
			comp = [name,url]
			if len(name) < 4:
				pass
			else:
				urls.append(comp)
		return urls
		
def get_proxy():
	try:
		conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='db', port=3306, charset='utf8')
		cur = conn.cursor()
		sql = 'SELECT ip,port FROM proxy_test'
		cur.execute(sql)
		conn.commit()
		pros = cur.fetchall()
	except Exception as e:
		print(u'获取代理异常%s' %e)
	finally:
		cur.close()
		conn.close()
		proxys = []
		for pro in pros:
			ip = pro[0].strip()
			port = pro[1].strip()
			proxy = ip+':'+port
			proxys.append(proxy)
		return proxys
		
def put_db(company,content):
	try:
		conn = pymysql.connect(host='127.0.0.1', user='root', password='123', db='tyc', port=3306, charset='utf8')
		cur = conn.cursor()
		sql = 'INSERT INTO tyc_jbxx626_new (name,jbxx)VALUES(%s,%s)'
		cur.execute(sql,(company,content))
		conn.commit()
		print(u'导入基本信息成功')
	except Exception as e:
		print(u'导入基本信息失败%s' %e)
	finally:
		cur.close()
		conn.close()

		