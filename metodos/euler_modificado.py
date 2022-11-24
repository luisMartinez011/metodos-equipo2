import numpy as np
import sympy as sp
import functools
from random import randint
from math import *
from metodos.metodos_padre import Metodo_Padre

# eee


class Euler_Modificado(Metodo_Padre):

    def __init__(self):
        self.problemImage = "EulerModificado_1.png"

    @staticmethod
    def formula():
        return "Euler_Modificado.png"

    @staticmethod
    def methodName():
        return "EulerModificado"

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
