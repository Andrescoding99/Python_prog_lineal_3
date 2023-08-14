# Desarrolle un algoritmo que valide el inicio de sesión con los posibles casos:  
#a.Usuarios: “admin” o usuario1
#b.Contraseñas: “CompuIntgrl??” o “compu1?”
#c.Muestre en pantalla un mensaje de bienvenida personalizado para cada usuario (administrador o invitado)

print("Validación de inicio de sesión")

#Defincion de variables 

usuario1 = "admin"
usuario2 = "usuario1"
contra1 = 0
contra2 = 0

val = 0 # Valor ingresado por el usuario, del dicconario

print("\n1. admin")
print("2. usuario1")

dicc = {    #dicc singnifica diccionario, donde se alamcenan los meses
1: "admin",
2: "usuario1",
}

#Captura de datos 

val = int(input("\nSeleccione entre los números 1-2, dependiendo del usuario que es: "))

if val in dicc:
    if val == 1:
        contra1 = input("Administrador favor ingresar su contraseña: ")
    elif val == 2:
        contra2 = input("Usuario favor ingresar su contraseña: ")
else:
    print("Opcion invalida intente de nuevo")

if contra1 == "CompuIntgrl??":
    print("Bienvenido administrador, te estabamos esperando ponte a trabajar.")
elif contra2 == "compu1?":
    print("Bienvenido usuario, te estabamos esperando ponte a trabajar.")
else:
    print("Contraseña invalida, vuelva a intentarlo")



