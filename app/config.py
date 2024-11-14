import psycopg2

class Config:
    DB_HOST = 'localhost'
    DB_PORT = '5432'  # Puerto predeterminado de PostgreSQL
    DB_NAME = 'sistema_inventario_BD'
    DB_USER = 'postgres'
    DB_PASSWORD = 'Americ@1927'


def get_connection():
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
