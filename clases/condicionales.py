variable= 'cadena de texto' # str (string)
variable2= 2        # int (integer)
variable3= 4.3      # float
variable4= True     # bool (boolean)


# edad= int(input('Dime tu edad: '))       #int(str)
# if(edad >= 18):
#     print('Adelante caballero')
# else:
#     print('Niño pa tu casa')

# notas= int(input('Niño dame las notas: '))
# if(notas == 10):                                #alternativa 1
#     print('Ole miniño')
# elif(notas == 9 or notas == 8):                 #alternativa 2
#     print('Muy bien hecho')
# elif(notas == 5 or notas == 6 or notas == 7):   #alternativa 3
#     print('Te salvas por los pelos campeon')
# else:                                           # en cualquier otro caso
#     print('Corre que te vas a enterar')





## Ejercicio 1
# Algoritmo que pida dos números e indique si el 
# primero es mayor que el segundo o no.

# numero1= int(input('Dame el primer número: '))  #importante!!!
# numero2= int(input('Dame el segundo número: '))

# # True si n1 > n2
# # False si n2 > n1

# if(numero1 > numero2):
#     print('El número 1 es el mayor')
# else:
#     print('El número 1 no es el mayor')



## Ejercicio 2
# Algoritmo que pida un número y diga si es positivo, negativo o 0.

# numero= (input('Introduce un número: '))

# if(numero.lstrip('-').isdigit()):
    
#     numero= int(numero)

#     if(numero > 0):
#         print('Positivo!!!!!')
#     elif(numero < 0):
#         print('Negativo :´(')
#     elif(numero == 0):
#         print('Es cero!')

# else:
#     print('Eso no es un número')




## Ejercicio 5
# Escribe un programa que pida un nombre de usuario y una contraseña 
# y si se ha introducido “pepe” y “asdasd” se indica 
# “Has entrado al sistema”, sino se da un error.

# usuario= input('Dame tu nombre de usuario: ')   #str
# contraseña= input('introduce tu contraseña: ')


# if (usuario.lower()=='pepe' and contraseña=='asdasd'):
#     print('Has entrado al sistema')
# else:
#     print('Error al iniciar sesión')



## Ejercicio 9
# Algoritmo que pida tres números y los muestre ordenados 
# (de mayor a menor);

# n1= int(input('Dame el 1º número: '))
# n2= int(input('Dame el 2º número: '))
# n3= int(input('Dame el 3º número: '))

# if(n1>n2):                      #n1 > n2
#     if(n1>n3):                      #n1 > n3
#         if(n2>n3):                      #n1 > n2 > n3
#             print(n1,n2,n3)
#         else:                           #n1 > n3 > n2
#             print(n1,n3,n2)
    
#     else:                               #n3 > n1 > n2
#         print(n3,n1,n2)

# else:                           #n2 > n1
#     if(n1>n3):                          #n2 > n1 > n3
#         print(n2,n1,n3)
    
#     else:                           #n3 > n1 
#         if(n2>n3):                      #n2 > n3 > n1
#             print(n2,n3,n1)
#         else:                           #n3 > n2 > n1
#             print(n3,n2,n1)




## Ejercicio 13
# Escribe un programa que pida una fecha (día, mes y año) 
# y diga si es correcta.

# dia= int(input('Día: '))
# mes= int(input('Mes: '))
# año= int(input('Año: '))

# if(mes < 1 or mes > 12):
#     print('Error al poner el mes, solo hay 12 meses')
# if(año < 0):
#     print('Error: el año no puede ser anterior a 0')

# # 30 --> nov, abr, jun, sept
# # 31 --> resto
# # 28/29 --> feb
# if(dia < 1 or dia > 31):
#     print('Error: los días van del 1 al 31')
# else:
#     if(mes==4 or mes==6 or mes==9 or mes==11):
#         if(dia>30):
#             print('No hay más de 30 días en este mes')
#     elif(mes==2):
#         # año bisiesto
#         if((año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)):
#             if(dia > 29):
#                 print('Febrero no tiene más de 29 días en bisisesto')
#         # año no bisiesto
#         else:
#             if(dia > 28):
#                 print('Febrero no tiene más de 28 días si no es bisisesto')
