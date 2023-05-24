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

"""
Otra de las ventajas que Python nos provee,
es la de poder asignar en una sola instrucción, múltiples variables:
"""
a, b, c = "string", 15, True

"""
En una sola instrucción, estamos declarando tres variables:
a, b y c y asignándoles un valor concreto a cada una:
"""

print(a)
print(b)
print(c)


##################################
# Conocer mas la funcion print()
###################################

a = "azul"
b = "verde"
c = "rojo"

# Primer punto a observar: print() separa cada argumento empleando un espacio en blanco.

print(a, b, c)

# Segundo punto: cada impresión con print() concluye con un salto de línea.

print(a)
print()
print(b)
print(c)

print("aaaa \n" "bbbb")


"""
La función print() admite un argumento, llamado sep, 
que contiene la cadena de caracteres que emplearemos para separar cada elemento.
"""
print(a, b, c, sep="-")

# El argumento end =“” , permite continúe justo donde acabó, sin generar salto de línea.

print(a, b, c, end=" ")
print("Hola mundo")
print("Hola mundo")

########################
# Cadenas f
########################
'''
En Python 3.6 se añadió (PEP 498) una nueva notación para cadenas llamada cadenas "f", 
que simplifica la inserción de variables y expresiones en las cadenas. 
Una cadena "f" contiene variables y expresiones entre llaves ({}) que se sustituyen directamente por su valor. 
Las cadenas "f" se reconocen porque comienzan por una letra f antes de las comillas de apertura.
'''
nombre = "Pepe"
edad = 25
print(f"Me llamo {nombre} y tengo {edad} años.")

semanas = 4
print(f"En {semanas} semanas hay {7 * semanas} días.")

# Esta notación no añade espacios que en la notación "clásica"

