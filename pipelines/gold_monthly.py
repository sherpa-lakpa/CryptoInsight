from utils.spark_utils import get_spark
from pyspark.sql.functions import avg, month

spark = get_spark()

def run(config):

    df = spark.read.table(config["silver_table"])

    df_gold = df.withColumn("month", month("ingestion_time")) \
        .groupBy("coin", "month") \
        .agg(avg("price").alias("avg_price"))

    df_gold.write.format("delta") \
        .mode("overwrite") \
        .saveAsTable(config["gold_tables"]["monthly"])