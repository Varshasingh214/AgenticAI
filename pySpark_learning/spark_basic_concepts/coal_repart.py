
import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

# sc = SparkContext("local[*]","About Partition")
spark = SparkSession.builder.appName("Partitioning in Spark").getOrCreate()


df1 = spark.range(1,15).toDF("id").withColumn("c1",lit(1))
df2 = spark.range(16, 22).toDF("id").withColumn("c2",lit(2))

df3 = df1.join(df2, "id","full")
df3.show()
print("------printing number of partitions----------\n")
print(df3.rdd.getNumPartitions())


print("from Original-----")
df3=df3.repartition(4)
print(df3.rdd.glom().collect())


print("from coalesce-----")
df4 = df3.coalesce(3)
print(df4.rdd.glom().collect())

print("from repartition-----")
df5 = df3.repartition(3)
print(df5.rdd.glom().collect())

# print(df3.rdd.getNumPartitions())
# df3=df3.repartition(10)
# print(df3.rdd.getNumPartitions())


