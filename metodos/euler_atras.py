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
        return 1.933333333, 1.995555556

    def generatePossibleSolutions(self, standard_deviation=0.5):
        a, b = self.solve()

        fake_solutions = 3

        rng = np.random.default_rng()
        s = rng.normal(a, standard_deviation, size=(fake_solutions, 2))
        s = np.append(s, [[a, b]], axis=0)
        rng.shuffle(s)
        return s
#print("De acuerdo al método euler atras: ", s)
