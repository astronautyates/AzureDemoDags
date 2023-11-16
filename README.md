

Project Contents
================

This project includes two dags, `azure_services_dag` which demonstrates how to manage Azure Data Factory(ADF) pipeline runs to perform an ETL processing with Azure Blob Storage and Azure SQL Server using Airflow, and `ml_with_azure` which demonstrates how to use Airflow to manage Machine Learning operations on Azure Databricks and Azure Data Factory. Both DAG's leverage data that is in the `/include/data/customer-churn-records.csv` file. This data contains financial information on customers of a credit card company in Europe. This includes information like Credit score, Card Type, Name, Geography, and more. Please familiarize yourself with the data beginning to better understand how the DAG's are functioning. 

This project showcases the use of the new Azure Workload Identity feature that allows you to connect to an Azure workload identity that can manage multiple services, all through the same connection. 

The `Azure_services_dag` consists of 4 tasks:

- `start` Task: A dummy task to begin the pipeline
- `ingest_data` Task: This task uses ADF to retrieve the customer data from a public github repo, and store it in an Azure container
- `transform_data` Task: This task uses ADF to retrieve the customer data from an Azure container, drops several non-relevant columns like customer name, and stores the clean data back into the same Azure container
- `load_into_mssql` Task: This task uses ADF to load the cleaned customer data from an Azure container into an Azure SQL Server.

The `ml_with_azure` dag consists of 3 tasks: 
- `start` Task: A dummy task to begin the pipeline
- `feature_engineer_data` Task: This task uses ADF to retrieve the customer dataset we produced in the previous DAG, and then prepares it for ML work by dropping non-correlated columns and filtering for only card holders
- `randomforestmodelpredictions` Task: This task uses Azure Databricks to retrieve the prepared customer data set, use it to train a RandomForestModel, and then generates predictions on Credit Scores using the trained model. 
