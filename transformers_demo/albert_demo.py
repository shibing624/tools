# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from transformers import BertTokenizer, AlbertForMaskedLM, FillMaskPipeline
tokenizer = BertTokenizer.from_pretrained("uer/albert-base-chinese-cluecorpussmall")
model = AlbertForMaskedLM.from_pretrained("uer/albert-base-chinese-cluecorpussmall")
unmasker = FillMaskPipeline(model, tokenizer)
print(unmasker("中国的首都是[MASK]京。"))

from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("uer/albert-base-chinese-cluecorpussmall")
model = AlbertForMaskedLM.from_pretrained("uer/albert-base-chinese-cluecorpussmall")
unmasker = FillMaskPipeline(model, tokenizer)
print(unmasker("中国的首都是[MASK]京。"))