# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import numpy as np


def try_divide(x, y, val=0.0):
    """
    try to divide two numbers
    """
    if y != 0.0:
        val = float(x) / y
    return val


def max_min_normalize(x, max_value=1.0, min_value=0.0):
    x = try_divide(x - min_value, max_value - min_value)
    return x


def z_score_normalize(x, mu, sigma):
    """
    z-score normalize
    :param x:
    :param mu: np.average(x=list)
    :param sigma: np.std(x=list)
    :return:
    """
    x = try_divide(x - mu, sigma)
    return x


def sigmoid(x):
    x = try_divide(1.0, 1.0 + np.exp(-x))
    return x


a = [0.01001541, -0.99099492, -1.12597902, -0.03748764, 1, 0]
# from sklearn.preprocessing import MinMaxScaler
# scaler = MinMaxScaler()
# print(a)
# a = np.array(a)
# # scaler.fit(a)
# d = scaler.transform(a)
# print(d)

for i in a:
    print(i)
    print("max_min_normalize:", max_min_normalize(i))
    print("simoid:", sigmoid(i))
