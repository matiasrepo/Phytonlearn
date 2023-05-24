####################################
# ENTRADA DE DATOS - FUNCION input()
####################################

"""
La función input() permite a los usuarios introducir datos de distintos tipos
desde la entrada estándar (normalmente se corresponde con la entrada de un teclado).
Y estos valores ingresados se pueden guardar en una variaable
"""

nombre = input("Escribe tu nombre: ")
print(nombre)

"""
También, como el resultado de input es  siempre una cadena,
podemos usar el  operador de suma para mostrar un saludo:
"""

nombre = input("Escribe tu nombre:")
print("Hola" + " " + nombre)
if nombre == "Repo":
    print("Que onda turro")
else:
    print("quien so vo")


####################################
# CONVERSIONES ENTRE TIPOS DE DATOS
####################################

"""
Es una acción muy común y muy sencilla la de  convertir de un tipo de dato a otro.
Por ejemplo, podemos convertir un número de coma  flotante a un número entero vía la instrucción int.
Como los números enteros no pueden tener parte  decimal,
convertir un número de coma flotante a un  número entero implica despreciar los decimales.

"""

pi = 3.14
pi_entero = int(pi)
print(pi_entero)

print(type(pi))

print(type(pi_entero))

type(int())


# Conversión de una cadena  a un número entero, usamos int

numero_en_cadena = "30"
numero_entero = int(numero_en_cadena)
print(numero_entero)

print(type(numero_en_cadena))

print(type(numero_entero))


# Conversión de un número  entero a una cadena, usamos str

numero_entero = 30
print(numero_en_cadena)

print(type(numero_en_cadena))


####################
# Asignación múltiple
####################

'''
Otra de las ventajas que Python nos provee,
es la de poder asignar en una sola instrucción, múltiples variables:
'''
a, b, c = 'string', 15, True

'''
En una sola instrucción, estamos declarando tres variables:
a, b y c y asignándoles un valor concreto a cada una:
'''

print(a)
print(b)
print(c)



##################################
# Conocer mas la funcion print()
###################################

a = 'azul'
b = 'verde'
c = 'rojo'

# Primer punto a observar: print() separa cada argumento empleando un espacio en blanco.

print(a,b,c)

# Segundo punto: cada impresión con print() concluye con un salto de línea.

print(a)
print()
print(b)
print(c)