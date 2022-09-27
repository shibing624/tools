# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

from jina import Client
from docarray import Document, DocumentArray

c = Client(port=50001)
r = c.post('/', inputs=DocumentArray([Document(text='如何更换花呗绑定银行卡')]))
print('jina client:', r, r.to_dict())
