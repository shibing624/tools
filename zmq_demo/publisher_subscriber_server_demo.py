# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 发布-订阅模式
"""
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")
topic = ["client1", "client2"]
while True:
    for t in topic:
        data = "message for {}".format(t)
        msg = [t.encode("utf-8"), data.encode("utf-8")]  # 列表中的第一项作为消息的topic，sub根据topic过滤消息
        print(msg)
        socket.send_multipart(msg)
