

# PySpark map (map()) is an RDD transformation that is used to apply 
# the transformation function (lambda) on every element of RDD/DataFrame 
# and returns a new RDD. In this article, you will learn the syntax 
# and usage of the RDD map() transformation with an example and how to use it with DataFrame.

# RDD map() transformation is used to apply any complex operations like adding a column, 
# updating a column, transforming the data e.t.c, the output of map 
# transformations would always have the same number of records as input.

# Notes
#   |_ Note1: DataFrame doesn’t have map() transformation to use with DataFrame hence you need to DataFrame to RDD first.
#   |_ Note2: If you have a heavy initialization use PySpark mapPartitions() transformation instead of map(), 
#       as with mapPartitions() 
#       heavy initialization executes only once for each partition instead of every record.

# map() Syntax
# map(f, preservesPartitioning=False)

from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]") \
    .appName("SparkByExamples.com").getOrCreate()


data = [(1, "Project"),(2, "Gutenberg’s")]

columns = ["Seq","Name"]

df = spark.createDataFrame(data=data,schema=columns)

df.show()

rs = df.rdd.map(lambda x: (x[0] + 1)).collect()
print(rs)

# for element in rs:
#     print(element)



