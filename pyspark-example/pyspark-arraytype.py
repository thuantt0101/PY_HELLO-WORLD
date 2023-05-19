# -*- coding: utf-8 -*-
"""
Create on Wed Apr 2023 --002
@author: Thuan-Tran
@Pyspark : 3.3.1

"""
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, ArrayType, StructType, StructField

appName = "PySpark Example - "
master = "local"
spark = SparkSession.builder \
        .appName(appName) \
        .master(master) \
        .getOrCreate()

arrayCol = ArrayType(StringType(), False)
data = [
 ("James,,Smith",["Java","Scala","C++"],["Spark","Java"],"OH","CA"),
 ("Michael,Rose,",["Spark","Java","C++"],["Spark","Java"],"NY","NJ"),
 ("Robert,,Williams",["CSharp","VB"],["Spark","Python"],"UT","NV")
]

schema = StructType([
    StructField("name", StringType(), True),
    StructField("languagesAtSchool", ArrayType(StringType()) ,True),
    StructField("languagesAtWork", ArrayType(StringType()), True),
    StructField("currentState", StringType(),True),
    StructField("previousState", StringType(), True)
])
df = spark.createDataFrame(data, schema)
df.printSchema()
df.show()

print('---------------------------------------------------')



from pyspark.sql.functions import explode
df.select(df.name, explode(df.languagesAtSchool)).show()

# +----------------+------+
# |            name|   col|
# +----------------+------+
# |    James,,Smith|  Java|
# |    James,,Smith| Scala|
# |    James,,Smith|   C++|
# |   Michael,Rose,| Spark|
# |   Michael,Rose,|  Java|
# |   Michael,Rose,|   C++|
# |Robert,,Williams|CSharp|
# |Robert,,Williams|    VB|
# +----------------+------+

from pyspark.sql.functions import split
df.select(split(df.name,",").alias("nameAsArray")).show()

from pyspark.sql.functions import array
df.select(df.name, array(df.currentState, df.previousState).alias("States")).show()

from pyspark.sql.functions import array_contains
df.select(df.name, array_contains(df.languagesAtSchool, "Java")).alias("array_contains").show()