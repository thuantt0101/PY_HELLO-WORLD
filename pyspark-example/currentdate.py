# -*- coding: utf-8 -*-
"""
Create on Wed Apr 2023
@author: Thuan-Tran
@Pyspark : 3.4.0

"""

from pyspark.sql import SparkSession
from pyspark.sql.types import ArrayType, StructField, StructType, StringType, IntegerType

appName = "PySpark Example - Python Array/List to Spark Data Frame"
master = "local"

# Create Spark session
spark = SparkSession.builder \
        .appName(appName) \
        .master(master) \
        .getOrCreate()

fields = [  
            StructField('seq', IntegerType(), True)  ,
            StructField('name', StringType(), True)
            ]

schema = StructType(fields)

names = [(1, "Thuan-Tran"),
         (2, "Tien-Tran")]

# Create Data Frame
df = spark.createDataFrame(names, schema=schema)

df.show()