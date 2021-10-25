# -*- coding: utf-8 -*-
from transformers import BertTokenizer, BertModel
import os
tokenizer = BertTokenizer.from_pretrained("Langboat/mengzi-bert-base")
model = BertModel.from_pretrained("Langboat/mengzi-bert-base")
print(model)
tokenizer.save_pretrained('../../transformers_models/mengzi-bert-base')
model.save_pretrained(os.path.expanduser('../../transformers_models/mengzi-bert-base'))
