# -*- coding: utf-8 -*-
"""
author SparkByExamples.com

 câu hỏi : nhờ thầy giáo làm rõ về spark-partition.
 van loi khong write duoc file
 
"""

from pyspark.sql import SparkSession
from pathlib import Path

spark = SparkSession.builder \
        .appName("Spark example") \
        .master("local[2]") \
        .getOrCreate()

data= [("James","Smith","USA","CA"),("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),("Maria","Jones","USA","FL")
  ]

schema = ["firstname","lastname","country","state"]
df = spark.createDataFrame(data, schema)
df.printSchema()
df.show(truncate=False)
print(df.rdd.getNumPartitions()) # 2

df.coalesce(1).write.csv("resources/tmp/zipcodes-state")



# can not export file because of error denpendency.
# df.write.option("header", True).csv("resources/tmp/zipcodes-state.json")
# df.write.json("resources/tmp/zipcodes-state.json")




