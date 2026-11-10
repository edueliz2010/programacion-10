from abc import ABC, abstractmethod 

class empleado(ABC):
    def __init__(self, nombre, salario_base):
        self.nombre= nombre
        self.salario_base = salario_base
    @abstractmethod
    def calcular_salario (self):
        pass
class vendedor(empleado):
    def __init__(self, nombre, salario_base, ventas, comision):
        super().__init__(self, nombre, salario_base)
        self.ventas = ventas
        self.comision = comision

    def calcular_salario(self):
        return self.salario_base + self.ventas * (self.comision / 100 + 1) 

class gerente(empleado):
    def __init__(self, nombre, salario_base, bono_fijo):
        super().__init__(nombre, salario_base)
        self.bono_fijo = bono_fijo
    
    def calcular_salario(self):
        return self.salario_base + self.bono_fijo

def nomina_total (empleados):
    total = 0
    for empleado in empleados:
        total += empleado.calcular_salario()
        return total

lista_empleados = []