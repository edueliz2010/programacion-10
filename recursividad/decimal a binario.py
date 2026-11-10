def a_binario(n):
    if n == 0:                                  
        return "0"
    if n == 1:                                  
        return "1"
    return a_binario(n // 2) + str(n % 2)      

n = int(input("Ingrese un entero positivo: "))
print(f"{n} en binario es: {a_binario(n)}")