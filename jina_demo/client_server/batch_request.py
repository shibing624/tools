# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from docarray import Document, DocumentArray
from jina import Flow, Client


c = Client(port=12345)
c.post(on='/bar', inputs=DocumentArray(Document(text='hello') for _ in range(100)), request_size=10, on_done=print)
