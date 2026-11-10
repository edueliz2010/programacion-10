def collatz(n):
    if n == 1:                          
        return 0
    if n % 2 == 0:                      
        return 1 + collatz(n // 2)
    return 1 + collatz(3 * n + 1)       

n = int(input("Ingrese un entero positivo: "))
print(f"Pasos para llegar a 1 desde {n}: {collatz(n)}")