#Diseña un algoritmo que lea un numero del 1 al 12

#a.	Mostrar el mes perteneciente al numero
#b.	Mostrar época del año, dependiendo del rango de 
#meses: Invierno (1-3), Primavera (4-6), Verano (7-9), Otoño (10-12)

print("Lectura de meses y epocas")

#Definicion de variables

num = 0

inv = "Invierno" # Meses del 1 al 3
pri = "Primavera" # Meses del 4 al 6
ver = "Verano" # Meses del 7 al 9
oto = "Otoño" # Meses del 10 al 12

# Captura de datos

num = int(input("Ingresa un numero del 1 al 12: "))

#Calculo de operaciones

if num >= 1 and num <= 12:
    if num == 1:
        print("El mes es enero")
        print("La temporada es " + inv)
    elif num == 2:
        print("El mes es febrero")
        print("La temporada es " + inv)
    elif num == 3:
        print("El mes es marzo")
        print("La temporada es " + inv)
    elif num == 4:
        print("El mes es abril")
        print("La temporada es " + pri)
    elif num == 5:
        print("El mes es mayo")
        print("La temporada es " + pri)
    elif num == 6:
        print("El mes es junio")
        print("La temporada es " + pri)
    elif num == 7:
        print("El mes es julio")
        print("La temporada es " + ver)
    elif num == 8:
        print("El mes es agosto")
        print("La temporada es " + ver)
    elif num == 9:
        print("El mes es septiembre")
        print("La temporada es " + ver)
    elif num == 10:
        print("El mes es octibre")
        print("La temporada es " + oto)
    elif num == 11:
        print("El mes es noviembre")
        print("La temporada es " + oto)
    elif num == 12:
        print("El mes es diciembre")
        print("La temporada es " + oto)
else:
    print("Numero invalido, intentar otra vez")
