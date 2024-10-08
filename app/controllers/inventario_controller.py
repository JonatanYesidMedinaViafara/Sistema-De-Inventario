from flask import Blueprint, render_template
import psycopg2
from config import Config

# Definir el Blueprint
inventario_bp = Blueprint('inventario_bp', __name__)

# Conectar a la base de datos y obtener los productos
def obtener_productos():
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
            SELECT id_producto, nombre_producto, precio, cantidad
            FROM productos
            ORDER BY nombre_producto
        """)
        productos = cursor.fetchall()
        cursor.close()
        conn.close()

        # Convertir los resultados en una lista de diccionarios
        lista_productos = []
        for producto in productos:
            lista_productos.append({
                'id_producto': producto[0],
                'nombre_producto': producto[1],
                'precio': producto[2],
                'cantidad': producto[3]
            })

        return lista_productos

    except (Exception, psycopg2.Error) as error:
        print(f"Error al obtener productos: {error}")
        return []

# Ruta para mostrar el inventario
@inventario_bp.route('/inventario')
def mostrar_inventario():
    productos = obtener_productos()
    return render_template('inventario.html', productos=productos)
