from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash
from models.login_model import connect_to_db
from psycopg2 import Error
app = Flask(__name__)
app.secret_key = 'a_secure_key_that_is_long_and_unique'
  # Necesaria para manejar mensajes flash
# Controlador para el inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Verificar las credenciales en la base de datos
        connection = connect_to_db()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
                user = cursor.fetchone()
                cursor.close()
                if user and check_password_hash(user[2], password):  # user[2] asumiendo que es la columna de la contraseña hash
                    # Usuario autenticado, redirigir a la página de bienvenida
                    return redirect(url_for('bienvenida'))
                else:
                    # Credenciales incorrectas, mostrar mensaje de error
                    error_message = "Credenciales incorrectas. Por favor, intente de nuevo."
                    print("error de credenciales")
                    return render_template('login.html', error=error_message)
            except Error as e:
                print("Error al verificar las credenciales en la base de datos:", e)
                flash('Error al verificar las credenciales en la base de datos', 'error')
                return render_template('login.html')
            finally:
                connection.close()
        else:
            flash('Error al conectar a la base de datos', 'error')
            return render_template('login.html')
    else:
        return render_template('login.html')
# Controlador para la página de bienvenida
@app.route('/bienvenida')
def bienvenida():
    return render_template('bienvenida.html')
if __name__ == '__main__':
    app.run(port=7000, debug=True)