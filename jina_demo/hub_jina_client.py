# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from docarray import Document, DocumentArray
from jina import Client

c = Client(port=12345)
r = c.post('/', inputs=DocumentArray([Document(text='hello')]))
print(r, r.texts)
print(r.to_json())