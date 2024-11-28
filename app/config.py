import os
import psycopg2

class Config:
    # Utiliza la variable de entorno DATABASE_URL en Render. Si no está definida, usa valores locales.
    DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:Americ@1927@localhost:5432/sistema_inventario_BD')



#configuracion de manera local
#class Config:
#    DB_HOST = 'localhost'
#    DB_PORT = '5432'  # Puerto predeterminado de PostgreSQL
#    DB_NAME = 'sistema_inventario_BD'
#    DB_USER = 'postgres'
#    DB_PASSWORD = 'Americ@1927'


#def get_connection():
#    try:
#        connection = psycopg2.connect(
#            host=Config.DB_HOST,
#            user=Config.DB_USER,
#            password=Config.DB_PASSWORD,
#            database=Config.DB_NAME
#        )
#        print("Conexión exitosa")
#        return connection
#   except Exception as ex:
#        print(f"Error de conexión: {ex}")
#        return None
    
def get_connection():
    try:
        connection = psycopg2.connect(Config.DATABASE_URL)
        print("Conexión exitosa a la base de datos")
        return connection
    except Exception as ex:
        print(f"Error al conectar a la base de datos: {ex}")
        raise ex  # Vuelve a lanzar la excepción para verla en los logs
