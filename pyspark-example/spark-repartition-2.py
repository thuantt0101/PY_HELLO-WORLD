# -*- coding: utf-8 -*-
"""
author SparkByExamples.com

 câu hỏi : nhờ thầy giáo làm rõ về spark-partition.
 
"""


from pyspark.sql import SparkSession
from pathlib import Path

spark = SparkSession.builder \
        .appName("Spark example") \
        .getOrCreate()

df = spark.read.option("header", True) \
        .csv("resources/simple-zipcodes.csv")

df.printSchema()
df.show(truncate=False)

print("number of partition of df : {0}".format(df.rdd.getNumPartitions()))
# 1

newDF = df.repartition(3)
print("number of partition of newDF : {0}".format(newDF.rdd.getNumPartitions()))
# 3

newDF.write.option("header", True).mode("overwrite")\
        .csv("resources/tmp/zipcodes-state.csv")








