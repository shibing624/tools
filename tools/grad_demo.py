# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import torch
import torch.autograd
from torch.autograd import Variable
def loss_function(x):
    mask = (x < 0.003).float()
    print(mask)
    print(1-mask)
    gamma_x = mask * 12.9 * x + (1-mask) * (x ** 0.5)
    loss = torch.mean((x - gamma_x) ** 2)
    return loss

def loss_function_new(x):
    mask = x < 0.003
    print(mask)

    gamma_x = torch.FloatTensor(x.size()).type_as(x)
    print(gamma_x)
    gamma_x[mask] = 12.9 * x[mask]
    print(gamma_x)
    mask = x >= 0.003
    gamma_x[mask] = x[mask] ** 0.5
    loss = torch.mean((x - gamma_x) ** 2)
    return loss

if __name__ == '__main__':
    x = Variable(torch.FloatTensor([0, 0.0025, 0.5, 0.8, 1]), requires_grad=True)
    loss = loss_function_new(x)
    print('loss:', loss)
    loss.backward()
    print(x.grad)