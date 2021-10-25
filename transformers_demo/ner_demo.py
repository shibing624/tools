# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from transformers import AutoModelForTokenClassification, AutoTokenizer
import torch
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
model = AutoModelForTokenClassification.from_pretrained("bert-base-uncased")
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

sequence = "Hugging Face Inc. is a company based in New York City. Its headquarters are in DUMBO, " \
           "therefore very close to the Manhattan Bridge."

inputs = tokenizer(sequence, return_tensors="pt")
tokens = inputs.tokens()

outputs = model(**inputs).logits
predictions = torch.argmax(outputs, dim=2)
for token, prediction in zip(tokens, predictions[0].numpy()):
    print((token, model.config.id2label[prediction]))
