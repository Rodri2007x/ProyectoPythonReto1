from datetime import datetime

from Model.Classes.clases import Libro, Socio


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


def registrar_actividad(evento, detalles):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open("log.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"[{fecha}][{evento}][{detalles}]\n")
    except OSError as error:
        print(f"No se pudo escribir en log.txt: {error}")
        return False

    return True
