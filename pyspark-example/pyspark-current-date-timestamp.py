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

data=[["1"]]
df=spark.createDataFrame(data,["id"])
df.show(truncate=False)

from pyspark.sql.functions import *

#current_date() & current_timestamp()
df.withColumn("current_date", current_date())\
  .withColumn("current_timestamp", current_timestamp())\
  .show(truncate=False)

print('--------------------------------sql current_date & current_timestamp----------------')
#SQL
spark.sql("select current_date() as current_date, current_timestamp() as current_timestamp")\
    .show(truncate=False)


print('------------------# Date & Timestamp into custom format--------------')
# Date & Timestamp into custom format
df.withColumn("current_date", date_format(current_date(), "MM-dd-yyyy"))\
  .withColumn("current_timestamp", to_timestamp(current_timestamp(),"MM-dd-yyyy HH mm ss SSS"))\
  .show(truncate=False)





