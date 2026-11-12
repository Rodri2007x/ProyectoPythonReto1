from Model.Classes.clases import *
from Model.Functions.funciones import *

# Decir que todos los datos se han cargado 
libros = cargar_libros()
socios = cargar_socios()

print(f"Se han cargado {len(libros)} libros y {len(socios)} socios.")


# Menu principal
def menu_principal():
    while True:
        print("\n+++ Menú Principal +++")
        print("1. Mostrar libros")
        print("2. Mostrar libros disponibles")
        print("3. buscar libros(Titulo)")
        print("4. Mostrar socios")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Mostrar socios con libros prestados")
        print("8. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            mostrar_libros(libros)
        elif opcion == "2":
            mostrar_librosdisponibles(libros)
        elif opcion == "3":
            buscar_libros_por_titulo(libros)
        elif opcion == "4":
            mostrar_socios(socios)
        elif opcion == "5":
            prestar_libro(libros, socios)
        elif opcion == "6":
            devolver_libro(libros, socios)
        elif opcion == "7":
            mostrar_socios_con_prestamo(libros, socios)
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu_principal()
