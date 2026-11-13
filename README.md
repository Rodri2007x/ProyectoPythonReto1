# Reto 1 Python

Aplicación de consola en Python para consultar el catálogo de una biblioteca, gestionar socios y registrar préstamos y devoluciones.

## Posibles mejoras de la aplicación

### 1. Usar una base de datos

Podríamos guardar los libros, los socios y los préstamos en una base de datos en lugar de usar archivos TXT. Para una primera versión se podría usar SQLite e importar los datos actuales. Esto permitiría conservar los cambios al cerrar el programa y consultar el historial de préstamos de cada socio.

### 2. Consultar el catálogo desde una web

Podríamos crear una página web donde los socios puedan buscar libros y ver si están disponibles. El personal de la biblioteca podría usar la misma página para dar de alta libros y socios y gestionar los préstamos desde el navegador.

### 3. Reservar libros prestados

Si un libro está prestado, el socio podría reservarlo. Al devolverlo, el sistema avisaría al primer socio de la lista de espera para que pueda recogerlo.

### 4. Añadir fechas de devolución

Cada préstamo podría tener una fecha límite. Así los socios podrían consultar cuándo deben devolver sus libros y la biblioteca podría identificar los préstamos atrasados.

## Cómo ejecutar el proyecto

Con Python 3, abre una terminal en la carpeta que contiene `main.py` y ejecuta `python main.py`.
