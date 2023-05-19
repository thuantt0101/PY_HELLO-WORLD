# -*- coding: utf-8 -*-

"""
Create on Apr 2023 --003
author : Thuan-Tran
using pandas version  before 2.0
"""

from pyspark.sql import SparkSession


appName = "PySpark Example - "
master = "local[1]"

spark = SparkSession.builder \
        .appName(appName) \
        .master(master) \
        .getOrCreate()


import pandas as pd
data = [ ['Scott', 50], ['Jeff', 45], ['Thomas', 54], ['Ann', 34] ]

# Create the pandas dataframe
pandasDF = pd.DataFrame(data, columns = ['Name', 'Age']) 
print(pandasDF)
# print(pandasDF.columns)
# print(pandasDF.values)
sparkDF = spark.createDataFrame(pandasDF)
sparkDF.printSchema()
sparkDF.show()


#sparkDF=spark.createDataFrame(pandasDF.astype(str)) 
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
mySchema = StructType([StructField("Frist Name", StringType(), True) \
                      ,StructField("Age", IntegerType(), True)])

sparkDF2 = spark.createDataFrame(pandasDF, schema=mySchema)
sparkDF2.printSchema()
sparkDF2.show()


spark.conf.set("spark.sql.execution.arrow.enabled","true")
spark.conf.set("spark.sql.execution.arrow.pyspark.fallback.enabled","true")

pandasDF2 = sparkDF2.select("*").toPandas()
print(pandasDF2)

test = spark.conf.get("spark.sql.execution.arrow.enabled")
print(test)

test123 = spark.conf.get("spark.sql.execution.arrow.pyspark.fallback.enabled")
print(test123)











