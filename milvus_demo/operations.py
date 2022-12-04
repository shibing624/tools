# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import sys
import pandas as pd
from loguru import logger

sys.path.append(".")
from config import DEFAULT_TABLE, TOP_K


def do_count(table_name, milvus_cli):
    if not table_name:
        table_name = DEFAULT_TABLE
    try:
        if not milvus_cli.has_collection(table_name):
            return None
        num = milvus_cli.count(table_name)
        return num
    except Exception as e:
        logger.error(f" Error with count table {e}")
        sys.exit(1)


def do_drop(table_name, milvus_cli, db_cli):
    if not table_name:
        table_name = DEFAULT_TABLE
    try:
        if not milvus_cli.has_collection(table_name):
            msg = f"Milvus doesn't have a collection named {table_name}"
            return msg
            # return {'status': True, 'msg': msg}
        status = milvus_cli.delete_collection(table_name)
        db_cli.delete_table(table_name)
        return status
    except Exception as e:
        logger.error(f" Error with  drop table: {e}")
        sys.exit(1)


# Get the vector of question
def extract_features(file_dir, model):
    try:
        data = pd.read_csv(file_dir)
        question_data = data['question'].tolist()
        answer_data = data['answer'].tolist()
        sentence_embeddings = model.sentence_encode(question_data)
        # sentence_embeddings = model.encode(question_data)
        # sentence_embeddings = normalize(sentence_embeddings).tolist()
        return question_data, answer_data, sentence_embeddings
    except Exception as e:
        logger.error(f" Error with extracting feature from question {e}")
        sys.exit(1)


# Combine the id of the vector and the question data into a list
def format_data(ids, question_data, answer_data):
    data = []
    for i in range(len(ids)):
        value = (str(ids[i]), question_data[i], answer_data[i])
        data.append(value)
    return data


# Import vectors to Milvus and data to Mysql respectively
def do_load(table_name, file_dir, model, milvus_client, db_cli):
    if not table_name:
        table_name = DEFAULT_TABLE
    question_data, answer_data, sentence_embeddings = extract_features(file_dir, model)
    ids = milvus_client.insert(table_name, sentence_embeddings)
    milvus_client.create_index(table_name)
    db_cli.create_mysql_table(table_name)
    db_cli.load_data_to_mysql(table_name, format_data(ids, question_data, answer_data))
    return len(ids)


def do_search(table_name, question, model, milvus_client, db_cli):
    try:
        if not table_name:
            table_name = DEFAULT_TABLE
        feat = model.sentence_encode([question])
        results = milvus_client.search_vectors(table_name, feat, TOP_K)
        vids = [str(x.id) for x in results[0]]
        # print('--------------------', vids, '-----------------')
        questions = db_cli.search_by_milvus_ids(vids, table_name)
        distances = [x.distance for x in results[0]]
        return questions, distances
    except Exception as e:
        logger.error(f" Error with search : {e}")
        sys.exit(1)


def do_get_answer(table_name, question, db_cli):
    try:
        if not table_name:
            table_name = DEFAULT_TABLE
        answer = db_cli.search_by_question(question, table_name)
        return answer
    except Exception as e:
        logger.error(f" Error with search by question : {e}")
        sys.exit(1)
