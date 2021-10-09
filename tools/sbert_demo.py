# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

from sentence_transformers import SentenceTransformer
import pandas as pd
from sklearn.preprocessing import normalize

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
print(model)
sentence_embeddings = model.encode(['hello world', 'hi what is?'])
print(len(sentence_embeddings))
