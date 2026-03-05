import pandas as pd
from sqlalchemy import create_engine
import os
import time

# 1. Configuración de conexión con URL Encoding (%40 representa el @)
# Usuario: Portafolio2026%40 | Password: Portafolio2026%40
DB_URL = "postgresql://Portafolio2026%40:Portafolio2026%40@127.0.0.1:5432/Source"
engine = create_engine(DB_URL)

# Lista de tablas en orden lógico
TABLES = [
    "distribution_centers", 
    "products", 
    "users", 
    "inventory_items", 
    "orders", 
    "order_items", 
    "events"
]

def seed_local_data():
    print("🚀 Iniciando carga desde archivos locales...")
    
    for table in TABLES:
        file_path = f"data/{table}.csv"
        
        if not os.path.exists(file_path):
            print(f"❌ Error: No se encuentra {file_path}. Descárgalo a la carpeta 'data/'.")
            continue
            
        try:
            start_time = time.time()
            print(f"⏳ Procesando {table}...")
            
            # low_memory=False evita el error de tipos mixtos en columnas grandes
            df = pd.read_csv(file_path, low_memory=False)
            
            # Limpieza de fechas
            date_cols = [c for c in df.columns if c.endswith('_at')]
            for col in date_cols:
                df[col] = pd.to_datetime(df[col], errors='coerce')
            
            # Carga a Postgres
            df.to_sql(table, engine, if_exists='append', index=False, method='multi', chunksize=1000)
            
            print(f"✅ {table} cargada con {len(df)} filas en {round(time.time() - start_time, 2)}s")
            
        except Exception as e:
            print(f"❌ Error crítico en {table}: {e}")

if __name__ == "__main__":
    seed_local_data()