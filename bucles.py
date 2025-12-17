# while --> repeticion indeterminada (1-856 intentos)
# for --> repeticion controlada (x repeticiones)

# usuario= input('Nombre de usuario: ')
# contraseña= input('Contraseña: ')

# si alguno esta mal, repite sin terminar
# while(usuario!='pepe' or contraseña!='asdasd'):
#     usuario= input('Incorrecto, introduce tu nombre de usuario: ')
#     contraseña= input('Incorrecta, introduce tu contraseña: ')

# print('Enhorabuena has entrado!!')

## intentos contados para acertar
# intentos = 3

# while(intentos > 0 and (usuario!='pepe' or contraseña!='asdasd')):
#     intentos = intentos - 1
#     usuario= input('Incorrecto, introduce tu nombre de usuario: ')
#     contraseña= input('Incorrecta, introduce tu contraseña: ')

# if(intentos== 0):
#     print('te has quedado sin intentos')


# siempre hace los intentos que se digan
# for numero in range(0,11):  # 1,2,3,4,5,6,7,8,9,10
#     if(numero % 2 == 0):      #par => al dividir entre 2, resto 0
#         print(numero)



## Ejercicio 1
# Crea una aplicación que pida un número y calcule su factorial 
# (El factorial de un número es el producto de todos los enteros 
#  entre 1 y el propio número y se representa por el número seguido 
#  de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120),

# numero= int(input('Introduce un número: '))
# factorial= 1
# representacion= str(numero) + '! = '

# for anterior in range(1, numero+1):
#     factorial= factorial*anterior

#     representacion = representacion + str(anterior)

#     if(anterior!=numero):
#         representacion = representacion + 'x'
#     else:
#         representacion = representacion + ' = ' + str(factorial)

# print(representacion)




## Ejercicio 3
# Algoritmo que pida números hasta que se introduzca un cero. 
# Debe imprimir la suma y la media de todos los números introducidos.
numero= (input('Dame un número: '))

if(numero.isdigit()):
    numero= int(numero)
else:
    print('Eso no es un número')

suma = 0
media = 0    #suma / cantidad de valores
cantidad = 0

while(numero!=0):
    suma += numero  # suma = suma + numero
    cantidad += 1   # cantidad = cantidad + 1
    numero= int(input('Dame otro número: '))

media= suma / cantidad
print(suma)
print(media)
