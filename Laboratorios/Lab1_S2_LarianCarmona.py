from functools import reduce


playlist = []

def menu():
    print("=== REPRODUCTOR DE MUSICA ===")
    print("1. Registrar cancion")
    print("2. Ver duracion total de la playlist")
    print("3. Ver playlist en modo radio (maximo 3 minutos por cancion)")
    print("4. Ver solo las canciones cortas")
    print("5. Ver si alguna cancion supera las 1000 reproducciones")
    print("6. Ver la cancion mas reproducida")
    print("7. Salir")
    
    
def registrar_cancion():     
    titulo = input("Titulo: ")
    try:
        duracion = float(input("Duracion (minutos): "))
    except ValueError:
        print("La duracion debe ser un numero.") 
        return 
    if duracion <= 0:
        print("La duracion debe ser mayor que 0.")
        return
    try:
        reproducciones = int(input("Reproducciones: "))
    except ValueError:
        print("El numero de reproducciones debe ser un numero entero.")
        return
    if reproducciones < 0:
        print("El numero de reproducciones no puede ser negativo.")
        return
    
    playlist.append({"Titulo": titulo, "Duracion": duracion, "Reproducciones": reproducciones})
    print(f"Cancion '{titulo}' registrada.")


def duracion_total():
    if not playlist:
        print("No hay canciones registradas.")
        return
    total = reduce(lambda acumulado, cancion: acumulado + cancion["Duracion"], playlist, 0)
    print(f"Duracion total de la playlist: {total} minutos")

def modo_radio():
   version_radio = list(map(lambda cancion: {"Titulo": cancion["Titulo"], "Duracion": min(cancion["Duracion"], 3), "Reproducciones": cancion["Reproducciones"]}, playlist))
   print("--- Playlist en modo radio ---") 
   for cancion in version_radio:
       print(f"{cancion['Titulo']}: {cancion['Duracion']} min")
    
    
def canciones_cortas():
    ccortas = list(filter(lambda cancion: cancion["Duracion"] <= 3, playlist))
    print(" --- Canciones cortas ---")
    for cancion in ccortas:
        print(f"{cancion['Titulo']}: {cancion['Duracion']} min")

def mas_de_1000():
   T_F = any(cancion["Reproducciones"] > 1000 for cancion in playlist)
   print(f"Alguna cancion supera las 1000 reproducciones? {T_F}")


def mas_reproducida():
    if not playlist:
        print("No hay canciones registradas.")
        return
    cancion_mas_reproducida = max(playlist, key=lambda cancion: cancion["Reproducciones"])
    print(f"Cancion mas reproducida:{cancion_mas_reproducida['Titulo']} ({cancion_mas_reproducida['Reproducciones']} reproducciones)")


while True:
    menu()
    opcion = input("Opcion: ")
    if opcion == "1":
        registrar_cancion()
    elif opcion == "2":
        duracion_total()
    elif opcion == "3":
        modo_radio()
    elif opcion == "4":
        canciones_cortas()
    elif opcion == "5":
        mas_de_1000()
    elif opcion == "6":
        mas_reproducida()
    elif opcion == "7":
        break
    else:
        print("Opcion invalida, intente de nuevo.")

