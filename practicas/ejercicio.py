
class estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self._nota = 0

    def asignar_nota(self, valor):
        if valor < 0 or valor > 100:
            print("Nota no valida")
            return
        self._nota = valor

    def aprobado(self):
        return self._nota >= 70

est = estudiante("Camila")
est.asignar_nota(85)
print(est.aprobado())    

est.asignar_nota(150)    
print(est._nota)