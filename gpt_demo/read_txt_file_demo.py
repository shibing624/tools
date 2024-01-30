# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
import os

os.environ["OPENAI_API_KEY"] = ''  # set your openai api key
# load documents
documents = SimpleDirectoryReader(input_files=['./data/sample.txt']).load_data()

index = GPTSimpleVectorIndex(documents)
index.save_to_disk('./sample_index.json')
print(index)

index = GPTSimpleVectorIndex.load_from_disk('./sample_index.json')
response = index.query(
    "文章是关于啥的内容",
)

print(response)

response = index.query(
    "n-grams来学习句子表示是哪一年的论文提出的?",
)
print(response)
