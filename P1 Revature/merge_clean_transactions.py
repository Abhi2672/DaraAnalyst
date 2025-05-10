
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("MergeAndCleanEnhanced").getOrCreate()

df = spark.read.csv("gs://abhishek11/raw/*.csv", header=True, inferSchema=True)

df_clean = df.dropna(subset=["transaction_id", "status"])
df_clean = df_clean.filter((col("transaction_id") != "") & (col("status") != ""))

df_clean.write.csv("gs://abhishek11/processed/cleaned_transactions.csv", header=True, mode="overwrite")

spark.stop()
