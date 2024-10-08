import psycopg2
from config import Config

class EmpleadoModel:
    @staticmethod
    def crear_empleado(cedula, primer_nombre, primer_apellido, segundo_apellido, telefono, cargo, ciudad, direccion, numero_emergencia, nombre_quien_contesta, tipo_sangre):
        try:
            conn = psycopg2.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                database=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD
            )

            cursor = conn.cursor()

            # Verificar si la cédula ya existe
            cursor.execute("SELECT COUNT(*) FROM empleados WHERE cedula = %s", (cedula,))
            if cursor.fetchone()[0] > 0:
                return False, "La cédula ya existe."

            cursor.execute("""
                INSERT INTO empleados (cedula, primer_nombre, primer_apellido, segundo_apellido, telefono, cargo, ciudad, direccion, numero_emergencia, nombre_quien_contesta, tipo_sangre)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (cedula, primer_nombre, primer_apellido, segundo_apellido, telefono, cargo, ciudad, direccion, numero_emergencia, nombre_quien_contesta, tipo_sangre))

            conn.commit()

            cursor.close()
            conn.close()

            return True, "Empleado creado exitosamente."

        except (Exception, psycopg2.Error) as error:
            return False, f"Error al crear empleado: {error}"

    def obtener_empleado_por_cedula(cedula):
        try:
            conn = psycopg2.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                database=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM empleados WHERE cedula = %s", (cedula,))
            empleado = cursor.fetchone()
            cursor.close()
            conn.close()
            return empleado
        except (Exception, psycopg2.Error) as error:
            print(f"Error al obtener empleado: {error}")
            return None

    @staticmethod
    def eliminar_empleado(cedula):
        try:
            conn = psycopg2.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                database=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD
            )
            cursor = conn.cursor()
            cursor.execute("DELETE FROM empleados WHERE cedula = %s", (cedula,))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except (Exception, psycopg2.Error) as error:
            print(f"Error al eliminar empleado: {error}")
            return False
