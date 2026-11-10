def crear_bus(filas, columnas):
    bus = [[0] * columnas for _ in range(filas)]
    return bus

def mostrar_bus(bus):
    print("         Col 1   Col 2   Col 3   Col 4")
    for i in range(len(bus)):
        print(f"Fila {i+1} |", end="")
        for j in range(len(bus[0])):
            if bus[i][j] == 0:
                print("  [ ]  |", end="")
            else:
                print("  [X]  |", end="")
        print()  

def reservar_asiento(bus, fila, columna):
    if bus[fila-1][columna-1] == 1:
        return False
    bus[fila-1][columna-1] = 1
    return True

def cancelar_reserva(bus, fila, columna):
    if bus[fila-1][columna-1] == 0:
        return False
    bus[fila-1][columna-1] = 0
    return True

def disponibles_por_fila(bus):
    total = 0
    print("Disponibilidad por fila:")
    for i in range(len(bus)):
        libres = 0
        for asiento in bus[i]:
            if asiento == 0:
                libres += 1
        print(f"Fila {i+1}: {libres} asientos libres")
        total += libres
    print(f"Total general de asientos disponibles: {total}")
bus = crear_bus(5, 4)
bus[0][1] = 1  # fila 1 col 2
bus[1][0] = 1  # fila 2 col 1
bus[1][3] = 1  # fila 2 col 4
bus[2][2] = 1  # fila 3 col 3
bus[3][1] = 1  # fila 4 col 2
bus[4][0] = 1  # fila 5 col 1
bus[4][2] = 1  # fila 5 col 3

continuar = True
while continuar:
    print("=== Servicio de Autobuses Puriscal ===")
    print("1. Ver estado del bus")
    print("2. Reservar un asiento")
    print("3. Cancelar una reserva")
    print("4. Ver disponibilidad por fila")
    print("5. Salir")
    
    try:
        opcion = int(input("Elija una opción: "))
    except ValueError:
        print("Opción inválida. Por favor ingrese un número.")
        continue
    
    if opcion == 1:
        mostrar_bus(bus)
    elif opcion == 2:
        print("Ingrese los datos para reservar")
        try:
            fila = int(input("Fila (1-5): "))
            columna = int(input("Columna (1-4): "))
            if fila < 1 or fila > 5 or columna < 1 or columna > 4:
                print("Error: Posición fuera de rango.")
                continue
            if reservar_asiento(bus, fila, columna):
                print(f"¡Reserva exitosa en Fila {fila}, Columna {columna}!")
            else:
                print("Lo siento, el asiento ya estaba ocupado.")
        except ValueError:
            print("Error: Ingrese solo números enteros.")
    elif opcion == 3:
        try:
            fila = int(input("Fila (1-5): "))
            columna = int(input("Columna (1-4): "))
            if not (1 <= fila <= 5 and 1 <= columna <= 4):
                print("Error: La posición no es válida.")
                continue
            if cancelar_reserva(bus, fila, columna):
                print(f"Cancelación exitosa en Fila {fila} Columna {columna}.")
            else:
                print("El asiento ya estaba disponible.")
        except ValueError:
            print("Error: Debes ingresar números.")
    elif opcion == 4:
        disponibles_por_fila(bus)
    elif opcion == 5:
        print("Gracias por usar el sistema de Autobuses Puriscal. ¡Hasta la próxima!")
        continuar = False
    else:
        print("Opción no válida, elige entre 1 y 5.")