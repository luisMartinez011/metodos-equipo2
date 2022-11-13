import pandas as pd
import numpy as np
import functools
import sympy as sp
from math import *


class Newton_Raphson:
    tol = 10**(-5)

    @staticmethod
    def formula():
        return "Raphson.png"

    @staticmethod
    def methodName():
        return "Newton Raphson"

    def solve(self):
        x = sp.symbols('x')  # Crea la variable para la formula
        f = input('Digite la funcion con variable x:')
        df = sp.diff(f)  # derivada de la funcion
        f = sp.lambdify(x, f)  # Crea la funcion respecto a x
        df = sp.lambdify(x, df)
        x0 = int(input('Valor inicial de  X: '))
        x1 = 0
        lx1 = []
        lxE = []
        n = int(input('Numero de interacciones aproximadas: '))
        for k in range(n):
            x1 = x0-f(x0)/df(x0)
            if (abs(x1-x0) < tol):
                aux = abs(x1-x0)
                lx1.append[format(x1, '0.9f')]
                lxE.append[format(aux, '0.9f')]
                self.coords = pd.DataFrame(list(zip(lx1, ixE)),
                                           columns=["X(i+1)", "Margen Error"])
                return
            x0 = x1
            aux = abs(x1-x0)
            lx1.append[format(x1, '0.9f')]
            lxE.append[format(aux, '0.9f')]

    def error(self):
        ext = abs(x1-x0)
        return format(abs(x1-x0), '0.9f')
