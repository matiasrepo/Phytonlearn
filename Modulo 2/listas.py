s###########
# LISTAS
###########

"""Las listas nos permiten agrupar varios objetos  (de cualquiera de los cuatro tipos de dato  básicos que vimos) en una misma variable.
Cada  uno de estos objetos se conoce como elemento.
Para crear una lista vamos a escoger un nombre  e indicar, entre corchetes y separados por  comas, los elementos.
Por ejemplo, el siguiente  código crea una lista de cinco números primos:"""

numeros_primos = [2, 3, 5, 7, 11]

print(numeros_primos)
print(type(numeros_primos))

# La siguiente es una lista con nombres de  alumnos:

alumnos = ["Jorge", "Matias", "Juan", "Martin"]
print(alumnos)
print(type(alumnos))

print("____________________________")


# Y esta última una lista con valores de  distintos tipos de dato:
print("____________________________")


datos = [3.14, True, -1, False, "Hola  mundo"]
print(datos)
print(type(datos))


print("____________________________")
print("____________________________")
print("____________________________")
print("____________________________")
print("____________________________")
print("____________________________")
print("____________________________")
# Acceder a los elementos de una Listas

"""Para acceder a un elemento de una lista a  partir de su índice,
vamos a indicarlo entre  corchetes luego del nombre de la lista.
"""

numeros_primos[0]
numeros_primos[1]
numeros_primos[2]
numeros_primos[3]
numeros_primos[4]


# Agregar  elementos a una Lista
"""
Para realizarlos usamos las sintaxis:
nombre_lista.append(elemento) 
nombre_lista.insert(indice, elemento)
"""

numeros_primos = [2, 3, 5, 7, 11]


numeros_primos.append(13)
print(numeros_primos[5])
print(numeros_primos)


numeros_primos.insert(2, 3.14) # type: ignore
print(numeros_primos[2])
print(numeros_primos)



# Eliminar elementos  y longitud de una Listas

'''Para realizarlos usamos las sintaxis: 

del nombre_lista[indice]

len(nombre_lista)'''

numeros_primos = [2, 3, 5, 7, 11]
print (numeros_primos)
del numeros_primos[2]

print (numeros_primos)

len(numeros_primos) #len nos dice la longitud o 
# cantidad de elementos que tiene una lista
#es abreviacion de lenght


'''Por último, para crear una lista vacía  usamos dos corchetes sin elementos:
Esto puede resultar útil cuando no  conocemos los elementos de la lista al  momento de crearla, 
pero los iremos  añadiendo vía append o insert en el  transcurso del programa.
'''
lista_vacia = []
print(lista_vacia)

lista_vacia.append(17)

print(lista_vacia)

lista_vacia.append(300)

print(lista_vacia)

