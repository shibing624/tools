# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

from transformers import BertTokenizer, GPT2LMHeadModel, TextGenerationPipeline
import torch
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# tokenizer = BertTokenizer.from_pretrained("uer/gpt2-chinese-couplet")
# model = GPT2LMHeadModel.from_pretrained("uer/gpt2-chinese-couplet")
# text_generator = TextGenerationPipeline(model, tokenizer)
# srcs = ['书香醉我凌云梦',
#         '春回大地，对对黄莺鸣暖树',
#         '松风吼夜潮，巧剜明月染春水',
#         '丹枫江冷人初去',
#         ]
#
# format_srcs = ['[CLS]' + ' '.join(src) for src in srcs]
# for i in format_srcs:
#     r = text_generator(i, max_length=25, do_sample=True)
#     print(r)
# [{'generated_text': '[CLS]丹 枫 江 冷 人 初 去 - 黄 叶 声 从 天 外 来 阅 旗'}]

from textgen import T5Model

model = T5Model("t5", "shibing624/t5-chinese-couplet")
r = model.predict(["对联：丹枫江冷人初去"])
print(r)
r = model.predict(["丹枫江冷人初去"])
print(r)

from transformers import T5ForConditionalGeneration, T5Tokenizer

tokenizer = T5Tokenizer.from_pretrained("shibing624/t5-chinese-couplet")
model = T5ForConditionalGeneration.from_pretrained("shibing624/t5-chinese-couplet")


def batch_generate(input_texts, max_length=64):
    features = tokenizer(input_texts, return_tensors='pt')
    outputs = model.generate(input_ids=features['input_ids'],
                             attention_mask=features['attention_mask'],
                             max_length=max_length)
    return tokenizer.batch_decode(outputs, skip_special_tokens=True)


r = batch_generate(["对联：丹枫江冷人初去"])
print(r)
