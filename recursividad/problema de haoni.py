def hanoi(n, origen, destino, auxiliar):
    if n == 1:                                          
        print(f"Mover disco de {origen} a {destino}")
        return
    hanoi(n - 1, origen, auxiliar, destino)            
    print(f"Mover disco de {origen} a {destino}")      
    hanoi(n - 1, auxiliar, destino, origen)            

n = int(input("Número de discos: "))
hanoi(n, "A", "C", "B")