# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import os
from transformers import BertTokenizer

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

sequence = "A Titan RTX has 24GB of VRAM"
print('"[unused1]" in vocab?', "[unused1]" in tokenizer.vocab)
print('"[unused1]" index in vocab', tokenizer.vocab["[unused1]"] if "[unused1]" in tokenizer.vocab else "NA")

idxs = tokenizer.encode("[unused1]", add_special_tokens=False)
print("indices", idxs)
recoded = tokenizer.decode(idxs)
print("recoded", recoded)

# do basic tokenization
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased", do_basic_tokenize=False)
print(tokenizer.tokenize("[unused1]"))

print(tokenizer.encode("[unused1]", add_special_tokens=True))
print(tokenizer.decode([1]))

# add special tokens
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
tokenizer.add_special_tokens({"additional_special_tokens": ["[unused1]", "[unused2]"]})
print(tokenizer.encode("[unused1]", add_special_tokens=False))
print(tokenizer.encode("[unused1]", add_special_tokens=False))
ids = tokenizer.encode("[unused1] a big one", add_special_tokens=False)
print(ids)
recoded = tokenizer.decode(ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)
print("recoded:", recoded)

print(tokenizer.all_special_tokens)