CREATE TABLE empleados (
    id SERIAL PRIMARY KEY,
    cedula VARCHAR(50) UNIQUE NOT NULL,
    primer_nombre VARCHAR(100) NOT NULL,
    primer_apellido VARCHAR(100) NOT NULL,
    segundo_apellido VARCHAR(100),
    telefono VARCHAR(50) NOT NULL,
    cargo VARCHAR(100) NOT NULL,
    ciudad VARCHAR(100) NOT NULL,
    direccion TEXT NOT NULL,
    numero_emergencia VARCHAR(50) NOT NULL,
    nombre_quien_contesta VARCHAR(100) NOT NULL,
    tipo_sangre VARCHAR(10) NOT NULL
);

    estado BOOLEAN NOT NULL DEFAULT TRUE
);

SELECT * FROM empleados
SELECT * FROM users

UPDATE empleados SET estado = false WHERE cedula = '"111873213121231212"';
UPDATE empleados SET estado = false WHERE cedula = '111873213121231212';

-- Crear la tabla proveedores
SELECT * FROM proveedores
CREATE TABLE proveedores (
    id SERIAL PRIMARY KEY,
    empresa VARCHAR(100) NOT NULL,
    representante VARCHAR(100) NOT NULL,
    cel_tel VARCHAR(50),
    nit_cedula VARCHAR(50) NOT NULL
);
DELETE FROM proveedores WHERE nit_cedula = '123456'
SELECT empresa, representante, cel_tel FROM proveedores WHERE nit_cedula ='14785236'

--crear la tabla de productos
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    id_producto VARCHAR(50) UNIQUE NOT NULL,
    nombre_producto VARCHAR(100) NOT NULL,
    precio NUMERIC(10, 2) NOT NULL,
    cantidad INTEGER NOT NULL
);
ALTER TABLE productos RENAME COLUMN numero_producto TO id_producto;

DROP TABLE empleados;

SELECT * FROM productos
DELETE  productos
SELECT nombre_producto, proveedor, precio, cantidad FROM productos WHERE numero_producto = '1111'

CREATE TABLE cargos (
    id SERIAL PRIMARY KEY,
    nombre_cargo VARCHAR(100) UNIQUE NOT NULL,
    descripcion_cargo TEXT NOT NULL,
    usos_compra BOOLEAN NOT NULL,
    usos_venta BOOLEAN NOT NULL
);
SELECT * FROM cargos

INSERT INTO empleados (cedula, primer_nombre, primer_apellido, segundo_apellido, telefono, cargo, ciudad, direccion, numero_emergencia, nombre_quien_contesta, tipo_sangre) 
VALUES 
('1234567890', 'María', 'González', 'López', '555-1234', 'MESERA', 'Ciudad de México', 'Calle 123, Colonia Centro', '555-5678', 'Pedro González', 'O+'),
('0987654321', 'Ana', 'Martínez', 'Pérez', '555-4321', 'MESERA', 'Guadalajara', 'Av. Principal 456, Colonia Norte', '555-8765', 'Juan Martínez', 'A-'),
('5678901234', 'Laura', 'Rodríguez', 'Gómez', '555-9876', 'MESERA', 'Monterrey', 'Carrera 789, Colonia Sur', '555-2345', 'Luis Rodríguez', 'B+');

