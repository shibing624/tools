# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from tokenizers import Tokenizer
from tokenizers.models import BPE

tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
print(tokenizer)

from tokenizers.trainers import BpeTrainer, UnigramTrainer, WordLevelTrainer, WordPieceTrainer

trainers = [(BpeTrainer(), "BPE")
            # (UnigramTrainer(), "Unigram"),
            # (WordLevelTrainer(), "WordLevel"),
            # (WordPieceTrainer(), "WordPiece")
            ]

from tokenizers.pre_tokenizers import Whitespace, CharDelimiterSplit

tokenizer.pre_tokenizer = Whitespace()
train_file = "../data/english_text.txt"

# Different training methods
for trainer, name in trainers:
    # if name == "Unigram":
    #     tokenizer.pre_tokenizer = CharDelimiterSplit(' ')
    tokenizer.train([train_file], trainer)
    # tokenizer.save(f"{name}_model.json")

# Use it
tokenizer.from_file("bpe_model.json")
out = tokenizer.encode("This is a sentence. Hllo world!")
print(out)
print(out.tokens)
print(out.ids)
