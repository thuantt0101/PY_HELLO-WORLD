# -*- coding: utf-8 -*-
"""
Create on Wed Apr 2023 --002
@author: Thuan-Tran
@Pyspark : 3.3.1

"""

from pyspark.sql import SparkSession,Row

appName = "PySpark Example - "
master = "local"
spark = SparkSession.builder \
        .appName(appName) \
        .master(master) \
        .getOrCreate()

columns = ["language","users_count"]
data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]
rdd = spark.sparkContext.parallelize(data)

dfFromRDD1 = rdd.toDF()
dfFromRDD1.printSchema()
dfFromRDD1.show(truncate=False)

dfFromRDD1 = rdd.toDF(columns)
dfFromRDD1.printSchema()
dfFromRDD1.show(truncate=False)

dfFromRDD2 = spark.createDataFrame(rdd).toDF(*columns)
dfFromRDD2.printSchema()
dfFromRDD2.show(truncate=False)

rowData = map(lambda x: Row(*x), data)
print(type(Row))
dfFromData3 = spark.createDataFrame(rowData, columns)
dfFromData3.printSchema()