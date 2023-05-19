# -*- coding: utf-8 -*-
"""
Create on Wed Apr 2023 --002
@author: Thuan-Tran
@Pyspark : 3.3.1

"""

from pyspark.sql import SparkSession
appName = "PySpark Example - array-string"
master = "local"

spark = SparkSession.builder \
        .appName(appName) \
        .master(master) \
        .getOrCreate()

states = {"NY":"New York", "CA":"California", "FL":"Florida"}
broadcastStates = spark.sparkContext.broadcast(states)

data = [("James","Smith","USA","CA"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL")
  ]

columns = ["firstname","lastname","country","state"]
df = spark.createDataFrame(data=data, schema=columns)
df.printSchema()
df.show(truncate=False)

def state_convert(code):
    return broadcastStates.value[code]

result = df.rdd.map(lambda x: (x[0], x[1], x[2], state_convert(x[3]))).toDF(columns)
result.show(truncate=False)

# Broadcast variable on filter
filteDf= df.where((df['state'].isin(broadcastStates.value)))
filteDf.show()



