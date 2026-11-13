from Model.Classes.clases import *


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

# Añadir socio
def anadir_socio(socios):
    codigo = input("Código del socio: ").strip().upper()

    for socio in socios:
        if socio.codsocio == codigo:
            print("Ya existe un socio con ese código.")
            return

    nombre = input("Nombre: ").strip()
    email = input("Email: ").strip()

    for campo in [codigo, nombre, email]:
        if not campo or "," in campo:
            print("Rellena todos los campos y evita las comas.")
            return

    nuevo_socio = Socio(codigo, nombre, email, None)
    socios.append(nuevo_socio)
    print(f"Socio {codigo} añadido.")
