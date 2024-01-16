# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description:

pip install fastapi uvicorn openai==0.28.0 pydantic sse_starlette dashscope
"""
import openai
openai.api_base = "http://localhost:5000/v1"
openai.api_key = "sk-xxx"

# 使用流式回复的请求
for chunk in openai.ChatCompletion.create(
    model="none",
    messages=[
        {"role": "user", "content": "你好"}
    ],
    stream=True
    # 流式输出的自定义stopwords功能尚未支持
):
    print(chunk)
    if hasattr(chunk.choices[0].delta, "content"):
        print(chunk.choices[0].delta.content, end="", flush=True)

def gen():
    # 不使用流式回复的请求
    response = openai.ChatCompletion.create(
        model="none",
        messages=[
            {"role": "user", "content": "你好"}
        ],
        stream=False
    )
    print('no stream:', response.choices[0].message.content)
gen()