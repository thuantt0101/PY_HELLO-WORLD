# -*- coding: utf-8 -*-
"""
Create on Wed Apr 2023 --002
@author: Thuan-Tran
@Pyspark : 3.3.1

"""

from pyspark.sql import SparkSession

appName = "PySpark Example - "
master = "local"
spark = SparkSession.builder \
        .appName(appName) \
        .master(master) \
        .getOrCreate()


data = [("James","Smith","USA","CA"),("Michael","Rose","USA","NY"), \
    ("Robert","Williams","USA","CA"),("Maria","Jones","USA","FL") \
  ]
columns=["firstname","lastname","country","state"]

df = spark.createDataFrame(data, columns)
df.show()
print(df.collect())


states1 = df.rdd.map(lambda x: x[3]).collect()
print(states1)
# ['CA', 'NY', 'CA', 'FL']

from collections import OrderedDict
res = list(OrderedDict.fromkeys(states1))
print(res)
#['CA', 'NY', 'FL']

#Example 2 : state  = column state
states2 = df.rdd.map(lambda x: x.state).collect()
print(states2)

state21 = df.rdd.map(lambda x: x.country).collect()
print(state21)
# ['USA', 'USA', 'USA', 'USA']

states3 = df.select(df.state).collect()
print(states3)
print(type(states3))
# [Row(state='CA'), Row(state='NY'), Row(state='CA'), Row(state='FL')]

states4 = df.select(df.state).rdd.flatMap(lambda x: x).collect()
print(states4)
# ['CA', 'NY', 'CA', 'FL']

states5=df.select(df.state).toPandas()
print(type(states5))
print(states5)
states6 = list(states5['state'])
print(states6)
# ['CA', 'NY', 'CA', 'FL']

pandDF = df.select(df.state, df.firstname).toPandas()
print(list(pandDF['state']))
print(list(pandDF['firstname']))
# ['CA', 'NY', 'CA', 'FL']
# ['James', 'Michael', 'Robert', 'Maria']







