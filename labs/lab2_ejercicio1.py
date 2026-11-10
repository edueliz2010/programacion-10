secuencia = []
continuar = True
while continuar:
    entrada = input("Número (0 para terminar): ")
    
    try:
        num = int(entrada)
    except:
        print("Error: debe ingresar un número entero.")
        continue

    if num == 0:
        break

    secuencia.append(num)
if len(secuencia) < 3:
    print("no es montaña.")
else:
    print("Secuencia:", secuencia)
    i = 0
    for i in range(len(secuencia) - 1):
        if secuencia[i] >= secuencia[i + 1]:
            break
    if i == 0:
        print("No es montaña")
    elif i == len(secuencia) - 1:
        print("No es montaña")
    else:
        pico = secuencia[i]

        es_montana = True
        for j in range(i, len(secuencia) - 1):
            if secuencia[j] <= secuencia[j + 1]:
                es_montana = False
                break

        if es_montana:
            print(f"Es una secuencia montaña. Pico: {pico}")
        else:
            print("No es montaña")