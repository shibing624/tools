# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import os.path
import sqlite3
import sys
from loguru import logger

from config import DEFAULT_TABLE


class DBHelper:
    """
    Say something about the Example Class...
    Args:
        args_0 (`type`):
        ...
    """

    def __init__(self):
        self.conn = sqlite3.connect(DEFAULT_TABLE)
        self.cursor = self.conn.cursor()

    def test_connection(self):
        try:
            os.path.exists(DEFAULT_TABLE)
        except Exception:
            self.conn = sqlite3.connect(DEFAULT_TABLE)
            self.cursor = self.conn.cursor()

    def create_sqlite_table(self, table_name):
        # Create sqlite table if not exists
        self.test_connection()
        sql = "create table if not exists " + table_name + " (milvus_id TEXT PRIMARY KEY NOT NULL, question TEXT, answer TEXT);"
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            logger.debug(f"sqlite create table: {table_name} with sql: {sql}")
        except Exception as e:
            logger.error(f"sqlite ERROR: {e} with sql: {sql}")
            sys.exit(1)

    def load_data_to_sqlite(self, table_name, data):
        # Batch insert (Milvus_ids, img_path) to sqlite
        self.test_connection()
        logger.debug(f"insert data first row:{data[0]}, len:{len(data)}")
        sql = "insert into " + table_name + " (milvus_id,question,answer) values (?,?,?);"
        try:
            self.cursor.executemany(sql, data)
            self.conn.commit()
            logger.debug(f"sqlite loads data to table: {table_name} successfully")
        except Exception as e:
            logger.error(f"sqlite ERROR: {e} with sql: {sql}")
            sys.exit(1)

    def search_by_milvus_ids(self, ids, table_name):
        # Get the img_path according to the milvus ids
        self.test_connection()
        str_ids = str(ids).replace('[', '').replace(']', '')
        sql = "select question from " + table_name + " where milvus_id in (" + str_ids + ") order by (milvus_id," + str_ids + ");"
        try:
            results = self.cursor.execute(sql)
            # results = self.cursor.fetchall()
            results = [res[0] for res in results]
            logger.debug("sqlite search by milvus id.")
            return results
        except Exception as e:
            logger.error(f"sqlite ERROR: {e} with sql: {sql}")
            sys.exit(1)

    def search_by_question(self, question, table_name):
        sql = "select answer from " + table_name + " where question = '" + question + "';"
        try:
            results = self.cursor.execute(sql)
            # results = self.cursor.fetchall()
            logger.debug("sqlite search by question.")
            if results:
                return results[0][0]
            else:
                return results
        except Exception as e:
            logger.error(f"sqlite ERROR: {e} with sql: {sql}".format(e, sql))
            sys.exit(1)

    def delete_table(self, table_name):
        # Delete sqlite table if exists
        self.test_connection()
        sql = "drop table if exists " + table_name + ";"
        try:
            self.cursor.execute(sql)
            logger.debug(f"sqlite delete table:{table_name}")
        except Exception as e:
            logger.error(f"sqlite ERROR: {e} with sql: {sql}")
            sys.exit(1)

    def delete_all_data(self, table_name):
        # Delete all the data in sqlite table
        self.test_connection()
        sql = 'delete from ' + table_name + ';'
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            logger.debug(f"sqlite delete all data in table:{table_name}")
        except Exception as e:
            logger.error(f"sqlite ERROR: {e} with sql: {sql}")
            sys.exit(1)

    def count_table(self, table_name):
        # Get the number of sqlite table
        self.test_connection()
        sql = "select count(milvus_id) from " + table_name + ";"
        try:
            results = self.cursor.execute(sql)
            # results = self.cursor.fetchall()
            logger.debug(f"sqlite count table:{table_name}")
            return results[0][0]
        except Exception as e:
            logger.error(f"sqlite ERROR: {e} with sql: {sql}")
            sys.exit(1)
