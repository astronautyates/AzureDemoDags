

Project Contents
================

This project includes two dags, `azure_services_dag` which demonstrates how to manage Azure Data Factory pipeline runs to perform an ETL processing with Azure Blob Storage and Azure SQL Server using Airflow, and `ml_with_azure` which demonstrates how to use Airflow to manage Machine Learning operations on Azure Databricks and Azure Data Factory. Both DAG's leverage data that is in the `/include/data/customer-churn-records.csv` file. This data contains financial information on customers of a credit card company in Europe. This includes information like Credit score, Card Type, Name, Geography, and more. Please familiarize yourself with the data beginning to better understand how the DAG's are functioning. 

The `Azure_services_dag` consists of 4 tasks:

- `start` Task: A dummy task to begin the pipeline
- `ingest_data` Task: 

