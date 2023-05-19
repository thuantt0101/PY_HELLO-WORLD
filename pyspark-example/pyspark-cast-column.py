# -*- coding: utf-8 -*-
"""
Create on Wed Apr 2023 --002
@author: Thuan-Tran
@Pyspark : 3.3.1

"""

from pyspark.sql import SparkSession
appName = "PySpark Example - cast-column"
master = "local"

spark = SparkSession.builder \
        .appName(appName) \
        .master(master) \
        .getOrCreate()

simpleData = [("James",34,"2006-01-01","true","M",3000.60),
    ("Michael",33,"1980-01-10","true","F",3300.80),
    ("Robert",37,"06-01-1992","false","M",5000.50)
  ]

columns = ["firstname","age","jobStartDate","isGraduated","gender","salary"]

df = spark.createDataFrame(simpleData, columns)
df.printSchema()
df.show(truncate=False)

from pyspark.sql.functions import col
from pyspark.sql.types import StringType, BooleanType, DateType
df2 = df.withColumn("age", col("age").cast(StringType()) ) \
        .withColumn("isGraduated", col("isGraduated").cast(BooleanType()) )\
        .withColumn("jobStartDate",col("jobStartDate").cast(DateType())) 

df2.printSchema()
df2.show(truncate=False)

df3 = df2.selectExpr("cast(age as int) age",
        "cast(isGraduated as string) isGraduated ",
        "cast(jobStartDate as string) jobStartDate")

df3.printSchema()

df3.createOrReplaceTempView("CastExample")
df4 = spark.sql("SELECT STRING(age), BOOLEAN(isGraduated), DATE(jobStartDate) from CastExample")
df4.printSchema()
df4.show(truncate=False)
