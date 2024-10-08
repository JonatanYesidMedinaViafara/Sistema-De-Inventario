import psycopg2
from config import Config

class CargoModel:
    @staticmethod
    def crear_cargo(nombre_cargo, descripcion_cargo, usos_compra, usos_venta):
        try:
            conn = psycopg2.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                database=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD
            )

            cursor = conn.cursor()

            # Verificar si el nombre del cargo ya existe
            cursor.execute("SELECT COUNT(*) FROM cargos WHERE nombre_cargo = %s", (nombre_cargo,))
            if cursor.fetchone()[0] > 0:
                return False, "El nombre del cargo ya existe."

            cursor.execute("""
                INSERT INTO cargos (nombre_cargo, descripcion_cargo, usos_compra, usos_venta)
                VALUES (%s, %s, %s, %s)
            """, (nombre_cargo, descripcion_cargo, usos_compra, usos_venta))

            conn.commit()

            cursor.close()
            conn.close()

            return True, "Cargo creado exitosamente."

        except (Exception, psycopg2.Error) as error:
            return False, f"Error al crear cargo: {error}"

    @staticmethod
    def obtener_todos_los_cargos():
        try:
            conn = psycopg2.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                database=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD
            )
            cursor = conn.cursor()
            cursor.execute("SELECT nombre_cargo, descripcion_cargo, usos_compra, usos_venta FROM cargos")
            cargos = cursor.fetchall()
            cursor.close()
            conn.close()
            return cargos
        except (Exception, psycopg2.Error) as error:
            print(f"Error al obtener cargos: {error}")
            return []

    @staticmethod
    def obtener_solo_los_cargos():
        try:
            conn = psycopg2.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                database=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD
            )
            cursor = conn.cursor()
            cursor.execute("SELECT nombre_cargo FROM cargos")
            cargos = cursor.fetchall()
            cursor.close()
            conn.close()
            return cargos
        except (Exception, psycopg2.Error) as error:
            print(f"Error al obtener cargos: {error}")
            return []
