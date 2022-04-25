# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

import torch
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained('bert-base-chinese')
text1 = '花呗更改'
text2 = '我什么'
inputs = tokenizer(text1, text2, max_length=64, truncation=True,padding=True, return_tensors='pt')
print(inputs)
a= tokenizer(text1, max_length=64)
print(a)
