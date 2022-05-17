/opt/local/bizhadoop_online/spark/bin/spark-submit --master yarn --name UserWordRecommendHouse --deploy-mode cluster \
    --conf spark.driver.maxResultSize=2g --num-executors 10  --executor-memory 2g --executor-cores 4  --driver-memory 8g --driver-cores 4 \
    --conf spark.sql.shuffle.partitions=10 --conf spark.memory.fraction=0.8 --conf spark.yarn.executor.memoryOverhead=2g \
    --conf spark.memory.offHeap.enabled=true --conf spark.memory.offHeap.size=5g --conf spark.rpc.message.maxSize=1024 \
    --conf spark.yarn.maxAppAttempts=1 \
    --conf spark.pyspark.driver.python=python2 \
    --conf spark.pyspark.python=python2 \
    --conf spark.yarn.appMasterEnv.PYSPARK_PYTHON=python2 \
    count_num.py