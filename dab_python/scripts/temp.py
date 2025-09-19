from databricks.connect import DatabricksSession
# from pyspark.sql import SparkSession


# spark = DatabricksSession.builder.getOrCreate()
spark = DatabricksSession.builder.remote(cluster_id="0910-040157-l38vfs81").getOrCreate()

spark.sql("SELECT 1").show()