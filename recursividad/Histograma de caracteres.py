def contar_letras(texto):
    frecuencia = {}
    for c in texto.lower():
        if c.isalpha():                                 
            frecuencia[c] = frecuencia.get(c, 0) + 1
    return frecuencia

def mostrar_histograma(frecuencia):
    # Ordenar de mayor a menor frecuencia
    ordenado = sorted(frecuencia.items(), key=lambda par: par[1], reverse=True)
    for letra, cantidad in ordenado:
        print(f"{letra} | {'*' * cantidad}")

texto = input("Ingrese un texto: ")
frecuencia = contar_letras(texto)
mostrar_histograma(frecuencia)