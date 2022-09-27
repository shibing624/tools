# -*- coding: utf-8 -*-
"""
@author:flemingxu(flemingxu@tencent.com)
@description:
"""

import sys
import os
from datetime import timedelta, datetime
from pytoolkit import TDWSQLProvider, TDWUtil
from pyspark.sql import SparkSession

if len(sys.argv) > 1:
    print("params:{}".format(sys.argv[1]))
    curr_date = sys.argv[1]
else:
    yesterday = datetime.today() + timedelta(-1)
    curr_date = yesterday.strftime('%Y%m%d')
    print("argv error")
print("curr_date:{}".format(curr_date))

print(sys.version)
spark = SparkSession.builder.appName("fill_brand").getOrCreate()
provider = TDWSQLProvider(spark, db='ams_search_ads_delivery')
tdwUtil = TDWUtil(dbName='ams_search_ads_delivery')
# CREATE TABLE ods_search_tid_contents(
#     imp_date BIGINT COMMENT '导入日期',
#     ftid BIGINT COMMENT '创意ID(广告id)',
#     fuid BIGINT COMMENT '广告主ID',
#     sourcetype TINYINT COMMENT '类型（0:APP; 1:SDPA; 2:MDPA; 3:其他',
#     fdynamicadtype TINYINT COMMENT '广告类型（0:普通广告; 1:动态商品广告; 2:动态文章广告; 3:动态元素广告; 4:动态创意广告; 5:多创意广告）',
#     fdynamicadsubtype TINYINT COMMENT '商品广告类型（1:sdpa; 2:mdpa）',
#     fproducttype BIGINT,
#     fadcreativeid BIGINT COMMENT '广告创意ID',
#     sourceid TINYINT COMMENT '类型（1:dpa; 2:非dpa）',
#     genertype TINYINT COMMENT '生成类型（1撞库; 2模板匹配; 3生成分; 4客户自提）',
#     deliverytype TINYINT COMMENT '广告投放类型（1直投; 2通投; 3暗投）',
#     containwildcard TINYINT COMMENT '内容是否包含通配符（1包含; 0不包含）',
#     template_title STRING COMMENT '模板标题',
#     template_desc STRING COMMENT '模板描述',
#     brand_word STRING COMMENT '品牌词',
#     core_word STRING COMMENT '核心词',
#     title STRING COMMENT '信息流原始文本文案（title）',
#     description STRING COMMENT '信息流原始文本文案（desc）',
#     fdynamicad_productname STRING COMMENT '动态商品名称',
#     fpname STRING COMMENT '普通广告-商品名称',
#     generate_title STRING COMMENT '最终生成标题',
#     generate_desc STRING COMMENT '最终生成描述'
# )
# STORED AS ORCFILE;

tid_contents_table = provider.table('ods_search_tid_contents')

# select appname,
#        title,
#        ideadesc,
#        tradenames,
#        totalcost
# from ams_search_ads_delivery::ods_search_sg_app_template
# limit 1000;
app_tpl_table = provider.table('ods_search_sg_app_template')

tid_contents_filter = tid_contents_table.where(
    "genertype = 2 and template_title <> ''")  # 对于调用的数据做类似sql中的条件筛选
app_tpl_filter = app_tpl_table.where(
    "appname <> '' and totalcost > 10")

print(tid_contents_filter.printSchema())  # 类似pandas中的head，注意这里是一个行动操作
print(app_tpl_filter.printSchema())  # 注意这里的数据类型为spark dataframe，如果想转化成pandas dataframe可以使用
# pdtmpdf=tmpdf.toPandas()做转化，但是这里会把分布储存的data序列化，如果数据量太大会造成driver OOM(out of memory)，
# 这里可以通过设置driver memory做扩充，但是也不是根本的解决方法

app_rdd = app_tpl_filter.rdd


####此处省略中间过程####
if tdwUtil.tableExist('ods_search_tmp_account'):  # 查看数据库中是否存在一张表
    if tdwUtil.partitionExist('ods_search_tmp_account',
                              'p_{}'.format(curr_date)):  # 查看这张表指定的分区是否存在
        tdwUtil.dropPartition('ods_search_tmp_account',
                              'p_{}'.format(curr_date))  # 如果存在就把这分区去掉，以便重复执行任务任务的时候造成数据冗余错乱等问题

table_info = tdwUtil.getTableInfo('ods_search_tmp_account')  # 获取表的格式信息
# tdwUtil.createListPartition('ods_search_tmp_account', 'p_{}'.format(curr_date), curr_date)  # 创建表的指定分区
# provider.saveToTable(dfunion_spark_df.select(*table_info.colNames), 'ods_search_tmp_account', 'p_{}'.format(curr_date))
provider.saveToTable(app_tpl_filter.select("appname", "title", "ideadesc", "tradenames"), 'ods_search_tmp_account')
