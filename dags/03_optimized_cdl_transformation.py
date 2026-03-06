from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'AlbertDataMaster',
    'depends_on_past': False,
    'start_date': datetime(2026, 3, 6),
    'email_on_failure': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    '03_optimized_cdl_transformation',
    default_args=default_args,
    description='Transformación LZ a CDL con Particiones y Clustering',
    schedule_interval='@daily',
    catchup=False,
    tags=['Performance', 'CDL', 'BigQuery']
) as dag:

    # Ejecución del Procedimiento Almacenado de Alto Performance
    run_cdl_sp = BigQueryExecuteQueryOperator(
        task_id='build_optimized_cdl',
        sql="CALL `ecommerce-data-pipeline-489322.core_ecommerce.sp_build_cdl_optimized`();",
        use_legacy_sql=False,
        gcp_conn_id='google_cloud_default',
        location='US'
    )

    run_cdl_sp