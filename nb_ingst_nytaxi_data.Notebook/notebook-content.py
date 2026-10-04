# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse_name": "",
# META       "default_lakehouse_workspace_id": ""
# META     },
# META     "environment": {}
# META   }
# META }

# CELL ********************

 # Azure Blob Storage access info
 blob_account_name = "azureopendatastorage"
 blob_container_name = "nyctlc"
 blob_relative_path = "yellow"

 workspace_name = "fabric_cicd_basic"
 lakehouse_name = "lh_cicd_basic"
    
 # Construct connection path
 wasbs_path = f'wasbs://{blob_container_name}@{blob_account_name}.blob.core.windows.net/{blob_relative_path}'
 print(wasbs_path)
    
 # Read parquet data from Azure Blob Storage path
 blob_df = spark.read.parquet(wasbs_path)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(blob_df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Declare file name    
file_name = "yellow_taxi"

# Construct destination path
output_parquet_path = f"abfss://{workspace_name}@onelake.dfs.fabric.microsoft.com/{lakehouse_name}.Lakehouse/Files/Raw/{file_name}"

print(output_parquet_path)

# Load the first 10000 rows as a Parquet file
blob_df.limit(10000).write.mode("overwrite").parquet(output_parquet_path)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
