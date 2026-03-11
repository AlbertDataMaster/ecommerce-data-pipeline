from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
from airflow.providers.google.cloud.hooks.gcs import GCSHook
from airflow.operators.python import PythonOperator
from datetime import datetime

default_args = {
    'owner': 'AlbertDataMaster',
    'start_date': datetime(2026, 3, 1),
}

# Esta función usa un Hook, que es la forma más compatible de conectar con Google
def download_sql_from_gcs(**kwargs):
    hook = GCSHook(gcp_conn_id='google_cloud_default')
    sql_content = hook.download(
        bucket_name='bkt-ecommerce-reporting-logic',
        object_name='reporting-logic/reporting_sales_logic.sql'
    )
    # El contenido viene en bytes, lo decodificamos a texto
    return sql_content.decode('utf-8')

with DAG(
    '04_create_final_report_table',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['BigQuery', 'ML', 'RDL_Optimized']
) as dag:

    # 1. Descarga garantizada sin depender de operadores de descarga complejos
    get_sql = PythonOperator(
        task_id='download_sql_task',
        python_callable=download_sql_from_gcs
    )

    # 2. Materialización RDL con OPTIMIZACIÓN (Particionado y Clustered)
    materialize_table = BigQueryExecuteQueryOperator(
        task_id='create_final_report_table',
        # Jalamos el texto del SQL directamente de la memoria de Airflow
        sql="{{ task_instance.xcom_pull(task_ids='download_sql_task') }}",
        use_legacy_sql=False,
        destination_dataset_table='ecommerce-data-pipeline-489322.reporting_ecommerce.final_sales_report',
        write_disposition='WRITE_TRUNCATE',
        
        # --- CONFIGURACIÓN DE RENDIMIENTO REQUERIDA ---
        time_partitioning={
            "type": "DAY",
            "field": "full_date" 
        },
        cluster_fields=["country", "category", "brand"],
        
        gcp_conn_id='google_cloud_default'
    )

    # 3. Analítica con BigQuery ML
    forecast_model = BigQueryExecuteQueryOperator(
        task_id='bqml_sales_forecast',
        sql="""
            CREATE OR REPLACE MODEL `ecommerce-data-pipeline-489322.reporting_ecommerce.model_sales_forecast`
            OPTIONS(model_type='ARIMA_PLUS', time_series_timestamp_col='full_date', 
                    time_series_data_col='total_sales', auto_arima=TRUE, data_frequency='DAILY') AS
            SELECT full_date, SUM(sale_price) AS total_sales 
            FROM `ecommerce-data-pipeline-489322.reporting_ecommerce.final_sales_report` GROUP BY 1;
        """,
        use_legacy_sql=False,
        gcp_conn_id='google_cloud_default'
    )

    get_sql >> materialize_table >> forecast_model