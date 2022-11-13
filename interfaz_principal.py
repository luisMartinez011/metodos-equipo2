from ast import Index
from cProfile import label
from multiprocessing.sharedctypes import Value
import tkinter as tk
from tkinter import *
from unittest import main
from PIL import ImageTk, Image
import metodos

# Variable global para que todas las funciones puedan manejar todas las ventanas
main_window = tk.Tk()

# VENTANAS DE INICIO DE CADA METODO - Aporte: Moises Gomez 2 nov 2022


def Interfaz_del_Metodo(metodo):

    main_window.withdraw()
    ventanita = tk.Toplevel()
    # ventanita.geometry('600x400')
    ventanita.geometry('1000x1000')
    ventanita.configure()

    # Create a countdown timer in the window
    def countdown(count):

        label['text'] = count

        if count > 0:
            # call countdown again after 1000ms (1s)
            ventanita.after(1000, countdown, count-1)

    label = tk.Label(ventanita)
    label.place(x=50, y=150)

    countdown(360)

    # Window´s header

    def header():
        formula = metodo.formula()

        titulo1 = tk.Label(
            ventanita, text=f"({metodo.methodName()})", bg="green", fg="black")
        titulo1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
        Desc = tk.Label(
            ventanita, text=f"En este Metodo puedes asignar valores a las variables",
            fg="black")
        Desc.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
        displayFormula = tk.Label(
            ventanita, text=f"La formula de para resolver este metodo es: {formula}",
            fg="black")
        displayFormula.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    # get the input from user

    # This function solves the problem

    def solvesTheProblem():

        resultado = tk.Label(
            ventanita, text=f"El resultado es de: {metodo.solve()}",
            fg="black")
        resultado.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

        margenDeError = tk.Label(
            ventanita, text=f"El margen de error es de: {metodo.error()}",
            fg="black")
        margenDeError.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    header()
    # this button returns the solution
    returnSolution = Button(ventanita, text="Resolver problema",
                            command=lambda: solvesTheProblem())
    returnSolution.pack(padx=5, pady=5, ipadx=5, ipady=5,
                        fill=tk.X)

#    Estos botones son los que redirijen hacia la ventana de menu funcionan de igual manera que el boton de ventana principal
    botonMenu = tk.Button(ventanita, text="Menu principal", command=lambda: [
                          principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(
        ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.pack(padx=50, pady=10)

    # this function generates a formula image
    def generateImages():
        canvas = Canvas(
            ventanita,
            width=500,
            height=400
        )
        canvas.pack()
        global img
        img = ImageTk.PhotoImage(Image.open(f'metodos/img/{metodo.formula()}'))

        canvas.create_image(
            10,
            10,
            anchor=NW,
            image=img
        )
        Label(
            text=f'width: {img.width()} height: {img.height()}'
        ).pack()

    generateImages()

# VENTANAS DE OPERACIONES POR CADA METODO - Aporte: Moises Gomez 2 nov 2022


# COfuncion DE CERRAR VENTANA - Aporte: Moises Gomez 2 nov 2022
def CerrarVentana():
    main_window.destroy()

 # CODIGO Y CARACTERISTICAS DE LA VENTANA PRINCIPAL - Aporte: Moises Gomez 2 nov 2022"

# SE CREO COMO FUNCION LA VENTANA PRINCIPAL PARA QUE PUEDA SER LLAMADA DESDE OTRAS FUNCIONES


def principal():

    main_window.withdraw()
    vprincipal = tk.Toplevel()
    vprincipal.geometry('900x900')
    vprincipal.configure()
    """ Es el nombre de la aplicacion en la ventana """
    vprincipal.title("Aplicacion de metodos numericos")
    """ codigo para colocar texto, necesita colocar main_window para referenciar el menu principal de la funcion principal """
    etiqueta = Label(
        vprincipal, text="En esta aplicacion podras poner en practica tu habilidad para resolver cualquier metodo numerico")
    etiqueta2 = Label(vprincipal, text="Selecciona el metodo de las opciones")
    etiqueta.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
    etiqueta2.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    # Lambda es utilizado para poder combinar dos funciones dentro de un solo boton, este metodo abre la ventana del metodo 0 y cierra la ventana del menu principal

    infoMetodos = [
        {"nombre": "Interpolacion",
         "metodo": metodos.Interpolacion_lineal,
         "interfaz": Interfaz_del_Metodo},
        {"nombre": "Newton hacia adelante",
            "metodo": metodos.Newton_hacia_adelante, "interfaz": Interfaz_del_Metodo},
        {"nombre": "Newton hacia atras", "metodo": metodos.Newton_hacia_atras,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Lagrange", "metodo": metodos.Lagrange,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Newton con diferencias Divididas",
            "metodo": metodos.Interpolacion_lineal, "interfaz": Interfaz_del_Metodo},
        {"nombre": "Metodo de la bisectriz",
            "metodo": metodos.Interpolacion_lineal, "interfaz": Interfaz_del_Metodo},
        {"nombre": "Punto fijo", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Rhapson", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Falsa posicion", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Secante", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Gauss Seidel", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Jacobi", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Linea recta", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Linea recta cuadratica",
            "metodo": metodos.Interpolacion_lineal, "interfaz": Interfaz_del_Metodo},
        {"nombre": "Linea recta cubica", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Lineal con interfaz", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Lineal con funcion Matriz cuadratica",
            "metodo": metodos.Interpolacion_lineal, "interfaz": Interfaz_del_Metodo},
        {"nombre": "Regla trapezoidal", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Regla 1/3 Simpson", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Regla 3/8 Simpson", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Newton cotes cerradas",
            "metodo": metodos.Interpolacion_lineal, "interfaz": Interfaz_del_Metodo},
        {"nombre": "Montante", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Gauss-Jordan", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Newton cotes abiertas",
            "metodo": metodos.Interpolacion_lineal, "interfaz": Interfaz_del_Metodo},
        {"nombre": "EDO Euler modificado",
            "metodo": metodos.Interpolacion_lineal, "interfaz": Interfaz_del_Metodo},
        {"nombre": "Runge Kutta 2ndo orden",
            "metodo": metodos.Interpolacion_lineal, "interfaz": Interfaz_del_Metodo},
        {"nombre": "Runge Kutta 3er orden",
            "metodo": metodos.Interpolacion_lineal, "interfaz": Interfaz_del_Metodo},
        {"nombre": "", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo}

    ]
    for x in range(29):
        button = tk.Button(vprincipal, text=f"#{x+1}: {infoMetodos[x]['nombre']}",
                           command=lambda: [infoMetodos[0]["interfaz"](infoMetodos[0]["metodo"]), vprincipal.destroy()])
        button.place(x=10, y=(70+25*x))


# Aqui es llamada la funcion principal por primera vez
ventana1 = principal()
main_window.mainloop()
