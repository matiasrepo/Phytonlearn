""" Ejercicio 1
Crear, en un script de Python, tres variables nombradas a , b y c con valores
numéricos cualesquiera; una cuarta llamada resultado que sea la suma de las
primeras tres, y por último imprimir en pantalla cada una de ellas. Antes de mostrar el
valor de cada variable, indicar su nombre en una línea anterior.
Un ejemplo de lo que se debería mostrar en pantalla es el siguiente:
a:
5
b:
7
c:
10
resultado:
22 
"""
"""
# Paso 1 -- declarar variables
a = 30
b = 40
c = 100
# Paso 2 -- declarar formula
resultado = a + b + c
print("a:")
print(a)
print("b:")
print(b)
print("c:")
print(c)
print("_____")
print("resultado:")
print(resultado)

"""


""" Ejercicio 2
Crear dos variables, saludo y nombre , cuyos contenidos sean " Hola, " en el
primer caso y tu nombre en el segundo. Intenta sumarlas vía el operador + y mostrar el
resultado en pantalla. Para guardar el resultado de la suma puedes crear una tercera
variable. """

saludo = "Hola"
nombre = "Matías Nuñez"
separador = " "
saludoCompleto = saludo + separador + nombre  # Junto todas las variables en una
print(saludoCompleto)



"""Ejercicio 3
Mostrar el precio del IVA de un producto con un valor de 100 y su precio final."""

iva = 0.21
precio_producto = 100
precio_iva = precio_producto * iva
print("El precio del IVA es", precio_iva, "$")
print("El precio final es", precio_iva + precio_producto,"$")

