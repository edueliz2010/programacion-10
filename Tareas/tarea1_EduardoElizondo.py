# Listas paralelas predefinidas
candidatos = ["Valeria", "Andrés", "Camila", "Diego", "Fernanda"]
votos = [45, 38, 52, 29, 41]

print("=== Sistema de Votación Estudiantil ===")
print("1. Consultar votos de un candidato")
print("2. Registrar votos a un candidato")
print("3. Ver estadísticas generales")
print("4. Ver candidato ganador")

opcion = input("\nElija una opción: ").strip()

# Opción 1
if opcion == "1":
    nombre = input("Digite el nombre del candidato: ").strip().title()
    
    if nombre in candidatos:
        posicion = candidatos.index(nombre)
        cantidad_votos = votos[posicion]
        
        print(f"\nCandidato: {nombre}")
        print(f"Votos: {cantidad_votos}")
        
        if cantidad_votos >= 50:
            print("Clasificación: Candidato destacado")
        elif 35 <= cantidad_votos <= 49:
            print("Clasificación: Candidato competitivo")
        else:
            print("Clasificación: Candidato con pocos votos")
    else:
        print("El candidato no existe.")

# Opción 2
elif opcion == "2":
    nombre = input("Digite el nombre del candidato: ").strip().title()
    
    if nombre in candidatos:
        posicion = candidatos.index(nombre)
        
        try:
            nuevos_votos = int(input("Digite la cantidad de votos a agregar: ").strip())
            
            if nuevos_votos > 0:
                votos[posicion] += nuevos_votos
                print(f"Votos actualizados correctamente.")
                print(f"Nuevo total para {nombre}: {votos[posicion]}")
            else:
                print("Error: La cantidad de votos debe ser mayor a cero.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
    else:
        print("El candidato no existe.")

# Opción 3
elif opcion == "3":
    total_votos = sum(votos)
    promedio = total_votos / len(votos)
    max_votos = max(votos)
    min_votos = min(votos)
    
    candidato_max = candidatos[votos.index(max_votos)]
    candidato_min = candidatos[votos.index(min_votos)]
    
    print(f"\nTotal de votos registrados: {total_votos}")
    print(f"Promedio de votos por candidato: {promedio:.2f}")
    print(f"Candidato con más votos: {candidato_max} ({max_votos})")
    print(f"Candidato con menos votos: {candidato_min} ({min_votos})")

# Opción 4
elif opcion == "4":
    max_votos = max(votos)
    ganadores = []
    
    for i in range(len(votos)):
        if votos[i] == max_votos:
            ganadores.append(candidatos[i])
    
    if len(ganadores) == 1:
        print(f"\nGanador: {ganadores[0]} con {max_votos} votos.")
    else:
        print(f"\nHay un empate entre: {', '.join(ganadores)} con {max_votos} votos.")

# Opción inválida
else:
    print("Opción inválida. Intente nuevamente.")