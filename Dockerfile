# Usa una imagen oficial de Python
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt e instala las dependencias
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código fuente de la app
COPY . /app

# Establece el subdirectorio donde se encuentra el archivo app.py
WORKDIR /app/app

# Expone el puerto 5000
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
