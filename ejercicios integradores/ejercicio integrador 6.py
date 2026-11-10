productos = []

while True:
    print("\n=== CATÁLOGO DE LA TIENDA ===")
    print("1. Registrar producto")
    print("2. Ver catálogo ordenado por precio")
    print("3. Ver productos con pocas existencias (5 o menos)")
    print("4. Ver si todos los productos tienen existencias")
    print("5. Ver el valor total del inventario")
    print("6. Salir")

    opcion = input("Opción: ")
    
    if opcion == "1":
        nombre = input("Nombre del producto: ").strip()

        try:
            precio = float(input("Precio: "))
            existencias = int(input("Existencias: "))
        except ValueError:
            print("Precio y existencias deben ser numéricos.")
            continue

        if precio < 0 or existencias < 0:
            print("Precio y existencias no pueden ser negativos.")
            continue

        productos.append({"nombre": nombre, "precio": precio, "existencias": existencias})
        print(f"Producto '{nombre}' registrado.")

    elif opcion == "2":
        if not productos:
            print("No hay productos registrados.")
            continue

        print("\n--- Catálogo ordenado por precio ---")
        for producto in sorted(productos, key=lambda p: p["precio"]):   
            print(f"{producto['nombre']}: ₡{producto['precio']:,.2f} ({producto['existencias']} unidades)")

    elif opcion == "3":
        if not productos:
            print("No hay productos registrados.")
            continue

        pocas_existencias = [p for p in productos if p["existencias"] <= 5]   

        if not pocas_existencias:
            print("Ningún producto tiene pocas existencias.")
            continue

        print("\n--- Productos con pocas existencias ---")
        for producto in pocas_existencias:
            print(f"{producto['nombre']}: {producto['existencias']} unidades")

    elif opcion == "4":
        if not productos:
            print("No hay productos registrados.")
            continue

        hay_existencias = all(p["existencias"] > 0 for p in productos)   
        print(f"¿Todos los productos tienen existencias? {hay_existencias}")

    elif opcion == "5":
        if not productos:
            print("No hay productos registrados.")
            continue

        valor_total = sum(p["precio"] * p["existencias"] for p in productos)   
        print(f"Valor total del inventario: ₡{valor_total:,.2f}")

    elif opcion == "6":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida.")