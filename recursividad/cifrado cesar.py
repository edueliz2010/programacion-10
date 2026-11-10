def desplazar(caracter, k):
    if caracter.islower():
        return chr((ord(caracter) - ord('a') + k) % 26 + ord('a'))  
    if caracter.isupper():
        return chr((ord(caracter) - ord('A') + k) % 26 + ord('A'))  
    return caracter                                                   

def cifrar(mensaje, k):
    resultado = ""
    for c in mensaje:
        resultado += desplazar(c, k)
    return resultado

def descifrar(mensaje, k):
    return cifrar(mensaje, -k)                                       

mensaje = input("Mensaje: ")
k = int(input("Desplazamiento: "))
cifrado = cifrar(mensaje, k)
print(f"Cifrado:    {cifrado}")
print(f"Descifrado: {descifrar(cifrado, k)}")