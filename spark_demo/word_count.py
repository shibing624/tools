# -*- coding: utf-8 -*-
"""
@author:flemingxu(flemingxu@tencent.com)
@description:
"""

import sys
import os
import jieba
from loguru import logger
from datetime import timedelta, datetime
from pytoolkit import TDWSQLProvider, TDWUtil
import pyspark.sql.functions as F
from pyspark.sql import Row, SQLContext, SparkSession
from pyspark.sql.types import StringType, StructField, StructType, IntegerType

if len(sys.argv) > 1:
    print("params:{}".format(sys.argv[1]))
    curr_date = sys.argv[1]
else:
    yesterday = datetime.today() + timedelta(-1)
    curr_date = yesterday.strftime('%Y%m%d')
print("curr_date:{}".format(curr_date))

print(sys.version)
spark = SparkSession.builder.appName("word_count").getOrCreate()
sqlContext = SQLContext(spark.sparkContext)

tdwUtil = TDWUtil(dbName='ams_search_ads_delivery')
provider = TDWSQLProvider(spark, db='ams_search_ads_delivery')

provider.table('ods_search_matched_app').createOrReplaceTempView('tmp2')


# row format: keyword, title, ideadesc, sogouappname, click
def processor(row, dt=None):
    row_list = []
    # logger.debug(row)
    row_dict = row.asDict()
    # logger.debug(row_dict)
    keyword = row_dict.get('keyword', '')
    title = row_dict.get('title', '')
    desc = row_dict.get('ideadesc', '')
    content = keyword + ' ' + title + ' ' + desc
    content_seg_str = "/".join(jieba.lcut(content))
    sogouappname = row_dict['sogouappname']
    click = row_dict['click']
    row_info = Row(content=content, content_seg_str=content_seg_str, sogouappname=sogouappname, click=click)
    row_list.append(row_info)
    return row_list


app_sdf = spark.sql('select keyword, title, ideadesc, sogouappname, click from tmp2 where sogouappname <> "" limit 10')
app_rdd = app_sdf.rdd

app_rdd_new = app_rdd.map(lambda row: processor(row, None))
app_rdd_new_flat = app_rdd_new.flatMap(lambda x: x)
schema = StructType([
    StructField("content", StringType()),
    StructField("content_seg_str", StringType()),
    StructField("sogouappname", StringType()),
    StructField("click", IntegerType())
])
app_sdf_new = sqlContext.createDataFrame(app_rdd_new_flat, schema=schema)
# action
logger.info(app_sdf_new.show(3))

# split and wordcount
df = app_sdf_new.where(app_sdf_new.content_seg_str != "").select(['content_seg_str']).rdd. \
    flatMap(lambda x: x['content_seg_str'].split('/')).map(lambda x: (x, 1)). \
    reduceByKey(lambda x, y: (x + y)).toDF().selectExpr("_1 as word", "_2 as cnt").orderBy(F.col('cnt').desc())

df = df.withColumn('ftime', F.lit(str(curr_date)))
df = df.select('word', 'cnt', 'ftime')
logger.info(df.show(5))

provider.saveToTable(df.select('word', 'cnt', 'ftime'), tblName='ods_search_tmp_account', overwrite=True)
logger.info('table saved.')
table_info = tdwUtil.getTableInfo('ods_search_tmp_account')  # 获取表的格式信息
logger.debug("table_info:{}".format(table_info.colNames))
