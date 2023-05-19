# -*- coding: utf-8 -*-
"""
Create on Wed Apr 2023 --002
@author: Thuan-Tran
@Pyspark : 3.3.1

"""

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

appName = "PySpark Example - "
master = "local"
spark = SparkSession.builder \
        .appName(appName) \
        .master(master) \
        .getOrCreate()

data = [ ("36636","Finance",3000,"USA"), 
    ("40288","Finance",5000,"IND"), 
    ("42114","Sales",3900,"USA"), 
    ("39192","Marketing",2500,"CAN"), 
    ("34534","Sales",6500,"USA") ]

schema = StructType([
    StructField('id', StringType(), True),
    StructField('dept', StringType(), True),
    StructField('salary', IntegerType(), True),
    StructField('location', StringType(), True)
])

df = spark.createDataFrame(data, schema)
df.printSchema()
df.show()

# Convert scolumns to Map
from pyspark.sql.functions import col, lit, create_map
df = df.withColumn("propertiesMap", create_map(
    lit("salary"), col("salary"),
    lit("location"), col("location")
    )).drop("salary", "location")

df.printSchema()
df.show(truncate=False)

