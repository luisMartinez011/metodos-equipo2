import pandas as pd
import numpy as np
import functools
from math import *


class Punto_Fijo:
    
    
    def __init__(self):
        self.tol = 10**(-5)
        self.a = 0
        self.x = 0 

    @staticmethod
    def formula():
        return "Ayuda_PuntoFijo.png"

    @staticmethod
    def methodName():
        return "Punto Fijo"

    def func(self):
        return exp(-self.x)

    def solve(self):
        aux = 0
        m = self.func(self.a)
        k = 0
        iA = []
        iB = []
        iE = []
        while (abs(a-m) > self.tol):
            a = m
            aux = m
            m = self.func(self.a)

            k = k+1
            iA.append[aux]
            iB.append[m]
            iE.append[(a-m)]
        self.coords = pd.DataFrame(list(zip(iA, iB, iE)),
                                   columns=["Indice A", "Indice B", "Margen Error"])

    def error(self):
        e = self.a - self.m
        return abs(e)
