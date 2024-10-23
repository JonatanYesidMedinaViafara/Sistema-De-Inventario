import psycopg2
from psycopg2 import Error

# Función para conectar a la base de datos
def connect_to_db():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="Americ@1927",
            host="127.0.0.1",
            port="5432",
            database="sistema_inventario_BD"
        )
        return connection
    except Error as e:
        print("Error al conectar a la base de datos:", e)