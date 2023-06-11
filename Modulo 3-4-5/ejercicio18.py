'''
EJERCICIO 18 Crear una aplicación de escritorio con dos cajas de
texto y un botón, de modo que al presionarlo se
imprima en pantalla la suma de los dos números
ingresados en las primeras. La disposición de los
controles y el tamaño de la ventana son a elección
del alumno.
'''

import tkinter as tk


###################################################

def convertir(dato):
    if dato.isdecimal():
        dato = int(dato)
    else:
        dato = "error"
    return dato


def sumar():
    # Obtenemos el texto ingresado por el usuario en cada caja
    # y lo convertimos a un entero para poder sumarlo.
    a = caja_a.get()
    a = convertir(a)
    b = caja_b.get()
    b = convertir(b)
    if a != "error" and b != "error":
        print(a + b)
    else:
        print("No se puede realizar")


###################################################
import tkinter as tk

ventana = tk.Tk()
ventana.config(width=250, height=200)
ventana.title("Ejemplo")

caja_a = tk.Entry()
caja_a.place(x=20, y=20, width=50, height=25)

caja_b = tk.Entry()
caja_b.place(x=20, y=60, width=50, height=25)

boton = tk.Button(text="Sumar", command=sumar)
boton.place(x=20, y=100)

ventana.mainloop()



'''
EJERCICIO 19 Escribir una función que sirva para multiplicar cada elemento
de una lista numérica por un valor. Y devuelva la nueva lista con
cada elemento en su respectiva posición, pero ya multiplicado.
'''
def multiplicar(lista,valor):
    nueva = []
    for n in lista:
        resultado = n * valor
        nueva.append(resultado)
    return nueva


############################

#Valores de ejemplo

numeros = [10,5,3,20]
m = 5

print(multiplicar(numeros,m))
