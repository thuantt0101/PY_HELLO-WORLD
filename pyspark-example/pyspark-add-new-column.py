# -*- coding: utf-8 -*-
"""
Create on Wed Apr 2023 --002
@author: Thuan-Tran
@Pyspark : 3.3.1

"""
from pyspark.sql import SparkSession

appName = "Spark example - add new column"
master = "local"
spark = SparkSession.builder \
            .appName(appName) \
            .master(master) \
            .getOrCreate()

data = [('James','Smith','M',3000),
  ('Anna','Rose','F',4100),
  ('Robert','Williams','M',6200), 
]

columns = ["firstname","lastname","gender","salary"]
df = spark.createDataFrame(data, columns)
df.show()

if 'salary1' not in df.columns:
    print("aa")

# Add new constant column
from pyspark.sql.functions import lit
df.withColumn("bonus_percent", lit(0.3)) \
    .show()

# Add column from existing column
df.withColumn("bonus_amount", df.salary*0.3) \
    .show()

# Add column by concatinating existing columns
from pyspark.sql.functions import concat_ws
df.withColumn("name", concat_ws(",", "firstname", 'lastname')) \
    .show()

# Add current date
from pyspark.sql.functions import current_date
df.withColumn("current_date", current_date())\
    .show()

from pyspark.sql.functions import when
df.withColumn("grade", \
   when((df.salary < 4000), lit("A")) \
     .when((df.salary >= 4000) & (df.salary <= 5000), lit("B")) \
     .otherwise(lit("C")) \
  ).show()


# Add column using SQl
print("-----------------------------------------SPARK SQL--------------------------")
df.createOrReplaceTempView("PER")
spark.sql("select firstname, salary, 0.3 as bonus from PER").show()
spark.sql("select firstname,salary, salary * 0.3 as bonus_amount from PER").show()
spark.sql("select firstname, salary, current_date() as to_day_date from PER").show()
spark.sql("select firstname, salary, " + 
          "case salary when salary < 4000 then 'A' " +
          "else 'B' END as grade " +
          "from PER").show()