################
# TIPO DE DATOS
################

"""
En Python, distinguimos  cuatro tipos de dato básicos: números enteros,  
números de coma flotante (racionales), cadenas  (conjunto de caracteres para representar un texto)  y booleanos (aquellos que solo pueden contener  dos valores: verdadero o falso).

"""

a = 12
saludo = "Hola mundo"
pi = 3.14
encendido = True

"""
La sintaxis de Python para representar números  decimales es usando la coma por un punto 
En el caso de  los booleanos, los únicos dos valores que  aceptan son True y False. 
Nótese que Python  distingue entre minúsculas y mayúsculas; por  ende,  true o TRUE son incorrectos.
"""

print(type(a))
print("_________")
print(type(saludo))
print("_________")
print(type(pi))
print("_________")
print(type(encendido))
print("_________")
print("_________")
print("_________")

# TIPADO DINAMICO
"""
Un  lenguaje de programación es dinámicamente  tipado si una variable puede tomar valores de  distinto tipo. """

b = 1
print(type(b))

b = "Hola mundo"
print(type(b))
