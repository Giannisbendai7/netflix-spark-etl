from pyspark.sql import SparkSession


def create_spark_session():
    return SparkSession.builder \
        .appName("Netflix_ETL_Project") \
        .getOrCreate()


def load_data(spark, path):
    return spark.read.csv(
        path,
        header=True,
        inferSchema=True
    )


def clean_data(df):
    df = df.dropDuplicates()
    df = df.dropna(subset=["title", "type"])
    return df