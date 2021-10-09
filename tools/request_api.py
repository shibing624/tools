# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import urllib.parse

import json
import requests
import time
import re
se = requests.session()

if __name__ == '__main__':
    url = "http://180.76.108.51:5001/api/oneq/lexer}?q="
    data = '床前明'
    get_url = url + urllib.parse.quote(data)
    t = se.get(get_url).text
    print(t)
    print(type(t))
    p = json.loads(t)
    print(p, type(p))

    r = se.get(url + data).text
    print(r, type(r))
    p = json.loads(r)
    print(p, type(p))
