q = int(input())

for _ in range(q):
    a, b, c, p = map(int, input().split())
    objetivo = p * p

    izquierda = 0
    derecha = 100000

    while izquierda < derecha:
        medio = (izquierda + derecha) // 2

        valor = a * medio + b * medio * medio + c * medio * medio * medio

        if valor >= objetivo:
            derecha = medio
        else:
            izquierda = medio + 1

    print(izquierda)