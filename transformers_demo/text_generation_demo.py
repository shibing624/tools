# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from transformers import AutoModelForCausalLM, AutoTokenizer
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
model = AutoModelForCausalLM.from_pretrained("hfl/chinese-xlnet-base")
tokenizer = AutoTokenizer.from_pretrained("hfl/chinese-xlnet-base")

# Padding text helps XLNet with short prompts - proposed by Aman Rusia in https://github.com/rusiaaman/XLNet-gen#methodology
PADDING_TEXT = """1991年，俄国沙皇尼古拉斯二世及其家人的遗体
（除了阿列克谢和玛丽亚）被发现。
尼古拉斯的小儿子沙雷维奇·阿列克谢·尼古拉耶维奇的声音讲述了故事的其余部分。1883年西伯利亚西部，
一个年轻的格里戈里·拉斯普京被他的父亲和一群人邀请表演魔术。
拉斯普京有远见，谴责其中一人是偷马贼。虽然他的父亲最初因为这样的指控而打了他一巴掌，但拉斯普金看着这名男子被追赶到外面并被殴打。
二十年后，拉斯普京看到了圣母玛利亚的幻象，促使他成为一名牧师。拉斯普京很快成名，人们，甚至主教，都在乞求他的祝福。<eod> </s> <eos>"""
prompt = "今天俄国人开始在西伯利亚表演"

inputs = tokenizer(PADDING_TEXT + prompt, add_special_tokens=False, return_tensors="pt")["input_ids"]

prompt_length = len(tokenizer.decode(inputs[0]))
outputs = model.generate(inputs, max_length=250, do_sample=True, top_p=0.95, top_k=60)
generated = prompt + tokenizer.decode(outputs[0])[prompt_length+1:]

print(generated)