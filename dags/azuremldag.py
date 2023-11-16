from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.microsoft.azure.operators.container_instances import AzureContainerInstancesOperator
from airflow.providers.microsoft.azure.operators.data_factory import AzureDataFactoryRunPipelineOperator
from airflow.providers.microsoft.azure.operators.cosmos import AzureCosmosInsertDocumentOperator
from airflow.operators.dummy_operator import DummyOperator

RESOURCE_GROUP = 'DemoGroup'
FACTORY_NAME = 'DemoDFYates'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
}

with DAG('ml_with_azure',
          default_args=default_args,
          description='An Airflow DAG that uses Azure services',
          schedule_interval=timedelta(days=1),
          start_date=datetime(2023, 10, 31),
          catchup=False) as dag:
    
    start = DummyOperator(task_id="start")

    prepare_data = AzureDataFactoryRunPipelineOperator(
        task_id='feature_engineer_data',
        azure_data_factory_conn_id='azure_conn',
        resource_group_name=RESOURCE_GROUP,
        factory_name=FACTORY_NAME,
        pipeline_name='MLDataPrep'
    )

    generate_predictions = AzureDataFactoryRunPipelineOperator(
        task_id='randomforestmodelpredictions',
        azure_data_factory_conn_id='azure_conn',
        resource_group_name=RESOURCE_GROUP,
        factory_name=FACTORY_NAME,
        pipeline_name='DatabricksMLPredictions'
    )


    # Define dependency chain
    start >> prepare_data >> generate_predictions