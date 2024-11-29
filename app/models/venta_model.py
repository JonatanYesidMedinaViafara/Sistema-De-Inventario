import psycopg2
from config import Config

class VentaModel:
    @staticmethod
    def registrar_venta(numero_producto, nombre_producto, cantidad, cedula_empleado, nombre_empleado, fecha, hora, precio):
        try:
            conn = psycopg2.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                database=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD
            )
            cursor = conn.cursor()

            # Insertar la venta en la tabla ventas
            cursor.execute("""
                INSERT INTO ventas (numero_producto, nombre_producto, cantidad, cedula_empleado, nombre_empleado, fecha, hora, precio)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (numero_producto, nombre_producto, cantidad, cedula_empleado, nombre_empleado, fecha, hora, precio))

            conn.commit()
            cursor.close()
            conn.close()
            return True, "Venta registrada exitosamente."
        except (Exception, psycopg2.Error) as error:
            return False, f"Error al registrar la venta: {error}"

    @staticmethod
    def buscar_venta_por_id(id_venta):
        try:
            conn = psycopg2.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                database=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ventas WHERE id_venta = %s", (id_venta,))
            venta = cursor.fetchone()
            cursor.close()
            conn.close()
            return venta
        except (Exception, psycopg2.Error) as error:
            print(f"Error al buscar la venta: {error}")
            return None

    @staticmethod
    def eliminar_venta(id_venta):
        try:
            conn = psycopg2.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                database=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD
            )
            cursor = conn.cursor()
            cursor.execute("DELETE FROM ventas WHERE id_venta = %s", (id_venta,))
            conn.commit()
            cursor.close()
            conn.close()
            return True, "Venta eliminada exitosamente."
        except (Exception, psycopg2.Error) as error:
            return False, f"Error al eliminar la venta: {error}"

    @staticmethod
    def actualizar_precio_venta(id_venta, nuevo_precio):
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
                UPDATE ventas 
                SET precio = %s
                WHERE id_venta = %s
            """, (nuevo_precio, id_venta))
            conn.commit()
            cursor.close()
            conn.close()
            return True, "Precio de la venta actualizado exitosamente."
        except (Exception, psycopg2.Error) as error:
            return False, f"Error al actualizar el precio de la venta: {error}"
# Prueba unitaria para la conexión a la base de datos y extracción de datos de la tabla "productos"
def test_conexion_db_productos():
    try:
        # Establecer conexión
        conn = psycopg2.connect(
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            database=Config.DB_NAME,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD
        )
        cursor = conn.cursor()
        
        # Ejecutar consulta
        cursor.execute("SELECT * FROM productos LIMIT 1;")
        producto = cursor.fetchone()
        
        # Cerrar conexión
        cursor.close()
        conn.close()
        
        # Verificar si se obtuvieron resultados
        if producto:
            print("Conexión exitosa y datos obtenidos de la tabla 'productos':", producto)
        else:
            print("Conexión exitosa, pero no se encontraron datos en la tabla 'productos'.")
    except (Exception, psycopg2.Error) as error:
        print("Error al conectar con la base de datos o al extraer datos:", error)

# Ejecutar prueba
test_conexion_db_productos()