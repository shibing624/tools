# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: producer -> consumer -> result_collector
"""

import random
import zmq

context = zmq.Context()
consumer_id = random.randint(1, 1000)
# 接收工作
consumer_receiver = context.socket(zmq.PULL)
consumer_receiver.connect("tcp://0.0.0.0:5577")
# 转发结果
consumer_sender = context.socket(zmq.PUSH)
consumer_sender.bind("tcp://*:5578")
while True:
    msg = consumer_receiver.recv_json()
    data = msg["num"]
    print(msg, "num:", data)
    result = {"consumer_id": consumer_id, "num": data}
    consumer_sender.send_json(result)
