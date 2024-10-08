from flask import Blueprint, render_template, request, redirect, url_for
from models.cargo_model import CargoModel

cargo_bp = Blueprint('cargo_bp', __name__)

@cargo_bp.route('/cargos_empleados', methods=['GET', 'POST'])
def crear_cargo():
    if request.method == 'POST':
        nombre_cargo = request.form.get('nombre_cargo')
        descripcion_cargo = request.form.get('descripcion_cargo')
        usos_compra = request.form.get('usos_compra') == 'true'
        usos_venta = request.form.get('usos_venta') == 'true'

        success, message = CargoModel.crear_cargo(
            nombre_cargo=nombre_cargo,
            descripcion_cargo=descripcion_cargo,
            usos_compra=usos_compra,
            usos_venta=usos_venta
        )

        if success:
            return redirect(url_for('cargo_bp.crear_cargo'))
        else:
            return f"Error: {message}"

    return render_template('cargos_empleados.html')

@cargo_bp.route('/lista_cargos')
def listar_cargos():
    cargos = CargoModel.obtener_todos_los_cargos()
    return render_template('lista_cargo.html', cargos=cargos)
