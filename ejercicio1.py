""" Cree una lista de frutas de 7 elementos, y realice un programa que 
muestre el tercer elemento de la lista en la pantalla. """

from tkinter import *

root = Tk()
e = Entry(root)
e.pack()
e.focus_set()

# espacio a modificar

frutas = ["Manzana", "Banana", "Pera", "Frutilla", "Cereza", "Limon", "Coco"]

# espacio a modificar

var = IntVar()
e.config(textvariable=var)
var.set(frutas[2])
mainloop()
