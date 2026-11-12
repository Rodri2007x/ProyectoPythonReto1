from Model.Functions.archivos import cargar_libros, cargar_socios
from Model.Functions.libros import (
    anadir_libro,
    buscar_libros_por_titulo,
    mostrar_libros,
    mostrar_librosdisponibles,
)
from Model.Functions.prestamos import (
    devolver_libro,
    mostrar_socios_con_prestamo,
    prestar_libro,
)
from Model.Functions.socios import anadir_socio, mostrar_socios

# Decir que todos los datos se han cargado 
libros = cargar_libros()
socios = cargar_socios()

print(f"Se han cargado {len(libros)} libros y {len(socios)} socios.")


def menu_socios_y_libros(libros, socios):
    print("\n+++ Socios y libros +++")
    print("1. Añadir socio")
    print("2. Añadir libro")
    print("3. Mostrar socios")
    print("0. Volver al menú principal")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        anadir_socio(socios)
    elif opcion == "2":
        anadir_libro(libros)
    elif opcion == "3":
        mostrar_socios(socios)
    elif opcion != "0":
        print("Opción inválida. Por favor, seleccione una opción válida.")


# Menu principal
def menu_principal():
    while True:
        print("\n+++ Menú Principal +++")
        print("1. Mostrar libros")
        print("2. Mostrar libros disponibles")
        print("3. buscar libros(Titulo)")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Mostrar socios con libros prestados")
        print("7. Añadir socios y libros")
        print("8. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            mostrar_libros(libros)
        elif opcion == "2":
            mostrar_librosdisponibles(libros)
        elif opcion == "3":
            buscar_libros_por_titulo(libros)
        elif opcion == "4":
            prestar_libro(libros, socios)
        elif opcion == "5":
            devolver_libro(libros, socios)
        elif opcion == "6":
            mostrar_socios_con_prestamo(libros, socios)
        elif opcion == "7":
            menu_socios_y_libros(libros, socios)
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu_principal()
