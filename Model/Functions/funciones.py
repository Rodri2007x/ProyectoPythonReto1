# cargar libros
from Model.Classes.clases import Socio
from Model.Classes.clases import Libro

def cargar_libros():
    libros = []
    with open("Data/libros.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            codigo = datos[0]
            titulo = datos[1]
            autor = datos[2]
            año = datos[3]
            categoría = datos[4]
            codsocio = datos[5] if datos[5] != "None" else None #si no es igual a None, lo asigna, si no, asigna None - Rodrigo

            libro = Libro(codigo, titulo, autor, año, categoría, codsocio)
            libros.append(libro)

    return libros

# cargar socios
def cargar_socios():
    socios = []
    with open("Data/socios.txt", "r", encoding="utf-8") as archivo:
         for linea in archivo:
            datos = linea.strip().split(",")
            codsocio = datos[0]
            nombre = datos[1]
            email = datos[2]
            codiprestado = datos[3] if datos[3] != "None" else None

            socio = Socio(codsocio, nombre, email, codiprestado)
            socios.append(socio)

    return socios

    
# Mostrar libros
def mostrar_libros(libros):
    print("\n+++ Lista de Libros +++")
    for libro in libros:
        print(
            f"\033[1;33mCódigo:\033[0m {libro.codigo}, "
            f"\033[1;33mTítulo:\033[0m {libro.titulo}, "
            f"\033[1;33mAutor:\033[0m {libro.autor}, "
            f"\033[1;33mAño:\033[0m {libro.año}, "
            f"\033[1;33mCategoría:\033[0m {libro.categoría}, "
            f"\033[1;33mCódigo Socio:\033[0m {libro.codsocio}"
        )

# Mostrar socios
def mostrar_socios(socios):
    print("\n+++ Lista de Socios +++")
    for socio in socios:
        print(
            f"\033[1;33mCódigo Socio:\033[0m {socio.codsocio}, "
            f"\033[1;33mNombre:\033[0m {socio.nombre}, "
            f"\033[1;33mEmail:\033[0m {socio.email}, "
            f"\033[1;33mCódigo Prestado:\033[0m {socio.codiprestado}"
        )
# Mostrar libros disponibles
def mostrar_librosdisponibles(libros):
    print("\n+++ Lista de Libros Disponibles +++")
    for libro in libros:
        if libro.codsocio is None:
            print(
                f"\033[1;33mCódigo:\033[0m {libro.codigo}, "
                f"\033[1;33mTítulo:\033[0m {libro.titulo}, "
                f"\033[1;33mAutor:\033[0m {libro.autor}, "
                f"\033[1;33mAño:\033[0m {libro.año}, "
                f"\033[1;33mCategoría:\033[0m {libro.categoría}"
            )


# Buscar libros por título
def buscar_libros_por_titulo(libros):      
    termino_busqueda = input("Ingrese el término de busqueda:").strip().lower()

    if not termino_busqueda:
        print("No se ingresó ningun termino de búsqueda.")
        return

    coincidencias = []

    for libro in libros:
        if termino_busqueda in libro.titulo.lower():
            coincidencias.append(libro)

    if coincidencias:
        mostrar_libros(coincidencias)
    else:
        print("No se encontraron libros que coincidan con el término de búsqueda.")


# Prestar libro
def prestar_libro(libros, socios):
    codigo_libro = input("Código del libro: ").strip()
    codigo_socio = input("Código del socio: ").strip()

    libro_encontrado = None

    for libro in libros:
        if libro.codigo == codigo_libro:
            libro_encontrado = libro
            break

    if libro_encontrado is None:
        print("No existe un libro con ese código.")
        return

    socio_encontrado = None

    for socio in socios:
        if socio.codsocio == codigo_socio:
            socio_encontrado = socio
            break

    if socio_encontrado is None:
        print("No existe un socio con ese código.")
        return

    if socio_encontrado.codiprestado is not None:
        print(f"El socio ya tiene el libro {socio_encontrado.codiprestado}.")
        return

    if libro_encontrado.codsocio is not None:
        print(f"El libro ya está prestado al socio {libro_encontrado.codsocio}.")
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

    codigo_libro = socio_encontrado.codiprestado

    if codigo_libro is None:
        print("El socio no tiene ningún libro prestado.")
        return

    for libro in libros:
        if libro.codigo == codigo_libro and libro.codsocio == codigo_socio:
            libro.codsocio = None
            socio_encontrado.codiprestado = None
            print(f"Se ha devuelto «{libro.titulo}».")
            return

    print("No se encontró el préstamo de ese socio.")

# Mostrar socios con libros prestados
def mostrar_socios_con_prestamo(libros, socios):
    hay_prestamos = False

    for socio in socios:
        if socio.codiprestado is not None:
            for libro in libros:
                if libro.codigo == socio.codiprestado:
                    print(f"{socio.nombre} tiene prestado «{libro.titulo}».")
                    hay_prestamos = True
                    break

    if not hay_prestamos:
        print("No hay socios con libros prestados.")

