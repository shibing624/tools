# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import zmq

context = zmq.Context()  # 创建上下文
socket = context.socket(zmq.REP)  # 创建Response服务端socket
socket.bind("tcp://*:5555")  # socket绑定，*表示本机ip，端口号为5555，采用tcp协议通信

while True:
    message = socket.recv_string()
    # #发送数据
    # socket.send_json(data)   #data 会被json序列化后进行传输 (json.dumps)
    # socket.send_string(data, encoding="utf-8")   #data为unicode字符串，会进行编码成子节再传输
    # socket.send_pyobj(obj)    #obj为python对象，采用pickle进行序列化后传输
    # socket.send_multipart(msg_parts)   # msg_parts, 发送多条消息组成的迭代器序列，每条消息是子节类型，
    #                                     # 如[b"message1", b"message2", b"message2"]
    print(type(message))  # 接收到的消息也会bytes类型(字节)
    print("收到消息：{}".format(message))
    socket.send_string("new message")  # 发送消息，字节码消息
