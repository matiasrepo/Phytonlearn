##############################################
# ESTRUCTURAS DE CONTROL DE FLUJO ITERATIVAS
##############################################


"""
Un bucle o ciclo en programación es la ejecución  continua de un determinado bloque de código mientras una condición asignada se cumple..
En python iteran sobre los ítem de cualquier secuencia (lista, cadena, diccionario) en el orden en que aparecen en la secuencia.
Iterar: significa realizar cierta acción repetidas veces y en el caso de for hace referencia a recorrer elementos iterables
"""

#  BUCLE WHILE
"""
El bucle “while” en particular repite una  porción de código siempre que una expresión  sea verdadera. 
"""


i = 1
while i <= 3:
    print(i)
    i += 1
print("Programa terminado")

#################################

i = 1
while i <= 50:
    print(i)
    i = 3 * i + 1
print("Programa terminado")


##################################

numero = int(input("Escriba un número positivo: "))
while numero < 0:
    print("¡Ha escrito un número negativo! Inténtelo de nuevo")
    numero = int(input("Escriba un número positivo: "))
print(f"Gracias por su colaboración. Usted a ingresado el número: {numero}")


# Bucles infinitos

"""
Si la condición del bucle se cumple siempre, el bucle no terminará nunca de ejecutarse y tendremos lo que se denomina un bucle infinito. 
Los bucles infinitos no intencionados deben evitarse pues significan perder el control del programa. 
Para interrumpir un bucle infinito, hay que pulsar la combinación de teclas Ctrl+C. 
Al interrumpir un programa se mostrará un mensaje de error
"""


# i = 1
# while i <= 10:
#   print(i, end=" ")


# while True:
#  # Código
#  if <condición>:
#  break
#  # Código


# i = 1
# while i != 100:
#    print(i, end=" ")
#    i += 2


# ## Sentencia Else en bucle While
# Se encadena al While para ejecutar un bloque de código una vez la condición ya no devuelve True (normalmente al final).

c = 0
while c <= 5:
    c += 1
    print("c vale", c)
else:
    print("Se ha completado toda la iteración y c vale", c)

    # ## Instrucción Break
# Sirve para "romper" la ejecución del While en cualquier momento. No se ejecutará el Else, ya que éste sólo se llama al finalizar la iteración.

c = 0
while c <= 5:
    c += 1
    if c == 4:
        print("Rompemos el bucle cuando c vale", c)
        break
    print("c vale", c)
else:
    print("Se ha completado toda la iteración y c vale", c)


while True:
    NUMERO = int(input("Ingrese un numero entero: "))
    if NUMERO % 2 != 0:
        print("Este numero es impar")
        break
    print("Este numero es par")


print("Bienvenido al menú interactivo")
while(True):
    print("""¿Qué quieres hacer? Escribe una opción
    1) Saludar
    2) Sumar dos números
    3) Salir""")
    opcion = input("Escriba una opcion: ")
    if opcion == '1':
        print("Hola, espero que te lo estés pasando bien")
    elif opcion == '2':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print("El resultado de la suma es: ",n1+n2)
    elif opcion =='3':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")
