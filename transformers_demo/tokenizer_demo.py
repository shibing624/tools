# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from transformers import BertTokenizer
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

sequence = "A Titan RTX has 24GB of VRAM"
tokenized_sequence = tokenizer.tokenize(sequence)
print('tokenized_sequence:', tokenized_sequence)
inputs = tokenizer(sequence)
print('inputs:', inputs)

encoded_sequence = inputs["input_ids"]
print('encoded_sequence:', encoded_sequence)
decoded_sequence = tokenizer.decode(encoded_sequence)
print('decoded_sequence:', decoded_sequence)

sequence_a = "This is a short sequence."
sequence_b = "This is a rather long sequence. It is at least longer than the sequence A."

encoded_sequence_a = tokenizer(sequence_a)["input_ids"]
encoded_sequence_b = tokenizer(sequence_b)["input_ids"]
print('encoded_sequence_a:', encoded_sequence_a)
print(len(encoded_sequence_a), len(encoded_sequence_b))

padded_sequences = tokenizer([sequence_a, sequence_b], padding=True)
print('padded_sequences:', padded_sequences)
