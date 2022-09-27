# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from jina import Flow
from docarray import Document, DocumentArray

f = Flow(port=12345, monitoring=True, port_monitoring=9090).add(
  uses='jinahub://TransformerTorchEncoder/latest',port_monitoring=9091)

with f:
  f.block()
  # r = f.post('/', inputs=DocumentArray([Document(text='hello')]))
  # print(r.to_json())