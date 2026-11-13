from Model.Classes.clases import *


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


# Mostrar libros disponibles
def mostrar_librosdisponibles(libros):
    print("\n+++ Lista de Libros Disponibles +++")
    for libro in libros:
        if libro.esta_disponible():
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

# Añadir libro
def anadir_libro(libros):
    codigo = input("Código del libro: ").strip().upper()

    for libro in libros:
        if libro.codigo == codigo:
            print("Ya existe un libro con ese código.")
            return

    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    año = input("Año: ").strip()
    categoria = input("Categoría: ").strip()

    for campo in [codigo, titulo, autor, categoria]:
        if not campo or "," in campo:
            print("Rellena todos los campos y evita las comas.")
            return

    if not año.isdecimal():
        print("Escribe el año con números.")
        return

    nuevo_libro = Libro(codigo, titulo, autor, año, categoria, None)
    libros.append(nuevo_libro)
    print(f"Libro {codigo} añadido.")
