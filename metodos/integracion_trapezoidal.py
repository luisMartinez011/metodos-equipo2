import numpy as np
from metodos.metodos_padre import Metodo_Padre


class Integracion_trapezoidal(Metodo_Padre):

    def __init__(self):
        self.a = 2
        self.b = 3
        self.n = 4
        self.h = ((self.b - self.a)/self.n)

        self.x = 4
        self.problemImage = "Trapezoidal2.png"

    # returns a formula´s string
    @staticmethod
    def formula():
        return "Trapezoidal.png"

    @staticmethod
    def methodName():
        return "Integracion trapezoidal"

    # solves the problem
    def solve(self):

        ValorI = (self.h)/2
        f_a = (1/(1+(self.a)**2))
        f_b = (1/(1+(self.b)**2))

        f_h1 = (1 / (1+(self.a + (self.h*1))**2))
        f_h2 = (1 / (1+(self.a + (self.h*2))**2))
        f_h3 = (1 / (1+(self.a + (self.h*3))**2))
        f_suma = 2*(f_h1 + f_h2 + f_h3)

        g_x = ValorI * (f_a + f_b + f_suma)

        self.g_x = g_x

        return g_x
