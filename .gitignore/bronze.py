rom pyspark.sql import SparkSession

def load_bronze(spark, path):
    return spark.read.csv(
        path,
        header=True,
        inferSchema=True
    )