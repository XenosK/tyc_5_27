# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import ProxyType
from url_proxy import get_url,get_proxy,put_db
import time
import random
import json
import sys


proxies = '117.143.109.147:80'
dcap = dict(webdriver.DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0")
#dcap["phantomjs.page.settings.resourceTimeout"] = ("10")
dcap["phantomjs.page.settings.loadImages"] = False
service_args = [
	'--proxy='+proxies
	] #默认为http代理，可以指定proxy type
print service_args[0]
driver = webdriver.PhantomJS(service_args=service_args, desired_capabilities=dcap)
#设置延时10秒
driver.set_page_load_timeout(100)
driver.set_script_timeout(100)
print(u'开始请求链接')
url = 'http://www.tianyancha.com/company/22944923'
#driver.get(url)
try:
    driver.get(url)
except:
    print(u'加载时间太长了，可能会有问题')
    driver.execute_script("window.stop()")
# driver.save_screenshot(r'%s.png'%company)
time.sleep(5)


#print content


#print driver.find_element_by_xpath("//div[@class='baseInfo_model2017]/tbody/td[]")

#点击详细信息
for driv in driver.find_elements_by_link_text('详细'):
    print driv.get_attribute('ng-click')
    print('CLICK')
    driv.click()
time.sleep(1)
content = driver.page_source.encode('utf-8')
soup = BeautifulSoup(content,'html.parser')

a = soup.find('div', class_="baseInfo_model2017").find('tbody').find_all('td')
frdb = a[0].find('a').text
print frdb


b = soup.find('div', class_="row b-c-white company-content base2017").find('tbody').find_all('div',class_='c8')
jbxx = {}
for i in b:
	#print i.text
	c = i.text.split(u'：')
	#print len(c)
	jbxx[c[0]]=i.find('span').text
jbxx_js = json.dumps(jbxx,ensure_ascii=False)
print jbxx_js
print jbxx[u'经营范围']


driver.quit()
