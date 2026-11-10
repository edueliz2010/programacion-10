
from collections import deque

red = {
    "Santiago": ["Mercedes Sur", "Barbacoas", "Candelarita"],
    "Mercedes Sur": ["Santiago", "San Rafael"],
    "Barbacoas": ["Santiago", "Grifo Alto"],
    "San Rafael": ["Mercedes Sur", "Grifo Alto"],
    "Grifo Alto": ["Barbacoas", "San Rafael"],
    "Candelarita": ["Santiago"],
    "Desamparaditos": ["Chires"],
    "Chires": ["Desamparaditos"],
    "Zapatón": []
}

obras = {
    "Estudio": ["Permisos", "Materiales"],
    "Permisos": ["Excavación"],
    "Materiales": ["Alcantarillado", "Asfaltado"],
    "Excavación": ["Alcantarillado"],
    "Alcantarillado": ["Asfaltado"],
    "Asfaltado": ["Señalización"],
    "Señalización": []
}


def normalizar(nombre):
    return nombre.strip().title()


def mostrar_nombres(nombres):
    return " -> ".join(nombres)


def dfs_iterativo(grafo, inicio):
    pila = [inicio]
    visitados = []

    while pila:
        actual = pila.pop()

        if actual not in visitados:
            visitados.append(actual)

            for vecino in reversed(grafo[actual]):
                if vecino not in visitados:
                    pila.append(vecino)

    return visitados


def ruta_mas_corta(grafo, inicio, destino):
    cola = deque([inicio])
    padres = {inicio: None}

    while cola:
        actual = cola.popleft()

        if actual == destino:
            break

        for vecino in grafo[actual]:
            if vecino not in padres:
                padres[vecino] = actual
                cola.append(vecino)

    if destino not in padres:
        return None

    ruta = []
    actual = destino

    while actual is not None:
        ruta.append(actual)
        actual = padres[actual]

    ruta.reverse()
    return ruta


def contar_componentes(grafo):
    visitados = set()
    componentes = {}
    numero_componente = 0

    for inicio in grafo:
        if inicio not in visitados:
            numero_componente += 1
            pila = [inicio]

            while pila:
                actual = pila.pop()

                if actual not in visitados:
                    visitados.add(actual)
                    componentes[actual] = numero_componente

                    for vecino in grafo[actual]:
                        if vecino not in visitados:
                            pila.append(vecino)

    return numero_componente, componentes


def tiene_ciclo(grafo):
    visitados = set()

    def dfs(actual, padre):
        visitados.add(actual)

        for vecino in grafo[actual]:
            if vecino not in visitados:
                if dfs(vecino, actual):
                    return True
            elif vecino != padre:
                return True

        return False

    for comunidad in grafo:
        if comunidad not in visitados:
            if dfs(comunidad, None):
                return True

    return False


def orden_topologico(grafo):
    grados_entrada = {obra: 0 for obra in grafo}

    for dependientes in grafo.values():
        for dependiente in dependientes:
            grados_entrada[dependiente] += 1

    cola = deque(
        obra for obra in grafo
        if grados_entrada[obra] == 0
    )

    orden = []

    while cola:
        actual = cola.popleft()
        orden.append(actual)

        for dependiente in grafo[actual]:
            grados_entrada[dependiente] -= 1

            if grados_entrada[dependiente] == 0:
                cola.append(dependiente)

    return orden


def ver_red():
    print("\nRed de caminos de Puriscal")
    total_grados = 0

    for comunidad, vecinos in red.items():
        grado = len(vecinos)
        total_grados += grado

        if vecinos:
            lista_vecinos = ", ".join(vecinos)
        else:
            lista_vecinos = "sin caminos"

        print(f"{comunidad} (grado {grado}): {lista_vecinos}")

    print(f"Total de caminos: {total_grados // 2}")


def agregar_camino():
    primera = normalizar(input("Primera comunidad: "))
    segunda = normalizar(input("Segunda comunidad: "))

    if primera not in red:
        print(f"No existe la comunidad '{primera}'.")
        return

    if segunda not in red:
        print(f"No existe la comunidad '{segunda}'.")
        return

    if primera == segunda:
        print("Una comunidad no puede conectarse consigo misma.")
        return

    if segunda in red[primera]:
        print(f"Ya existe un camino entre {primera} y {segunda}.")
        return

    red[primera].append(segunda)
    red[segunda].append(primera)

    print(f"Camino agregado entre {primera} y {segunda}.")


def mostrar_alcanzables():
    inicio = normalizar(input("Comunidad de inicio: "))

    if inicio not in red:
        print(f"No existe la comunidad '{inicio}'.")
        return

    alcanzables = dfs_iterativo(red, inicio)

    print(
        f"Comunidades alcanzables desde {inicio}: "
        f"{len(alcanzables)}"
    )
    print(mostrar_nombres(alcanzables))


def mostrar_ruta():
    inicio = normalizar(input("Comunidad de origen: "))
    destino = normalizar(input("Comunidad de destino: "))

    if inicio not in red:
        print(f"No existe la comunidad '{inicio}'.")
        return

    if destino not in red:
        print(f"No existe la comunidad '{destino}'.")
        return

    if inicio == destino:
        print("El origen y el destino no pueden ser iguales.")
        return

    ruta = ruta_mas_corta(red, inicio, destino)

    if ruta is None:
        print(f"No existe una ruta entre {inicio} y {destino}.")
    else:
        print(f"Ruta con menos tramos: {mostrar_nombres(ruta)}")
        print(f"Cantidad de tramos: {len(ruta) - 1}")


def mostrar_componentes():
    cantidad, componentes = contar_componentes(red)

    print()

    for numero in range(1, cantidad + 1):
        comunidades = [
            comunidad
            for comunidad in red
            if componentes[comunidad] == numero
        ]

        print(f"Componente {numero}: {', '.join(comunidades)}")

    if cantidad == 1:
        print("Todas las comunidades están comunicadas entre sí.")
    else:
        print(
            f"La red tiene {cantidad} componentes conexas "
            "y no todas las comunidades están comunicadas."
        )


def detectar_ciclos():
    ciclo_dfs = tiene_ciclo(red)
    cantidad_componentes, _ = contar_componentes(red)

    total_caminos = sum(
        len(vecinos) for vecinos in red.values()
    ) // 2

    cantidad_comunidades = len(red)
    caminos_sin_ciclos = cantidad_comunidades - cantidad_componentes

    ciclo_conteo = total_caminos > caminos_sin_ciclos

    if ciclo_dfs:
        print("Búsqueda con DFS: la red tiene al menos un camino circular.")
    else:
        print("Búsqueda con DFS: la red no tiene caminos circulares.")

    print(
        f"Comprobación por conteo: {total_caminos} caminos frente a "
        f"{caminos_sin_ciclos} permitidos sin ciclos "
        f"({cantidad_comunidades} comunidades - "
        f"{cantidad_componentes} componentes)."
    )

    if ciclo_conteo:
        print("La comprobación por conteo indica que hay ciclos.")
    else:
        print("La comprobación por conteo indica que no hay ciclos.")

    if ciclo_dfs == ciclo_conteo:
        print("Los dos métodos coinciden.")
    else:
        print("Los dos métodos no coinciden.")


def mostrar_orden_obras():
    orden = orden_topologico(obras)

    if len(orden) == len(obras):
        print("\nOrden de ejecución de las obras:")
        print(mostrar_nombres(orden))
    else:
        print("\nHay un ciclo de prerrequisitos: no existe un orden válido.")

        ejecutables = set(orden)

        bloqueadas = [
            obra for obra in obras
            if obra not in ejecutables
        ]

        print(f"Obras bloqueadas: {', '.join(bloqueadas)}")


def agregar_prerrequisito():
    previa = normalizar(input("Obra previa: "))
    dependiente = normalizar(input("Obra que depende de ella: "))

    if previa not in obras:
        print(f"No existe la obra '{previa}'.")
        return

    if dependiente not in obras:
        print(f"No existe la obra '{dependiente}'.")
        return

    if previa == dependiente:
        print("Una obra no puede depender de sí misma.")
        return

    if dependiente in obras[previa]:
        print(f"Ya existe esa dependencia entre {previa} y {dependiente}.")
        return

    obras[previa].append(dependiente)

    print(
        f"Prerrequisito agregado: {previa} debe terminar "
        f"antes de {dependiente}."
    )


while True:
    print("""
=== RED VIAL DE PURISCAL ===
1. Ver la red de caminos
2. Agregar un camino
3. Comunidades alcanzables desde una comunidad
4. Ruta con menos tramos entre dos comunidades
5. Componentes conexas de la red
6. Detectar caminos circulares
7. Orden de ejecución de las obras
8. Agregar un prerrequisito entre obras
9. Salir
""")

    try:
        opcion = int(input("Elija una opción: "))
    except ValueError:
        print("Opción inválida. Debe digitar un número del 1 al 9.")
        continue

    if opcion == 1:
        ver_red()
    elif opcion == 2:
        agregar_camino()
    elif opcion == 3:
        mostrar_alcanzables()
    elif opcion == 4:
        mostrar_ruta()
    elif opcion == 5:
        mostrar_componentes()
    elif opcion == 6:
        detectar_ciclos()
    elif opcion == 7:
        mostrar_orden_obras()
    elif opcion == 8:
        agregar_prerrequisito()
    elif opcion == 9:
        print("Gracias por utilizar el programa. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Debe digitar un número del 1 al 9.")
