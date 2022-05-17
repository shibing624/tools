# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 发布-订阅模式
"""

import zmq


context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.subscribe("client1")          #订阅主题topic为：client1
socket.connect("tcp://0.0.0.0:5555")
msg = socket.recv_multipart()
print(msg)