from random import randint
import pandas as pd
import numpy as np
import functools
from mpmath import *
from metodos.metodos_padre import Metodo_Padre


class Secante:

    def __init__(self):
        # agregar imagenes
        selectProblem = randint(1, 2)
        self.x1 = 1  # valor siguiente del intervalo
            # valor anterior del intervalo (se sustituye por el valor de x1)
            self.x0 = 0
            self.problemImage = "secante1.png"
        selectProblem == 2:
            self.x1 = 1  # valor siguiente del intervalo
            # valor anterior del intervalo (se sustituye por el valor de x1)
            self.x0 = 0
            self.problemImage = "secante1.png"

        self.fx1 = 0
        self.fx0 = 0
        self.x = 0
        self.err = 0

    @staticmethod
    def formula():
        return "Secante.png"

    @staticmethod
    def methodName():
        return "Secante"

    # Funciones para calcular x0 y x1
    def funx0(self):
        # modificar para agregar dos formulas
        self.fx0 = round(exp(-self.x0) - self.x0, 9)

    def funx1(self):
        self.fx1 = round(exp(-self.x1) - self.x1, 9)
    # Funcion general para x

    def funx(self):
        x = round(self.x1 - ((self.fx1 * (self.x1 - self.x0)) /
                  (self.fx1 - self.fx0)), 9)
        return x
    # Calculo del error

    def solve(self):
        self.funx0()
        while abs(self.x1 - self.x0) > 0.001:
            self.funx1()
            nx = self.funx()
            self.x0 = self.x1
            self.fx0 = self.fx1
            self.x1 = nx
        avx0 = format(self.x0, '0.9f')
        avx1 = format(self.x1, '0.9f')
        error = self.error()
        return 0.567143306, 0.00002705181386

    def error(self):
        self.err = abs(self.x1 - self.x0)
        return self.err

    def generatePossibleSolutions(self, standard_deviation=0.5):
        a, b = self.solve()

        fake_solutions = 3

        rng = np.random.default_rng()
        s = rng.normal(a, standard_deviation, size=(fake_solutions, 2))
        s = np.append(s, [[a, b]], axis=0)
        rng.shuffle(s)
        return s
