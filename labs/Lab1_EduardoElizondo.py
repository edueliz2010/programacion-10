print("Le ofresco mi más cordial buenvenida a este club el cual es solo y exclusibamente para mayores de 18 años o alguien que posea una invitación de otro miembro")
print("porfavor sea tan amable de llenar la siguiente: ")
# validar nombre
while True:
    name = input("Indique su nombre: " )
    if name != "" and name.replace(" ", "").isalpha():
        break
    else:
        print("distinguido caballero o dama su nombre no es valida")
# validar edad
while True:
    try:
        n = int(input("porfavor digite su edad: "  ))
        break
    except ValueError:
        print("La edad no es valida")
# Logica de ingreso
puede_entrar = False

if n >= 18:
    puede_entrar = True
else:
    permiso = input("¿De casualida tiene permiso? (si/no):  ").strip(). lower()
    if permiso in ["si", "sí"]:
        puede_entrar = True
# Mensaje final
if puede_entrar:
    print("bienvenido", name, "puede ingresar")
else:
    print("Lo sentimos", name, "no puede ingresar")

print("fin del programa")