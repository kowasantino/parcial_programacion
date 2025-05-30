def mostrar_menu():
    print("\n--- MENU PRINCIPAL ---")
    print("1. Cargar participantes")
    print("2. Cargar puntuaciones")
    print("3. Mostrar puntuaciones")
    print("4. Participantes con promedio menor a 4")
    print("5. Participantes con promedio menor a 8")
    print("6. Promedio de cada jurado")
    print("7. Jurado mas estricto")
    print("8. Jurado mas generoso")
    print("9. Participantes con puntuaciones iguales")
    print("10. Buscar participante por nombre")
    print("11. Mostrar top 3 participantes")
    print("12. Mostrar participantes ordenados alfabeticamente")
    print("0. Salir")

def programa():
    salir = False
    while not salir:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            cargar_participantes()
        elif opcion == "2":
            cargar_puntuaciones() 
        elif opcion == "3":
            mostrar_puntuaciones()
        elif opcion == "4":
            mostrar_menores_a_4()
        elif opcion == "5":
            mostrar_menores_8()  
        elif opcion == "6":
            mostrar_promedio_por_jurado() 
        elif opcion == "7":
            jurado_mas_estricto() 
        elif opcion == "8":
            jurado_mas_generoso()
        elif opcion == "9":
            participantes_con_puntajes_iguales()
        elif opcion == "10": 
            buscar_participante()
        elif opcion == "11":
            mostrar_top_3()
        elif opcion == "12":
            mostrar_participantes_ordenados()
        elif opcion == "0":
            print("Saliendo del programa...")
            salir = True
        else:
            print("Opcion no valida. Intente nuevamente")

participantes = [""] * 5

def nombre_valido(nombre):
    if len(nombre) < 3:
        return False
    for caracter in nombre:
        if not (caracter.isalpha() or caracter == " "):
            return False
    return True

def cargar_participantes():
    print("\n--- Cargar Participantes ---")
    for i in range(5):
        while True:
            nombre = input(f"Ingrese el nombre del participante #{i + 1}: ").strip()
            if nombre_valido(nombre):
                participantes[i] = nombre
                break
            else:
                print("Nombre inválido. Debe tener al menos 3 letras y solo contener letras y espacios.")

puntajes = [[0,0,0] for _ in range(5)]
def puntuacion_valida(p):
    return p.isdigit() and 1 <= int(p) <= 10

def cargar_puntuaciones():
    print("\n--- CARGAR PUNTUACIONES ---")
    for i in range(5):
        print(f"\nParticipante: {participantes[i]}")
        for j in range(3):
            while True:
                entrada = input(f"Ingrese puntaje del jurado #{j + 1}: ")
                if puntuacion_valida(entrada):
                    puntajes[i][j] = int(entrada)
                    break
                else:
                    print("Puntaje inválido. Debe ser un número del 1 al 10.")

def mostrar_puntuaciones():
    print("\n--- PUNTUACIONES ---\n")
    for i in range(5):
        nombre = participantes[i]
        p1 = puntajes[i][0]
        p2 = puntajes[i][1]
        p3 = puntajes[i][2]
        total = p1 +  p2 + p3
        promedio = total / 3

        print(f"NOMBRE PARTICIPANTE: {nombre}")
        print(f"PUNTAJE JURADO 1: {p1}")
        print(f"PUNTAJE JURADO 2: {p2}")
        print(f"PUNTAJE JURADO 3: {p3}")
        print(f"PUNTAJE PROMEDIO: {round(promedio, 2)}/10\n")

def promedio (p1, p2, p3):
    return (p1 + p2 + p3) / 3

def mostrar_menores_a_4():
    print("\n--- PARTICIPANTES CON PROMEDIO MENOR A 4 ---\n")
    hay_menores = False

    for i in range(5):
        p1, p2, p3 = puntajes[i]
        prom = promedio(p1,p2,p3)
        if prom < 4:
            print(f"{participantes[i]} - Promedio: {round(prom, 2)}/10")
            hay_menores = True
    if not hay_menores:
        print("No hay participantes con promedio menor a 4")
    
def mostrar_menores_8():
    print("\n--- PARTICIPANTES CON PROMEDIO MENOR A 8 ---\n")
    hay_resultados = False

    for i in range(5):
        p1, p2, p3 = puntajes[i]
        prom = promedio(p1,p2,p3)
        if 4 <= prom < 8:
            print(f"{participantes[i]} - Promedio: {round(prom, 2)}/10")
            hay_resultados = True
    if not hay_resultados:
        print("No hay participantes con promedio menor a 8 y mayor o igual a 4")

def promedio_jurado(jurado_index):
    total = 0
    for i in range(5):
        total += puntajes [i][jurado_index]
    return total / 5

def mostrar_promedio_por_jurado():
    print("\n--- PROMEDIO POR JURADO ---\n")
    for j in range(3):
        promedio = promedio_jurado(j)
        print(f"Jurado #{j + 1}: Promedio {round(promedio, 2)}/10")

def jurado_mas_estricto():
    menor_promedio = promedio_jurado(0)
    jurado_estricto = 0

    for j in range(1, 3):
        promedio_actual = promedio_jurado(j)
        if promedio_actual < menor_promedio:
            menor_promedio = promedio_actual
            jurado_estricto = j

    print(f"\nJurado mas estricto: Jurado #{jurado_estricto + 1} con promedio {round(menor_promedio, 2)}/10")

def jurado_mas_generoso():
    mayor_promedio = promedio_jurado(0)
    jurado_generoso = 0

    for j in range(1, 3):
        promedio_actual = promedio_jurado(j)
        if promedio_actual > mayor_promedio:
            mayor_promedio = promedio_actual
            jurado_generoso = j
    print(f"\nJurado mas generoso: Jurado #{jurado_generoso + 1} con promedio {round(mayor_promedio, 2)}/10.")

def participantes_con_puntajes_iguales():
    print("\n--- PARTICIPANTES CON PUNTUACIONES IGUALES ---\n")
    hay_iguales= False

    for i in range(5):
        p1 = puntajes [i][0]
        p2 = puntajes [i][1]
        p3 = puntajes [i][2]

        if p1 == p2 == p3:
            print(f"{participantes[i]}: Puntaje igual de {p1} en los 3 jurados.")
            hay_iguales = True

    if not hay_iguales:
        print("No hay participantes con puntajes iguales en los tres jurados.")

def buscar_participante():
    print("\n--- BUSCAR PARTICIPANTE POR NOMBRE ---\n")
    nombre_buscado = input("Ingrese el nombre del participante a buscar:").strip()
    
    encontrado = False
    for i in range(5):
        if participantes[i].lower() == nombre_buscado.lower():
            print(f"\nNOMBRE PARTICIPANTE: {participantes[i]}")
            for j in range(3):
                print(f"PUNTAJE JURADO {j + 1}: {puntajes[i][j]}")
            promedio = (puntajes[i][0] + puntajes[i][1] + puntajes[i][2]) / 3
            print(f"PUNTAJE PROMEDIO: {round(promedio, 2)}/10")
            encontrado = True
            break
    if not encontrado:
        print("No se encontro ningun participante con ese nombre.")

def mostrar_top_3():
    print("\n--- TOP 3 PARTICIPANTES ---\n")
    promedios = [0] * 5
    nombres = ["" for _ in range(5)]

    for i in range(5):
        promedio = (puntajes[i][0] + puntajes[i][1] + puntajes[i][2]) / 3
        promedios[i] = promedio
        nombres[i] = participantes[i]
    
    for i in range(4):
        for j in range(i + 1, 5):
            if promedios[j] > promedios[i]:
                promedios[i], promedios[j] = promedios[j], promedios[i]
                nombres[i], nombres[j] = nombres[j], nombres[i]
    for i in range(3):
        print(f"{i + 1}. {nombres[i]} - Promedio: {round(promedios[i], 2)}")

def mostrar_participantes_ordenados():
    print("\n--- PARTICIPANTES ORDENADOS ALFABETICAMENTE ---\n")
    nombres = participantes[:]
    notas = [fila[:]for fila in puntajes]

    for i in range(4):
        for j in range(i + 1, 5):
            if nombres[j].lower() < nombres[i].lower():
                nombres[i], nombres[j] = nombres[j], nombres[i]
                notas[i], notas[j] = notas[j], notas[i]
    for i in range(5):
        print(f"{nombres[i]}:{notas[i]}")

programa()

