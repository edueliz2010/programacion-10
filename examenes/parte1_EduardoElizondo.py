def agregar_ruta(grafo, a, b):
    if a not in grafo:
        grafo[a] = []
    if b not in grafo:
        grafo[b] = []
    grafo[a].append(b)
    grafo[b].append(a)

def rutas_directas(grafo, ciudad):
    if ciudad in grafo:
        return sorted(grafo[ciudad])
    return []

def se_puede_llegar(grafo, origen, destino, visitados=None):
    if visitados is None:
        visitados = set()
    if origen == destino:
        return True
    visitados.add(origen)
    for vecino in grafo.get(origen, []):
        if vecino not in visitados:
            if se_puede_llegar(grafo, vecino, destino, visitados):
                return True
    return False

def minimo_trayecto(grafo, origen, destino):
    from collections import deque
    queue = deque([(origen, [origen])])
    visitados = set()
    while queue:
        actual, camino = queue.popleft()
        if actual == destino:
            return camino
        visitados.add(actual)
        for vecino in grafo.get(actual, []):
            if vecino not in visitados:
                queue.append((vecino, camino + [vecino]))
    return None

def contar_zonas(grafo):
    visitados = set()
    zonas = 0
    for ciudad in grafo:
        if ciudad not in visitados:
            zonas += 1
            dfs(grafo, ciudad, visitados)
    return zonas

def dfs(grafo, ciudad, visitados):
    visitados.add(ciudad)
    for vecino in grafo.get(ciudad, []):
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)

grafo = {}

while True:
    print("===Red de buses===")
    print("1.consultar rutas directas")
    print("2.verificar si se puede llegar")
    print("3.calcular el trayecto minimo")
    print("4.contar zonas")
    print("5.agregar ruta")
    print("6.salir")
    input_opcion = input("Ingrese una opcion: ")

    if input_opcion == "1":
        ciudad = input("Ingrese la ciudad: ")
        rutas = rutas_directas(grafo, ciudad)
        print("Rutas directas:", rutas)

    elif input_opcion == "2":
        origen = input("Ingrese la ciudad de origen: ")
        destino = input("Ingrese la ciudad de destino: ")
        if se_puede_llegar(grafo, origen, destino):
            print("Si se puede llegar")
        else:
            print("No se puede llegar")

    elif input_opcion == "3":
        origen = input("Ingrese la ciudad de origen: ")
        destino = input("Ingrese la ciudad de destino: ")
        trayecto = minimo_trayecto(grafo, origen, destino)
        if trayecto:
            print("Trayecto minimo:", len(trayecto) - 1)
        else:
            print("No hay trayecto disponible")
    
    elif input_opcion == "4":
        zonas = contar_zonas(grafo)
        print("Zonas sin conexión:", zonas)
    
    elif input_opcion == "5":
        origen = input("Ingrese la primera ciudad: ")
        destino = input("Ingrese la segunda ciudad: ")
        agregar_ruta(grafo, origen, destino)
        print("Ruta agregada")

    elif input_opcion == "6":
        break
    
    else:
        print("Opción no válida")