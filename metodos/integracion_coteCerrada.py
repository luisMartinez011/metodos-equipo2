import numpy as np


class Integracion_cotasCerrada:

    def __init__(self):
        self.a = -2
        self.b = 2
        self.n = 4
        self.ah = (2/45)
        self.h = ((self.b - self.a)/(self.n))

        self.x = 4
    # returns a formula´s string
    @staticmethod
    def formula():
        return "/Cotescerradas2.png"

    @staticmethod
    def methodName():
        return "Integracion_cotasCerrada"

    # solves the problem
    def solve(self):
        ValorI = (self.h)* (self.ah)
        f_a = (7 *( (3*(self.a)**3)-10))
        f_b = (7 *( (3*(self.b)**3)-10))

        f_h1 = (32 *((3*  ( self.a + (self.h*1))**3) -10))
        f_h2 = (12 *((3*  ( self.a + (self.h*2))**3) -10))
        f_h3 = (32 *((3*  ( self.a + (self.h*3))**3) -10))
     

        f_suma = (f_h1 + f_h2 + f_h3 )

        g_x = ValorI * (f_a + f_b + f_suma)

        self.g_x = g_x

        return g_x

    # return error margin
    def error(self):
        f_x = np.log(self.x)
        error = abs(f_x - self.g_x)

        return error
