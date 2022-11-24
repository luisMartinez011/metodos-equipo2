import numpy as np


class Integracion_simpson38:

    def __init__(self):
        self.a = 0
        self.b = 1
        self.e = 2.71828182845
        self.n = 3

        self.h = (self.b - self.a)/self.n
        
        self.x = 4

    # returns a formula´s string
    @staticmethod
    def formula():
        return "/3octavos_simpson.png"

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
        
        f_suma = 3* (f_h1 + f_h2)

        g_x = ValorI * (f_a + f_b + f_suma)

        self.g_x = g_x

        return g_x
    

    

    # return error margin
    def error(self):
        f_x = np.log(self.x)
        error = abs(f_x - self.g_x)

        return error
