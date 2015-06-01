# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "gaofeng"
__date__ = "$May 24, 2015 12:02:41 AM$"

import requests
import re
import time
from datetime import datetime
import requests

class Monitor:
    
    lastPrice = 100    
    
    def query_stock(self, stock_code):
        url = 'http://www.sgx.com/wps/stocksearch/SearchProcessor'
        params = {'stock' : stock_code}
        r = requests.get(url, params=params)
        if (r.status_code == 200):
            m = re.search('LT:(\d+.?\d*).*C:([+-]?\d+.?\d*)', r.text)
            return (float(m.group(1)), float(m.group(2)))
        else:
            return ('','')

    def send_msg(self, msg):
        params = {'id':'gaofeng', 'msg':msg}
        # host = 'http://localhost:8096'
        host = 'http://btproxy.gaofeng.com'
        loginUrl = '%s/users/6500618000/login' % (host)
        msgUrl = '%s/users/6500618000/chat/text' % (host)
        try :
            r = requests.get(loginUrl)
            r = requests.get(msgUrl, params=params)
        except:
            pass

    def check(self):
        try:
            stock = self.query_stock('BN4')
            msg = 'time: %s price: %s, change: %s' % (datetime.now().strftime('%m-%d %H:%M:%S'), stock[0], stock[1])
            print msg
            if stock[0] < self.lastPrice:
                self.send_msg(msg)
            self.lastPrice = stock[0]
        except:
            pass


if __name__ == "__main__":
    monitor = Monitor()
    while True:
        monitor.check()
        time.sleep(60)