import psycopg2
from psycopg2 import Error
from config import Config  # Se importa la configuración desde config.py

# Función para conectar a la base de datos
def connect_to_db():
    try:
        connection = psycopg2.connect(
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            database=Config.DB_NAME
        )
        print("Conexión exitosa a la base de datos.")
        return connection
    except Error as e:
        print("Error al conectar a la base de datos:", e)
        return None