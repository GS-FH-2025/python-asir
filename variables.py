# # STRING(str) --> ?,$,4,p
# variable = "Hola me llamo juan"
# print(type(variable))
# print(variable)

# # INTEGER(int) --> 4, 173, 0
# numero = 5
# print(type(numero))
# print(numero)

# # FLOAT(float) --> 4.0, 173.5, 0.9
# barco = 13.56
# print(type(barco))
# print(barco)

# # BOOLEAN(bool) --> True, False
# booleano= True
# print(type(booleano))
# print(booleano)





# TIPOS DE VARIABLES -- INTEGER/FLOAT
# numero1 = int(input('Dame un número: '))   #str --> int
# numero2 = float(input('Dame otro número: ')) #str --> int

# cuenta1 = numero1 / numero2  # division normal
# cuenta2 = numero1 // numero2  # division entera (solo cociente)
# cuenta3 = numero1 % numero2  # division entera (solo resto)

# cuenta = numero1 + numero2
# print(int(cuenta))


# TIPOS DE VARIABLES -- STRING
# caracter1= input('Dame una letra: ')
# caracter2= 'becedario'
# caracter3= '2025'
# print(caracter1+caracter2+caracter3)

# dato= True
# print(type(dato))
# print(dato)

# dato= str(True)
# print(type(dato))
# print(dato)


# TIPOS DE VARIABLES -- BOOLEAN

# variable1 = True
# variable2 = False  # 0, 0.0, ''(vacío sin espacios)

# print(bool(numero1))
# print(bool(caracter1))

# print( 5 <= 7 )














# EJERCICIOS

## Ejercicio 1
# Escribir un programa que pregunte al usuario su nombre, y luego lo salude.

# nombre= input('Dime tu nombre: ')

# print('Hola', nombre)



## Ejercicio 3
# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
# h^2 = c^2 + c^2   -->     h= raiz(c^2 + c^2)


# import math

# cateto1= int(input('Cateto 1: '))
# cateto2= int(input('Cateto 2: '))

# hipotenusaCuadrado= cateto1**2 + cateto2**2

# hipotenusa= math.sqrt(hipotenusaCuadrado)

# print('El valor de la hipotenusa es %.2f' % hipotenusa)




# % --> variable
#   s= string (cadena texto)
#   d= integer (numero entero)
#   f= float (numero con decimales)

# print('%s yo me llamo: %s y tu te llamas %s' % (tipoSaludo, minombre, tunombre))



## Ejercicio 10
# Un alumno desea saber cual será su calificación final en la materia de Algoritmos. 
# Dicha calificación se compone de los siguientes porcentajes:

# 55% del promedio de sus tres calificaciones parciales.
# 30% de la calificación del examen final.
# 15% de la calificación de un trabajo final.

parcial1= int(input('Nota parcial 1: '))
parcial2= int(input('Nota parcial 2: '))
parcial3= int(input('Nota parcial 3: '))

promedio= (parcial1+parcial2+parcial3)/3

examen= int(input('Nota examen: '))
trabajo= int(input('Nota trabajo: '))

nota= promedio*0.55 + examen*0.30 + trabajo*0.15

print('Tu nota final es de %s' % (nota))




## Ejercicio 15
# Dadas dos variables numéricas A y B, que el usuario debe teclear, 
# se pide realizar un algoritmo que intercambie los valores de ambas 
# variables y muestre cuanto valen al final las dos variables.

# A= int(input('Variable numerica A: '))
# B= int(input('Variable numerica B: '))

# print('A: %s, B: %s' % (A,B))

# copia = A 

# A = B         

# B = copia    

# print('Nuevo A: %s, Nuevo B: %s' % (A,B))




## Ejercicio 17
# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
# Escribir un algoritmo que determine la hora de llegada a la ciudad B.

# horaSalida= int(input('Hora de salida: '))
# minutoSalida= int(input('Minuto de salida: '))
# segundoSalida= int(input('Segundo de salida: '))

# segundosViaje= int(input('Segundos que dura el viaje: '))


# segundosTotalesSalida= segundoSalida + minutoSalida*60 + horaSalida*3600

# segundosFinal= segundosViaje+segundosTotalesSalida


# horaLlegada= int(segundosFinal/3600)                  # / division entera (cociente)
# minutoLlegada= int((segundosFinal%3600) / 60)                  # % división entera (resto)
# segundoLlegada= int((segundosFinal % 3600) % 60)

# print('%d:%d:%d' % (horaLlegada, minutoLlegada, segundoLlegada))


# Ejercicio 18
# Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

# nombre= input('Nombre: ')
# ap1= input('Apellido 1: ')
# ap2= input('Apellido 2: ')

# # NUMEROS (int)  suma A + B = C
# # STRING (str) concatena 'A' + 'B' = 'AB'
# iniciales= nombre[0] + ap1[0] + ap2[0]

# print(iniciales.upper())
