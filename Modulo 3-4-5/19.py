'''
EJERCICIO 19 Escribir una función que sirva para multiplicar cada elemento
de una lista numérica por un valor. Y devuelva la nueva lista con
cada elemento en su respectiva posición, pero ya multiplicado.
'''


def multiplicar(lista, valor):
    nueva = []
    for n in lista:
        resultado = n * valor
        nueva.append(resultado)
    return nueva


############################

# Valores de ejemplo

numeros = [10, 5, 3, 20]
m = 5

print(multiplicar(numeros, m))
