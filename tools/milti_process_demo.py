# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import multiprocessing
import time


def do(n):
    # 获取处理名字
    name = multiprocessing.current_process().name
    time.sleep(2)
    print(name, 'starting')
    print("worker ", n)
    return 'done ' + n


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)
    t1 = time.time()
    result = []
    for i in range(10):
        msg = "hello, %d" % i
        r = pool.apply_async(do, (msg,))
        result.append(r)
    pool.close()
    pool.join()
    for res in result:
        print(res.get())
    print("spend time:", time.time() - t1)
    print("Process end.")
