import psycopg2
from config import Config
class ProductoModel:
    @staticmethod
    def agregar_producto(id_producto, nombre_producto, precio_producto, cantidad_producto):
        try:
            # Conexión a la base de datos
            conn = psycopg2.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                database=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD
            )
            cursor = conn.cursor()
            # Verificar si el producto ya existe
            cursor.execute("SELECT * FROM producto WHERE id_producto = %s OR nombre_producto = %s", (id_producto, nombre_producto))
            producto_existente = cursor.fetchone()
            if producto_existente:
                return False, "El producto ya existe."
            # Insertar el nuevo producto
            cursor.execute("""
                INSERT INTO producto (id_producto, nombre_producto, precio_producto, cantidad_producto)
                VALUES (%s, %s, %s, %s)
            """, (id_producto, nombre_producto, precio_producto, cantidad_producto))
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
            cursor.execute("SELECT nombre_producto, precio_producto, cantidad_producto FROM producto WHERE id_producto = %s", (id_producto,))
            row = cursor.fetchone()
            cursor.close()
            conn.close()
            if row:
                return {'nombre_producto': row[0], 'precio_producto': row[1], 'cantidad_producto': row[2]}
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
            cursor.execute("DELETE FROM producto WHERE id_producto = %s", (id_producto,))
            conn.commit()
            cursor.close()
            conn.close()
            return True, "Producto eliminado exitosamente."
        except (Exception, psycopg2.Error) as error:
            return False, f"Error al eliminar producto: {error}"

    @staticmethod
    def modificar_producto(id_producto, nombre_producto, precio_producto, cantidad_producto):
        try:
            # Conexión a la base de datos
            conn = psycopg2.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                database=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD
            )
            cursor = conn.cursor()
            
            # Verificar si el producto existe
            cursor.execute("SELECT id_producto FROM producto WHERE id_producto = %s", (id_producto,))
            if not cursor.fetchone():
                cursor.close()
                conn.close()
                return False, "Producto no encontrado."

            # Modificar el producto en la base de datos
            cursor.execute("""
                UPDATE producto
                SET nombre_producto = %s,
                    precio_producto = %s,
                    cantidad_producto = %s
                WHERE id_producto = %s
            """, (nombre_producto, precio_producto, cantidad_producto, id_producto))

            # Confirmar cambios
            conn.commit()
            cursor.close()
            conn.close()
            return True, "Producto actualizado exitosamente."

        except (Exception, psycopg2.Error) as error:
            print(f"Error al modificar producto: {error}")
            return False, "Error al modificar producto."