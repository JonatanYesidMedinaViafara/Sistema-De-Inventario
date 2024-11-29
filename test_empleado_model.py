import unittest
import sys
import os

# Agregar el directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

from models.empleado_model import EmpleadoModel

class TestEmpleadoModel(unittest.TestCase):
    def test_crear_empleado(self):
        # Datos reales para crear un empleado
        cedula = '1234567890'
        primer_nombre = 'María'
        primer_apellido = 'González'
        segundo_apellido = 'López'
        telefono = '555-1234'
        cargo = 'MESERA'
        ciudad = 'Ciudad de México'
        direccion = 'Calle 123, Colonia Centro'
        numero_emergencia = '555-5678'
        nombre_quien_contesta = 'Pedro González'
        tipo_sangre = 'O+'

        # Eliminar el empleado si ya existe
        EmpleadoModel.eliminar_empleado(cedula)

        # Crear el empleado
        success, message = EmpleadoModel.crear_empleado(
            cedula, primer_nombre, primer_apellido, segundo_apellido,
            telefono, cargo, ciudad, direccion, numero_emergencia,
            nombre_quien_contesta, tipo_sangre
        )
        
        # Comprobar si el empleado fue creado exitosamente
        self.assertTrue(success, f"Fallo al crear el empleado: {message}")

    def test_obtener_empleado_por_cedula(self):
        # Cédula real para buscar un empleado
        cedula = '1234567890'

        # Obtener el empleado
        empleado = EmpleadoModel.obtener_empleado_por_cedula(cedula)

        # Comprobar si el empleado fue encontrado
        self.assertIsNotNone(empleado, "No se pudo encontrar el empleado con la cédula proporcionada.")
        self.assertEqual(str(empleado[1]), cedula, "La cédula del empleado recuperado no coincide.")

if __name__ == "__main__":
    unittest.main()

