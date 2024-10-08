from flask import Blueprint, render_template, request, jsonify, redirect, url_for

from models.empleado_model import EmpleadoModel
from models.cargo_model import CargoModel  # Añade esta línea para importar CargoModel

empleado_bp = Blueprint('empleado_bp', __name__)

@empleado_bp.route('/empleado', methods=['GET', 'POST'])
def crear_empleado():
    if request.method == 'POST':
        cedula = request.form.get('cedula')
        primer_nombre = request.form.get('primer_nombre')
        primer_apellido = request.form.get('primer_apellido')
        segundo_apellido = request.form.get('segundo_apellido')
        telefono = request.form.get('telefono')
        cargo = request.form.get('cargo')
        ciudad = request.form.get('ciudad')
        direccion = request.form.get('direccion')
        numero_emergencia = request.form.get('numero_emergencia')
        nombre_quien_contesta = request.form.get('nombre_quien_contesta')
        tipo_sangre = request.form.get('tipo_sangre')

        success, message = EmpleadoModel.crear_empleado(
            cedula=cedula,
            primer_nombre=primer_nombre,
            primer_apellido=primer_apellido,
            segundo_apellido=segundo_apellido,
            telefono=telefono,
            cargo=cargo,
            ciudad=ciudad,
            direccion=direccion,
            numero_emergencia=numero_emergencia,
            nombre_quien_contesta=nombre_quien_contesta,
            tipo_sangre=tipo_sangre
        )

        if success:
            return redirect(url_for('empleado_bp.crear_empleado'))
        else:
            return f"Error: {message}"

    cargos = CargoModel.obtener_solo_los_cargos()
    print(cargos)  # Esto imprimirá la lista de cargos en la consola del servidor Flask
    return render_template('empleado.html', cargos=cargos)


@empleado_bp.route('/', methods=['GET', 'POST'])
def buscar_empleado():
    if request.method == 'POST':
        cedula = request.form.get('cedula')
        empleado = EmpleadoModel.obtener_empleado_por_cedula(cedula)
        if empleado:
            return jsonify({"status": "success", "data": empleado})
        else:
            return jsonify({"status": "error", "message": "Empleado no encontrado."})
    return render_template('eliminar_empleado.html')

@empleado_bp.route('/liminar', methods=['POST'])
def eliminar_empleado():
    cedula = request.form.get('cedula')
    success = EmpleadoModel.eliminar_empleado(cedula)
    if success:
        return jsonify({"status": "success", "message": "Empleado eliminado exitosamente."})
    else:
        return jsonify({"status": "error", "message": "Error al eliminar el empleado."})
