def esta_ordenada(lista):
    if len(lista) <= 1:                                         
        return True
    if lista[0] > lista[1]:                                     
        return False
    return esta_ordenada(lista[1:])                             

numeros = [int(x) for x in input("Ingrese números separados por espacio: ").split()]
if esta_ordenada(numeros):
    print("La lista está ordenada.")
else:
    print("La lista NO está ordenada.")