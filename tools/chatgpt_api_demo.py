# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

import argparse
import uvicorn
import sys
import os
from fastapi import FastAPI, Query, Form
from starlette.middleware.cors import CORSMiddleware
from loguru import logger
import openai

openai.api_key = "your_key"



# define the app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

def openai_reply(content):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # gpt-3.5-turbo-0301
        messages=[
            {"role": "user", "content": content}
        ],
        temperature=0.7,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response.choices[0].message.content


@app.get('/')
async def index():
    return {"message": "index, docs url: /docs"}


@app.get('/chatgpt')
async def query_classify(q: str = Query(..., min_length=1, max_length=2000, title='question')):
    try:
        res = openai_reply(q)
        result_dict = {'query': q, 'chatgpt': res}
        logger.debug(f"Successfully get chatgpt response, q:{q}, res:{res}")
        return result_dict
    except Exception as e:
        logger.error(e)
        return {'status': False, 'msg': e}, 400


if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=8080)
