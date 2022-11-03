from ast import Index
from cProfile import label
from multiprocessing.sharedctypes import Value
import tkinter as tk
from tkinter import *
from unittest import main
from interpolacion_lineal import interpolacion

# Variable global para que todas las funciones puedan manejar todas las ventanas
main_window = tk.Tk()

# VENTANAS DE INICIO DE CADA METODO - Aporte: Moises Gomez 2 nov 2022


def M0():

    main_window.withdraw()
    ventanita = tk.Toplevel()
    # ventanita.geometry('600x400')
    ventanita.geometry('800x600')
    ventanita.configure()

    def header():
        titulo1 = tk.Label(
            ventanita, text=f"Metodo numerico (Interpolacion)", bg="green", fg="black")
        titulo1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

        Desc = tk.Label(
            ventanita, text=f"En este Metodo puedes asignar valores a las variables",
            fg="black")
        Desc.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    # Return the problem solved
    def returnResult():

        # interpolacion(2,5,4)
        metodo = interpolacion(int(A.get()), int(B.get()), int(X.get()))

        resultado = tk.Label(
            ventanita, text=f"El resultado es de: {metodo.solve()}",
            fg="black")
        resultado.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

        margenDeError = tk.Label(
            ventanita, text=f"El margen de error es de: {metodo.error()}",
            fg="black")
        margenDeError.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    # Form to get the values
    def getValues():
        L1 = Label(ventanita, text="A")
        L1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X, side=LEFT)
        A = Entry(ventanita, bd=5)
        A.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X, side=LEFT)

        L2 = Label(ventanita, text="B")
        L2.pack(side=LEFT)
        B = Entry(ventanita, bd=5)
        B.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X, side=LEFT)

        L3 = Label(ventanita, text="X")
        L3.pack(side=LEFT)
        X = Entry(ventanita, bd=5)
        X.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X, side=LEFT)

        boton1 = Button(ventanita, text="Envíar", command=returnResult)
        boton1.pack(padx=5, pady=5, ipadx=5, ipady=5,
                    fill=tk.X, side=RIGHT)

    header()
    getValues()
# Estos botones son los que redirijen hacia la ventana de menu funcionan de igual manera que el boton de ventana principal
    botonMenu = tk.Button(ventanita, text="Menu principal", command=lambda: [
                          principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1, side=BOTTOM)
    botonCerrar = tk.Button(
        ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.pack(padx=50, pady=10, side=BOTTOM)


def M1():

    main_window.withdraw()
    ventanita = tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1 = tk.Label(
        ventanita, text=f"Metodo numerico (Newton Adelante)", bg="Red", fg="black")
    titulo1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    Desc = tk.Label(
        ventanita, text=f"En este Metodo No puedes asignar valores a las variables, se generaran de forma aleatoria", fg="black")
    Desc.pack(padx=5, pady=20, ipadx=5, ipady=5, fill=tk.X)

    botonMenu = tk.Button(ventanita, text="Menu principal", command=lambda: [
                          principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(
        ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)


def M2():

    main_window.withdraw()
    ventanita = tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1 = tk.Label(
        ventanita, text=f"Metodo numerico (Newton Atras)", bg="blue", fg="black")
    titulo1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    Desc = tk.Label(
        ventanita, text=f"En este Metodo puedes asignar valores a las variables", fg="black")
    Desc.pack(padx=5, pady=20, ipadx=5, ipady=5, fill=tk.X)

    botonMenu = tk.Button(ventanita, text="Menu principal", command=lambda: [
                          principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(
        ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)


def M3():

    main_window.withdraw()
    ventanita = tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1 = tk.Label(
        ventanita, text=f"Metodo numerico (Lagrange) ", bg="gray", fg="black")
    titulo1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    Desc = tk.Label(
        ventanita, text=f"En este Metodo puedes asignar valores a las variables", fg="black")
    Desc.pack(padx=5, pady=20, ipadx=5, ipady=5, fill=tk.X)

    botonMenu = tk.Button(ventanita, text="Menu principal", command=lambda: [
                          principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(
        ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)


def M4():

    main_window.withdraw()
    ventanita = tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1 = tk.Label(
        ventanita, text=f"Metodo numerico (Newton con diferencias Divididas)", bg="pink", fg="black")
    titulo1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    Desc = tk.Label(
        ventanita, text=f"En este Metodo puedes asignar valores a las variables", fg="black")
    Desc.pack(padx=5, pady=20, ipadx=5, ipady=5, fill=tk.X)

    botonMenu = tk.Button(ventanita, text="Menu principal", command=lambda: [
                          principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(
        ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)


def M5():

    main_window.withdraw()
    ventanita = tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1 = tk.Label(
        ventanita, text=f"Metodo numerico (Metodo de la bisectriz)", bg="pink", fg="black")
    titulo1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    Desc = tk.Label(
        ventanita, text=f"En este Metodo puedes asignar valores a las variables", fg="black")
    Desc.pack(padx=5, pady=20, ipadx=5, ipady=5, fill=tk.X)

    botonMenu = tk.Button(ventanita, text="Menu principal", command=lambda: [
                          principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(
        ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)


def M6():

    main_window.withdraw()
    ventanita = tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1 = tk.Label(
        ventanita, text=f"Metodo numerico (Punto fijo)", bg="pink", fg="black")
    titulo1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    Desc = tk.Label(
        ventanita, text=f"En este Metodo puedes asignar valores a las variables", fg="black")
    Desc.pack(padx=5, pady=20, ipadx=5, ipady=5, fill=tk.X)

    botonMenu = tk.Button(ventanita, text="Menu principal", command=lambda: [
                          principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(
        ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)


def M7():

    main_window.withdraw()
    ventanita = tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1 = tk.Label(
        ventanita, text=f"Metodo numerico (Rhapson)", bg="pink", fg="black")
    titulo1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    Desc = tk.Label(
        ventanita, text=f"En este Metodo puedes asignar valores a las variables", fg="black")
    Desc.pack(padx=5, pady=20, ipadx=5, ipady=5, fill=tk.X)

    botonMenu = tk.Button(ventanita, text="Menu principal", command=lambda: [
                          principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(
        ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)


def M8():

    main_window.withdraw()
    ventanita = tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1 = tk.Label(
        ventanita, text=f"Metodo numerico (Falsa posicion)", bg="pink", fg="black")
    titulo1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    Desc = tk.Label(
        ventanita, text=f"En este Metodo puedes asignar valores a las variables", fg="black")
    Desc.pack(padx=5, pady=20, ipadx=5, ipady=5, fill=tk.X)

    botonMenu = tk.Button(ventanita, text="Menu principal", command=lambda: [
                          principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(
        ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)


def M9():

    main_window.withdraw()
    ventanita = tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1 = tk.Label(
        ventanita, text=f"Metodo numerico (Secante)", bg="pink", fg="black")
    titulo1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    Desc = tk.Label(
        ventanita, text=f"En este Metodo puedes asignar valores a las variables", fg="black")
    Desc.pack(padx=5, pady=20, ipadx=5, ipady=5, fill=tk.X)

    botonMenu = tk.Button(ventanita, text="Menu principal", command=lambda: [
                          principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(
        ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)


def M10():

    main_window.withdraw()
    ventanita = tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1 = tk.Label(
        ventanita, text=f"Metodo numerico (Gauss Seidel)", bg="pink", fg="black")
    titulo1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    Desc = tk.Label(
        ventanita, text=f"En este Metodo puedes asignar valores a las variables", fg="black")
    Desc.pack(padx=5, pady=20, ipadx=5, ipady=5, fill=tk.X)

    botonMenu = tk.Button(ventanita, text="Menu principal", command=lambda: [
                          principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(
        ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)


def M11():

    main_window.withdraw()
    ventanita = tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1 = tk.Label(
        ventanita, text=f"Metodo numerico (Jacobi)", bg="pink", fg="black")
    titulo1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    Desc = tk.Label(
        ventanita, text=f"En este Metodo puedes asignar valores a las variables", fg="black")
    Desc.pack(padx=5, pady=20, ipadx=5, ipady=5, fill=tk.X)

    botonMenu = tk.Button(ventanita, text="Menu principal", command=lambda: [
                          principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(
        ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)


def M12():

    main_window.withdraw()
    ventanita = tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1 = tk.Label(
        ventanita, text=f"Metodo numerico (Linea recta)", bg="pink", fg="black")
    titulo1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    Desc = tk.Label(
        ventanita, text=f"En este Metodo puedes asignar valores a las variables", fg="black")
    Desc.pack(padx=5, pady=20, ipadx=5, ipady=5, fill=tk.X)

    botonMenu = tk.Button(ventanita, text="Menu principal", command=lambda: [
                          principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(
        ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)


def M13():

    main_window.withdraw()
    ventanita = tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1 = tk.Label(
        ventanita, text=f"Metodo numerico (Linea recta Cuadratica)", bg="pink", fg="black")
    titulo1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    Desc = tk.Label(
        ventanita, text=f"En este Metodo puedes asignar valores a las variables", fg="black")
    Desc.pack(padx=5, pady=20, ipadx=5, ipady=5, fill=tk.X)

    botonMenu = tk.Button(ventanita, text="Menu principal", command=lambda: [
                          principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(
        ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)


def M14():

    main_window.withdraw()
    ventanita = tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1 = tk.Label(
        ventanita, text=f"Metodo numerico (Linea recta Cubica)", bg="pink", fg="black")
    titulo1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    Desc = tk.Label(
        ventanita, text=f"En este Metodo puedes asignar valores a las variables", fg="black")
    Desc.pack(padx=5, pady=20, ipadx=5, ipady=5, fill=tk.X)

    botonMenu = tk.Button(ventanita, text="Menu principal", command=lambda: [
                          principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(
        ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)


def M15():

    main_window.withdraw()
    ventanita = tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1 = tk.Label(
        ventanita, text=f"Metodo numerico (Lineal con funcion)", bg="pink", fg="black")
    titulo1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    Desc = tk.Label(
        ventanita, text=f"En este Metodo puedes asignar valores a las variables", fg="black")
    Desc.pack(padx=5, pady=20, ipadx=5, ipady=5, fill=tk.X)

    botonMenu = tk.Button(ventanita, text="Menu principal", command=lambda: [
                          principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(
        ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)


def M16():

    main_window.withdraw()
    ventanita = tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1 = tk.Label(
        ventanita, text=f"Metodo numerico (Lineal con funcion Matriz cuadratica)", bg="pink", fg="black")
    titulo1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    Desc = tk.Label(
        ventanita, text=f"En este Metodo puedes asignar valores a las variables", fg="black")
    Desc.pack(padx=5, pady=20, ipadx=5, ipady=5, fill=tk.X)

    botonMenu = tk.Button(ventanita, text="Menu principal", command=lambda: [
                          principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(
        ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)


def M17():

    main_window.withdraw()
    ventanita = tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1 = tk.Label(
        ventanita, text=f"Metodo numerico (Integracion - Regla trapezoidal)", bg="pink", fg="black")
    titulo1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    Desc = tk.Label(
        ventanita, text=f"En este Metodo puedes asignar valores a las variables", fg="black")
    Desc.pack(padx=5, pady=20, ipadx=5, ipady=5, fill=tk.X)

    botonMenu = tk.Button(ventanita, text="Menu principal", command=lambda: [
                          principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(
        ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)


def M18():

    main_window.withdraw()
    ventanita = tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1 = tk.Label(
        ventanita, text=f"Metodo numerico (Integracion - Regla 1/3 Simpson)", bg="pink", fg="black")
    titulo1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    Desc = tk.Label(
        ventanita, text=f"En este Metodo puedes asignar valores a las variables", fg="black")
    Desc.pack(padx=5, pady=20, ipadx=5, ipady=5, fill=tk.X)

    botonMenu = tk.Button(ventanita, text="Menu principal", command=lambda: [
                          principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(
        ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)


def M19():

    main_window.withdraw()
    ventanita = tk.Toplevel()
    ventanita.geometry('600x400')
    ventanita.configure()
    titulo1 = tk.Label(
        ventanita, text=f"Metodo numerico (Integracion - Regla 3/8 Simpson)", bg="pink", fg="black")
    titulo1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    Desc = tk.Label(
        ventanita, text=f"En este Metodo puedes asignar valores a las variables", fg="black")
    Desc.pack(padx=5, pady=20, ipadx=5, ipady=5, fill=tk.X)

    botonMenu = tk.Button(ventanita, text="Menu principal", command=lambda: [
                          principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(
        ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.place(x=120, y=122)


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
    button = tk.Button(vprincipal, text="Metodo numerico #1: Interpolacion",
                       command=lambda: [M0(), vprincipal.destroy()])
    button.place(x=10, y=70)
    button = tk.Button(vprincipal, text="Metodo numerico #2: Newton Adelante",
                       command=lambda: [M1(), vprincipal.destroy()])
    button.place(x=10, y=95)
    button = tk.Button(vprincipal, text="Metodo numerico #3: Newton Atras",
                       command=lambda: [M2(), vprincipal.destroy()])
    button.place(x=10, y=120)
    button = tk.Button(vprincipal, text="Metodo numerico #4: Lagrange",
                       command=lambda: [M3(), vprincipal.destroy()])
    button.place(x=10, y=145)
    button = tk.Button(vprincipal, text="Metodo numerico #5: Newton con diferencias Divididas",
                       command=lambda: [M4(), vprincipal.destroy()])
    button.place(x=10, y=170)
    button = tk.Button(vprincipal, text="Metodo numerico #6: Metodo de la bisectriz",
                       command=lambda: [M5(), vprincipal.destroy()])
    button.place(x=10, y=195)
    button = tk.Button(vprincipal, text="Metodo numerico #7: Punto fijo",
                       command=lambda: [M6(), vprincipal.destroy()])
    button.place(x=10, y=220)
    button = tk.Button(vprincipal, text="Metodo numerico #8: Rhapson",
                       command=lambda: [M7(), vprincipal.destroy()])
    button.place(x=10, y=245)
    button = tk.Button(vprincipal, text="Metodo numerico #9: Falsa posicion",
                       command=lambda: [M8(), vprincipal.destroy()])
    button.place(x=10, y=270)
    button = tk.Button(vprincipal, text="Metodo numerico #10: Secante",
                       command=lambda: [M9(), vprincipal.destroy()])
    button.place(x=10, y=295)
    button = tk.Button(vprincipal, text="Metodo numerico #11: Gauss Seidel",
                       command=lambda: [M10(), vprincipal.destroy()])
    button.place(x=10, y=320)
    button = tk.Button(vprincipal, text="Metodo numerico #12: Jacobi",
                       command=lambda: [M11(), vprincipal.destroy()])
    button.place(x=10, y=345)
    button = tk.Button(vprincipal, text="Metodo numerico #13: Linea recta",
                       command=lambda: [M12(), vprincipal.destroy()])
    button.place(x=10, y=370)
    button = tk.Button(vprincipal, text="Metodo numerico #14: Linea recta Cuadratica",
                       command=lambda: [M13(), vprincipal.destroy()])
    button.place(x=10, y=395)
    button = tk.Button(vprincipal, text="Metodo numerico #15: Linea recta Cubica",
                       command=lambda: [M14(), vprincipal.destroy()])
    button.place(x=10, y=420)
    button = tk.Button(vprincipal, text="Metodo numerico #16: Lineal con funcion",
                       command=lambda: [M15(), vprincipal.destroy()])
    button.place(x=10, y=445)
    button = tk.Button(vprincipal, text="Metodo numerico #17: Lineal con funcion Matriz cuadratica",
                       command=lambda: [M16(), vprincipal.destroy()])
    button.place(x=10, y=470)
    button = tk.Button(vprincipal, text="Metodo numerico #18: Integracion - Regla trapezoidal",
                       command=lambda: [M17(), vprincipal.destroy()])
    button.place(x=10, y=495)
    button = tk.Button(vprincipal, text="Metodo numerico #19: Integracion - Regla 1/3 Simpson",
                       command=lambda: [M18(), vprincipal.destroy()])
    button.place(x=10, y=520)
    button = tk.Button(vprincipal, text="Metodo numerico #20: Integracion - Regla 3/8 Simpson",
                       command=lambda: [M19(), vprincipal.destroy()])
    button.place(x=10, y=545)


# Aqui es llamada la funcion principal por primera vez
ventana1 = principal()
main_window.mainloop()
