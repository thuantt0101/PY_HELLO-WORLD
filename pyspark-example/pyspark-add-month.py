# -*- coding: utf-8 -*-
"""
Create on Wed Apr 2023 --002
@author: Thuan-Tran
@Pyspark : 3.3.1

"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import col,expr

appName = "Spark example"
master = "local"
spark = SparkSession.builder \
        .appName(appName) \
        .master(master) \
        .getOrCreate()


data = [ ("2019-01-23",2),("2019-06-24", 2), ("2019-09-20",3)]

# add_months like add-month in  oracle
spark.createDataFrame(data).toDF("date","increment") \
        .select( col("date"), col("increment") , \
            expr("add_months(to_date(date, 'yyyy-MM-dd'), increment)").alias("inc_date")) \
        .show()
          


