# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from clip_client import Client

c = Client('grpc://0.0.0.0:51000')

r = c.encode(
    [
        '如何更换花呗绑定银行卡',
    ]
)
print('clip_client:', r)
