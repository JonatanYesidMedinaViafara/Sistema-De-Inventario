import psycopg2
from config import Config

class ProveedorModel:

    @staticmethod
    def agregar_proveedor(empresa, representante, cel_tel, nit_cedula):
        try:
            # Conexión a la base de datos
            conn = psycopg2.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                database=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD
            )

            # Crear un cursor para ejecutar consultas SQL
            cursor = conn.cursor()

            # Consulta para insertar un nuevo proveedor en la base de datos
            cursor.execute("""
                INSERT INTO proveedores (empresa, representante, cel_tel, nit_cedula)
                VALUES (%s, %s, %s, %s)
            """, (empresa, representante, cel_tel, nit_cedula))

            # Guardar los cambios en la base de datos
            conn.commit()

            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()

            return True, "Proveedor agregado exitosamente."

        except (Exception, psycopg2.Error) as error:
            return False, f"Error al agregar proveedor: {error}"

    @staticmethod
    def eliminar_proveedor(nit_cedula):
        try:
            conn = psycopg2.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                database=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD
            )

            cursor = conn.cursor()

            cursor.execute("""
                DELETE FROM proveedores WHERE nit_cedula = %s
            """, (nit_cedula,))

            conn.commit()

            cursor.close()
            conn.close()

            return True, "Proveedor eliminado exitosamente."

        except (Exception, psycopg2.Error) as error:
            return False, f"Error al eliminar proveedor: {error}"

    @staticmethod
    def buscar_proveedor(nit_cedula):
        try:
            conn = psycopg2.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                database=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD
            )

            cursor = conn.cursor()

            print("Buscando proveedor con nit_cedula:", nit_cedula)  # Impresión para depuración

            cursor.execute("""
                SELECT empresa, representante, cel_tel FROM proveedores WHERE nit_cedula = %s
            """, (nit_cedula,))

            # Obtener el primer resultado de la consulta
            proveedor = cursor.fetchone()

            cursor.close()
            conn.close()

            if proveedor:
                # Si se encuentra el proveedor, devolver los datos
                empresa, representante, cel_tel = proveedor
                return True, {"empresa": empresa, "representante": representante, "cel_tel": cel_tel}
            else:
                # Si no se encuentra el proveedor, devolver un mensaje de error
                return False, None

        except (Exception, psycopg2.Error) as error:
            return False, f"Error al buscar proveedor: {error}"
    @staticmethod
    def modificar_proveedor(nit_cedula, empresa, representante, cel_tel):
        try:
            conn = psycopg2.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                database=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD
            )

            cursor = conn.cursor()

            cursor.execute("""
                UPDATE proveedores
                SET empresa = %s, representante = %s, cel_tel = %s
                WHERE nit_cedula = %s
            """, (empresa, representante, cel_tel, nit_cedula))

            conn.commit()

            cursor.close()
            conn.close()

            return True, "Proveedor actualizado exitosamente."

        except (Exception, psycopg2.Error) as error:
            return False, f"Error al actualizar proveedor: {error}"
        

    @staticmethod
    def obtener_todos():
        try:
            conn = psycopg2.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                database=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD
            )
            cursor = conn.cursor()

            cursor.execute("SELECT empresa, nit_cedula FROM proveedores")
            proveedores = cursor.fetchall()

            cursor.close()
            conn.close()

            return [{"empresa": proveedor[0], "nit_cedula": proveedor[1]} for proveedor in proveedores]

        except (Exception, psycopg2.Error) as error:
            print(f"Error al obtener proveedores: {error}")
            return []
        
