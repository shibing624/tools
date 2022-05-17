# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: producer -> consumer -> result_collector
"""
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://*:5577")
for num in range(2000):
    work_message = {"num": num}
    socket.send_json(work_message)