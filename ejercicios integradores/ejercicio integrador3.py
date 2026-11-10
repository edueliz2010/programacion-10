from abc import ABC, abstracmethod

class cliente(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
        self._compras = []

    @abstracmethod
    def calcular_descuento(self, monto):
        pass

    def generar_factura(self,monto):
        descuento = self.calcular_descuento(monto)
        total = monto - descuento
        self._compras.append(total)
        return total

    def total_comprado(self):
        return sum(self._compras)

class ClienteRegular(cliente):
    def calcular_descuento(self, monto):
        return 0

class ClienteMayorista(cliente):
    def calcular_descuento(self, monto):
        if monto >= 100000:
            return monto * 0.10
        return 0 

class ClienteVIP(cliente):
    def calcular_descuento(self, monto):
        return monto * 0.20

def buscar_cliente(clientes, nombre):
    for cliente in clientes:
        if cliente.nombre == nombre:
            return cliente
    return None


def registrar_cliente(clientes):
    nombre = input("Nombre: ").strip()

    if buscar_cliente(clientes, nombre) is not None:
        print(f"Ya existe un cliente llamado '{nombre}'.")
        return

    tipo = input("Tipo (regular/mayorista/vip): ").strip().lower()

    if tipo == "regular":
        clientes.append(ClienteRegular(nombre))
    elif tipo == "mayorista":
        clientes.append(ClienteMayorista(nombre))
    elif tipo == "vip":
        clientes.append(ClienteVIP(nombre))
    else:
        print("Tipo inválido.")
        return

    print(f"Cliente '{nombre}' registrado como {tipo}.")

def generar_factura_cliente(clientes):
    nombre = input("Cliente: ").strip()
    cliente = buscar_cliente(clientes, nombre)

    if cliente is None:
        print(f"No existe un cliente llamado '{nombre}'.")
        return

    try:
        monto = float(input("Monto de la compra: "))
    except ValueError:
        print("El monto debe ser numérico.")
        return

    total = cliente.generar_factura(monto)
    print(f"Factura generada para '{nombre}'. Total a pagar: ₡{total:,.2f}")


def ver_historial(clientes):
    nombre = input("Cliente: ").strip()
    cliente = buscar_cliente(clientes, nombre)

    if cliente is None:
        print(f"No existe un cliente llamado '{nombre}'.")
        return

    if not cliente._compras:
        print(f"'{nombre}' no tiene compras registradas.")
        return

    print(f"\n--- Historial de {nombre} ---")
    for i, monto in enumerate(cliente._compras, start=1):
        print(f"Factura {i}: ₡{monto:,.2f}")
    print(f"Total comprado: ₡{cliente.total_comprado():,.2f}")


def ver_clientes(clientes):
    if not clientes:
        print("No hay clientes registrados.")
        return

    print("\n--- Clientes registrados ---")
    for cliente in clientes:
        tipo = type(cliente).__name__                
        print(f"{cliente.nombre} ({tipo}): ₡{cliente.total_comprado():,.2f} comprados")