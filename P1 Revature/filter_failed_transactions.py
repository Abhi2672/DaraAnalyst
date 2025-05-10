
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("FilterFailedTransactions").getOrCreate()

df = spark.read.option("header", True).csv("gs://abhishek11/processed/cleaned_transactions.csv/*.csv")
df_failed = df.filter(df.status == "FAILED")

jdbc_url = "jdbc:mysql://34.170.92.75:3306/workdb"
properties = {
    "user": "admin",
    "password": "admin",
    "driver": "com.mysql.cj.jdbc.Driver"
}

df_failed.write \
    .jdbc(url=jdbc_url, table="failed_transactions", mode="overwrite", properties=properties)

spark.stop()
