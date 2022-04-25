# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from tokenizers import Tokenizer, models,normalizers,pre_tokenizers,decoders, trainers

tokenizer = Tokenizer(models.Unigram())
print(tokenizer)
tokenizer.normalizer = normalizers.NFKC()
tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()
# tokenizer.decoder = decoders.Decoder()

trainer = trainers.UnigramTrainer(
    vocab_size=200,
)
train_file = "../data/english_text.txt"
tokenizer.train([train_file], trainer)
out = tokenizer.encode("This is a sentence . Hllo world!")
print(out)
print(out.tokens)
print(out.ids)
print(tokenizer.decode(out.ids))
