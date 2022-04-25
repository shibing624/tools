# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from typing import Union,List

class SimilarityABC:
    def __init__(self, corpus=None):
        """

        Parameters
        ----------
        corpus : iterable of list of (int, number)
            Corpus in sparse Gensim bag-of-words format.

        """
        raise NotImplementedError("cannot instantiate Abstract Base Class")

    def get_similarities(self, doc):
        """Get similarities of the given document or corpus against this index.

        Parameters
        ----------
        doc : {list of (int, number), iterable of list of (int, number)}
            Document in the sparse Gensim bag-of-words format, or a streamed corpus of such documents.

        """
        raise NotImplementedError("cannot instantiate Abstract Base Class")

    def most_sim(self, q: str, topn: int = 10):
        """
        获取最相似的topn个文档
        :param query:
        :param topn:
        :return:
        """
        result = 1.0
        result += 100
        return result

    def get_key(self):
        return self.__class__.__name__ + "100"


class BertSim(SimilarityABC):
    def __init__(self, corpus, docs, num_epochs=10):
        # super(BertSim, self).__init__()
        self.corpus = corpus
        self.docs = docs

    def get_similarities(self, doc):
        return 1.0

    def get_vec(self, doc1, doc2):
        return 1.0

    def kkk(self):
        return "kkk"

    def most_sim(self, query: str = "hi", topn: int = 10):
        query += "hiii"
        return query


class ABSim(BertSim):
    def __init__(self, corpus, docs):
        super().__init__(corpus, docs)

    def most_sim(self, k: Union[str,List[str]] = "hi", topn: int = 10):
        k += "kkk"
        return k

    def get_similarities(self, doc):
        return 1.0

    def get_vec(self, doc1, doc2):
        return 1.0

    def kkk(self):
        return "mmm"


if __name__ == '__main__':
    m = ABSim([], [])
    print(m.get_key())
    print(m.most_sim("", 10))
    n = BertSim([], [])
    print(n)
    print(n.get_key())
    print(n.most_sim("", 10))
