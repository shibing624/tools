# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://0.0.0.0:5555")
while True:
    input_text = input("input:")
    socket.send_string(input_text, encoding='utf-8')
    response = socket.recv_string()
    print(response)