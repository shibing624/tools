# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from jina import Flow, Executor, requests

from docarray import Document


class MyExecutor(Executor):
    @requests(on='/bar')
    def foo(self, docs, parameters, **kwargs):
        print(docs)
        print(parameters)
        print('len:', len(docs), docs[0], docs.contents)
        docs.append(Document(text=f'bar was here and got {len(docs)} document'))


f = Flow(port=12345).add(name='myexec1', uses=MyExecutor)

with f:
    f.block()
