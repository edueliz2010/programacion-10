class Producto:
    total_productos = 0

    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        Producto.total_productos += 1

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor

    @staticmethod
    def es_codigo_valido(codigo):
        return len(codigo) == 6 and codigo[0].isalpha() and codigo[1:].isdigit()

    @classmethod
    def cantidad_registrada(cls):
        return cls.total_productos

    def __str__(self):
        return f"{self.codigo} | {self.nombre} | ₡{self.precio:,.2f} | {self.cantidad} unid."

    def __eq__(self, otro):
        return self.precio == otro.precio

    def __lt__(self, otro):
        return self.precio < otro.precio

    def __add__(self, otro):
        if self.codigo != otro.codigo:
            raise ValueError("Solo se pueden fusionar productos con el mismo código")
        return Producto(self.codigo, self.nombre, self.precio, self.cantidad + otro.cantidad)


def buscar_producto(inventario, codigo):
    for producto in inventario:
        if producto.codigo == codigo:
            return producto
    return None


def registrar_producto(inventario):
    codigo = input("Código (letra + 5 dígitos): ").strip().upper()

    if not Producto.es_codigo_valido(codigo):
        print(f"Código inválido: '{codigo}'.")
        return
    if buscar_producto(inventario, codigo) is not None:
        print(f"El código '{codigo}' ya está registrado.")
        return

    nombre = input("Nombre: ").strip()

    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("Precio y cantidad deben ser numéricos.")
        return

    try:
        inventario.append(Producto(codigo, nombre, precio, cantidad))  
    except ValueError as error:
        print(f"Error: {error}")
        return

    print(f"Producto '{nombre}' registrado.")


def ver_inventario_ordenado(inventario):
    if not inventario:
        print("No hay productos registrados.")
        return

    print("\n--- Inventario ordenado por precio ---")
    for producto in sorted(inventario):     
        print(producto)


def ver_extremos(inventario):
    if not inventario:
        print("No hay productos registrados.")
        return

    print(f"Más barato: {min(inventario)}")  
    print(f"Más caro:   {max(inventario)}")


def total_inventario(inventario):
    total = sum(p.precio * p.cantidad for p in inventario)
    print(f"Total del inventario: ₡{total:,.2f}")


inventario = []

while True:
    print("\n=== INVENTARIO ===")
    print("1. Registrar producto")
    print("2. Ver inventario ordenado por precio")
    print("3. Ver producto más barato y más caro")
    print("4. Ver total del inventario")
    print("5. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        registrar_producto(inventario)
    elif opcion == "2":
        ver_inventario_ordenado(inventario)
    elif opcion == "3":
        ver_extremos(inventario)
    elif opcion == "4":
        total_inventario(inventario)
    elif opcion == "5":
        print("¡Hasta la próxima!")
        break
    else:
        print("Opción inválida.")