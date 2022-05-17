# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

import sys
import os
from pyspark import SparkContext

if __name__ == "__main__":
    sc = SparkContext(appName='firt app')
    # data_file = '/user/bizdev_cd/algorithm/word_recommend/src/count_num.py'
    data_file = '/tmp/readonly/xuming/temp/count_num.py'
    word = sc.textFile(data_file)
    num_i = word.filter(lambda s: 'i' in s).count()
    print('python version:', sys.version)
    print(os.environ)

    print(num_i)
    print('my log is here. pppppppppp, i size: %d' % num_i)
    rdd = sc.parallelize(["hadoop", "spark", "hive123"])
    # rdd.saveAsTextFile("/user/bizdev_cd/algorithm/word_recommend/src/test_sa2")
    rdd.saveAsTextFile("/tmp/readonly/xuming/temp/test_sa211")
