#Leer 2 números ingresados por el usuario, evaluar y mostrar en pantalla a cuál cuadrante 
#del plano cartesiano pertenece, considerar que también pueden darse los casos de:
    #a.	Ordenada positiva u Ordenada negativa
    #b.	Abscisa positiva o Abscisa negativa
    #c.	Punto origen

"""Planteamiento del problema

Existen 5 posibles combinaciones dentro de un plano cartesiano, dado que
los laterales o abscisas le pertenecen a X y los verticales u ordenadas a Y:

(+x,+y)
(-x,+y)
(-x,-y)
(+x,-y)
(0,0)"""

# Aunque el ejercicio limita de forma imaginaria las combinaciones
# El programa no serviria si no tomo en cuenta las otros 4 posibles combinaciones

"""(0,+y)
(0,-y)
(+x,0)
(-x,0)"""

print("Cuadrante de pertencia de 2 números")

# Defincion de variables

x = 0
y = 0

pc = 0
sc = 0
tc = 0
cc = 0

# Captura de datos

print("\nSolo ingresa números enteros")

x = int(input("\nIngresa el valor de X o la abscisa del cuadrante: "))
y = int(input("Ingresa el valor de Y o la ordenada del cuadrante: "))

# Procesamiento de datos

"""if x == x:
    print ("\nEl valor de la abscisa es: {}".format(x))
elif x == -x:
     print("\nEl valor de la abscisa es: {}".format(x))
else:
    print("Opcion no valida")

if y == y:
    print("\nEl valor de la ordenada es: {}".format(y))
elif y == -y:
    print("\nEl valor de la ordenada es: {}".format(y))
else:
        print("Opcion no valida")"""

print ("\nEl valor de la abscisa es: {}".format(x))
print("\nEl valor de la ordenada es: {}".format(y))

if x > 0 and y > 0:
    print("\nLos valores {} y {} pertenecen al primer cuadrante".format(x,y))
elif x < 0 and y > 0:
    print("\nLos valores {} y {} pertenecen al segundo cuadrante".format(x,y))
elif x < 0 and y < 0:
    print("\nLos valores {} y {} pertenecen al tercer cuadrante".format(x,y))
elif x > 0 and y < 0:
    print("\nLos valores {} y {} pertenecen al cuarto cuadrante".format(x,y))
elif x == 0 and y == 0:
    print("\nLos valores {} y {} pertenecen al punto de origen ".format(x,y))
elif x == 0 and y > 0:
    print("\nNo existe el valor de abscisa dado que es {} y el valor {} pertenece a su ordenada positiva".format(x,y))
elif x == 0 and y < 0:
    print("\nNo existe el valor de abscisa dado que es {} y el valor {} pertenece a su ordenada negativa".format(x,y))
elif x > 0 and y == 0:
    print("\nEl valor {} pertenece a su abscisa postiva y no existe el valor de ordenada dado que es {} ".format(x,y))
elif x < 0 and y == 0:
    print("\nEl valor {} pertenece a su abscisa negativa y no existe el valor de ordenada dado que es {} ".format(x,y))
else:
    print("Opcion no valida")


#NO SÉ COMO PRESIONAR UN MENSAJE DE ERROR CUANDO NO SE INGRESA EL TIPO DE DATO CORRECTO
# En este caso, como hacer que aparezca un mensaje de error en el caso que el usuario
# pongan un avlor diferente de INT

"""Traté con

if x and y == int:
    (todo el cuerpo de arriba)
else:
    print(Dato ingresado no valida)"""