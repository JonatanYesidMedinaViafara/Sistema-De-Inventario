import os
import psycopg2

class Config:
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_NAME = os.environ.get('DB_NAME')
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')

def get_connection():
    try:
        connection = psycopg2.connect(
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME
        )
        print("Conexión exitosa")
        return connection
    except Exception as ex:
        print(f"Error de conexión: {ex}")
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
    
