from functools import reduce

playlist = []

while True:
    print("\n=== REPRODUCTOR DE MÚSICA ===")
    print("1. Registrar canción")
    print("2. Ver duración total de la playlist")
    print("3. Ver playlist en modo radio (máximo 3 minutos por canción)")
    print("4. Ver solo las canciones cortas")
    print("5. Ver si alguna canción supera las 1000 reproducciones")
    print("6. Ver la canción más reproducida")
    print("7. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        titulo = input("Título: ")

        try:
            duracion = float(input("Duración (minutos): "))
        except ValueError:
            print("La duración debe ser numérica.")
            continue

        if duracion <= 0:
            print("La duración debe ser mayor que 0.")
            continue

        try:
            reproducciones = int(input("Reproducciones: "))
        except ValueError:
            print("Las reproducciones deben ser numéricas.")
            continue

        if reproducciones < 0:
            print("Las reproducciones no pueden ser negativas.")
            continue

        playlist.append({
            "titulo": titulo,
            "duracion": duracion,
            "reproducciones": reproducciones
        })

        print(f"Canción '{titulo}' registrada.")

    elif opcion == "2":
        if not playlist:
            print("La playlist está vacía.")
        else:
            duracion_total = reduce(
                lambda total, cancion: total + cancion["duracion"],
                playlist,
                0
            )
            print(f"Duración total: {duracion_total} minutos")

    elif opcion == "3":
        if not playlist:
            print("La playlist está vacía.")
        else:
            playlist_radio = map(
                lambda cancion: {
                    "titulo": cancion["titulo"],
                    "duracion": min(cancion["duracion"], 3),
                    "reproducciones": cancion["reproducciones"]
                },
                playlist
            )

            print("\n=== MODO RADIO ===")
            for cancion in playlist_radio:
                print(
                    f"{cancion['titulo']} - "
                    f"{cancion['duracion']} minutos - "
                    f"{cancion['reproducciones']} reproducciones"
                )

    elif opcion == "4":
        if not playlist:
            print("La playlist está vacía.")
        else:
            canciones_cortas = filter(
                lambda cancion: cancion["duracion"] <= 3,
                playlist
            )

            print("\n=== CANCIONES CORTAS ===")
            for cancion in canciones_cortas:
                print(
                    f"{cancion['titulo']} - "
                    f"{cancion['duracion']} minutos - "
                    f"{cancion['reproducciones']} reproducciones"
                )

    elif opcion == "5":
        if not playlist:
            print("La playlist está vacía.")
        else:
            hay_mas_de_1000 = any(
                cancion["reproducciones"] > 1000
                for cancion in playlist
            )

            if hay_mas_de_1000:
                print("Sí, hay una canción que supera las 1000 reproducciones.")
            else:
                print("No, ninguna canción supera las 1000 reproducciones.")

    elif opcion == "6":
        if not playlist:
            print("La playlist está vacía.")
        else:
            mas_reproducida = max(
                playlist,
                key=lambda cancion: cancion["reproducciones"]
            )

            print(
                f"La canción más reproducida es "
                f"'{mas_reproducida['titulo']}' con "
                f"{mas_reproducida['reproducciones']} reproducciones."
            )

    elif opcion == "7":
        print("Saliendo del reproductor...")
        break

    else:
        print("Opción inválida. Intente nuevamente.")