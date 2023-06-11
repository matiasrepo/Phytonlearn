'''
EJERCICIO 21 Este ejercicio consiste en armar una calculadora sencilla
'''


# DESARROLLAMOS  EL PROGRAMA

def convertir(dato):
    if dato.isdecimal():
        dato = int(dato)
    else:
        dato = "error"
    return dato


def sumar():
    cajatres.delete(0, tk.END)
    a = cajauno.get()
    a = convertir(a)
    b = cajados.get()
    b = convertir(b)
    if a != "error" and b != "error":
        c = a + b
    else:
        c = "error"
    cajatres.insert(0, c)


def restar():
    cajatres.delete(0, tk.END)
    a = cajauno.get()
    a = convertir(a)
    b = cajados.get()
    b = convertir(b)
    if a != "error" and b != "error":
        c = a - b
    else:
        c = "error"
    cajatres.insert(0, c)


def multiplicar():
    cajatres.delete(0, tk.END)
    a = cajauno.get()
    a = convertir(a)
    b = cajados.get()
    b = convertir(b)
    if a != "error" and b != "error":
        c = a * b
    else:
        c = "error"
    cajatres.insert(0, c)


def dividir():
    cajatres.delete(0, tk.END)
    a = cajauno.get()
    a = convertir(a)
    b = cajados.get()
    b = convertir(b)
    if a != "error" and b != "error" and b != 0:
        c = a / b
    else:
        c = "error"
    cajatres.insert(0, c)
