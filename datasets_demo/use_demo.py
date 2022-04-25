# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

from sklearn import metrics
from datasets import load_dataset

# dataset = load_dataset("shibing624/source_code", "python")
# print(dataset)
# print(dataset['test'][0:10])

metrics.f1_score()
dataset = load_dataset("shibing624/nli_zh", "ATEC", split='train')
print(dataset)
print(dataset[0]['label'])

# dataset = load_dataset("glue", "stsb")
# print(dataset)
# print(dataset['test'][0])
