# test_datetime_utils.py via databrick connet venv_dbc
import datetime
import unittest
import pytest

# run the tests from the root
# Adjust the sys.path if needed (usually in conftest.py or at the top of your test files)
# sys.path.append(os.getcwd())
from src.utils.datetime_utils import timestamp_to_date_col
   
class testCitibikeUtilsDateTime(unittest.TestCase): 

    @pytest.fixture(autouse=True)
    def _setup(self, spark) -> None:
        self.spark = spark 
  
    # @classmethod
    # def tearDownClass(self) -> None:
    #     self.spark.stop()


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