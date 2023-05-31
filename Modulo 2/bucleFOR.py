# Bucle FOR

"""
En el caso de un bucle FOR se debe especificar la variable donde se alojarán los ítem del elemento iterable (lista, diccionario, cadena, etc.)
Se coloca la sentencia FOR seguida de la variable donde se almacenarán los ítem y luego del operador «in» el elemento a iterar:
El bucle FOR, como tal, también repite la ejecución de un
bloque de código, tantas veces como elementos contenga unalista.
"""

alumnos = ["Matias", "Jorge", "Martin", "Pablo"]
for alumno in alumnos:
    print("Hola mundo")

print("_______________")
for alumno in alumnos:
    print(alumno)

print("___________________________________________")

print("Comienzo")
for i in [0, 1, 2]:
    print("Hola ", end="")
print()
print("Final")

print("___________________________________________")
print("Comienzo")
for i in []:
    print("Hola ", end="")
print()
print("Final")

print("_________________________________________")
print("Comienzo")
for i in [1, 1, 1]:
    print("Hola ", end="")
print()
print("Final")

print("_________________________________________")
print("Comienzo")
for _ in [0, 1, 2]:
    print("Hola ", end="")
print()
print("Final")

print("________________________________________")
print("Comienzo")
for i in [3, 4, 5]:
    print(f"Hola. Ahora i vale {i} y su cuadrado {i ** 2}")

print("Final")



i = 10
print(f"El bucle no ha comenzado. Ahora i vale {i}")

for i in [0, 1, 2, 3, 4]:
    print(f"{i} * {i} = {i ** 2}")

print(f"El bucle ha terminado. Ahora i vale {i}")



print("_____________________________________")
for i in "AMIGO":
    print(f"Dame una {i}")
print("¡AMIGO!")