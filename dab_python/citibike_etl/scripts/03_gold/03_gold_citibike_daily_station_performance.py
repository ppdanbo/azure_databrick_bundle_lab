from pyspark.sql.functions import avg, count, round
import sys

catalog = sys.argv[1]

df = spark.read.table(f"{catalog}.02_silver.jc_citibike")

df = df.\
    groupBy("trip_start_date", "start_station_name").\
    agg(
    round(avg("trip_duration_mins"),2).alias("avg_trip_duration_mins"),
    count("ride_id").alias("total_trips")
    )

df.write.\
    mode("overwrite").\
    option("overwriteSchema", "true").\
    saveAsTable(f"{catalog}.03_gold.daily_station_performance")