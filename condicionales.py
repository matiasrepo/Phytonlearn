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


# Usando sentencia else
a = 12
if a > 10:
    print("a es mayor que 10.")
else:
    print("a es menor o igual que 10.")
