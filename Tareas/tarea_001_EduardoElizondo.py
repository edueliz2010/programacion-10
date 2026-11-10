from abc import ABC, abstractmethod

class Atraccion(ABC):
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self._capacidad = capacidad
        self._visitantes_actuales = 0

    @abstractmethod
    def calcular_tiempo_ciclo(self):
        pass

    @abstractmethod
    def verificar_restriccion(self, altura):
        pass

    def subir_visitantes(self, cantidad):
        if self._visitantes_actuales + cantidad <= self._capacidad:
            self._visitantes_actuales += cantidad
            return True
        return False

    def vaciar(self):
        self._visitantes_actuales = 0

    def cupos_disponibles(self):
        return self._capacidad - self._visitantes_actuales

class MontañaRusa(Atraccion):
    def __init__(self, nombre, capacidad, altura_minima):
        super().__init__(nombre, capacidad)
        self.altura_minima = altura_minima

    def calcular_tiempo_ciclo(self):
        return 3

    def verificar_restriccion(self, altura):
        return altura >= self.altura_minima

class RuedaFortuna(Atraccion):
    def __init__(self, nombre, capacidad, altura_minima):
        super().__init__(nombre, capacidad)
        self.altura_minima = altura_minima

    def calcular_tiempo_ciclo(self):
        return 10

    def verificar_restriccion(self, altura):
        return altura >= self.altura_minima

class Carrusel(Atraccion):
    def __init__(self, nombre, capacidad):
        super().__init__(nombre, capacidad)

    def calcular_tiempo_ciclo(self):
        return 5

    def verificar_restriccion(self, altura):
        return True

class Parque:
    def __init__(self, nombre):
        self.nombre = nombre
        self._atracciones = []

    def agregar_atraccion(self, atraccion):
        self._atracciones.append(atraccion)

    def listar_atracciones(self):
        return self._atracciones.copy()

    def buscar_atraccion(self, nombre):
        for atraccion in self._atracciones:
            if atraccion.nombre == nombre:
                return atraccion
        return None

    def atracciones_disponibles(self):
        return [a for a in self._atracciones if a.cupos_disponibles() > 0]

    def tiempo_total_recorrido(self, nombres):
        total = 0
        no_encontradas = []
        for nombre in nombres:
            atraccion = self.buscar_atraccion(nombre)
            if atraccion is not None:
                total += atraccion.calcular_tiempo_ciclo()
            else:
                no_encontradas.append(nombre)
        return total, no_encontradas

parque = Parque("Parque Aventura Puriscal")
parque.agregar_atraccion(MontañaRusa("Trueno Salvaje", 8, 140))
parque.agregar_atraccion(RuedaFortuna("Vista Central", 12, 100))
parque.agregar_atraccion(Carrusel("Caballitos", 16))

while True:
    print("\n=== PARQUE AVENTURA PURISCAL ===")
    print("1. Ver todas las atracciones")
    print("2. Ver atracciones con cupo disponible")
    print("3. Subir visitantes a una atracción")
    print("4. Vaciar una atracción")
    print("5. Verificar restricción de altura")
    print("6. Calcular tiempo total de un recorrido")
    print("7. Salir")

    opcion = input("\nElija una opción: ").strip()

    if opcion == "1":
        atracciones = parque.listar_atracciones()
        for atraccion in atracciones:
            print(f"{atraccion.nombre} ({type(atraccion).__name__}): {atraccion._visitantes_actuales}/{atraccion._capacidad} visitantes, ciclo de {atraccion.calcular_tiempo_ciclo()} min")

    elif opcion == "2":
        disponibles = parque.atracciones_disponibles()
        if not disponibles:
            print("No hay atracciones con cupo disponible.")
        else:
            for atraccion in disponibles:
                print(f"{atraccion.nombre}: {atraccion.cupos_disponibles()} cupos disponibles")

    elif opcion == "3":
        nombre = input("Nombre de la atracción: ").strip()
        atraccion = parque.buscar_atraccion(nombre)
        if atraccion is None:
            print("Atracción no encontrada.")
        else:
            try:
                cantidad = int(input("Cantidad de visitantes: ").strip())
                if atraccion.subir_visitantes(cantidad):
                    print("Visitantes subidos exitosamente.")
                else:
                    print(f"No hay cupo suficiente. Cupos disponibles: {atraccion.cupos_disponibles()}")
            except ValueError:
                print("Error: la cantidad debe ser un número entero.")

    elif opcion == "4":
        nombre = input("Nombre de la atracción: ").strip()
        atraccion = parque.buscar_atraccion(nombre)
        if atraccion is None:
            print("Atracción no encontrada.")
        else:
            atraccion.vaciar()
            print("Atracción vaciada exitosamente.")

    elif opcion == "5":
        nombre = input("Nombre de la atracción: ").strip()
        atraccion = parque.buscar_atraccion(nombre)
        if atraccion is None:
            print("Atracción no encontrada.")
        else:
            try:
                altura = int(input("Estatura del visitante (cm): ").strip())
                if atraccion.verificar_restriccion(altura):
                    print("El visitante puede subir.")
                else:
                    print("El visitante no puede subir.")
            except ValueError:
                print("Error: la estatura debe ser un número entero.")

    elif opcion == "6":
        entrada = input("Nombres de atracciones separados por espacio: ").strip()
        nombres = entrada.split()
        total, no_encontradas = parque.tiempo_total_recorrido(nombres)
        print(f"Tiempo total del recorrido: {total} min")
        if no_encontradas:
            print(f"Atracciones no encontradas: {', '.join(no_encontradas)}")

    elif opcion == "7":
        print("¡Gracias por visitar el Parque Aventura Puriscal!")
        break

    else:
        print("Opción inválida. Intente de nuevo.")