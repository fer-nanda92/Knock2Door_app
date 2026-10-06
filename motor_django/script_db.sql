-- Script de creación de Base de Datos y Usuario para la entrega
CREATE DATABASE IF NOT EXISTS mi_base_datos CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'Usuario'@'%' IDENTIFIED BY 'mi_contraseña';

GRANT ALL PRIVILEGES ON mi_base_datos.* TO 'Usuario'@'%';

FLUSH PRIVILEGES;

