# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import os

############### Milvus Configuration ###############
# MILVUS_HOST = os.getenv("MILVUS_HOST", "127.0.0.1")
MILVUS_HOST = os.getenv("MILVUS_HOST", "9.135.143.192")
MILVUS_PORT = int(os.getenv("MILVUS_PORT", "19530"))
VECTOR_DIMENSION = int(os.getenv("VECTOR_DIMENSION", "64"))
INDEX_FILE_SIZE = int(os.getenv("INDEX_FILE_SIZE", "1024"))
METRIC_TYPE = os.getenv("METRIC_TYPE", "HAMMING")
DEFAULT_TABLE = os.getenv("DEFAULT_TABLE", "milvus_qa_search_1.db")
TOP_K = int(os.getenv("TOP_K", "10"))
