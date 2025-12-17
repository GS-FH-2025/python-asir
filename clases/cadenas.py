# str -> cadena de caracteres
# string= input('Dame una cadena de caracteres: ')

# print(string[0]) #primer elemento (izq -> der)
# ultima= len(string) -1
# print(string[ultima])

# print(string[-1]) #primer elemento (der -> izq)
# print(len(string)) #longitud de la cadena




# # 0  1  2  3  4  5  6  7
# # s  u  p  u  e  s  t  a
# #-8 -7 -6 -5 -4 -3 -2 -1 (negativos)

# cadena = 'supuesta'

# print(cadena[2:6]) #posiciones 2,3,4,5
# print(cadena[0:3])
# ultima= len(cadena)
# print(cadena[2:ultima])



prueba= 'paTaTa cOn huevo'

# print(prueba.upper()) #todo mayus
# print(prueba.title()) # mayus cada palabra (1ª letra)
# prueba = prueba.title()
# print(prueba) # mayus primera letra, resto minus

# print('b' not in prueba)







# listas --> cadenas de variables

# lista= [2, 4, 6, 'hola', True, [1,2,3]]

# print(lista[3][0])
# print(lista[-1][-1])


# print(3 in lista[-1])

# lista.append('final')
# print(len(lista))

# listaNotas= [5,6,7,8,9]
# print(max(listaNotas))
# print(sorted(listaNotas, reverse=True))
# listaNotas.reverse()
# print(listaNotas)
 

# lista[0]
# print(lista[0])
# lista.append(3) #añade al final
# print(lista)
# del lista[-1]   #elimina por posicion
# print(lista)




# muestrame una lista con las posiciones en las que está la letra 'a'

prueba= 'paTaTa cOn huevo'
posiciones= []              #3

contador= prueba.count('a')   #3
inicio = 0

while(len(posiciones) < contador):
    posicion= prueba.find('a', inicio) #1
    inicio = posicion + 1
    posiciones.append(posicion)

print(posiciones)