# test_datetime_utils.py via local venv_pyspark 
# test_citibike_utils.py
import unittest
import datetime

import os
import sys
from pyspark.sql import SparkSession
from pyspark.testing import assertDataFrameEqual

# run the tests from the root
# Adjust the sys.path if needed (usually in conftest.py or at the top of your test files)
sys.path.append(os.getcwd())
from src.citibike.citibike_utils import get_trip_duration_mins


    
class testCitibikeUtils(unittest.TestCase): 

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

    def test_get_trip_duration_mins(self):            
        # Create a test DataFrame with known start and end timestamps using datetime objects
        data = [
            (datetime.datetime(2025, 8, 10, 10, 0, 0), datetime.datetime(2025, 8, 10, 10, 10, 0)),  # 10 minutes
            (datetime.datetime(2025, 8, 10, 10, 0, 0), datetime.datetime(2025, 8, 10, 10, 30, 0))   # 30 minutes
        ]
        schema = "start_timestamp timestamp, end_timestamp timestamp"
        df = self.spark.createDataFrame(data, schema=schema)
        
        # Apply the function to calculate trip duration in minutes
        result_df = get_trip_duration_mins(self.spark, df, "start_timestamp", "end_timestamp", "trip_duration_mins")
        
        # Collect the results for assertions
        results = result_df.select("trip_duration_mins").collect()
        
        # Assert that the differences are as expected
        assert results[0]["trip_duration_mins"] == 10
        assert results[1]["trip_duration_mins"] == 30