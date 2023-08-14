#Diseñe un algortimo que capture nombre y edad de usuario

#a.	Validar que la edad debe ser mayor que 0 
#b.	Comparar cual de ambos hermanos es mayor y destacarlo
#c.	Mostrar en pantalla, si es niño, adolescente, adulto o adulto mayor, 
#dependiendo de la edad

#Bebes de 0 a 1 año
#Niños de 2 a 11 años
#Adolescente de 12 a 17 años
#Adulto de 18 a 59 años
#Adulto mayor de 60 a 1000

print("Captura de nombre y edad de un usuario")

#Definicion de variables

nombre1 = 0
edad1 = 0 
nombre2 = 0
edad2 = 0

#Captura de datos

nombre1 = input("\nIngrese el nombre del primer hermano: ")
edad1 = int(input("Ingrese la edad del primer hermano: "))

nombre2 = input("\nIngrese el nombre del segundo hermano: ")
edad2 = int(input("Ingrese la edad del segundo hermano: "))


if edad1 >=0 or edad2 >= 0:# ---> Hizo falta comparar la primera edad, solo comparaba la segunda, por eso no funcionaba
#a.	Validar que la edad debe ser mayor que 0 
    if edad1 and edad2 != 0:# ---> Hizo falta comparar la primera edad, pero, aqui ya no es necesario
       print("\nLa edad es valida, por que es mayor que 0")
    else:
       print("\nLa edad no es valida porque es igual a 0")
   #b.	Comparar cual de ambos hermanos es mayor y destacarlo
    if edad1 > edad2:#Falto evaluar si son iguales
       print("\nLa edad de {} es mayor que {}".format(nombre1,nombre2))
    else:
       print("\nLa edad de {} es mayor que {}".format(nombre2,nombre1))
    #c.	Mostrar en pantalla, si es niño, adolescente, adulto o adulto mayor, 
    #dependiendo de la edad
    if edad1 <= 1:
       print("\nLa edad de " + nombre1 + " esta en la categoria de bebe")
    elif edad1 <= 11:
        print("\nLa edad de " + nombre1 + " esta en la categoria de niño")
    elif edad1 <= 17:
        print("\nLa edad de " + nombre1 + " esta en la categoria de adolescente")
    elif edad1 <= 59:
        print("\nLa edad de " + nombre1 + " esta en la categoria de adulto")
    else:
      print("\nLa edad de " + nombre1 + " esta en la categoria de adulto mayor")

    if edad2 <= 1:
        print("\nLa edad de " + nombre2 + " esta en la categoria de bebe")
    elif edad2 <= 11:
        print("\nLa edad de " + nombre2 + " esta en la categoria de niño")
    elif edad2 <= 17:
        print("\nLa edad de " + nombre2 + " esta en la categoria de adolescente")
    elif edad2 <= 59:
        print("\nLa edad de " + nombre2 + " esta en la categoria de adulto")
    else:
      print("\nLa edad de " + nombre2 + " esta en la categoria de adulto mayor")
else:
   print("\nEl programa termina porque una de las edades es igual a 0")