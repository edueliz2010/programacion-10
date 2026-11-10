def calcular_puntos(matriz, i):
    puntos = 0
    for j in range(len(matriz)):
        if i == j:                  
            continue
        if matriz[i][j] == 1:
            puntos += 3
        elif matriz[i][j] == 0:
            puntos += 1
    return puntos

def mostrar_tabla(equipos, matriz):
    resultados = []
    for i in range(len(equipos)):
        pts = calcular_puntos(matriz, i)
        resultados.append((equipos[i], pts))

    resultados.sort(key=lambda par: par[1], reverse=True)

    print(f"\n{'Equipo':<15} {'Puntos':>6}")
    print("-" * 22)
    for nombre, pts in resultados:
        print(f"{nombre:<15} {pts:>6}")

equipos = ["Tigres", "Halcones", "Lobos", "Águilas"]

# Resultados: fila i vs columna j (1=gana i, 0=empate, -1=pierde i)
matriz = [
    [ 0,  1,  1, -1],   # Tigres
    [-1,  0,  0,  1],   # Halcones
    [-1,  0,  0,  1],   # Lobos
    [ 1, -1, -1,  0],   # Águilas
]

mostrar_tabla(equipos, matriz)