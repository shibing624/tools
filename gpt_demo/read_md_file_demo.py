# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: pip install llama_index
"""
from pathlib import Path
from llama_index import download_loader
from llama_index import GPTSimpleVectorIndex
import os

os.environ["OPENAI_API_KEY"] = ''  # set your openai api key
MarkdownReader = download_loader("MarkdownReader")

loader = MarkdownReader()
documents = loader.load_data(file=Path('../README.md'))
print(documents)
index = GPTSimpleVectorIndex(documents)
r = index.query('What are these files about?')
print(r)
while True:
    input_str = input('input:')
    r = index.query(input_str)
    print(r)
    print('')
