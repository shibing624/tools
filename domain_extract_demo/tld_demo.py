# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: pip install tld
"""
from tld import get_tld, get_fld

urls = [
    "http://meiwen.me/src/index.html",
    "http://www.meiwen.me/src/index.html",
    "http://1000chi.com/game/index.html",
    "http://see.xidian.edu.cn/cpp/html/1429.html",
    "https://docs.python.org/2/howto/regex.html",
    """https://www.google.com.hk/search?client=aff-cs-360chromium&hs=TSj&q=url%E8%A7%A3%E6%9E%90%E5%9F%9F%E5%90%8Dre&oq=url%E8%A7%A3%E6%9E%90%E5%9F%9F%E5%90%8Dre&gs_l=serp.3...74418.86867.0.87673.28.25.2.0.0.0.541.2454.2-6j0j1j1.8.0....0...1c.1j4.53.serp..26.2.547.IuHTj4uoyHg""",
    "file:///D:/code/echarts-2.0.3/doc/example/tooltip.html",
    "http://api.mongodb.org/python/current/faq.html#is-pymongo-thread-safe",
    "https://pypi.python.org/pypi/publicsuffix/",
    "http://127.0.0.1:8000"
]


def get_first_domain(urls):
    res = []
    for url in urls:
        r = ''
        try:
            r = get_fld(url)
        except Exception as e:
            r = ''
        finally:
            res.append(r)
    return res


res = get_first_domain(urls)
print(res)
