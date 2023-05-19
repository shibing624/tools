# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import psutil

virtual_memory = psutil.virtual_memory()
total = virtual_memory.total / (1024*1024)
available = virtual_memory.available / (1024*1024)
percent = virtual_memory.percent


print(f"Total memory: {total:.2f} MB")
print(f"Available memory: {available:.2f} MB")
print(f"Memory usage: {percent}%")
m = range(100000)
import numpy as np
n = np.matmul(m, range(100000))


virtual_memory = psutil.virtual_memory()
total = virtual_memory.total / (1024*1024)
available = virtual_memory.available / (1024*1024)
percent = virtual_memory.percent
print(f"Total memory: {total:.2f} MB")
print(f"Available memory: {available:.2f} MB")
print(f"Memory usage: {percent}%")