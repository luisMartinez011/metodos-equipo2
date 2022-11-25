import numpy as np
import sympy as sp
from random import randint
from metodos.metodos_padre import Metodo_Padre
from math import *


class Euler_Atras(Metodo_Padre):

    def __init__(self):
        self.problemImage = "EulerModificado_1.png"

    @staticmethod
    def formula():
        return "Euler_Atras.png"

    @staticmethod
    def methodName():
        return "Euler hacia atras"

    def f(self, t, y):
        func = t*exp(3*t)-2*y
        return func

    def solve(self):
        t = 0
        y = 1.2
        h = 0.3
        n = 2
        print('y(', t, ')=', y)
        for k in range(n):
            y0 = y+h*self.f(t, y)
            y = y+(h/2)*(self.f(t, y)+self.f(t+h, y0))
            t = t+h
            print('y(', t, ')=', y)
        return y
#print("De acuerdo al método euler atras: ", s)
