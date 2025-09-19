# dab_project
A lab I used while learning from the Udemy course CI/CD with Databricks Asset Bundles.
This repository was built from the original repo https://github.com/pathfinder-analytics-uk/dab_project/

### Virtual Environment Setup

#### macOS / Linux

1. **Create and activate the Databricks Connect environment (using Python 3.11)**
   ```bash
   # at the project root
   python3.11 -m venv .venv_dbc
   source .venv_dbc/bin/activate
   ```
2. **Install Databricks Connect dependencies**
   ```bash
   pip install -r requirements-dbc.txt
   ```
3. **Verify installation**
   ```bash
   pip list
   deactivate
   ```

4. **Create and activate the local PySpark environment**
   ```bash
   python3.11 -m venv .venv_pyspark
   source .venv_pyspark/bin/activate
   ```
5. **Install PySpark dependencies**
   ```bash
   pip install -r requirements-pyspark.txt
   ```
6. **Verify installation**
   ```bash
   pip list
   deactivate
   ```
---
### Databricks and Azure CLI, Set-Up and Bundle Commands

1. Install Databricks CLI for Windows
   ```
   winget search databricks
   winget install Databricks.DatabricksCli
   

   (Optional)
   Install Azure CLI for Windows 
   winget search Microsoft.AzureCLI    
   winget install Microsoft.AzureCLI
   ```
   Verify: 
   ```
   az login --use-device-code
   ```

2. Authenticate to your Databricks workspace
    ```bash
    databricks configure
    databricks auth profiles
    databricks auth describe
    
    ```
       
   #### databrick cluster cmds
   ```bash
   databricks clusters create --json @myfile.json --profile myprofile
   
   databricks clusters list --profile myprofile
   ID                    Name                       State
   0909-180414-ynyxs4na  Danbo Cluster  RUNNING
   
   databricks clusters delete 0909-180414-ynyxs4na
   ```

   #### databricks bundle cmds:
   ```bash
   databricks bundle init
   databricks bundle validate
   databricks bundle summary

   databricks bundle deploy --profile DEFAULT
   databricks bundle deploy --target test
   databricks bundle deploy -t test
   databricks bundle destroy 

   #### az cmds
   ``` bash
   az login --use-device-code
   
   az account show
   ```  

3. To deploy a development copy of this project, type:
    ```bash
    databricks bundle deploy --target dev
    ```
    (Note that "dev" is the default target, so the `--target` parameter
    is optional here.)

    This deploys everything that's defined for this project.
    For example, the default template would deploy a job called
    `[dev yourname] dab_project_job` to your workspace.
    You can find that job by opening your workspace and clicking on **Workflows**.

4. Similarly, to deploy a production copy, type:
   ```bash
   databricks bundle deploy --target prod
   ```

   Note that the default job from the template has a schedule that runs every day
   (defined in resources/dab_project.job.yml). The schedule
   is paused when deploying in development mode (see
   https://docs.databricks.com/dev-tools/bundles/deployment-modes.html).

5. To run a job or pipeline, use the "run" command:
   ```bash
   databricks bundle run
   ```
6. Optionally, install developer tools such as the Databricks extension for Visual Studio Code from
   https://docs.databricks.com/dev-tools/vscode-ext.html.


7. To set up and run pytest, run the following commands:

   ```bash
   pip install pytest-cov

   pytest --cov=src --cov-report=term

   pytest --cov=src --cov-report=term --cov-report=html
   ```
## References：
- DataBricks CLI:  https://learn.microsoft.com/en-us/azure/databricks/dev-tools/cli/commands
- DataBricks API:  https://docs.databricks.com/api/azure/workspace/introduction
- DataBricks Connect: https://learn.microsoft.com/en-us/azure/databricks/dev-tools/databricks-connect/python/advanced
- Asset Bundles: https://learn.microsoft.com/en-us/azure/databricks/dev-tools/bundles/settings
- Bundles Index: https://docs.databricks.com/dev-tools/bundles/index.html
- Bundles Examples:  https://learn.microsoft.com/en-us/azure/databricks/dev-tools/bundles/examples
- AZURE CLI: https://learn.microsoft.com/en-us/cli/azure/?view=azure-cli-latest
- https://learn.microsoft.com/en-us/azure/databricks/jobs/dynamic-value-references
- https://docs.databricks.com/api/azure/workspace/introduction

- Pyspark: https://spark.apache.org/docs/latest/api/python/getting_started/install.html#dependencies
- PYTEST: https://docs.pytest.org/en/stable/
