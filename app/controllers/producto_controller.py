from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from models.producto_model import ProductoModel  

producto_bp = Blueprint('producto_bp', __name__)

@producto_bp.route('/producto', methods=['GET', 'POST'])
def producto_form():
    if request.method == 'POST':
        id_producto = request.form['id_producto']
        nombre_producto = request.form['nombre_producto']
        precio = request.form['precio']
        cantidad = request.form['cantidad']

        success, message = ProductoModel.agregar_producto(
            id_producto=id_producto,
            nombre_producto=nombre_producto,
            precio_producto=precio,
            cantidad_producto=cantidad
        )

        if success:
            return render_template('producto.html', success_message='Producto agregado exitosamente.')
        else:
            return render_template('producto.html', error_message=message)

    return render_template('producto.html')

@producto_bp.route('/buscar_producto', methods=['POST'])
def buscar_producto():
    id_producto = request.form.get('id_producto')
    producto = ProductoModel.buscar_producto(id_producto)
    if producto:
        return render_template('buscar_producto.html', producto=producto)
    else:
        return render_template('buscar_producto.html', error_message='Producto no encontrado')

@producto_bp.route('/eliminar', methods=['POST'])
def eliminar_producto():
    id_producto = request.form.get('id_producto')
    success, message = ProductoModel.eliminar_producto(id_producto)
    if success:
        return jsonify({'status': 'success', 'message': message})
    else:
        return jsonify({'status': 'error', 'message': message})
 

@producto_bp.route('/modificar_producto', methods=['POST','GET'])
def modificar_producto():
    id_producto = request.form.get('id_producto')
    nombre_producto = request.form.get('nombre_producto')
    precio = request.form.get('precio')
    cantidad = request.form.get('cantidad')  # No olvides incluir la cantidad si se va a modificar

    success, message = ProductoModel.modificar_producto(
        id_producto=id_producto,
        nombre_producto=nombre_producto,
        precio_producto=precio,
        cantidad_producto=cantidad
    )

    if success:
        return render_template('buscar_producto.html', success_message='Producto actualizado exitosamente.')
    else:
        return render_template('buscar_producto.html', error_message=message)

