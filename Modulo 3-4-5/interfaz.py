import tkinter as tk


def boton_presionado():
    print("Hola mundo")


def boton_boton():
    print(caja.get())


ventana = tk.Tk()

ventana.config(width=400, height=300)
ventana.title("Este es el titulo de la ventana")

boton = tk.Button(text="Boton", command=boton_boton)
boton.place(x=20, y=50, width=100, height=30)

etiqueta = tk.Label(text="Ingresa tu nombre:")
etiqueta.place(x=20, y=90)

caja = tk.Entry()
caja.place(x=20, y=120, width=200, height=25)

boton = tk.Button(text="Hola Mundo", command=boton_presionado)
boton.place(x=20, y=200, width=100, height=30)

ventana.mainloop()
