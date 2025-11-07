import pandas as pd
from sqlalchemy import create_engine, text

# === CONFIGURACIÓN DE CONEXIÓN ===
# Ajusta estos valores con tu configuración de pgAdmin / PostgreSQL
DB_USER = "postgres"          # tu usuario de PostgreSQL
DB_PASSWORD = "admin"   # tu contraseña
DB_HOST = "localhost"         # o la IP/host del servidor
DB_PORT = "5432"              # puerto por defecto de PostgreSQL
DB_NAME = "diplomado_proyecto_m3"      # base de datos que ya creaste
TABLE_NAME = "inmuebles"  # nombre de la tabla destino

# === CARGA DEL CSV ===
CSV_PATH = "./resultados/inmuebles_header.csv"  # ruta local del archivo CSV

print("📥 Cargando CSV...")
df = pd.read_csv(CSV_PATH)

print(f"✅ CSV cargado con {len(df)} filas y {len(df.columns)} columnas")

# === CREACIÓN DE CONEXIÓN A POSTGRES ===
engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# === OPCIONAL: LIMPIAR TABLA ANTES DE CARGAR ===
with engine.begin() as conn:
    conn.execute(text(f"DROP TABLE IF EXISTS {TABLE_NAME} CASCADE;"))

# === MIGRAR A POSTGRES ===
print(f"🚀 Migrando datos a PostgreSQL (tabla '{TABLE_NAME}')...")
df.to_sql(TABLE_NAME, engine, index=False, if_exists="replace")

print("✅ Migración completada exitosamente.")
print(f"Puedes consultar la tabla con: SELECT * FROM {TABLE_NAME} LIMIT 10;")