import psycopg2
from config import Config

class ProductoModel:

    @staticmethod
    def agregar_producto(id_producto, nombre_producto, precio, cantidad):
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
                INSERT INTO productos (id_producto, nombre_producto, precio, cantidad)
                VALUES (%s, %s, %s, %s)
            """, (id_producto, nombre_producto, precio, cantidad))
            conn.commit()
            cursor.close()
            conn.close()
            return True, "Producto agregado exitosamente."
        except (Exception, psycopg2.Error) as error:
            return False, f"Error al agregar producto: {error}"

    @staticmethod
    def buscar_producto(id_producto):
        try:
            conn = psycopg2.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                database=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD
            )
            cursor = conn.cursor()
            cursor.execute("SELECT nombre_producto, precio, cantidad FROM productos WHERE id_producto = %s", (id_producto,))
            row = cursor.fetchone()
            cursor.close()
            conn.close()
            if row:
                return {'nombre_producto': row[0], 'precio': row[1], 'cantidad': row[2]}
            else:
                return None
        except (Exception, psycopg2.Error) as error:
            print(f"Error al buscar producto: {error}")
            return None

    @staticmethod
    def eliminar_producto(id_producto):
        try:
            conn = psycopg2.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                database=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD
            )
            cursor = conn.cursor()
            cursor.execute("DELETE FROM productos WHERE id_producto = %s", (id_producto,))
            conn.commit()
            cursor.close()
            conn.close()
            return True, "Producto eliminado exitosamente."
        except (Exception, psycopg2.Error) as error:
            return False, f"Error al eliminar producto: {error}"

    @staticmethod
    def buscar_producto(id_producto):
        try:
            conn = psycopg2.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                database=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD
            )
            cursor = conn.cursor()
            cursor.execute("SELECT nombre_producto, precio FROM productos WHERE id_producto = %s", (id_producto,))
            producto = cursor.fetchone()
            cursor.close()
            conn.close()
            if producto:
                return {'nombre_producto': producto[0], 'precio': producto[1]}
            else:
                return None
        except Exception as error:
            print(f"Error al buscar el producto: {error}")
            return None

    @staticmethod
    def modificar_producto(id_producto, nombre_producto, precio):
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
                UPDATE productos 
                SET nombre_producto = %s, precio = %s
                WHERE id_producto = %s
            """, (nombre_producto, precio, id_producto))
            conn.commit()
            cursor.close()
            conn.close()
            return True, "Producto actualizado exitosamente."
        except Exception as error:
            return False, f"Error al actualizar el producto: {error}"

