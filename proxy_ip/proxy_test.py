# -*- coding:utf-8 -*-

import requests

url = 'http://www.tianyancha.com'

def test_proxy(ip,port):
    ip = str(ip)
    port = str(port)
    IP = 'http://'+ip+':'+port
    proxy = {'http':IP}
    #NETWORK_STATUS = True

    '''
    try:
        requests.get(url, proxies=proxy, timeout=10)
    except:
        NETWORK_STATUS = False
    return NETWORK_STATUS
    '''

    try:
        response = requests.get(url,proxies=proxy, timeout=10)
        if response.status_code == 200:
            NETWORK_STATUS = True
        else:
            NETWORK_STATUS = False
    except:
        NETWORK_STATUS = False
    return NETWORK_STATUS

