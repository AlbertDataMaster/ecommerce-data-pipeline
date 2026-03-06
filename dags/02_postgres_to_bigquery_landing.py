from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook
from datetime import datetime, timedelta
import pandas as pd

# Configuración de la conexión basada en tu YAML
# En la UI de Airflow, crea una conexión 'postgres_default' con:
# Host: postgres_oltp | Login: Portafolio2026@ | Password: Portafolio2026@ | Port: 5432 | Schema: Source

def extract_to_landing(table_name):
    # 1. Extraer desde el origen (OLTP)
    pg_hook = PostgresHook(postgres_conn_id='postgres_default')
    df = pg_hook.get_pandas_df(sql=f"SELECT * FROM {table_name}")
    
    # 2. Conectar con la Landing Zone (OLAP en BigQuery)
    bq_hook = BigQueryHook(gcp_conn_id='google_cloud_default')
    project_id = 'ecommerce-data-pipeline-489322'
    dataset_id = 'landing_ecommerce'
    
    # 3. Carga directa (Sustituye 'replace' por 'append' si deseas histórico)
    df.to_gbq(
        destination_table=f"{dataset_id}.{table_name}",
        project_id=project_id,
        if_exists='replace', 
        credentials=bq_hook.get_credentials(),
        progress_bar=False
    )
    print(f"Éxito: Tabla {table_name} migrada a BigQuery.")

default_args = {
    'owner': 'AlbertDataMaster',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='02_oltp_to_bigquery_landing',
    default_args=default_args,
    start_date=datetime(2026, 3, 5),
    schedule_interval='@daily',
    catchup=False,
    tags=['ETL', 'OLTP', 'BigQuery']
) as dag:

    # Lista completa de tablas del origen ecommerce
    tablas_ecommerce = ['users', 'products', 'orders', 'order_items', 'inventory_items', 'events' ]

    for tabla in tablas_ecommerce:
        PythonOperator(
            task_id=f'extract_{tabla}_to_landing',
            python_callable=extract_to_landing,
            op_kwargs={'table_name': tabla}
        )