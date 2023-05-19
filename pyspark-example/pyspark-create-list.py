# -*- coding: utf-8 -*-
"""
Create on Wed Apr 2023 --002
@author: Thuan-Tran
@Pyspark : 3.3.1

"""

from pyspark.sql import SparkSession,Row
from pyspark.sql.types import StructType,StructField, StringType

appName = "PySpark Example - "
master = "local"
spark = SparkSession.builder \
        .appName(appName) \
        .master(master) \
        .getOrCreate()

#Using List
dept = [("Finance",10), 
        ("Marketing",20), 
        ("Sales",30), 
        ("IT",40) 
      ]

deptColumns = ["dept_name","dept_id"]
deptDF = spark.createDataFrame(dept, deptColumns)
deptDF.printSchema()
deptDF.show(truncate=False)

deptSchema = StructType([       
    StructField('firstname', StringType(), True),
    StructField('middlename', StringType(), True),
    StructField('lastname', StringType(), True)
])

# Convert list to RDD
rdd = spark.sparkContext.parallelize(dept)
rdd.toDF(["dept_name","dept_id"]).show()