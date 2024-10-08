from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from psycopg2 import Error

app = Flask(__name__)

# Conexión a la base de datos
def connect_to_db():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="Americ@1927",
            host="127.0.0.1",
            port="5432",
            database="sistema_inventario_BD"
        )
        return connection
    except Error as e:
        print("Error al conectar a la base de datos:", e)

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
                cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
                user = cursor.fetchone()
                cursor.close()

                if user:
                    # Usuario autenticado, redirigir a la página de bienvenida
                    return redirect(url_for('bienvenida'))
                else:
                    # Credenciales incorrectas, mostrar mensaje de error
                    return render_template('login.html', error='Credenciales incorrectas')
            except Error as e:
                print("Error al verificar las credenciales en la base de datos:", e)
                return render_template('login.html', error='Error al verificar las credenciales en la base de datos')
            finally:
                connection.close()
        else:
            return render_template('login.html', error='Error al conectar a la base de datos')
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(port=7000, debug=True)
