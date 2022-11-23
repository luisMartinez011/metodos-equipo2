from ast import Index
from cProfile import label
from multiprocessing.sharedctypes import Value
import tkinter as tk
from tkinter import *
from unittest import main
from PIL import ImageTk, Image
from time import strftime
from time import gmtime
from functools import partial
import metodos

# Variable global para que todas las funciones puedan manejar todas las ventanas
main_window = tk.Tk()

# VENTANAS DE INICIO DE CADA METODO - Aporte: Moises Gomez 2 nov 2022


def Interfaz_del_Metodo(metodoElegido):
    metodo = metodoElegido()

    main_window.withdraw()
    ventanita = tk.Toplevel()
    # ventanita.geometry('600x400')
    ventanita.geometry('1000x1000')
    ventanita.configure()

    # Window´s header
    def header():
        titulo1 = tk.Label(
            ventanita, text=f"({metodo.methodName()})", bg="green", fg="black")
        titulo1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
        Desc = tk.Label(
            ventanita, text=f"En este Metodo puedes asignar valores a las variables",
            fg="black")
        Desc.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
        displayFormula = tk.Label(
            ventanita, text=f"La formula de para resolver este metodo es:",
            fg="black")
        displayFormula.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
        generateImages()
        displayFormula = tk.Label(
            ventanita, text=f"El problema es el siguinte:",
            fg="black")
        displayFormula.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
        printProblemImage()

    # this function generates a formula image

    def generateImages():
        canvas = Canvas(
            ventanita,
            width=500,
            height=300
        )
        canvas.pack()
        global formulaIMG
        formulaIMG = ImageTk.PhotoImage(
            Image.open(f'metodos/img/{metodo.formula()}'))

        canvas.create_image(
            10,
            10,
            anchor=NW,
            image=formulaIMG
        )
        Label(
            text=f'width: {formulaIMG.width()} height: {formulaIMG.height()}'
        ).pack()

    # Prints an image of the problem in the window
    def printProblemImage():
        canvas = Canvas(
            ventanita,
            width=500,
            height=100
        )
        canvas.pack()
        global problemIMG
        problemIMG = ImageTk.PhotoImage(
            Image.open(f'metodos/problems_img/{metodo.problemImage}'))

        canvas.create_image(
            10,
            10,
            anchor=NW,
            image=problemIMG
        )
        Label(
            text=f'width: {problemIMG.width()} height: {problemIMG.height()}'
        ).pack()

    header()
    # Create a countdown timer in the window
    global sec
    global doTick
    sec = 300
    doTick = True

    def tick():
        global sec
        if not doTick:
            return
        sec -= 0.1
        sec = round(sec, 1)
        timeLabel.configure(text=sec)
        ventanita.after(100, tick)

    def stop():
        global doTick
        doTick = False

    def start():
        global doTick
        doTick = True
        # Perhaps reset `sec` too?
        tick()

    tituloTemporizador = tk.Label(ventanita, text=f"Temporizador: ")
    tituloTemporizador.place(x=50, y=120)
    timeLabel = tk.Label(ventanita, font=('Helvetica', 25))
    timeLabel.place(x=50, y=150)
    start()

    # This function solves the problem

    def solvesTheProblem(opcionElegida):
        stop()
        solution = metodo.solve()
        selection = ""
        try:
            float(opcionElegida.get())
        except:
            print("")
        else:
            if float(opcionElegida.get()) == metodo.solve():
                selection = "Tu respuesta es correcta "

        try:
            int(opcionElegida.get())
        except:
            print("")
        else:
            if int(opcionElegida.get()) == metodo.solve():
                selection = "Tu respuesta es correcta "

        if len(selection) == 0:
            selection = "Respuesta incorrecta, la respuesta correcta era: " + \
                str(solution)

        resultado = tk.Label(
            ventanita, text=selection,
            fg="black")
        resultado.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

        # margenDeError = tk.Label(
        #     ventanita, text=f"El margen de error es de: {metodo.error()}",
        #     fg="black")
        # margenDeError.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    opcionElegida = StringVar()
    opcionElegida.set("1")
    possibleSolutions = metodo.generatePossibleSolutions()

    # Don´t remove this function, if you remove it, the program isn´t going to work
    def ShowChoice():
        return

    for i in possibleSolutions:
        tk.Radiobutton(ventanita,
                       text=i,
                       padx=20,
                       variable=opcionElegida,
                       command=ShowChoice,
                       value=i).pack(anchor=tk.W)

    # this button returns the solution
    returnSolution = Button(ventanita, text="Resolver problema",
                            command=lambda: solvesTheProblem(opcionElegida))
    returnSolution.pack(padx=5, pady=5, ipadx=5, ipady=5,)

#    Estos botones son los que redirijen hacia la ventana de menu funcionan de igual manera que el boton de ventana principal
    botonMenu = tk.Button(ventanita, text="Menu principal", command=lambda: [
        principal(), ventanita.destroy()])
    botonMenu.pack(padx=50, pady=10, ipadx=1, ipady=1)
    botonCerrar = tk.Button(
        ventanita, text="Cerrar programa", command=CerrarVentana)
    botonCerrar.pack(padx=50, pady=10)


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

    etiquetaM1 = Label(vprincipal, text="Interpolacion")
    etiquetaM1.place(x=10, y=95)
    etiquetaM2 = Label(vprincipal, text="Ecuaciones No lineales")
    etiquetaM2.place(x=300, y=95)
    etiquetaM3 = Label(vprincipal, text="Ecuaciones Lineales")
    etiquetaM3.place(x=600, y=95)
    etiquetaM4 = Label(vprincipal, text="Minimos cuadrados")
    etiquetaM4.place(x=10, y=320)
    etiquetaM5 = Label(vprincipal, text="Integracion")
    etiquetaM5.place(x=300, y=320)
    etiquetaM6 = Label(vprincipal, text="Ecuaciones diferenciales ordinarias")
    etiquetaM6.place(x=600, y=320)
    # Lambda es utilizado para poder combinar dos funciones dentro de un solo boton, este metodo abre la ventana del metodo 0 y cierra la ventana del menu principal


# una segunda funcion for porque ya noi caben los botones y se ve  feo
    infoMetodos1 = [
        {"nombre": "Interpolacion", "metodo": metodos.Interpolacion_lineal,
         "interfaz": Interfaz_del_Metodo},
        {"nombre": "Newton hacia adelante",
            "metodo": metodos.Newton_hacia_adelante, "interfaz": Interfaz_del_Metodo},
        {"nombre": "Newton hacia atras", "metodo": metodos.Newton_hacia_atras,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Lagrange", "metodo": metodos.Lagrange,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Newton con diferencias Divididas",
            "metodo": metodos.Interpolacion_lineal, "interfaz": Interfaz_del_Metodo},
    ]

    def combine_funcs(*funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return combined_func
    for y in range(5):
        button = tk.Button(vprincipal, text=f"#{y+1}: {infoMetodos1[y]['nombre']}",
                           command=lambda metodo=infoMetodos1[y]["metodo"]: infoMetodos1[y]["interfaz"](metodo) or vprincipal.destroy())
        button.place(x=10, y=(120+25*y))

    infoMetodos2 = [
        {"nombre": "Metodo de la bisectriz",
         "metodo": metodos.Interpolacion_lineal, "interfaz": Interfaz_del_Metodo},
        {"nombre": "Punto fijo", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Newton - Rhapson", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Falsa posicion", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Secante", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
    ]

    def combine_funcs(*funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return combined_func
    for r in range(5):
        button = tk.Button(vprincipal, text=f"#{r+1}: {infoMetodos2[r]['nombre']}",
                           command=lambda metodo=infoMetodos2[r]["metodo"]: infoMetodos2[r]["interfaz"](metodo) or vprincipal.destroy())
        button.place(x=300, y=(120+25*r))

    infoMetodos3 = [
        {"nombre": "Montante", "metodo": metodos.Interpolacion_lineal,
         "interfaz": Interfaz_del_Metodo},
        {"nombre": "Gauss-Jordan", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Eliminacion Gaussiana", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Gauss Seidel", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Jacobi", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Raices con Polinomios", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
    ]

    def combine_funcs(*funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return combined_func
    for p in range(5):
        button = tk.Button(vprincipal, text=f"#{p+1}: {infoMetodos3[p]['nombre']}",
                           command=lambda metodo=infoMetodos3[p]["metodo"]: infoMetodos3[p]["interfaz"](metodo) or vprincipal.destroy())
        button.place(x=600, y=(120+25*p))

    infoMetodos4 = [
        {"nombre": "Linea recta", "metodo": metodos.Interpolacion_lineal,
         "interfaz": Interfaz_del_Metodo},
        {"nombre": "Cuadratica",
            "metodo": metodos.Interpolacion_lineal, "interfaz": Interfaz_del_Metodo},
        {"nombre": "Cubica", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Lineal con funcion", "metodo": metodos.Interpolacion_lineal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Cuadratica con funcion",
            "metodo": metodos.Interpolacion_lineal, "interfaz": Interfaz_del_Metodo},
    ]

    def combine_funcs(*funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return combined_func
    for x in range(5):
        button = tk.Button(vprincipal, text=f"#{x+1}: {infoMetodos4[x]['nombre']}",
                           command=lambda metodo=infoMetodos4[x]["metodo"]: infoMetodos4[x]["interfaz"](metodo) or vprincipal.destroy())
        button.place(x=10, y=(345+25*x))

    infoMetodos5 = [
        {"nombre": "Regla trapezoidal", "metodo": metodos.Integracion_trapezoidal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Regla 1/3 de Simpson", "metodo": metodos.Integracion_simpson13,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Regla 3/8 de Simpson", "metodo": metodos.Integracion_simpson38,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Newton cotes cerradas",
            "metodo": metodos.Integracion_cotasCerrada, "interfaz": Interfaz_del_Metodo},
        {"nombre": "Newton cotes abiertas",
            "metodo": metodos.Integracion_cotasAbiertas, "interfaz": Interfaz_del_Metodo},
    ]

    def combine_funcs(*funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return combined_func
    for i in range(5):
        button = tk.Button(vprincipal, text=f"#{i+1}: {infoMetodos5[i]['nombre']}",
                           command=lambda metodo=infoMetodos5[i]["metodo"]: infoMetodos5[i]["interfaz"](metodo) or vprincipal.destroy())
        button.place(x=300, y=(345+25*i))

    infoMetodos6 = [
        {"nombre": "Euler hacia adelante", "metodo": metodos.Integracion_trapezoidal,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Euler hacia atras", "metodo": metodos.Integracion_simpson13,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Euler Modificado", "metodo": metodos.Integracion_simpson38,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Runge Kutta 2do Orden",
            "metodo": metodos.Integracion_cotasCerrada, "interfaz": Interfaz_del_Metodo},
        {"nombre": "Runge Kutta 3er Orden",
            "metodo": metodos.Integracion_cotasAbiertas, "interfaz": Interfaz_del_Metodo},
        {"nombre": "Runge Kutta 4to Orden: 1/3 Simpson", "metodo": metodos.Integracion_simpson38,
            "interfaz": Interfaz_del_Metodo},
        {"nombre": "Runge Kutta 4to Orden: 3/8 Simpson",
            "metodo": metodos.Integracion_cotasCerrada, "interfaz": Interfaz_del_Metodo},
        {"nombre": "Runge Kutta Orden superior",
            "metodo": metodos.Integracion_cotasAbiertas, "interfaz": Interfaz_del_Metodo},
    ]

    def combine_funcs(*funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return combined_func
    for n in range(8):
        button = tk.Button(vprincipal, text=f"#{n+1}: {infoMetodos6[n]['nombre']}",
                           command=lambda metodo=infoMetodos6[n]["metodo"]: infoMetodos6[n]["interfaz"](metodo) or vprincipal.destroy())
        button.place(x=600, y=(345+25*n))


# Aqui es llamada la funcion principal por primera vez
ventana1 = principal()
main_window.mainloop()
