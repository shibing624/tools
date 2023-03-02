# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

import json

sents = """
苍穹传之指尖江湖。   仙侠
苍穹传之指尖江湖1。  仙侠2
"""

ms = [(query, label) for query, label in [sent.strip().split() for sent in sents.splitlines() if sent.strip()]]
print(ms)
with open('a.json', 'w', encoding='utf-8') as f:
    for i in ms:
        d = {'token': i[0], 'doc_label': i[1]}
        f.write(json.dumps(d, ensure_ascii=False) + '\n')
