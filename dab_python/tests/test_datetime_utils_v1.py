# test_datetime_utils.py via local venv_pyspark 
import os
import sys
import datetime
import unittest
from pyspark.sql import SparkSession

# run the tests from the root
# Adjust the sys.path if needed (usually in conftest.py or at the top of your test files)
sys.path.append(os.getcwd())
from src.utils.datetime_utils import timestamp_to_date_col

   
class testCitibikeUtilsDateTime(unittest.TestCase): 

    @classmethod
    def setUpClass(self) -> None:
        os.environ["PYSPARK_PYTHON"] = r"C:\\aa_project_azure_dab\\danbo_dab\\.venv_pyspark\\Scripts\\python.exe"
        os.environ["PYSPARK_DIRVER_PYTHON"] = r"C:\\aa_project_azure_dab\\danbo_dab\\.venv_pyspark\\Scripts\\python.exe"
        # self.spark = SparkSession.builder.appName("app").getOrCreate()
        self.spark = ( SparkSession.builder.appName("app")
                .config("spark.driver.extraJavaOptions", "-Djava.security.manager=allow")
                .config("spark.local.dir", "C:\\aa_project_azure_dab\\danbo_dab\\dab_pyspark\\spark_temp")
                .getOrCreate()
                )
        self.spark.sparkContext.setLogLevel("ERROR")
    
    @classmethod
    def tearDownClass(self) -> None:
        self.spark.stop()


    def test_timestamp_to_date_col(self):
                
        # Create a DataFrame with a known timestamp column using a datetime object
        data = [(datetime.datetime(2025, 5, 10, 10, 30, 0),)]
        schema = "ride_timestamp timestamp"
        df = self.spark.createDataFrame(data, schema=schema)
        
        # Use the utility to add a date column
        result_df = timestamp_to_date_col(self.spark, df, "ride_timestamp", "ride_date")
        
        # Assert that the extracted date matches the expected value
        row = result_df.select("ride_date").first()

        expected_date = datetime.date(2025, 5, 10)  # Expected: 2025-04-10

        assert row["ride_date"] == expected_date