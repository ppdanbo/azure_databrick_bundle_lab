"""This file configures pytest."""

import os
import sys
import pytest

# run the tests from the root
sys.path.append(os.getcwd())

@pytest.fixture(scope="class")
def spark(): 
    """Provide a SparkSession fixture for tests."""
    try:          
            from databricks.connect import DatabricksSession
            spark = DatabricksSession.builder.remote(cluster_id="0910-040157-l38vfs81").getOrCreate()
            print("Run Remotely via DataBrick Connecct")
            return spark
    except ImportError:
            try:
                from pyspark.sql import SparkSession as session
                print("Run via Local Pyspark")
                os.environ["PYSPARK_PYTHON"] = r"C:\\aa_project_azure_dab\\danbo_dab\\.venv_pyspark\\Scripts\\python.exe"
                os.environ["PYSPARK_DIRVER_PYTHON"] = r"C:\\aa_project_azure_dab\\danbo_dab\\.venv_pyspark\\Scripts\\python.exe"      
                spark = ( session.builder.appName("app")
                        .config("spark.driver.extraJavaOptions", "-Djava.security.manager=allow")
                        .config("spark.local.dir", "C:\\aa_project_azure_dab\\danbo_dab\\dab_pyspark\\spark_temp")
                        .getOrCreate()
                        )
                return spark 
            except Exception: 
                raise ImportError("Neither DataBricks session or Local Spark Session is available.")     
    
