matriz = []

for _ in range(3):
    matriz.append(list(map(int, input().split())))

if matriz[0][0] == matriz[0][2] and matriz[2][2] == matriz[2][0]:
    print("Tesoro encontrado")
else:
    print("Sigue buscando")