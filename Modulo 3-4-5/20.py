'''
EJERCICIO 20 Hacer un programa de consola que tenga un menú y permita
generar números aleatorios entre 0 a 36, tipo una ruleta de
casino. Que diga la frase: “ruleta girando” cuando elijamos la
opción de probar suerte. Y que cuando pasen 5 segundos diga:
“¡no va más!” y luego de 2 segundos muestre el número
generado al azar, indicando si es par o impar. Que indique
también si está en la primera(1-12), segunda(13-24) o tercera
docena(25-36).
Menú:
a. Probar Suerte
b. Salir
'''
import time, random


def par_impar(dato):
    if dato % 2 == 0:
        print("-> Par")
    else:
        print("-> Impar")


def docena(dato):
    if 1 <= dato <= 12:
        print("--> Primera docena")
    elif 13 <= dato <= 24:
        print("--> Segunda docena")
    elif 25 <= dato <= 36:
        print("--> Tercera docena")
    else:
        print("--> ¡Salio el Cero!")


######################################


while True:
    print("Menú")
    print("1 - Probar Suerte")
    print("2 - Salir")
    opcion = input(">>> ")
    if opcion == "1":
        print("Ruleta Girando...")
        time.sleep(5)
        print("¡No va más!")
        time.sleep(2)
        valor = random.randint(0, 36)
        print("Salio el:", valor)
        par_impar(valor)
        docena(valor)
    elif opcion == "2":
        print(" ¡Gracias por usar nuestro programa! ")
        break
    else:
        print("¡No existe esa opción!")
