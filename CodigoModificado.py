from ast import Index
from cProfile import label
from multiprocessing.sharedctypes import Value
from tkinter import messagebox, ttk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from unittest import main


#Variable global para que todas las funciones puedan manejar todas las ventanas
main_window = tk.Tk()

    
 # VENTANAS DE INICIO DE CADA METODO - Aporte: Moises Gomez 2 nov 2022
def M0():
   
    main_window.withdraw()
    ventanita=tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1=tk.Label(ventanita,text=f"Metodo numerico (Metodo numerico)", bg="green", fg= "black")
    titulo1.pack(padx=5, pady=5,ipadx=5,ipady=5,fill=tk.X)
   
    Desc=tk.Label(ventanita,text=f"En este Metodo puedes asignar valores a las variables" , fg= "black")
    Desc.pack(padx=5, pady=20,ipadx=5,ipady=5,fill=tk.X)

#Estos botones son los que redirijen hacia la ventana de menu funcionan de igual manera que el boton de ventana principal
    botonMenu=tk.Button(ventanita,text="Menu principal",command=lambda: [principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)

def M1():
    
    main_window.withdraw()
    ventanita=tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1=tk.Label(ventanita,text=f"Metodo numerico (Metodo numerico)", bg="Red", fg= "black")
    titulo1.pack(padx=5, pady=5,ipadx=5,ipady=5,fill=tk.X)
   
    Desc=tk.Label(ventanita,text=f"En este Metodo No puedes asignar valores a las variables, se generaran de forma aleatoria" , fg= "black")
    Desc.pack(padx=5, pady=20,ipadx=5,ipady=5,fill=tk.X)

    botonMenu=tk.Button(ventanita,text="Menu principal",command=lambda: [principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)
def M2():
    
    main_window.withdraw()
    ventanita=tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1=tk.Label(ventanita,text=f"Metodo numerico (Metodo numerico)", bg="green", fg= "black")
    titulo1.pack(padx=5, pady=5,ipadx=5,ipady=5,fill=tk.X)
   
    Desc=tk.Label(ventanita,text=f"En este Metodo puedes asignar valores a las variables" , fg= "black")
    Desc.pack(padx=5, pady=20,ipadx=5,ipady=5,fill=tk.X)

    botonMenu=tk.Button(ventanita,text="Menu principal",command=lambda: [principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)

def M3():
   
    main_window.withdraw()
    ventanita=tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1=tk.Label(ventanita,text=f"Metodo numerico (Metodo numerico) ", bg="green", fg= "black")
    titulo1.pack(padx=5, pady=5,ipadx=5,ipady=5,fill=tk.X)
   
    Desc=tk.Label(ventanita,text=f"En este Metodo puedes asignar valores a las variables" , fg= "black")
    Desc.pack(padx=5, pady=20,ipadx=5,ipady=5,fill=tk.X)

    botonMenu=tk.Button(ventanita,text="Menu principal",command=lambda: [principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)

def M4():
   
    main_window.withdraw()
    ventanita=tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1=tk.Label(ventanita,text=f"Metodo numerico (Metodo numerico)", bg="green", fg= "black")
    titulo1.pack(padx=5, pady=5,ipadx=5,ipady=5,fill=tk.X)
   
    Desc=tk.Label(ventanita,text=f"En este Metodo puedes asignar valores a las variables" , fg= "black")
    Desc.pack(padx=5, pady=20,ipadx=5,ipady=5,fill=tk.X)

    botonMenu=tk.Button(ventanita,text="Menu principal",command=lambda: [principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)

# VENTANAS DE OPERACIONES POR CADA METODO - Aporte: Moises Gomez 2 nov 2022



# COfuncion DE CERRAR VENTANA - Aporte: Moises Gomez 2 nov 2022
def CerrarVentana():
    main_window.destroy()


 # CODIGO Y CARACTERISTICAS DE LA VENTANA PRINCIPAL - Aporte: Moises Gomez 2 nov 2022"

#SE CREO COMO FUNCION LA VENTANA PRINCIPAL PARA QUE PUEDA SER LLAMADA DESDE OTRAS FUNCIONES
def principal():
    
    main_window.withdraw()
    vprincipal = tk.Toplevel()
    vprincipal.geometry('600x600')
    vprincipal.configure()
    """ Es el nombre de la aplicacion en la ventana """
    vprincipal.title("Aplicacion de metodos numericos")
    """ codigo para colocar texto, necesita colocar main_window para referenciar el menu principal de la funcion principal """
    etiqueta = Label(vprincipal, text="En esta aplicacion podras poner en practica tu habilidad para resolver cualquier metodo numerico")
    etiqueta2 = Label(vprincipal, text="Selecciona el metodo de las opciones")
    etiqueta.pack(padx=5, pady=5,ipadx=5,ipady=5,fill=tk.X)
    etiqueta2.pack(padx=5, pady=5,ipadx=5,ipady=5,fill=tk.X)
    #Lambda es utilizado para poder combinar dos funciones dentro de un solo boton, este metodo abre la ventana del metodo 0 y cierra la ventana del menu principal
    button =tk.Button(vprincipal,text="Metodo numerico #1", command=lambda:[M0(), vprincipal.destroy()])
    button.pack(padx=30, pady=30, ipadx=5, ipady=5)
    button =tk.Button(vprincipal,text="Metodo numerico #2", command=lambda:[M1(), vprincipal.destroy()])
    button.pack(padx=30, pady=31, ipadx=5, ipady=5)
    button =tk.Button(vprincipal,text="Metodo numerico #3", command=lambda:[M2(), vprincipal.destroy()])
    button.pack(padx=30, pady=32, ipadx=5, ipady=5)
    button =tk.Button(vprincipal,text="Metodo numerico #4", command=lambda:[M3(), vprincipal.destroy()])
    button.pack(padx=30, pady=33, ipadx=5, ipady=5)

#Aqui es llamada la funcion principal por primera vez
ventana1 = principal()
