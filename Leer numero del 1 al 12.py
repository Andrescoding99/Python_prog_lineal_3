#Diseña un algoritmo que lea un numero del 1 al 12

#a.	Mostrar el mes perteneciente al numero
#b.	Mostrar época del año, dependiendo del rango de 
#meses: Invierno (1-3), Primavera (4-6), Verano (7-9), Otoño (10-12)

print("Lectura de un número del 1 al 12")

#Definir las variables 

ene = "Enero"
feb = "Febrero"
mar = "Marzo"
abr = "Abril"
may = "Mayo"
jun = "Junio"
jul = "Julio"
ago = "Agosto"
sep = "Septiembre"
oct = "Octubre"
nov = "Noviembre"
dic = "Diciembre"

inv = "Invierno" # Mes del 1 - 3
pri = "Primavera" # Mes del 4 - 6
ver = "Verano" # Mes del 7 - 9
oto = "Otoño" # Mes del 10 - 12

val = 0

print("\n1. Enero")
print("2. Febrero")
print("3. Marzo")
print("4. Abril")
print("5. Mayo")
print("6. Junio")
print("7. Julio")
print("8. Agosto")
print("9. Septiembre")
print("10. Octubre")
print("11. Noviembre")
print("12. Diciembre")

dicc = {    #dicc singnifica diccionario, donde se alamcenan los meses
1: "Enero",
2: "Febrero",
3: "Marzo",
4: "Abril",
5: "Mayo",
6: "Junio",
7: "Julio",
8: "Agosto",
9: "Septiembre",
10: "Octubre",
11: "Noviembre",
12: "Diciembre",
}

#Captura de datos 

val = int(input("\nSeleccione entre los números 1-12, dependiendo del mes en que se encuentre: "))

if val in dicc:
    if val == 1:
     print("\nEl mes es: " + ene)
    elif val == 2:
     print("\nEl mes es: " + feb)
    elif val == 3:
     print("\nEl mes es: " + mar)
    elif val == 4:
     print("\nEl mes es: " + abr)
    elif val == 5:
     print("\nEl mes es: " + may)
    elif val == 6:
     print("\nEl mes es: " + jun)
    elif val == 7:
     print("\nEl mes es: " + jul)
    elif val == 8:
     print("\nEl mes es: " + ago)
    elif val == 9:
     print("\nEl mes es: " + sep)
    elif val == 10:
     print("\nEl mes es: " + oct)
    elif val == 11:
     print("\nEl mes es: " + nov)
    elif val == 12:
     print("\nEl mes es: " + dic)
else:
 print("Opcion no valida")



if val == 1:
 print("La epoca del año es: " + inv)
elif val == 2:
    print("\nLa epoca del año es: " + inv)
elif val == 3:
    print("\nLa epoca del año es: " + inv)
elif val == 4:
    print("\nLa epoca del año es: " + pri)
elif val == 5:
    print("\nLa epoca del año es: " + pri)
elif val == 6:
    print("\nLa epoca del año es: " + pri)
elif val == 7:
    print("\nLa epoca del año es: " + ver)
elif val == 8:
    print("\nLa epoca del año es: " + ver)
elif val == 9:
    print("\nLa epoca del año es: " + ver)
elif val == 10:
    print("\nLa epoca del año es: " + oto)
elif val == 11:
    print("\nLa epoca del año es: " + oto)
elif val == 12:
    print("\nLa epoca del año es: " + oto)
else:
 print("Opcion no valida")

# NO SUPE COMO PUNER UNA FUNCION (IN RANGE) PARA QUE PUSIERA TAMBINE LAS ESTACIONES JUNTAS
# SIN NECESIDAD DE VOLVER A CORRER OTRO IF