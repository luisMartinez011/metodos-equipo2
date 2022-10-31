from cProfile import label
from tkinter import messagebox, ttk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk


""" Es la declaracion de enseñar la seleccion"""
def show_selection():
    # Obtener la opción seleccionada.
    selection = combo.get()
    messagebox.showinfo(
        message=f"La opción seleccionada es: {selection}",
        title="Selección"
    )

main_window = tk.Tk()

""" Es el tamaño del menu """
main_window.config(width=600, height=200) 

""" Es el nombre de la aplicacion en la ventana """
main_window.title("Aplicacion de metodos numericos")

""" codigo para colocar texto, necesita colocar main_window para referenciar el menu principal de la funcion principal """
etiqueta = Label(main_window, text="En esta aplicacion podras poner en practica tu habilidad para resolver cualquier metodo numerico")
etiqueta2 = Label(main_window, text="Selecciona el metodo de las opciones")
combo = ttk.Combobox(
    state="readonly",
    values=["Newton adelante", "Lagrange", "NewtonAtras", "Interpolacion", "PuntoFijo"]
)

etiqueta.place(x=10, y=10)
etiqueta2.place(x=170, y=50)
combo.place(x=10, y=50)
button = ttk.Button(text="Escoger selección", command=show_selection)
button.place(x=10, y=80)


main_window.mainloop()