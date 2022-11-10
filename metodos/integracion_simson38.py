import numpy as np


class Integracion_simpson38:

    def __init__(self):
        self.a = 0
        self.b = 1
        self.n = 3
        self.h = ((self.b - self.a)/self.n)

    # returns a formula´s string
    @staticmethod
    def formula():
        return "/3octavos_simpson.png"

    @staticmethod
    def methodName():
        return "Integracion_simpson 3/8"

    # solves the problem
    def solve(self):
        ValorI = np((self.h)*(3/8))
        f_a = np(1-(self.a)^2)
        f_sumatoria = np(3*((1-((self.h)*1)^2) +  (1-((self.h)*2)^2) + (1-((self.h)*3)^2) ))
        f_b = np(1-(self.b)^2)
        
        g_x = ValorI * (f_a + f_b + f_sumatoria)
        self.g_x = g_x
        return g_x

    # return error margin
    def error(self):
        f_x = np.log(self.x)
        error = abs(f_x - self.g_x)

        return error
