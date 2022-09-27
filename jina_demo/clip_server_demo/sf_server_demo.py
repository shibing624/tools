# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from jina import Flow
from docarray import Document, DocumentArray

f = Flow(port=50001).add(
    uses='jinahub://TransformerSentenceEncoder/latest',
    uses_with={'model_name': 'shibing624/text2vec-base-chinese'}
)

with f:
    r = f.post('/', inputs=DocumentArray([Document(text='如何更换花呗绑定银行卡'), Document(text='花呗更改绑定银行卡')]))
    print(r.embeddings)
    f.block()
