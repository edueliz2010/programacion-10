class Vehiculo:
    def __init__(self, placa, modelo):
        self.placa = placa
        self.modelo = modelo
        self.disponible = True
        self.kilometraje = 0

    def alquilar(self):
        self.disponible = False

    def devolver(self, km_recorridos):
        self.disponible = True
        self.kilometraje += km_recorridos

    def info(self):
        estado = "Disponible" if self.disponible else "Alquilado"
        return f"{self.placa} | {self.modelo} | {estado} | {self.kilometraje} km"

def buscar_vehiculo(flota, placa):
    for vehiculo in flota:
        if vehiculo.placa == placa:
            return vehiculo
    return None

def registrar_vehiculo(flota):
    placa = input("Placa: ").strip().upper()

    if buscar_vehiculo(flota, placa) is not None:
        print(f"La placa '{placa}' ya está registrada.")
        return

    modelo = input("Modelo: ").strip()
    flota.append(Vehiculo(placa, modelo))
    print(f"Vehículo '{placa}' registrado.")

def alquilar_vehiculo(flota):
    placa = input("Placa a alquilar: ").strip().upper()
    vehiculo = buscar_vehiculo(flota, placa)

    if vehiculo is None:
        print(f"No existe un vehículo con placa '{placa}'.")
        return
    if not vehiculo.disponible:
        print(f"El vehículo '{placa}' ya está alquilado.")
        return

    vehiculo.alquilar()
    print(f"Vehículo '{placa}' alquilado.")

def devolver_vehiculo(flota):
    placa = input("Placa a devolver: ").strip().upper()
    vehiculo = buscar_vehiculo(flota, placa)

    if vehiculo is None:
        print(f"No existe un vehículo con placa '{placa}'.")
        return
    if vehiculo.disponible:
        print(f"El vehículo '{placa}' no está alquilado.")
        return

    try:
        km = float(input("Kilómetros recorridos: "))
    except ValueError:
        print("El valor de kilómetros debe ser numérico.")
        return

    vehiculo.devolver(km)
    print(f"Vehículo '{placa}' devuelto. Kilometraje total: {vehiculo.kilometraje}")

def ver_flota(flota):
    if not flota:
        print("No hay vehículos registrados.")
        return

    print("\n--- Flota de la agencia ---")
    for vehiculo in flota:
        print(vehiculo.info())

flota = []

while True:
    print("\n=== AGENCIA DE ALQUILER ===")
    print("1. Registrar vehículo")
    print("2. Alquilar vehículo")
    print("3. Devolver vehículo")
    print("4. Ver flota completa")
    print("5. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        registrar_vehiculo(flota)
    elif opcion == "2":
        alquilar_vehiculo(flota)
    elif opcion == "3":
        devolver_vehiculo(flota)
    elif opcion == "4":
        ver_flota(flota)
    elif opcion == "5":
        print("¡Hasta la próxima!")
        break
    else:
        print("Opción inválida.")