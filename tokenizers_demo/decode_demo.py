# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from tokenizers import Tokenizer, trainers
from tokenizers.models import WordLevel,WordPiece
tokenizer = Tokenizer(WordPiece())

trainer = trainers.WordPieceTrainer()
train_file = "../data/english_text.txt"
tokenizer.train([train_file], trainer)

s = "This is a sentence . Hllo world!"
out = tokenizer.encode(s)
print(out)
print(out.tokens)
print(out.ids)
print(tokenizer.decode(out.ids))

