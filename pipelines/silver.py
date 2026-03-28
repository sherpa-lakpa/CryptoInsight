from utils.spark_utils import get_spark
from utils.logger import get_logger
from pyspark.sql.functions import col
from delta.tables import DeltaTable

spark = get_spark()
logger = get_logger()

def run(config):

    logger.info("Starting Silver Layer")

    df = spark.read.table(config["bronze_table"])

    df_clean = df.dropDuplicates(["coin", "ingestion_time"])

    target = config["silver_table"]

    if spark.catalog.tableExists(target):

        delta_table = DeltaTable.forName(spark, target)

        delta_table.alias("t").merge(
            df_clean.alias("s"),
            "t.coin = s.coin AND t.ingestion_time = s.ingestion_time"
        ).whenNotMatchedInsertAll().execute()

    else:
        df_clean.write.format("delta").saveAsTable(target)

    logger.info("Silver Load Complete")