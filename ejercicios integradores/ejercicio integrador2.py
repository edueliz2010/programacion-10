
class personaje():

    def __init__(self, nombre):
        self.nombre = nombre
        self._vida = 100

    def obtener_vida(self):
        return self._vida

    def dañar(self, cantidad):
        self._vida -= cantidad
        if self._vida < 0:
            self._vida = 0

    def curar(self, cantidad):
        self._vida += cantidad
        if self._vida > 100:
            self._vida = 100

    def atacar(self, objetivo):
        objetivo.dañar(10)
        print(f"{self.nombre} ataca a {objetivo.nombre}.")

    def info(self):
        return f"{self.nombre} | vida: {self.obtener_vida}"

class guerrero(personaje):

    def __init__(self, nombre, fuerza):
        super().__init__(nombre)
        self.fuerza = fuerza

    def atacar(self, objetivo):
        objetivo.dañar(10 + self.fuerza)
        print(f"{self.nombre} ataca a {objetivo.nombre} con fuerza extra.")

    def info(self):
        return super().info() + f" | fuerza: {self.fuerza}"

class mago(personaje):

    def __init__(self, nombre):
        super().__init__(nombre)
        self._mana = 50

    def atacar(self, objetivo):
        if self._mana < 20:
            print(f"{self.nombre} sin mana.")
            return

        self._mana -= 20
        objetivo.dañar(25)
        print(f"{self.nombre} castea spell en {objetivo.nombre}.")

    def info(self):
        return super().info() + f" | mana: {self._mana}"

class elfo(personaje):
    def __init__(self, nombre, flecha):
        super().__init__(nombre)
        self.flecha = flecha

    def atacar(self, objetivo):
        objetivo.dañar(10 + self.flecha)
        print(f"{self.nombre} acribillo a {objetivo.nombre}.")

    def info(self):
        return super().info() + f" | daño de flecha: {self.flecha}"

def buscar_personaje(personajes, nombre):
    for personaje in personajes:
        if personaje.nombre == nombre:
            return personaje
        return  None

def registrar_personaje(personajes):
    nombre = input("nombre: ").strip()

    if buscar_personaje(personajes, nombre) is not None:
        print(f"personaje {nombre} ya registrado")
        return

    tipo = input("indique su gremio").strip().lower()

    if tipo == "guerreo":
        fuerza = int(input("fuerza: "))
        personaje.append(guerrero(nombre, fuerza))
    elif tipo == "mago":
        personaje.append(mago(nombre))
    elif tipo == "elfo":
        flecha = int(input("ingrese el daño de la flecha: "))
        personaje.append(elfo(nombre, flecha))
    else:
        print("gremio no encontrado")
        return

    print(f"personaje '{nombre}' registrado al gremio de {tipo}.")

def atacar_personaje(personajes):
    nombre_atacante = input("atacante: ").strip()
    nombre_objetivo = input("objetivo: ").strip()

    atacante = buscar_personaje(personajes, nombre_atacante)
    objetivo = buscar_personaje(personajes, nombre_objetivo)

    if atacante is None or objetivo is None:
        print("uno de los personajes no esta registrado.")
        return

    atacante.atacar(objetivo)

def curar_personaje(personajes):
    nombre = input("personaje a curar: ").strip()
    personaje = buscar_personaje(personaje, nombre)

    if personaje is None:
        print("personaje no registrado")
        return

    try:
        cantidad = int(input("cantidad a curar: "))
    except ValueError:
        print("La cantidad debe ser numerica")
        return

    personaje.curar(cantidad)
    print(f"'{nombre}' fue curado. Vida actual: {personaje.obtener_vida()}")

def ver_personajes(personajes):
    if not personajes:
        print("No hay personajes registrados.")
        return

    print("\n--- Personajes de la arena ---")
    for personaje in personajes:
        print(personaje.info())