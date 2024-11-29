from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from models.venta_model import VentaModel
from models.producto_model import ProductoModel
from models.empleado_model import EmpleadoModel
from datetime import datetime

venta_bp = Blueprint('venta_bp', __name__)

@venta_bp.route('/registrar_venta', methods=['POST'])
def registrar_venta():
    numero_producto = request.form['numero_producto']
    cantidad = int(request.form['cantidad'])
    cedula_empleado = request.form['cedula']
    
    # Obtener información del producto
    producto = ProductoModel.buscar_producto(numero_producto)
    if not producto:
        return "Producto no encontrado", 404

    nombre_producto = producto['nombre_producto']
    precio_unitario = producto['precio']
    if cantidad > producto['cantidad']:
        return "Cantidad solicitada no disponible", 400

    # Obtener información del empleado
    empleado = EmpleadoModel.obtener_empleado_por_cedula(cedula_empleado)
    if not empleado:
        return "Empleado no encontrado", 404

    nombre_empleado = f"{empleado[1]} {empleado[2]}"

    # Generar fecha y hora actual
    fecha = datetime.now().date()
    hora = datetime.now().time()

    # Calcular el precio total
    precio_total = precio_unitario * cantidad

    # Registrar la venta
    success, message = VentaModel.registrar_venta(numero_producto, nombre_producto, cantidad, cedula_empleado, nombre_empleado, fecha, hora, precio_total)
    if success:
        return redirect(url_for('venta_bp.registro_ventas'))
    else:
        return message, 500

@venta_bp.route('/registro_ventas', methods=['GET'])
def registro_ventas():
    return render_template('venta.html')

@venta_bp.route('/buscar_producto/<numero_producto>', methods=['GET'])
def buscar_producto(numero_producto):
    producto = ProductoModel.buscar_producto(numero_producto)
    if producto:
        return jsonify(producto)
    else:
        return jsonify(None), 404

@venta_bp.route('/buscar_empleado/<cedula>', methods=['GET'])
def buscar_empleado(cedula):
    empleado = EmpleadoModel.obtener_empleado_por_cedula(cedula)
    if empleado:
        return jsonify({
            'primer_nombre': empleado[1],
            'primer_apellido': empleado[2]
        })
    else:
        return jsonify(None), 404

@venta_bp.route('/obtener_nombre_producto', methods=['POST'])
def obtener_nombre_producto():
    numero_producto = request.json.get('numero_producto')
    producto = ProductoModel.buscar_producto(numero_producto)
    if producto:
        return jsonify({'nombre_producto': producto['nombre_producto']})
    else:
        return jsonify({'error': 'Producto no encontrado'}), 404
