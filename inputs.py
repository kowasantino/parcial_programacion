participantes = [""] * 5
puntajes = [[0, 0, 0] for _ in range(5)]

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

def puntuacion_valida(p):
    return 1 <= int(p) <= 10

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