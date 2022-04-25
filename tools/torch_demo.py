# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from typing import List, Union
import numpy as np
import torch
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["TOKENIZERS_PARALLELISM"] = "TRUE"

# 假设是时间步T1的输出
T1 = torch.tensor([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
# 假设是时间步T2的输出
T2 = torch.tensor([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])
print(torch.stack((T1, T2), dim=0))
print(torch.stack((T1, T2), dim=0).shape)
print(torch.stack((T1, T2), dim=1))
print(torch.stack((T1, T2), dim=1).shape)
print(torch.stack((T1, T2), dim=2).shape)
# print(torch.stack((T1,T2),dim=3).shape)

print(torch.vstack((T1, T2)))
from tqdm import tqdm

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in tqdm(a):
    print(i)

k = torch.tensor([[0.1839]])
print(k.shape)
print(k)
print(float(k))
m = torch.Tensor([[0.1839]])
print(m)
print(torch.FloatTensor([[0.1839]]))


def cos_sim(a: Union[torch.Tensor, np.ndarray], b: Union[torch.Tensor, np.ndarray]):
    """
    Computes the cosine similarity cos_sim(a[i], b[j]) for all i and j.
    :return: Matrix with res[i][j]  = cos_sim(a[i], b[j])
    """
    if not isinstance(a, torch.Tensor):
        a = torch.tensor(a)

    if not isinstance(b, torch.Tensor):
        b = torch.tensor(b)

    if len(a.shape) == 1:
        a = a.unsqueeze(0)

    if len(b.shape) == 1:
        b = b.unsqueeze(0)

    a_norm = torch.nn.functional.normalize(a, p=2, dim=1)
    b_norm = torch.nn.functional.normalize(b, p=2, dim=1)
    return torch.mm(a_norm, b_norm.transpose(0, 1))
    # return torch.mm(a, b.transpose(0, 1))


def compare_cos():
    def get_cos_similar(v1: list, v2: list):
        num = float(np.dot(v1, v2))  # 向量点乘
        denom = np.linalg.norm(v1) * np.linalg.norm(v2)  # 求模长的乘积
        return num / denom
    def get_cos_similar_multi(v1: list, v2: list):
        num = np.dot([v1], np.array(v2).T)  # 向量点乘
        denom = np.linalg.norm(v1) * np.linalg.norm(v2, axis=1)  # 求模长的乘积
        res = num / denom
        res[np.isneginf(res)] = 0
        return res

    def get_cos_similar_matrix(v1, v2):
        num = np.dot(v1, np.array(v2).T)  # 向量点乘
        denom = np.linalg.norm(v1, axis=1).reshape(-1, 1) * np.linalg.norm(v2, axis=1)  # 求模长的乘积
        res = num / denom
        res[np.isneginf(res)] = 0
        return res

    print(get_cos_similar([1, 2, 3], [2, 3, -1]))  # 0.6785714285714286
    print(get_cos_similar([1, 2, 3], [2, -1, -1]))  # 0.3363365823230057
    print(get_cos_similar([2, 5, -1], [2, 3, -1]))  # 0.9879500364742666
    print(get_cos_similar([2, 5, -1], [2, -1, -1]))  # 0.5
    print(get_cos_similar_multi([1, 2, 3], [[2, 3, -1], [2, -1, -1]]))  # [[0.67857143 0.33633658]]
    print(get_cos_similar_matrix([[1, 2, 3], [2, 5, -1]], [[2, 3, -1], [2, -1, -1]]))
    a = np.array([1, 2, 3], dtype=np.float32)
    b = np.array([[2, 3, -1], [2, -1, -1]], dtype=np.float32)
    print(cos_sim(a, b))
    print(cos_sim(a, b).shape)

    import time
    v1 = [1, 2, 3, 5, 7, 6, 2, 5, 9, 10]
    v2 = [[2, 5, 1, 8, 4, 1, 1, 3, 1, -5]] * 10000
    t1 = time.time()
    [get_cos_similar(v1, x) for x in v2]
    t2 = time.time()
    print(t2 - t1)  # 0.25322484970092773， 可见矩阵一次点乘的效率最高，遍历之后多次点乘的效率最低
    t3 = time.time()
    get_cos_similar_multi(v1, v2)
    t4 = time.time()
    print(t4 - t3)  # 0.025495529174804688，矩阵效率最高

    t3 = time.time()
    v1 = np.array(v1, dtype=np.float32)
    v2 = np.array(v2, dtype=np.float32)
    cos_sim(v1, v2)
    t4 = time.time()
    print(t4 - t3)  # 0.0114，torch矩阵效率最高


compare_cos()
