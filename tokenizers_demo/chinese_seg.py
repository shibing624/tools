# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import operator
import sys
import time
import os
from transformers import AutoTokenizer, T5ForConditionalGeneration, BertTokenizer
import jieba
from functools import partial
from tqdm import tqdm
import torch
from typing import List
from loguru import logger

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


class T5PegasusTokenizer(BertTokenizer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pre_tokenizer = partial(jieba.cut, HMM=False)

    def _tokenize(self, text, *arg, **kwargs):
        split_tokens = []
        for text in self.pre_tokenizer(text):
            if text in self.vocab:
                split_tokens.append(text)
            else:
                split_tokens.extend(super()._tokenize(text))
        return split_tokens

tokenizer = T5PegasusTokenizer.from_pretrained("bert-base-chinese")
r = tokenizer.tokenize("我是中国人，百度App")
print(r)
