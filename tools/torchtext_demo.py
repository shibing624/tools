# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import torchtext


train_txt, val_txt, test_txt = torchtext.datasets.WikiText2(root='data', split=('train', 'valid', 'test'))

from sklearn.linear_model import LogisticRegression