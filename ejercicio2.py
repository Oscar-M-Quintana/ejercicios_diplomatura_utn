""" Cree una lista de frutas de 2 elementos, y realice un programa con tkinder
que muestre una oración conteniendo los dos elemetos de la lista
concatenándose con texto para formar una oración con sentido."""

from tkinter import *

root = Tk()
e = Entry(root)
e.pack()
e.focus_set()

# espacio a modificar
frutas = ["cereza", "mora"]
C = "La " + frutas[0] + " y " + "la " + frutas[1] + " son frutos rojos."
# espacio a modificar

var = IntVar()
e.config(textvariable=var)
var.set(C)
mainloop()
