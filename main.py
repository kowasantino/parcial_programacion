from inputs import participantes, puntajes, cargar_participantes, cargar_puntuaciones
from funciones import (
    mostrar_puntuaciones,
    mostrar_menores_a_4,
    mostrar_menores_8,
    mostrar_promedio_por_jurado,
    jurado_mas_estricto,
    jurado_mas_generoso,
    participantes_con_puntajes_iguales,
    buscar_participante,
    mostrar_top_3,
    mostrar_participantes_ordenados,
    mostrar_ganador
)

def mostrar_menu():
    print("\n--- MENU PRINCIPAL ---")
    print("1. Cargar participantes")
    print("2. Cargar puntuaciones")
    print("3. Mostrar puntuaciones")
    print("4. Participantes con promedio menor a 4")
    print("5. Participantes con promedio menor a 8")
    print("6. Promedio de cada jurado")
    print("7. Jurado más estricto")
    print("8. Jurado más generoso")
    print("9. Participantes con puntuaciones iguales")
    print("10. Buscar participante por nombre")
    print("11. Mostrar top 3 participantes")
    print("12. Mostrar participantes ordenados alfabéticamente")
    print("13. Mostrar ganador")
    print("0. Salir")

def programa():
    cargado = False
    puntajes_cargados = False
    salir = False

    while not salir:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            cargar_participantes()
            cargado = True
        elif opcion == "2":
            if cargado:
                cargar_puntuaciones()
                puntajes_cargados = True
            else:
                print("Primero debe cargar los participantes.")
        elif opcion == "3":
            if cargado and puntajes_cargados:
                mostrar_puntuaciones(participantes, puntajes)
            else:
                print("Debe cargar participantes y puntajes.")
        elif opcion == "4":
            mostrar_menores_a_4(participantes, puntajes)
        elif opcion == "5":
            mostrar_menores_8(participantes, puntajes)
        elif opcion == "6":
            mostrar_promedio_por_jurado(puntajes)
        elif opcion == "7":
            jurado_mas_estricto(puntajes)
        elif opcion == "8":
            jurado_mas_generoso(puntajes)
        elif opcion == "9":
            participantes_con_puntajes_iguales(participantes, puntajes)
        elif opcion == "10":
            buscar_participante(participantes, puntajes)
        elif opcion == "11":
            mostrar_top_3(participantes, puntajes)
        elif opcion == "12":
            mostrar_participantes_ordenados(participantes, puntajes)
        elif opcion == "13":
            if cargado and puntajes_cargados:
             mostrar_ganador(participantes, puntajes)
            else:
                print("Debe cargar participantes y puntajes.")
        elif opcion == "0":
            print("Saliendo del programa...")
            salir = True
        else:
            print("Opción no válida. Intente nuevamente.")

programa()
