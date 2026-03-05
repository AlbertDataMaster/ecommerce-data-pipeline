from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# 1. Definir la configuración básica del DAG
default_args = {
    'owner': 'AlbertDataMaster',
    'depends_on_past': False,
    'start_date': datetime(2026, 3, 5),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    '01_ingesta_oltp_ecommerce',
    default_args=default_args,
    description='Automatización de la carga inicial de datos en Postgres',
    schedule_interval='@daily', # Se ejecutará cada día automáticamente
    catchup=False
) as dag:

    # 2. Definir la Tarea: Ejecutar el script seed_data.py
    # Usamos BashOperator para ejecutar el comando como si estuviéramos en la terminal
    tarea_carga_datos = BashOperator(
        task_id='ejecutar_seed_data',
        bash_command='python3 /opt/airflow/seed_data.py' 
    )

    tarea_carga_datos