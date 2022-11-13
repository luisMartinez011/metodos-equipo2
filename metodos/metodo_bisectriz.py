import pandas as pd
import numpy as np
import functools
import sympy as sp
from math import *


class Bisectriz:
    tol = 10**(-3)

    @staticmethod
    def formula():
        return "Bisectriz.png"

    @staticmethod
    def methodName():
        return "Metodo Bisectriz"

    def solve(self):
        x = sp.symbols('x')  # Crea la variable para la formula
        f = input('Digite la funcion con variable x:')
        f = sp.lambdify(x, f)
        a = int(input('Intervalo A: '))
        b = int(input('Intervalo B:'))
        m1 = a
        m = b
        k = 0
        iA = []
        iB = []
        iE = []
        if (f(a)*f(b) > 0):
            print('La funcion no cambia de signo')

        while (abs(m1-m) > tol):
            m1 = m
            m = (a+b)/2
            if (f(a)*f(m) < 0):  # Cambia de signo en el intervalo [a,m]
                b = m
            if (f(m)*f(b) < 0):  # Cambia de signo en el intervalo [m,b]
                a = m

            iA.append[a]
        iB.append[b]
        ext = abs(m1-m)
        iE.append[(ext)]

        self.coords = pd.DataFrame(list(zip(iA, iB, iE)),
                                   columns=["Indice A", "Indice B", "Margen Error"])
        return

    def error(self):
        er = self.m
        return er
