# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
bert_model = 'luhua/chinese_pretrain_mrc_macbert_large'
tokenizer = AutoTokenizer.from_pretrained(bert_model)
model = AutoModelForQuestionAnswering.from_pretrained(bert_model)

text = r"""
大家好，我是张亮，目前任职当当网架构部架构师一职，也是高可用架构群的一员。我为大家提供了一份imagenet数据集，希望能够为图像分类任务做点贡献。
"""

questions = [
    "张亮在哪里任职?",
    "张亮为图像分类提供了什么数据集?",
    "🤗 Transformers provides interoperability between which frameworks?",
]

for question in questions:
    inputs = tokenizer(question, text, add_special_tokens=True, return_tensors="pt")
    input_ids = inputs["input_ids"].tolist()[0]
    outputs = model(**inputs)
    answer_start_scores = outputs.start_logits
    answer_end_scores = outputs.end_logits
    # Get the most likely beginning of answer with the argmax of the score
    answer_start = torch.argmax(answer_start_scores)
    # Get the most likely end of answer with the argmax of the score
    answer_end = torch.argmax(answer_end_scores) + 1
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))
    print(f"Question: {question}")
    print(f"Answer: {answer}")