# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import ProxyType
from url_proxy import get_url#,get_proxy,put_db
import time
import random
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
urls = get_url()

	
def get_json(content):
	print(u'开始获取soup')
	soup = BeautifulSoup(content,'html.parser')
	jbxx = {}
	#表格中基本信息(4)：
	a = soup.find('div', class_="baseInfo_model2017").find('tbody').find_all('td')
	#法人代表
	frdb = a[0].find('a').text
	jbxx[u'法人代表'] = frdb
	#注册资本
	zczb = a[1].text
	jbxx[u'注册资本'] = zczb
	#注册时间
	zcsj = a[2].text
	jbxx[u'注册时间'] = zcsj
	#经营状态
	jyzt = a[3].text
	jbxx[u'经营状态'] = jyzt
	
	print(u'获取余下json信息')
	#余下信息(10)：
	b = soup.find('div', class_="row b-c-white company-content base2017").find('tbody').find_all('div',class_='c8')
	for i in b:
		#print i.text
		c = i.text.split(u'：')
		#print len(c)
		#jbxx[c[0]]=c[1]
		jbxx[c[0]] = i.find('span').text
	jbxx_js = json.dumps(jbxx,ensure_ascii=False)	
	return jbxx_js

	

def get_data(driver):
	while not len(urls) == 0:
		try:
			com = urls[0]
			company = com[0]
			url = com[1]
			print(u'开始请求链接%s'%url)
			try:
				driver.get(url)
			except:
				print(u'加载时间太长了，可能会有问题')
				driver.execute_script("window.stop()")
			#driver.save_screenshot(r'%s.png'%company)
			time.sleep(5)
			try:
				for driv in driver.find_elements_by_link_text('详细'):
				#print driv.get_attribute('ng-click')
					print('CLICK')
					driv.click()
				#time.sleep(1)
				print(u'获取详细信息')
			except:
				print(u'没有详细信息')
			#driver.save_screenshot(r'%s5.png'%company)
			content = driver.page_source.encode('utf-8')
			#print content				
			jbxxjs = get_json(content)
		except:
			print(u'在%s请求页面异常，换个代理'%company)
			driver.close()
			get_data()
		else:
			print(u'信息已经获取，准备入库')
			#put_db(company,jbxxjs)
			urls.pop(0)
			print(u'%s入库成功'%company)
			
		
if __name__=='__main__':
	proxies = '117.143.109.146:80'
	print(u'当前代理为%s'%proxies)
	try:
		dcap = dict(webdriver.DesiredCapabilities.PHANTOMJS)
		dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0")
		dcap["phantomjs.page.settings.loadImages"] = False 
		service_args = [
			'--proxy='+proxies
			] #默认为http代理，可以指定proxy type
		print service_args[0]
		driver = webdriver.PhantomJS(service_args=service_args, desired_capabilities=dcap)
		#设置延时10秒
		driver.set_page_load_timeout(100)
		driver.set_script_timeout(100)
	except Exception as e:
		print(u'代理设置异常%s'%e)
	else:
		get_data(driver)
	finally:
		driver.quit()