__author__ = "gaofeng"
__date__ = "$May 20, 2015 10:13:48 PM$"

import requests
import re
import time
from datetime import datetime

def query_stock(stock_code):
    url = 'http://www.sgx.com/wps/stocksearch/SearchProcessor'
    params = {'stock' : stock_code}
    r = requests.get(url, params=params)
    if (r.status_code == 200):
        m = re.search('LT:(\d+.?\d*).*C:([+-]?\d+.?\d*)', r.text)
        return (float(m.group(1)), float(m.group(2)))
    else:
        return ('','')
    
    
    
if __name__ == "__main__":
    while True:
        try:
            stock = query_stock('S51')
            print 'time: %s price: %s, change: %s' % (datetime.now().strftime('%m-%d %H:%M:%S'), stock[0], stock[1])
        except:
            pass
        time.sleep(10)
    
    