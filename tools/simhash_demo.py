# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: simhash在文本长度大于500字符时效果好
"""
from simhash import Simhash
import re


def filter_html(html):
    """
    :param html: html
    :return: 返回去掉html的纯净文本
    """
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', html).strip()
    return dd


def simhash_similarity(text1, text2):
    """
    求两篇文章相似度，simhash把文本高维特征映射到64位编码，汉明距离小于等于3则两个文本相同
    :param tex1: 文本1
    :param text2: 文本2
    :return: 返回两篇文章的相似度
    """
    aa_simhash = Simhash(text1)
    bb_simhash = Simhash(text2)

    max_hashbit = max(len(bin(aa_simhash.value)), (len(bin(bb_simhash.value))))

    print(max_hashbit)

    # 汉明距离
    distance = aa_simhash.distance(bb_simhash)
    print(distance)

    sim_ratio = 1 - distance / max_hashbit
    return sim_ratio, distance


def zh_simhash_similarity(text1, text2):
    """
    求两篇中文文章相似度，simhash把文本高维特征映射到64位编码，汉明距离小于等于3则两个文本相同
    :param text1:
    :param text2:
    :return:
    """
    import jieba
    jieba.setLogLevel('INFO')
    from nlpcommon import stopwords

    words1 = [i.strip() for i in jieba.lcut(text1, cut_all=False, HMM=False) if i not in stopwords]
    words2 = [i.strip() for i in jieba.lcut(text2, cut_all=False, HMM=False) if i not in stopwords]
    words_1 = [i for i in words1 if i]
    words_2 = [i for i in words2 if i]

    simhash1 = Simhash(words_1)
    simhash2 = Simhash(words_2)
    max_hashbit = max(len(bin(simhash1.value)), (len(bin(simhash2.value))))

    # 汉明距离, 高维特征映射到64位编码，汉明距离小于等于3则两个文本相同
    distance = simhash1.distance(simhash2)
    print(distance)
    sim_ratio = 1 - distance / max_hashbit
    return sim_ratio, distance


if __name__ == '__main__':
    text1 = "simhash算法的主要思想是降维，将高维的特征向量映射成一个低维的特征向量，通过两个向量的Hamming Distance来确定文章是否重复或者高度近似。2不是 .我说3是2  "
    text2 = "simhash算法的主要思想是降维，将高维的特征映射成一个低维的特征向量，通过两个向量的Hamming Distance 。这 是 来确定文章是否重复或者高度近似。1 你 2 说3是不是 . ,"

    print(simhash_similarity(text1, text2))

    print(zh_simhash_similarity(text1, text2))
