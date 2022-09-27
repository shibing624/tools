# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

print(spark.version)
spark.read.load()
from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row
import numpy as np

spark.conf.set('spark.sql.execution.arrow.enabled', 'true')
df = pd.DataFrame(np.random.randn(100, 4), columns=['A', 'B', 'C', 'D'])
sdf = spark.createDataFrame(df)
print(df, type(sdf), sdf)

res = sdf.select("*").toPandas()
print(type(res), res)

# df = spark.CreateDataFrame([Row(name='Alice', age=2, height=80),
#                             Row(name='Bob', age=5, height=85),
#                             Row(name='Tom', age=3, height=75)])
# print(df)
