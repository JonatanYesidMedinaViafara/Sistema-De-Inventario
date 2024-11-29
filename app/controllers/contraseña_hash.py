from werkzeug.security import generate_password_hash

# Cambia "mi_contraseña" por la contraseña que desees hashear
password = "Americ@1927"
hashed_password = generate_password_hash(password)
print(hashed_password)
