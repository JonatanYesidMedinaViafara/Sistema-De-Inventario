# Usa una imagen oficial de Python como base
FROM python:3.10-slim

# Instala las dependencias necesarias para psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requisitos y los instala
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación
COPY . /app


# Establece la variable de entorno FLASK_APP
ENV FLASK_APP=app/app.py

# Exponer el puerto que usará Flask
EXPOSE 5000

# Comando para ejecutar la app
CMD ["flask", "run", "--host=0.0.0.0"]


