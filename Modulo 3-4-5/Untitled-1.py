lista = [11, False]
mi_var = lista[0]
print(mi_var)

lista[0] = 22

print(mi_var)

# prueba con indices negativos para testear

lista_nueva = [1, 2, 3, 4, 5, 6]
print(lista_nueva[-2])

# esto me daria como print 5, dado que es el anteultimo (en este caso -1 toma al ultimo de la fila)

# slicing en python (particionado)

lista_slicing = [1, 2, 3, "True", [1, 2]]
variable_slicing = lista_slicing[1:4]
print(variable_slicing)

# podemos ver que al hacer 1:4 toma el primer indice HASTA el cuato indice SIN INCLUIR ESTE ULTIMO


# indentacion, es importante la correcta indentancion

fav = "2000"
if fav == "1975":
    print("Genial")
print("Si no indento, vas a ver este comentario aunque la condicion no se cumpla")

if fav == "2000":
    print("Genial")
    print("Este mensaje lo verias solo si se cumple la condicion dado que esta indentado correctamente")

'''
Una función puede tener múltiples argumentos, la cantidad que nosotros
precisemos. Para indicar más de uno separamos sus nombres por comas.
Por ejemplo:
'''


def imprimir_suma(a, b):
    print("Resultado:")
    print(a + b)


imprimir_suma(7, 5)
imprimir_suma(-5, 3.5)

# La función imprimir_suma() requiere dos argumentos, al primero de ellos le dimos
# el nombre a y, al segundo, b. Al llamarla, indicamos en orden los valores que
# queremos otorgarle, separados por comas.


###################
# Sentencia RETURN
###################

'''
Una sentencia es una instrucción que el intérprete de Python puede ejecutar. 
Cuando usted digita una sentencia en la línea de comandos, Python la ejecuta y despliega el resultado, si hay alguno.
Cuando acaba la última instrucción de una función, 
el flujo del programa continúa por la instrucción que sigue a la llamada de dicha función. 
Hay una excepción: usar la sentencia RETURN, hace que termine la ejecución de la función cuando aparece 
y el programa continúa por su flujo normal.
Además, return se puede utilizar para devolver un valor.
'''


def saludo():
    print('Buenos')
    print('Dias')


saludo()


def saludo():
    print('Buenos')
    print('Dias')


saludo()


# Otro uso de la sentencia return

def saludo():
    print('Buenos')
    print('Dias')


saludo()


# Otro uso de la sentencia return

def cal(x, y):
    z = x + y


a = cal(1, 2)
b = cal(3, 4)
c = cal(5, 6)

d = a + b + c

print(d)

###################
# EJERCICIOS
###################

'''
EJERCICIO 14. Escriba un programa que permita crear una lista de
nombres. Para ello, el programa tiene que pedir un número
y luego solicitar esa cantidad de nombres para crear la lista.
Por último, el programa tiene que mostrar la lista creada
recorriendo la lista con un for.
'''
# Ingreso por teclado de la cantidad de nombres
cantidad = input("¿Cuantos nombres desea ingresar?: ")

# Chequeamos que sea un numero
while cantidad.isdecimal() == False:
    print("¡Error. Solo numeros!")
    cantidad = input("Ingrese un numero: ")

# Convertimos
cantidad = int(cantidad)

# Arranca la lista vacia
nombres = []

# Variable contador = 0
contador = 0

# Este bucle generara el ingreso de los nombres segun cantidad
while contador < cantidad:
    # Variable name para que sea auxiliar para guardar ingresos
    name = input("Ingrese un nombre: ")
    # el append siempre agrega al final de las listas
    nombres.append(name)
    # variable contador(de vueltas) se usara para comparar con cantidad
    contador = contador + 1

print(nombres)

for i in nombres:
    print(i)

'''
EJERCICIO 15
. Escriba un programa que permita crear una lista de nombres
(como en el ejercicio anterior). Luego pida un nombre y que
diga cuántas veces aparece ese nombre en la lista.
'''
# Ingreso por teclado de la cantidad de nombres
cantidad = input("¿Cuantos nombres desea ingresar?: ")

# Chequeamos que sea un numero
while cantidad.isdecimal() == False:
    print("¡Error. Solo numeros!")
    cantidad = input("Ingrese un numero: ")

# Convertimos
cantidad = int(cantidad)

# Arranca la lista vacia
nombres = []

# Variable contador = 0
contador = 0

# Este bucle generara el ingreso de los nombres segun cantidad
while contador < cantidad:
    # Variable name para que sea auxiliar para guardar ingresos
    name = input("Ingrese un nombre: ")
    # el append siempre agrega al final de las listas
    nombres.append(name)
    # variable contador(de vueltas) se usara para comparar con cantidad
    contador = contador + 1

print("*** ATENCION ***")

# Ahora tenemos que pedir el nombre que queremos ver cuantas veces aparece
dato = input("Ingrese nombre para verificar: ")

# Veces sera una variable donde contaremos las veces que aparece ese 'x' nombre
veces = 0

# con el for recorremos la lista nombres (n es la auxiliar del for)
for n in nombres:
    # Este if verifica si hay coincidencia
    if n == dato:
        # incrementamos la variable veces si hay coincidencia
        veces = veces + 1

    # Al terminar el for sabremos si hubo repeticiones

print(dato + " aparece " + str(veces) + " veces")

'''
EJERCICIO 16. Crea una función que calcule el factorial de un
número pasado por parámetro(argumento). Y
‘muestre’ el resultado.
'''


def factorial(numero):
    num = 1
    for n in range(1, numero + 1, 1):
        num = num * n
    print(num)


factorial(6)

'''
EJERCICIO 17. Escribir un programa que cree un diccionario vacío y lo
vaya llenando con personas. Donde el nombre(str) será la
clave(el key) y el valor(value) la edad(int).
El programa debe estar acompañado de un menú:
Menú:
A) Agregar.
B) Mostrar el más chico.
C) Mostrar el más grande.
D) Salir.
La opción de agregar inserta a una persona. Mostrar el más
chico, nos debería mostrar el nombre de la persona más chica,
y viceversa el de mostrar el más grande. Con la opción 4
deberíamos salir del programa.
'''


def verificar(texto):
    while texto == "":
        print("Error")
        texto = input("Ingrese nuevamente: ")
    return texto


def convertir(dato):
    while dato.isdecimal() == False:
        print("¡Error!")
        dato = input("Ingrese nuevamente: ")
    return int(dato)


personas = {}

while True:
    print("Menú:")
    print("1 - Agregar")
    print("2 - Mostrar el más chico")
    print("3 - Mostrar el más grande")
    print("4 - Salir")
    opcion = input(">>> ")
    if opcion == "1":
        nombre = input("Ingrese un nombre: ")
        nombre = verificar(nombre)
        edad = input("Ingrese una edad: ")
        edad = convertir(edad)
        personas[nombre] = edad
        print("¡Se agrego una persona!")
    elif opcion == "2":
        # El 'truco' consiste en poner el 200 para
        # que arranque aux_edad con un número grande
        # y siempre tome el primero del diccionario.
        aux_edad = 200
        # aux_nombre la dejamos vacio
        aux_nombre = ""
        for n in personas:
            if personas[n] < aux_edad:
                aux_edad = personas[n]
                aux_nombre = n
        print(aux_nombre + " es la persona más chica")
    elif opcion == "3":
        # El 'truco' consiste en poner el 0 para
        # que arranque aux_edad con cero
        # y siempre tome el primero del diccionario.
        aux_edad = 0
        # aux_nombre la dejamos vacio
        aux_nombre = ""
        for n in personas:
            if personas[n] > aux_edad:
                aux_edad = personas[n]
                aux_nombre = n
        print(aux_nombre + " es la persona más grande")
    elif opcion == "4":
        print("¡Gracias por utilizar el programa!")
        break
    else:
        print("¡Error de opción!")
