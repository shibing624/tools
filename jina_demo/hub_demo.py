# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from docarray import Document, DocumentArray

da = DocumentArray([Document(text='hello')])
r = da.post('jinahub://TransformerTorchEncoder')

print(r.to_json())


