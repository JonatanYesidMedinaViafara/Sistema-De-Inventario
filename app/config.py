import os
import psycopg2
import urllib.parse as urlparse

class Config:
    DATABASE_URL = os.environ.get('DATABASE_URL')
    if DATABASE_URL:
        url = urlparse.urlparse(DATABASE_URL)
        DB_HOST = url.hostname
        DB_PORT = url.port
        DB_NAME = url.path[1:]  # Quita el '/'
        DB_USER = url.username
        DB_PASSWORD = url.password
    else:
        # Maneja el caso en que DATABASE_URL no esté definida
        print("La variable de entorno DATABASE_URL no está definida.")
        DB_HOST = None
        DB_PORT = None
        DB_NAME = None
        DB_USER = None
        DB_PASSWORD = None

def get_connection():
    try:
        connection = psycopg2.connect(
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME
        )
        print("Conexión exitosa a la base de datos")
        return connection
    except Exception as ex:
        print(f"Error al conectar a la base de datos: {ex}")
        return None

#configuracion de manera local
class Config_anterior:
    DB_HOST = 'localhost'
    DB_PORT = '5432'  # Puerto predeterminado de PostgreSQL
    DB_NAME = 'sistema_inventario_BD'
    DB_USER = 'postgres'
    DB_PASSWORD = 'Americ@1927'


def get_connection_anterior():
    try:
        connection = psycopg2.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME
        )
        print("Conexión exitosa")
        return connection
    except Exception as ex:
        print(f"Error de conexión: {ex}")
        return None
    
