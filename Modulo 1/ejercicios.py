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
print("Ejercicio 2")
saludo = "Hola"
nombre = "Matías Nuñez"
separador = " "
saludoCompleto = saludo + separador + nombre  # Junto todas las variables en una
print(saludoCompleto)


"""Ejercicio 3
Mostrar el precio del IVA de un producto con un valor de 100 y su precio final."""
print("Ejercicio 3")
iva = 0.21
precio_producto = 100
precio_iva = precio_producto * iva
print("El porcentaje del IVA es",int(iva * 100), "%")
print("El precio del IVA es", precio_iva, "$")
print("El precio final es", precio_iva + precio_producto, "$")
print("_____________________")
print("_____________________")
print("_____________________")
print("_____________________")
print("_____________________")
print("_____________________")
print("_____________________")

"""Ejercicio 4
Realizar un programa que tenga 2 variables, base = 10 y altura = 5,
calcular el área de un rectángulo y mostrar por pantalla."""
print("Ejercicio 4")
base = 10.5
altura = 5.9

area = base * altura

print("El area del rectangulo es:",(round(area,2))) #el ROUND asigna la cantidad de decimales


print ("_________________________")
print ("_________________________")
print ("_________________________")
print ("_________________________")
print ("_________________________")
"""Ejercicio 5
Dadas 2 variables: a = 20 y b = 10, mostrar por pantalla su suma,
resta, multiplicación y división."""
print("Ejercicio 5")
a = 20
b = 10

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b

print("La suma es:", suma)
print("La resta es:",resta)
print("La multiplicación es:", multiplicacion)
print("La división es:", division)

"""Ejercicio 6
Un empleado cobro 300 dólares por mes desde enero a junio, 500
dólares de julio a octubre, y 700 dólares por mes en noviembre y
en diciembre.
Hace un programa que calcule el sueldo promedio. Y que diga si
este “empleado” esta cobrando un sueldo bajo, normal o mejor de
lo normal.
a. Sueldo Bajo: por debajo de 300 dólares
b. Sueldo Normal: entre 300 a 900
c. Sueldo mejor de lo normal: más de 900 dólares"""
print("_____________")
print("_____________")
print("_____________")
print("_____________")
print("_____________")
print("_____________")
print("Ejercicio 6")
print("_____________")
sueldo_total = 300 * 6 + 500 * 4 + 700 * 2
sueldo_promedio = round(sueldo_total / 12, 2)

print("El sueldo promedio es:",sueldo_promedio)

if sueldo_promedio < 300:
    print("Sueldo Bajo")
elif sueldo_promedio < 900:
    print("Sueldo Normal")
else:
    print("Sueldo mejor de lo Normal")
    

