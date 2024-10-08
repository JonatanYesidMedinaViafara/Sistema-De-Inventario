from flask import Blueprint, jsonify,render_template, request, redirect, url_for
from models.producto_model import ProductoModel


producto_bp = Blueprint('producto_bp', __name__)

@producto_bp.route('/', methods=['GET', 'POST'])
def producto_form():
    if request.method == 'POST':
        id_producto = request.form['id_producto']
        nombre_producto = request.form['nombre_producto']
        precio = request.form['precio']
        cantidad = request.form['cantidad']

        success, message = ProductoModel.agregar_producto(
            id_producto=id_producto,
            nombre_producto=nombre_producto,
            precio=precio,
            cantidad=cantidad
        )

        if success:
            return redirect(url_for('producto_bp.producto_form'))
        else:
            return f"Error: {message}"

    return render_template('producto.html')

@producto_bp.route('/buscar_producto', methods=['POST'])
def buscar_producto():
    id_producto = request.form.get('id_producto')
    producto = ProductoModel.buscar_producto(id_producto)
    if producto:
        return jsonify({'status': 'success', 'data': producto})
    else:
        return jsonify({'status': 'error', 'message': 'Producto no encontrado'})

@producto_bp.route('/eliminar', methods=['POST'])
def eliminar_producto():
    id_producto = request.form.get('id_producto')
    success, message = ProductoModel.eliminar_producto(id_producto)
    if success:
        return jsonify({'status': 'success', 'message': message})
    else:
        return jsonify({'status': 'error', 'message': message})
 

@producto_bp.route('/modificar_producto', methods=['POST'])
def modificar_producto():
    id_producto = request.form.get('id_producto')
    nombre_producto = request.form.get('nombre_producto')
    precio = request.form.get('precio')
    success, message = ProductoModel.modificar_producto(id_producto, nombre_producto, precio)
    if success:
        return jsonify({'status': 'success', 'message': 'Producto actualizado exitosamente.'})
    else:
        return jsonify({'status': 'error', 'message': message})


