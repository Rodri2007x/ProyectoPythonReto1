# cargar libros
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