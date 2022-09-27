# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from docarray import Document
from jina import Client

c = Client(port=12345)
r = c.post(on='/bar', inputs=Document(text='hello'), parameters={'p': 0.5})
print(r, r.texts)

d1 = Document(content='hello')
d2 = Document(content='world')
r = c.post('/bar', [d1, d2])
print(r, r.contents)
