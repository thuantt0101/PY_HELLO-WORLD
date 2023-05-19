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

dataDictionary = [
        ('James',{'hair':'black','eye':'brown'}),
        ('Michael',{'hair':'brown','eye':None}),
        ('Robert',{'hair':'red','eye':'black'}),
        ('Washington',{'hair':'grey','eye':'grey'}),
        ('Jefferson',{'hair':'brown','eye':''})
        ]

df = spark.createDataFrame(dataDictionary, schema=['name', 'properties'])
df.printSchema()
df.show(truncate=False)

# Using StructType schema
from pyspark.sql.types import StructField, StructType, StringType, MapType,IntegerType
schema = StructType([
    StructField('name', StringType(), True),
    StructField('properties', MapType(StringType(), StringType()), True)
])

df2 = spark.createDataFrame(dataDictionary, schema=schema)
df2.printSchema()
df2.show(truncate=False)

# split columns
df3 = df2.rdd.map(lambda x: \
                  (x.name, x.properties["hair"], x.properties["eye"]))\
                  .toDF(["name", "hair","eye"])
df3.printSchema()
df3.show()

# split column using withColumn and getItem
df.withColumn("hair", df.properties.getItem("hair"))\
    .withColumn("eye", df.properties.getItem("eye"))\
    .drop("properties")\
    .show(truncate=False)

# Split column using Function
from pyspark.sql.functions import explode,map_keys,col
keysDF = df.select(explode(map_keys(df.properties))).distinct()
keysList = keysDF.rdd.map(lambda x:x[0]).collect()
keyCols = list(map(lambda x: col("properties").getItem(x).alias(str(x)), keysList))
df.select(df.name, *keyCols).show()



