from abc import ABC, abstractmethod

class empleado(ABC):
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    @abstractmethod
    def calcular_salario(self):
        pass

class vendedor(empleado):
    def __init__(self, nombre, salario_base, ventas, comision):
        super().__init__(nombre, salario_base)
        self.ventas = ventas
        self.comision = comision

    def calcular_salario(self):
        return self.salario_base + self.ventas * self.comision

class gerente(empleado):
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.bono = bono

    def calcular_salario(self):
        return self.salario_base + self.bono

def nomina_total(empleados):
    total = 0
    for empleado in empleados:
        total += empleado.calcular_salario()
    return total

empleados = []

for empleado in empleados:
    print(f"{empleado.nombre}: ${empleado.calcular_salario():,;0f}")

print(f"nomina total: ${nomina_total(empleados):,.0f}")