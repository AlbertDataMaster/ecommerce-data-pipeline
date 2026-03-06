import pandas as pd
from sqlalchemy import create_engine
import os
import time

# 1. CAMBIO CRÍTICO: Host de base de datos
# Fuera de Docker usas 127.0.0.1, pero DENTRO de Docker debes usar el nombre del servicio: postgres_oltp
DB_URL = "postgresql://Portafolio2026%40:Portafolio2026%40@postgres_oltp:5432/Source"
engine = create_engine(DB_URL)

# Lista de tablas en orden lógico de integridad referencial
TABLES = [
    "products", 
    "users", 
    "inventory_items", 
    "orders", 
    "order_items", 
    "events"
]

def seed_local_data():
    # 2. CAMBIO CRÍTICO: Ruta absoluta dentro del contenedor
    # Airflow monta tu carpeta 'data' en /opt/airflow/data/
    base_path = "/opt/airflow/data"
    
    print(f"🚀 Iniciando carga desde: {base_path}")
    
    for table in TABLES:
        file_path = os.path.join(base_path, f"{table}.csv")
        
        if not os.path.exists(file_path):
            # Lanzamos una excepción real para que Airflow marque la tarea como FAILED
            raise FileNotFoundError(f"❌ Error: No se encuentra {file_path} dentro del contenedor.")
            
        try:
            start_time = time.time()
            print(f"⏳ Procesando {table}...")
            
            # Leemos el CSV
            df = pd.read_csv(file_path, low_memory=False)
            
            # Limpieza de fechas (Optimizado)
            date_cols = [c for c in df.columns if 'at' in c]
            for col in date_cols:
                df[col] = pd.to_datetime(df[col], errors='coerce')
            
            # Carga a Postgres
            # Usamos 'replace' inicialmente para limpiar intentos fallidos previos
            df.to_sql(table, engine, if_exists='replace', index=False, chunksize=1000)
            
            print(f"✅ {table} cargada con {len(df)} filas en {round(time.time() - start_time, 2)}s")
            
        except Exception as e:
            print(f"❌ Error crítico en {table}: {e}")
            raise e # Obliga a Airflow a mostrar el error en rojo

if __name__ == "__main__":
    seed_local_data()