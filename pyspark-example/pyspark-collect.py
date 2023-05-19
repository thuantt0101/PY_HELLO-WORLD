# -*- coding: utf-8 -*-
"""
Create on Wed Apr 2023 --002
@author: Thuan-Tran
@Pyspark : 3.3.1

"""

from pyspark.sql import SparkSession
from pyspark.sql.types import DoubleType, IntegerType
appName = "PySpark Example - cast-column"
master = "local"

spark = SparkSession.builder \
        .appName(appName) \
        .master(master) \
        .getOrCreate()

dept = [("Finance",10), \
    ("Marketing",20), \
    ("Sales",30), \
    ("IT",40) \
  ]

deptColumns = ["dept_name","dept_id"]
deptDF = spark.createDataFrame(dept, deptColumns)
deptDF.printSchema()
deptDF.show(truncate=False)


dataCollect = deptDF.collect()
print(dataCollect)

dataCollect2 = deptDF.select("dept_name").collect()
print(dataCollect2)

for row in dataCollect:
    print(row['dept_name'] + ", " + str(row['dept_id']))

