# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import sys
from loguru import logger
import numpy as np
import random
from similarities import SimHashSimilarity
from sentence_transformers import SentenceTransformer
from sklearn.preprocessing import normalize


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
        raw_vectors = []
        binary_vectors = []
        for text in sentences:
            raw_vector = [int(i) for i in self.model.simhash(text)]
            raw_vectors.append(raw_vector)
            # binary_vectors.append(bytes(np.packbits(raw_vector, axis=-1).tolist()))
        raw_vectors = [[random.random() for _ in range(dim)] for _ in range(5000)]
        return raw_vectors


class SentenceBERTModel:
    """
    Say something about the ExampleCalass...
    Args:
        args_0 (`type`):
        ...
    """

    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

    def sentence_encode(self, data):
        embedding = self.model.encode(data)
        sentence_embeddings = normalize(embedding)
        return sentence_embeddings.tolist()


if __name__ == '__main__':
    model = SentenceModel()
    sentences = ['姚明多高1？', '姚明多高2？', '姚明多高3？']
    embeddings = model.sentence_encode(sentences)
    print(embeddings)

    dim = 10
    raw_vectors = []
    binary_vectors = []
    for i in range(10):
        raw_vector = [random.randint(0, 1) for i in range(dim)]
        raw_vectors.append(raw_vector)
        binary_vectors.append(bytes(np.packbits(raw_vector, axis=-1).tolist()))
    print(binary_vectors)
    print(raw_vectors)
