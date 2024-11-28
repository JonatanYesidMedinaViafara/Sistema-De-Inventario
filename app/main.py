from flask import Flask, render_template, request, jsonify, redirect, url_for
from controllers.login_controller import login
from controllers.proveedor_controller import proveedor_bp, ProveedorModel
from controllers.producto_controller import producto_bp
from controllers.empleado_controller import empleado_bp
from controllers.inventario_controller import inventario_bp 
from controllers.cargo_controller import cargo_bp 
from models.empleado_model import EmpleadoModel
import os
#importacion del Flask Monitoring Dashboard
import flask_monitoringdashboard as dashboard # type: ignore


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'bc6e60f303378878e77f05b318fe3c2a')
# Inicializa Flask Monitoring Dashboard
#dashboard.bind(app)
dashboard.config.init_from(file='config.cfg')


# Registrar el Blueprint
# Registro del blueprint
app.register_blueprint(proveedor_bp, url_prefix='/proveedor')
app.register_blueprint(producto_bp, url_prefix='/producto')
app.register_blueprint(empleado_bp, url_prefix='/empleado')
app.register_blueprint(inventario_bp)
app.register_blueprint(cargo_bp)

# Ruta para la página de inicio
app.config.from_object('config.Config')

@app.route('/')
def index():
    return render_template('login.html')
@app.route('/eliminar_empleado', methods=['GET', 'POST'])
def eliminar_empleado():
    if request.method == 'POST':
        # Manejar la lógica para eliminar un empleado
        cedula = request.form.get('cedula')
        success = EmpleadoModel.eliminar_empleado(cedula)
        if success:
            return jsonify({"status": "success", "message": "Empleado eliminado exitosamente."})
        else:
            return jsonify({"status": "error", "message": "Error al eliminar el empleado."})

    # Si la solicitud es GET, simplemente renderiza el template para la página de eliminación
    return render_template('eliminar_empleado.html')

@app.route('/empleado', methods=['GET', 'POST'])
def empleado():
    if request.method == 'POST':
        # Manejar la lógica para crear un empleado con los datos del formulario

        # Redirigir a la función crear_empleado dentro del blueprint empleado_bp
        return redirect(url_for('empleado_bp.crear_empleado'))

    else:
        return render_template('empleado.html')  # Renderizar la página de empleado para solicitudes GET


# Ruta para la página de bienvenida
@app.route('/bienvenida')
def bienvenida():
    return render_template('bienvenida.html')

# Ruta para la página de bienvenida
@app.route('/lista_cargo')
def lista_cargo():
    return redirect(url_for('cargo_bp.listar_cargos'))

@app.route('/cargos_empleados')
def cargos_empleados():
    return render_template('cargos_empleados.html')

@app.route('/buscar_proveedor', methods=['POST'])
def buscar_proveedor():
    if request.method == 'POST':
        nit_cedula = request.form['nit_cedula']
        success, data = ProveedorModel.buscar_proveedor(nit_cedula)
        if success:
            return jsonify({"status": "success", "data": data})
        else:
            return jsonify({"status": "error", "message": "Proveedor no encontrado."})

# Ruta para la página base
@app.route('/basep')
def base():
    return render_template('base.html')

# Ruta para el controlador del inicio de sesión
app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])

@app.route('/compra')
def compra():
    return render_template('compra.html')

@app.route('/modificar_proveedor', methods=['GET', 'POST'])
def modificar_proveedor():
    if request.method == 'GET':
        return render_template('modificar_proveedor.html')

    if request.method == 'POST':
        nit_cedula = request.form['nit_cedula']
        empresa = request.form['empresa']
        representante = request.form['representante']
        cel_tel = request.form['cel_tel']

        success, message = ProveedorModel.modificar_proveedor(nit_cedula, empresa, representante, cel_tel)

        if success:
            return jsonify({"status": "success", "message": "Proveedor actualizado exitosamente."})
        else:
            return jsonify({"status": "error", "message": message})

@app.route('/venta')
def venta():
    return render_template('venta.html')

@app.route('/eliminar_proveedor')
def eliminar_proveedor():
    return render_template('eliminar_proveedor.html')

@app.route('/inventario')
def inventario():
    return render_template('inventario.html')

@app.route('/producto')
def producto():
    return render_template('producto.html')


@app.route('/buscar_producto')
def buscar_producto():
    return render_template('buscar_producto.html')

@app.route('/eliminar_producto')
def eliminar_producto():
    return render_template('eliminar_producto.html')

# Ruta para cargar la página de modificación de producto
@app.route('/modificar_producto')
def modificar_producto():
    return render_template('modificar_producto.html')

@app.route('/proveedor')
def proveedor():
    return render_template('proveedor.html')

# Ruta para la página de soporte
@app.route('/soporte')
def soporte():
    return render_template('soporte.html')

@app.route('/informacion')
def informacion():
    return render_template('informacion.html')

# Manejador para página no encontrada
def pagina_no_encontrada(error):
    return render_template('404.html'), 404

# Registrar el manejador de página no encontrada
app.register_error_handler(404, pagina_no_encontrada)

#esta era anterio configuracion de app principal cuando se usaba de manera local
#if __name__ == '__main__':
#    app.run(port=7000, debug=True)

#def test_db():
#    conn = get_connection()
#    if conn:
#        return "Conexión a la base de datos exitosa"
#    else:
#        return "Fallo al conectar a la base de datos"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
 