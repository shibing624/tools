# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import sys
from loguru import logger
from similarities import SimHashSimilarity


class SentenceModel:
    """
    Say something about the Example Class...
    Args:
        args_0 (`type`):
        ...
    """

    def __init__(self):
        self.model = SimHashSimilarity()
        logger.info(f'SentenceModel inited. Use {self.model}')

    def sentence_encode(self, sentences):
        embeddings = [[int(i) for i in self.model.simhash(text)] for text in sentences]
        return embeddings
