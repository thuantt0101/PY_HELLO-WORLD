# -*- coding: utf-8 -*-
"""
Create on Wed Apr 2023 --002
@author: Thuan-Tran
@Pyspark : 3.3.1

Spark flatMap() transformation flattens the RDD/DataFrame column after 
applying the function on every element and returns a new RDD/DataFrame respectively.
The returned RDD/DataFrame can have the same count or more number of elements. 
This is one of the major differences between flatMap() and map(), where map() 
transformation always returns the same number of elements as input.

"""

from pyspark.sql import SparkSession


appName = "PySpark Example - "
master = "local"

spark = SparkSession.builder \
        .appName(appName) \
        .master(master) \
        .getOrCreate()


columns = ["name","languagesAtSchool","currentState"]
data = [("James,,Smith",["Java","Scala","C++"],"CA"), \
    ("Michael,Rose,",["Spark","Java","C++"],"NJ"), \
    ("Robert,,Williams",["CSharp","VB"],"NV")]


df = spark.createDataFrame(data, columns)
df.printSchema()
df.show(truncate=False)


names = df.select(df.name).rdd.flatMap(lambda x: x).collect()
print(names)


