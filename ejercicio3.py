""" Cree un diccionario con las claves: identificador, nombre, apellido y
teléfono. Realice un programa que a partir del diccionario creado
retome en una oracion: El número de elementos del diccionario y las
claves del diccionario. """

from tkinter import *

root = Tk()
e = Entry(root)
e.pack()
e.focus_set()

# espacio a modificar

sujeto = {
    "identificador": "1",
    "nombre": "Cristian",
    "apellido": "Rita",
    "telefono": "479-029",
}

texto = (
    "Este diccionario contiene "
    + str(len(sujeto))
    + " elementos, cuyas claves son: "
    + ", ".join(sujeto.keys())
    + "."
)

# espacio a modificar

var = IntVar()
e.config(textvariable=var)
var.set(texto)
mainloop()

""" Pregunta: ¿Cree que epara guardar y recuperar informacion es mejor un diccionario o una lista?"
Respuesta: En lo que respecta a una base de datos, como la de ejercicio es evidente que el
diccionario es la mejor opcion, ya que la busqueda de los elementos esta ligado a las claves.
Pero en cuanto a las listas, creo que tienen la ventaja de ser mas simples, ante datos menos
complejos, y con una relacion entre ellos, como frutas, animales, paises.
 """
