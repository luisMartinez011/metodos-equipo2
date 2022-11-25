import numpy as np
import sympy as sp
from random import randint
from metodos.metodos_padre import Metodo_Padre
from math import *


class Euler_Adelante(Metodo_Padre):

    def __init__(self):
        self.t = 0
        self.y = 2
        self.h = 0.2
        self.n = 2
        self.y0 = 2
        self.problemImage = "Euler_Adelante_1.png"

    @staticmethod
    def formula():
        return "Euler_Adelante.png"

    @staticmethod
    def methodName():
        return "Euler hacia adelante"

    def f(self, t, y):
        func = t*exp(3*t)-2*y
        return func

    def solve(self):
        def f( t, y):
            func = ((5*y*t)-1) /3
            return func

        t = self.t
        y = self.y
        h = self.h
        n = self.n
        y0 = self.y0

        result = np.array([])

        for k in range(n):
                    if(k==0):
                        y0 = y
                    else:
                        y0 = y+h*f(t, y)
                    #y = y+(h)*(f(t, y)+f(t+h, y0))
                    y = y+(h)*(f(t, y))
                    t = t+h
                    result = np.append(result,y)
        y
        a , b = result
        a = np.round(a,9)
        b = np.round(b,9)
        return a,b

    def generatePossibleSolutions(self, standard_deviation=0.5):
        a, b = self.solve()

        fake_solutions = 3

        rng = np.random.default_rng()
        s = rng.normal(a, standard_deviation, size=(fake_solutions, 2))
        s = np.append(s, [[a, b]], axis=0)
        rng.shuffle(s)
        return s
#print("De acuerdo al metodo euler hacia adelante: ", s1)
