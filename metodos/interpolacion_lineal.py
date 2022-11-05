import numpy as np


class Interpolacion_lineal:

    def __init__(self):
        self.a = 2
        self.b = 5
        self.x = 4

    # returns a formula´s string
    @staticmethod
    def formula():
        return "( ( f(b) - f(a) ) / (b - a) ) * (x - a) + f(a) "

    # solves the problem
    def solve(self):
        f_a = np.log(self.a)
        f_b = np.log(self.b)
        g_x = (((f_b - f_a) / (self.b-self.a)) * (self.x-self.a)) + f_a
        self.g_x = g_x

        return g_x

    # return error margin
    def error(self):
        f_x = np.log(self.x)
        error = abs(f_x - self.g_x)

        return error
