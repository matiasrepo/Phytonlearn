#########################
# OPERADORES ARITMETICOS
##########################

# +	Suma los valores de tipo numérico
5 + 2
# –	Resta los valores de tipo numérico
5 - 2

# – Asigna un valor negativo a un dato numérico
-5

# *	Multiplica los valores de tipo numérico
5 * 2

# /	Divide los valores de tipo numérico
5 / 2

# %	Devuelve el resto de la división entre los valores de tipo numérico
5 % 2

#  //	Devuelve el cociente de la división entre los valores de tipo numérico
5 // 2

# **	Calcula el exponente entre valores de tipo numérico
5**2


##############################
# OPERADORES DE COMPARACION
##############################

"""
Son los que utilizamos para comparar dos valores. 
Devuelve un valor booleano (true o false) dependiendo de la condición.
"""

# ==	Compara los valores para ver si son iguales
5 == 2
# != Compara los valores para ver si son distintos
5 != 2

# <	Compara que el valor situado a la izquierda sea menor que el situado a la derecha
5 < 2

# >	Compara que el valor situado a la izquierda sea mayor que el situado a la derecha
5 > 2

# <= Compara que el valor situado a la izquierda sea menor o igual que el situado a la derecha
5 <= 2

# >= Compara que el valor situado a la izquierda sea mayor o igual que el situado a la derecha
5 >= 2

"""
Los operadores >, >=, < y <= sólo pueden aplicarse sobre  números enteros o de coma flotante; 
no obstante, los  operadores de igualdad y desigualdad permiten comparar  
indistintamente cualquiera de los cuatro tipos de dato  básicos 
"""
"Hola mundo" == 3.14
3.14 != True

"Hola" != "mundo"

######################
# OPERADORES LOGICOS
######################

# and Comprueba que el valor izquierdo y derecho se cumple	
True and False

# or Comprueba que el valor izquierdo o el derecho se cumple
print(True or False)
print()


##############
# CONJUNCIÓN
#############

'''¿Cómo puedo determinar si x es mayor a 1 y  menor a 10, 
o, lo que es lo mismo, si x se  encuentra entre 1 y 10? 
Necesito combinar dos  operaciones de comparación.
La conjuncion nos permite  saber si ambas comparaciones son verdaderas
'''
x = 12
print(x > 1 and x < 10)
