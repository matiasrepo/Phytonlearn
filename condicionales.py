################
# CONDICIONALES
################

"""
Los condicionales nos permiten diferir la ejecución de  una porción de código (es decir, una o más líneas)  
según se cumpla una condición u otra; o, lo que es lo  mismo, 
hacer que un bloque de código se ejecute  únicamente cuando se cumpla una condición. 
Es decir,  los condicionales nos permiten modificar el flujo del  programa.
"""

""" a = 12  # Esta línea define una variable a con  el valor 12
if (
    a > 10
):  # Esta línea indica que el  código a continuación sólo debe ejecutarse  cuando la condición a > 10 sea verdadera.
    print("a es mayor que 10.")
    
    """

"""
# Usando sentencia else
a = 3
if a > 10:
    print("a es mayor que 10.")
else:
    print("a es menor o igual que 10.")
"""


"""
# Otra forma
a = 12
if a > 10:
	print("a es mayor que 10.")  
if a <= 10:
	print("a es menor o igual que 10.")
"""

"""
# Veamos otra condicion

a = 99
if a == 1:
    print("a es 1.")
elif a == 2:
    print("a es 2.")
elif a > 2 and a < 10:
    print("a es mayor que 2 y menor que 10.")
else:
    print("a es mayor o igual que 10.")

"""


"""
# Otro ejemplo

n = 11
if n % 2 == 0:
    print(n,"es un número par")
else:
    print(n,"es un número impar")	
"""

comando = "OTRA COSA"
if comando == "ENTRAR":
    print("Bienvenido al sistema")
elif comando == "SALUDAR":
    print("Hola, espero que te lo estés pasando bien aprendiendo Python")
elif comando == "SALIR":
    print("Saliendo del sistema...")
else:
    print("Este comando no se reconoce")
