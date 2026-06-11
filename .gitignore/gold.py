from pyspark.sql import functions as F

def top_countries(df):
    return (
        df.groupBy("country")
        .count()
        .orderBy(F.desc("count"))
    )