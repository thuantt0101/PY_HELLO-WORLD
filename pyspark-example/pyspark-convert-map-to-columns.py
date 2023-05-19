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

df = spark.createDataFrame(data=dataDictionary, schema=['name', 'properties'])
df.printSchema()
df.show(truncate=False)

print('----------------------------convert using rdd.map function------------------')
df3 = df.rdd.map(lambda x: \
                 (x.name,x.properties["hair"], x.properties['eye'] )) \
                 .toDF(["name", "hair", "eye"])
df3.printSchema()
df3.show(truncate=False)

print('----------------------------convert using getItem------------------')
df.withColumn("hair", df.properties.getItem("hair")) \
  .withColumn("eye", df.properties["eye"]) \
  .drop("properties") \
  .show(truncate=False)

# Functions
from pyspark.sql.functions import explode, map_keys, col
keysDF = df.select(explode(map_keys(df.properties))).distinct()

print('-----------------------keysDF---------------------')
keysDF.show(truncate=False)
# +----+
# |col |
# +----+
# |eye |
# |hair|
# +----+

keysList = keysDF.rdd.map(lambda x: x[0]).collect()
print('-----------------------keysList---------------------')
print(keysList)
# ['eye', 'hair']

keyCols = list(map(lambda x: col("properties").getItem(x).alias(str(x)), keysList ) )
print('-----------------------keyCols---------------------')
print(keyCols)
# [Column<'properties[eye] AS eye'>, Column<'properties[hair] AS hair'>]

df.select(df.name, *keyCols).show()






  


