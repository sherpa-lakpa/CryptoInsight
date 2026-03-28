from utils.api_client import fetch_crypto_data
from utils.spark_utils import get_spark
from utils.logger import get_logger
from pyspark.sql.functions import current_timestamp

spark = get_spark()
logger = get_logger()

def run(config):

    logger.info("Starting Bronze Layer")

    data = fetch_crypto_data(config["coins"])

    df = spark.createDataFrame(data)

    df = df.withColumn("ingestion_time", current_timestamp())

    df.write.format("delta") \
        .mode("append") \
        .saveAsTable(config["bronze_table"])

    logger.info("Bronze Load Complete")