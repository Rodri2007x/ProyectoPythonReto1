from Errors.errores import *
from Model.Functions.archivos import *


# Prestar libro
def prestar_libro(libros, socios):
    codigo_libro = input("Código del libro: ").strip()
    codigo_socio = input("Código del socio: ").strip()

    try:
        libro_encontrado = None
        for libro in libros:
            if libro.codigo == codigo_libro:
                libro_encontrado = libro
                break

        if libro_encontrado is None:
            raise ErrorPrestamo("No existe un libro con ese código.", codigo_libro)

        socio_encontrado = None
        for socio in socios:
            if socio.codsocio == codigo_socio:
                socio_encontrado = socio
                break

        if socio_encontrado is None:
            raise ErrorPrestamo("No existe un socio con ese código.", codigo_socio)

        if socio_encontrado.tiene_libro_prestado():
            raise ErrorPrestamo(
                f"El socio ya tiene el libro {socio_encontrado.codiprestado}.",
                codigo_socio,
            )

        if not libro_encontrado.esta_disponible():
            raise ErrorPrestamo(
                f"El libro ya está prestado al socio {libro_encontrado.codsocio}.",
                codigo_libro,
            )
    except ErrorPrestamo as error:
        print(error.mensaje_detallado())
        return

    detalles = f"Libro {libro_encontrado.codigo}, socio {socio_encontrado.codsocio}"
    if not registrar_actividad("Préstamo", detalles):
        return

    libro_encontrado.codsocio = socio_encontrado.codsocio
    socio_encontrado.codiprestado = libro_encontrado.codigo

    print(f"Se ha prestado «{libro_encontrado.titulo}» a {socio_encontrado.nombre}.")


# Devolver libro
def devolver_libro(libros, socios):
    codigo_socio = input("Código del socio: ").strip()
    socio_encontrado = None

    for socio in socios:
        if socio.codsocio == codigo_socio:
            socio_encontrado = socio
            break

    if socio_encontrado is None:
        print("No existe un socio con ese código.")
        return

    if not socio_encontrado.tiene_libro_prestado():
        print("El socio no tiene ningún libro prestado.")
        return

    codigo_libro = socio_encontrado.codiprestado
    for libro in libros:
        if libro.codigo == codigo_libro and libro.codsocio == codigo_socio:
            detalles = f"Libro {libro.codigo}, socio {socio_encontrado.codsocio}"
            if not registrar_actividad("Devolución", detalles):
                return

            libro.codsocio = None
            socio_encontrado.codiprestado = None
            print(f"Se ha devuelto «{libro.titulo}».")
            return

    print("No se encontró el préstamo de ese socio.")


# Mostrar socios con libros prestados
def mostrar_socios_con_prestamo(libros, socios):
    hay_prestamos = False

    for socio in socios:
        if socio.tiene_libro_prestado():
            for libro in libros:
                if libro.codigo == socio.codiprestado:
                    print(f"{socio.nombre} tiene prestado «{libro.titulo}».")
                    hay_prestamos = True
                    break

    if not hay_prestamos:
        print("No hay socios con libros prestados.")
