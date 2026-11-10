
suma = 0
contador = 0
numero = int(input("Ingrese un número entero (0 para terminar): "))

while numero != 0:

    if numero > 0 and numero % 2 == 0:
        suma += numero
        contador += 1

    numero = int(input("Ingrese un número entero (0 para terminar): "))

if contador > 0:
    promedio = suma / contador
    print("Cantidad de números pares positivos:", contador)
    print("Suma de los números:", suma)
    print("Promedio de los números:", promedio)
else:
    print("No se ingresaron números pares positivos.")