'''
EJERCICIO 21 Al ejercicio que está en el módulo 4, el de generar un
numero aleatorio de 1 al 6 (simulábamos el arrojar un
dado), ahora debemos pasarlo a una aplicación de
escritorio. La vista de la aplicación debería ser similar a
la figura 1.
En la caja deberían de aparecer los resultados aleatorios
cada vez que se presiona el botón. Antes de mostrar los
resultados se limpia la caja, dejando el mismo resultado
hasta que se vuelve a pulsar.
Ayuda
Si tenemos una “caja” generada con tk.Entry()
● caja.delete(0,tk.END) llamada desde cualquier función
limpia la “caja”.
● caja.insert(0,variable) llamada desde cualquier función
inserta el valor de variable en la “caja”.
'''

import tkinter as tk
import random


####################################
def arrojar():
    caja.delete(0, tk.END)
    valor = random.randint(1, 6)
    caja.insert(0, valor)


####################################

ventana = tk.Tk()
ventana.config(width=220, height=200)
ventana.title("Dado 2.0")
boton = tk.Button(text="Arrojar el dado", command=arrojar)
boton.place(x=60, y=40, width=100, height=50)
etq = tk.Label(text="Valor: ")
etq.place(x=60, y=110)
caja = tk.Entry()
caja.place(x=60, y=140, width=100)
ventana.mainloop()
