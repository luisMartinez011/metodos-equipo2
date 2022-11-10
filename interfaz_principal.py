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
            ventanita, text=f"Metodo numerico ({metodo.methodName()})", bg="green", fg="black")
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
    vprincipal.geometry('600x600')
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

    # Mucho ojo con esta funcion Interfaz_del_Metodo(metodos.Interpolacion_lineal) tienen que cambiar el parametro
    # dependiendo de que metodo se maneje ya que ahorita todos son iguales
    # Ejemplo Interfaz_del_Metodo(metodos.nombre de la clase del metodo)
    button = tk.Button(vprincipal, text="Metodo numerico #1: Interpolacion",
                       command=lambda: [Interfaz_del_Metodo(metodos.Interpolacion_lineal), vprincipal.destroy()])
    button.place(x=10, y=70)
    button = tk.Button(vprincipal, text="Metodo numerico #2: Newton Adelante",
                       command=lambda: [Interfaz_del_Metodo(metodos.Newton_hacia_adelante), vprincipal.destroy()])
    button.place(x=10, y=95)
    button = tk.Button(vprincipal, text="Metodo numerico #3: Newton Atras",
                       command=lambda: [Interfaz_del_Metodo(metodos.Newton_hacia_atras), vprincipal.destroy()])
    button.place(x=10, y=120)
    button = tk.Button(vprincipal, text="Metodo numerico #4: Lagrange",
                       command=lambda: [Interfaz_del_Metodo(metodos.Interpolacion_lineal), vprincipal.destroy()])
    button.place(x=10, y=145)
    button = tk.Button(vprincipal, text="Metodo numerico #5: Newton con diferencias Divididas",
                       command=lambda: [Interfaz_del_Metodo(metodos.Interpolacion_lineal), vprincipal.destroy()])
    button.place(x=10, y=170)
    button = tk.Button(vprincipal, text="Metodo numerico #6: Metodo de la bisectriz",
                       command=lambda: [Interfaz_del_Metodo(metodos.Interpolacion_lineal), vprincipal.destroy()])
    button.place(x=10, y=195)
    button = tk.Button(vprincipal, text="Metodo numerico #7: Punto fijo",
                       command=lambda: [Interfaz_del_Metodo(metodos.Punto_Fijo), vprincipal.destroy()])
    button.place(x=10, y=220)
    button = tk.Button(vprincipal, text="Metodo numerico #8: Rhapson",
                       command=lambda: [Interfaz_del_Metodo(metodos.Interpolacion_lineal), vprincipal.destroy()])
    button.place(x=10, y=245)
    button = tk.Button(vprincipal, text="Metodo numerico #9: Falsa posicion",
                       command=lambda: [Interfaz_del_Metodo(metodos.Interpolacion_lineal), vprincipal.destroy()])
    button.place(x=10, y=270)
    button = tk.Button(vprincipal, text="Metodo numerico #10: Secante",
                       command=lambda: [Interfaz_del_Metodo(metodos.Interpolacion_lineal), vprincipal.destroy()])
    button.place(x=10, y=295)
    button = tk.Button(vprincipal, text="Metodo numerico #11: Gauss Seidel",
                       command=lambda: [Interfaz_del_Metodo(metodos.Interpolacion_lineal), vprincipal.destroy()])
    button.place(x=10, y=320)
    button = tk.Button(vprincipal, text="Metodo numerico #12: Jacobi",
                       command=lambda: [Interfaz_del_Metodo(metodos.Interpolacion_lineal), vprincipal.destroy()])
    button.place(x=10, y=345)
    button = tk.Button(vprincipal, text="Metodo numerico #13: Linea recta",
                       command=lambda: [Interfaz_del_Metodo(metodos.Interpolacion_lineal), vprincipal.destroy()])
    button.place(x=10, y=370)
    button = tk.Button(vprincipal, text="Metodo numerico #14: Linea recta Cuadratica",
                       command=lambda: [Interfaz_del_Metodo(metodos.Interpolacion_lineal), vprincipal.destroy()])
    button.place(x=10, y=395)
    button = tk.Button(vprincipal, text="Metodo numerico #15: Linea recta Cubica",
                       command=lambda: [Interfaz_del_Metodo(metodos.Interpolacion_lineal), vprincipal.destroy()])
    button.place(x=10, y=420)
    button = tk.Button(vprincipal, text="Metodo numerico #16: Lineal con funcion",
                       command=lambda: [Interfaz_del_Metodo(metodos.Interpolacion_lineal), vprincipal.destroy()])
    button.place(x=10, y=445)
    button = tk.Button(vprincipal, text="Metodo numerico #17: Lineal con funcion Matriz cuadratica",
                       command=lambda: [Interfaz_del_Metodo(metodos.Interpolacion_lineal), vprincipal.destroy()])
    button.place(x=10, y=470)
    button = tk.Button(vprincipal, text="Metodo numerico #18: Integracion - Regla trapezoidal",
                       command=lambda: [Interfaz_del_Metodo(metodos.Interpolacion_lineal), vprincipal.destroy()])
    button.place(x=10, y=495)
    button = tk.Button(vprincipal, text="Metodo numerico #19: Integracion - Regla 1/3 Simpson",
                       command=lambda: [Interfaz_del_Metodo(metodos.Interpolacion_lineal), vprincipal.destroy()])
    button.place(x=10, y=520)
    button = tk.Button(vprincipal, text="Metodo numerico #20: Integracion - Regla 3/8 Simpson",
                       command=lambda: [Interfaz_del_Metodo(metodos.Interpolacion_lineal), vprincipal.destroy()])
    button.place(x=10, y=545)


# Aqui es llamada la funcion principal por primera vez
ventana1 = principal()
main_window.mainloop()
