# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import time
import sys

sys.path.append('..')
from jina import Client
from docarray import Document, DocumentArray

def encode(c, sentences):
    def gen_docs(sent_list):
        for s in sent_list:
            if isinstance(s, str):
                yield Document(text=s)

    r = c.post('/', inputs=gen_docs(sentences), request_size=256)
    return r

c = Client(port=50001)

data = ['如何更换花呗绑定银行卡',
        '花呗更改绑定银行卡']
print("data:", data)
num_tokens = sum([len(i) for i in data])
for j in range(5):
    tmp = data * (2 ** j)
    c_num_tokens = num_tokens * (2 ** j)
    start_t = time.time()
    r = encode(c, tmp)
    if j == 0:
        print('batch embs:', r.embeddings)
    print('count size:', len(r))
    time_t = time.time() - start_t
    print('encoding %d sentences, spend %.2fs, %4d samples/s, %6d tokens/s' %
          (len(tmp), time_t, int(len(tmp) / time_t), int(c_num_tokens / time_t)))
