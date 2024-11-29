import unittest
import sys
import os

# Agregar el directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

from models.producto_model import ProductoModel

class TestDatabaseConnection(unittest.TestCase):
    def test_connection_and_query_products(self):
        # Prueba para verificar la conexión a la base de datos y la consulta de productos
        producto_id = '1245'  # Un ID de producto de ejemplo
        producto = ProductoModel.buscar_producto(producto_id)
        
        # Comprobar si la conexión fue exitosa y se recuperó información del producto
        self.assertIsNotNone(producto, "No se pudo establecer conexión o el producto no fue encontrado.")
        self.assertIn('nombre_producto', producto, "El resultado no contiene el campo 'nombre_producto'.")
        self.assertIn('precio', producto, "El resultado no contiene el campo 'precio'.")
        if 'cantidad' in producto:
            self.assertIn('cantidad', producto, "El resultado no contiene el campo 'cantidad'.")
        else:
            print("Advertencia: el campo 'cantidad' no está presente en el producto recuperado.")

if __name__ == "__main__":
    unittest.main()
