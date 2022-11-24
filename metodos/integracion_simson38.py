import numpy as np
from metodos.metodos_padre import Metodo_Padre


class Integracion_simpson38(Metodo_Padre):

    def __init__(self):
        self.a = 0
        self.b = 1
        self.e = 2.71828182845
        self.n = 3

        self.h = (self.b - self.a)/self.n

        self.x = 4
        self.problemImage = "3octavos_simpson2.png"

    # returns a formula´s string

    @staticmethod
    def formula():
        return "3octavos_simpson.png"

    @staticmethod
    def methodName():
        return "Integracion_simpson 3/8"

    # solves the problem
    def solve(self):
        ValorI = (self.h)*(3/8)
        f_a = ((self.a)**3)*(self.e**(self.a))
        f_b = ((self.b)**3)*(self.e**(self.b))

        f_h1 = ((self.h*1)**3) * (self.e**(self.h*1))
        f_h2 = ((self.h*2)**3) * (self.e**(self.h*2))

        f_suma = 3 * (f_h1 + f_h2)

        g_x = ValorI * (f_a + f_b + f_suma)

        self.g_x = g_x

        return g_x
