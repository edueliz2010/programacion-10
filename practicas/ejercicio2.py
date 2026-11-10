oracion = input("Ingrese una oración: ")

vocales = 0
espacios = 0

for caracter in oracion:
    
    if caracter in "AaEeIiOoUu":
        vocales += 1
    
    if caracter == " ":
        espacios += 1

total = len(oracion)

sin_espacios = total - espacios

print("Cantidad de vocales:", vocales)
print("Cantidad de espacios:", espacios)
print("Total de caracteres:", total)
print("Caracteres sin espacios:", sin_espacios)
print("Oración en mayúsculas:", oracion.upper())
print("Oración en minúsculas:", oracion.lower())