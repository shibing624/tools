# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from pyspark import SparkContext

sc = SparkContext(appName="count app")
words = sc.parallelize(
    ["scala",
     "java",
     "hadoop",
     "spark",
     "akka",
     "spark vs hadoop",
     "pyspark",
     "pyspark and spark"], 4
)
counts = words.count()
print("Number of elements in RDD -> %i" % counts)
# words.saveAsTextFile("/tmp/readonly/xuming/temp/test_sa12")

list_values = [['Sam', 28, 88], ['Flora', 28, 90], ['Run', 1, 60]]
Spark_df = sc.createDataFrame(list_values, ['name', 'age', 'score'])
Spark_df.show()
