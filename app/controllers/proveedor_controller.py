from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models.proveedor_model import ProveedorModel

proveedor_bp = Blueprint('proveedor_bp', __name__)

@proveedor_bp.route('/', methods=['GET', 'POST'])
def proveedor_form():
    if request.method == 'POST':
        empresa = request.form['empresa']
        representante = request.form['representante']
        cel_tel = request.form['cel_tel']
        nit_cedula = request.form['nit_cedula']

        success, message = ProveedorModel.agregar_proveedor(
            empresa=empresa,
            representante=representante,
            cel_tel=cel_tel,
            nit_cedula=nit_cedula
        )

        if success:
            return redirect(url_for('proveedor_bp.proveedor_form'))
        else:
            return f"Error: {message}"

    return render_template('proveedor.html')

@proveedor_bp.route('/eliminar', methods=['POST'])
def eliminar_proveedor():
    if request.method == 'POST':
        nit_cedula = request.form['nit_cedula']

        success, message = ProveedorModel.eliminar_proveedor(nit_cedula)

        if success:
            return jsonify({"status": "success", "message": "Proveedor eliminado exitosamente."})
        else:
            return jsonify({"status": "error", "message": message})

@proveedor_bp.route('/modificar_proveedor', methods=['POST'])
def modificar_proveedor():
    nit_cedula = request.form['nit_cedula']
    empresa = request.form['empresa']
    representante = request.form['representante']
    cel_tel = request.form['cel_tel']

    success, message = ProveedorModel.modificar_proveedor(nit_cedula, empresa, representante, cel_tel)

    if success:
        return jsonify({"status": "success", "message": "Proveedor actualizado exitosamente."})
    else:
        return jsonify({"status": "error", "message": message})

@proveedor_bp.route('/buscar_proveedor', methods=['POST'])
def buscar_proveedor():
    if request.method == 'POST':
        nit_cedula = request.form['nit_cedula']

        # Llama al método en el modelo para buscar el proveedor
        success, data = ProveedorModel.buscar_proveedor(nit_cedula)

        if success:
            return jsonify({"status": "success", "data": data})
        else:
            return jsonify({"status": "error", "message": "Proveedor no encontrado."})
