# 1. Variables iniciales
# Al inicio del programa, actual es la suma del subgrupo que se está evaluando en ese momento,
# mientras que mejor guarda la mayor suma encontrada hasta ahora.
#
# Se inicializan con numeros[0] y no con 0 porque el algoritmo debe funcionar incluso si todos
# los numeros son negativos. Si empezara en 0, el resultado estaría mal, ya que daría 0 en vez
# del número negativo más grande.

# 2. La decisión clave
# En esta parte el algoritmo decide si seguir sumando o empezar desde el número actual.
#
# Si actual es negativo, se descarta porque afecta la suma total. Entonces es mejor empezar
# desde el numero actual, ya que sumar un negativo hace que el resultado sea menor.
#
# Ejemplo: si actual = -3 y el siguiente número es 5:
# -3 + 5 = 2, pero empezar desde 5 da 5, entonces es mejor empezar desde 5.

# 3. Caso extremo
# Para la lista [-5, -2, -8, -1, -4], el resultado es -1.
#
# Esto pasa porque todos los números son negativos, entonces el algoritmo escoge el número
# más grande (el menos negativo). No es 0 porque el problema pide usar al menos un elemento.

# 4. Identificación del ciclo
# Se usa un ciclo for para recorrer la lista.
#
# Esto tiene sentido porque ya se sabe cuantos elementos hay y solo se recorren uno por uno.
# Es más facil que usar un while, ya que no hay que controlar el índice manualmente.