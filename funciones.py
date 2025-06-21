def promedio(p1, p2, p3):
    return (p1 + p2 + p3) / 3

def mostrar_puntuaciones(participantes, puntajes):
    print("\n--- PUNTUACIONES ---\n")
    for i in range(5):
        nombre = participantes[i]
        p1, p2, p3 = puntajes[i]
        total = p1 + p2 + p3
        prom = total / 3

        print(f"NOMBRE PARTICIPANTE: {nombre}")
        print(f"PUNTAJE JURADO 1: {p1}")
        print(f"PUNTAJE JURADO 2: {p2}")
        print(f"PUNTAJE JURADO 3: {p3}")
        print(f"PUNTAJE PROMEDIO: {round(prom, 2)}/10\n")

def mostrar_menores_a_4(participantes, puntajes):
    print("\n--- PARTICIPANTES CON PROMEDIO MENOR A 4 ---\n")
    hay_menores = False
    for i in range(5):
        p1, p2, p3 = puntajes[i]
        prom = promedio(p1, p2, p3)
        if prom < 4:
            print(f"{participantes[i]} - Promedio: {round(prom, 2)}/10")
            hay_menores = True
    if not hay_menores:
        print("No hay participantes con promedio menor a 4")

def mostrar_menores_8(participantes, puntajes):
    print("\n--- PARTICIPANTES CON PROMEDIO MENOR A 8 ---\n")
    hay_resultados = False
    for i in range(5):
        p1, p2, p3 = puntajes[i]
        prom = promedio(p1, p2, p3)
        if 4 <= prom < 8:
            print(f"{participantes[i]} - Promedio: {round(prom, 2)}/10")
            hay_resultados = True
    if not hay_resultados:
        print("No hay participantes con promedio menor a 8 y mayor o igual a 4")

def promedio_jurado(puntajes, jurado_index):
    total = 0
    for i in range(5):
        total += puntajes[i][jurado_index]
    return total / 5

def mostrar_promedio_por_jurado(puntajes):
    print("\n--- PROMEDIO POR JURADO ---\n")
    for j in range(3):
        promedio_j = promedio_jurado(puntajes, j)
        print(f"Jurado #{j + 1}: Promedio {round(promedio_j, 2)}/10")

def jurado_mas_estricto(puntajes):
    menor_promedio = promedio_jurado(puntajes, 0)
    jurado_estricto = 0
    for j in range(1, 3):
        promedio_actual = promedio_jurado(puntajes, j)
        if promedio_actual < menor_promedio:
            menor_promedio = promedio_actual
            jurado_estricto = j
    print(f"\nJurado más estricto: Jurado #{jurado_estricto + 1} con promedio {round(menor_promedio, 2)}/10")

def jurado_mas_generoso(puntajes):
    mayor_promedio = promedio_jurado(puntajes, 0)
    jurado_generoso = 0
    for j in range(1, 3):
        promedio_actual = promedio_jurado(puntajes, j)
        if promedio_actual > mayor_promedio:
            mayor_promedio = promedio_actual
            jurado_generoso = j
    print(f"\nJurado más generoso: Jurado #{jurado_generoso + 1} con promedio {round(mayor_promedio, 2)}/10.")

def participantes_con_puntajes_iguales(participantes, puntajes):
    print("\n--- PARTICIPANTES CON PUNTUACIONES IGUALES ---\n")
    hay_iguales = False
    for i in range(5):
        p1, p2, p3 = puntajes[i]
        if p1 == p2 == p3:
            print(f"{participantes[i]}: Puntaje igual de {p1} en los 3 jurados.")
            hay_iguales = True
    if not hay_iguales:
        print("No hay participantes con puntajes iguales en los tres jurados.")

def buscar_participante(participantes, puntajes):
    print("\n--- BUSCAR PARTICIPANTE POR NOMBRE ---\n")
    nombre_buscado = input("Ingrese el nombre del participante a buscar:").strip()
    encontrado = False
    for i in range(5):
        if participantes[i].lower() == nombre_buscado.lower():
            print(f"\nNOMBRE PARTICIPANTE: {participantes[i]}")
            for j in range(3):
                print(f"PUNTAJE JURADO {j + 1}: {puntajes[i][j]}")
            promedio_final = promedio(*puntajes[i])
            print(f"PUNTAJE PROMEDIO: {round(promedio_final, 2)}/10")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró ningún participante con ese nombre.")

def mostrar_top_3(participantes, puntajes):
    print("\n--- TOP 3 PARTICIPANTES ---\n")
    promedios = [0] * 5
    nombres = [""] * 5
    for i in range(5):
        promedios[i] = promedio(*puntajes[i])
        nombres[i] = participantes[i]
    for i in range(4):
        for j in range(i + 1, 5):
            if promedios[j] > promedios[i]:
                promedios[i], promedios[j] = promedios[j], promedios[i]
                nombres[i], nombres[j] = nombres[j], nombres[i]
    for i in range(3):
        print(f"{i + 1}. {nombres[i]} - Promedio: {round(promedios[i], 2)}")

def mostrar_participantes_ordenados(participantes, puntajes):
    print("\n--- PARTICIPANTES ORDENADOS ALFABÉTICAMENTE ---\n")
    nombres = participantes[:]
    notas = [fila[:] for fila in puntajes]
    for i in range(4):
        for j in range(i + 1, 5):
            if nombres[j].lower() < nombres[i].lower():
                nombres[i], nombres[j] = nombres[j], nombres[i]
                notas[i], notas[j] = notas[j], notas[i]
    for i in range(5):
        print(f"{nombres[i]}: {notas[i]}")

def mostrar_ganador(participantes, puntajes):
    print("\n--- GANADOR DE LA COMPETENCIA ---\n")

    
    mayor_prom = promedio(*puntajes[0])

    for i in range(1, 5):
        prom = promedio(*puntajes[i])
        if prom > mayor_prom:
            mayor_prom = prom

    
    cantidad = 0
    for i in range(5):
        if promedio(*puntajes[i]) == mayor_prom:
            cantidad += 1

    if cantidad == 1:
        
        for i in range(5):
            if promedio(*puntajes[i]) == mayor_prom:
                print(f"El ganador es: {participantes[i]} con promedio {round(mayor_prom, 2)}")
                break
    else:
        print("Hay un empate entre los siguientes participantes:")
        for i in range(5):
            if promedio(*puntajes[i]) == mayor_prom:
                print(f"- {participantes[i]}")
        print("Debe realizarse un desempate.")
