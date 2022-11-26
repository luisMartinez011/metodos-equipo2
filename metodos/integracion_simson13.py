import numpy as np
from metodos.metodos_padre import Metodo_Padre


class Integracion_simpson13(Metodo_Padre):

    def __init__(self):
        self.a = 2
        self.b = 3
        self.n = 10
        self.h = ((self.b - self.a)/self.n)

        self.x = 4
        self.problemImage = "1tercio_simpson2.png"

    def generatePossibleSolutions(self, standard_deviation=0.5):
        solution,a = self.solve()

        fake_solutions = 3

        rng = np.random.default_rng()
        s = rng.normal(solution, standard_deviation, size=(fake_solutions,2))
        s = np.append(s,[[solution , a]], axis=0)
        rng.shuffle(s)
        return s

    # returns a formula´s string
    @staticmethod
    def formula():
        return "1tercio_simpson.png"

    @staticmethod
    def methodName():
        return "Integración_simpson13"

    # solves the problem
    def solve(self):

        ValorI = (self.h)/3
        f_a = (1/(1+(self.a)**2))
        f_b = (1/(1+(self.b)**2))

        f_h1 = 4 * (1 / (1+(self.a + (self.h*1))**2))
        f_h2 = 2 * (1 / (1+(self.a + (self.h*2))**2))
        f_h3 = 4 * (1 / (1+(self.a + (self.h*3))**2))
        f_h4 = 2 * (1 / (1+(self.a + (self.h*4))**2))
        f_h5 = 4 * (1 / (1+(self.a + (self.h*5))**2))
        f_h6 = 2 * (1 / (1+(self.a + (self.h*6))**2))
        f_h7 = 4 * (1 / (1+(self.a + (self.h*7))**2))
        f_h8 = 2 * (1 / (1+(self.a + (self.h*8))**2))
        f_h9 = 4 * (1 / (1+(self.a + (self.h*9))**2))

        f_suma = (f_h1 + f_h2 + f_h3 + f_h4 + f_h5 + f_h6 + f_h7 + f_h8 + f_h9)

        g_x = ValorI * (f_a + f_b + f_suma)

        self.g_x = g_x

        return g_x,f_suma
