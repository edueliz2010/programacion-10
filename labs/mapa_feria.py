nodos = ["E", "C", "J", "R", "T", "S"]

mapa = {
    "E": ["C", "J"],
    "C": ["E", "R", "T"],
    "J": ["E", "S"],
    "R": ["C", "S"],
    "T": ["C", "S"],
    "S": ["J", "R", "T"]
}

nombres = {
    "E": "Entrada",
    "C": "Exposición de ciencias",
    "J": "Zona de juegos",
    "R": "Robótica",
    "T": "Talleres",
    "S": "Salida"
}


def construir_matriz(mapa, nodos):
    matriz = []

    for origen in nodos:
        fila = []

        for destino in nodos:
            if destino in mapa[origen]:
                fila.append(1)
            else:
                fila.append(0)

        matriz.append(fila)

    return matriz


def dfs_recursivo(mapa, inicio):
    visitados = set()
    recorrido = []

    def visitar(nodo):
        visitados.add(nodo)
        recorrido.append(nodo)

        for vecino in mapa[nodo]:
            if vecino not in visitados:
                visitar(vecino)

    visitar(inicio)
    return recorrido


def dfs_iterativo(mapa, inicio):
    visitados = set()
    recorrido = []
    pila = [inicio]

    while pila:
        nodo = pila.pop()

        if nodo in visitados:
            continue

        visitados.add(nodo)
        recorrido.append(nodo)

        for vecino in reversed(mapa[nodo]):
            if vecino not in visitados:
                pila.append(vecino)

    return recorrido


def mostrar_matriz(matriz, nodos):
    print("\n  " + " ".join(nodos))

    for i, fila in enumerate(matriz):
        print(nodos[i], " ".join(str(valor) for valor in fila))


def solicitar_nodo(mensaje):
    while True:
        nodo = input(mensaje).strip().upper()

        if nodo in mapa:
            return nodo

        print("Ese espacio no existe en el mapa.")


def menu():
    matriz = construir_matriz(mapa, nodos)

    while True:
        print("\n=== MAPA DE LA FERIA CIENTÍFICA ===")
        print("1. Ver conexiones de un espacio")
        print("2. Ver matriz de adyacencia")
        print("3. Recorrer con DFS recursivo")
        print("4. Recorrer con DFS iterativo")
        print("5. Consultar si hay un pasillo directo")
        print("6. Salir")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            espacio = input("Espacio: ").strip().upper()

            if espacio not in mapa:
                print("Ese espacio no existe en el mapa.")
                continue

            vecinos = ", ".join(mapa[espacio])
            print(f"{espacio} · {nombres[espacio]} se conecta con: {vecinos}")

        elif opcion == "2":
            mostrar_matriz(matriz, nodos)

        elif opcion == "3":
            inicio = solicitar_nodo("Nodo inicial: ")
            recorrido = dfs_recursivo(mapa, inicio)
            print(" -> ".join(recorrido))

        elif opcion == "4":
            inicio = solicitar_nodo("Nodo inicial: ")
            recorrido = dfs_iterativo(mapa, inicio)
            print(" -> ".join(recorrido))

        elif opcion == "5":
            origen = solicitar_nodo("Nodo de origen: ")
            destino = solicitar_nodo("Nodo de destino: ")

            i = nodos.index(origen)
            j = nodos.index(destino)

            if matriz[i][j] == 1:
                print(f"Existe un pasillo directo entre {origen} y {destino}.")
            else:
                print(f"No existe un pasillo directo entre {origen} y {destino}.")

        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta pronto!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()