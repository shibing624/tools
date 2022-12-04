# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description:
原理：simhash可以存储为64位的整数，可以用于文本去重，文本相似度计算，文本聚类等。
1.milvus支持binary类型，可以用于存储simhash的hash值；
2.milvus支持汉明距离度量计算，可以用于计算simhash的汉明距离。
因而基于以上两点，可以用milvus实现simhash的相似度搜索。
For binary vectors:
HAMMING (Hamming distance)
https://milvus.io/docs/calculate_distance.md
"""
import uvicorn
import os
import sys
from loguru import logger
from fastapi import FastAPI, File, UploadFile
from starlette.middleware.cors import CORSMiddleware

sys.path.append(".")
from milvus_helpers import MilvusHelper
from operations import do_drop, do_load, do_count, do_search, do_get_answer
from db_helpers import DBHelper
from encode import SentenceModel

pwd_path = os.path.abspath(os.path.dirname(__file__))
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL = SentenceModel()
MILVUS_CLI = MilvusHelper()
DB_CLI = DBHelper()


@app.post('/qa/load_data')
async def do_load_api(file: UploadFile = File(...), table_name: str = None):
    try:
        text = await file.read()
        fname = file.filename
        dirs = os.path.join(pwd_path, './data_dir/')
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        fname_path = os.path.join(os.getcwd(), os.path.join(dirs, fname))
        with open(fname_path, 'wb') as f:
            f.write(text)
    except Exception:
        return {'status': False, 'msg': 'Failed to load data.'}
    try:
        total_num = do_load(table_name, fname_path, MODEL, MILVUS_CLI, DB_CLI)
        logger.info(f"Successfully loaded data, total count: {total_num}")
        return {'status': True, 'msg': f"Successfully loaded data: {total_num}"}, 200
    except Exception as e:
        logger.error(e)
        return {'status': False, 'msg': e}, 400


@app.get('/qa/search')
async def do_get_question_api(question: str, table_name: str = None):
    try:
        questions, _ = do_search(table_name, question, MODEL, MILVUS_CLI, DB_CLI)
        # res = dict(zip(questions, distances))
        # res = sorted(res.items(), key=lambda item: item[1])
        logger.info("Successfully searched similar images!")
        return {'status': True, 'msg': questions}, 200
    except Exception as e:
        logger.error(e)
        return {'status': False, 'msg': e}, 400


@app.get('/qa/answer')
async def do_get_answer_api(question: str, table_name: str = None):
    try:
        results = do_get_answer(table_name, question, DB_CLI)
        return {'status': True, 'msg': results}
    except Exception as e:
        logger.error(e)
        return {'status': False, 'msg': e}


@app.post('/qa/count')
async def count_images(table_name: str = None):
    # Returns the total number of questions in the system
    try:
        num = do_count(table_name, MILVUS_CLI)
        logger.info("Successfully count the number of questions!")
        return num
    except Exception as e:
        logger.error(e)
        return {'status': False, 'msg': e}, 400


@app.post('/qa/drop')
async def drop_tables(table_name: str = None):
    # Delete the collection of Milvus and MySQL
    try:
        status = do_drop(table_name, MILVUS_CLI, DB_CLI)
        logger.info("Successfully drop tables in Milvus and MySQL!")
        return {'status': True, 'msg': status}
    except Exception as e:
        logger.error(e)
        return {'status': False, 'msg': e}, 400


if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=8000)
