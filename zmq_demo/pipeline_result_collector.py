# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: producer -> consumer -> result_collector
"""

import zmq

context = zmq.Context()
result_receiver = context.socket(zmq.PULL)
result_receiver.connect("tcp://0.0.0.0:5578")
result = result_receiver.recv_json()
collecter_data = {}
for x in range(1000):
    if result['consumer_id'] in collecter_data:
        collecter_data[result['consumer_id']] = collecter_data[result['consumer_id']] + 1
    else:
        collecter_data[result['consumer_id']] = 1
    if x >= 995:
        print(collecter_data)
