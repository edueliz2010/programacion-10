class Nodo:
    def __init__(self, valor, izquierdo=None, derecho=None):
        self.valor = valor
        self.izquierdo = izquierdo   
        self.derecho = derecho

arbol = Nodo("Tomás",
             Nodo("Mateo",
                  Nodo("Andrés", Nodo("Emilio")),
                  Nodo("Rosa")),
             Nodo("Lucía",
                  Nodo("Carlos")))

print(arbol.valor)                       
print(arbol.izquierdo.valor)             
print(arbol.izquierdo.derecho.valor)     
print(arbol.derecho.derecho)

def tamano(nodo):
    if nodo is None:
        return 0                                                
    return 1 + tamano(nodo.izquierdo) + tamano(nodo.derecho)    
print(tamano(arbol))

def contar_hojas(nodo):
    if nodo is None:
        return 0
    if nodo.izquierdo is None and nodo.derecho is None:
        return 1
    return contar_hojas(nodo.izquierdo) + contar_hojas(nodo.derecho)
print(contar_hojas(arbol))

def altura(nodo):
    if nodo is None:
        return -1
    return 1 + max(altura(nodo.izquierdo), altura(nodo.derecho))
print(altura(arbol))            
print(altura(arbol.derecho))

def contiene(nodo, valor):
    if nodo is None:
        return False
    if nodo.valor == valor:
        return True
    return contiene(nodo.izquierdo, valor) or contiene(nodo.derecho, valor)   


print(contiene(arbol, "Rosa"))    
print(contiene(arbol, "Pedro"))