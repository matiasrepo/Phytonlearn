#
EOFError  # https://1drv.ms/f/s!Anh5cvrOJtUTlOIU252oztvwXQVBjA?e=lwRVoj

###############
# BIBLIOTECA
###############

'''
En informática, una biblioteca o, llamada por vicio del  idioma librería (del inglés library) 
es un conjunto de  implementaciones funcionales, codificadas en un  lenguaje de programación, 
que ofrece una interfaz  bien definida para la funcionalidad que se invoca.
La biblioteca estándar de Python es muy amplia, ofrece  una gran variedad de módulos incorporados 
que brindan  acceso a las funcionalidades del sistema y soluciones  
estandarizadas para los diversos problemas que pueden  ocurrir en el día a día en la programación.
'''
#########################
########################

# El módulo “time”
# https://docs.python.org/es/3/library/time.html )  proporciona varias funciones relacionadas  con el tiempo.

import time

print(time.asctime())  # arroja la fecha y hora actual.

time.sleep(10)  # demora la ejecucuion del programa.

print(time.asctime())

'''Hacer un script contador de 0 hasta 10, que vaya  mostrando los números segundo a segundo.
'''

import time as ti

i = 0

while i < 10:
    print(i)

    ti.sleep(1)

    i = i + 1

###########################
# El módulo “random”
import random

print(random.randint(1, 100))

print(random.randint(1, 100))

print(random.randint(1, 100))

print(random.randint(1, 100))
print(random.randint(1, 100))

print(random.randint(1, 100))

'''Generar un programa de consola que tenga un
menú y permita generar números aleatorios
entre 1 y 6, como si fuera un dado.
Menú:
1. Tirar dado.
2. Salir
'''
import random

while True:
    print("Menú")
    print("1 - Tirar dado")
    print("2 - Salir")
    opcion = input(">>> ")
    if opcion == "1":
        valor = random.randint(1, 6)
        print("El valor del dado es:", valor)
    elif opcion == "2":
        print(" ¡Gracias por usar nuestro programa! ")
        break
    else:
        print("¡No existe esa opción!")
