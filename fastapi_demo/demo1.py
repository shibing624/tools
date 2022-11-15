# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import uvicorn
from typing import Union
import sys
sys.path.append('.')
from lex import Lexer
from fastapi import FastAPI
from loguru import logger
logger.add('{time}.log', rotation='1 day', encoding='utf-8')
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    m = Lexer()
    r = m.check('北京图书馆')
    logger.info(r)
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)