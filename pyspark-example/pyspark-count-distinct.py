# -*- coding: utf-8 -*-
"""
Create on Wed Apr 2023 --002
@author: Thuan-Tran
@Pyspark : 3.3.1

"""

from pyspark.sql import SparkSession,Row

appName = "PySpark Example - "
master = "local"
spark = SparkSession.builder \
        .appName(appName) \
        .master(master) \
        .getOrCreate()

data = [("James", "Sales", 3000),
    ("Michael", "Sales", 4600),
    ("Robert", "Sales", 4100),
    ("Maria", "Finance", 3000),
    ("James", "Sales", 3000),
    ("Scott", "Finance", 3300),
    ("Jen", "Finance", 3900),
    ("Jeff", "Marketing", 3000),
    ("Kumar", "Marketing", 2000),
    ("Saif", "Sales", 4100)
  ]

columns = ["Name","Dept","Salary"]
df = spark.createDataFrame(data, columns)
df.printSchema()
df.show(truncate=False)

print('--------------------------df.distinct()----------------------')
df.distinct().show(truncate=False)
print("Distinct count: {0}".format(df.distinct().count()))

# Using countDistrinct()
print('------------------------countDistinct function--------------------------')
from pyspark.sql.functions import countDistinct
df2 = df.select(countDistinct("Dept","Salary"))
df2.printSchema()
df2.show(truncate=False)

print("Distinct Count of Department &amp; Salary: "+ str(df2.collect()[0][0]))

df.createOrReplaceTempView("PERSON")
spark.sql("select distinct(count(*)) from PERSON ").show()
